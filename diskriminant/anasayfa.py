# This Python file uses the following encoding: utf-8
import sys
import math
from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_anaSayfa

class anaSayfa(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_anaSayfa()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.hesapla)

    def hesapla(self):
        a = int(self.ui.lineEdit_A.text())
        b = int(self.ui.lineEdit_B.text())
        c = int(self.ui.lineEdit_C.text())

        delta=math.sqrt(b*b-4*a*c)
        sonuc1 = (-b+delta) / (2*a)
        sonuc2 = (-b-delta) / (2*a)


        self.ui.label_x1.setText("x= "+str(sonuc1))
        self.ui.label_x2.setText("x= "+str(sonuc2))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = anaSayfa()
    widget.show()
    sys.exit(app.exec())
