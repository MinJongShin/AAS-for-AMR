'''from basyx.aas.model import AssetInformation, AssetKind, Property, datatypes, AssetAdministrationShell, Submodel, ModelReference, DictObjectStore
from basyx.aas.adapter import json as aas_json
import time

# Create asset information
asset_information = AssetInformation(
    asset_kind=AssetKind.INSTANCE,
    global_asset_id='AIoT_SerBOT'
)

# Create AAS
aas = AssetAdministrationShell(
    id_='IAI_AMR_1',
    asset_information=asset_information
)

# Create submodel for identification
submodel_identifier = Submodel(id_='identifier')
property_manufacturer = Property(id_short='manufacturer', value_type=datatypes.String, value='amrcompany')
property_supplier = Property(id_short='supplier', value_type=datatypes.String, value='amrcompany')
submodel_identifier.submodel_element.add(property_manufacturer)
submodel_identifier.submodel_element.add(property_supplier)

# Soda_OS 서브모델 생성
soda_os = Submodel(
    id_="Soda_OS"
)

# OS Information 속성 추가
os_info_property = Property(
    id_short="OS_Information",
    value="Soda OS, Linux Kernel 4.19",
    value_type=datatypes.String
)

# Desktop 환경 속성 추가
desktop_property = Property(
    id_short="Desktop_Environment",
    value="X-Server, Openbox, LightDM, Tint2, blueman, network-manager, conky",
    value_type=datatypes.String
)

# CLI 환경 속성 추가
cli_property = Property(
    id_short="CLI_Environment",
    value="Zsh, Tmux, Peco, powerlevel9k theme, Powerline fonts",
    value_type=datatypes.String
)

# Tool Chain 속성 추가
tool_chain_property = Property(
    id_short="Tool_Chain",
    value="GCC 9, JDK, Node JS, Python3, Clang",
    value_type=datatypes.String
)

# IDE 속성 추가
ide_property = Property(
    id_short="IDE",
    value="Visual Studio Code, NeoVim, Geany",
    value_type=datatypes.String
)

# Connectivity 속성 추가
connectivity_property = Property(
    id_short="Connectivity",
    value="Mosquitto(MQTT), Bluez, mtr, nmap, iptraf, Samba, Blynk Server, Remote Desktop Server",
    value_type=datatypes.String
)

# Multimedia 속성 추가
multimedia_property = Property(
    id_short="Multimedia",
    value="portaudio, sox, OpenCV 4, snowboy, Google Assistant",
    value_type=datatypes.String
)

# Data Science & AI 속성 추가
data_science_property = Property(
    id_short="Data_Science_and_AI",
    value="Python3, Numpy, Matplotlib, sympy, Pandas, Seaborn, Scipy, Gym, Scikit-learn, Tensorflow, Keras",
    value_type=datatypes.String
)

# Soda_OS 서브모델에 속성들 추가
soda_os.submodel_element.add(os_info_property)
soda_os.submodel_element.add(desktop_property)
soda_os.submodel_element.add(cli_property)
soda_os.submodel_element.add(tool_chain_property)
soda_os.submodel_element.add(ide_property)
soda_os.submodel_element.add(connectivity_property)
soda_os.submodel_element.add(multimedia_property)
soda_os.submodel_element.add(data_science_property)

# Pop_Library 서브모델 생성
pop_library = Submodel(
    id_="Pop_Library"
)

# Output Object 속성 추가
output_object_property = Property(
    id_short="Output_Object",
    value="(C/C++, Python3): Led, Laser, Buzzer, Relay, RGBLed, DCMotor, StepMotor, OLed, PiezoBuzzer, PixelDisplay, TextLCD, FND, Led Bar",
    value_type=datatypes.String
)

# Input Object 속성 추가
input_object_property = Property(
    id_short="Input_Object",
    value="(C/C++, Python3): Switch, Touch, Reed, LimitSwitch, Mercury, Knock, Tilt, Opto, Pir, Flame, LineTrace, TempHumi, UltraSonic, Shock, Sound, Potentiometer, CdS, SoilMoisture, Thermistor, Temperature, Gas, Dust, Psd, Gesture",
    value_type=datatypes.String
)

# Multimedia 속성 추가
multimedia_property = Property(
    id_short="Multimedia",
    value="(Python3): AudioPlay, AudioPlayList, AudioRecord, Tone, SoundMeter",
    value_type=datatypes.String
)

# Voice Assistant 속성 추가
voice_assistant_property = Property(
    id_short="Voice_Assistant",
    value="(Python3): GAssistant, create_conversation_stream",
    value_type=datatypes.String
)

# AI 속성 추가
ai_property = Property(
    id_short="AI",
    value="(Python3): Linear Regression, Logistic Regression, Perceptron, ANN, DNN, CNN, DQN",
    value_type=datatypes.String
)

# Pop_Library 서브모델에 속성들 추가
pop_library.submodel_element.add(output_object_property)
pop_library.submodel_element.add(input_object_property)
pop_library.submodel_element.add(multimedia_property)
pop_library.submodel_element.add(voice_assistant_property)
pop_library.submodel_element.add(ai_property)

# Motor Control Board 서브모델 생성
motor_control_board = Submodel(
    id_="Motor_Control_Board"
)

# 배터리 속성 추가
battery_voltage_property = Property(
    id_short="Battery_Voltage",
    value="11.1V",  # 배터리 전압
    value_type=datatypes.String
)

battery_capacity_property = Property(
    id_short="Battery_Capacity",
    value="14000mA",  # 배터리 용량
    value_type=datatypes.String
)

# 바퀴 속성 추가
wheels_type_property = Property(
    id_short="Wheels_Type",
    value="Omni-Wheels",  # 바퀴 유형
    value_type=datatypes.String
)

wheels_count_property = Property(
    id_short="Wheels_Count",
    value=3,  # 바퀴 개수
    value_type=datatypes.Integer
)

# 모터 속성 추가
motor_voltage_property = Property(
    id_short="Motor_Voltage",
    value="12V",  # 모터 전압
    value_type=datatypes.String
)

motor_count_property = Property(
    id_short="Motor_Count",
    value=3,  # 모터 개수
    value_type=datatypes.Integer
)

gear_rate_property = Property(
    id_short="Gear_Rate",
    value="1:50",  # 기어 비율
    value_type=datatypes.String
)

motor_speed_property = Property(
    id_short="Motor_Speed",
    value="6000RPM",  # 모터 속도
    value_type=datatypes.String
)

# 속성들을 Motor Control Board 서브모델에 추가
motor_control_board.submodel_element.add(battery_voltage_property)
motor_control_board.submodel_element.add(battery_capacity_property)
motor_control_board.submodel_element.add(wheels_type_property)
motor_control_board.submodel_element.add(wheels_count_property)
motor_control_board.submodel_element.add(motor_voltage_property)
motor_control_board.submodel_element.add(motor_count_property)
motor_control_board.submodel_element.add(gear_rate_property)
motor_control_board.submodel_element.add(motor_speed_property)

# Main Module 서브모델 생성
main_module = Submodel(
    id_="Main_Module"
)

# CPU 속성 추가
cpu_property = Property(
    id_short="CPU",
    value="Quad-Core ARM A57 @ 1.43 GHz",
    value_type=datatypes.String
)

# GPU 속성 추가
gpu_property = Property(
    id_short="GPU",
    value="Maxwell Core 128EA",
    value_type=datatypes.String
)

# Memory 속성 추가
memory_property = Property(
    id_short="Memory",
    value="4GB 64-bit LPDDR4 25.6 GB/s",
    value_type=datatypes.String
)

# Storage 속성 추가
storage_property = Property(
    id_short="Storage",
    value="MicroSD (64GB)",
    value_type=datatypes.String
)

# Video Encoder 속성 추가
video_encoder_property = Property(
    id_short="Video_Encoder",
    value="4K@30 | 4x 1080p@30 | 9x 720p@30 (H.264/H.265)",
    value_type=datatypes.String
)

# Video Decoder 속성 추가
video_decoder_property = Property(
    id_short="Video_Decoder",
    value="4K@60 | 2x 4K@30 | 8x 1080p@30 | 18x 720p@30 (H.264/H.265)",
    value_type=datatypes.String
)

# Camera 속성 추가
camera_property = Property(
    id_short="Camera",
    value="MIPI CSI-2 DPHY Lanes",
    value_type=datatypes.String
)

# Connectivity 속성 추가
connectivity_property = Property(
    id_short="Connectivity",
    value="Dual Band Wireless Wi-Fi 2GHz/5GHz Band, 867Mbps, 802.11ac, Bluetooth 4.2, Gigabit Ethernet",
    value_type=datatypes.String
)

# Display 속성 추가
display_property = Property(
    id_short="Display",
    value="HDMI and Display Port",
    value_type=datatypes.String
)

# USB 속성 추가
usb_property = Property(
    id_short="USB",
    value="4x USB 3.0, USB 2.0 Micro-B",
    value_type=datatypes.String
)

# 속성들을 Main Module 서브모델에 추가
main_module.submodel_element.add(cpu_property)
main_module.submodel_element.add(gpu_property)
main_module.submodel_element.add(memory_property)
main_module.submodel_element.add(storage_property)
main_module.submodel_element.add(video_encoder_property)
main_module.submodel_element.add(video_decoder_property)
main_module.submodel_element.add(camera_property)
main_module.submodel_element.add(connectivity_property)
main_module.submodel_element.add(display_property)
main_module.submodel_element.add(usb_property)

# Base_Board 서브모델 생성
base_board = Submodel(
    id_="Base_Board"
)

# Microphone 속성 추가
microphone_property = Property(
    id_short="Microphone",
    value="High Performance Digital Microphone x 4EA, Sensitivity: -26 dBFS (Omnidirectional), Acoustic Overload Point: 120dBSPL, SNR: 63dB",
    value_type=datatypes.String
)

# Speaker 속성 추가
speaker_property = Property(
    id_short="Speaker",
    value="Output: 3W x 2EA, 3.5mm Audio Jack, Frequency Response: 30Hz ~ 20KHz",
    value_type=datatypes.String
)

# Sensor Module Interface 속성 추가
sensor_module_interface_property = Property(
    id_short="Sensor_Module_Interface",
    value="Block 4EA +5V, +3.3V, GND, I2C, ADC, GPIO, SPI",
    value_type=datatypes.String
)

# 6-Axis Sensor 속성 추가
six_axis_sensor_property = Property(
    id_short="six_Axis_Sensor",
    value="MPU6050N, Resolution: 16bit, Gyroscope Range: +-250, +-500, +-1000, +-2000°/S, Accelerometer Range: +-2, +-4, +-8, +-18g",
    value_type=datatypes.String
)

# Camera 속성 추가
camera_property = Property(
    id_short="Camera",
    value="Image Sensor: Sony IMX219, Resolution: 8M Pixel (3280 x 2464 Pixel Static Images), Video: 1080p30, 720p60, 640x480p90, Angle of View: 160 Degrees",
    value_type=datatypes.String
)

# LCD 속성 추가
lcd_property = Property(
    id_short="LCD",
    value="7inch TFT LCD, HDMI, Resolution: 1024 x 600",
    value_type=datatypes.String
)

# Weight 속성 추가
weight_property = Property(
    id_short="Weight",
    value="5.2Kg",
    value_type=datatypes.String
)

# Size 속성 추가
size_property = Property(
    id_short="Size",
    value="290 X 290 X 310 (mm)",
    value_type=datatypes.String
)

# Basic Module 속성 추가
basic_module_property = Property(
    id_short="Basic_Module",
    value="Input Device: Tact Switch x 2EA(GPIO), Output Device: LED 8EA(I2C), Actuator: Passive Buzzer(GPIO)",
    value_type=datatypes.String
)

# 속성들을 Base_Board 서브모델에 추가
base_board.submodel_element.add(microphone_property)
base_board.submodel_element.add(speaker_property)
base_board.submodel_element.add(sensor_module_interface_property)
base_board.submodel_element.add(six_axis_sensor_property)
base_board.submodel_element.add(camera_property)
base_board.submodel_element.add(lcd_property)
base_board.submodel_element.add(weight_property)
base_board.submodel_element.add(size_property)
base_board.submodel_element.add(basic_module_property)

# 서브모델 생성 (operation)
submodel_operation = Submodel(
    id_="operation"
)

# on/off 상태 프로퍼티 추가
property_on_off = Property(
    id_short="on_off_state",
    value_type=datatypes.Boolean,
    value=False  # 기본적으로 on 상태로 설정
)

# 현재 속도 프로퍼티 추가
property_operating_time = Property(
    id_short="operation_time",
    value_type=datatypes.Float,
    value=0.0  # 초기 속도는 0으로 설정
)

# 서브모델에 프로퍼티 추가
submodel_operation.submodel_element.add(property_on_off)
submodel_operation.submodel_element.add(property_operating_time)

# Submodel들을 AAS에 추가
aas.submodel.add(ModelReference.from_referable(submodel_identifier))
aas.submodel.add(ModelReference.from_referable(soda_os))
aas.submodel.add(ModelReference.from_referable(pop_library))
aas.submodel.add(ModelReference.from_referable(motor_control_board))
aas.submodel.add(ModelReference.from_referable(main_module))
aas.submodel.add(ModelReference.from_referable(base_board))
aas.submodel.add(ModelReference.from_referable(submodel_operation))

# AAS를 DictObjectStore에 저장
aas_store = DictObjectStore()
aas_store.add(aas)
aas_store.add(submodel_identifier)
aas_store.add(soda_os)
aas_store.add(pop_library)
aas_store.add(motor_control_board)
aas_store.add(main_module)
aas_store.add(base_board)
aas_store.add(submodel_operation)

# AAS를 JSON으로 직렬화
with open('AMR_AAS.json', 'w', encoding='utf-8') as json_file:
    aas_json.write_aas_json_file(json_file, aas_store)  # AAS store 직렬화

try:
    while True:
        # 외부로부터 새로운 데이터 수신 (여기선 임시값으로 처리)
        new_on_off_state = True  # 예시: 로봇이 작동 중인 상태
        new_speed = 3.5  # 예시: 로봇의 현재 속도 (예: 3.5 m/s)

        # 동적 프로퍼티 값 업데이트
        property_on_off.value = new_on_off_state
        property_operating_time.value = new_speed

        # AAS에 저장된 값 업데이트 (필요 시 JSON으로 저장)
        with open('AMR_AAS.json', 'w', encoding='utf-8') as json_file:
            aas_json.write_aas_json_file(json_file, aas_store)

        print('on-off state: ', new_on_off_state, 'speed: ', new_speed)

        # 5초 대기 후 값 갱신
        time.sleep(5)

except KeyboardInterrupt:
    print("Operation stopped by user")


import json

# JSON 파일 불러오기
with open('AMR_AAS.json', 'r', encoding='utf-8') as json_file:
    aas_data = json.load(json_file)


# 가공된 데이터를 JSON 파일로 저장
with open('AMR_AAS2.json', 'w', encoding='utf-8') as json_file:
    json.dump(aas_data, json_file, indent=4, sort_keys=True, ensure_ascii=False)'''







