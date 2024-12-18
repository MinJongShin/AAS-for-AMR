import requests

# JSON 파일 경로 및 서버 URL
file_path = "AMR_AAS.json"
server_url = "opc.tcp://localhost:4840/freeopcua/server/"  # 서버의 업로드 엔드포인트


# JSON 파일을 서버로 업로드하는 함수
def upload_json_file(file_path, server_url):
    # JSON 파일 읽기
    with open(file_path, "rb") as f:
        files = {"file": f}
        # 파일을 서버에 POST 요청으로 전송
        response = requests.post(server_url, files=files)

    # 서버 응답 출력
    if response.status_code == 200:
        print("JSON 파일이 성공적으로 업로드되었습니다.")
    else:
        print(f"업로드 실패: {response.status_code}, {response.text}")


# 예시 실행
upload_json_file(file_path, server_url)

'''from opcua import Client
import time
import random
from pop import Pilot
from pop import LiDAR

bot = Pilot.SerBot()

# OPC UA 클라이언트 설정
# url = "opc.tcp://0.0.0.0:4840/freeopcua/server/"

# url = "opc.tcp://localhost:4840/freeopcua/server/"
url = "opc.tcp://192.168.55.100:4840/freeopcua/server/"

client = Client(url)

try:
    client.connect()
    print("OPC UA Client connected to server")

    # 서버의 노드 찾아오기
    root_node = client.get_root_node()
    print(f"Root node is: {root_node}")

    # 변수 노드 가져오기
    normal_operation = client.get_node("ns=1;s=1630AT155-NO")

    t = 0

    # 지속적으로 값을 서버에 전송
    while True:
        x = 0
        operating_time = t
        normal_operation.set_value([x, operating_time])
        print("connection: ", x, "operating_time: ", t)

        # 1초마다 값 전송
        time.sleep(1)
        t = t + 1

except KeyboardInterrupt:
    print("Client stopped by user")
finally:
    client.disconnect()
    print("OPC UA Client disconnected from server")'''


'''from opcua import Client
import time
import random

from pop import Pilot
bot = Pilot.SerBot()

from pop import LiDAR
lidar = LiDAR.Rplidar()
lidar.connect()
lidar.startMotor()

bot = Pilot.SerBot()

# OPC UA 클라이언트 설정
# url = "opc.tcp://0.0.0.0:4840/freeopcua/server/"

# url = "opc.tcp://localhost:4840/freeopcua/server/"
url = "opc.tcp://192.168.55.100:4840/freeopcua/server/"

client = Client(url)

try:
    client.connect()
    print("OPC UA Client connected to server")

    # 서버의 노드 찾아오기
    root_node = client.get_root_node()
    print(f"Root node is: {root_node}")

    # 변수 노드 가져오기
    normal_operation = client.get_node("ns=1;s=1630AT155-NO")
    
    speed = 50
    bot.setSpeed(speed)
    
    t = 0

    # 지속적으로 값을 서버에 전송
    while True:
        x = 0
        operating_time = t
        print("connection: ", x, "operating_time: ", t)

        
        gyro = bot.getGyro()    # 회전각 측정
        print(gyro)
        
        accel = bot.getAccel()
        print(accel)
        
        vectors = lidar.getVectors()
        for v in vectors:
            print("angle : ", v[0], "\ndistance : ", v[1], "\n")
            
        angle = v[0]
        distance = v[1]
        
        coords = lidar.getXY()
        for c in coords:
            print(c)
            
        normal_operation.set_value([x, operating_time, gyro, accel, speed])
        
        # 1초마다 값 전송
        time.sleep(1)
        t = t + 1


except KeyboardInterrupt:
    print("Client stopped by user")
finally:
    client.disconnect()
    print("OPC UA Client disconnected from server")'''

