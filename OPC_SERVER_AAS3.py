'''from opcua import Server
import json
import time
import math
import matplotlib
matplotlib.use('TkAgg')  # PyCharm 또는 GUI 환경에서 그래프 표시
import matplotlib.pyplot as plt

show_animation = True


def plot_arrow(x, y, yaw, length=1.0, width=0.5, fc="r", ec="k"):
    """
    Plot arrow
    """

    if not isinstance(x, float):
        for ix, iy, iyaw in zip(x, y, yaw):
            plot_arrow(ix, iy, iyaw)
    else:
        plt.arrow(x, y, length * math.cos(yaw), length * math.sin(yaw),
                  fc=fc, ec=ec, head_width=width, head_length=width)
        plt.plot(x, y)

# OPC UA 서버 설정
server = Server()
url = "opc.tcp://192.168.55.100:4840/freeopcua/server/"
server.set_endpoint(url)

name = "OPCUA_SERVER"
addspace = server.register_namespace(name)
node = server.get_objects_node()

# 기존 객체 추가
Param = node.add_object(addspace, "251-AH-001")
normal_operation = Param.add_variable("ns=1;s=1630AT155-NO", "normal_operation", "")
normal_operation.set_writable()

# JSON 변수를 위한 추가 노드
JsonParam = node.add_object(addspace, "JSON-Param")
json_variable = JsonParam.add_variable("ns=1;s=JSON-Data", "json_data", "")
json_variable.set_writable()

# 서버 시작
server.start()
print("OPC UA Server started at {}".format(url))

# x, y 좌표의 궤적을 저장할 리스트 추가
trajectory_x = []
trajectory_y = []

try:
    while True:
        # 클라이언트로부터 JSON 형식의 위치 데이터 수신
        json_data_str = normal_operation.get_value()
        if json_data_str:
            try:
                json_data = json.loads(json_data_str)
                print(f"AMR 데이터 수신 - 위치 (x, y): ({json_data.get('x')}, {json_data.get('y')}),\n"
                      f"방향 (orientation): {json_data.get('orientation')},\n"
                      f"속력 (speed): {json_data.get('speed')},\n"
                      f"조향 (gyro): ({json_data.get('gyro_x')}, {json_data.get('gyro_y')}, {json_data.get('gyro_z')}),\n"
                      f"가속도 (accel): ({json_data.get('accel_x')}, {json_data.get('accel_y')}, {json_data.get('accel_z')}),\n"
                      f"운영 시간 (operating_time): {json_data.get('operating_time')}")

                # 누적 궤적 저장
                if json_data.get('x') is not None and json_data.get('y') is not None:
                    trajectory_x.append(json_data.get('x'))
                    trajectory_y.append(json_data.get('y'))

                # 그래프 갱신
                if show_animation:
                    plt.cla()
                    plot_arrow(json_data.get('x'), json_data.get('y'), json_data.get('orientation'))
                    plt.plot(trajectory_x, trajectory_y, "-b", label="trajectory")
                    plt.axis("equal")
                    plt.grid(True)
                    plt.legend()
                    plt.pause(0.01)

            except json.JSONDecodeError as e:
                print("JSON 디코딩 실패:", e)

        time.sleep(1)

except KeyboardInterrupt:
    print("Server stopped by user")
finally:
    server.stop()
    if show_animation:
        plt.show()'''



