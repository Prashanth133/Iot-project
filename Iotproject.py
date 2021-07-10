import serial
from firebase import firebase
from time import sleep
from datetime import datetime
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port, desc, hwid))

ser = serial.Serial("COM2", 9600)
res = 1
i = 0
time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)

while res:
  
    firebase1 = firebase.FirebaseApplication('https://iot-project-1592f-default-rtdb.firebaseio.com/', None)

    for i in range(0, 4):
        
        string1=str(ser.readline())
        string1=string1[2:7]
        string1 = float(string1)
        data = {'date': datetime.now().strftime("%Y-%m-%d"),
                'reading': string1,
                'time': datetime.now().strftime("%H:%M")
                }
        result = firebase1.patch(
            'https://iot-project-1592f-default-rtdb.firebaseio.com/' + '/Temperature_data/' + str(i), data)
        print(result)

    for i in range(0, 4):
        string2=str(ser.readline())
        string2=string2[8:9]
        string2 = int(string2)
        data1 = {'date': datetime.now().strftime("%Y-%m-%d"),
                 'reading': string2,
                 'time': datetime.now().strftime("%H:%M")
                 }
        result1 = firebase1.patch('https://iot-project-1592f-default-rtdb.firebaseio.com/' + '/Flame_detection/' + str(i),
                                  data1)
        print(result1)
    for i in range(0, 4):
        string3=str(ser.readline())
        string3=string3[10:11]
        string3 = int(string3)
        data1 = {'date': datetime.now().strftime("%Y-%m-%d"),
                 'reading': string3,
                 'time': datetime.now().strftime("%H:%M")
                 }
        result2 = firebase1.patch('https://iot-project-1592f-default-rtdb.firebaseio.com/' + '/Smoke_detection/' + str(i),
                                  data1)
        print(result2)
    res = 0

