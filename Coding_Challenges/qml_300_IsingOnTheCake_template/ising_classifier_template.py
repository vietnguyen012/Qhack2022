import sys
import numpy as np
import pennylane as qml
from pennylane import numpy as np
import pennylane.optimize as optimize

DATA_SIZE = 250


def square_loss(labels, predictions):
    """Computes the standard square loss between model predictions and true labels.

    Args:
        - labels (list(int)): True labels (1/-1 for the ordered/disordered phases)
        - predictions (list(int)): Model predictions (1/-1 for the ordered/disordered phases)

    Returns:
        - loss (float): the square loss
    """

    loss = 0
    for l, p in zip(labels, predictions):
        loss = loss + (l - p) ** 2

    loss = loss / len(labels)
    return loss


def accuracy(labels, predictions):
    """Computes the accuracy of the model's predictions against the true labels.

    Args:
        - labels (list(int)): True labels (1/-1 for the ordered/disordered phases)
        - predictions (list(int)): Model predictions (1/-1 for the ordered/disordered phases)

    Returns:
        - acc (float): The accuracy.
    """

    acc = 0
    for l, p in zip(labels, predictions):
        if abs(l - p) < 1e-5:
            acc = acc + 1
    acc = acc / len(labels)

    return acc


def classify_ising_data(ising_configs, labels):
    """Learn the phases of the classical Ising model.

    Args:
        - ising_configs (np.ndarray): 250 rows of binary (0 and 1) Ising model configurations
        - labels (np.ndarray): 250 rows of labels (1 or -1)

    Returns:
        - predictions (list(int)): Your final model predictions

    Feel free to add any other functions than `cost` and `circuit` within the "# QHACK #" markers 
    that you might need.
    """

    # QHACK #

    num_wires = ising_configs.shape[1] 
    dev = qml.device("default.qubit", wires=num_wires)

    def get_angles(x):

        beta0 = 2 * np.arcsin(np.sqrt(x[1] ** 2) / np.sqrt(x[3] ** 2 + x[1] ** 2 + 1e-12))
        beta1 = 2 * np.arcsin(np.sqrt(x[2] ** 2) / np.sqrt(x[2] ** 2 + x[0] ** 2 + 1e-12))
        beta2 = 2 * np.arcsin(
            np.sqrt(x[2] ** 2 + x[3] ** 2)
            / (np.sqrt(x[0] ** 2 + x[1] ** 2 + x[2] ** 2 + x[3] ** 2) + 1e-12)
        )
        beta3 = 2 * np.arcsin(np.sqrt(x[3] ** 2) / np.sqrt(x[3] ** 2 + x[2] ** 2 + 1e-12))
        beta4 = 2 * np.arcsin(np.sqrt(x[0] ** 2) / np.sqrt(x[1] ** 2 + x[0] ** 2 + 1e-12))

        # return np.array([beta2, -beta1 / 2, beta1 / 2, -beta0 / 2, beta0 / 2])
        # return np.array([beta2, beta1, beta0, beta3, beta4])
        return np.array([beta1, beta0, beta3, beta4, beta2])

    def statepreparation(a):
        # qml.BasisState(a, wires=[0, 1, 2, 3])

        qml.RY(a[0], wires=0)
        qml.CNOT(wires=[0, 1])

        qml.RY(a[1], wires=1)
        qml.CNOT(wires=[1, 2])

        qml.RY(a[2], wires=2)
        qml.PauliX(wires=0)
        qml.CNOT(wires=[2, 3])

        qml.RY(a[3], wires=3)
        qml.CNOT(wires=[3, 0])
        qml.RY(a[4], wires=0)
        qml.PauliX(wires=0)

        qml.CNOT(wires=[3, 1])
        qml.RY(a[1], wires=1)
        qml.CNOT(wires=[1, 3])
        qml.RY(a[3], wires=3)

    def layer(W):

        qml.Rot(W[0, 0], W[0, 1], W[0, 2], wires=0)
        qml.Rot(W[1, 0], W[1, 1], W[1, 2], wires=1)
        qml.Rot(W[2, 0], W[2, 1], W[2, 2], wires=2)
        qml.Rot(W[3, 0], W[3, 1], W[3, 2], wires=3)

        qml.CNOT(wires=[0, 1])
        qml.CNOT(wires=[1, 2])
        qml.CNOT(wires=[2, 3])
        qml.CNOT(wires=[3, 0])


    # Define a variational circuit below with your needed arguments and return something meaningful
    @qml.qnode(dev)
    def circuit(weights, angles):
        statepreparation(angles)
        for W in weights:
            layer(W)
        return qml.expval(qml.PauliZ(0))

    def variational_classifier(weights, bias, angles):
        return circuit(weights, angles) + bias


    # Define a cost function below with your needed arguments
    def cost(weights, bias, features, Y):

        # QHACK #

        # Insert an expression for your model predictions here
        predictions = [variational_classifier(weights, bias, f) for f in features]

        # QHACK #

        return square_loss(Y, predictions) # DO NOT MODIFY this line

    # optimize your circuit here
    normalization = np.sqrt(np.sum(ising_configs ** 2, -1)) + 1e-12
    ising_configs_norm = (ising_configs.T / normalization).T

    features = np.array([get_angles(x) for x in ising_configs_norm], requires_grad=False)

    num_qubits = 4
    num_layers = 2

    weights_init = 0.01 * np.random.randn(num_layers, num_qubits, 3, requires_grad=True)
    bias_init = np.array(0.0, requires_grad=True)

    opt = optimize.NesterovMomentumOptimizer(0.1)
    batch_size = 64

    weights = weights_init
    bias = bias_init

    import time

    t0 = time.time()
    for it in range(100):
        # Update the weights by one optimizer step
        batch_index = np.random.randint(0, DATA_SIZE, (batch_size,))
        feats_train_batch = features[batch_index]
        Y_train_batch = labels[batch_index]

        # print(feats_train_batch, Y_train_batch)
        weights, bias, _, _ = opt.step(cost, weights, bias, feats_train_batch, Y_train_batch)

        # Compute predictions on train and validation set
        predictions_train = [np.sign(variational_classifier(weights, bias, f)) for f in feats_train_batch]

        # Compute accuracy on train and validation set
        acc_train = accuracy(Y_train_batch, predictions_train)

        # print(
        #     "Iter: {:5d} | Cost: {:0.7f} | Acc train: {:0.7f} | Acc total: {:0.7f} "
        #     "".format(it + 1, cost(weights, bias, features, labels), acc_train, acc_total)
        # )

        if it % 5 == 0:
            prediction_total = [np.sign(variational_classifier(weights, bias, f)) for f in features]
            acc_total = accuracy(labels, prediction_total)
            if acc_total >= 0.9:
                predictions = [int(item) for item in prediction_total]
                t1 = time.time()
                # print(f'Training time: {t1-t0} seconds')
                break

    # QHACK #

    return predictions


if __name__ == "__main__":
    inputs = np.array(
        sys.stdin.read().split(","), dtype=int, requires_grad=False
    ).reshape(DATA_SIZE, -1)
    ising_configs = inputs[:, :-1]
    labels = inputs[:, -1]
    predictions = classify_ising_data(ising_configs, labels)
    print(*predictions, sep=",")