'''from basyx.aas.model import AssetInformation, AssetKind, Property, datatypes, AssetAdministrationShell, Submodel, ModelReference, DictObjectStore
from basyx.aas.adapter import json as aas_json
import time

# Create asset information
asset_information = AssetInformation(
    asset_kind=AssetKind.INSTANCE,
    global_asset_id='AIoT_SerBOT'
)

# Create AAS
aas = AssetAdministrationShell(
    id_='IAI_AMR_1',
    asset_information=asset_information
)

# Create submodel for identification
submodel_identifier = Submodel(id_='identifier')
property_manufacturer = Property(id_short='manufacturer', value_type=datatypes.String, value='amrcompany')
property_supplier = Property(id_short='supplier', value_type=datatypes.String, value='amrcompany')
submodel_identifier.submodel_element.add(property_manufacturer)
submodel_identifier.submodel_element.add(property_supplier)

# Soda_OS 서브모델 생성
soda_os = Submodel(
    id_="Soda_OS"
)

# OS Information 속성 추가
os_info_property = Property(
    id_short="OS_Information",
    value="Soda OS, Linux Kernel 4.19",
    value_type=datatypes.String
)

# Desktop 환경 속성 추가
desktop_property = Property(
    id_short="Desktop_Environment",
    value="X-Server, Openbox, LightDM, Tint2, blueman, network-manager, conky",
    value_type=datatypes.String
)

# CLI 환경 속성 추가
cli_property = Property(
    id_short="CLI_Environment",
    value="Zsh, Tmux, Peco, powerlevel9k theme, Powerline fonts",
    value_type=datatypes.String
)

# Tool Chain 속성 추가
tool_chain_property = Property(
    id_short="Tool_Chain",
    value="GCC 9, JDK, Node JS, Python3, Clang",
    value_type=datatypes.String
)

# IDE 속성 추가
ide_property = Property(
    id_short="IDE",
    value="Visual Studio Code, NeoVim, Geany",
    value_type=datatypes.String
)

# Connectivity 속성 추가
connectivity_property = Property(
    id_short="Connectivity",
    value="Mosquitto(MQTT), Bluez, mtr, nmap, iptraf, Samba, Blynk Server, Remote Desktop Server",
    value_type=datatypes.String
)

# Multimedia 속성 추가
multimedia_property = Property(
    id_short="Multimedia",
    value="portaudio, sox, OpenCV 4, snowboy, Google Assistant",
    value_type=datatypes.String
)

# Data Science & AI 속성 추가
data_science_property = Property(
    id_short="Data_Science_and_AI",
    value="Python3, Numpy, Matplotlib, sympy, Pandas, Seaborn, Scipy, Gym, Scikit-learn, Tensorflow, Keras",
    value_type=datatypes.String
)

# Soda_OS 서브모델에 속성들 추가
soda_os.submodel_element.add(os_info_property)
soda_os.submodel_element.add(desktop_property)
soda_os.submodel_element.add(cli_property)
soda_os.submodel_element.add(tool_chain_property)
soda_os.submodel_element.add(ide_property)
soda_os.submodel_element.add(connectivity_property)
soda_os.submodel_element.add(multimedia_property)
soda_os.submodel_element.add(data_science_property)

# Pop_Library 서브모델 생성
pop_library = Submodel(
    id_="Pop_Library"
)

# Output Object 속성 추가
output_object_property = Property(
    id_short="Output_Object",
    value="(C/C++, Python3): Led, Laser, Buzzer, Relay, RGBLed, DCMotor, StepMotor, OLed, PiezoBuzzer, PixelDisplay, TextLCD, FND, Led Bar",
    value_type=datatypes.String
)

# Input Object 속성 추가
input_object_property = Property(
    id_short="Input_Object",
    value="(C/C++, Python3): Switch, Touch, Reed, LimitSwitch, Mercury, Knock, Tilt, Opto, Pir, Flame, LineTrace, TempHumi, UltraSonic, Shock, Sound, Potentiometer, CdS, SoilMoisture, Thermistor, Temperature, Gas, Dust, Psd, Gesture",
    value_type=datatypes.String
)

# Multimedia 속성 추가
multimedia_property = Property(
    id_short="Multimedia",
    value="(Python3): AudioPlay, AudioPlayList, AudioRecord, Tone, SoundMeter",
    value_type=datatypes.String
)

# Voice Assistant 속성 추가
voice_assistant_property = Property(
    id_short="Voice_Assistant",
    value="(Python3): GAssistant, create_conversation_stream",
    value_type=datatypes.String
)

# AI 속성 추가
ai_property = Property(
    id_short="AI",
    value="(Python3): Linear Regression, Logistic Regression, Perceptron, ANN, DNN, CNN, DQN",
    value_type=datatypes.String
)

# Pop_Library 서브모델에 속성들 추가
pop_library.submodel_element.add(output_object_property)
pop_library.submodel_element.add(input_object_property)
pop_library.submodel_element.add(multimedia_property)
pop_library.submodel_element.add(voice_assistant_property)
pop_library.submodel_element.add(ai_property)

# Motor Control Board 서브모델 생성
motor_control_board = Submodel(
    id_="Motor_Control_Board"
)

# 배터리 속성 추가
battery_voltage_property = Property(
    id_short="Battery_Voltage",
    value="11.1V",  # 배터리 전압
    value_type=datatypes.String
)

battery_capacity_property = Property(
    id_short="Battery_Capacity",
    value="14000mA",  # 배터리 용량
    value_type=datatypes.String
)

# 바퀴 속성 추가
wheels_type_property = Property(
    id_short="Wheels_Type",
    value="Omni-Wheels",  # 바퀴 유형
    value_type=datatypes.String
)

wheels_count_property = Property(
    id_short="Wheels_Count",
    value=3,  # 바퀴 개수
    value_type=datatypes.Integer
)

# 모터 속성 추가
motor_voltage_property = Property(
    id_short="Motor_Voltage",
    value="12V",  # 모터 전압
    value_type=datatypes.String
)

motor_count_property = Property(
    id_short="Motor_Count",
    value=3,  # 모터 개수
    value_type=datatypes.Integer
)

gear_rate_property = Property(
    id_short="Gear_Rate",
    value="1:50",  # 기어 비율
    value_type=datatypes.String
)

motor_speed_property = Property(
    id_short="Motor_Speed",
    value="6000RPM",  # 모터 속도
    value_type=datatypes.String
)

# 속성들을 Motor Control Board 서브모델에 추가
motor_control_board.submodel_element.add(battery_voltage_property)
motor_control_board.submodel_element.add(battery_capacity_property)
motor_control_board.submodel_element.add(wheels_type_property)
motor_control_board.submodel_element.add(wheels_count_property)
motor_control_board.submodel_element.add(motor_voltage_property)
motor_control_board.submodel_element.add(motor_count_property)
motor_control_board.submodel_element.add(gear_rate_property)
motor_control_board.submodel_element.add(motor_speed_property)

# Main Module 서브모델 생성
main_module = Submodel(
    id_="Main_Module"
)

# CPU 속성 추가
cpu_property = Property(
    id_short="CPU",
    value="Quad-Core ARM A57 @ 1.43 GHz",
    value_type=datatypes.String
)

# GPU 속성 추가
gpu_property = Property(
    id_short="GPU",
    value="Maxwell Core 128EA",
    value_type=datatypes.String
)

# Memory 속성 추가
memory_property = Property(
    id_short="Memory",
    value="4GB 64-bit LPDDR4 25.6 GB/s",
    value_type=datatypes.String
)

# Storage 속성 추가
storage_property = Property(
    id_short="Storage",
    value="MicroSD (64GB)",
    value_type=datatypes.String
)

# Video Encoder 속성 추가
video_encoder_property = Property(
    id_short="Video_Encoder",
    value="4K@30 | 4x 1080p@30 | 9x 720p@30 (H.264/H.265)",
    value_type=datatypes.String
)

# Video Decoder 속성 추가
video_decoder_property = Property(
    id_short="Video_Decoder",
    value="4K@60 | 2x 4K@30 | 8x 1080p@30 | 18x 720p@30 (H.264/H.265)",
    value_type=datatypes.String
)

# Camera 속성 추가
camera_property = Property(
    id_short="Camera",
    value="MIPI CSI-2 DPHY Lanes",
    value_type=datatypes.String
)

# Connectivity 속성 추가
connectivity_property = Property(
    id_short="Connectivity",
    value="Dual Band Wireless Wi-Fi 2GHz/5GHz Band, 867Mbps, 802.11ac, Bluetooth 4.2, Gigabit Ethernet",
    value_type=datatypes.String
)

# Display 속성 추가
display_property = Property(
    id_short="Display",
    value="HDMI and Display Port",
    value_type=datatypes.String
)

# USB 속성 추가
usb_property = Property(
    id_short="USB",
    value="4x USB 3.0, USB 2.0 Micro-B",
    value_type=datatypes.String
)

# 속성들을 Main Module 서브모델에 추가
main_module.submodel_element.add(cpu_property)
main_module.submodel_element.add(gpu_property)
main_module.submodel_element.add(memory_property)
main_module.submodel_element.add(storage_property)
main_module.submodel_element.add(video_encoder_property)
main_module.submodel_element.add(video_decoder_property)
main_module.submodel_element.add(camera_property)
main_module.submodel_element.add(connectivity_property)
main_module.submodel_element.add(display_property)
main_module.submodel_element.add(usb_property)

# Base_Board 서브모델 생성
base_board = Submodel(
    id_="Base_Board"
)

# Microphone 속성 추가
microphone_property = Property(
    id_short="Microphone",
    value="High Performance Digital Microphone x 4EA, Sensitivity: -26 dBFS (Omnidirectional), Acoustic Overload Point: 120dBSPL, SNR: 63dB",
    value_type=datatypes.String
)

# Speaker 속성 추가
speaker_property = Property(
    id_short="Speaker",
    value="Output: 3W x 2EA, 3.5mm Audio Jack, Frequency Response: 30Hz ~ 20KHz",
    value_type=datatypes.String
)

# Sensor Module Interface 속성 추가
sensor_module_interface_property = Property(
    id_short="Sensor_Module_Interface",
    value="Block 4EA +5V, +3.3V, GND, I2C, ADC, GPIO, SPI",
    value_type=datatypes.String
)

# 6-Axis Sensor 속성 추가
six_axis_sensor_property = Property(
    id_short="six_Axis_Sensor",
    value="MPU6050N, Resolution: 16bit, Gyroscope Range: +-250, +-500, +-1000, +-2000°/S, Accelerometer Range: +-2, +-4, +-8, +-18g",
    value_type=datatypes.String
)

# Camera 속성 추가
camera_property = Property(
    id_short="Camera",
    value="Image Sensor: Sony IMX219, Resolution: 8M Pixel (3280 x 2464 Pixel Static Images), Video: 1080p30, 720p60, 640x480p90, Angle of View: 160 Degrees",
    value_type=datatypes.String
)

# LCD 속성 추가
lcd_property = Property(
    id_short="LCD",
    value="7inch TFT LCD, HDMI, Resolution: 1024 x 600",
    value_type=datatypes.String
)

# Weight 속성 추가
weight_property = Property(
    id_short="Weight",
    value="5.2Kg",
    value_type=datatypes.String
)

# Size 속성 추가
size_property = Property(
    id_short="Size",
    value="290 X 290 X 310 (mm)",
    value_type=datatypes.String
)

# Basic Module 속성 추가
basic_module_property = Property(
    id_short="Basic_Module",
    value="Input Device: Tact Switch x 2EA(GPIO), Output Device: LED 8EA(I2C), Actuator: Passive Buzzer(GPIO)",
    value_type=datatypes.String
)

# 속성들을 Base_Board 서브모델에 추가
base_board.submodel_element.add(microphone_property)
base_board.submodel_element.add(speaker_property)
base_board.submodel_element.add(sensor_module_interface_property)
base_board.submodel_element.add(six_axis_sensor_property)
base_board.submodel_element.add(camera_property)
base_board.submodel_element.add(lcd_property)
base_board.submodel_element.add(weight_property)
base_board.submodel_element.add(size_property)
base_board.submodel_element.add(basic_module_property)

# 서브모델 생성 (operation)
submodel_operation = Submodel(
    id_="operation"
)

# on/off 상태 프로퍼티 추가
property_on_off = Property(
    id_short="on_off_state",
    value_type=datatypes.Boolean,
    value=False  # 기본적으로 on 상태로 설정
)

# 현재 속도 프로퍼티 추가
property_operating_time = Property(
    id_short="operation_time",
    value_type=datatypes.Float,
    value=0.0  # 초기 속도는 0으로 설정
)

# 서브모델에 프로퍼티 추가
submodel_operation.submodel_element.add(property_on_off)
submodel_operation.submodel_element.add(property_operating_time)

# Submodel들을 AAS에 추가
aas.submodel.add(ModelReference.from_referable(submodel_identifier))
aas.submodel.add(ModelReference.from_referable(soda_os))
aas.submodel.add(ModelReference.from_referable(pop_library))
aas.submodel.add(ModelReference.from_referable(motor_control_board))
aas.submodel.add(ModelReference.from_referable(main_module))
aas.submodel.add(ModelReference.from_referable(base_board))
aas.submodel.add(ModelReference.from_referable(submodel_operation))

# AAS를 DictObjectStore에 저장
aas_store = DictObjectStore()
aas_store.add(aas)
aas_store.add(submodel_identifier)
aas_store.add(soda_os)
aas_store.add(pop_library)
aas_store.add(motor_control_board)
aas_store.add(main_module)
aas_store.add(base_board)
aas_store.add(submodel_operation)

# AAS를 JSON으로 직렬화
with open('AMR_AAS.json', 'w', encoding='utf-8') as json_file:
    aas_json.write_aas_json_file(json_file, aas_store)  # AAS store 직렬화

import json

try:
    while True:
        # 외부로부터 새로운 데이터 수신 (여기선 임시값으로 처리)
        new_on_off_state = True  # 예시: 로봇이 작동 중인 상태
        new_speed = 3.5  # 예시: 로봇의 현재 속도 (예: 3.5 m/s)

        # 동적 프로퍼티 값 업데이트
        property_on_off.value = new_on_off_state
        property_operating_time.value = new_speed

        # AAS에 저장된 값 업데이트 (필요 시 JSON으로 저장)
        with open('AMR_AAS.json', 'w', encoding='utf-8') as json_file:
            aas_json.write_aas_json_file(json_file, aas_store)

        print('on-off state: ', new_on_off_state, 'speed: ', new_speed)

        # 5초 대기 후 값 갱신
        time.sleep(5)

except KeyboardInterrupt:
    print("Operation stopped by user")

# JSON 파일 불러오기
with open('AMR_AAS.json', 'r', encoding='utf-8') as json_file:
    aas_data = json.load(json_file)


# 가공된 데이터를 JSON 파일로 저장
with open('AMR_AAS2.json', 'w', encoding='utf-8') as json_file:
    json.dump(aas_data, json_file, indent=4, sort_keys=True, ensure_ascii=False)'''


