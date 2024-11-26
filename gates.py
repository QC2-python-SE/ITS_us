## GATES

"""
Gates script:
=============

- Provides a class of standard gates for 1 and 2 qubits.
- Allows for custom gate creation, and scales to unitary if necessary.
- Allows for controlled-gate for any gate.
- Can perform tensor product of gates.

Dependencies:
~~~~~~~~~~~~~
- numpy

Built-in 1 qubit gates:
~~~~~~~~~~~~~~~~~~~~~~~

- X_gate: X gate.
- Y_gate: Y gate.
- Z_gate: Z gate.
- H_gate: Hadamard gate.
- S_gate: S gate.
- T_gate: T gate.


Built-in 2 qubit gates:
~~~~~~~~~~~~~~~~~~~~~~~

- CNOT_gate2(control): CNOT gate with specified control.
- SWAP_gate2: SWAP gate.
- HH_gate2: double Hadamard gate (Hadamard on each qubit).
- FT_gate2: Quantum Fourier Transform gate on 2 qubits.

Example for calling gates:
~~~~~~~~~~~~~~~~~~~~~~~~~~

x       = gates.X_gate          # produces instance of an X gate.
cnot1   = gates.CNOT_gate2(1)   # produces instance of a CNOT gate with control on the first qubit.

"""

import numpy as np

class Gate(object):
    """
    The Gate object is an n-qubit gate represented in the standard basis.
    
    Attributes:
        num_qubits (int): The number of qubits that pass through the gate,
        array (ndarray): 2^n by 2^n array representing the gate.
    """

    def __init__(self, num_qubits, array):
        """
        Initiates the Gate class.

        Args:
            num_qubits (int): the number of qubits that pass through the gate,
            array (array_like): A 2^n by 2^n array of floats, where n = num_qubits (int) is the number of qubits.
        """

        self.num_qubits = num_qubits
        self.array = np.array(array)


    def get_array(self):
        """
        Reads the gate in matrix form.

        Returns:
            ndarray: copy of gate array
        """
        copy = np.copy(self.array)
        return copy
    
    def get_num_qubits(self):
        """
        Reads the number of qubits that pass through the gate.

        Returns:
            int: number of qubits
        """
        return self.num_qubits
        

def create_gate(num_qubits, array):
    """
    Creates a customised gate U. It needs to be unitary or scalable to unitary, in which case it is automatically scaled to a unitary matrix.

    Args:
        num_qubits (int): the number of qubits that pass through the gate,
        array (array_like): A 2^n by 2^n array of floats, where n = num_qubits (int) is the number of qubits.
    
    Returns:
        Gate: the custom gate.

    """
    
    gate = Gate(num_qubits, array)

    # Array must contain ints, floats or complex numbers.
    try:
        np.sum(gate.array)
    except:
        raise TypeError('Input array contains non-numerical elements. Elements of the array \
                        should be integers, float points, or complex numbers of the form (<float> + <float> j).')
    
    # Array must be square of the form (2^n x 2^n).
    if gate.array.shape != (2**gate.num_qubits, 2**gate.num_qubits):
        raise ValueError('The number of qubits does not match array size. Check that a- your \
                            array is square, b- its size is (2^n x 2^n).')
    
    # Array must be unitary or scalable to a unitary matrix. For the latter case, it is rescaled to a unitary matrix.
    check_identity = gate.array * gate.array.conj().T

    if np.array_equal(check_identity, np.identity(gate.num_qubits) * check_identity[0,0]):
        raise ValueError('The gate is not unitary or scalable to unitary. Check for typos in the matrix elements.')
    elif check_identity[0,0] != 1:
        gate.array /= np.sqrt(check_identity[0,0])
    
    return gate



class PhaseGate(Gate):
    def __init__(self, phase):
        """
        Initiates a phase gate from a given input phase.

        Args:
            phase (float): The input phase, must be a real number.
        
        Returns:
            Gate: the corresponding phase gate.
        """
        num_qubits = 1
        array = [[1,0],[0,np.exp(1j*phase)]]
        super().__init__(num_qubits, array)


