# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:03:59 2023

@author: shiva
"""
# Assignment Part 2


class ComplexNumbers:
    # Complex Number with attributres real and imaginary.
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __repr__(self):
        # To return printable representation of Complex Numbers.
        if self.imaginary < 0:
            return f"{self.real}-{abs(self.imaginary)}i"
        else:
            return f"{self.real}+{self.imaginary}i" 
       
            
    def __add__(self,other)
        # Dunder method for addition to handle complex number objects
        img = self.imaginary + other.imaginary
        real = self.real + other.real
        return ComplexNumbers(real,img)
    
    
    def __sub__(self,other):
        # Dunder method for subtraction to handle complex number objects
        img = self.imaginary - other.imaginary
        real = self.real - other.real
        return ComplexNumbers(real,img)
    
    def __mul__(self,other):
        #Dunder method for multiplication to handle complex number objects.
        img = self.imaginary * other.imaginary
        real = self.real * other.real
        return ComplexNumbers(real,img)
    
    def __truediv__(self,other):
        # Dunder method for division to handle complex number objects.
        img = (self.imaginary * other.real - self.real * other.imaginary)/(other.real**2 + other.imaginary**2)
        real = (self.real * other.real + self.imaginary * other.imaginary)/(other.real**2 + other.imaginary**2)
        return ComplexNumbers(real,img)
    
   
    
    # Reference for division of complex numbers : https://www.cuemath.com/numbers/division-of-complex-numbers/
    
    # To do 
    ## Implement Other representations of complex Numbers..
'''    
Commented to use it as Library.Added for test purpose.Test cases are written in ComplexNumberTests.
if __name__ == '__main__':
    CompNum1 = ComplexNumbers(2,3)
    CompNum2 = ComplexNumbers(7,4)
    # Addition
    print(CompNum1 + CompNum2)
    # Subtraction
    print(CompNum1 - CompNum2)
    # Multiplication
    print(CompNum1 * CompNum2)
    # Division
    print(CompNum1 /CompNum2)
'''