from basyx.aas.model import AssetInformation, AssetKind, Property, datatypes, AssetAdministrationShell, Submodel, ModelReference, DictObjectStore
from basyx.aas.adapter import json as aas_json
import time

# Create asset information
asset_information = AssetInformation(
    asset_kind=AssetKind.INSTANCE,
    global_asset_id='AIoT_SerBOT'
)

# Create AAS
aas = AssetAdministrationShell(
    id_='IAI_AMR_1',
    asset_information=asset_information
)

# Create submodel for identification
submodel_identifier = Submodel(id_='identifier')
property_manufacturer = Property(id_short='manufacturer', value_type=datatypes.String, value='amrcompany')
property_supplier = Property(id_short='supplier', value_type=datatypes.String, value='amrcompany')
submodel_identifier.submodel_element.add(property_manufacturer)
submodel_identifier.submodel_element.add(property_supplier)

# Soda_OS 서브모델 생성
soda_os = Submodel(
    id_="Soda_OS"
)

# OS Information 속성 추가
os_info_property = Property(
    id_short="OS_Information",
    value="Soda OS, Linux Kernel 4.19",
    value_type=datatypes.String
)

# Desktop 환경 속성 추가
desktop_property = Property(
    id_short="Desktop_Environment",
    value="X-Server, Openbox, LightDM, Tint2, blueman, network-manager, conky",
    value_type=datatypes.String
)

