import serial

yaw = 0
pitch = 0
roll = 0

ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate = 4800,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )

def calculate():
        global yaw
        global pitch
        global roll
        global ser
        temp = ""

        i = 0
        j = 0
        x = str(ser.readline())
        if(len(x) > 7 and len(x) < 15):
                indexData = len(x) - 2
                i = 0
                while (i < indexData):
                        if(x[i] == ','):
                                if(j == 0):
                                        yaw = int(temp)
                                        print("Yaw = " + str(yaw))
                                        j = j + 1
                                        temp = ""
                                elif(j == 1):
                                        pitch = (temp)
                                        print("Pitch = " + str(pitch))
                                        j = j + 1
                                        temp = ""
                                elif(j == 2):
                                        roll = int(temp)
                                        print("Roll = " + str(roll))
                                        j = 0
                                        temp = ""
                        else:
                                temp = temp + x[i]      
                        i = i + 1

def get_yaw():
        global yaw
        return yaw

def get_pitch():
        global pitch
        return pitch

def get_roll():
        global roll
        return roll
