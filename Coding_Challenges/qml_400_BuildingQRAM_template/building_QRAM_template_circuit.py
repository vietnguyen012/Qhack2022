#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml


def qRAM(thetas):
    """Function that generates the superposition state explained above given the thetas angles.

    Args:
        - thetas (list(float)): list of angles to apply in the rotations.

    Returns:
        - (list(complex)): final state.
    """

    # QHACK #

    # Use this space to create auxiliary functions if you need it.

    # QHACK #

    dev = qml.device("default.qubit", wires=range(4))
    thetas_ = thetas

    @qml.qnode(dev)
    def circuit():

        # QHACK #

        # Create your circuit: the first three qubits will refer to the index, the fourth to the RY rotation.
        #----------------
        # Superposition
        qml.U2(0, np.pi, wires=0)
        qml.U2(0, np.pi, wires=1)
        qml.U2(0, np.pi, wires=2)
        qml.PhaseShift(0, wires=3)
        qml.Barrier(only_visual=True)

        #===============================
        # Input = (q2, q1, q0) = (0,0,0)
        #===============================
        theta = float(thetas_[0])/8
        #----------------
        qml.U3(np.pi, 0, np.pi, wires=0)
        qml.U3(np.pi, 0, np.pi, wires=1)
        qml.U3(np.pi, 0, np.pi, wires=2)
        qml.PhaseShift(0, wires=2)
        # qml.PhaseShift(0, wires=2)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[2, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 1])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #----------------
        qml.PhaseShift(0, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=1)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[1, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 1])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #----------------
        qml.PhaseShift(0, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=1)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[1, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 0])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 0])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 0])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.U3(np.pi, 0, np.pi, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 0])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.U3(np.pi, 0, np.pi, wires=2)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.U3(np.pi, 0, np.pi, wires=0)
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #===============================
        # Input = (q2, q1, q0) = (1,0,1)
        #===============================
        theta = float(thetas_[5])/8
        #----------------
        qml.U3(np.pi, 0, np.pi, wires=1)
        qml.PhaseShift(0, wires=2)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=2)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[2, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 1])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #----------------
        qml.PhaseShift(0, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=1)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[1, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 1])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #----------------
        qml.PhaseShift(0, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=1)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[1, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 0])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 0])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 0])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.U3(np.pi, 0, np.pi, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 0])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #===============================
        # Input = (q2, q1, q0) = (0,1,0)
        #===============================
        theta = float(thetas_[2])/8
        #----------------
        qml.U3(np.pi, 0, np.pi, wires=0)
        qml.U3(np.pi, 0, np.pi, wires=2)
        qml.PhaseShift(0, wires=3)
        qml.PhaseShift(0, wires=2)
        # qml.PhaseShift(0, wires=2)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[2, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 1])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #----------------
        qml.PhaseShift(0, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=1)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[1, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 1])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #----------------
        qml.PhaseShift(0, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=1)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[1, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 0])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 0])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 0])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 0])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.U3(np.pi, 0, np.pi, wires=2)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.U3(np.pi, 0, np.pi, wires=0)
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)


        #===============================
        # Input = (q2, q1, q0) = (1,1,0)
        #===============================
        theta = float(thetas_[6])/8
        #----------------
        qml.U3(np.pi, 0, np.pi, wires=0)
        qml.PhaseShift(0, wires=2)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=2)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[2, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 1])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #----------------
        qml.PhaseShift(0, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=1)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[1, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 1])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #----------------
        qml.PhaseShift(0, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=1)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[1, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 0])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 0])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 0])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 0])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.U3(np.pi, 0, np.pi, wires=0)
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)


        #===============================
        # Input = (q2, q1, q0) = (0,0,1)
        #===============================
        theta = float(thetas_[1])/8
        #----------------
        qml.U3(np.pi, 0, np.pi, wires=1)
        qml.U3(np.pi, 0, np.pi, wires=2)
        qml.PhaseShift(0, wires=3)
        qml.PhaseShift(0, wires=2)
        # qml.PhaseShift(0, wires=2)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[2, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 1])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #----------------
        qml.PhaseShift(0, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=1)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[1, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 1])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #----------------
        qml.PhaseShift(0, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=1)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[1, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 0])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 0])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 0])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.U3(np.pi, 0, np.pi, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 0])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.U3(np.pi, 0, np.pi, wires=2)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)



        #===============================
        # Input = (q2, q1, q0) = (1,0,0)
        #===============================
        theta = float(thetas_[4])/8
        #----------------
        qml.U3(np.pi, 0, np.pi, wires=0)
        qml.U3(np.pi, 0, np.pi, wires=1)
        qml.PhaseShift(0, wires=2)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=2)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[2, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 1])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #----------------
        qml.PhaseShift(0, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=1)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[1, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 1])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #----------------
        qml.PhaseShift(0, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=1)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[1, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 0])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 0])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 0])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.U3(np.pi, 0, np.pi, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 0])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.U3(np.pi, 0, np.pi, wires=0)
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #===============================
        # Input = (q2, q1, q0) = (0,1,1)
        #===============================
        theta = float(thetas_[3])/8
        #----------------
        qml.U3(np.pi, 0, np.pi, wires=2)
        qml.PhaseShift(0, wires=3)
        qml.PhaseShift(0, wires=2)
        # qml.PhaseShift(0, wires=2)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[2, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 1])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #----------------
        qml.PhaseShift(0, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=1)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[1, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 1])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #----------------
        qml.PhaseShift(0, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=1)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[1, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 0])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 0])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 0])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 0])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.U3(np.pi, 0, np.pi, wires=2)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)


        #===============================
        # Input = (q2, q1, q0) = (1,1,1)
        #===============================
        theta = float(thetas_[7])/8
        #----------------
        qml.PhaseShift(0, wires=2)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=2)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[2, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 1])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #----------------
        qml.PhaseShift(0, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=1)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[1, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 1])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        #----------------
        qml.PhaseShift(0, wires=1)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=1)
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[1, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 0])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 0])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[1, 0])
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.CNOT(wires=[2, 0])
        qml.U3(-theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        qml.PhaseShift(0, wires=0)
        qml.PhaseShift(0, wires=3)
        # qml.PhaseShift(0, wires=0)
        qml.Barrier(only_visual=True)

        qml.CNOT(wires=[0, 3])
        qml.U3(-theta, 0, 0, wires=3)
        qml.CNOT(wires=[0, 3])
        qml.Barrier(only_visual=True)

        #----------------
        qml.U3(theta, 0, 0, wires=3)
        qml.Barrier(only_visual=True)

        # QHACK #

        return qml.state()

    return circuit()


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    thetas = np.array(inputs, dtype=float)

    output = qRAM(thetas)
    output = [float(i.real.round(6)) for i in output]
    print(*output, sep=",")