# CLI 환경 속성 추가
cli_property = Property(
    id_short="CLI_Environment",
    value="Zsh, Tmux, Peco, powerlevel9k theme, Powerline fonts",
    value_type=datatypes.String
)

# Tool Chain 속성 추가
tool_chain_property = Property(
    id_short="Tool_Chain",
    value="GCC 9, JDK, Node JS, Python3, Clang",
    value_type=datatypes.String
)

# IDE 속성 추가
ide_property = Property(
    id_short="IDE",
    value="Visual Studio Code, NeoVim, Geany",
    value_type=datatypes.String
)

# Connectivity 속성 추가
connectivity_property = Property(
    id_short="Connectivity",
    value="Mosquitto(MQTT), Bluez, mtr, nmap, iptraf, Samba, Blynk Server, Remote Desktop Server",
    value_type=datatypes.String
)

# Multimedia 속성 추가
multimedia_property = Property(
    id_short="Multimedia",
    value="portaudio, sox, OpenCV 4, snowboy, Google Assistant",
    value_type=datatypes.String
)

# Data Science & AI 속성 추가
data_science_property = Property(
    id_short="Data_Science_and_AI",
    value="Python3, Numpy, Matplotlib, sympy, Pandas, Seaborn, Scipy, Gym, Scikit-learn, Tensorflow, Keras",
    value_type=datatypes.String
)

