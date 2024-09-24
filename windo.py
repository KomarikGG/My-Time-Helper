from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui_1 import Ui_MainWindow
from windo_2 import Win_2
from windo_3 import Win_3
from windo_4 import Win_4
from PyQt5.QtCore import QTime,QTimer

class Win_1(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.win_2 = Win_2()
        self.win_3 = Win_3()
        self.win_4 = Win_4()
        timer  = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
        self.update_time()
        self.ui.time_country.clicked.connect(self.show_world_time)
        self.ui.second_time.clicked.connect(self.show_seconder_time)
        self.ui.timer.clicked.connect(self.show_timer_time)
        self.win_2.ui.time_country.clicked.connect(self.back_from_world_time)
        self.win_3.ui.second_time.clicked.connect(self.back_from_seconder)
        self.win_4.ui.timer.clicked.connect(self.back_from_timer)
    def show_world_time(self):
        self.hide()
        self.win_2.show()
    def show_seconder_time(self):
        self.hide()
        self.win_3.show()
    def show_timer_time(self):
        self.hide()
        self.win_4.show()  
    def back_from_world_time(self):
        self.win_2.hide()
        self.show()
    def back_from_seconder(self):
        self.win_3.hide()
        self.show()
    def back_from_timer(self):
        self.win_4.hide()
        self.show()
    def update_time(self):
        current_time = QTime.currentTime()
        text = current_time.toString('hh:mm:ss')
        self.ui.number.setText(text)
app = QApplication([])
ex = Win_1()
ex.show()
app.exec_()
