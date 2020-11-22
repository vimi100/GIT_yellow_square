import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPainter, QPixmap, QColor, QBrush, QPen
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.change)
        self.painter = QPainter(self)
        self.value = 0.5
        self.flag = False

    def paintEvent(self, event):
        if self.flag:
            x = random.randint(10, 400)
            y = random.randint(10, 400)
            z = random.randint(10, 100)
            self.painter.begin(self)
            self.pen = QPen(Qt.gray, 2)
            self.painter.setPen(self.pen)
            self.painter.setBrush(QBrush(Qt.yellow))
            self.painter.drawEllipse(x, y, z, z)
            self.painter.end()

    def change(self):
        self.flag = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
