from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class main_window(QtWidgets.QWidget):
    
    
    def Label(self):
        layout=QtWidgets.QHBoxLayout()
        layout.addWidget(QtWidgets.QLabel("This is a QLabel"))
        layout.addWidget(QtWidgets.QLabel("This is a Label"))
        return layout

    def LineEdit(self):
        layout=QtWidgets.QHBoxLayout()
        layout.addWidget(QtWidgets.QLabel("This is a QLineEdit"))
        layout.addWidget(QtWidgets.QLineEdit(""))
        return layout

    def TextEdit(self):
        layout=QtWidgets.QHBoxLayout()
        layout.addWidget(QtWidgets.QLabel("This is a QTextEdit"))
        layout.addWidget(QtWidgets.QTextEdit(""))
        return layout

    def PushButton(self):
        layout=QtWidgets.QHBoxLayout()
        layout.addWidget(QtWidgets.QLabel("This is a QPushButton"))
        layout.addWidget(QtWidgets.QPushButton("Botton"))
        return layout

    def RadioButton(self):
        layout=QtWidgets.QHBoxLayout()
        layout.addWidget(QtWidgets.QLabel("This is a QRadioButton"))
        layout.addWidget(QtWidgets.QRadioButton("Item 1"))
        return layout

    def CheckBox(self):
        layout=QtWidgets.QHBoxLayout()
        layout.addWidget(QtWidgets.QLabel("This is a QCheckBox"))
        layout.addWidget(QtWidgets.QCheckBox("Check 1"))
        return layout

    def ComBox(self):
        layout=QtWidgets.QHBoxLayout()
        Combox = QtWidgets.QComboBox()
        Combox.addItems(["1","2","3"])
        layout.addWidget(QtWidgets.QLabel("This is a QComboBox"))
        layout.addWidget(Combox)
        return layout
    
    def SpinBox(self):
        layout = QtWidgets.QHBoxLayout()
        Spinbox=QtWidgets.QSpinBox()
        layout.addWidget(QtWidgets.QLabel("This is a QSpinBox"))
        layout.addWidget(Spinbox)
        return layout
    
    def CalendarWidget(self):    
        layout=QtWidgets.QHBoxLayout()
        Date=QtWidgets.QCalendarWidget()
        layout.addWidget(QtWidgets.QLabel("This is a QCalendarWidget"))
        layout.addWidget(Date)
        return layout

    def Table(self):
        layout=QtWidgets.QHBoxLayout()
        Table=QtWidgets.QTableWidget(1,10)
        layout.addWidget(QtWidgets.QLabel("This is a QTableWidget"))
        layout.addWidget(Table)
        return layout
        
    def Slider(self):    
        layout=QtWidgets.QHBoxLayout()
        Slider=QtWidgets.QSlider(QtCore.Qt.Horizontal)
        layout.addWidget(QtWidgets.QLabel("This is a QSlider"))
        layout.addWidget(Slider)
        return layout

    def ProgressBar(self):         
        layout=QtWidgets.QHBoxLayout()
        ProgressBar=QtWidgets.QProgressBar()
        layout.addWidget(QtWidgets.QLabel("This is a QProgressBar"))
        layout.addWidget(ProgressBar)
        return layout

    def Dial(self):    
        layout=QtWidgets.QHBoxLayout()
        Dial=QtWidgets.QDial()
        layout.addWidget(QtWidgets.QLabel("This is a QDial"))
        layout.addWidget(Dial)
        return layout

    def RadioButtonGroup(self): 
        groupbox=QtWidgets.QGroupBox("This is a QGroupBox example with three QRadioButton")
        gb_lay=QtWidgets.QVBoxLayout()
        gb_lay.addWidget(QtWidgets.QRadioButton("1"))
        gb_lay.addWidget(QtWidgets.QRadioButton("2"))
        gb_lay.addWidget(QtWidgets.QRadioButton("3"))
        groupbox.setLayout(gb_lay)
        return groupbox

    def CheckBoxGroup(self): 
        groupboxCheck=QtWidgets.QGroupBox("This is a QGroupBox example with three QCheckBox")
        gb_lay=QtWidgets.QVBoxLayout()
        gb_lay.addWidget(QtWidgets.QCheckBox("1"))
        gb_lay.addWidget(QtWidgets.QCheckBox("2"))
        gb_lay.addWidget(QtWidgets.QCheckBox("3"))
        groupboxCheck.setLayout(gb_lay)
        return groupboxCheck
        
    def __init__(self):
        super().__init__()
        vlayout =QtWidgets.QVBoxLayout()
        vlayout.addLayout(self.Label())
        vlayout.addLayout(self.LineEdit())
        vlayout.addLayout(self.TextEdit())
        vlayout.addLayout(self.PushButton())
        vlayout.addLayout(self.RadioButton())
        vlayout.addLayout(self.CheckBox())
        vlayout.addLayout(self.ComBox())
        vlayout.addLayout(self.SpinBox())
        vlayout.addLayout(self.CalendarWidget())
        vlayout.addLayout(self.Table())
        vlayout.addLayout(self.Slider())
        vlayout.addLayout(self.ProgressBar())
        vlayout.addLayout(self.Dial())
        vlayout.addWidget(self.RadioButtonGroup())
        vlayout.addWidget(self.CheckBoxGroup())
        self.setGeometry(100,100,100,50)
        self.resize(415,300)
        self.setLayout(vlayout)
        
        
if __name__ =="__main__":

    app=QtWidgets.QApplication([])
    window=main_window()
    window.show()
    sys.exit(app.exec_())