'''from opcua import Client
import time
import random
from pop import Pilot
from pop import LiDAR

bot = Pilot.SerBot()

# OPC UA 클라이언트 설정
# url = "opc.tcp://0.0.0.0:4840/freeopcua/server/"

# url = "opc.tcp://localhost:4840/freeopcua/server/"
url = "opc.tcp://192.168.55.100:4840/freeopcua/server/"

client = Client(url)

try:
    client.connect()
    print("OPC UA Client connected to server")

    # 서버의 노드 찾아오기
    root_node = client.get_root_node()
    print(f"Root node is: {root_node}")

    # 변수 노드 가져오기
    normal_operation = client.get_node("ns=1;s=1630AT155-NO")

    t = 0

    # 지속적으로 값을 서버에 전송
    while True:
        x = 0
        operating_time = t
        normal_operation.set_value([x, operating_time])
        print("connection: ", x, "operating_time: ", t)

        # 1초마다 값 전송
        time.sleep(1)
        t = t + 1

except KeyboardInterrupt:
    print("Client stopped by user")
finally:
    client.disconnect()
    print("OPC UA Client disconnected from server")'''

'''from opcua import Client
import time
import random
from pop import Pilot
from pop import LiDAR

bot = Pilot.SerBot()

# OPC UA 클라이언트 설정
# url = "opc.tcp://0.0.0.0:4840/freeopcua/server/"

# url = "opc.tcp://localhost:4840/freeopcua/server/"
url = "opc.tcp://192.168.55.100:4840/freeopcua/server/"

client = Client(url)

try:
    client.connect()
    print("OPC UA Client connected to server")

    # 서버의 노드 찾아오기
    root_node = client.get_root_node()
    print(f"Root node is: {root_node}")

    # 변수 노드 가져오기
    normal_operation = client.get_node("ns=1;s=1630AT155-NO")

    t = 0

    # 지속적으로 값을 서버에 전송
    while True:
        x = 0
        operating_time = t
        normal_operation.set_value([x, operating_time, 1, 2, 3])
        print("connection: ", x, "operating_time: ", t, 1, 2, 3)

        # 1초마다 값 전송
        time.sleep(1)
        t = t + 1

except KeyboardInterrupt:
    print("Client stopped by user")
finally:
    client.disconnect()
    print("OPC UA Client disconnected from server")'''

'''from opcua import Client
from opcua import ua
import time
import random
import json

from pop import Pilot
bot = Pilot.SerBot()

from pop import LiDAR
lidar = LiDAR.Rplidar()
lidar.connect()
lidar.startMotor()

# OPC UA 클라이언트 설정
# url = "opc.tcp://0.0.0.0:4840/freeopcua/server/"

# url = "opc.tcp://localhost:4840/freeopcua/server/"
url = "opc.tcp://192.168.55.100:4840/freeopcua/server/"

client = Client(url)

try:
    client.connect()
    print("OPC UA Client connected to server")

    # 서버의 노드 찾아오기
    root_node = client.get_root_node()
    print(f"Root node is: {root_node}")

    # 변수 노드 가져오기
    normal_operation = client.get_node("ns=1;s=1630AT155-NO")

    speed = 50
    #bot.setSpeed(speed)

    t = 0

    # 지속적으로 값을 서버에 전송
    while True:
        x = 0
        operating_time = t
        print("connection: ", x, "operating_time: ", t)


        gyro = bot.getGyro()    # 회전각 측정
        print(gyro)

        accel = bot.getAccel()
        print(accel)

        vectors = lidar.getVectors()
        #for v in vectors:
        #    print("angle : ", v[0], "\ndistance : ", v[1], "\n")

        #angle = v[0]
        #distance = v[1]

        coords = lidar.getXY()
        #for c in coords:
        #    print(c)

        normal_operation.set_value([x, operating_time, gyro, accel, speed])

        # 1초마다 값 전송
        time.sleep(1)
        t = t + 1


except KeyboardInterrupt:
    print("Client stopped by user")
finally:
    client.disconnect()
    print("OPC UA Client disconnected from server")'''

