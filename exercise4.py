import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

matrix_a = sp.Matrix([[1,2],[3,3]])
matrix_b = sp.Matrix([[20,20],[10,10]])

"""Print matrices"""
def print_matrices():
    sp.pprint(matrix_a)
    print("\n")
    sp.pprint(matrix_b)
    print("\n")

"""Multiply matrices"""
def multiply_Matrices():
    matrix_c = matrix_a*matrix_b #matrix product
    sp.pprint(matrix_c)
    print("\n")
    matrix_c_representation = sp.MatMul(matrix_a, matrix_b) #representation for console
    #print all
    sp.pprint(matrix_c_representation)
    print("=")
    sp.pprint(matrix_c)
    print("\n")

"""Print A_01"""
def print_a01():
    sp.pprint(matrix_a[0,1])
    print("\n")

"""Transpose matrix A"""
def transpose():
    sp.pprint(sp.Transpose(matrix_a)) #representation
    print("=")
    sp.pprint(matrix_a.T) #transposition
    print("\n")

"""Invert matrix A"""
def invert():
    sp.pprint(sp.Inverse(matrix_a))# representation
    print("=")
    sp.pprint(matrix_a.inv()) #inversion
    print("proof:")
    sp.pprint(sp.MatMul(matrix_a.inv(), matrix_a)) #representation
    print("=")
    sp.pprint(matrix_a.inv()*matrix_a) #product of A and its inverse
    print("\n")

if __name__ == '__main__':
    sp.init_printing()
    #a)
    print_matrices()
    #b)
    multiply_Matrices()
    #c)
    print_a01()
    #c)
    transpose()
    #d)
    invert()