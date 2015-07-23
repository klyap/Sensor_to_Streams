import sys
import serial

port = "/dev/ttyACM1"
serialFromArduino = serial.Serial(port, 115200)
serialFromArduino.flushInput()

def getSensorData():
    print('*MPU-6050*')
    r_accel = serialFromArduino.readline()
    print(r_accel)
    r_temp = serialFromArduino.readline()
    print(r_temp)
    r_gyro = serialFromArduino.readline()
    print(r_gyro)

    accel = r_accel.split()
    temp = r_temp.split()
    gyro = r_gyro.split()
    acc_x, acc_y, acc_z = accel[2],accel[3],accel[4]
    temp = temp[1]
    gyro_x, gyro_y, gyro_z = gyro[2],gyro[3],gyro[4]

    return(acc_x,acc_y,acc_z,temp,gyro_x,gyro_y,gyro_z)

def main():
    print('starting...')
    while True:
        if(serialFromArduino.inWaiting() > 0):
            if(serialFromArduino.readline().find('*') != -1 and serialFromArduino.readline().find('=') != -1):
                acc_x,acc_y,acc_z,temp,gyro_x,gyro_y,gyro_z = getSensorData()
            
if __name__ == '__main__':
    main()
