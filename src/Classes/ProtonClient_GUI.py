from PyQt5 import QtCore, QtGui, QtWidgets
import Classes.ProtonClientRC_rc



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(588, 568)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Background_label = QtWidgets.QLabel(self.centralwidget)
        self.Background_label.setEnabled(False)
        self.Background_label.setGeometry(QtCore.QRect(0, 0, 1000, 1000))
        self.Background_label.setStyleSheet("background-color: #1d1d1d;")
        self.Background_label.setText("")
        self.Background_label.setObjectName("Background_label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(9, 11, 571, 471))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("/* Set the font properties for the tab bar */\n"
"QTabBar {\n"
"    text-transform: uppercase;\n"
"    font-weight: bold;\n"
"    font: 800 9pt \"Noto Serif Lao\";\n"
"    background-color: #2C2C2C;\n"
"}\n"
"\n"
"/* Style the individual tabs */\n"
"QTabBar::tab {\n"
"    color: #FFFFFF;\n"
"    border: 0;\n"
"    padding: 2px 20px;\n"
"}\n"
"\n"
"/* Style the top and bottom tabs */\n"
"QTabBar::tab:top,\n"
"QTabBar::tab:bottom {\n"
"    height: 25px;\n"
"}\n"
"\n"
"/* Style the hover effect for tabs */\n"
"QTabBar::tab:hover {\n"
"    border-top: 3px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.658, fx:0.5, fy:0.500364, stop:0 rgba(138, 77, 170, 255), stop:1 rgba(197, 110, 244, 255));\n"
"}\n"
"\n"
"/* Style the selected tab */\n"
"QTabBar::tab:selected {\n"
"    color: #8A4DAA;\n"
"    border-top: 3px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.658, fx:0.5, fy:0.500364, stop:0 rgba(138, 77, 170, 255), stop:1 rgba(197, 110, 244, 255));\n"
"}\n"
"\n"
"/* Style the content pane */\n"
"QTabWidget::pane {\n"
"    border: none;\n"
"    background-color: #2C2C2C;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.General_Tab = QtWidgets.QWidget()
        self.General_Tab.setObjectName("General_Tab")
        self.Combat_groupBox = QtWidgets.QGroupBox(self.General_Tab)
        self.Combat_groupBox.setEnabled(True)
        self.Combat_groupBox.setGeometry(QtCore.QRect(10, 20, 271, 281))
        self.Combat_groupBox.setStyleSheet("QGroupBox {\n"
"    font: 9pt \"Source Code Pro Black\";\n"
"    background-color: #3C3C3C;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: #FFFFFF;\n"
"    subcontrol-position: top center;\n"
"    padding: 10px;\n"
"}")
        self.Combat_groupBox.setObjectName("Combat_groupBox")
        self.Combo_checkBox = QtWidgets.QCheckBox(self.Combat_groupBox)
        self.Combo_checkBox.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.Combo_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.Combo_checkBox.setObjectName("Combo_checkBox")
        self.Macro_checkBox = QtWidgets.QCheckBox(self.Combat_groupBox)
        self.Macro_checkBox.setGeometry(QtCore.QRect(10, 60, 111, 31))
        self.Macro_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.Macro_checkBox.setObjectName("Macro_checkBox")
        self.BowSpam_checkBox = QtWidgets.QCheckBox(self.Combat_groupBox)
        self.BowSpam_checkBox.setGeometry(QtCore.QRect(10, 90, 111, 31))
        self.BowSpam_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.BowSpam_checkBox.setObjectName("BowSpam_checkBox")
        self.RiptideZR_checkBox = QtWidgets.QCheckBox(self.Combat_groupBox)
        self.RiptideZR_checkBox.setGeometry(QtCore.QRect(10, 210, 121, 31))
        self.RiptideZR_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.RiptideZR_checkBox.setObjectName("RiptideZR_checkBox")
        self.Reach_checkBox = QtWidgets.QCheckBox(self.Combat_groupBox)
        self.Reach_checkBox.setGeometry(QtCore.QRect(10, 150, 121, 31))
        self.Reach_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.Reach_checkBox.setObjectName("Reach_checkBox")
        self.KillAura_checkBox = QtWidgets.QCheckBox(self.Combat_groupBox)
        self.KillAura_checkBox.setGeometry(QtCore.QRect(10, 120, 111, 31))
        self.KillAura_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.KillAura_checkBox.setObjectName("KillAura_checkBox")
        self.RiptideNoRain_checkBox = QtWidgets.QCheckBox(self.Combat_groupBox)
        self.RiptideNoRain_checkBox.setGeometry(QtCore.QRect(10, 180, 91, 31))
        self.RiptideNoRain_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.RiptideNoRain_checkBox.setObjectName("RiptideNoRain_checkBox")
        self.Visual_groupBox = QtWidgets.QGroupBox(self.Combat_groupBox)
        self.Visual_groupBox.setGeometry(QtCore.QRect(130, 60, 131, 191))
        self.Visual_groupBox.setStyleSheet("QGroupBox {\n"
"    font: 9pt \"Source Code Pro Black\";\n"
"    background-color: #4C4C4C;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: #FFFFFF;\n"
"    subcontrol-position: top center;\n"
"    padding: 10px;\n"
"}")
        self.Visual_groupBox.setObjectName("Visual_groupBox")
        self.Hitbox_checkBox = QtWidgets.QCheckBox(self.Visual_groupBox)
        self.Hitbox_checkBox.setGeometry(QtCore.QRect(0, 30, 121, 31))
        self.Hitbox_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.Hitbox_checkBox.setObjectName("Hitbox_checkBox")
        self.ESP_checkBox = QtWidgets.QCheckBox(self.Visual_groupBox)
        self.ESP_checkBox.setGeometry(QtCore.QRect(0, 120, 121, 31))
        self.ESP_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.ESP_checkBox.setObjectName("ESP_checkBox")
        self.HitboxXRAY_checkBox = QtWidgets.QCheckBox(self.Visual_groupBox)
        self.HitboxXRAY_checkBox.setGeometry(QtCore.QRect(0, 60, 121, 31))
        self.HitboxXRAY_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.HitboxXRAY_checkBox.setObjectName("HitboxXRAY_checkBox")
        self.HPDisplay_checkBox = QtWidgets.QCheckBox(self.Visual_groupBox)
        self.HPDisplay_checkBox.setGeometry(QtCore.QRect(0, 90, 121, 31))
        self.HPDisplay_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.HPDisplay_checkBox.setObjectName("HPDisplay_checkBox")
        self.ArmorHud_checkBox = QtWidgets.QCheckBox(self.Visual_groupBox)
        self.ArmorHud_checkBox.setGeometry(QtCore.QRect(0, 150, 121, 31))
        self.ArmorHud_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.ArmorHud_checkBox.setObjectName("ArmorHud_checkBox")
        self.Movement_groupBox = QtWidgets.QGroupBox(self.General_Tab)
        self.Movement_groupBox.setGeometry(QtCore.QRect(290, 20, 271, 141))
        self.Movement_groupBox.setStyleSheet("QGroupBox {\n"
"    font: 9pt \"Source Code Pro Black\";\n"
"    background-color: #3C3C3C;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: #FFFFFF;\n"
"    subcontrol-position: top center;\n"
"    margin-top: 6px;\n"
"}")
        self.Movement_groupBox.setObjectName("Movement_groupBox")
        self.Fly_checkBox = QtWidgets.QCheckBox(self.Movement_groupBox)
        self.Fly_checkBox.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.Fly_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.Fly_checkBox.setObjectName("Fly_checkBox")
        self.SwimFly_checkBox = QtWidgets.QCheckBox(self.Movement_groupBox)
        self.SwimFly_checkBox.setGeometry(QtCore.QRect(10, 60, 111, 31))
        self.SwimFly_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.SwimFly_checkBox.setObjectName("SwimFly_checkBox")
        self.AutoSprint_checkBox = QtWidgets.QCheckBox(self.Movement_groupBox)
        self.AutoSprint_checkBox.setGeometry(QtCore.QRect(140, 60, 121, 31))
        self.AutoSprint_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.AutoSprint_checkBox.setObjectName("AutoSprint_checkBox")
        self.NoSlowdown_checkBox = QtWidgets.QCheckBox(self.Movement_groupBox)
        self.NoSlowdown_checkBox.setGeometry(QtCore.QRect(10, 90, 131, 31))
        self.NoSlowdown_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.NoSlowdown_checkBox.setObjectName("NoSlowdown_checkBox")
        self.BHop_checkBox = QtWidgets.QCheckBox(self.Movement_groupBox)
        self.BHop_checkBox.setGeometry(QtCore.QRect(140, 30, 111, 31))
        self.BHop_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.BHop_checkBox.setObjectName("BHop_checkBox")
        self.NoKnockback_checkBox = QtWidgets.QCheckBox(self.Movement_groupBox)
        self.NoKnockback_checkBox.setGeometry(QtCore.QRect(140, 90, 131, 31))
        self.NoKnockback_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.NoKnockback_checkBox.setObjectName("NoKnockback_checkBox")
        self.Adjustable_groupBox = QtWidgets.QGroupBox(self.General_Tab)
        self.Adjustable_groupBox.setGeometry(QtCore.QRect(10, 318, 551, 101))
        self.Adjustable_groupBox.setStyleSheet("QGroupBox {\n"
"    font: 9pt \"Source Code Pro Black\";\n"
"    background-color: #3C3C3C;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: #FFFFFF;\n"
"    subcontrol-position: top center;\n"
"    margin-top: 6px;\n"
"}")
        self.Adjustable_groupBox.setObjectName("Adjustable_groupBox")
        self.Speed_horizontalSlider = QtWidgets.QSlider(self.Adjustable_groupBox)
        self.Speed_horizontalSlider.setEnabled(True)
        self.Speed_horizontalSlider.setGeometry(QtCore.QRect(350, 54, 181, 16))
        self.Speed_horizontalSlider.setStyleSheet("QSlider::sub-page:horizontal {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(138, 77, 170, 255), stop:1 rgba(211, 144, 232, 255));\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #2c2c2c;\n"
"    border: 2px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.658, fx:0.5, fy:0.500364, stop:0 rgba(138, 77, 170, 255), stop:1 rgba(197, 110, 244, 255));;\n"
"    border-radius: 5px;\n"
"}")
        self.Speed_horizontalSlider.setMinimum(1)
        self.Speed_horizontalSlider.setMaximum(10)
        self.Speed_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Speed_horizontalSlider.setObjectName("Speed_horizontalSlider")
        self.Speed_label = QtWidgets.QLabel(self.Adjustable_groupBox)
        self.Speed_label.setGeometry(QtCore.QRect(420, 34, 61, 17))
        self.Speed_label.setStyleSheet("color: #FFFFFF;")
        self.Speed_label.setObjectName("Speed_label")
        self.Hitbox_horizontalSlider = QtWidgets.QSlider(self.Adjustable_groupBox)
        self.Hitbox_horizontalSlider.setEnabled(True)
        self.Hitbox_horizontalSlider.setGeometry(QtCore.QRect(20, 54, 181, 16))
        self.Hitbox_horizontalSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Hitbox_horizontalSlider.setStyleSheet("QSlider::sub-page:horizontal {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(138, 77, 170, 255), stop:1 rgba(211, 144, 232, 255));\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #2c2c2c;\n"
"    border: 2px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.658, fx:0.5, fy:0.500364, stop:0 rgba(138, 77, 170, 255), stop:1 rgba(197, 110, 244, 255));;\n"
"    border-radius: 5px;\n"
"}")
        self.Hitbox_horizontalSlider.setMinimum(1)
        self.Hitbox_horizontalSlider.setMaximum(10)
        self.Hitbox_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Hitbox_horizontalSlider.setObjectName("Hitbox_horizontalSlider")
        self.Hitbox_label = QtWidgets.QLabel(self.Adjustable_groupBox)
        self.Hitbox_label.setGeometry(QtCore.QRect(90, 34, 61, 17))
        self.Hitbox_label.setStyleSheet("color: #FFFFFF;")
        self.Hitbox_label.setObjectName("Hitbox_label")
        self.Aimbot_label = QtWidgets.QLabel(self.Adjustable_groupBox)
        self.Aimbot_label.setGeometry(QtCore.QRect(254, 30, 54, 17))
        self.Aimbot_label.setStyleSheet("color: #FFFFFF;")
        self.Aimbot_label.setObjectName("Aimbot_label")
        self.Aimbot_comboBox = QtWidgets.QComboBox(self.Adjustable_groupBox)
        self.Aimbot_comboBox.setGeometry(QtCore.QRect(216, 50, 121, 25))
        self.Aimbot_comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Aimbot_comboBox.setStyleSheet("color: #FFFFFF;\n"
"font: 10pt;\n"
"background-color: #2C2C2C;\n"
"border: 2px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.658, fx:0.5, fy:0.500364, stop:0 rgba(138, 77, 170, 255), stop:1 rgba(197, 110, 244, 255));;")
        self.Aimbot_comboBox.setFrame(True)
        self.Aimbot_comboBox.setObjectName("Aimbot_comboBox")
        self.Aimbot_comboBox.addItem("")
        self.Aimbot_comboBox.addItem("")
        self.Aimbot_comboBox.addItem("")
        self.Utility_groupBox = QtWidgets.QGroupBox(self.General_Tab)
        self.Utility_groupBox.setGeometry(QtCore.QRect(290, 170, 271, 131))
        self.Utility_groupBox.setStyleSheet("QGroupBox {\n"
"    font: 9pt \"Source Code Pro Black\";\n"
"    background-color: #3C3C3C;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: #FFFFFF;\n"
"    subcontrol-position: top center;\n"
"    margin-top: 6px;\n"
"}")
        self.Utility_groupBox.setObjectName("Utility_groupBox")
        self.FOF_checkBox = QtWidgets.QCheckBox(self.Utility_groupBox)
        self.FOF_checkBox.setGeometry(QtCore.QRect(10, 30, 121, 31))
        self.FOF_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.FOF_checkBox.setObjectName("FOF_checkBox")
        self.AntiBan_checkBox = QtWidgets.QCheckBox(self.Utility_groupBox)
        self.AntiBan_checkBox.setGeometry(QtCore.QRect(140, 30, 121, 31))
        self.AntiBan_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.AntiBan_checkBox.setObjectName("AntiBan_checkBox")
        self.LockServer_checkBox = QtWidgets.QCheckBox(self.Utility_groupBox)
        self.LockServer_checkBox.setGeometry(QtCore.QRect(10, 60, 121, 31))
        self.LockServer_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.LockServer_checkBox.setObjectName("LockServer_checkBox")
        self.DebugText_checkBox = QtWidgets.QCheckBox(self.Utility_groupBox)
        self.DebugText_checkBox.setGeometry(QtCore.QRect(140, 60, 121, 31))
        self.DebugText_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.DebugText_checkBox.setObjectName("DebugText_checkBox")
        self.FreeCraft_checkBox = QtWidgets.QCheckBox(self.Utility_groupBox)
        self.FreeCraft_checkBox.setGeometry(QtCore.QRect(10, 90, 121, 31))
        self.FreeCraft_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.FreeCraft_checkBox.setObjectName("FreeCraft_checkBox")
        self.UnlockDLC_checkBox = QtWidgets.QCheckBox(self.Utility_groupBox)
        self.UnlockDLC_checkBox.setGeometry(QtCore.QRect(140, 90, 121, 31))
        self.UnlockDLC_checkBox.setStyleSheet("QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #FFFFFF;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 38px;\n"
"  height: 38px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"QCheckBox:indicator:checked {\n"
"    image: url(:/Icons/switch-on.svg);\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked {\n"
"    image: url(:/Icons/switch-off.svg);\n"
"}")
        self.UnlockDLC_checkBox.setObjectName("UnlockDLC_checkBox")
        self.tabWidget.addTab(self.General_Tab, "")
        self.Misc_Tab = QtWidgets.QWidget()
        self.Misc_Tab.setObjectName("Misc_Tab")
        self.label = QtWidgets.QLabel(self.Misc_Tab)
        self.label.setGeometry(QtCore.QRect(160, 90, 241, 241))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Icons/UnderConstruction.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.Misc_Tab, "")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 500, 571, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Connection_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.Connection_lineEdit.setStyleSheet("color: #FFFFFF;\n"
"font: 800 10pt \"Noto Serif Lao\";\n"
"background-color: #2C2C2C;\n"
"height: 20px;\n"
"border: 2px solid #FF0000; /* #8A4DAA for valid */\n"
"border-width: 0 0 2px 0;\n"
"padding: 8px 16px ;\n"
"border-radius: 15px;")
        self.Connection_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Connection_lineEdit.setObjectName("Connection_lineEdit")
        self.horizontalLayout.addWidget(self.Connection_lineEdit)
        self.Connection_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Connection_pushButton.setEnabled(True)
        self.Connection_pushButton.setStyleSheet("QPushButton {\n"
"    font: 800 9pt \"Noto Serif Lao\";\n"
"    color: #FFFFFF;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.658, fx:0.5, fy:0.500364, stop:0 rgba(138, 77, 170, 255), stop:1 rgba(197, 110, 244, 255));\n"
"    border: 2px solid #8A4DAA;\n"
"    border-radius: 15px;\n"
"    padding: 8px 16px;\n"
"    height: 20px;\n"
"    text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #31363B;\n"
"    background-color: #9B60C2;\n"
"    border: 2px solid #9B60C2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #4D4D4D;\n"
"    border: 2px solid #4D4D4D;\n"
"}")
        self.Connection_pushButton.setObjectName("Connection_pushButton")
        self.horizontalLayout.addWidget(self.Connection_pushButton)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 492, 570, 3))
        self.line.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.658, fx:0.5, fy:0.500364, stop:0 rgba(138, 77, 170, 255), stop:1 rgba(197, 110, 244, 255));\n"
