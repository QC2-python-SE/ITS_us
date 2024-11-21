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

class states:
    def __init__(self, state = np.array([[1], [0]]), N = 1):
        self.state = state
        self.N = N

    #Inititial Normalised State Function
    def norm_init(self, coef_list, N):

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

    #1 qubit states
    def Zero(self):
        """
        This function gives the |0> = [[1],[0]] state.

        Returns:
            array : An array of numbers.
        """
        self.state = np.array([[1], [0]])
        return self.state

    def One(self):
        """
        This function gives the state: |1> = [[0],[1]].

        Returns:
            array : An array of numbers.
        """
        self.state = np.array([[0], [1]])
        return self.state
    
    def Plus(self):
        """
        This function gives the state: |+> = (|0>+|1>)/sqrt(2).

        Returns:
            array : An array of numbers.
        """
        self.state = (1/math.sqrt(2))*np.array([[1], [1]])
        return self.state
    
    def Minus(self):
        """
        This function gives the state: |-> = (|0>-|1>)/sqrt(2).

        Returns:
            array : An array of numbers.
        """
        self.state = (1/math.sqrt(2))*np.array([[1], [-1]])
        return self.state
    
    def Plus_i(self):
        """
        This function gives the state: |i> = (|0>+i|1>)/sqrt(2).

        Returns:
            array : An array of complex numbers.
        """
        self.state = (1/math.sqrt(2))*np.array([[1], [complex(0,1)]])
        return self.state
    
    def Minus_i(self):
        """
        This function gives the state: |-i> = (|0>-i|1>)/sqrt(2).

        Returns:
            array : An array of complex numbers.
        """
        self.state = (1/math.sqrt(2))*np.array([[1], [complex(0,-1)]])
        return self.state
    
    #Bell States (2 qubits)
    zero = np.array([[1], [1]])
    one = np.array([[0], [1]])
    
    def Psi_plus(self):
        """
        This function gives the state: |Psi+> = (|01>+|10>)/sqrt(2).

        Returns:
            array : An array of numbers.
        """
        self.state = (1/math.sqrt(2))*((np.kron(zero, one) + np.kron(one, zero)))
        return self.state
    
    def Psi_minus(self):
        """
        This function gives the state: |Psi-> = (|01>-|10>)/sqrt(2).

        Returns:
            array : An array of numbers.
        """
        self.state = (1/math.sqrt(2))*((np.kron(zero, one) - np.kron(one, zero)))
        return self.state
    
    def Phi_plus(self):
        """
        This function gives the state: |Phi+> = (|00>+|11>)/sqrt(2).

        Returns:
            array : An array of numbers.
        """
        self.state = (1/math.sqrt(2))*((np.kron(zero, zero) + np.kron(one, one)))
        return self.state
    
    def Phi_minus(self):
        """
        This function gives the state: |Psi-> = (|00>-|11>)/sqrt(2).

        Returns:
            array : An array of complex numbers.
        """
        self.state = (1/math.sqrt(2))*((np.kron(zero, zero) - np.kron(one, one)))
        return self.state
    
    #Tensor Product for only 2 qubits
    #Items in list could be one of the built-in functions (Zero, One). It will be normalised using norm_init.
    def tp(self, lst):
        """
        Takes an input of two lists of length 2:
            1. Checks if the length of a list for 2 qubits is 4.
            2. Applies norm_init function to normalise each state within list and check for errors.
            3. Returns the tensor product of the given two states.

        Args:
            lst (list): Two initial states lists.

        Returns:
            array: A normalised initial tensor product array of complex numbers for 2 qubits.

        """
        #Check length of list
        if (len(lst[0])+ len(lst[1])) == 4:

            #New list of normalised states to tensor product
            lst_new = []

            for l in lst:
                #normalise each state within the list using norm_init
                s = state.norm_init(l,1)
                lst_new.append(s)
            #create a tensor product of each item in the list
            new_state = np.kron(lst_new[0],lst_new[1])
        else:
            raise TypeError("The length of initial states list for 2 qubits is not " + str(len(lst[0])+len(lst[1]))+ ". It should be equal to 4.")
        return new_state

        

#Calling states
state = states()

#Check
print(state.norm_init([1,8],1))
print(state.Minus())
print(state.tp([[2,7],[4,5]]))
print(state.tp([state.Zero(), state.One()]))    

#Error Check
#print(state.tp([[2,"f"],[4,5]]))
#print(state.tp([[2,7,3],[4,5]]))