# Soda_OS 서브모델에 속성들 추가
soda_os.submodel_element.add(os_info_property)
soda_os.submodel_element.add(desktop_property)
soda_os.submodel_element.add(cli_property)
soda_os.submodel_element.add(tool_chain_property)
soda_os.submodel_element.add(ide_property)
soda_os.submodel_element.add(connectivity_property)
soda_os.submodel_element.add(multimedia_property)
soda_os.submodel_element.add(data_science_property)

# Pop_Library 서브모델 생성
pop_library = Submodel(
    id_="Pop_Library"
)

# Output Object 속성 추가
output_object_property = Property(
    id_short="Output_Object",
    value="(C/C++, Python3): Led, Laser, Buzzer, Relay, RGBLed, DCMotor, StepMotor, OLed, PiezoBuzzer, PixelDisplay, TextLCD, FND, Led Bar",
    value_type=datatypes.String
)

# Input Object 속성 추가
input_object_property = Property(
    id_short="Input_Object",
    value="(C/C++, Python3): Switch, Touch, Reed, LimitSwitch, Mercury, Knock, Tilt, Opto, Pir, Flame, LineTrace, TempHumi, UltraSonic, Shock, Sound, Potentiometer, CdS, SoilMoisture, Thermistor, Temperature, Gas, Dust, Psd, Gesture",
    value_type=datatypes.String
)

