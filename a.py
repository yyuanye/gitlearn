#!/usr/bin/env python
# coding=utf-8

from functools import reduce

def sum(n):
    sum=0
    for i in range(n+1):
        sum=sum+i
    return sum

def power1(a,n):
    sum=1
    for i in range(n):
        sum=sum*a
    return sum

def list1(L=[]):
    L.append("end")
    return L

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

def map1(s):
    def f(s1):
        return s1.capitalize()
    return list(map(f,s))

def prod(L):
    def mul1(x,y):
        return x*y
    return reduce(mul1,L)

def sushu(L):
    def is_odd(s):
        return s%2==1
    return list(filter(is_odd,L))

def lazy_sum(*args):
    def sum():
        ax=0
        for i in args:
            ax=ax+i
        return ax
    return sum

print('Hello!')
