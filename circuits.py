#this is a placeholder
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
from states import States
from gates import Gates

class Circuits:

    def __init__(self, N_wires = 1, state_init= np.array([[1], [0]])):

        self.N_wires = N_wires
        self.states = States()
        self.gates = []
        
    def add_single_qubit_gate(self, gate: Gates, target_wire: int):
        """
            Function to add a single wubit gate to the circuit at a given wire.
            Creates a tuple of the gate and the target wire and appends it to the gates list.

            Args:
                gate (Gates): The gate to be added to the circuit.
                target_wire (int): The wire the gate is to be applied to.
        """
        if target_wire >= self.N_wires:
            raise ValueError("target wire must not exceed the number of wires in the circuit.")
        if gate.get_num_qubits() != 1:
            raise ValueError("The gate must be a single qubit gate.")

        gate_target_tuple = (gate, target_wire)
        self.gates.append(gate_target_tuple)


