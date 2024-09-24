from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui_4 import Ui_Form
from PyQt5.QtCore import QTime,QTimer,QUrl
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent

class Win_4(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_timer)
        self.ui.pushButton_2.clicked.connect(self.stop)
        self.player = QMediaPlayer()
    def timer1Event(self):
        self.time = self.time.addSecs(-1)
        self.ui.label.setText(self.time.toString('hh:mm:ss'))
        if self.time.secsTo(QTime(0,0,0)) == 0:
            self.timer.stop()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile('microwave-timer-117077.mp3')))
            self.player.play()
    def stop(self):
        try:
            self.timer.stop()
        except:
            pass
    def start_timer(self):
        self.data = self.ui.lineEdit.text().split(':')
        print(self.data)
        try:
            self.time = QTime(int(self.data[0]),int(self.data[1]),int(self.data[2]))
            self.timer  = QTimer()
            self.timer.timeout.connect(self.timer1Event)
            self.timer.start(1000)
            self.ui.label.setText(self.time.toString('hh:mm:ss'))
        except:
            mb = QMessageBox()
            mb.setStyleSheet('font-weight: bold;font-size:15')
            mb.setText('Please enter the data in the format hh:mm:ss')
            mb.exec_()
        self.ui.lineEdit.clear()