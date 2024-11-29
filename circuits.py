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
from states import *
from gates import Gate


class Circuits:

    def __init__(self, N_wires=1, state_init= Zero()):

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
        Function to add a single qubit gate to the circuit at a given wire.
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

    def add_two_qubit_gate(self, gate: Gate, target_wires: list = [0,1]):
        """
        Function to add a two qubit gate to the circuit at a given wire.
        Creates a tuple of the gate and the target wires and appends it to the gates list.

        Args:
            gate (Gates): The gate to be added to the circuit.
            target_wire (int): The wire the gate is to be applied to.
        """
        if max(target_wires) > self.N_wires - 1 or min(target_wires) < 0:
            raise ValueError(
                "Target wires must not exceed the number of wires in the circuit."
            )
        if gate.get_num_qubits() != 2:
            raise ValueError("The gate must be a single qubit gate.")
        
        gate_target_tuple = (target_wires, gate)
        self.gates.append(gate_target_tuple)

    def run_circuit(self):
        
        for gate in self.gates:
            #create a temporary identity matrix based on the number of wires

            if gate[1].num_qubits == 1:
                identity_list = [np.eye(2)]*self.N_wires
                identity_list[gate[0]] = gate[1].get_array()
                try:
                    #for 2 wires
                    N_wire_gate = np.kron(*identity_list)
                except TypeError:
                    # for 1 wire
                    N_wire_gate = gate[1].get_array()

            elif gate[1].num_qubits == 2:
                N_wire_gate = gate[1].get_array()

            self.state = N_wire_gate @ self.state

            
        return self.state
                
        
    def measure_qubits():
        raise NotImplementedError
