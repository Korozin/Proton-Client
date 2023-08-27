# Global Imports #
from PyQt5 import QtWidgets
from functools import partial

# Local Imports #
from Classes import Codes
from Classes import uGecko
from Classes import ExtWindow
from Classes import Verification
from Classes import RichPresence
from Classes import ProtonClient_GUI



class ProtonClient_Main(QtWidgets.QMainWindow, ProtonClient_GUI.Ui_MainWindow):
    def __init__(self):
        super(ProtonClient_Main, self).__init__()

        # Set up base GUI parameters
        self.setupUi(self)
        self.Set_Functions()
        self.Change_All_States(False)

        # Set vars
        self.connected = False


    def Set_Functions(self):
        self.Connection_lineEdit.textChanged.connect(self.Validate_IP)
        self.Connection_pushButton.clicked.connect(self.Connect)
        self.Aimbot_comboBox.activated.connect(self.Aimbot_Toggle)

        ''' Simple Kernel Writes '''
        checkboxes = [
            # Combat Section
            (self.Combo_checkBox, 275144224, 1090519040, 1056964608),
            (self.Macro_checkBox, 277744780, 3196059648, 1048576000),
            (self.BowSpam_checkBox, 35008260, 1004535809, 1004535828),
            (self.ArmorHud_checkBox, 48869808, 2145713016, 2143613816),
            (self.KillAura_checkBox, 274585928, 1090519040, 1056964608),
            (self.RiptideNoRain_checkBox, 36880912, 945815553, 945815552),
            (self.RiptideZR_checkBox, 52384900, 2288190352, 2288192008),
            (self.Hitbox_checkBox, 51355668, 738787329, 738787328),
            # Movement Section
            (self.Fly_checkBox, 41003636, 945815553, 2145647480),
            (self.SwimFly_checkBox, 39184412, 939524097, 939524096),
            (self.AutoSprint_checkBox, 52318436, 1317011488, 2147682504),
            (self.NoSlowdown_checkBox, 277745248, 1065353216, 1045220557),
            (self.NoKnockback_checkBox, 39311452, 1317011488, 2485256104),
            # Utility Section
            (self.AntiBan_checkBox, 54580264, 1317011488, 2080899750),
            (self.LockServer_checkBox, 49662084, 945815553, 945815552),
            (self.DebugText_checkBox, 49662068, 945815553, 945815552),
            (self.UnlockDLC_checkBox, 44993328, 945815553, 945815552)
        ]

        for checkbox, a, v, o in checkboxes:
            checkbox.stateChanged.connect(partial(self.Simple_Kernel_Write, address=a, value=v, origin=o))

        ''' Multi-Line Kernel Writes '''
        checkboxes = [
            # Combat Section
            (self.Reach_checkBox, Codes.Reach_Enabled, Codes.Reach_Disabled),
            (self.HitboxXRAY_checkBox, Codes.HitboxXRAY_Enabled, Codes.HitboxXRAY_Disabled),
            (self.HPDisplay_checkBox, Codes.HPDisplay_Enabled, Codes.HPDisplay_Disabled),
            (self.ESP_checkBox, Codes.ESP_Enabled, Codes.ESP_Disabled),
            # Movement Section
            (self.BHop_checkBox, Codes.BHop_Enabled, Codes.BHop_Disabled),
            # Utility Section
            (self.FOF_checkBox, Codes.FOF_Enabled, Codes.FOF_Disabled),
            (self.FreeCraft_checkBox, Codes.FreeCraft_Enabled, Codes.FreeCraft_Disabled)
        ]

        for checkbox, ev, dv in checkboxes:
            checkbox.stateChanged.connect(partial(self.MultiLine_Kernel_Write, Enabled_Values=ev, Disabled_Values=dv))

        ''' Slider Functions '''
        sliders = [
            (self.Hitbox_horizontalSlider, "Hitbox"),
            (self.Speed_horizontalSlider, "Speed")
        ]

        for slider, typing in sliders:
            slider.valueChanged.connect(partial(self.Slider_Kernel_Write, slider_type=typing))


    def Show_Modal(self, Title, GroupBoxText, FieldText, ButtonText):
        window_dialog = QtWidgets.QDialog(self)
        window_ui = ExtWindow.Ui_Form(Title, GroupBoxText, FieldText, ButtonText)
        window_ui.setupUi(window_dialog)
        window_ui.pushButton.clicked.connect(window_dialog.accept)
        window_dialog.exec_()


    def Change_All_States(self, state):
        self.Combat_groupBox.setEnabled(state)
        self.Visual_groupBox.setEnabled(state)
        self.Movement_groupBox.setEnabled(state)
        self.Utility_groupBox.setEnabled(state)
        self.Adjustable_groupBox.setEnabled(state)


    def Validate_IP(self):
        if Verification.IP_Verification(self.Connection_lineEdit.text()):
                self.Connection_lineEdit.setStyleSheet(self.Connection_lineEdit.styleSheet() + "border-bottom: 2px solid #8A4DAA;")
                self.Connection_pushButton.setEnabled(True)
        else:
                self.Connection_lineEdit.setStyleSheet(self.Connection_lineEdit.styleSheet() + "border-bottom: 2px solid #FF0000;")
                self.Connection_pushButton.setEnabled(False)


    def Connect(self):
        try:
            if not self.connected:
                self.tcp_con = uGecko.uGecko(self.Connection_lineEdit.text())
                self.tcp_con.connect()
                self.Connection_pushButton.setText("Disconnect")
                self.connected = True
                self.Change_All_States(self.connected)
                rpc.update_connection_state(self.connected)
            else:
                self.Connection_pushButton.setText("Connect")
                self.tcp_con.disconnect()
                self.connected = False
                self.Change_All_States(self.connected)
                rpc.update_connection_state(self.connected)
        except Exception as e:
                self.Show_Modal("Error!", "Connection Error!", f"{e}", "OK")


    def Simple_Kernel_Write(self, state, address, value, origin):
        if state == 2:
            self.tcp_con.kernelWrite(address, value)
        elif state == 0:
            self.tcp_con.kernelWrite(address, origin)


    def MultiLine_Kernel_Write(self, state, Enabled_Values, Disabled_Values):
        if state == 2:
            lines = Enabled_Values.split("\n")
        elif state == 0:
            if Disabled_Values == None:
                self.Show_Modal("Oh, Snap!", "Disabling Unsupported...", f"Unfortunately this code doesn't have a disable method.\nThis is usually due to it being long, and not having any undo lines.", "OK")
                return None
            else:
                lines = Disabled_Values.split("\n")

        for line in lines:
            address, value = line.split()
            self.tcp_con.kernelWrite(int(address), int(value))


    def Slider_Kernel_Write(self, level, slider_type):
        if slider_type == 'Hitbox':
            level_map = Codes.Hitbox_Level_Map
            prefix = level_map["address"]
        elif slider_type == 'Speed':
            level_map = Codes.Speed_Level_Map
            prefix = level_map["address"]
        else:
            self.tcp_con.kernelWrite("Invalid slider type")
            return

        if level in level_map:
            self.tcp_con.kernelWrite(prefix, level_map[level])


    def Aimbot_Toggle(self):
        current_text = self.Aimbot_comboBox.currentText()

        options = {
            "Disable": [(67109476, 1610612736)],

            "Entity Aim": [(67109476, 1610612736),
                           (67111096, 2158231608),
                           (67111100, 2160328764),
                           (67111784, 2156134456),
                           (67109476, 1207961108)],

            "Player Aim": [(67109476, 1610612736),
                           (67111096, 2158231752),
                           (67111100, 2160328908),
                           (67109476, 1207961108)]
        }

        if current_text in options:
            for option in options[current_text]:
                self.tcp_con.kernelWrite(option[0], option[1])



if __name__ == "__main__":
    import sys
    ProtonClient_App = QtWidgets.QApplication(sys.argv)
    ProtonClient_Var = ProtonClient_Main()

    # Create an instance of the ProtonClientRPC class
    rpc = RichPresence.ProtonClientRPC(
        client_id = "1143633642690723923",
        main_image_key = "proton_main",
        connected_image_key = "proton_connected",
        disconnected_image_key = "proton_disconnected"
    )
    rpc.start_presence()

    ProtonClient_Var.show()
    ProtonClient_App.aboutToQuit.connect(rpc.stop_presence)
    sys.exit(ProtonClient_App.exec_())