'''from opcua import Server
import json
import time
import math
import matplotlib
matplotlib.use('TkAgg')  # PyCharm 또는 GUI 환경에서 그래프 표시
import matplotlib.pyplot as plt

show_animation = True


def plot_arrow(x, y, yaw, length=1.0, width=0.5, fc="r", ec="k"):
    """
    Plot arrow
    """

    if not isinstance(x, float):
        for ix, iy, iyaw in zip(x, y, yaw):
            plot_arrow(ix, iy, iyaw)
    else:
        plt.arrow(x, y, length * math.cos(yaw), length * math.sin(yaw),
                  fc=fc, ec=ec, head_width=width, head_length=width)
        plt.plot(x, y)

# OPC UA 서버 설정
server = Server()
url = "opc.tcp://192.168.55.100:4840/freeopcua/server/"
server.set_endpoint(url)

name = "OPCUA_SERVER"
addspace = server.register_namespace(name)
node = server.get_objects_node()

# 기존 객체 추가
Param = node.add_object(addspace, "251-AH-001")
normal_operation = Param.add_variable("ns=1;s=1630AT155-NO", "normal_operation", "")
normal_operation.set_writable()

# JSON 변수를 위한 추가 노드
JsonParam = node.add_object(addspace, "JSON-Param")
json_variable = JsonParam.add_variable("ns=1;s=JSON-Data", "json_data", "")
json_variable.set_writable()

# 서버 시작
server.start()
print("OPC UA Server started at {}".format(url))

# x, y 좌표의 궤적을 저장할 리스트 추가
trajectory_x = []
trajectory_y = []

try:
    while True:
        json_data_str = normal_operation.get_value()
        if json_data_str:
            try:
                json_data = json.loads(json_data_str)

                # 값들을 소수점 3자리로 제한
                x = round(json_data.get('x'), 1) if json_data.get('x') is not None else None
                y = round(json_data.get('y'), 1) if json_data.get('y') is not None else None
                orientation = round(json_data.get('orientation'), 1) if json_data.get('orientation') is not None else None
                speed = round(json_data.get('speed'), 1) if json_data.get('speed') is not None else None
                gyro_x = round(json_data.get('gyro_x'), 1) if json_data.get('gyro_x') is not None else None
                gyro_y = round(json_data.get('gyro_y'), 1) if json_data.get('gyro_y') is not None else None
                gyro_z = round(json_data.get('gyro_z'), 1) if json_data.get('gyro_z') is not None else None
                accel_x = round(json_data.get('accel_x'), 1) if json_data.get('accel_x') is not None else None
                accel_y = round(json_data.get('accel_y'), 1) if json_data.get('accel_y') is not None else None
                accel_z = round(json_data.get('accel_z'), 1) if json_data.get('accel_z') is not None else None

                print(f"AMR 데이터 수신 - 위치 (x, y): ({x}, {y}),\n"
                      f"방향 (orientation): {orientation},\n"
                      f"속력 (speed): {speed},\n"
                      f"조향 (gyro): ({gyro_x}, {gyro_y}, {gyro_z}),\n"
                      f"가속도 (accel): ({accel_x}, {accel_y}, {accel_z}),\n"
                      f"운영 시간 (operating_time): {json_data.get('operating_time')}")

                # 그래프 그리기
                if show_animation:
                    plt.cla()
                    plot_arrow(x, y, orientation)
                    trajectory_x.append(x)
                    trajectory_y.append(y)
                    plt.plot(trajectory_x, trajectory_y, "-b", label="trajectory")
                    plt.axis("equal")
                    plt.grid(True)
                    plt.legend()
                    plt.pause(0.01)

            except json.JSONDecodeError as e:
                print("JSON 디코딩 실패:", e)

        time.sleep(1)


except KeyboardInterrupt:
    print("Server stopped by user")
finally:
    server.stop()
    if show_animation:
        plt.show()'''



