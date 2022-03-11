import serial
import datetime
from mintsXU4 import mintsSensorReader as mSR
from mintsXU4 import mintsDefinitions as mD

dataFolder  = mD.dataFolder
qlmPort     = mD.radPorts[0]

def main():
    if(len(qlmPort)>=1):

        ser = serial.Serial(
        port= qlmPort,\
        baudrate=115200,\
        parity  =serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
        timeout=0)

        print(" ")
        print("Connected to: " + ser.portstr)
        print(" ")

        #this will store the line
        line = []

        while True:
            try:
                for c in ser.read():
                    line.append(chr(c))

                    if chr(c) == '\n':
                        dataString     = (''.join(line))
                        dataStringPost = dataString.replace('\n', '')
                        currentDateTime = datetime.datetime.now()
                        if dataString.find('START Watchdog Reset;')>0:
                            dataStringPost = dataStringPost.replace('START Watchdog Reset;', '')
                            mSR.QLMRAD001Write(dataStringPost,currentDateTime)
                            mSR.QLMRAD001Write("-100",currentDateTime)
                        else:
                            print("================")
                            print(dataStringPost)
                            mSR.QLMRAD001Write(dataStringPost,currentDateTime)
                        line = []
                        break

            except:
                print("Incomplete String Read")
                line = []
        ser.close()


if __name__ == "__main__":
   main()
