import random
from random import randint
import sys
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint, QPropertyAnimation



class Shapes(object):
	"""docstring fss Shapes"""
	def __init__(self, xcord, ycord):
		self.height = randint(10,75)
		self.width = randint(25,75)
		self.cordx = xcord
		self.cordy = ycord
		color = ["blue" , "black" , "brown" , "red" , "yellow" , "green" , "orange" , "beige" , "turquoise" , "pink"]
		self.color = color[randint(0,len(color)-1)]



class Rectangle(Shapes):

	def __init__(self, xcord, ycord):

		super().__init__(xcord, ycord)

	def Draw(self, qp):
#setting up the drawing for rectangles
		pen_color = QPen(QColor(self.color))
		qp.setPen(pen_color)
		qp.setBrush(QColor(self.color))
		qp.drawRect(self.cordx - (self.width/2) , self.cordy - (self.height/2) , self.width, self.height)

	def step(self):
		if self.cordx < 400:
			self.cordx += 5

		if self.cordy < 400:
			self.cordy += 5


class Squares(Rectangle):
	"""docstring for Squares"""
	def __init__(self, xcord, ycord):

		super().__init__(xcord, ycord)
		

	def Draw(self, qp):
#squares have the same side length!!!
		pen_color = QPen(QColor(self.color))
		qp.setPen(pen_color)
		qp.setBrush(QColor(self.color))
		qp.drawRect(self.cordx - (self.width/2), self.cordy - (self.width/2), self.width, self.width)

	def step(self):
		if self.cordx < 400:
			self.cordx += 5
		if self.cordy < 400:
			self.cordy += 5

		
class Ellipses(Shapes):

	def __init__(self, xcord, ycord):

		super().__init__(xcord, ycord)
#make sure to take into account the difference in each side
	def Draw(self, qp):

		pen_color = QPen(QColor(self.color))
		qp.setPen(pen_color)
		qp.setBrush(QColor(self.color))
		qp.drawEllipse(self.cordx - (self.width/2), self.cordy - (self.height/2), self.width, self.height)

	def step(self):
		if self.cordx < 400:
			self.cordx += 5
		if self.cordy < 400:
			self.cordy += 5

class Circles(Ellipses):
	"""docstring for Circles"""
	def __init__(self, xcord, ycord):

		super().__init__(xcord, ycord)
	
	def Draw(self, qp):
#like squares, they are equal
		pen_color = QPen(QColor(self.color))
		qp.setPen(pen_color)
		qp.setBrush(QColor(self.color))
		qp.drawEllipse(self.cordx - (self.width/2), self.cordy - (self.width/2), self.width, self.width)

	def step(self):
		if self.cordx < 400:
			self.cordx += 5
		if self.cordy < 400:
			self.cordy += 5
		

class Triangles(Shapes):
	"""docstring for Triangle"""
	def __init__(self, xcord, ycord):

		super().__init__(xcord, ycord)

	def Draw(self, qp):
#3 line segments will allow for a nice triangle
		pen_color = QPen(QColor(self.color))
		qp.setPen(pen_color)
		qp.setBrush(QColor(self.color))
		qp.drawPolygon(QPoint(self.cordx - self.width, self.cordy - (self.height/2)), QPoint(self.cordx, self.cordy + (self.height/2)), QPoint(self.cordx + self.width, self.cordy - (self.height)))

	def step(self):
		if self.cordx < 400:
			self.cordx += 5
		if self.cordy < 400:
			self.cordy += 5