'''from opcua import Server
import json
import time
import math
import matplotlib
matplotlib.use('TkAgg')  # PyCharm 또는 GUI 환경에서 그래프 표시
import matplotlib.pyplot as plt

show_animation = True


def plot_arrow(x, y, yaw, length=1.0, width=0.5, fc="r", ec="k"):
    """
    Plot arrow
    """

    if not isinstance(x, float):
        for ix, iy, iyaw in zip(x, y, yaw):
            plot_arrow(ix, iy, iyaw)
    else:
        plt.arrow(x, y, length * math.cos(yaw), length * math.sin(yaw),
                  fc=fc, ec=ec, head_width=width, head_length=width)
        plt.plot(x, y)

# OPC UA 서버 설정
server = Server()
url = "opc.tcp://192.168.55.100:4840/freeopcua/server/"
server.set_endpoint(url)

name = "OPCUA_SERVER"
addspace = server.register_namespace(name)
node = server.get_objects_node()

# 기존 객체 추가
Param = node.add_object(addspace, "251-AH-001")
normal_operation = Param.add_variable("ns=1;s=1630AT155-NO", "normal_operation", "")
normal_operation.set_writable()

# JSON 변수를 위한 추가 노드
JsonParam = node.add_object(addspace, "JSON-Param")
json_variable = JsonParam.add_variable("ns=1;s=JSON-Data", "json_data", "")
json_variable.set_writable()

# 서버 시작
server.start()
print("OPC UA Server started at {}".format(url))

# x, y 좌표의 궤적을 저장할 리스트 추가
trajectory_x = []
trajectory_y = []

try:
    while True:
        json_data_str = normal_operation.get_value()
        if json_data_str:
            try:
                json_data = json.loads(json_data_str)

                # 값들을 소수점 3자리로 제한
                x = round(json_data.get('x'), 0) if json_data.get('x') is not None else None
                y = round(json_data.get('y'), 0) if json_data.get('y') is not None else None
                orientation = round(json_data.get('orientation'), 1) if json_data.get('orientation') is not None else None
                speed = round(json_data.get('speed'), 0) if json_data.get('speed') is not None else None
                gyro_x = round(json_data.get('gyro_x'), 1) if json_data.get('gyro_x') is not None else None
                gyro_y = round(json_data.get('gyro_y'), 1) if json_data.get('gyro_y') is not None else None
                gyro_z = round(json_data.get('gyro_z'), 1) if json_data.get('gyro_z') is not None else None
                accel_x = round(json_data.get('accel_x'), 1) if json_data.get('accel_x') is not None else None
                accel_y = round(json_data.get('accel_y'), 1) if json_data.get('accel_y') is not None else None
                accel_z = round(json_data.get('accel_z'), 1) if json_data.get('accel_z') is not None else None

                print(f"AMR 데이터 수신 - 위치 (x, y): ({x}, {y}),\n"
                      f"방향 (orientation): {orientation},\n"
                      f"속력 (speed): {speed},\n"
                      f"조향 (gyro): ({gyro_x}, {gyro_y}, {gyro_z}),\n"
                      f"가속도 (accel): ({accel_x}, {accel_y}, {accel_z}),\n"
                      f"운영 시간 (operating_time): {json_data.get('operating_time')}")

                # 그래프 그리기
                if show_animation:
                    plt.cla()
                    plot_arrow(x, y, orientation)
                    trajectory_x.append(x)
                    trajectory_y.append(y)
                    plt.plot(trajectory_x, trajectory_y, "-b", label="trajectory")
                    plt.scatter([0, 1000], [0, 0], color='red', label="Points A and B")  # 점 표시
                    plt.text(0, 0, "A(0, 0)", fontsize=10, color="red", ha="right")  # A 레이블
                    plt.text(1000, 0, "B(1000, 0)", fontsize=10, color="red", ha="left")  # B 레이블
                    plt.axis("equal")
                    plt.grid(True)
                    plt.legend()
                    plt.pause(0.01)

            except json.JSONDecodeError as e:
                print("JSON 디코딩 실패:", e)

        time.sleep(1)


except KeyboardInterrupt:
    print("Server stopped by user")
finally:
    server.stop()
    if show_animation:
        plt.show()'''



