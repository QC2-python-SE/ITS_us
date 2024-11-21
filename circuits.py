# this is a placeholder
"""
States script:
==============

- Provides built-in initial states for 1 and 2 qubits.
- Normalises given initial states for N qubits.

Dependencies:
~~~~~~~~~~~~~
- numpy
- math

"""


import numpy as np
from states import states
from gates import Gate


class Circuits:

    def __init__(self, N_wires=1, state_init=states().Zero()):

        self.N_wires = N_wires
        self.state = state_init
        self.gates = []

        # check that the initial state has the correct dimension for the number of wires
        if np.log2(len(state_init)) != N_wires:
            raise ValueError("The initial state must be a power of 2.")

    def get_gates(self):
        """
        Returns the current list of gates in the circuit
        """
        return self.gates

    def get_state(self):
        """
        Returns the current quantum state of the circuit
        """
        return self.state

    def add_single_qubit_gate(self, gate: Gate, target_wire: int = 0):
        """
        Function to add a single wubit gate to the circuit at a given wire.
        Creates a tuple of the gate and the target wire and appends it to the gates list.

        Args:
            gate (Gates): The gate to be added to the circuit.
            target_wire (int): The wire the gate is to be applied to.
        """
        if target_wire > self.N_wires - 1:
            raise ValueError(
                "target wire must not exceed the number of wires in the circuit."
            )
        if gate.get_num_qubits() != 1:
            raise ValueError("The gate must be a single qubit gate.")

        gate_target_tuple = (target_wire, gate)
        self.gates.append(gate_target_tuple)


# circuit = Circuits()
# H_gate = Gate(1, [[1, 1], [1, -1]] / np.sqrt(2))
# circuit.add_single_qubit_gate(H_gate)
