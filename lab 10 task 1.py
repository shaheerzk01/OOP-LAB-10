#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 14:36:52 2022

@author: macbook
"""

class GeometricShape:
    
    def __init__(self, color):
        self.__color = color
        
    def get_color(self):
        return self.__color
    
class Rectangle(GeometricShape):
    
    def __init__(self, width, height, color):
        super().__init__(color)
        self.__width = width
        self.__height = height
        
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    def get_Area(self):
        print(self.__width * self.__height)
    
    def get_perimeter(self):
        print(2 * (self.__width + self.__height))
    
def main():
    R1 = Rectangle(a, b, c)
    R2 = Rectangle(x, y, z)
    R3 = Rectangle(r, s, t)
    print()
    R1.get_color(),R1.get_Area(),R1.get_perimeter()
    R2.get_color(),R2.get_Area(),R2.get_perimeter()
    R3.get_color(),R3.get_Area(),R3.get_perimeter()
a = int(input("Enter width for R1 : "))
b = int(input("Enter height for R1 : "))
c = str(input("Enter color for R1 : "))
x = int(input("Enter width for R2 : "))
y = int(input("Enter height for R2 : "))
z = str(input("Enter color for R2 : "))
r = int(input("Enter width for R3 : "))
s = int(input("Enter height for R3 : "))
t = str(input("Enter color for R3 : "))
main()    