'''from opcua import Server
import json
import time
import math
import matplotlib
matplotlib.use('TkAgg')  # PyCharm 또는 GUI 환경에서 그래프 표시
import matplotlib.pyplot as plt

show_animation = True


def plot_arrow(x, y, yaw, length=1.0, width=0.5, fc="r", ec="k"):
    """
    Plot arrow
    """

    if not isinstance(x, float):
        for ix, iy, iyaw in zip(x, y, yaw):
            plot_arrow(ix, iy, iyaw)
    else:
        plt.arrow(x, y, length * math.cos(yaw), length * math.sin(yaw),
                  fc=fc, ec=ec, head_width=width, head_length=width)
        plt.plot(x, y)

# OPC UA 서버 설정
server = Server()
url = "opc.tcp://192.168.55.100:4840/freeopcua/server/"
server.set_endpoint(url)

name = "OPCUA_SERVER"
addspace = server.register_namespace(name)
node = server.get_objects_node()

# 기존 객체 추가
Param = node.add_object(addspace, "251-AH-001")
normal_operation = Param.add_variable("ns=1;s=1630AT155-NO", "normal_operation", "")
normal_operation.set_writable()

# JSON 변수를 위한 추가 노드
JsonParam = node.add_object(addspace, "JSON-Param")
json_variable = JsonParam.add_variable("ns=1;s=JSON-Data", "json_data", "")
json_variable.set_writable()

# 서버 시작
server.start()
print("OPC UA Server started at {}".format(url))

# x, y 좌표의 궤적을 저장할 리스트 추가
trajectory_x = []
trajectory_y = []

try:
    while True:
        json_data_str = normal_operation.get_value()
        if json_data_str:
            try:
                json_data = json.loads(json_data_str)

                # 값들을 소수점 3자리로 제한
                x = round(json_data.get('x'), 0) if json_data.get('x') is not None else None
                y = round(json_data.get('y'), 0) if json_data.get('y') is not None else None
                orientation = round(json_data.get('orientation'), 1) if json_data.get('orientation') is not None else None
                speed = round(json_data.get('speed'), 0) if json_data.get('speed') is not None else None
                gyro_x = round(json_data.get('gyro_x'), 1) if json_data.get('gyro_x') is not None else None
                gyro_y = round(json_data.get('gyro_y'), 1) if json_data.get('gyro_y') is not None else None
                gyro_z = round(json_data.get('gyro_z'), 1) if json_data.get('gyro_z') is not None else None
                accel_x = round(json_data.get('accel_x'), 1) if json_data.get('accel_x') is not None else None
                accel_y = round(json_data.get('accel_y'), 1) if json_data.get('accel_y') is not None else None
                accel_z = round(json_data.get('accel_z'), 1) if json_data.get('accel_z') is not None else None

                print(f"AMR 데이터 수신 - 위치 (x, y): ({x}, {y}), "
                      f"방향 (orientation): {orientation}, "
                      f"속력 (speed): {speed},\n"
                      f"조향 (gyro): ({gyro_x}, {gyro_y}, {gyro_z}), "
                      f"가속도 (accel): ({accel_x}, {accel_y}, {accel_z}), "
                      f"운영 시간 (operating_time): {json_data.get('operating_time')}")

                # 그래프 그리기
                if show_animation:
                    plt.cla()
                    plot_arrow(x, y, orientation)
                    trajectory_x.append(x)
                    trajectory_y.append(y)
                    plt.plot(trajectory_x, trajectory_y, "bo", label="trajectory")
                    plt.scatter([0, 10000], [0, 0], color='black', label="Points A and B")  # 점 표시
                    plt.text(0, 0, "Start(0, 0)", fontsize=10, color="black", ha="right")  # A 레이블
                    plt.text(10000, 0, "Target(10000, 0)", fontsize=10, color="black", ha="left")  # B 레이블
                    plt.axis("equal")
                    plt.grid(True)
                    plt.legend()
                    plt.pause(0.01)

            except json.JSONDecodeError as e:
                print("JSON 디코딩 실패:", e)

        time.sleep(1)


except KeyboardInterrupt:
    print("Server stopped by user")
finally:
    server.stop()
    if show_animation:
        plt.show()'''



