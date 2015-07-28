import sys
import serial

port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port, 9600)
serialFromArduino.flushInput()

def getSensorData():
    print('*DHT11*')
    input1 = serialFromArduino.readline()
    print(input1)
    tem = input1.split()[1]
    input2 = serialFromArduino.readline()
    print(input2)
    hum = input2.split()[1]
    return (float(tem), float(hum))

def main():
    print('starting...')

    while True:
        if(serialFromArduino.inWaiting() > 0):
            if(serialFromArduino.readline().find('*') != -1):
                tem, hum = getSensorData()
            
if __name__ == '__main__':
    main()
