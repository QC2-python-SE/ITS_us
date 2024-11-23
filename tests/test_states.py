#Test states.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import numpy as np
import math
from states import States, BuiltIn, tp

@pytest.fixture
def test_States():
    """
    Test if norm method creates a normalised initial state correctly.
    """
    sqrt2 = 1/math.sqrt(2)
    test_states = States()
    s0 = test_states.norm(1,[1,0])
    s1 = test_states.norm(1, [1, 1])
    s2 = test_states.norm(2, [1, 1, 1, 1])
    assert (s0 == np.array([[1],[0]])).all()
    assert (s1 == np.array([[sqrt2], [sqrt2]])).all()
    assert (s2 == np.array([[0.5],[0.5],[0.5],[0.5]])).all()

def test_tp():
    """
    1. Test if tp function creates a tensor product correctly.
    2. Test if tp function outputs the right dimensions.
    """
    s0 = [[1],[0]]
    s1 = [[0],[1]]
    tp_ex1 = np.array([[0],[1],[0],[0]])
    tp_test1 = tp(s0, s1)
    dim1, dim2, dimF = len(s0), len(s1), len(tp_test1)
    assert (tp_test1 == tp_ex1).all()
    assert (dim1 == 2) and (dim2 == 2)
    assert (dim1 + dim2) == dimF