'''from opcua import Server
import json
import time
import math
import matplotlib
matplotlib.use('TkAgg')  # PyCharm 또는 GUI 환경에서 그래프 표시
import matplotlib.pyplot as plt

show_animation = True


def plot_arrow(x, y, yaw, length=1.0, width=0.5, fc="r", ec="k"):
    """
    Plot arrow
    """

    if not isinstance(x, float):
        for ix, iy, iyaw in zip(x, y, yaw):
            plot_arrow(ix, iy, iyaw)
    else:
        plt.arrow(x, y, length * math.cos(yaw), length * math.sin(yaw),
                  fc=fc, ec=ec, head_width=width, head_length=width)
        plt.plot(x, y)

# OPC UA 서버 설정
server = Server()
url = "opc.tcp://192.168.55.100:4840/freeopcua/server/"
server.set_endpoint(url)

name = "OPCUA_SERVER"
addspace = server.register_namespace(name)
node = server.get_objects_node()

# 기존 객체 추가
Param = node.add_object(addspace, "251-AH-001")
normal_operation = Param.add_variable("ns=1;s=1630AT155-NO", "normal_operation", "")
normal_operation.set_writable()

# JSON 변수를 위한 추가 노드
JsonParam = node.add_object(addspace, "JSON-Param")
json_variable = JsonParam.add_variable("ns=1;s=JSON-Data", "json_data", "")
json_variable.set_writable()

# 서버 시작
server.start()
print("OPC UA Server started at {}".format(url))

# x, y 좌표의 궤적을 저장할 리스트 추가
trajectory_x = []
trajectory_y = []

try:
    while True:
        json_data_str = normal_operation.get_value()
        if json_data_str:
            try:
                json_data = json.loads(json_data_str)

                # 값들을 소수점 3자리로 제한
                x = round(json_data.get('x'), 0) if json_data.get('x') is not None else None
                y = round(json_data.get('y'), 0) if json_data.get('y') is not None else None
                orientation = round(json_data.get('orientation'), 1) if json_data.get('orientation') is not None else None
                speed = round(json_data.get('speed'), 0) if json_data.get('speed') is not None else None
                gyro_x = round(json_data.get('gyro_x'), 1) if json_data.get('gyro_x') is not None else None
                gyro_y = round(json_data.get('gyro_y'), 1) if json_data.get('gyro_y') is not None else None
                gyro_z = round(json_data.get('gyro_z'), 1) if json_data.get('gyro_z') is not None else None
                accel_x = round(json_data.get('accel_x'), 1) if json_data.get('accel_x') is not None else None
                accel_y = round(json_data.get('accel_y'), 1) if json_data.get('accel_y') is not None else None
                accel_z = round(json_data.get('accel_z'), 1) if json_data.get('accel_z') is not None else None

                print(f"AMR 데이터 수신 - 위치 (x, y): ({x}, {y}), "
                      f"방향 (orientation): {orientation}, "
                      f"속력 (speed): {speed},\n"
                      f"조향 (gyro): ({gyro_x}, {gyro_y}, {gyro_z}), "
                      f"가속도 (accel): ({accel_x}, {accel_y}, {accel_z}), "
                      f"운영 시간 (operating_time): {json_data.get('operating_time')}")

                # 운영 시간을 저장할 리스트
                operating_times = []

                # 그래프 업데이트
                if show_animation:
                    plt.cla()
                    plot_arrow(x, y, orientation)

                    # 점 좌표와 궤적 업데이트
                    trajectory_x.append(x)
                    trajectory_y.append(y)
                    operating_times.append(len(trajectory_x))  # 현재 점의 순서를 기반으로 1, 2, 3, ... 추가

                    # 점과 궤적 그리기
                    plt.plot(trajectory_x, trajectory_y, "bo", markersize=3, label="trajectory")  # 점 크기 축소

                    # 각 점 위에 운영 시간 표시
                    for tx, ty, op_time in zip(trajectory_x, trajectory_y, operating_times):
                        plt.text(tx, ty + 50, f"{op_time}s", fontsize=6, color="blue",
                                 ha="center")  # 점 위에 텍스트 추가, y 오프셋 50

                    # 시작점과 목표점 표시
                    plt.scatter([0, 10000], [0, 0], color='black', label="Points A and B")  # 점 표시
                    plt.text(0, 0, "Start(0, 0)", fontsize=10, color="black", ha="right")  # A 레이블
                    plt.text(10000, 0, "Target(10000, 0)", fontsize=10, color="black", ha="left")  # B 레이블
                    plt.axis("equal")
                    plt.grid(True)
                    plt.legend()
                    plt.pause(0.01)



            except json.JSONDecodeError as e:
                print("JSON 디코딩 실패:", e)

        time.sleep(1)


except KeyboardInterrupt:
    print("Server stopped by user")
finally:
    server.stop()
    if show_animation:
        plt.show()'''


from opcua import Server
import json
import time
import math
import matplotlib
matplotlib.use('TkAgg')  # PyCharm 또는 GUI 환경에서 그래프 표시
import matplotlib.pyplot as plt

show_animation = True


