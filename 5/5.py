#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math
from copy import deepcopy


f = open('5/in.raw', 'r')
#f = open('5/sample.raw', 'r')
lines = f.read().splitlines()



def check_list(l,r):
    ok=True
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if (l[j],l[i]) in r:
                ok=False
    if ok:
        print(l)
        print(l[len(l)//2])
        return(l[len(l)//2])
    else:
        return(0)


def find_leftmost(rules,l):
    for p in l:
        if all((rule[1]!=p for rule in rules )):
            return(p)
def fix_list(l,r):
    ok=False
    my_rules=set()
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if (l[j],l[i]) in r:
                ok=True
                my_rules.add((l[j],l[i]))
            else:
                assert((l[i],l[j]) in r)
                my_rules.add((l[i],l[j]))
    if ok:
        new_l = []
        old_l = set(l)
        for _ in range(len(l)):
            leftmost=find_leftmost(my_rules,old_l)
            new_l.append(leftmost)
            old_l.discard(leftmost)
            my_rules=set([my_rule for my_rule in my_rules if my_rule[0]!=leftmost ])
        print(new_l)
        print(new_l[len(new_l)//2])
        return(new_l[len(new_l)//2])
    else:
        return(0)


list_zone = False
rules=set()
res1=0
res2=0
for line in lines:
    if line=="":
        list_zone = True
    else:
        if list_zone:
            res1+=check_list(list(map(int,line.split(','))),rules)
            res2+=fix_list(list(map(int,line.split(','))),rules)
        else:
            rules.add(tuple(int(i) for i in line.split('|')))
print(res1,res2)
#print(rules)

