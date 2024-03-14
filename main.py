import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QComboBox, QTextEdit, QLineEdit, QFileDialog
import qdarkstyle
import random

class ConfigGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Ai gen for celex/severe saaaaaal1')
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        game_label = QLabel('Select Game:')
        self.game_combobox = QComboBox()
        self.game_combobox.addItems(['Da Hood'])

        latency_label = QLabel('Latency (ms):')
        self.latency_edit = QLineEdit()

        config_type_label = QLabel('Select External:')
        self.config_type_combobox = QComboBox()
        self.config_type_combobox.addItems(['Severe', 'Celex'])

        self.generate_button = QPushButton('Generate Config')
        self.generate_button.clicked.connect(self.generate_config)

        self.save_button = QPushButton('Save As')
        self.save_button.clicked.connect(self.save_config_as)

        layout.addWidget(game_label)
        layout.addWidget(self.game_combobox)
        layout.addWidget(latency_label)
        layout.addWidget(self.latency_edit)
        layout.addWidget(config_type_label)
        layout.addWidget(self.config_type_combobox)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.save_button)

        self.output_edit = QTextEdit()
        self.output_edit.setReadOnly(True)
        layout.addWidget(self.output_edit)

        self.setLayout(layout)

    def calculate_prediction(self, latency):
        pred_x = 7.317 + -0.01578 * latency
        pred_y = 8 + -0.01608 * latency
        return pred_x, pred_y

    def generate_config(self):
        game = self.game_combobox.currentText().strip()
        latency = self.latency_edit.text().strip()
        config_type = self.config_type_combobox.currentText()

        if game.lower() != 'da hood':
            self.show_message_box('Error', 'Only "Da Hood" is supported.')
            return

        if not latency.isdigit():
            self.show_message_box('Error', 'Latency must be a number.')
            return

        latency = int(latency)

        if config_type == 'Celex':
            pred_x, pred_y = self.calculate_prediction(latency)
            config_template = f"""
aimbot-enabled = "1";
aimbot-smoothing = "1";
camera-smoothing = "1";
aimbot-sensitivity = "1";
aimbot-bind = "67";
aimbot-bind-mode = "1";
aimbot-part = "2";
streamproof = "0";
v-sync = "1";
show_name = "0";
show_boxes = "0";
show_fov = "0";
show_deadzone = "0";
show_tracers = "0";
prediction = "1";
stickyaim = "1";
teamcheck = "0";
knockcheck = "0";
aimbot-fov = "93";
filled_fov = "0";
aimbot-deadzone = "0";
filled_deadzone = "0";
pred_x = "{pred_x}";  
pred_y = "{pred_y}";  
x_offset = "0";
y_offset = "0";
deadzone_flag = "0";
fov_flag = "0";
prediction_dot = "0";
pred_dot_type = "0";
tracer_type = "0";
shake = "0";
shake_x = "0";
shake_y = "0";
box_type = "0";
aimbot_type = "1";
no_jump = "0";
"""
        elif config_type == 'Severe':
            pred_x, pred_y = self.calculate_prediction(latency)
            config_template = f"""
1-waypoint = "PlaceHolder:[position]-(0.000000,0.000000,0.000000)";
prediction_type = "Dynamic";
transform = "WorldToScreenPoint";
type = "2D_AABB";
tname = "Username";
box = "Box";
bot = "Mouse";
apart = "HumanoidRootPart";
a_type = "Linear";
s_type = "Bodyshot";
cbased = "internal";
aim_key_name = "SIDE_MOUSE";
font = "proxyma_condensed";
vallign = "Buttom_Left";
cursor_url = "none";
background_url = "none";
macro_pov = "third_person";
macrokey = "E";
shape = "Sphere";
tp_part = "Head";
tp_method = "behind";
flightkey = "F";
walkspeedkey = "G";
ragekey = "Q";
setkey = "V";
back_allign_x = "0";
back_allign_y = "0";
tip_allign = "30";
fov = "70";
pred_x = "{pred_x}";  
pred_y = "{pred_y}";  
drop = "0";
speed = "0.4";
stablization = "0.3";
distance = "500";
adistance = "4416.16";
vdistance = "100";
clsplr_d = "100";
cdistance = "150";
view = "10.987";
thickness = "4.664";
restrictor = "0.539";
noise = "0";
intensity = "20";
dfov = "0";
chealth = "3";
radius = "150";
hair_size = "10";
zoom = "0.5";
ping_delay = "2";
smoothness = "1";
strength = "2";
multipiler = "0";
flight_speed = "5";
transport_speed = "1";
decreaser = "0";
increaser = "1";
sensitivity = "1";
avatar_allign = "608";
vert_dec = "15";
unlock_on_death = "1";
bounce = "0";
show_avatar = "1";
lock_indicator = "1";
speed_stab = "0";
enb_stab = "0";
sensitive = "0";
sound = "0";
abs_v = "0";
hide_cursor = "0";
anti_ground = "0";
keybind_logger = "0";
server_transparent = "0";
display_server = "0";
waypoints = "0";
visualize_waypoint = "0";
high_transport = "0";
rage_fov = "0";
radar_value = "0";
rage_snaplines = "0";
hold_rage = "0";
look_at_plr = "0";
rage_teleport = "0";
unlock_reload = "0";
manipulate_loop = "0";
manipulate_char = "0";
gun_check = "0";
character_fly = "0";
client_lag = "1";
show_prediction = "0";
mouse_tp = "0";
material_esp = "0";
m_toggle = "0";
auto_macro = "0";
auto_scroll = "1";
unlock_knockout = "0";
smart_fov = "1";
rdirections = "1";
radar = "0";
crosshair = "0";
offscreen = "0";
certain_health = "0";
toggle = "1";
disable_images = "0";
fov_zone = "0";
vdotted = "0";
c_allign = "0";
dmg_indicator = "0";
vtransprent = "1";
ping_interpolation = "0";
snaplines_a = "0";
snaplines_v = "0";
chams = "0";
cfilled = "0";
cflat = "0";
limit = "0";
center = "0";
allign = "1";
loutline = "1";
background = "1";
indicator = "1";
stats = "0";
name = "1";
lhealth = "0";
override = "0";
team_check = "1";
invisible_check = "0";
ffield_check = "0";
close_ind = "1";
close_camera = "0";
sticky_aim = "0";
ohealth = "1";
esp_box = "0";
esp_ground = "1";
esp_bone = "0";
forientation = "0";
ooutline = "1";
arc_bar = "1";
sfont = "1";
oname = "1";
aimbot = "1";
amplify = "0";
vision = "1";
CAPS = "1";
circle_filled = "0";
cfilled_hcolor = "0";
box_filled = "0";
bfilled_hcolor = "0";
chams_filled = "0";
hfilled_hcolor = "0";
fov_circle = "1";
dotted = "0";
perlin_noise = "0";
auto_reload = "0";
arsenal_hitbox = "1";
fly_hold = "0";
gun_chams = "0";
aim_delay = "0";
delay = "70";
walkspeed = "80";
jumppower = "80";
aim_key = "5";
flight = "70";
macro = "69";
walkspeedk = "71";
m_delay = "25";
range = "10";
rage_size = "30";
"""

        else:
            self.show_message_box('Error', 'Invalid config type selected.')
            return

        self.output_edit.clear()
        self.output_edit.append(config_template)
        self.show_message_box('Success', 'Config generated successfully.')

    def save_config_as(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Config As", "", "Config Files (*.cfg);;All Files (*)", options=options)
        if fileName:
            with open(fileName, "w") as file:
                file.write(self.output_edit.toPlainText())
            self.show_message_box('Success', f'Config saved as {fileName}')

    def show_message_box(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = ConfigGenerator()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
