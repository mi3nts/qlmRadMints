
from getmac import get_mac_address
import serial.tools.list_ports

def findPort(find):
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        currentPort = str(p)
        if(currentPort.endswith(find)):
            return(currentPort.split(" ")[0])

def findRadPorts():
    ports = list(serial.tools.list_ports.comports())
    outPorts = []
    for p in ports:
        currentPort = str(p[2])
        if(currentPort.find("PID=067B")>=0):
            outPorts.append(str(p[0]).split(" ")[0])
    return outPorts

def findMacAddress():
    macAddress= get_mac_address(interface="eth0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    macAddress= get_mac_address(interface="docker0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    macAddress= get_mac_address(interface="enp1s0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    macAddress= get_mac_address(interface="wlan0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    return "xxxxxxxx"



dataFolderReference       = "/home/teamlary/mintsData/reference"
dataFolderMQTTReference   = "/home/teamlary/mintsData/referenceMQTT"
dataFolder                = "/home/teamlary/mintsData/raw"
dataFolderMQTT            = "/home/teamlary/mintsData/rawMQTT"

macAddress            = findMacAddress()
latestDisplayOn       = False
latestOn              = False
radPorts               = findRadPorts()
# For MQTT 
mqttOn                    = True
mqttCredentialsFile      = 'mintsXU4/credentials.yml'
mqttBroker               = "mqtt.circ.utdallas.edu"
mqttPort                 =  8883  # Secure port


if __name__ == "__main__":
    # the following code is for debugging
    # to make sure everything is working run python3 mintsDefinitions.py 
    print("Mac Address          : {0}".format(macAddress))
    print("Data Folder Reference: {0}".format(dataFolderReference))
    print("Data Folder Raw      : {0}".format(dataFolder))
    print("Latest On            : {0}".format(latestDisplayOn))
    print("Latest On                  : {0}".format(latestOn))
    print("MQTT On                    : {0}".format(mqttOn))
    print("MQTT Credentials File      : {0}".format(mqttCredentialsFile))
    print("MQTT Broker and Port       : {0}, {1}".format(mqttOn,mqttPort))
   #-------------------------------------------#
    print("QLM Port :")
    for dev in radPorts:
        print("\t{0}".format(dev))
    
   
