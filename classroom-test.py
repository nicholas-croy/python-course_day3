# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 19:18:13 2022

@author: niccr151
"""

from classroom import Student, Teacher

me = Student('Benedikt','Daurer','physics')
print(me.printNameSubject())

you = Teacher('Benedik','Daurier','physics')
print(you.printNameCourse())