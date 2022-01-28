from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        MainWindow.setWindowTitle("Loopster")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleBar = QtWidgets.QWidget(self.centralwidget)
        self.titleBar.setGeometry(QtCore.QRect(0, 0, 640, 31))
        self.titleBar.setStyleSheet("background-color: rgb(18, 18, 18);")
        self.titleBar.setObjectName("titleBar")
        self.quitButton = QtWidgets.QPushButton(self.titleBar)
        self.quitButton.setGeometry(QtCore.QRect(609, -1, 32, 33))
        self.quitButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(18, 18, 18);\n"
"    border: none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(34, 34, 34);\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(39, 39, 39);\n"
"    border: none;\n"
"}")
        self.quitButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/CloseButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quitButton.setIcon(icon)
        self.quitButton.setObjectName("quitButton")
        self.miniButton = QtWidgets.QPushButton(self.titleBar)
        self.miniButton.setGeometry(QtCore.QRect(577, -1, 32, 33))
        self.miniButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(18, 18, 18);\n"
"    border: none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(34, 34, 34);\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(39, 39, 39);\n"
"    border: none;\n"
"}")
        self.miniButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/MiniButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.miniButton.setIcon(icon1)
        self.miniButton.setObjectName("miniButton")
        self.mainBody = QtWidgets.QWidget(self.centralwidget)
        self.mainBody.setGeometry(QtCore.QRect(0, 30, 641, 481))
        self.mainBody.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.mainBody.setObjectName("mainBody")
        self.header = QtWidgets.QWidget(self.mainBody)
        self.header.setGeometry(QtCore.QRect(0, 0, 641, 80))
        self.header.setStyleSheet("background-color: rgb(50, 63, 75);")
        self.header.setObjectName("header")
        self.lblogo = QtWidgets.QLabel(self.header)
        self.lblogo.setGeometry(QtCore.QRect(10, 10, 311, 61))
        self.lblogo.setText("")
        self.lblogo.setPixmap(QtGui.QPixmap("assets/logowhite.png"))
        self.lblogo.setScaledContents(True)
        self.lblogo.setObjectName("lblogo")
        self.footer = QtWidgets.QWidget(self.mainBody)
        self.footer.setGeometry(QtCore.QRect(0, 419, 641, 31))
        self.footer.setStyleSheet("background-color: rgb(50, 63, 75);")
        self.footer.setObjectName("footer")
        self.lblcred = QtWidgets.QLabel(self.footer)
        self.lblcred.setGeometry(QtCore.QRect(10, 0, 621, 31))
        self.lblcred.setStyleSheet("font: 75 10pt \"Orbitron\";\n"
"color: rgb(123, 135, 148);")
        self.lblcred.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblcred.setObjectName("lblcred")
        self.step = QtWidgets.QWidget(self.mainBody)
        self.step.setGeometry(QtCore.QRect(0, 80, 641, 41))
        self.step.setStyleSheet("background-color: rgb(31, 41, 51);")
        self.step.setObjectName("step")
        self.lblstep = QtWidgets.QLabel(self.step)
        self.lblstep.setGeometry(QtCore.QRect(10, 0, 631, 41))
        self.lblstep.setStyleSheet("font: 75 12pt \"Orbitron\";\n"
"color: rgb(123, 135, 148);")
        self.lblstep.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblstep.setObjectName("lblstep")
        self.l_shad_2 = QtWidgets.QFrame(self.step)
        self.l_shad_2.setGeometry(QtCore.QRect(-1, 32, 642, 16))
        self.l_shad_2.setStyleSheet("color: rgb(26, 26, 26);")
        self.l_shad_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.l_shad_2.setLineWidth(2)
        self.l_shad_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.l_shad_2.setObjectName("l_shad_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainBody)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 121, 641, 291))
        self.stackedWidget.setObjectName("stackedWidget")
        self.getStarted = QtWidgets.QWidget()
        self.getStarted.setObjectName("getStarted")
        self.startButton = QtWidgets.QPushButton(self.getStarted)
        self.startButton.setGeometry(QtCore.QRect(80, 80, 481, 131))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    border-radius: 8px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.startButton.setObjectName("startButton")
        self.stackedWidget.addWidget(self.getStarted)
        self.step1 = QtWidgets.QWidget()
        self.step1.setObjectName("step1")
        self.prog1 = QtWidgets.QPushButton(self.step1)
        self.prog1.setGeometry(QtCore.QRect(80, 20, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.prog1.setFont(font)
        self.prog1.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    border-radius: 8px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.prog1.setObjectName("prog1")
        self.prog2 = QtWidgets.QPushButton(self.step1)
        self.prog2.setGeometry(QtCore.QRect(80, 120, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.prog2.setFont(font)
        self.prog2.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    border-radius: 8px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.prog2.setObjectName("prog2")
        self.prog3 = QtWidgets.QPushButton(self.step1)
        self.prog3.setGeometry(QtCore.QRect(80, 220, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.prog3.setFont(font)
        self.prog3.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    border-radius: 8px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.prog3.setObjectName("prog3")
        self.stackedWidget.addWidget(self.step1)
        self.step2 = QtWidgets.QWidget()
        self.step2.setObjectName("step2")
        self.bck1 = QtWidgets.QPushButton(self.step2)
        self.bck1.setGeometry(QtCore.QRect(160, 240, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.bck1.setFont(font)
        self.bck1.setStyleSheet("QPushButton{\n"
"    background-color: rgb(230, 168, 106);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(208, 122, 36);\n"
"    border-radius: 8px;\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(234, 182, 130);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(208, 122, 36);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(220, 139, 58);\n"
"    border: none;\n"
"    border-top: 2px solid rgb(208, 122, 36);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.bck1.setObjectName("bck1")
        self.nxt1 = QtWidgets.QPushButton(self.step2)
        self.nxt1.setGeometry(QtCore.QRect(330, 240, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.nxt1.setFont(font)
        self.nxt1.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    border-radius: 8px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.nxt1.setObjectName("nxt1")
        self.rBod_s2 = QtWidgets.QWidget(self.step2)
        self.rBod_s2.setGeometry(QtCore.QRect(80, 10, 481, 211))
        self.rBod_s2.setStyleSheet("background-color: rgb(31, 41, 51);")
        self.rBod_s2.setObjectName("rBod_s2")
        self.l_shad = QtWidgets.QFrame(self.rBod_s2)
        self.l_shad.setGeometry(QtCore.QRect(0, 200, 481, 20))
        self.l_shad.setStyleSheet("color: rgb(26, 26, 26);")
        self.l_shad.setFrameShadow(QtWidgets.QFrame.Plain)
        self.l_shad.setLineWidth(2)
        self.l_shad.setFrameShape(QtWidgets.QFrame.HLine)
        self.l_shad.setObjectName("l_shad")
        self.rb1_s2 = QtWidgets.QRadioButton(self.rBod_s2)
        self.rb1_s2.setGeometry(QtCore.QRect(17, 10, 24, 24))
        self.rb1_s2.setStyleSheet("QRadioButton::indicator::unchecked{\n"
"image: url(:/newPrefix/rbUnselected.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image: url(:/newPrefix/rbSelected.png);\n"
"}")
        self.rb1_s2.setText("")
        self.rb1_s2.setObjectName("rb1_s2")
        self.rb2_s2 = QtWidgets.QRadioButton(self.rBod_s2)
        self.rb2_s2.setGeometry(QtCore.QRect(17, 63, 24, 24))
        self.rb2_s2.setStyleSheet("QRadioButton::indicator::unchecked{\n"
"image: url(:/newPrefix/rbUnselected.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image: url(:/newPrefix/rbSelected.png);\n"
"}")
        self.rb2_s2.setText("")
        self.rb2_s2.setObjectName("rb2_s2")
        self.rb3_s2 = QtWidgets.QRadioButton(self.rBod_s2)
        self.rb3_s2.setGeometry(QtCore.QRect(17, 117, 24, 24))
        self.rb3_s2.setStyleSheet("QRadioButton::indicator::unchecked{\n"
"image: url(:/newPrefix/rbUnselected.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image: url(:/newPrefix/rbSelected.png);\n"
"}")
        self.rb3_s2.setText("")
        self.rb3_s2.setObjectName("rb3_s2")
        self.rb4_s2 = QtWidgets.QRadioButton(self.rBod_s2)
        self.rb4_s2.setGeometry(QtCore.QRect(17, 170, 24, 24))
        self.rb4_s2.setStyleSheet("QRadioButton::indicator::unchecked{\n"
"image: url(:/newPrefix/rbUnselected.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image: url(:/newPrefix/rbSelected.png);\n"
"}")
        self.rb4_s2.setText("")
        self.rb4_s2.setObjectName("rb4_s2")
        self.l1_s2 = QtWidgets.QLabel(self.rBod_s2)
        self.l1_s2.setGeometry(QtCore.QRect(50, 10, 381, 24))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l1_s2.setFont(font)
        self.l1_s2.setAlignment(QtCore.Qt.AlignCenter)
        self.l1_s2.setObjectName("l1_s2")
        self.l2_s2 = QtWidgets.QLabel(self.rBod_s2)
        self.l2_s2.setGeometry(QtCore.QRect(50, 63, 381, 24))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l2_s2.setFont(font)
        self.l2_s2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2_s2.setObjectName("l2_s2")
        self.l3_s2 = QtWidgets.QLabel(self.rBod_s2)
        self.l3_s2.setGeometry(QtCore.QRect(50, 117, 381, 24))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l3_s2.setFont(font)
        self.l3_s2.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_s2.setObjectName("l3_s2")
        self.l4_s2 = QtWidgets.QLabel(self.rBod_s2)
        self.l4_s2.setGeometry(QtCore.QRect(50, 170, 381, 24))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l4_s2.setFont(font)
        self.l4_s2.setAlignment(QtCore.Qt.AlignCenter)
        self.l4_s2.setObjectName("l4_s2")
        self.p1_s2 = QtWidgets.QPushButton(self.rBod_s2)
        self.p1_s2.setGeometry(QtCore.QRect(440, 10, 24, 24))
        self.p1_s2.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    border-radius: 4px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.p1_s2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p1_s2.setIcon(icon2)
        self.p1_s2.setObjectName("p1_s2")
        self.p2_s2 = QtWidgets.QPushButton(self.rBod_s2)
        self.p2_s2.setGeometry(QtCore.QRect(440, 63, 24, 24))
        self.p2_s2.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    border-radius: 4px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.p2_s2.setText("")
        self.p2_s2.setIcon(icon2)
        self.p2_s2.setObjectName("p2_s2")
        self.p3_s2 = QtWidgets.QPushButton(self.rBod_s2)
        self.p3_s2.setGeometry(QtCore.QRect(440, 117, 24, 24))
        self.p3_s2.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    border-radius: 4px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.p3_s2.setText("")
        self.p3_s2.setIcon(icon2)
        self.p3_s2.setObjectName("p3_s2")
        self.p4_s2 = QtWidgets.QPushButton(self.rBod_s2)
        self.p4_s2.setGeometry(QtCore.QRect(440, 170, 24, 24))
        self.p4_s2.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    border-radius: 4px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.p4_s2.setText("")
        self.p4_s2.setIcon(icon2)
        self.p4_s2.setObjectName("p4_s2")
        self.stackedWidget.addWidget(self.step2)
        self.step3 = QtWidgets.QWidget()
        self.step3.setObjectName("step3")
        self.nxt2 = QtWidgets.QPushButton(self.step3)
        self.nxt2.setGeometry(QtCore.QRect(330, 240, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.nxt2.setFont(font)
        self.nxt2.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    border-radius: 8px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.nxt2.setObjectName("nxt2")
        self.bck2 = QtWidgets.QPushButton(self.step3)
        self.bck2.setGeometry(QtCore.QRect(160, 240, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.bck2.setFont(font)
        self.bck2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(230, 168, 106);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(208, 122, 36);\n"
"    border-radius: 8px;\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(234, 182, 130);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(208, 122, 36);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(220, 139, 58);\n"
"    border: none;\n"
"    border-top: 2px solid rgb(208, 122, 36);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.bck2.setObjectName("bck2")
        self.rBod_s3 = QtWidgets.QWidget(self.step3)
        self.rBod_s3.setGeometry(QtCore.QRect(80, 10, 481, 211))
        self.rBod_s3.setStyleSheet("background-color: rgb(31, 41, 51);")
        self.rBod_s3.setObjectName("rBod_s3")
        self.l_shad_4 = QtWidgets.QFrame(self.rBod_s3)
        self.l_shad_4.setGeometry(QtCore.QRect(0, 200, 481, 20))
        self.l_shad_4.setStyleSheet("color: rgb(26, 26, 26);")
        self.l_shad_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.l_shad_4.setLineWidth(2)
        self.l_shad_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.l_shad_4.setObjectName("l_shad_4")
        self.rb1_s3 = QtWidgets.QRadioButton(self.rBod_s3)
        self.rb1_s3.setGeometry(QtCore.QRect(17, 10, 24, 24))
        self.rb1_s3.setStyleSheet("QRadioButton::indicator::unchecked{\n"
"image: url(:/newPrefix/rbUnselected.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image: url(:/newPrefix/rbSelected.png);\n"
"}")
        self.rb1_s3.setText("")
        self.rb1_s3.setObjectName("rb1_s3")
        self.rb2_s3 = QtWidgets.QRadioButton(self.rBod_s3)
        self.rb2_s3.setGeometry(QtCore.QRect(17, 63, 24, 24))
        self.rb2_s3.setStyleSheet("QRadioButton::indicator::unchecked{\n"
"image: url(:/newPrefix/rbUnselected.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image: url(:/newPrefix/rbSelected.png);\n"
"}")
        self.rb2_s3.setText("")
        self.rb2_s3.setObjectName("rb2_s3")
        self.rb3_s3 = QtWidgets.QRadioButton(self.rBod_s3)
        self.rb3_s3.setGeometry(QtCore.QRect(17, 117, 24, 24))
        self.rb3_s3.setStyleSheet("QRadioButton::indicator::unchecked{\n"
"image: url(:/newPrefix/rbUnselected.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image: url(:/newPrefix/rbSelected.png);\n"
"}")
        self.rb3_s3.setText("")
        self.rb3_s3.setObjectName("rb3_s3")
        self.rb4_s3 = QtWidgets.QRadioButton(self.rBod_s3)
        self.rb4_s3.setGeometry(QtCore.QRect(17, 170, 24, 24))
        self.rb4_s3.setStyleSheet("QRadioButton::indicator::unchecked{\n"
"image: url(:/newPrefix/rbUnselected.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image: url(:/newPrefix/rbSelected.png);\n"
"}")
        self.rb4_s3.setText("")
        self.rb4_s3.setObjectName("rb4_s3")
        self.l1_s3 = QtWidgets.QLabel(self.rBod_s3)
        self.l1_s3.setGeometry(QtCore.QRect(50, 10, 381, 24))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l1_s3.setFont(font)
        self.l1_s3.setAlignment(QtCore.Qt.AlignCenter)
        self.l1_s3.setObjectName("l1_s3")
        self.l2_s3 = QtWidgets.QLabel(self.rBod_s3)
        self.l2_s3.setGeometry(QtCore.QRect(50, 63, 381, 24))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l2_s3.setFont(font)
        self.l2_s3.setAlignment(QtCore.Qt.AlignCenter)
        self.l2_s3.setObjectName("l2_s3")
        self.l3_s3 = QtWidgets.QLabel(self.rBod_s3)
        self.l3_s3.setGeometry(QtCore.QRect(50, 117, 381, 24))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l3_s3.setFont(font)
        self.l3_s3.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_s3.setObjectName("l3_s3")
        self.l4_s3 = QtWidgets.QLabel(self.rBod_s3)
        self.l4_s3.setGeometry(QtCore.QRect(50, 170, 381, 24))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l4_s3.setFont(font)
        self.l4_s3.setAlignment(QtCore.Qt.AlignCenter)
        self.l4_s3.setObjectName("l4_s3")
        self.p1_s3 = QtWidgets.QPushButton(self.rBod_s3)
        self.p1_s3.setGeometry(QtCore.QRect(440, 10, 24, 24))
        self.p1_s3.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    border-radius: 4px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.p1_s3.setText("")
        self.p1_s3.setIcon(icon2)
        self.p1_s3.setObjectName("p1_s3")
        self.p2_s3 = QtWidgets.QPushButton(self.rBod_s3)
        self.p2_s3.setGeometry(QtCore.QRect(440, 63, 24, 24))
        self.p2_s3.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    border-radius: 4px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.p2_s3.setText("")
        self.p2_s3.setIcon(icon2)
        self.p2_s3.setObjectName("p2_s3")
        self.p3_s3 = QtWidgets.QPushButton(self.rBod_s3)
        self.p3_s3.setGeometry(QtCore.QRect(440, 117, 24, 24))
        self.p3_s3.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    border-radius: 4px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.p3_s3.setText("")
        self.p3_s3.setIcon(icon2)
        self.p3_s3.setObjectName("p3_s3")
        self.p4_s3 = QtWidgets.QPushButton(self.rBod_s3)
        self.p4_s3.setGeometry(QtCore.QRect(440, 170, 24, 24))
        self.p4_s3.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    border-radius: 4px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.p4_s3.setText("")
        self.p4_s3.setIcon(icon2)
        self.p4_s3.setObjectName("p4_s3")
        self.stackedWidget.addWidget(self.step3)
        self.step4 = QtWidgets.QWidget()
        self.step4.setObjectName("step4")
        self.nxt3 = QtWidgets.QPushButton(self.step4)
        self.nxt3.setGeometry(QtCore.QRect(330, 240, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.nxt3.setFont(font)
        self.nxt3.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    border-radius: 8px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.nxt3.setObjectName("nxt3")
        self.bck3 = QtWidgets.QPushButton(self.step4)
        self.bck3.setGeometry(QtCore.QRect(160, 240, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.bck3.setFont(font)
        self.bck3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(230, 168, 106);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(208, 122, 36);\n"
"    border-radius: 8px;\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(234, 182, 130);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(208, 122, 36);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(220, 139, 58);\n"
"    border: none;\n"
"    border-top: 2px solid rgb(208, 122, 36);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.bck3.setObjectName("bck3")
        self.rBod_s4 = QtWidgets.QWidget(self.step4)
        self.rBod_s4.setGeometry(QtCore.QRect(80, 10, 481, 211))
        self.rBod_s4.setStyleSheet("background-color: rgb(31, 41, 51);")
        self.rBod_s4.setObjectName("rBod_s4")
        self.l_shad_5 = QtWidgets.QFrame(self.rBod_s4)
        self.l_shad_5.setGeometry(QtCore.QRect(0, 200, 481, 20))
        self.l_shad_5.setStyleSheet("color: rgb(26, 26, 26);")
        self.l_shad_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.l_shad_5.setLineWidth(2)
        self.l_shad_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.l_shad_5.setObjectName("l_shad_5")
        self.rb1_s4 = QtWidgets.QRadioButton(self.rBod_s4)
        self.rb1_s4.setGeometry(QtCore.QRect(17, 10, 24, 24))
        self.rb1_s4.setStyleSheet("QRadioButton::indicator::unchecked{\n"
"image: url(:/newPrefix/rbUnselected.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image: url(:/newPrefix/rbSelected.png);\n"
"}")
        self.rb1_s4.setText("")
        self.rb1_s4.setObjectName("rb1_s4")
        self.rb2_s4 = QtWidgets.QRadioButton(self.rBod_s4)
        self.rb2_s4.setGeometry(QtCore.QRect(17, 63, 24, 24))
        self.rb2_s4.setStyleSheet("QRadioButton::indicator::unchecked{\n"
"image: url(:/newPrefix/rbUnselected.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image: url(:/newPrefix/rbSelected.png);\n"
"}")
        self.rb2_s4.setText("")
        self.rb2_s4.setObjectName("rb2_s4")
        self.rb3_s4 = QtWidgets.QRadioButton(self.rBod_s4)
        self.rb3_s4.setGeometry(QtCore.QRect(17, 117, 24, 24))
        self.rb3_s4.setStyleSheet("QRadioButton::indicator::unchecked{\n"
"image: url(:/newPrefix/rbUnselected.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image: url(:/newPrefix/rbSelected.png);\n"
"}")
        self.rb3_s4.setText("")
        self.rb3_s4.setObjectName("rb3_s4")
        self.rb4_s4 = QtWidgets.QRadioButton(self.rBod_s4)
        self.rb4_s4.setGeometry(QtCore.QRect(17, 170, 24, 24))
        self.rb4_s4.setStyleSheet("QRadioButton::indicator::unchecked{\n"
"image: url(:/newPrefix/rbUnselected.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image: url(:/newPrefix/rbSelected.png);\n"
"}")
        self.rb4_s4.setText("")
        self.rb4_s4.setObjectName("rb4_s4")
        self.l1_s4 = QtWidgets.QLabel(self.rBod_s4)
        self.l1_s4.setGeometry(QtCore.QRect(50, 10, 381, 24))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l1_s4.setFont(font)
        self.l1_s4.setAlignment(QtCore.Qt.AlignCenter)
        self.l1_s4.setObjectName("l1_s4")
        self.l2_s4 = QtWidgets.QLabel(self.rBod_s4)
        self.l2_s4.setGeometry(QtCore.QRect(50, 63, 381, 24))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l2_s4.setFont(font)
        self.l2_s4.setAlignment(QtCore.Qt.AlignCenter)
        self.l2_s4.setObjectName("l2_s4")
        self.l3_s4 = QtWidgets.QLabel(self.rBod_s4)
        self.l3_s4.setGeometry(QtCore.QRect(50, 117, 381, 24))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l3_s4.setFont(font)
        self.l3_s4.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_s4.setObjectName("l3_s4")
        self.l4_s4 = QtWidgets.QLabel(self.rBod_s4)
        self.l4_s4.setGeometry(QtCore.QRect(50, 170, 381, 24))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l4_s4.setFont(font)
        self.l4_s4.setAlignment(QtCore.Qt.AlignCenter)
        self.l4_s4.setObjectName("l4_s4")
        self.p1_s4 = QtWidgets.QPushButton(self.rBod_s4)
        self.p1_s4.setGeometry(QtCore.QRect(440, 10, 24, 24))
        self.p1_s4.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    border-radius: 4px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.p1_s4.setText("")
        self.p1_s4.setIcon(icon2)
        self.p1_s4.setObjectName("p1_s4")
        self.p2_s4 = QtWidgets.QPushButton(self.rBod_s4)
        self.p2_s4.setGeometry(QtCore.QRect(440, 63, 24, 24))
        self.p2_s4.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    border-radius: 4px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.p2_s4.setText("")
        self.p2_s4.setIcon(icon2)
        self.p2_s4.setObjectName("p2_s4")
        self.p3_s4 = QtWidgets.QPushButton(self.rBod_s4)
        self.p3_s4.setGeometry(QtCore.QRect(440, 117, 24, 24))
        self.p3_s4.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    border-radius: 4px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.p3_s4.setText("")
        self.p3_s4.setIcon(icon2)
        self.p3_s4.setObjectName("p3_s4")
        self.p4_s4 = QtWidgets.QPushButton(self.rBod_s4)
        self.p4_s4.setGeometry(QtCore.QRect(440, 170, 24, 24))
        self.p4_s4.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    border-radius: 4px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.p4_s4.setText("")
        self.p4_s4.setIcon(icon2)
        self.p4_s4.setObjectName("p4_s4")
        self.stackedWidget.addWidget(self.step4)
        self.step5 = QtWidgets.QWidget()
        self.step5.setObjectName("step5")
        self.nxt4 = QtWidgets.QPushButton(self.step5)
        self.nxt4.setGeometry(QtCore.QRect(330, 240, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.nxt4.setFont(font)
        self.nxt4.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    border-radius: 8px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.nxt4.setObjectName("nxt4")
        self.bck4 = QtWidgets.QPushButton(self.step5)
        self.bck4.setGeometry(QtCore.QRect(160, 240, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.bck4.setFont(font)
        self.bck4.setStyleSheet("QPushButton{\n"
"    background-color: rgb(230, 168, 106);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(208, 122, 36);\n"
"    border-radius: 8px;\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(234, 182, 130);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(208, 122, 36);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(220, 139, 58);\n"
"    border: none;\n"
"    border-top: 2px solid rgb(208, 122, 36);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.bck4.setObjectName("bck4")
        self.rBod_s5 = QtWidgets.QWidget(self.step5)
        self.rBod_s5.setGeometry(QtCore.QRect(80, 10, 481, 211))
        self.rBod_s5.setStyleSheet("background-color: rgb(31, 41, 51);")
        self.rBod_s5.setObjectName("rBod_s5")
        self.l_shad_6 = QtWidgets.QFrame(self.rBod_s5)
        self.l_shad_6.setGeometry(QtCore.QRect(0, 200, 481, 20))
        self.l_shad_6.setStyleSheet("color: rgb(26, 26, 26);")
        self.l_shad_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.l_shad_6.setLineWidth(2)
        self.l_shad_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.l_shad_6.setObjectName("l_shad_6")
        self.rb1_s5 = QtWidgets.QRadioButton(self.rBod_s5)
        self.rb1_s5.setGeometry(QtCore.QRect(17, 10, 24, 24))
        self.rb1_s5.setStyleSheet("QRadioButton::indicator::unchecked{\n"
"image: url(:/newPrefix/rbUnselected.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image: url(:/newPrefix/rbSelected.png);\n"
"}")
        self.rb1_s5.setText("")
        self.rb1_s5.setObjectName("rb1_s5")
        self.rb2_s5 = QtWidgets.QRadioButton(self.rBod_s5)
        self.rb2_s5.setGeometry(QtCore.QRect(17, 63, 24, 24))
        self.rb2_s5.setStyleSheet("QRadioButton::indicator::unchecked{\n"
"image: url(:/newPrefix/rbUnselected.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image: url(:/newPrefix/rbSelected.png);\n"
"}")
        self.rb2_s5.setText("")
        self.rb2_s5.setObjectName("rb2_s5")
        self.rb3_s5 = QtWidgets.QRadioButton(self.rBod_s5)
        self.rb3_s5.setGeometry(QtCore.QRect(17, 117, 24, 24))
        self.rb3_s5.setStyleSheet("QRadioButton::indicator::unchecked{\n"
"image: url(:/newPrefix/rbUnselected.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image: url(:/newPrefix/rbSelected.png);\n"
"}")
        self.rb3_s5.setText("")
        self.rb3_s5.setObjectName("rb3_s5")
        self.rb4_s5 = QtWidgets.QRadioButton(self.rBod_s5)
        self.rb4_s5.setGeometry(QtCore.QRect(17, 170, 24, 24))
        self.rb4_s5.setStyleSheet("QRadioButton::indicator::unchecked{\n"
"image: url(:/newPrefix/rbUnselected.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image: url(:/newPrefix/rbSelected.png);\n"
"}")
        self.rb4_s5.setText("")
        self.rb4_s5.setObjectName("rb4_s5")
        self.l1_s5 = QtWidgets.QLabel(self.rBod_s5)
        self.l1_s5.setGeometry(QtCore.QRect(50, 10, 381, 24))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l1_s5.setFont(font)
        self.l1_s5.setAlignment(QtCore.Qt.AlignCenter)
        self.l1_s5.setObjectName("l1_s5")
        self.l2_s5 = QtWidgets.QLabel(self.rBod_s5)
        self.l2_s5.setGeometry(QtCore.QRect(50, 63, 381, 24))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l2_s5.setFont(font)
        self.l2_s5.setAlignment(QtCore.Qt.AlignCenter)
        self.l2_s5.setObjectName("l2_s5")
        self.l3_s5 = QtWidgets.QLabel(self.rBod_s5)
        self.l3_s5.setGeometry(QtCore.QRect(50, 117, 381, 24))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l3_s5.setFont(font)
        self.l3_s5.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_s5.setObjectName("l3_s5")
        self.l4_s5 = QtWidgets.QLabel(self.rBod_s5)
        self.l4_s5.setGeometry(QtCore.QRect(50, 170, 381, 24))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l4_s5.setFont(font)
        self.l4_s5.setAlignment(QtCore.Qt.AlignCenter)
        self.l4_s5.setObjectName("l4_s5")
        self.p1_s5 = QtWidgets.QPushButton(self.rBod_s5)
        self.p1_s5.setGeometry(QtCore.QRect(440, 10, 24, 24))
        self.p1_s5.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    border-radius: 4px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.p1_s5.setText("")
        self.p1_s5.setIcon(icon2)
        self.p1_s5.setObjectName("p1_s5")
        self.p2_s5 = QtWidgets.QPushButton(self.rBod_s5)
        self.p2_s5.setGeometry(QtCore.QRect(440, 63, 24, 24))
        self.p2_s5.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    border-radius: 4px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.p2_s5.setText("")
        self.p2_s5.setIcon(icon2)
        self.p2_s5.setObjectName("p2_s5")
        self.p3_s5 = QtWidgets.QPushButton(self.rBod_s5)
        self.p3_s5.setGeometry(QtCore.QRect(440, 117, 24, 24))
        self.p3_s5.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    border-radius: 4px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.p3_s5.setText("")
        self.p3_s5.setIcon(icon2)
        self.p3_s5.setObjectName("p3_s5")
        self.p4_s5 = QtWidgets.QPushButton(self.rBod_s5)
        self.p4_s5.setGeometry(QtCore.QRect(440, 170, 24, 24))
        self.p4_s5.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    border-radius: 4px;\n"
"    color: rgb(18,18,18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 1px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.p4_s5.setText("")
        self.p4_s5.setIcon(icon2)
        self.p4_s5.setObjectName("p4_s5")
        self.stackedWidget.addWidget(self.step5)
        self.loopListen = QtWidgets.QWidget()
        self.loopListen.setObjectName("loopListen")
        self.listenComplete = QtWidgets.QPushButton(self.loopListen)
        self.listenComplete.setGeometry(QtCore.QRect(250, 70, 141, 141))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.listenComplete.setFont(font)
        self.listenComplete.setStyleSheet("QPushButton{\n"
"    background-color:rgb(54, 75, 182);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    border-radius: 8px;\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 87, 212);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(38, 55, 131);\n"
"    border: none;\n"
"    border-top: 2px solid rgb(34, 48, 116);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.listenComplete.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/play2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.listenComplete.setIcon(icon3)
        self.listenComplete.setIconSize(QtCore.QSize(64, 64))
        self.listenComplete.setObjectName("listenComplete")
        self.resetButton = QtWidgets.QPushButton(self.loopListen)
        self.resetButton.setGeometry(QtCore.QRect(180, 240, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.resetButton.setFont(font)
        self.resetButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(230, 168, 106);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(208, 122, 36);\n"
"    border-radius: 8px;\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(234, 182, 130);\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(208, 122, 36);\n"
"    color: rgb(18, 18, 18);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(220, 139, 58);\n"
"    border: none;\n"
"    border-top: 2px solid rgb(208, 122, 36);\n"
"    color: rgb(18, 18, 18);\n"
"}")
        self.resetButton.setObjectName("resetButton")
        self.stackedWidget.addWidget(self.loopListen)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.lblcred.setText(_translate("MainWindow", "Made by Ahmed Abutahoun"))
        self.lblstep.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Step 0:</span> Get Started</p></body></html>"))
        self.startButton.setText(_translate("MainWindow", "Get Started"))
        self.prog1.setText(_translate("MainWindow", "Progression 1"))
        self.prog2.setText(_translate("MainWindow", "Progression 2"))
        self.prog3.setText(_translate("MainWindow", "Progression 3"))
        self.bck1.setText(_translate("MainWindow", "Back"))
        self.nxt1.setText(_translate("MainWindow", "Next"))
        self.l1_s2.setText(_translate("MainWindow", "Track 1"))
        self.l2_s2.setText(_translate("MainWindow", "Track 2"))
        self.l3_s2.setText(_translate("MainWindow", "Track 3"))
        self.l4_s2.setText(_translate("MainWindow", "Track 4"))
        self.nxt2.setText(_translate("MainWindow", "Next"))
        self.bck2.setText(_translate("MainWindow", "Back"))
        self.l1_s3.setText(_translate("MainWindow", "Track 1"))
        self.l2_s3.setText(_translate("MainWindow", "Track 2"))
        self.l3_s3.setText(_translate("MainWindow", "Track 3"))
        self.l4_s3.setText(_translate("MainWindow", "Track 4"))
        self.nxt3.setText(_translate("MainWindow", "Next"))
        self.bck3.setText(_translate("MainWindow", "Back"))
        self.l1_s4.setText(_translate("MainWindow", "Track 1"))
        self.l2_s4.setText(_translate("MainWindow", "Track 2"))
        self.l3_s4.setText(_translate("MainWindow", "Track 3"))
        self.l4_s4.setText(_translate("MainWindow", "Track 4"))
        self.nxt4.setText(_translate("MainWindow", "Next"))
        self.bck4.setText(_translate("MainWindow", "Back"))
        self.l1_s5.setText(_translate("MainWindow", "Track 1"))
        self.l2_s5.setText(_translate("MainWindow", "Track 2"))
        self.l3_s5.setText(_translate("MainWindow", "Track 3"))
        self.l4_s5.setText(_translate("MainWindow", "Track 4"))
        self.resetButton.setText(_translate("MainWindow", "New Loop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
