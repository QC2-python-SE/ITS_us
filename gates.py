import numpy as np

class Gate(object):
    """
    The Gate object is an n-qubit gate represented in the standard basis.
    
    Attributes:
        num_qubits (int): The number of qubits that trhough the gate,
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
        

def tensorprod(gate_list):
    """
    Calculates the tensor product of gates from a list.

    Args:
        gate_list (list): list of Gate objects
    
    Returns:
        Gate object: resulting gate
    """

    tensor_array = gate_list[0].array
    tensor_num_qubits = gate_list[0].num_qubits
    
    for gate in gate_list[1:]:
        tensor_array = np.kron(tensor_array, gate.array)
        tensor_num_qubits += gate.num_qubits
    
    tensor_gate = Gate(tensor_num_qubits, tensor_array)
    return tensor_gate


def create_gate(num_qubits, array):
    """
    Creates a customised gate U. It needs to be unitary or scalable to unitary, in which case it is automatically scaled to a unitary matrix.

    Args:
        num_qubits (int): the number of qubits that pass through the gate,
        array (array_like): A 2^n by 2^n array of floats, where n = num_qubits (int) is the number of qubits.
    
    Returns:
        Gate object: the custom gate.

    """
    
    gate = Gate(num_qubits, array)

    ### Move these tests outside of initiation: move to generation of a U gate
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


def phi_gate(phi):
    """
    Creates a phase gate with an input phase.

    Args:
        phi (float): The input phase, must be a real number.
    
    Returns:
        Gate object: the corresponding phi gate.
    """
    if np.imag(phi) != 0:
        raise ValueError('Input phase is not real. The gate is not unitary.')
    
    return Gate(1, [[1,0],[0,np.exp(1j*phi)]])


### how do I docstring constants?

X_gate = Gate(1, [[0,1],[1,0]])
Y_gate = Gate(1, [[0,-1j],[1j,0]])
Z_gate = Gate(1, [[1,0],[0,-1]])
H_gate = Gate(1, [[1,1],[1,-1]]/np.sqrt(2))
S_gate = Gate(1, [[1,0],[0,1j]])
T_gate = Gate(1, [[1,0],[0,(1+1j)/np.sqrt(2)]])
CNOT_gate = Gate(2, [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])




