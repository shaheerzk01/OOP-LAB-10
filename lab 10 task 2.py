#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:05:11 2022

@author: macbook
"""

class Student:
    
    def __init__(self, name, test_score=0, grade=""):
        self._name = name
        self._test_score = test_score
        self._grade = grade
        
    def get_name(self):
        return self._name
    
    def set_test_score(self, new_test_score):
        self._test_score  = new_test_score
        
    def compute_grade(self):
        pass
    
    def get_grade(self):
        return self._grade
    
class UndergraduateStudent(Student):
    def __init__(self,name):
        super().__init__(name)
        
    def compute_grade(self):
        if self._test_score >=60:
            self._grade = "pass"
        else:
             self._grade = "fail"
             
class GraduateStudent(Student):
    def __init__(self,name):
        super().__init__(name)
        
    def compute_grade(self):
        if self._test_score >=70:
            self._grade = "pass"
        else:
             self._grade = "fail"
        
def main():
    S1 = UndergraduateStudent(a)
    S1.set_test_score(b)
    S1.compute_grade()
    print(S1.get_name(), S1._test_score, S1.get_grade())
    S2 = GraduateStudent(x)
    S2.set_test_score(y)
    S2.compute_grade()
    print(S2.get_name(), S2._test_score, S2.get_grade())
    S3 = UndergraduateStudent(r)
    S3.set_test_score(s)
    S3.compute_grade()
    print(S3.get_name(), S3._test_score, S3.get_grade())
a = str(input("Enter name : "))
b = int(input("Enter test score : "))
x = str(input("Enter name : "))
y = int(input("Enter test score : "))
r = str(input("Enter name : "))
s = int(input("Enter test score : "))
main()
