##STATES

"""
States script:
==============

- Provides built-in initial states for 1 and 2 qubits.
- Normalises given initial states for N qubits.

Dependencies:
~~~~~~~~~~~~~
- numpy
- math

Built-in 1 qubit states:
~~~~~~~~~~~~~~~~~~~~~~~~

- zero state = |0> = [[1],[0]]
- one state = |1> = [[0],[1]]
- plus state: |+> = (|0>+|1>)/sqrt(2).
- minus state: |-> = (|0>-|1>)/sqrt(2).
- plus_i state: |i> = (|0>+i|1>)/sqrt(2).
- minus_i state: |-i> = (|0>-i|1>)/sqrt(2).


Built-in Bell States (2 qubits):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- psi_plus state: |Psi+> = (|01>+|10>)/sqrt(2).
- psi_minus state: |Psi-> = (|01>-|10>)/sqrt(2).
- phi_plus state: |Phi+> = (|00>+|11>)/sqrt(2).
- phi_minus state: |Phi-> = (|01>-|11>)/sqrt(2).

"""

import numpy as np
import warnings
import math

# Ignore warnings for clean output
warnings.filterwarnings('ignore')

class States:
    def __init__(self, N = 1, state = np.array([[1], [0]])):
        self.N = N
        self.state = state

    #Initial Normalised State Function
    def norm(self, N, coef_list):

        """
        Takes a coefficients list:
            1. Checks if list contains only complex numbers with the real and imaginary parts being type integer or float. 
            2. Checks if the length of a list for N qubits is 2^N.
            3. Normalises the list such that sum of squared magnitudes is 1.
            4. Changes list to a column if it was a row.
            5. Returns the normalised list.

        Args:
            coef_list (list): An inititial state list of complex numbers for N qubits.

        Returns:
            array: A normalised initial state array of complex numbers for N qubits.

        """
        #Checks if list contains only complex numbers with the real and imaginary parts being type integer or float.      
        try:
            np.sum(coef_list)
        except:
            raise TypeError('List should contain only complex numbers with the real and imaginary parts being type integer or float.')
        
        #Checks if length of the state for N qubits is 2^N or else gives error and suggested correction.
        if len(coef_list) != 2**N:
            raise TypeError("The length of initial states list for " + str(N) + " qubit(s) is not " + str(len(coef_list))+ ". It should be equal to " + str(2**N) +".")


        coef_arr = np.array(coef_list)

        #Squared magnitude of coeff_list.
        sqrd_mag = []
        for i in range(0,len(coef_arr)):
            coeff2 = coef_arr[i]*(coef_arr[i].conjugate())
            sqrd_mag.append(coeff2)

        #Check if it's normalised.
        if sum(sqrd_mag) == 1:
            self.state = coef_arr.reshape(-1, 1)
            return self.state
        
        #If it's not normalised, normalise it.
        else:
            norm = math.sqrt(sum(sqrd_mag))
            norm_state = (1/norm)*(coef_arr)
            #Make it a column
            if coef_arr.ndim == 1:
                self.state = norm_state.reshape(-1, 1)
                return self.state
            else:
                self.state = norm_state
                return self.state
            



class BuiltIn(States):
    def __init__(self, N = 1, state = np.array([[1], [0]])):
        super().__init__(N, state)
    
    #1 qubit states
    @staticmethod
    def zero():
        """
        This function gives the |0> = [[1],[0]] state.

        Returns:
            array : An array of numbers.
        """
        return np.array([[1], [0]])
    
    @staticmethod
    def one():
        """
        This function gives the |1> = [[0],[1]] state.

        Returns:
            array : An array of numbers.
        """
        return np.array([[0], [1]])

    @staticmethod
    def plus():
        """
        This function gives the state:
        .. math::
            |+> =  \frac{1}{\sqrt{2}}(|0> + |1>)

        Returns:
            array : An array of numbers.
        """
        return (1/math.sqrt(2))*np.array([[1], [1]])
    
    @staticmethod
    def minus():
        """
        This function gives the state: 
        .. math::
            |-> =  \frac{1}{\sqrt{2}}(|0> - |1>)

        Returns:
            array : An array of numbers.
        """
        return (1/math.sqrt(2))*np.array([[1], [-1]])
    
    @staticmethod
    def plus_i():
        """
        This function gives the state: 
        .. math::
            |i> =  \frac{1}{\sqrt{2}}(|0> + i|1>)

        Returns:
            array : An array of complex numbers.
        """
        return (1/math.sqrt(2))*np.array([[1], [complex(0,1)]])
    
    @staticmethod
    def minus_i():
        """
        This function gives the state: 
        .. math::
            |i> =  \frac{1}{\sqrt{2}}(|0> - i|1>)

        Returns:
            array : An array of complex numbers.
        """
        return (1/math.sqrt(2))*np.array([[1], [complex(0,-1)]])

    #Bell States (2 qubits)
    def psi_plus(self):
        """
        This function gives the state: 
        .. math::
            | \Psi^+ > =  \frac{1}{\sqrt{2}}(|01> + |10>)

        Returns:
            array : An array of numbers.
        """
        return (1/math.sqrt(2))*((np.kron(self.zero(), self.one()) + np.kron(self.one(), self.zero())))

    def psi_minus(self):
        """
        This function gives the state:
        .. math::
            | \Psi^- > =  \frac{1}{\sqrt{2}}(|01> - |10>)

        Returns:
            array : An array of numbers.
        """
        return (1/math.sqrt(2))*((np.kron(self.zero(), self.one()) - np.kron(self.one(), self.zero())))

    def phi_plus(self):
        """
        This function gives the state: 
        .. math::
            | \Phi^+ > =  \frac{1}{\sqrt{2}}(|00> + |11>)

        Returns:
            array : An array of numbers.
        """
        return (1/math.sqrt(2))*(np.kron(self.zero(), self.zero()) + np.kron(self.one(), self.one()))

    def phi_minus(self):
        """
        This function gives the state:
        .. math::
            | \Phi^- > =  \frac{1}{\sqrt{2}}(|00> - |11>)

        Returns:
            array : An array of complex numbers.
        """
        return (1/math.sqrt(2))*((np.kron(self.zero(), self.zero()) - np.kron(self.one(), self.one())))

#Tensor Product for only 2 qubits
#State_1 and State_2 could be one of the built-in functions (zero, one); otherwise, it will be normalised using norm.
def tp(state_1, state_2):
    """
    Takes an input of two states of length 2:
        1. Checks if the length of each state is 2.
        2. Applies norm function to normalise each state within list and check for errors.
        3. Returns the tensor product of the given two states.

    Args:
        lst (list): Two initial states lists.

    Returns:
        array: A normalised initial tensor product array of complex numbers for 2 qubits.

    """
    #Checks length of list
    if len(state_1) == 2 and len(state_2) == 2:
        #Normalised states 1 and 2
        s1 = state.norm(1, state_1)
        s2 = state.norm(1, state_2)
        #Create a tensor product of each item in the list
        tp_state = np.kron(s1, s2)
    else:
        raise TypeError("The length of each initial state list for states 1 and 2 should be 2.")
    return tp_state

        

#Calling states
state = States()
#Calling subclass (Built-in states)
bis = BuiltIn()

#Check
state1 = state.norm(1, [3,5])
state2 = state.norm(1, [8,2])
print(state.norm(1, [1,8]))
print(bis.minus())
print(tp(state1, state2))
print(tp(bis.zero(), bis.one()))
print(bis.one())
print(bis.psi_plus())

#Error Check
#print(state.tp([[2,"f"],[4,5]]))
#print(state.tp([[2,7,3],[4,5]]))