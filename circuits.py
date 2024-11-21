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
        
    def add_gate(self, gate: Gates, target_wire: int):
        """
            Function to add a gate to the circuit operating on the target wire.

            Args:
                gate (Gates): The gate to be added to the circuit.
                target_wire (int): The wire the gate is to be applied to.
        """

        gate_target_tuple = (gate, target_wire)
        self.gates.append(gate_target_tuple)