class ControlledGate2(Gate):
    def __init__(self, control, gate1):
        
        """
        Initiates a controlled gate (custom) for 2 qubit systems, with the control from specified qubit.

        Args:
            gate (Gate): must be a 1-qubit gate.
            control (int): if 1, the control is the first qubit. If 2, the control is the second qubit.
        """

        num_qubits = 2
        if gate1.get_num_qubits() != 1:
            raise ValueError('The gate is not a one-qubit gate.')
        U_gate = gate1.get_array()
        if control == 1:
         array = [[1,0,0,0],[0,1,0,0],[0,0,U_gate[0,0],U_gate[0,1]],[0,0,U_gate[1,0],U_gate[1,1]]]
        elif control == 2:
            array = [[1,0,0,0],[0,U_gate[0,0],0,U_gate[0,1]],[0,0,1,0],[0,U_gate[1,0],0,U_gate[1,1]]]
        super().__init__(num_qubits, array)

    
class CNOTGate2(Gate):
    def __init__(self, control):
        """
        Initiates a CNOT gate for 2 qubit systems, with the control from specified qubit.
        This is equivalent to "controlled_gate2(X_gate, control)".

        Args:
            control (int): if 1, the control is the first qubit. If 2, the control is the second qubit.
        """
        num_qubits = 2
        if control == 1:
         array = [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]
        elif control == 2:
            array = [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]]
        super().__init__(num_qubits, array)


class XGate(Gate):
    """
    Initiates an X gate.
    
    Args:
        None.
    """
    def __init__(self):
        num_qubits = 1
        array = [[0,1],[1,0]]
        super().__init__(num_qubits, array)

class YGate(Gate):
    """
    Initiates a Y gate.
    
    Args:
        None.
    """
    def __init__(self):
        num_qubits = 1
        array = [[0,-1j],[1j,0]]
        super().__init__(num_qubits, array)

class ZGate(Gate):
    """
    Initiates a Z gate.
    
    Args:
        None.
    """
    def __init__(self):
        num_qubits = 1
        array = [[1,0],[0,-1]]
        super().__init__(num_qubits, array)

class HGate(Gate):
    """
    Initiates a Hadamard gate.
    
    Args:
        None.
    """
    def __init__(self):
        num_qubits = 1
        array = np.array([[1,1],[1,-1]])/np.sqrt(2)
        super().__init__(num_qubits, array)

class SGate(Gate):
    """
    Initiates an S gate.
    
    Args:
        None.
    """
    def __init__(self):
        num_qubits = 1
        array = [[1,0],[0,1j]]
        super().__init__(num_qubits, array)

class TGate(Gate):
    """
    Initiates a T gate.
    
    Args:
        None.
    """
    def __init__(self):
        num_qubits = 1
        array = [[1,0],[0,(1+1j)/np.sqrt(2)]]
        super().__init__(num_qubits, array)

class SWAPGate2(Gate):
    """
    Initiates a SWAP gate for 2 qubits.
    
    Args:
        None.
    """
    def __init__(self):
        num_qubits = 2
        array = [[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]]
        super().__init__(num_qubits, array)

class HHGate2(Gate):
    """
    Initiates a HxH gate.
    
    Args:
        None.
    """
    def __init__(self):
        num_qubits = 2
        array = [[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]]
        super().__init__(num_qubits, array)

class FTGate2(Gate):
    """
    Initiates a FT gate.
    
    Args:
        None.
    """
    def __init__(self):
        num_qubits = 2
        array = [[1,1,1,1],[1,1j,-1,-1j],[1,-1,1,-1],[1,-1j,-1,1j]]
        super().__init__(num_qubits, array)


def tensorprod(gate_list):
    """
    Calculates the tensor product of gates from a list.

    Args:
        gate_list (list): list of Gate objects
    
    Returns:
        Gate: resulting gate
    """

    tensor_array = gate_list[0].array
    tensor_num_qubits = gate_list[0].num_qubits
    
    for gate in gate_list[1:]:
        tensor_array = np.kron(tensor_array, gate.array)
        tensor_num_qubits += gate.num_qubits
    
    tensor_gate = Gate(tensor_num_qubits, tensor_array)
    return tensor_gate
