'''
Created on Dec 2, 2017

@author: nataliemorel
'''
from _ast import Num
def print_factors(x):
    list=[];
    print("The factors of," "x," "are:")
    for i in range (1, x+1):
        if x%i == 0:
            list.append(i)
            
num=int(input("Enter a number:"))
print_factors(Num)
