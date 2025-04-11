import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTextEdit
from PyQt5.QtCore import QTimer, Qt, QTime
from PyQt5.QtGui import QFont, QFontDatabase

class SpeedrunTimer(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("00:00:00.00", self)
        self.split_times = QTextEdit(self)
        self.split_times.setReadOnly(True)
        self.split_times.setFocusPolicy(Qt.NoFocus)
        self.timer = QTimer(self)
        self.time = QTime(0,0,0,0)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self._mouse_pos = None
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Speedrun Timer")
        self.setGeometry(500,500, 300,100)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.split_times)
        
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignJustify)
        
        self.time_label.setStyleSheet("font-size: 100px;"
                                      "color: hsl(111, 100%, 50%);")
        self.split_times.setStyleSheet("font-size: 50px;"
                                      "color: hsl(0, 0%, 100%);")
        self.setStyleSheet("background-color: black;")
        
        fontid = QFontDatabase.addApplicationFont("Tutorial Projects\PyQt5GUI\DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(fontid)[0]
        my_font = QFont(font_family, 100)
        self.time_label.setFont(my_font)
        
        # start timer - INACTIVE FIRST
        # self.timer.start(10)
        
        self.timer.timeout.connect(self.update_time)
        
    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
        
        
    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._mouse_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._mouse_pos and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self._mouse_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._mouse_pos = None

    def keyPressEvent(self, event):
        # Close Event
        if event.key() == Qt.Key_Escape:
            self.close()
        # Split Event
        if event.key() == Qt.Key_F:
            if self.timer.isActive():
                split_time = self.format_time(self.time)
                self.split_times.append(split_time)
        # Reset Event
        if event.key() == Qt.Key_R:
            self.time = QTime(0,0,0,0)
            self.time_label.setText(self.format_time(self.time))
            self.split_times.clear()
            self.timer.stop()
            self.time_label.setStyleSheet("font-size: 100px;""color: hsl(111, 100%, 50%);")
        # Start/Pause Event
        if event.key() == Qt.Key_Space:
            if self.timer.isActive():
                self.timer.stop()
                self.time_label.setStyleSheet("font-size: 100px;""color: hsl(111, 100%, 30%);")
            else:
                self.timer.start(10)
                self.time_label.setStyleSheet("font-size: 100px;""color: hsl(111, 100%, 50%);")
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    speedrun_timer = SpeedrunTimer()
    speedrun_timer.show()
    sys.exit(app.exec_())