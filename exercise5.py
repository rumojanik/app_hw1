import numpy as np
import sympy as sp

sigma_1 = sp.Matrix([[0,1],[1,0]])
sigma_2 = sp.Matrix([[0,-sp.I],[sp.I,0]])
sigma_3 = sp.Matrix([[1,0],[0,-1]])

def calculate_trace():
    trace_1 = sp.trace(sigma_1)
    print("trace_sigma_1=", trace_1)
    trace_2 = sp.trace(sigma_2)
    print("trace_sigma_2=", trace_2)
    trace_3 = sp.trace(sigma_3)
    print("trace_sigma_3=", trace_3)

def calculate_determinant():
    det_1 = sp.det(sigma_1)
    print("det_sigma_1=", det_1)
    det_2 = sp.det(sigma_2)
    print("det_sigma_2=", det_2)
    det_3 = sp.det(sigma_3) 
    print("det_sigma_3=", det_3)

def calculate_anticommutator(a,b):
    return a*b+b*a
    
def verify_anticommutator():
    print("{sigma_1, sidma_1}=")
    sp.pprint(calculate_anticommutator(sigma_1,sigma_1))
    print("{sigma_1, sidma_2}=")
    sp.pprint(calculate_anticommutator(sigma_1,sigma_2))
    print("{sigma_1, sidma_3}=")
    sp.pprint(calculate_anticommutator(sigma_1,sigma_3))
    print("{sigma_2, sidma_2}=")
    sp.pprint(calculate_anticommutator(sigma_2,sigma_2))
    print("{sigma_2, sidma_3}=")
    sp.pprint(calculate_anticommutator(sigma_2,sigma_3))
    print("{sigma_3, sidma_3}=")
    sp.pprint(calculate_anticommutator(sigma_3,sigma_3))  

if __name__ == '__main__':
    sp.init_printing()
    calculate_trace()
    calculate_determinant()
    verify_anticommutator()