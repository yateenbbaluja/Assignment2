from bluepy.btle import Scanner, DefaultDelegate
import binascii
from igsparser import MsdParser
import pprint
import blescan
import sys
import bluetooth._bluetooth as bluez

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print ("ble thread started")

except:
    print ("error accessing bluetooth device...")
    sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
	returnedList = blescan.parse_events(sock, 10)
	print ("----------")
	for beacon in returnedList:
		print (beacon)
# MACs of IBSXX devices
ibs = [
        '12:34:56:78:90:00'
]

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if dev.addr.upper() in ibs:
            value = dev.getValueText(255)
            if value:
                if type(value) is not str:
                    # for python2, convert unicode to str
                    value = value.encode('ascii', 'ignore')
                data = MsdParser.parse(value)
                pprint.pprint(vars(data))

scanner = Scanner().withDelegate(ScanDelegate())
scanner.start()
while True:
    scanner.process()
