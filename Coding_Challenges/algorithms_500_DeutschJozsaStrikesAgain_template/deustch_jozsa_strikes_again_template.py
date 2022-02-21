#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml


def deutsch_jozsa(fs):
    """Function that determines whether four given functions are all of the same type or not.

    Args:
        - fs (list(function)): A list of 4 quantum functions. Each of them will accept a 'wires' parameter.
        The first two wires refer to the input and the third to the output of the function.

    Returns:
        - (str) : "4 same" or "2 and 2"
    """

    # QHACK #
    dev = qml.device("default.qubit", wires=7)
    @qml.qnode(dev)
    def circuit():
        mywires = [0,1,2,3,4,5,6]
        qml.PauliX(wires=2)
        qml.Hadamard(wires=[0])
        qml.Hadamard(wires=[1])
        qml.Hadamard(wires=[2])
        fs[0](mywires)
        qml.Hadamard(wires=[0])
        qml.Hadamard(wires=[1])
        qml.Toffoli(wires=[0,1,3])
        qml.Hadamard(wires=[0])
        qml.Hadamard(wires=[1])
        fs[1](mywires)
        qml.Hadamard(wires=[0])
        qml.Hadamard(wires=[1])
        qml.Toffoli(wires=[0,1,4])
        qml.Hadamard(wires=[0])
        qml.Hadamard(wires=[1])
        fs[2](mywires)
        qml.Hadamard(wires=[0])
        qml.Hadamard(wires=[1])
        qml.Toffoli(wires=[0,1,5])
        qml.Hadamard(wires=[0])
        qml.Hadamard(wires=[1])
        fs[3](mywires)
        qml.Hadamard(wires=[0])
        qml.Hadamard(wires=[1])
        qml.Toffoli(wires=[0,1,6])
        return [qml.probs(wires=i) for i in range(7)]
    # QHACK #
    msmt = circuit()
    if msmt[3][1] < 0.5 and msmt[4][1] < 0.5 and msmt[5][1] < 0.5:
        return '4 same'
    elif msmt[3][1] > 0.5 and msmt[4][1] < 0.5 and msmt[5][1] > 0.5:
        return '4 same'
    else:
        return '2 and 2'


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    numbers = [int(i) for i in inputs]

    # Definition of the four oracles we will work with.

    def f1(wires):
        qml.CNOT(wires=[wires[numbers[0]], wires[2]])
        qml.CNOT(wires=[wires[numbers[1]], wires[2]])

    def f2(wires):
        qml.CNOT(wires=[wires[numbers[2]], wires[2]])
        qml.CNOT(wires=[wires[numbers[3]], wires[2]])

    def f3(wires):
        qml.CNOT(wires=[wires[numbers[4]], wires[2]])
        qml.CNOT(wires=[wires[numbers[5]], wires[2]])
        qml.PauliX(wires=wires[2])

    def f4(wires):
        qml.CNOT(wires=[wires[numbers[6]], wires[2]])
        qml.CNOT(wires=[wires[numbers[7]], wires[2]])
        qml.PauliX(wires=wires[2])

    output = deutsch_jozsa([f1, f2, f3, f4])
    print(f"{output}")
