#PyQt5 Introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        #Pass args from QMainWindow
        super().__init__()
        self.button = QPushButton("Submit", self)
        self.label = QLabel("Hello Reina", self)
        self.checkbox = QCheckBox("Do You Like Food?", self)
        self.photo_label = QLabel(self)
        self.line_edit = QLineEdit(self)
        
        #radio
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Giftcard", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("On-Line", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        
        self.initUI()
        
    
    def initUI(self):
        # Mending masukkin init label dll apapapun di __init__ & jadiin self. biar bisa diambil di def lainnya
        self.setWindowTitle("We Gaming Boys")
        self.setGeometry(0,0, 800, 600)
        self.setWindowIcon(QIcon("Tutorial Projects/PyQt5GUI/blow out.png"))

        self.label.setFont(QFont("Arial", 40))
        # self.label.setGeometry(0,0, 800,100)
        self.label.setStyleSheet("color:blue;"
                            "background-color: cyan;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: none;")
        
        # Align Font inside the geometry AlignTop, AlignBottom, AlignHCenter, AlignVCenter, AlignCenter, AlignRight, AlignLeft
        self.label.setAlignment(Qt.AlignCenter)
        
        # self.photo_label.setGeometry(0,100,800,200)
        pixmap = QPixmap("Tutorial Projects/PyQt5GUI/reina-tekken-8.webp")
        self.photo_label.setPixmap(pixmap)
        self.photo_label.setScaledContents(True)
        
        #Buttons
        # self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)
        
        #CheckBox
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        self.checkbox.stateChanged.connect(self.checkbox_changed)

        #RadioButton
        self.setStyleSheet("QRadioButton{"
                           "font-size: 20px;"
                           "font-family: area;"
                           "padding = 5px;"
                           "}")
        
        #ButtonGroup for radiobutton
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)
        
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

        #LineEdit / Textbox goddammit
        self.line_edit.setStyleSheet("font-size: 20px;"
                                     "font-family: Arial;")
        
        #EXAMPLE OF SETSTYLESHEET basically CSS
        
        #selecting individually
        self.button.setObjectName("button")
        
        self.setStyleSheet("""
                           QPushButton{
                               font-size:40px;
                               font-family: Arial;
                               border: 3px solid;
                               border-radius: 15px;
                           }
                           
                           QPushButton#button {
                               background-color: hsl(204, 100%, 64%);
                           }
                           QPushButton#button:hover {
                               background-color: hsl(204, 100%, 74%);
                           }
                           """)
        
        # Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # box layout - auto box
        # QHBoxLayout for horizontal and QVBoxLayout for vertical
        vbox = QVBoxLayout()
        radio_hbox1 = QHBoxLayout()
        radio_hbox2 = QHBoxLayout()
        # vbox.addWidget(self.label)
        # vbox.addWidget(self.photo_label)
        # vbox.addWidget(self.button)
        # vbox.addWidget(self.checkbox)
        radio_hbox1.addWidget(self.radio1)
        radio_hbox1.addWidget(self.radio2)
        radio_hbox1.addWidget(self.radio3)
        radio_hbox2.addWidget(self.radio4)
        radio_hbox2.addWidget(self.radio5)
        
        # grid layout - use rows and columns
        grid = QGridLayout()
        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.photo_label, 1, 0)
        grid.addWidget(self.checkbox, 2, 0)
        grid.addLayout(radio_hbox1, 3, 0)
        grid.addLayout(radio_hbox2, 4, 0)
        grid.addWidget(self.line_edit, 5, 0)
        grid.addWidget(self.button, 6, 0)
        
        # initialize layout kea CSS
        central_widget.setLayout(grid)
    
    def on_click(self):
        text = self.line_edit.text()
        self.button.setText("Clicked!")
        self.button.setDisabled(True)
        self.label.setText(f"Hello {text} 😔")

    def checkbox_changed(self, state):
        # Bisa juga pake if state == Qt.Checked:
        if state:
            print("You Like Food!")
        else:
            print("You do not Like Food!")
    
    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")
            
        
        
def main():
    # sys.argv = process any command line args, but you can also use empty list[]
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    #exec_ = execute method, waits for user input and handle events
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()