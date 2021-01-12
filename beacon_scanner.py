import time
from beacontools import BeaconScanner, EstimoteTelemetryFrameA, EstimoteTelemetryFrameB, EstimoteFilter,BeaconScanner, IBeaconFilter, IBeaconAdvertisement, EddystoneTLMFrame, EddystoneFilter, EddystoneUIDFrame, EddystoneURLFrame
from beacontools import parse_packet

def callback(bt_addr, rssi, packet, additional_info):
    print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))

scanner = BeaconScanner(callback, 
    packet_filter=[EstimoteTelemetryFrameA],
    #device_filter=EstimoteFilter(identifier="47a038d5eb032640")
    
)

scanner1 = BeaconScanner(callback,
    packet_filter=IBeaconAdvertisement 
   
)

scanner2 = BeaconScanner(callback,
    #device_filter=EddystoneFilter(namespace="12345678901234678901"),
    packet_filter=[EddystoneTLMFrame, EddystoneUIDFrame]
    
)

scanner.start()
time.sleep(10)
scanner1.stop()
scanner1.start()
scanner2.start()
time.sleep(30)
scanner.stop()
scanner2.stop()

'''
# iBeacon Advertisement
ibeacon_packet = b"\x02\x01\x06\x1a\xff\x4c\x00\x02\x15\x53\x59\x4F\x4F\x4B\x53\x4F\x43\x49" \
                 b"\x41\x4C\x44\x49\x53\x54\x45\x00\x00\x00\x00\xE8"
adv = parse_packet(ibeacon_packet)
print("UUID: %s" % adv.uuid)
print("Major: %d" % adv.major)
print("Minor: %d" % adv.minor)
print("TX Power: %d" % adv.tx_power)
print("-----")

# telemetry Advertisement
telemetry_a_packet =  b"\x02\x01\x06\x03\x03\xe1\xff\x12\x16\xe1\xff\xa1\x03\x64\xff\xf4"\
                      b"\x00\x0f\xff\x00\x37\x72\xa3\x3f\x23\xac"

telemetry = parse_packet(telemetry_a_packet)
print("Identifier: %s" % telemetry.identifier)
print("Protocol Version: %d" % telemetry.protocol_version)
print("Acceleration (g): (%f, %f, %f)" % telemetry.acceleration)
print("Is moving: %s" % telemetry.is_moving)
print("-----")
'''
