import sys
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint, QPropertyAnimation
from random import randint
import Shapes

class ShapeDrawer(QWidget):

    def __init__(self):
        super().__init__()
        self.__shapes = list()
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle('Shapes')
        self.show()



    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        #draw the list self.__shapes
        for i in self.__shapes:

            i.Draw(qp)
            
            '''for obj in self.__shapes[0:len(self.__shapes)-1]:
                obj.step()'''


        qp.end()


    def mousePressEvent(self, event):
    #randomly choose a shape to draw
        shapenum = randint(0,4)
        if shapenum == 0:
            #information to draw Rectangle
            rect = Shapes.Rectangle(event.x(), event.y())
            self.__shapes.append(rect)

        elif shapenum == 1:
            #information to draw Squares
            square = Shapes.Squares(event.x(), event.y())
            self.__shapes.append(square)

        elif shapenum == 2:
            #information to draw Ellipse
            elpse = Shapes.Ellipses(event.x(), event.y())
            self.__shapes.append(elpse)

        elif shapenum == 3:
            #information to draw Circle
            circle = Shapes.Circles(event.x(), event.y())
            self.__shapes.append(circle)

        elif shapenum == 4:
            #information to draw Triangle
            tri = Shapes.Triangles(event.x(), event.y())
            self.__shapes.append(tri)


        self.update()

    def keyPressEvent(self, event):
        if event.text().isspace():
            self.__shapes = []
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShapeDrawer()
    sys.exit(app.exec_())
