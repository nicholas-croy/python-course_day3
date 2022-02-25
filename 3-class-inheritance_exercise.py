# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 18:53:40 2022

@author: niccr151
"""

class Person():
    def __init__(self, first_name, last_name):
        self.full_name = first_name + " " + last_name
    def getName(self):
        return self.full_name

class Student(Person):
    def __init__(self, first_name, last_name, subject):
        super(Person, self).__init__(self, first_name, last_name)
        self.subject = subject
    def printNameSubject(self):
        self.NameSubject = self.full_name + ", " + self.subject
        return self.NameSubject