import sys, threading, time
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QDialog, QInputDialog, QErrorMessage
import random
from random import randint
from PyQt5.QtCore import QTimer

ROWS = 8
SEATS = 8
CELL_SIZE = 40
GRID_ORIGINX = 50
GRID_ORIGINY = 50

class Memory(QWidget):

	def __init__(self): 
	    super().__init__()
	    self.__number = [['' for i in range(SEATS)] for j in range(ROWS)]
	    self.num_list = list()
	    self.drawNum = [['' for i in range(SEATS)] for j in range(ROWS)]
	    self.setWindowTitle('Memory Game')
	    self.setGeometry(300, 300, 2 * GRID_ORIGINX + CELL_SIZE * SEATS, \
	        3 * GRID_ORIGINY + CELL_SIZE * ROWS)
	    self.Numbers()
	    self.fuse = QTimer()
	    self.fuse.timeout.connect(self.Check)
	    self.button = QPushButton('Clear/New Board', self)
	    self.button.setToolTip('Creating a New Board')
	    self.button.move(0,0)
	    self.button.clicked.connect(self.Clear)
	    self.show()

	def paintEvent(self, event): 
	    qp = QPainter()
	    blackPen = QPen(Qt.black)
	    qp.begin(self)
	    qp.setPen(blackPen)
	    for r in range(ROWS):
	      for c in range(SEATS):
	        qp.drawRect(GRID_ORIGINX + c * CELL_SIZE, GRID_ORIGINY + r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
	        qp.setPen(Qt.red)
	        qp.drawText(GRID_ORIGINX + c * CELL_SIZE + 8, GRID_ORIGINY + r * CELL_SIZE + 25, str(self.drawNum[r][c]))
	        qp.setPen(blackPen)
	    qp.end()

	def Numbers(self):
		for i in range(32):
			num = i**2
			self.num_list.append(num)
			self.num_list.append(num)
		for row in range(ROWS):
			for col in range(SEATS):
				num = self.num_list[randint(0, len(self.num_list)-1)]
				self.__number[row][col] = str(num)
				self.num_list.remove(num)
				self.update()
		return self.__number

	def mousePressEvent(self, event):
		row = (event.y() - GRID_ORIGINY) // CELL_SIZE
		col = (event.x() - GRID_ORIGINX) // CELL_SIZE
		if 0 <= row < ROWS and 0 <= col < SEATS:
			if self.drawNum[row][col] == '':
				if len(self.num_list) < 4: 
					self.drawNum[row][col] = int(self.__number[row][col])
					self.num_list.append(row)
					self.num_list.append(col)
					if len(self.num_list) == 4:
						self.fuse.start(1000)
				self.update() 

	def Check(self):
		self.fuse.stop()
		if len(self.num_list) >= 4:
			if self.drawNum[self.num_list[0]][self.num_list[1]] != self.drawNum[self.num_list[2]][self.num_list[3]]:
				self.drawNum[self.num_list[0]][self.num_list[1]] = ''
				self.drawNum[self.num_list[2]][self.num_list[3]] = ''
				self.num_list.clear()
				self.update()
			else:
				self.num_list.clear()
				self.update()

	def Clear(self):
		self.drawNum = [['' for i in range(SEATS)] for j in range(ROWS)]
		self.Numbers()
		self.num_list.clear()
		self.update()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Memory()
	sys.exit(app.exec_())