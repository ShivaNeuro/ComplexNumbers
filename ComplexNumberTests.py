# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:50:07 2023

@author: shiva
"""

import pytest

from ComplexNumbers import ComplexNumbers

#Test Case for addition
def test_addition():
    Num1 = ComplexNumbers(2,3)
    Num2 = ComplexNumbers(4,5)
    Sum = Num1 + Num2
    assert Sum.real ==6
    assert Sum.imaginary ==8
    
#Test Case for subtraction
def test_subtraction():
    Num1 = ComplexNumbers(2,3)
    Num2 = ComplexNumbers(4,5)
    Diff = Num1 - Num2
    assert Diff.real == -2
    assert Diff.imaginary == -2
    

#Test Case for multiplication
def test_multiplication():
    Num1 = ComplexNumbers(2,3)
    Num2 = ComplexNumbers(4,5)
    Mul = Num1 * Num2 
    assert Mul.real == 8
    assert Mul.imaginary == 15
    

#Test Case for division
def test_division():
    Num1 = ComplexNumbers(2,2)
    Num2 = ComplexNumbers(4,4)
    Div = Num1/Num2
    assert Div.real == 0.5
    assert Div.imaginary == 0 


if __name__ == '__main__':
    pytest.main()