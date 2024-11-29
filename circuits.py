# this is a placeholder
"""
Circuits module
==============

- Provides built-in initial states for 1 and 2 qubits.
- Normalises given initial states for N qubits.

Dependencies:
~~~~~~~~~~~~~
- numpy
- copy

"""


import numpy as np
from states import *
from gates import Gate
from copy import deepcopy

class Circuits:

    def __init__(self, N_wires=1, state_init= Zero()):

        self.N_wires = N_wires
        self.state_init = state_init
        self.gates = []

        #checks on the input variables
        if isinstance(state_init, States) == False:
            raise TypeError("Initial state must be State type")
        while N_wires not in [1, 2]:
            raise TypeError("Number of wires must be 1 or 2")

        # check that the initial state has the correct dimension for the number of wires
        if np.log2(len(state_init.get_state())) != N_wires:
            raise ValueError("The initial state dimension must match the number of wires.")

    def get_gates(self):
        """
        Returns the current list of gates in the circuit
        """
        return self.gates

    def get_state_init(self):
        """
        Returns the initial quantum state of the circuit as an array

        Returns:
            array: The state as a numpy array
    
        """
        return self.state_init.get_state()

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
        """
        Applies the circuit at the current stage 

        Returns:
            State: Final state after running the circuit
        """
        #prepare initial state array
        state_array = deepcopy(self.get_state_init())
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

            state_array = N_wire_gate @ state_array

            
        return States(state = state_array, N=self.N_wires)
                
        
    def measure_qubits():
        raise NotImplementedError

