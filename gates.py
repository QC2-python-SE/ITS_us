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


def phase_gate(phase):
    """
    Creates a phase gate from a given input phase.

    Args:
        phase (float): The input phase, must be a real number.
    
    Returns:
        Gate: the corresponding phase gate.
    """
    if np.imag(phase) != 0:
        raise ValueError('Input phase is not real. The gate is not unitary.')
    
    return Gate(1, [[1,0],[0,np.exp(1j*phase)]])


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


def controlled_gate2(gate, control):
    """
    Controlled gate (custom) for 2 qubit systems, with the control from specified qubit.

    Args:
        gate (Gate): must be a 1-qubit gate.
        control (int): if 1, the control is the first qubit. If 2, the control is the second qubit.
    
    Returns:
        Gate: the controlled gate.
    """
    U_gate = gate.array
    if control == 1:
        return  Gate(2, [[1,0,0,0],[0,1,0,0],[0,0,U_gate[0,0],U_gate[0,1]],[0,0,U_gate[1,0],U_gate[1,1]]])
    elif control == 2:
        return  Gate(2, [[1,0,0,0],[0,U_gate[0,0],0,U_gate[0,1]],[0,0,1,0],[0,U_gate[1,0],0,U_gate[1,1]]])
    else:
        raise ValueError('The control must be 1 or 2 for a 2-qubit system.')


def CNOT_gate2(control):
    """
    CNOT gate for 2 qubit systems, with the control from specified qubit.
    This is equivalent to "controlled_gate2(X_gate, control)".

    Args:
        control (int): if 1, the control is the first qubit. If 2, the control is the second qubit.
    
    Returns:
        Gate object: the CNOT gate.
    """
    if control == 1:
        return  Gate(2, [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    elif control == 2:
        return  Gate(2, [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])
    else:
        raise ValueError('The control must be 1 or 2 for a 2-qubit system.')
    
###COMMENTS FOR THEO (delete at some point)
# class CNOT(Gate):
#     def __init__(self, control=0):
#         super().__init__(num_qubits=2)#, [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])
#         if control == 0:
#             self.array =  [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]]
#         elif control == 1:
#              self.array =  [[1,0,0,0],[0,1,0,1],[0,0,1,0],[0,1,100,1]]


#ideally we should want a class that you could call like this:

# cnot_gate_01 =  CNOT(control= 0)
# cnot_gate_01.get_array()
# cnot_gate_01.get_num_qubits()


# cnot_gate_10 = CNOT(control=1)

# cnot_gate_10.get_array()

# class GenRotation(Gate):
#     def __init__(self, theta, phi):
#         super().__init__(1)#, [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])
        

### how do I docstring constants?

X_gate = Gate(1, [[0,1],[1,0]])
Y_gate = Gate(1, [[0,-1j],[1j,0]])
Z_gate = Gate(1, [[1,0],[0,-1]])
H_gate = Gate(1, np.array([[1,1],[1,-1]])/np.sqrt(2))
S_gate = Gate(1, [[1,0],[0,1j]])
T_gate = Gate(1, [[1,0],[0,(1+1j)/np.sqrt(2)]])
SWAP_gate2 = Gate(2, [[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
HH_gate = Gate(2, 0.5 * np.array([[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]]))
FT_gate = Gate(2, 0.5 * np.array([[1,1,1,1],[1,1j,-1,-1j],[1,-1,1,-1],[1,-1j,-1,1j]]))




