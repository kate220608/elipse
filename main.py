import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_elipse(qp)
            qp.end()

    def draw_elipse(self, qp):
        n = random.randrange(0, 100)
        for i in range(n):
            qp.setBrush(QColor(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)))
            d = random.randrange(0, 200)
            y = random.randrange(0, 600)
            x = random.randrange(0, 800)
            qp.drawEllipse(x, y, d, d)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
