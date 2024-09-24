from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui_2 import Ui_Form
from PyQt5.QtCore import QTime,QTimer

class Win_2(QMainWindow):
    def   __init__(self):
        global current_time
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        current_time = QTime.currentTime()
        current_time = current_time.addSecs(-2*3600)
        self.ui.spinBox.valueChanged.connect(self.on_value_changed)
        timer  = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
        self.update_time()
    def show_world_time(self):
        self.hide()
        self.win_2 = Win_2()
        self.win_2.show()
    def update_time(self):
        global  current_time
        current_time = current_time.addSecs(1)
        text = current_time.toString('hh:mm')
        self.ui.number.setText(text)
    def on_value_changed(self,value):
        global  current_time
        current_time = QTime.currentTime()
        current_time = current_time.addSecs(-2*3600)
        current_time = current_time.addSecs(value*3600)
        text = current_time.toString('hh:mm')
        self.ui.number.setText(text)
        