# Multimedia 속성 추가
multimedia_property = Property(
    id_short="Multimedia",
    value="(Python3): AudioPlay, AudioPlayList, AudioRecord, Tone, SoundMeter",
    value_type=datatypes.String
)

# Voice Assistant 속성 추가
voice_assistant_property = Property(
    id_short="Voice_Assistant",
    value="(Python3): GAssistant, create_conversation_stream",
    value_type=datatypes.String
)

# AI 속성 추가
ai_property = Property(
    id_short="AI",
    value="(Python3): Linear Regression, Logistic Regression, Perceptron, ANN, DNN, CNN, DQN",
    value_type=datatypes.String
)

# Pop_Library 서브모델에 속성들 추가
pop_library.submodel_element.add(output_object_property)
pop_library.submodel_element.add(input_object_property)
pop_library.submodel_element.add(multimedia_property)
pop_library.submodel_element.add(voice_assistant_property)
pop_library.submodel_element.add(ai_property)

# Motor Control Board 서브모델 생성
motor_control_board = Submodel(
    id_="Motor_Control_Board"
)

# 배터리 속성 추가
battery_voltage_property = Property(
    id_short="Battery_Voltage",
    value="11.1V",  # 배터리 전압
    value_type=datatypes.String
)

battery_capacity_property = Property(
    id_short="Battery_Capacity",
    value="14000mA",  # 배터리 용량
    value_type=datatypes.String
)

