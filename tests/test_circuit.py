import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from states import *
from gates import *
from circuits import Circuits
import pytest


def test_add_single_gates():
    """
    Test to ensure that the gate added to the Gates.gates list of tuples is added correctly
    """
    # check a Hadamard is added on the 0th wire
    H_gate = HGate()
    tuple_to_check = (0, H_gate)

    circuit_test = Circuits()
    circuit_test.add_single_qubit_gate(H_gate)

    circuit_test_entry = circuit_test.get_gates()[0]

    assert circuit_test_entry == tuple_to_check


def test_add_two_qubit_gates():
    """
    Test to ensure that the gate added to the Gates.gates list of tuples is added correctly
    """
    # check a Hadamard is added on the 0th wire
    CNOT = CNOTGate2(control=2)
    tuple_to_check = ([0, 1], CNOT)

    zero_two_wires = tp([1, 0], [1, 0])
    circuit_test = Circuits(N_wires=2, state_init=States(N=2, state=zero_two_wires))

    circuit_test.add_two_qubit_gate(CNOT, [0, 1])

    circuit_test_entry = circuit_test.get_gates()[0]

    assert circuit_test_entry == tuple_to_check


def test_run_one_wire():
    """
    Test the run_circuits method on a few cases:

    H|-> = |1>

    """
    state_test_p = One()  # |->
    circuit = Circuits(state_init=Minus())
    H_gate = HGate()
    circuit.add_single_qubit_gate(H_gate, 0)
    state_final = circuit.run_circuit()
    assert np.sum(state_final.get_state() - state_test_p.get_state()) < 10e-10


test_run_one_wire()

#     raise NotImplementedError


def test_run_one_qubit_two_wires():
    """
    Test the run_circuits method on a few cases:

    H⊗I|11> = |-1>

    H⊗H|00> = |++>, added as two different states
    """

    state_test_p1 = States(N=2, state=1 / np.sqrt(2) * np.array([0, 1, 0, -1]))  # |-1>
    state_init_11 = States(N=2, state=np.array([0, 0, 0, 1]))
    circuit = Circuits(N_wires=2, state_init=state_init_11)
    H_gate = HGate()
    circuit.add_single_qubit_gate(H_gate, 0)
    state_final = circuit.run_circuit()

    assert (state_final.get_state() == state_test_p1.get_state()).all()

    state_test_pp = States(N=2, state=1 / 2 * np.array([1, 1, 1, 1]))  # |++>
    state_init_00 = States(N=2, state=np.array([1, 0, 0, 0]))
    circuit = Circuits(N_wires=2, state_init=state_init_00)
    circuit.add_single_qubit_gate(H_gate, 0)
    circuit.add_single_qubit_gate(H_gate, 1)
    state_final_2 = circuit.run_circuit()

    assert (
        np.abs(np.sum(state_final_2.get_state() - state_test_pp.get_state())) < 10e-10
    )  # floating point junk


def test_run_two_qubit_two_wires():
    """
    Test the run_curcuits method on a few cases:

    CNOT|10> = |11>

    """
    state_to_check = States(N=2, state=np.array([0, 0, 0, 1]))
    state_init = States(N=1, state=np.array([0, 0, 1, 0]))
    circuit = Circuits(N_wires=2, state_init=state_init)
    CNOT = CNOTGate2(control=1)
    circuit.add_two_qubit_gate(CNOT, [0, 1])
    state_final = circuit.run_circuit()

    assert (state_final.get_state() == state_to_check.get_state()).all()


def test_prepare_bell():
    """
    Construct the Bell state by running run_curcuits method on a few cases:

    (CNOT_12)(H⊗I)|00> = (|00> + |11>)/sqrt(2)
    """

    state_to_check = PhiPlus()
    H_gate = HGate()
    CNOT = CNOTGate2(control=1)
    state_init = States(N=1, state=np.array([1, 0, 0, 0]))
    circuit = Circuits(N_wires=2, state_init=state_init)

    circuit.add_single_qubit_gate(H_gate, 0)
    circuit.add_two_qubit_gate(CNOT, [0, 1])

    final_state = circuit.run_circuit()

    assert np.abs(np.sum(final_state.get_state() - state_to_check.get_state())) < 10e-10