def plot_arrow(x, y, yaw, length=1.0, width=0.5, fc="r", ec="k"):
    """
    Plot arrow
    """
    plt.arrow(x, y, length * math.cos(yaw), length * math.sin(yaw),
              fc=fc, ec=ec, head_width=width, head_length=width)
    plt.plot(x, y)


# OPC UA 서버 설정
server = Server()
url = "opc.tcp://192.168.55.100:4840/freeopcua/server/"
server.set_endpoint(url)

name = "OPCUA_SERVER"
addspace = server.register_namespace(name)
node = server.get_objects_node()

# 기존 객체 추가
Param = node.add_object(addspace, "251-AH-001")
normal_operation = Param.add_variable("ns=1;s=1630AT155-NO", "normal_operation", "")
normal_operation.set_writable()

# 서버 시작
server.start()
print("OPC UA Server started at {}".format(url))

# x, y 좌표와 operating time 궤적을 저장할 리스트 추가
trajectory_x = []
trajectory_y = []

try:
    while True:
        json_data_str = normal_operation.get_value()
        if json_data_str:
            try:
                json_data = json.loads(json_data_str)

                # 값들을 소수점 3자리로 제한
                x = round(json_data.get('x'), 0) if json_data.get('x') is not None else None
                y = round(json_data.get('y'), 0) if json_data.get('y') is not None else None
                orientation = round(json_data.get('orientation'), 1) if json_data.get(
                    'orientation') is not None else None
                speed = round(json_data.get('speed'), 0) if json_data.get('speed') is not None else None
                gyro_x = round(json_data.get('gyro_x'), 1) if json_data.get('gyro_x') is not None else None
                gyro_y = round(json_data.get('gyro_y'), 1) if json_data.get('gyro_y') is not None else None
                gyro_z = round(json_data.get('gyro_z'), 1) if json_data.get('gyro_z') is not None else None
                accel_x = round(json_data.get('accel_x'), 1) if json_data.get('accel_x') is not None else None
                accel_y = round(json_data.get('accel_y'), 1) if json_data.get('accel_y') is not None else None
                accel_z = round(json_data.get('accel_z'), 1) if json_data.get('accel_z') is not None else None

                print(f" 운영 시간 (operating_time): {json_data.get('operating_time')}, "
                      f"위치 (x, y): ({x}, {y}), "
                      f"방향 (orientation): {orientation},\n"
                      f"속력 (speed): {speed}, "
                      f"각속도 (gyro): ({gyro_x}, {gyro_y}, {gyro_z}), "
                      f"가속도 (accel): ({accel_x}, {accel_y}, {accel_z}), ")

                # 궤적과 운영 시간 기록
                if x is not None and y is not None and json_data.get('operating_time') is not None:
                    trajectory_x.append(x)
                    trajectory_y.append(y)

                # 그래프 그리기
                if show_animation:
                    plt.cla()
                    plot_arrow(x, y, orientation)

                    # 궤적과 운영 시간 표시
                    plt.plot(trajectory_x, trajectory_y, "b.-", label="trajectory")

                    # 마지막 점에 운영 시간 표시
                    if len(trajectory_x) > 0 and len(trajectory_y) > 0:
                        last_x = trajectory_x[-1]
                        last_y = trajectory_y[-1]
                        plt.text(last_x, last_y + 100,  # 마지막 점 위에 표시
                                 f"{json_data.get('operating_time')}s", fontsize=7, color="blue", ha="center")

                    # Start와 Target 레이블 점 아래로 위치 조정
                    plt.scatter([0, 10000], [0, 0], color='black', label="Start and Target Points")
                    plt.text(0, -500, "Start(0, 0)", fontsize=10, color="black", ha="center")  # 점 아래에 표시
                    plt.text(10000, -500, "Target(10000, 0)", fontsize=10, color="black", ha="center")  # 점 아래에 표시

                    plt.axis("equal")
                    plt.grid(True)
                    plt.legend()
                    plt.pause(0.01)

            except json.JSONDecodeError as e:
                print("JSON 디코딩 실패:", e)

        time.sleep(1)

except KeyboardInterrupt:
    print("Server stopped by user")
finally:
    server.stop()
    if show_animation:
        plt.show()
