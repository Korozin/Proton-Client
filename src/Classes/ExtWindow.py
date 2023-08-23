from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def __init__(self, Title, GroupBoxText, FieldText, ButtonText):
        self.Title = Title
        self.GroupBoxText = GroupBoxText
        self.FieldText = FieldText
        self.ButtonText = ButtonText

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(482, 170)
        self.Background_label = QtWidgets.QLabel(Form)
        self.Background_label.setEnabled(False)
        self.Background_label.setGeometry(QtCore.QRect(-40, -190, 591, 561))
        self.Background_label.setStyleSheet("background-color: #1d1d1d;")
        self.Background_label.setText("")
        self.Background_label.setObjectName("Background_label")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 461, 151))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    font: 9pt \"Source Code Pro Black\";\n"
"    background-color: #3C3C3C;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: #FFFFFF;\n"
"    subcontrol-position: top left;\n"
"    margin-top: 6px;\n"
"    margin-left: 10px;\n"
"    border-radius: 10px;\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 109, 441, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setStyleSheet("QPushButton {\n"
"  font: 9pt \"Source Code Pro Black\";\n"
"  color: #FFFFFF;\n"
"  background-color: #8A4DAA;\n"
"  border: 2px solid #8A4DAA;\n"
"  border-radius: 15px;\n"
"  padding: 8px 16px;\n"
"  height: 10px;\n"
"  text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: #31363B;\n"
"  background-color: #9B60C2;\n"
"  border: 2px solid #9B60C2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"  background-color: #4D4D4D;\n"
"  border: 2px solid #4D4D4D;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 441, 71))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: #FFFFFF;\n"
"font: 500 9pt \"Open Sans\";")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", self.Title))
        self.groupBox.setTitle(_translate("Form", self.GroupBoxText))
        self.label.setText(_translate("Form", self.FieldText))
        self.pushButton.setText(_translate("Form", self.ButtonText))
