#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math
from copy import deepcopy
from numpy import base_repr

f = open('7/in.raw', 'r')
f = open('7/sample.raw', 'r')
lines = f.read().splitlines()

def old_eval_expr(i, operators,base):
    bin_i = list(f"{{:0{len(operators) - 1}b}}".format(i))
    x=operators[0]
    for j in range(signs_len):
        if bin_i[j]=="0":
            x+=operators[j+1]
        else:
            x*=operators[j+1]
    return(x)

#'''
def eval_expr(n, operators, base):
    #print(old_eval_expr(n, operators,base))
    ops = base_repr(n,base)
    ops = "0"*(len(operators)-1-len(ops))+ops
    new_operators=[operators[0]]
    new_ops=[]
    for i, op in enumerate(ops):
        if op == "2":
            new_operators[-1]=int(str(new_operators[-1])+str(operators[i+1]))
        else:
            new_operators.append(operators[i+1])
            new_ops.append(op)
    operators=new_operators
    ops=new_ops
    x=operators[0]
    for i in range(len(ops)):
        if ops[i]=="0":
            x+=operators[i+1]
        else:
            x*=operators[i+1]
    #print(x)
    #print
    return(x)
#'''
res=0
for line in lines:
    calibration_s, operators_s = line.split(": ")
    calibration=int(calibration_s)
    operators = list(map(int,operators_s.split(" ")))
    i=0
    signs_len = len(operators) - 1
    while i < pow(3,len(operators) - 1):
        if eval_expr(i,operators,3) == calibration:
            res+=calibration
            break
        i+=1
print(res)




