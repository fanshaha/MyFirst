#同心圆的绘制
# from turtle import *
# def Painting():
# 	for i in range(5):
# 		up()
# 		seth(90)
# 		fd(30)
# 		seth(180)
# 		down()
# 		circle(30 * (i + 1))
# setup(1200,800,50,50)
# pensize(2)
# Painting()
#彩色同心圆的绘制
from turtle import *
def Painting():
	temp = ('red','orange','yellow','green','cyan','blue')
	for i in range(6):
		color(temp[i])
		up()
		seth(90)
		fd(30)
		seth(180)
		down()
		circle(30 * (i + 1))
setup(1200,800,50,50)
pensize(10)
Painting()
