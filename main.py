import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 File Manager")
        self.resize(1000, 500)
        self.move(200, 200)
        self.show()

    def mousePressEvent(self, event):
        print("You just clicked on the window.")


app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

window = Window()
app.exec_()
