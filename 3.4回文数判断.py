#cording = utf-8
#3.4回文判断
from math import *
Num = input("输入一个五位数的自然数：")
a = eval(Num) % 10
b = eval(Num)//10%10
c = eval(Num)//100%10
d = eval(Num)//1000%10
f = eval(Num) // 10000
if (a != f and b != d):
	print("这个自然数不是回文数")
else:
	print("这个自然数是回文数")
