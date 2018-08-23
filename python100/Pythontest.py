'''


def gcd(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range[1,smaller + 1]:
        if ((x%i == 0 )and (y%i==0)):
            return i

if __name__ == '__main__':
    b = map(int, raw_input(" ").split(" "))
    Array=[]
    Array[0] = b[3]
    for i in range(1,b[0]):
        Array[i]=(Array[i-1]+153)%p
    sum = 0
    for i in range(1,b[1]+1):
        for j in range(1,b[2]+1):
            sum += Array(gcd(i,j))
    print sum

s = raw_input()
b = map(int, raw_input(" ").split(" "))
Array=[]
Array[0] = b[3]
for i in range(1,b[0]):
	Array[i]=(Array[i-1]+153)%p
sum = 0
for i in range(1,b[1]+1):
	for j in range(1,b[2]+1):
    	sum += Array[gcd(i,j)-1]
print sum
'''
'''
# !/usr/bin/python
# -*- coding: UTF-8 -*-

str = input("请输入：")
print("你输入的内容是: ", str)
print([x*5 for x in range(2,10,2)])
print([x**2 for x in [2,10,2]])
'''
import sys
if __name__ == '__main__':
    #l1=sys.stdin.readline().strip()
    #values = list(map(int,l1.split()))
   # print([x**2  for x in values])
    str = ('www.google.com')
    print(str)
    str_split = str.split('.')
    print(str_split)