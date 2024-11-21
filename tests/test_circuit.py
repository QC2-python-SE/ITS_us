import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from states import states
from gates import Gate
from circuits import Circuits

import pytest


def test_add_gates():
    """
    Test to ensure that the gate added to the Gates.gates list of tuples is added correctly
    """
    #check a Hadamard is added on the 0th wire
    H_gate = Gate(1, [[1, 1], [1, -1]] / np.sqrt(2))
    tuple_to_check = (0, H_gate)

    circuit_test = Circuits()
    circuit_test.add_single_qubit_gate(H_gate)

    circuit_test_entry = circuit_test.get_gates()[0]

    assert circuit_test_entry == tuple_to_check


