# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MruzmYBIcI09N-2c-Iya_BD81QegbupW
"""

a = input('enter the number: ')
b = input('enter the number: ')
c = input('enter the number: ')

if (a >= b) and (a >= c):
    largest=a
elif (b >= a) and (b >= c):
    largest=b
else:
    largest=c

print(largest, "is the greatest of all")