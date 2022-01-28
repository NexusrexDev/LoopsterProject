from PyQt5 import QtCore, QtGui, QtWidgets
from ui_ref import references
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio
import sys

class Ui_MainWindow(QtWidgets.QMainWindow):
    # Variables for music
    playback = None
    prog = 0
    drum = 0
    bass = 0
    pad = 0
    stab = 0

    def __init__(self): #Window Initialization
        super(Ui_MainWindow, self).__init__()
        #Size, window title, icon and disabling
        self.resize(640, 480)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        self.setWindowTitle("Loopster")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("assets/iconwhite.png"))
        #Draw GUI
        self.initUi()

    def initUi(self):
        #CentralWidget definition
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.resize(640, 480)
        self.centralwidget.setObjectName("centralwidget")
        #Titlebar definition
        self.titleBarDef()
        #Main body definition
        self.mainBody = QtWidgets.QWidget(self.centralwidget)
        self.mainBody.setGeometry(QtCore.QRect(0, 30, 641, 481))
        self.mainBody.setStyleSheet(references.styleSheet(self, "darkGray"))
        self.mainBody.setObjectName("mainBody")
        #Header definition
        self.headerDef()
        #Footer definition
        self.footerDef()
        #Stackedwidget definition
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainBody)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 121, 641, 291))
        self.stackedWidget.setObjectName("stackedWidget")
        #Page 1 definition
        self.p1Def()
        #Page 2 definition
        self.p2Def()
        #Page 3 definition
        self.p3Def()
        #Page 4 definition
        self.p4Def()
        #Page 5 definition
        self.p5Def()
        #Page 6 definition
        self.p6Def()
        #Page 7 definition
        self.p7Def()
        # Steps label definition
        self.stepsDef()

        self.setCentralWidget(self.centralwidget)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def titleBarDef(self):
        self.titleBar = QtWidgets.QWidget(self.centralwidget)
        self.titleBar.setGeometry(QtCore.QRect(0, 0, 640, 31))
        self.titleBar.setStyleSheet(references.styleSheet(self, "sysBlack"))
        self.titleBar.setObjectName("titleBar")
        self.quitButton = QtWidgets.QPushButton(self.titleBar)
        self.quitButton.setGeometry(QtCore.QRect(609, -1, 32, 33))
        self.quitButton.setStyleSheet(references.styleSheet(self, "sysButton"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/CloseButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quitButton.setIcon(icon)
        self.quitButton.setObjectName("quitButton")
        self.quitButton.clicked.connect(self.exitApp)
        self.miniButton = QtWidgets.QPushButton(self.titleBar)
        self.miniButton.setGeometry(QtCore.QRect(577, -1, 32, 33))
        self.miniButton.setStyleSheet(references.styleSheet(self, "sysButton"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/MiniButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.miniButton.setIcon(icon1)
        self.miniButton.setObjectName("miniButton")
        self.miniButton.clicked.connect(self.showMinimized)

    def headerDef(self):
        self.header = QtWidgets.QWidget(self.mainBody)
        self.header.setGeometry(QtCore.QRect(0, 0, 641, 80))
        self.header.setStyleSheet(references.styleSheet(self, "midBlueGray"))
        self.header.setObjectName("header")
        self.lb_Logo = QtWidgets.QLabel(self.header)
        self.lb_Logo.setGeometry(QtCore.QRect(10, 10, 311, 61))
        self.lb_Logo.setPixmap(QtGui.QPixmap("assets/logowhite.png"))
        self.lb_Logo.setScaledContents(True)
        self.lb_Logo.setObjectName("lb_Logo")

    def footerDef(self):
        self.footer = QtWidgets.QWidget(self.mainBody)
        self.footer.setGeometry(QtCore.QRect(0, 419, 641, 31))
        self.footer.setStyleSheet(references.styleSheet(self, "midBlueGray"))
        self.footer.setObjectName("footer")
        self.lb_Cred = QtWidgets.QLabel(self.footer)
        self.lb_Cred.setGeometry(QtCore.QRect(10, 0, 621, 31))
        self.lb_Cred.setStyleSheet(references.styleSheet(self, "smallgrayText"))
        self.lb_Cred.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lb_Cred.setObjectName("lb_Cred")
        self.lb_Cred.setText("Made by Ahmed Abutahoun")

    def stepsDef(self):
        self.step = QtWidgets.QWidget(self.mainBody)
        self.step.setGeometry(QtCore.QRect(0, 80, 641, 41))
        self.step.setStyleSheet(references.styleSheet(self, "darkBlueGray"))
        self.step.setObjectName("step")
        self.lb_Step = QtWidgets.QLabel(self.step)
        self.lb_Step.setGeometry(QtCore.QRect(10, 0, 631, 41))
        self.lb_Step.setStyleSheet(references.styleSheet(self, "grayText"))
        self.lb_Step.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.stepChange()
        self.lb_Step.setObjectName("lb_Step")
        self.l_shad_2 = QtWidgets.QFrame(self.step)
        self.l_shad_2.setGeometry(QtCore.QRect(-1, 32, 642, 16))
        self.l_shad_2.setStyleSheet(references.styleSheet(self, "shadow"))
        self.l_shad_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.l_shad_2.setLineWidth(2)
        self.l_shad_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.l_shad_2.setObjectName("l_shad_2")

    def p1Def(self):
        self.getStarted = QtWidgets.QWidget()
        self.getStarted.setObjectName("getStarted")
        self.startButton = QtWidgets.QPushButton(self.getStarted)
        self.startButton.setGeometry(QtCore.QRect(80, 80, 481, 131))
        self.startButton.setStyleSheet(references.styleSheet(self, "mainButton"))
        self.startButton.setText("Get Started")
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(lambda: self.gotoPage(self.stackedWidget.currentIndex()+1))
        self.stackedWidget.addWidget(self.getStarted)

    def p2Def(self):
        self.step1 = QtWidgets.QWidget()
        self.step1.setObjectName("step1")
        self.prog1 = QtWidgets.QPushButton(self.step1)
        self.prog1.setGeometry(QtCore.QRect(80, 20, 481, 61))
        self.prog1.setStyleSheet(references.styleSheet(self, "mainButton"))
        self.prog1.setObjectName("prog1")
        self.prog2 = QtWidgets.QPushButton(self.step1)
        self.prog2.setGeometry(QtCore.QRect(80, 120, 481, 61))
        self.prog2.setStyleSheet(references.styleSheet(self, "mainButton"))
        self.prog2.setObjectName("prog2")
        self.prog3 = QtWidgets.QPushButton(self.step1)
        self.prog3.setGeometry(QtCore.QRect(80, 220, 481, 61))
        self.prog3.setStyleSheet(references.styleSheet(self, "mainButton"))
        self.prog3.setObjectName("prog3")
        self.prog1.setText("Progression 1")
        self.prog2.setText("Progression 2")
        self.prog3.setText("Progression 3")

        #Buttons
        self.prog1.clicked.connect(lambda: [self.partAssign(0,0),self.gotoPage(self.stackedWidget.currentIndex() + 1)])
        self.prog2.clicked.connect(lambda: [self.partAssign(0,1),self.gotoPage(self.stackedWidget.currentIndex() + 1)])
        self.prog3.clicked.connect(lambda: [self.partAssign(0,2),self.gotoPage(self.stackedWidget.currentIndex() + 1)])

        self.stackedWidget.addWidget(self.step1)

    def p3Def(self):
        self.step2 = QtWidgets.QWidget()
        self.step2.setObjectName("step2")
        self.bck1 = QtWidgets.QPushButton(self.step2)
        self.bck1.setGeometry(QtCore.QRect(160, 240, 151, 41))
        self.bck1.setStyleSheet(references.styleSheet(self, "secondaryButton"))
        self.bck1.setObjectName("bck1")
        self.nxt1 = QtWidgets.QPushButton(self.step2)
        self.nxt1.setGeometry(QtCore.QRect(330, 240, 151, 41))
        self.nxt1.setStyleSheet(references.styleSheet(self, "mainButton"))
        self.nxt1.setObjectName("nxt1")
        self.rBod_s2 = QtWidgets.QWidget(self.step2)
        self.rBod_s2.setGeometry(QtCore.QRect(80, 10, 481, 211))
        self.rBod_s2.setStyleSheet(references.styleSheet(self, "darkBlueGray"))
        self.rBod_s2.setObjectName("rBod_s2")
        self.l_shad = QtWidgets.QFrame(self.rBod_s2)
        self.l_shad.setGeometry(QtCore.QRect(0, 200, 481, 20))
        self.l_shad.setStyleSheet(references.styleSheet(self, "shadow"))
        self.l_shad.setFrameShadow(QtWidgets.QFrame.Plain)
        self.l_shad.setLineWidth(2)
        self.l_shad.setFrameShape(QtWidgets.QFrame.HLine)
        self.l_shad.setObjectName("l_shad")
        self.rb1_s2 = QtWidgets.QRadioButton(self.rBod_s2)
        self.rb1_s2.setGeometry(QtCore.QRect(17, 10, 24, 24))
        self.rb1_s2.setStyleSheet(references.styleSheet(self, "radioButton"))
        self.rb1_s2.setObjectName("rb1_s2")
        self.rb2_s2 = QtWidgets.QRadioButton(self.rBod_s2)
        self.rb2_s2.setGeometry(QtCore.QRect(17, 63, 24, 24))
        self.rb2_s2.setStyleSheet(references.styleSheet(self, "radioButton"))
        self.rb2_s2.setObjectName("rb2_s2")
        self.rb3_s2 = QtWidgets.QRadioButton(self.rBod_s2)
        self.rb3_s2.setGeometry(QtCore.QRect(17, 117, 24, 24))
        self.rb3_s2.setStyleSheet(references.styleSheet(self, "radioButton"))
        self.rb3_s2.setObjectName("rb3_s2")
        self.rb4_s2 = QtWidgets.QRadioButton(self.rBod_s2)
        self.rb4_s2.setGeometry(QtCore.QRect(17, 170, 24, 24))
        self.rb4_s2.setStyleSheet(references.styleSheet(self, "radioButton"))
        self.rb4_s2.setObjectName("rb4_s2")
        self.l1_s2 = QtWidgets.QLabel(self.rBod_s2)
        self.l1_s2.setGeometry(QtCore.QRect(50, 10, 381, 24))
        self.l1_s2.setAlignment(QtCore.Qt.AlignCenter)
        self.l1_s2.setStyleSheet(references.styleSheet(self, "whiteText"))
        self.l1_s2.setObjectName("l1_s2")
        self.l2_s2 = QtWidgets.QLabel(self.rBod_s2)
        self.l2_s2.setGeometry(QtCore.QRect(50, 63, 381, 24))
        self.l2_s2.setStyleSheet(references.styleSheet(self, "whiteText"))
        self.l2_s2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2_s2.setObjectName("l2_s2")
        self.l3_s2 = QtWidgets.QLabel(self.rBod_s2)
        self.l3_s2.setGeometry(QtCore.QRect(50, 117, 381, 24))
        self.l3_s2.setStyleSheet(references.styleSheet(self, "whiteText"))
        self.l3_s2.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_s2.setObjectName("l3_s2")
        self.l4_s2 = QtWidgets.QLabel(self.rBod_s2)
        self.l4_s2.setGeometry(QtCore.QRect(50, 170, 381, 24))
        self.l4_s2.setStyleSheet(references.styleSheet(self, "whiteText"))
        self.l4_s2.setAlignment(QtCore.Qt.AlignCenter)
        self.l4_s2.setObjectName("l4_s2")
        self.p1_s2 = QtWidgets.QPushButton(self.rBod_s2)
        self.p1_s2.setGeometry(QtCore.QRect(440, 10, 24, 24))
        self.p1_s2.setStyleSheet(references.styleSheet(self, "smallPlayButton"))
        self.icon2 = QtGui.QIcon()
        self.icon2.addPixmap(QtGui.QPixmap("assets/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p1_s2.setIcon(self.icon2)
        self.p1_s2.setObjectName("p1_s2")
        self.p2_s2 = QtWidgets.QPushButton(self.rBod_s2)
        self.p2_s2.setGeometry(QtCore.QRect(440, 63, 24, 24))
        self.p2_s2.setStyleSheet(references.styleSheet(self, "smallPlayButton"))
        self.p2_s2.setIcon(self.icon2)
        self.p2_s2.setObjectName("p2_s2")
        self.p3_s2 = QtWidgets.QPushButton(self.rBod_s2)
        self.p3_s2.setGeometry(QtCore.QRect(440, 117, 24, 24))
        self.p3_s2.setStyleSheet(references.styleSheet(self, "smallPlayButton"))
        self.p3_s2.setIcon(self.icon2)
        self.p3_s2.setObjectName("p3_s2")
        self.p4_s2 = QtWidgets.QPushButton(self.rBod_s2)
        self.p4_s2.setGeometry(QtCore.QRect(440, 170, 24, 24))
        self.p4_s2.setStyleSheet(references.styleSheet(self, "smallPlayButton"))
        self.p4_s2.setIcon(self.icon2)
        self.p4_s2.setObjectName("p4_s2")
        self.bck1.setText("Back")
        self.nxt1.setText("Next")
        self.l1_s2.setText("Track 1")
        self.l2_s2.setText("Track 2")
        self.l3_s2.setText("Track 3")
        self.l4_s2.setText("Track 4")

        #Buttons
        self.nxt1.clicked.connect(lambda: [self.partAssign(1),self.gotoPage(self.stackedWidget.currentIndex() + 1)])
        self.bck1.clicked.connect(lambda: [self.gotoPage(self.stackedWidget.currentIndex() - 1)])

        self.stackedWidget.addWidget(self.step2)

    def p4Def(self):
        self.step3 = QtWidgets.QWidget()
        self.step3.setObjectName("step3")
        self.nxt2 = QtWidgets.QPushButton(self.step3)
        self.nxt2.setGeometry(QtCore.QRect(330, 240, 151, 41))
        self.nxt2.setStyleSheet(references.styleSheet(self, "mainButton"))
        self.nxt2.setObjectName("nxt2")
        self.bck2 = QtWidgets.QPushButton(self.step3)
        self.bck2.setGeometry(QtCore.QRect(160, 240, 151, 41))
        self.bck2.setStyleSheet(references.styleSheet(self, "secondaryButton"))
        self.bck2.setObjectName("bck2")
        self.rBod_s3 = QtWidgets.QWidget(self.step3)
        self.rBod_s3.setGeometry(QtCore.QRect(80, 10, 481, 211))
        self.rBod_s3.setStyleSheet(references.styleSheet(self, "darkBlueGray"))
        self.rBod_s3.setObjectName("rBod_s3")
        self.l_shad_4 = QtWidgets.QFrame(self.rBod_s3)
        self.l_shad_4.setGeometry(QtCore.QRect(0, 200, 481, 20))
        self.l_shad_4.setStyleSheet(references.styleSheet(self, "shadow"))
        self.l_shad_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.l_shad_4.setLineWidth(2)
        self.l_shad_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.l_shad_4.setObjectName("l_shad_4")
        self.rb1_s3 = QtWidgets.QRadioButton(self.rBod_s3)
        self.rb1_s3.setGeometry(QtCore.QRect(17, 10, 24, 24))
        self.rb1_s3.setStyleSheet(references.styleSheet(self, "radioButton"))
        self.rb1_s3.setObjectName("rb1_s3")
        self.rb2_s3 = QtWidgets.QRadioButton(self.rBod_s3)
        self.rb2_s3.setGeometry(QtCore.QRect(17, 63, 24, 24))
        self.rb2_s3.setStyleSheet(references.styleSheet(self, "radioButton"))
        self.rb2_s3.setObjectName("rb2_s3")
        self.rb3_s3 = QtWidgets.QRadioButton(self.rBod_s3)
        self.rb3_s3.setGeometry(QtCore.QRect(17, 117, 24, 24))
        self.rb3_s3.setStyleSheet(references.styleSheet(self, "radioButton"))
        self.rb3_s3.setObjectName("rb3_s3")
        self.rb4_s3 = QtWidgets.QRadioButton(self.rBod_s3)
        self.rb4_s3.setGeometry(QtCore.QRect(17, 170, 24, 24))
        self.rb4_s3.setStyleSheet(references.styleSheet(self, "radioButton"))
        self.rb4_s3.setObjectName("rb4_s3")
        self.l1_s3 = QtWidgets.QLabel(self.rBod_s3)
        self.l1_s3.setGeometry(QtCore.QRect(50, 10, 381, 24))
        self.l1_s3.setStyleSheet(references.styleSheet(self, "whiteText"))
        self.l1_s3.setAlignment(QtCore.Qt.AlignCenter)
        self.l1_s3.setObjectName("l1_s3")
        self.l2_s3 = QtWidgets.QLabel(self.rBod_s3)
        self.l2_s3.setGeometry(QtCore.QRect(50, 63, 381, 24))
        self.l2_s3.setStyleSheet(references.styleSheet(self, "whiteText"))
        self.l2_s3.setAlignment(QtCore.Qt.AlignCenter)
        self.l2_s3.setObjectName("l2_s3")
        self.l3_s3 = QtWidgets.QLabel(self.rBod_s3)
        self.l3_s3.setGeometry(QtCore.QRect(50, 117, 381, 24))
        self.l3_s3.setStyleSheet(references.styleSheet(self, "whiteText"))
        self.l3_s3.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_s3.setObjectName("l3_s3")
        self.l4_s3 = QtWidgets.QLabel(self.rBod_s3)
        self.l4_s3.setGeometry(QtCore.QRect(50, 170, 381, 24))
        self.l4_s3.setStyleSheet(references.styleSheet(self, "whiteText"))
        self.l4_s3.setAlignment(QtCore.Qt.AlignCenter)
        self.l4_s3.setObjectName("l4_s3")
        self.p1_s3 = QtWidgets.QPushButton(self.rBod_s3)
        self.p1_s3.setGeometry(QtCore.QRect(440, 10, 24, 24))
        self.p1_s3.setStyleSheet(references.styleSheet(self, "smallPlayButton"))
        self.p1_s3.setIcon(self.icon2)
        self.p1_s3.setObjectName("p1_s3")
        self.p2_s3 = QtWidgets.QPushButton(self.rBod_s3)
        self.p2_s3.setGeometry(QtCore.QRect(440, 63, 24, 24))
        self.p2_s3.setStyleSheet(references.styleSheet(self, "smallPlayButton"))
        self.p2_s3.setIcon(self.icon2)
        self.p2_s3.setObjectName("p2_s3")
        self.p3_s3 = QtWidgets.QPushButton(self.rBod_s3)
        self.p3_s3.setGeometry(QtCore.QRect(440, 117, 24, 24))
        self.p3_s3.setStyleSheet(references.styleSheet(self, "smallPlayButton"))
        self.p3_s3.setIcon(self.icon2)
        self.p3_s3.setObjectName("p3_s3")
        self.p4_s3 = QtWidgets.QPushButton(self.rBod_s3)
        self.p4_s3.setGeometry(QtCore.QRect(440, 170, 24, 24))
        self.p4_s3.setStyleSheet(references.styleSheet(self, "smallPlayButton"))
        self.p4_s3.setIcon(self.icon2)
        self.p4_s3.setObjectName("p4_s3")
        self.nxt2.setText("Next")
        self.bck2.setText("Back")
        self.l1_s3.setText("Track 1")
        self.l2_s3.setText("Track 2")
        self.l3_s3.setText("Track 3")
        self.l4_s3.setText("Track 4")

        # Buttons
        self.nxt2.clicked.connect(lambda: [self.partAssign(2),self.gotoPage(self.stackedWidget.currentIndex() + 1)])
        self.bck2.clicked.connect(lambda: [self.gotoPage(self.stackedWidget.currentIndex() - 1)])

        self.stackedWidget.addWidget(self.step3)

    def p5Def(self):
        self.step4 = QtWidgets.QWidget()
        self.step4.setObjectName("step4")
        self.nxt3 = QtWidgets.QPushButton(self.step4)
        self.nxt3.setGeometry(QtCore.QRect(330, 240, 151, 41))
        self.nxt3.setStyleSheet(references.styleSheet(self, "mainButton"))
        self.nxt3.setObjectName("nxt3")
        self.bck3 = QtWidgets.QPushButton(self.step4)
        self.bck3.setGeometry(QtCore.QRect(160, 240, 151, 41))
        self.bck3.setStyleSheet(references.styleSheet(self, "secondaryButton"))
        self.bck3.setObjectName("bck3")
        self.rBod_s4 = QtWidgets.QWidget(self.step4)
        self.rBod_s4.setGeometry(QtCore.QRect(80, 10, 481, 211))
        self.rBod_s4.setStyleSheet(references.styleSheet(self, "darkBlueGray"))
        self.rBod_s4.setObjectName("rBod_s4")
        self.l_shad_5 = QtWidgets.QFrame(self.rBod_s4)
        self.l_shad_5.setGeometry(QtCore.QRect(0, 200, 481, 20))
        self.l_shad_5.setStyleSheet(references.styleSheet(self, "shadow"))
        self.l_shad_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.l_shad_5.setLineWidth(2)
        self.l_shad_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.l_shad_5.setObjectName("l_shad_5")
        self.rb1_s4 = QtWidgets.QRadioButton(self.rBod_s4)
        self.rb1_s4.setGeometry(QtCore.QRect(17, 10, 24, 24))
        self.rb1_s4.setStyleSheet(references.styleSheet(self, "radioButton"))
        self.rb1_s4.setObjectName("rb1_s4")
        self.rb2_s4 = QtWidgets.QRadioButton(self.rBod_s4)
        self.rb2_s4.setGeometry(QtCore.QRect(17, 63, 24, 24))
        self.rb2_s4.setStyleSheet(references.styleSheet(self, "radioButton"))
        self.rb2_s4.setObjectName("rb2_s4")
        self.rb3_s4 = QtWidgets.QRadioButton(self.rBod_s4)
        self.rb3_s4.setGeometry(QtCore.QRect(17, 117, 24, 24))
        self.rb3_s4.setStyleSheet(references.styleSheet(self, "radioButton"))
        self.rb3_s4.setObjectName("rb3_s4")
        self.rb4_s4 = QtWidgets.QRadioButton(self.rBod_s4)
        self.rb4_s4.setGeometry(QtCore.QRect(17, 170, 24, 24))
        self.rb4_s4.setStyleSheet(references.styleSheet(self, "radioButton"))
        self.rb4_s4.setObjectName("rb4_s4")
        self.l1_s4 = QtWidgets.QLabel(self.rBod_s4)
        self.l1_s4.setGeometry(QtCore.QRect(50, 10, 381, 24))
        self.l1_s4.setStyleSheet(references.styleSheet(self, "whiteText"))
        self.l1_s4.setAlignment(QtCore.Qt.AlignCenter)
        self.l1_s4.setObjectName("l1_s4")
        self.l2_s4 = QtWidgets.QLabel(self.rBod_s4)
        self.l2_s4.setGeometry(QtCore.QRect(50, 63, 381, 24))
        self.l2_s4.setStyleSheet(references.styleSheet(self, "whiteText"))
        self.l2_s4.setAlignment(QtCore.Qt.AlignCenter)
        self.l2_s4.setObjectName("l2_s4")
        self.l3_s4 = QtWidgets.QLabel(self.rBod_s4)
        self.l3_s4.setGeometry(QtCore.QRect(50, 117, 381, 24))
        self.l3_s4.setStyleSheet(references.styleSheet(self, "whiteText"))
        self.l3_s4.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_s4.setObjectName("l3_s4")
        self.l4_s4 = QtWidgets.QLabel(self.rBod_s4)
        self.l4_s4.setGeometry(QtCore.QRect(50, 170, 381, 24))
        self.l4_s4.setStyleSheet(references.styleSheet(self, "whiteText"))
        self.l4_s4.setAlignment(QtCore.Qt.AlignCenter)
        self.l4_s4.setObjectName("l4_s4")
        self.p1_s4 = QtWidgets.QPushButton(self.rBod_s4)
        self.p1_s4.setGeometry(QtCore.QRect(440, 10, 24, 24))
        self.p1_s4.setStyleSheet(references.styleSheet(self, "smallPlayButton"))
        self.p1_s4.setIcon(self.icon2)
        self.p1_s4.setObjectName("p1_s4")
        self.p2_s4 = QtWidgets.QPushButton(self.rBod_s4)
        self.p2_s4.setGeometry(QtCore.QRect(440, 63, 24, 24))
        self.p2_s4.setStyleSheet(references.styleSheet(self, "smallPlayButton"))
        self.p2_s4.setIcon(self.icon2)
        self.p2_s4.setObjectName("p2_s4")
        self.p3_s4 = QtWidgets.QPushButton(self.rBod_s4)
        self.p3_s4.setGeometry(QtCore.QRect(440, 117, 24, 24))
        self.p3_s4.setStyleSheet(references.styleSheet(self, "smallPlayButton"))
        self.p3_s4.setIcon(self.icon2)
        self.p3_s4.setObjectName("p3_s4")
        self.p4_s4 = QtWidgets.QPushButton(self.rBod_s4)
        self.p4_s4.setGeometry(QtCore.QRect(440, 170, 24, 24))
        self.p4_s4.setStyleSheet(references.styleSheet(self, "smallPlayButton"))
        self.p4_s4.setIcon(self.icon2)
        self.p4_s4.setObjectName("p4_s4")
        self.nxt3.setText("Next")
        self.bck3.setText("Back")
        self.l1_s4.setText("Track 1")
        self.l2_s4.setText("Track 2")
        self.l3_s4.setText("Track 3")
        self.l4_s4.setText("Track 4")

        # Buttons
        self.nxt3.clicked.connect(lambda: [self.partAssign(3),self.gotoPage(self.stackedWidget.currentIndex() + 1)])
        self.bck3.clicked.connect(lambda: [self.gotoPage(self.stackedWidget.currentIndex() - 1)])

        self.stackedWidget.addWidget(self.step4)

    def p6Def(self):
        self.step5 = QtWidgets.QWidget()
        self.step5.setObjectName("step5")
        self.nxt4 = QtWidgets.QPushButton(self.step5)
        self.nxt4.setGeometry(QtCore.QRect(330, 240, 151, 41))
        self.nxt4.setStyleSheet(references.styleSheet(self, "mainButton"))
        self.nxt4.setObjectName("nxt4")
        self.bck4 = QtWidgets.QPushButton(self.step5)
        self.bck4.setGeometry(QtCore.QRect(160, 240, 151, 41))
        self.bck4.setStyleSheet(references.styleSheet(self, "secondaryButton"))
        self.bck4.setObjectName("bck4")
        self.rBod_s5 = QtWidgets.QWidget(self.step5)
        self.rBod_s5.setGeometry(QtCore.QRect(80, 10, 481, 211))
        self.rBod_s5.setStyleSheet(references.styleSheet(self, "darkBlueGray"))
        self.rBod_s5.setObjectName("rBod_s5")
        self.l_shad_6 = QtWidgets.QFrame(self.rBod_s5)
        self.l_shad_6.setGeometry(QtCore.QRect(0, 200, 481, 20))
        self.l_shad_6.setStyleSheet(references.styleSheet(self, "shadow"))
        self.l_shad_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.l_shad_6.setLineWidth(2)
        self.l_shad_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.l_shad_6.setObjectName("l_shad_6")
        self.rb1_s5 = QtWidgets.QRadioButton(self.rBod_s5)
        self.rb1_s5.setGeometry(QtCore.QRect(17, 10, 24, 24))
        self.rb1_s5.setStyleSheet(references.styleSheet(self, "radioButton"))
        self.rb1_s5.setObjectName("rb1_s5")
        self.rb2_s5 = QtWidgets.QRadioButton(self.rBod_s5)
        self.rb2_s5.setGeometry(QtCore.QRect(17, 63, 24, 24))
        self.rb2_s5.setStyleSheet(references.styleSheet(self, "radioButton"))
        self.rb2_s5.setObjectName("rb2_s5")
        self.rb3_s5 = QtWidgets.QRadioButton(self.rBod_s5)
        self.rb3_s5.setGeometry(QtCore.QRect(17, 117, 24, 24))
        self.rb3_s5.setStyleSheet(references.styleSheet(self, "radioButton"))
        self.rb3_s5.setObjectName("rb3_s5")
        self.rb4_s5 = QtWidgets.QRadioButton(self.rBod_s5)
        self.rb4_s5.setGeometry(QtCore.QRect(17, 170, 24, 24))
        self.rb4_s5.setStyleSheet(references.styleSheet(self, "radioButton"))
        self.rb4_s5.setObjectName("rb4_s5")
        self.l1_s5 = QtWidgets.QLabel(self.rBod_s5)
        self.l1_s5.setGeometry(QtCore.QRect(50, 10, 381, 24))
        self.l1_s5.setStyleSheet(references.styleSheet(self, "whiteText"))
        self.l1_s5.setAlignment(QtCore.Qt.AlignCenter)
        self.l1_s5.setObjectName("l1_s5")
        self.l2_s5 = QtWidgets.QLabel(self.rBod_s5)
        self.l2_s5.setGeometry(QtCore.QRect(50, 63, 381, 24))
        self.l2_s5.setStyleSheet(references.styleSheet(self, "whiteText"))
        self.l2_s5.setAlignment(QtCore.Qt.AlignCenter)
        self.l2_s5.setObjectName("l2_s5")
        self.l3_s5 = QtWidgets.QLabel(self.rBod_s5)
        self.l3_s5.setGeometry(QtCore.QRect(50, 117, 381, 24))
        self.l3_s5.setStyleSheet(references.styleSheet(self, "whiteText"))
        self.l3_s5.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_s5.setObjectName("l3_s5")
        self.l4_s5 = QtWidgets.QLabel(self.rBod_s5)
        self.l4_s5.setGeometry(QtCore.QRect(50, 170, 381, 24))
        self.l4_s5.setStyleSheet(references.styleSheet(self, "whiteText"))
        self.l4_s5.setAlignment(QtCore.Qt.AlignCenter)
        self.l4_s5.setObjectName("l4_s5")
        self.p1_s5 = QtWidgets.QPushButton(self.rBod_s5)
        self.p1_s5.setGeometry(QtCore.QRect(440, 10, 24, 24))
        self.p1_s5.setStyleSheet(references.styleSheet(self, "smallPlayButton"))
        self.p1_s5.setIcon(self.icon2)
        self.p1_s5.setObjectName("p1_s5")
        self.p2_s5 = QtWidgets.QPushButton(self.rBod_s5)
        self.p2_s5.setGeometry(QtCore.QRect(440, 63, 24, 24))
        self.p2_s5.setStyleSheet(references.styleSheet(self, "smallPlayButton"))
        self.p2_s5.setIcon(self.icon2)
        self.p2_s5.setObjectName("p2_s5")
        self.p3_s5 = QtWidgets.QPushButton(self.rBod_s5)
        self.p3_s5.setGeometry(QtCore.QRect(440, 117, 24, 24))
        self.p3_s5.setStyleSheet(references.styleSheet(self, "smallPlayButton"))
        self.p3_s5.setIcon(self.icon2)
        self.p3_s5.setObjectName("p3_s5")
        self.p4_s5 = QtWidgets.QPushButton(self.rBod_s5)
        self.p4_s5.setGeometry(QtCore.QRect(440, 170, 24, 24))
        self.p4_s5.setStyleSheet(references.styleSheet(self, "smallPlayButton"))
        self.p4_s5.setIcon(self.icon2)
        self.p4_s5.setObjectName("p4_s5")
        self.nxt4.setText("Next")
        self.bck4.setText("Back")
        self.l1_s5.setText("Track 1")
        self.l2_s5.setText("Track 2")
        self.l3_s5.setText("Track 3")
        self.l4_s5.setText("Track 4")

        # Buttons
        self.nxt4.clicked.connect(lambda: [self.partAssign(4),self.gotoPage(self.stackedWidget.currentIndex() + 1)])
        self.bck4.clicked.connect(lambda: [self.gotoPage(self.stackedWidget.currentIndex() - 1)])

        self.stackedWidget.addWidget(self.step5)

    def p7Def(self):
        self.loopListen = QtWidgets.QWidget()
        self.loopListen.setObjectName("loopListen")
        self.listenComplete = QtWidgets.QPushButton(self.loopListen)
        self.listenComplete.setGeometry(QtCore.QRect(250, 70, 141, 141))
        self.listenComplete.setStyleSheet(references.styleSheet(self, "mainButton"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/play2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.listenComplete.setIcon(icon3)
        self.listenComplete.setIconSize(QtCore.QSize(64, 64))
        self.listenComplete.setObjectName("listenComplete")
        self.resetButton = QtWidgets.QPushButton(self.loopListen)
        self.resetButton.setGeometry(QtCore.QRect(180, 240, 281, 41))
        self.resetButton.setStyleSheet(references.styleSheet(self, "secondaryButton"))
        self.resetButton.setObjectName("resetButton")
        self.resetButton.setText("New Loop")

        #Buttons
        self.listenComplete.clicked.connect(self.playSound)
        self.resetButton.clicked.connect(lambda: [self.resetSelection(),self.gotoPage(1)])

        self.stackedWidget.addWidget(self.loopListen)

    #Functionality
    def gotoPage(self,page):
        if self.stackedWidget.currentIndex() > 1 and self.stackedWidget.currentIndex() < 6 and page > self.stackedWidget.currentIndex():
            if self.canChange() == True: #Only works for next button
                self.stackedWidget.setCurrentIndex(page)
                self.stepChange()
        else:
            self.stackedWidget.setCurrentIndex(page)
            self.stepChange()

    def partAssign(self,part,num = None):
        if num == None:
            num = self.rbChecker()
        if part == 0:
            self.prog = num
        if part == 1:
            self.drum = num
        if part == 2:
            self.bass = num
        if part == 3:
            self.pad = num
        if part == 4:
            self.stab = num

    def rbChecker(self):
        #To check which radioButton is selected
        number = None
        rd1 = [self.rb1_s2, self.rb2_s2, self.rb3_s2, self.rb4_s2]
        rd2 = [self.rb1_s3, self.rb2_s3, self.rb3_s3, self.rb4_s3]
        rd3 = [self.rb1_s4, self.rb2_s4, self.rb3_s4, self.rb4_s4]
        rd4 = [self.rb1_s5, self.rb2_s5, self.rb3_s5, self.rb4_s5]

        if self.stackedWidget.currentIndex() == 2:
            for i in rd1:
                if i.isChecked():
                    number = rd1.index(i)
        if self.stackedWidget.currentIndex() == 3:
            for i in rd2:
                if i.isChecked():
                    number = rd2.index(i)
        if self.stackedWidget.currentIndex() == 4:
            for i in rd3:
                if i.isChecked():
                    number = rd3.index(i)
        if self.stackedWidget.currentIndex() == 5:
            for i in rd4:
                if i.isChecked():
                    number = rd4.index(i)
        return number

    def exitApp(self):
        sys.exit()

    def stepChange(self):
        self.stepSubText = ["Get Started", "Song Mood", "Drums", "Bass", "Pad", "Stabs", "Listen to the loop!"]
        self.stepText = [
            f"<html><head/><body><p><span style=\" font-weight:600;\">Step {self.stackedWidget.currentIndex()}:</span> {self.stepSubText[0]}</p></body></html>",
            f"<html><head/><body><p><span style=\" font-weight:600;\">Step 1.{self.stackedWidget.currentIndex()-1}:</span> Build the loop ({self.stepSubText[self.stackedWidget.currentIndex()]})</p></body></html>",
            f"<html><head/><body><p><span style=\" font-weight:600;\">Step 2:</span> {self.stepSubText[6]}</p></body></html>"
            ]
        if self.stackedWidget.currentIndex() == 0:
            self.lb_Step.setText(self.stepText[0])
        elif self.stackedWidget.currentIndex() > 0 and self.stackedWidget.currentIndex() < 6:
            self.lb_Step.setText(self.stepText[1])
        elif self.stackedWidget.currentIndex() == 6:
            self.lb_Step.setText(self.stepText[2])

    def canChange(self):
        #To force selection on every radio button
        rd1 = [self.rb1_s2,self.rb2_s2,self.rb3_s2,self.rb4_s2]
        rd2 = [self.rb1_s3, self.rb2_s3, self.rb3_s3, self.rb4_s3]
        rd3 = [self.rb1_s4, self.rb2_s4, self.rb3_s4, self.rb4_s4]
        rd4 = [self.rb1_s5, self.rb2_s5, self.rb3_s5, self.rb4_s5]
        selected = False

        if self.stackedWidget.currentIndex() == 2:
            for i in rd1:
                if i.isChecked():
                    selected = True
        if self.stackedWidget.currentIndex() == 3:
            for i in rd2:
                if i.isChecked():
                    selected = True
        if self.stackedWidget.currentIndex() == 4:
            for i in rd3:
                if i.isChecked():
                    selected = True
        if self.stackedWidget.currentIndex() == 5:
            for i in rd4:
                if i.isChecked():
                    selected = True

        return selected

    def resetSelection(self):
        rd = [self.rb1_s2, self.rb2_s2, self.rb3_s2, self.rb4_s2, self.rb1_s3, self.rb2_s3, self.rb3_s3, self.rb4_s3, self.rb1_s3, self.rb2_s3, self.rb3_s3, self.rb4_s3, self.rb1_s4, self.rb2_s4, self.rb3_s4, self.rb4_s4]
        for i in rd:
            if i.isChecked() == True:
                i.setChecked(False)

    def playSound(self):
        print(f"Sound consists of, Progression:{self.prog},\nDrums:{self.drum},\nBass:{self.bass},\nPad:{self.pad},\nStab:{self.stab}")

def windowStart():
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    sys.exit(app.exec_())

#Let's start!
windowStart()