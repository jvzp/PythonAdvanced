#!/usr/bin/env python

from collections import namedtuple

EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

import csv

employee_list = [EmployeeRecord(x) for x in csv.reader(open("employees.csv", "r"))]

print employee_list
