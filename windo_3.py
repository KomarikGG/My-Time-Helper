from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui_3 import Ui_Form
from PyQt5.QtCore import QTime,QTimer

class Win_3(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1event) 
        self.ui.start.clicked.connect(self.secoundure)
    def secoundure(self):
        if self.ui.start.text() == 'Start':
            self.timer.start(1)
            self.ui.start.setText('Stop')
            self.time = QTime(0,0,0,0)
            self.ui.label.setText(self.time.toString('mm:ss.zzz'))
        else:
            self.timer.stop()
            self.ui.start.setText('Start')
            self.ui.label.setText('00:00.000')
    def timer1event(self):
        self.time = self.time.addMSecs(1)
        self.ui.label.setText(self.time.toString('mm:ss.zzz'))
        