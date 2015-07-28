import sys
import serial

port0 = "/dev/ttyACM0"
port1 = "/dev/ttyACM1"

serialFromArduino0 = serial.Serial(port0, 9600)
serialFromArduino0.flushInput()
serialFromArduino1 = serial.Serial(port1, 115200)
serialFromArduino1.flushInput()


def getSensorData0():
    print('*DHT11*')
    input1 = serialFromArduino0.readline()
    print(input1)
    tem = input1.split()[1]
    input2 = serialFromArduino0.readline()
    print(input2)
    hum = input2.split()[1]
    return (float(tem), float(hum))

def getSensorData1():
    print('*MPU-6050*')
    r_accel = serialFromArduino1.readline()
    print(r_accel)
    r_temp = serialFromArduino1.readline()
    print(r_temp)
    r_gyro = serialFromArduino1.readline()
    print(r_gyro)

    accel = r_accel.split()
    temp = r_temp.split()
    gyro = r_gyro.split()
    acc_x, acc_y, acc_z = accel[2],accel[3],accel[4]
    temp = temp[1]
    gyro_x, gyro_y, gyro_z = gyro[2],gyro[3],gyro[4]

    return(float(acc_x),float(acc_y),float(acc_z),float(temp),float(gyro_x),float(gyro_y),float(gyro_z))

def main():
    print('starting...')

    while True:
        if(serialFromArduino0.inWaiting() > 0 and serialFromArduino1.inWaiting() > 0):
            if(serialFromArduino0.readline().find('*') != -1 and serialFromArduino1.readline().find('*') != -1 and serialFromArduino1.readline().find('=')!= -1):
                tem, hum = getSensorData0()
                acc_x,acc_y,acc_z,temp,gyro_x,gyro_y,gyro_z = getSensorData1()
                print('Raw Data: ')
                print(tem,hum,acc_x,acc_y,acc_z,temp,gyro_x,gyro_y,gyro_z)
                print('\n')

if __name__ == '__main__':
    main()