"border-radius: 15px;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ProtonClient"))
        self.Combat_groupBox.setTitle(_translate("MainWindow", "Combat"))
        self.Combo_checkBox.setText(_translate("MainWindow", "Combo\n"
"(Host Only)"))
        self.Macro_checkBox.setText(_translate("MainWindow", "Macro"))
        self.BowSpam_checkBox.setText(_translate("MainWindow", "Bow Spam"))
        self.RiptideZR_checkBox.setText(_translate("MainWindow", "Riptide [ZR]"))
        self.Reach_checkBox.setText(_translate("MainWindow", "Reach"))
        self.KillAura_checkBox.setText(_translate("MainWindow", "Kill Aura"))
        self.RiptideNoRain_checkBox.setText(_translate("MainWindow", "Riptide"))
        self.Visual_groupBox.setTitle(_translate("MainWindow", "Combat Visual"))
        self.Hitbox_checkBox.setText(_translate("MainWindow", "Show Hitbox"))
        self.ESP_checkBox.setText(_translate("MainWindow", "ESP"))
        self.HitboxXRAY_checkBox.setText(_translate("MainWindow", "Hitbox XRAY"))
        self.HPDisplay_checkBox.setText(_translate("MainWindow", "HP Display"))
        self.ArmorHud_checkBox.setText(_translate("MainWindow", "Armor HUD"))
        self.Movement_groupBox.setTitle(_translate("MainWindow", "Movement"))
        self.Fly_checkBox.setText(_translate("MainWindow", "Fly"))
        self.SwimFly_checkBox.setText(_translate("MainWindow", "Swim Fly"))
        self.AutoSprint_checkBox.setText(_translate("MainWindow", "AutoSprint"))
        self.NoSlowdown_checkBox.setText(_translate("MainWindow", "No Slowdown"))
        self.BHop_checkBox.setText(_translate("MainWindow", "B-Hop"))
        self.NoKnockback_checkBox.setText(_translate("MainWindow", "No Knockback"))
        self.Adjustable_groupBox.setTitle(_translate("MainWindow", "Adjustable"))
        self.Speed_label.setText(_translate("MainWindow", "Speed Lvl"))
        self.Hitbox_label.setText(_translate("MainWindow", "Hitbox Lvl"))
        self.Aimbot_label.setText(_translate("MainWindow", "AimBot"))
        self.Aimbot_comboBox.setItemText(0, _translate("MainWindow", "Disable"))
        self.Aimbot_comboBox.setItemText(1, _translate("MainWindow", "Entity Aim"))
        self.Aimbot_comboBox.setItemText(2, _translate("MainWindow", "Player Aim"))
        self.Utility_groupBox.setTitle(_translate("MainWindow", "Utility"))
        self.FOF_checkBox.setText(_translate("MainWindow", "FOF Bypass"))
        self.AntiBan_checkBox.setText(_translate("MainWindow", "Anti-Ban"))
        self.LockServer_checkBox.setText(_translate("MainWindow", "Lock Server"))
        self.DebugText_checkBox.setText(_translate("MainWindow", "Debug Text"))
        self.FreeCraft_checkBox.setText(_translate("MainWindow", "Free Craft"))
        self.UnlockDLC_checkBox.setText(_translate("MainWindow", "Unlock DLC"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.General_Tab), _translate("MainWindow", "General"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Misc_Tab), _translate("MainWindow", "Misc"))
        self.Connection_lineEdit.setPlaceholderText(_translate("MainWindow", "Wii U IPv4"))
        self.Connection_pushButton.setText(_translate("MainWindow", "connect"))
