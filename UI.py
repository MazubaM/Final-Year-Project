from PyQt5 import QtCore, QtGui, QtWidgets
from DBTCS import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(773, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton1.setGeometry(QtCore.QRect(60, 150, 82, 17))
        self.radioButton1.setObjectName("radioButton1")
        self.RadioBtnGroup = QtWidgets.QButtonGroup(MainWindow)
        self.RadioBtnGroup.setObjectName("RadioBtnGroup")
        self.RadioBtnGroup.addButton(self.radioButton1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 180, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.RadioBtnGroup.addButton(self.radioButton_2)
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(310, 320, 131, 41))
        self.Button1.setObjectName("Button1")
        self.Button1.clicked.connect(self.run_execute)
        self.TimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel.setGeometry(QtCore.QRect(50, 120, 121, 31))
        self.TimeLabel.setObjectName("TimeLabel")
        self.DelayLabel = QtWidgets.QLabel(self.centralwidget)
        self.DelayLabel.setGeometry(QtCore.QRect(50, 210, 131, 31))
        self.DelayLabel.setObjectName("DelayLabel")
        self.HeadLabel = QtWidgets.QLabel(self.centralwidget)
        self.HeadLabel.setGeometry(QtCore.QRect(40, 10, 711, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.HeadLabel.setFont(font)
        self.HeadLabel.setObjectName("HeadLabel")
        self.GenLabel = QtWidgets.QLabel(self.centralwidget)
        self.GenLabel.setGeometry(QtCore.QRect(450, 90, 191, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.GenLabel.setFont(font)
        self.GenLabel.setObjectName("GenLabel")
        self.Lane1Label = QtWidgets.QLabel(self.centralwidget)
        self.Lane1Label.setGeometry(QtCore.QRect(390, 130, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Lane1Label.setFont(font)
        self.Lane1Label.setObjectName("Lane1Label")
        self.CarTotlabel = QtWidgets.QLabel(self.centralwidget)
        self.CarTotlabel.setGeometry(QtCore.QRect(390, 250, 61, 16))
        self.CarTotlabel.setObjectName("CarTotlabel")
        self.GenLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.GenLabel_2.setGeometry(QtCore.QRect(40, 80, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.GenLabel_2.setFont(font)
        self.GenLabel_2.setObjectName("GenLabel_2")
        self.Lane1Label_2 = QtWidgets.QLabel(self.centralwidget)
        self.Lane1Label_2.setGeometry(QtCore.QRect(390, 160, 21, 16))
        self.Lane1Label_2.setObjectName("Lane1Label_2")
        self.Lane1Label_3 = QtWidgets.QLabel(self.centralwidget)
        self.Lane1Label_3.setGeometry(QtCore.QRect(390, 190, 21, 16))
        self.Lane1Label_3.setObjectName("Lane1Label_3")
        self.Lane1Label_4 = QtWidgets.QLabel(self.centralwidget)
        self.Lane1Label_4.setGeometry(QtCore.QRect(390, 220, 21, 16))
        self.Lane1Label_4.setObjectName("Lane1Label_4")
        self.Lane1Label1 = QtWidgets.QLabel(self.centralwidget)
        self.Lane1Label1.setGeometry(QtCore.QRect(410, 130, 241, 16))
        self.Lane1Label1.setObjectName("Lane1Label1")
        self.Lane4Label4 = QtWidgets.QLabel(self.centralwidget)
        self.Lane4Label4.setGeometry(QtCore.QRect(410, 220, 331, 16))
        self.Lane4Label4.setObjectName("Lane4Label4")
        self.Lane2Label2 = QtWidgets.QLabel(self.centralwidget)
        self.Lane2Label2.setGeometry(QtCore.QRect(410, 160, 281, 16))
        self.Lane2Label2.setObjectName("Lane2Label2")
        self.Lane3Label3 = QtWidgets.QLabel(self.centralwidget)
        self.Lane3Label3.setGeometry(QtCore.QRect(410, 190, 291, 16))
        self.Lane3Label3.setObjectName("Lane3Label3")
        self.cyctotlabel = QtWidgets.QLabel(self.centralwidget)
        self.cyctotlabel.setGeometry(QtCore.QRect(390, 280, 61, 16))
        self.cyctotlabel.setObjectName("cyctotlabel")
        self.Lane4Label4_2 = QtWidgets.QLabel(self.centralwidget)
        self.Lane4Label4_2.setGeometry(QtCore.QRect(450, 250, 271, 16))
        self.Lane4Label4_2.setObjectName("Lane4Label4_2")
        self.Lane4Label4_3 = QtWidgets.QLabel(self.centralwidget)
        self.Lane4Label4_3.setGeometry(QtCore.QRect(450, 280, 281, 16))
        self.Lane4Label4_3.setObjectName("Lane4Label4_3")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(60, 240, 33, 20))
        self.spinBox.setObjectName("spinBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton1.setText(_translate("MainWindow", "Short Time"))
        self.radioButton1.setChecked(True)
        self.radioButton_2.setText(_translate("MainWindow", "Long Time"))
        self.Button1.setText(_translate("MainWindow", "Calculate"))
        self.TimeLabel.setText(_translate("MainWindow", "Choose Time Variance "))
        self.DelayLabel.setText(_translate("MainWindow", "Choose Delay Time"))
        self.HeadLabel.setText(_translate("MainWindow", "Density Based Traffic Control System"))
        self.GenLabel.setText(_translate("MainWindow", "Generated Queue"))
        self.Lane1Label.setText(_translate("MainWindow", "1.: "))
        self.CarTotlabel.setText(_translate("MainWindow", "Total Cars: "))
        self.GenLabel_2.setText(_translate("MainWindow", "Configurations"))
        self.Lane1Label_2.setText(_translate("MainWindow", "2.: "))
        self.Lane1Label_3.setText(_translate("MainWindow", "3.: "))
        self.Lane1Label_4.setText(_translate("MainWindow", "4.: "))
        self.Lane1Label1.setText(_translate("MainWindow", "First"))
        self.Lane4Label4.setText(_translate("MainWindow", "Fourth"))
        self.Lane2Label2.setText(_translate("MainWindow", "Second "))
        self.Lane3Label3.setText(_translate("MainWindow", "Third"))
        self.cyctotlabel.setText(_translate("MainWindow", "Cycle Time: "))
        self.Lane4Label4_2.setText(_translate("MainWindow", "Car Total"))
        self.Lane4Label4_3.setText(_translate("MainWindow", "Cycle total"))

    def run_execute(self):
        variance = self.radioButton_2.isChecked()
        delay = self.spinBox.value()
        data = execute(delay, variance)
        _translate = QtCore.QCoreApplication.translate
        self.Lane1Label1.setText(_translate("MainWindow", str(data[0])))
        self.Lane2Label2.setText(_translate("MainWindow", str(data[1])))
        self.Lane3Label3.setText(_translate("MainWindow", str(data[2])))
        self.Lane4Label4.setText(_translate("MainWindow", str(data[3])))

        total_time = 0
        total_cars = 0
        
        for i in range(4):
            total_cars += data[i].get("TotalVehicles")
            total_time += data[i].get("Time")


        self.Lane4Label4_2.setText(_translate("MainWindow", str(total_cars)))
        self.Lane4Label4_3.setText(_translate("MainWindow", str(total_time)))
        # print(data[0])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())