# 바퀴 속성 추가
wheels_type_property = Property(
    id_short="Wheels_Type",
    value="Omni-Wheels",  # 바퀴 유형
    value_type=datatypes.String
)

wheels_count_property = Property(
    id_short="Wheels_Count",
    value=3,  # 바퀴 개수
    value_type=datatypes.Integer
)

# 모터 속성 추가
motor_voltage_property = Property(
    id_short="Motor_Voltage",
    value="12V",  # 모터 전압
    value_type=datatypes.String
)

motor_count_property = Property(
    id_short="Motor_Count",
    value=3,  # 모터 개수
    value_type=datatypes.Integer
)

gear_rate_property = Property(
    id_short="Gear_Rate",
    value="1:50",  # 기어 비율
    value_type=datatypes.String
)

motor_speed_property = Property(
    id_short="Motor_Speed",
    value="6000RPM",  # 모터 속도
    value_type=datatypes.String
)

# 속성들을 Motor Control Board 서브모델에 추가
motor_control_board.submodel_element.add(battery_voltage_property)
motor_control_board.submodel_element.add(battery_capacity_property)
motor_control_board.submodel_element.add(wheels_type_property)
motor_control_board.submodel_element.add(wheels_count_property)
motor_control_board.submodel_element.add(motor_voltage_property)
motor_control_board.submodel_element.add(motor_count_property)
motor_control_board.submodel_element.add(gear_rate_property)
motor_control_board.submodel_element.add(motor_speed_property)

# Main Module 서브모델 생성
main_module = Submodel(
    id_="Main_Module"
)

# CPU 속성 추가
cpu_property = Property(
    id_short="CPU",
    value="Quad-Core ARM A57 @ 1.43 GHz",
    value_type=datatypes.String
)

# GPU 속성 추가
gpu_property = Property(
    id_short="GPU",
    value="Maxwell Core 128EA",
    value_type=datatypes.String
)

# Memory 속성 추가
memory_property = Property(
    id_short="Memory",
    value="4GB 64-bit LPDDR4 25.6 GB/s",
    value_type=datatypes.String
)

# Storage 속성 추가
storage_property = Property(
    id_short="Storage",
    value="MicroSD (64GB)",
    value_type=datatypes.String
)

# Video Encoder 속성 추가
video_encoder_property = Property(
    id_short="Video_Encoder",
    value="4K@30 | 4x 1080p@30 | 9x 720p@30 (H.264/H.265)",
    value_type=datatypes.String
)

# Video Decoder 속성 추가
video_decoder_property = Property(
    id_short="Video_Decoder",
    value="4K@60 | 2x 4K@30 | 8x 1080p@30 | 18x 720p@30 (H.264/H.265)",
    value_type=datatypes.String
)

# Camera 속성 추가
camera_property = Property(
    id_short="Camera",
    value="MIPI CSI-2 DPHY Lanes",
    value_type=datatypes.String
)

# Connectivity 속성 추가
connectivity_property = Property(
    id_short="Connectivity",
    value="Dual Band Wireless Wi-Fi 2GHz/5GHz Band, 867Mbps, 802.11ac, Bluetooth 4.2, Gigabit Ethernet",
    value_type=datatypes.String
)

# Display 속성 추가
display_property = Property(
    id_short="Display",
    value="HDMI and Display Port",
    value_type=datatypes.String
)

# USB 속성 추가
usb_property = Property(
    id_short="USB",
    value="4x USB 3.0, USB 2.0 Micro-B",
    value_type=datatypes.String
)

# 속성들을 Main Module 서브모델에 추가
main_module.submodel_element.add(cpu_property)
main_module.submodel_element.add(gpu_property)
main_module.submodel_element.add(memory_property)
main_module.submodel_element.add(storage_property)
main_module.submodel_element.add(video_encoder_property)
main_module.submodel_element.add(video_decoder_property)
main_module.submodel_element.add(camera_property)
main_module.submodel_element.add(connectivity_property)
main_module.submodel_element.add(display_property)
main_module.submodel_element.add(usb_property)

# Base_Board 서브모델 생성
base_board = Submodel(
    id_="Base_Board"
)

# Microphone 속성 추가
microphone_property = Property(
    id_short="Microphone",
    value="High Performance Digital Microphone x 4EA, Sensitivity: -26 dBFS (Omnidirectional), Acoustic Overload Point: 120dBSPL, SNR: 63dB",
    value_type=datatypes.String
)

# Speaker 속성 추가
speaker_property = Property(
    id_short="Speaker",
    value="Output: 3W x 2EA, 3.5mm Audio Jack, Frequency Response: 30Hz ~ 20KHz",
    value_type=datatypes.String
)

# Sensor Module Interface 속성 추가
sensor_module_interface_property = Property(
    id_short="Sensor_Module_Interface",
    value="Block 4EA +5V, +3.3V, GND, I2C, ADC, GPIO, SPI",
    value_type=datatypes.String
)

# 6-Axis Sensor 속성 추가
six_axis_sensor_property = Property(
    id_short="six_Axis_Sensor",
    value="MPU6050N, Resolution: 16bit, Gyroscope Range: +-250, +-500, +-1000, +-2000°/S, Accelerometer Range: +-2, +-4, +-8, +-18g",
    value_type=datatypes.String
)