'''from opcua import Client
import time
from pop import Pilot

bot = Pilot.SerBot()

# OPC UA 클라이언트 설정
# url = "opc.tcp://0.0.0.0:4840/freeopcua/server/"

# url = "opc.tcp://localhost:4840/freeopcua/server/"
url = "opc.tcp://192.168.55.100:4840/freeopcua/server/"

client = Client(url)

#an = 0
#sp = 10
#bot.move(an, sp)

try:
    client.connect()
    print("OPC UA Client connected to server")

    # 서버의 노드 찾아오기
    root_node = client.get_root_node()
    print(f"Root node is: {root_node}")

    # 변수 노드 가져오기
    normal_operation = client.get_node("ns=1;s=1630AT155-NO")

    t = 0

    # 지속적으로 값을 서버에 전송
    while True:
        x = 0
        operating_time = t

        gyro = bot.getGyro()    # 회전각 측정
        print(gyro)

        accel = bot.getAccel()
        print(accel)


        normal_operation.set_value([x, operating_time, 1, 2, 3])
        print("connection: ", x, "operating_time: ", t, 1, 2, 3)

        # 1초마다 값 전송
        time.sleep(1)
        t = t + 1

except KeyboardInterrupt:
    print("Client stopped by user")
    bot.stop()
finally:
    client.disconnect()
    print("OPC UA Client disconnected from server")'''

'''from opcua import Client, ua
import time
from pop import Pilot, LiDAR
import json

bot = Pilot.SerBot()
lidar = LiDAR.Rplidar()
lidar.connect()
lidar.startMotor()
# 로봇과 OPC UA 클라이언트 설정
url = "opc.tcp://192.168.55.100:4840/freeopcua/server/"
client = Client(url, timeout=20)  # 타임아웃을 20초로 설정

try:
    client.connect()
    print("OPC UA Client connected to server")

    # 서버의 노드 가져오기
    root_node = client.get_root_node()
    print(f"Root node is: {root_node}")

    # 서버의 변수 노드 설정
    normal_operation = client.get_node("ns=1;s=1630AT155-NO")

    angle = 10
    speed = 20
    bot.move(angle, speed)

    t = 0
    while True:
        data = {
            "connection": 0,
            "operating_time": t,
            "gyro": bot.getGyro(),
            "accel": bot.getAccel(),
            "speed": speed
        }
        json_data = json.dumps(data)
        normal_operation.set_value(json_data, ua.VariantType.String)
        print("Sent data:", data)

        time.sleep(2)
        t += 1

except KeyboardInterrupt:
    print("Client stopped by user")
    bot.stop()
    lidar.stopMotor()
finally:
    client.disconnect()
    print("OPC UA Client disconnected from server")'''

'''from opcua import Client, ua
import time
import json
from pop import Pilot
import math

# Initialize the robot
bot = Pilot.SerBot()

# OPC UA client settings
url = "opc.tcp://192.168.55.100:4840/freeopcua/server/"
client = Client(url)

# Initial position and orientation
x, y = 0, 0
orientation = 0  # in radians, 0 is along the positive x-axis

try:
    client.connect()
    print("OPC UA Client connected to server")

    # Retrieve the root node and normal_operation node
    root_node = client.get_root_node()
    normal_operation = client.get_node("ns=1;s=1630AT155-NO")

    t = 0
    angle = 10
    speed = 20
    bot.move(angle, speed)
    dt = 1  # assuming updates every 1 second

    while True:
        # Gather data from sensors
        gyro = bot.getGyro()
        accel = bot.getAccel()
        steering_angle = gyro['z']  # Adjust as needed based on gyro interpretation

        # Calculate linear acceleration
        linear_accel = math.sqrt(accel['x'] ** 2 + accel['y'] ** 2 + accel['z'] ** 2)

        # Update speed and position
        speed += linear_accel * dt
        orientation += steering_angle * dt

        # Update x and y positions
        dx = speed * math.cos(orientation) * dt
        dy = speed * math.sin(orientation) * dt
        x += dx
        y += dy

        # Prepare data to send
        data = {
            "operating_time": t,
            "gyro": gyro,
            "accel": accel,
            "speed": speed,
            "x": x,
            "y": y,
            "orientation": orientation
        }

        # Send data to server
        normal_operation.set_value(json.dumps(data), ua.VariantType.String)
        print(f"Sent data: {data}")

        # Update time and wait for the next update
        t += dt
        time.sleep(dt)

except KeyboardInterrupt:
    print("Client stopped by user")
    bot.stop()
    lidar.stopMotor()
finally:
    client.disconnect()
    print("OPC UA Client disconnected from server")'''