# Camera 속성 추가
camera_property = Property(
    id_short="Camera",
    value="Image Sensor: Sony IMX219, Resolution: 8M Pixel (3280 x 2464 Pixel Static Images), Video: 1080p30, 720p60, 640x480p90, Angle of View: 160 Degrees",
    value_type=datatypes.String
)

# LCD 속성 추가
lcd_property = Property(
    id_short="LCD",
    value="7inch TFT LCD, HDMI, Resolution: 1024 x 600",
    value_type=datatypes.String
)

# Weight 속성 추가
weight_property = Property(
    id_short="Weight",
    value="5.2Kg",
    value_type=datatypes.String
)

# Size 속성 추가
size_property = Property(
    id_short="Size",
    value="290 X 290 X 310 (mm)",
    value_type=datatypes.String
)

# Basic Module 속성 추가
basic_module_property = Property(
    id_short="Basic_Module",
    value="Input Device: Tact Switch x 2EA(GPIO), Output Device: LED 8EA(I2C), Actuator: Passive Buzzer(GPIO)",
    value_type=datatypes.String
)

# 속성들을 Base_Board 서브모델에 추가
base_board.submodel_element.add(microphone_property)
base_board.submodel_element.add(speaker_property)
base_board.submodel_element.add(sensor_module_interface_property)
base_board.submodel_element.add(six_axis_sensor_property)
base_board.submodel_element.add(camera_property)
base_board.submodel_element.add(lcd_property)
base_board.submodel_element.add(weight_property)
base_board.submodel_element.add(size_property)
base_board.submodel_element.add(basic_module_property)

# 서브모델 생성 (operation)
submodel_operation = Submodel(
    id_="operation"
)

# on/off 상태 프로퍼티 추가
location_x = Property(
    id_short="location_x",
    value_type=datatypes.Float,
    value=0.0
)

location_y = Property(
    id_short="location_y",
    value_type=datatypes.Float,
    value=0.0
)

orientation = Property(
    id_short="orientation",
    value_type=datatypes.Float,
    value=0.0
)

speed = Property(
    id_short="speed",
    value_type=datatypes.Float,
    value=0.0
)

gyro_x = Property(
    id_short="gyro_x",
    value_type=datatypes.Float,
    value=0.0
)

gyro_y = Property(
    id_short="gyro_y",
    value_type=datatypes.Float,
    value=0.0
)

gyro_z = Property(
    id_short="gyro_z",
    value_type=datatypes.Float,
    value=0.0
)

accel_x = Property(
    id_short="accel_x",
    value_type=datatypes.Float,
    value=0.0
)

accel_y = Property(
    id_short="accel_y",
    value_type=datatypes.Float,
    value=0.0
)

accel_z = Property(
    id_short="accel_z",
    value_type=datatypes.Float,
    value=0.0
)

# 현재 속도 프로퍼티 추가
operation_time = Property(
    id_short="operation_time",
    value_type=datatypes.Float,
    value=0.0  # 초기 속도는 0으로 설정
)

# 서브모델에 프로퍼티 추가
submodel_operation.submodel_element.add(location_x)
submodel_operation.submodel_element.add(location_y)
submodel_operation.submodel_element.add(orientation)
submodel_operation.submodel_element.add(speed)
submodel_operation.submodel_element.add(gyro_x)
submodel_operation.submodel_element.add(gyro_y)
submodel_operation.submodel_element.add(gyro_z)
submodel_operation.submodel_element.add(accel_x)
submodel_operation.submodel_element.add(accel_y)
submodel_operation.submodel_element.add(accel_z)
submodel_operation.submodel_element.add(operation_time)

# Submodel들을 AAS에 추가
aas.submodel.add(ModelReference.from_referable(submodel_identifier))
aas.submodel.add(ModelReference.from_referable(soda_os))
aas.submodel.add(ModelReference.from_referable(pop_library))
aas.submodel.add(ModelReference.from_referable(motor_control_board))
aas.submodel.add(ModelReference.from_referable(main_module))
aas.submodel.add(ModelReference.from_referable(base_board))
aas.submodel.add(ModelReference.from_referable(submodel_operation))

# AAS를 DictObjectStore에 저장
aas_store = DictObjectStore()
aas_store.add(aas)
aas_store.add(submodel_identifier)
aas_store.add(soda_os)
aas_store.add(pop_library)
aas_store.add(motor_control_board)
aas_store.add(main_module)
aas_store.add(base_board)
aas_store.add(submodel_operation)

# AAS를 JSON으로 직렬화
with open('AMR_AAS.json', 'w', encoding='utf-8') as json_file:
    aas_json.write_aas_json_file(json_file, aas_store)  # AAS store 직렬화

import json

'''try:
    while True:
        # 외부로부터 새로운 데이터 수신 (여기선 임시값으로 처리)
        new_on_off_state = True  # 예시: 로봇이 작동 중인 상태
        new_speed = 3.5  # 예시: 로봇의 현재 속도 (예: 3.5 m/s)

        # 동적 프로퍼티 값 업데이트
        property_on_off.value = new_on_off_state
        property_operating_time.value = new_speed

        # AAS에 저장된 값 업데이트 (필요 시 JSON으로 저장)
        with open('AMR_AAS.json', 'w', encoding='utf-8') as json_file:
            aas_json.write_aas_json_file(json_file, aas_store)

        print('on-off state: ', new_on_off_state, 'speed: ', new_speed)

        # 5초 대기 후 값 갱신
        time.sleep(5)

except KeyboardInterrupt:
    print("Operation stopped by user")'''

# JSON 파일 불러오기
with open('AMR_AAS.json', 'r', encoding='utf-8') as json_file:
    aas_data = json.load(json_file)


# 가공된 데이터를 JSON 파일로 저장
with open('AMR_AAS2.json', 'w', encoding='utf-8') as json_file:
    json.dump(aas_data, json_file, indent=4, sort_keys=True, ensure_ascii=False)









