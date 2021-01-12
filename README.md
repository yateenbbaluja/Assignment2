**Beacon Scanner in Python**
========================
Introduction
------------------------
Beacon Scanner in Python is an application that scan any beacon either iBeacon or Eddystone and extract desired information.  


Install
------------------------
 * pip3 install beacontools
 * sudo apt-get install python3-dev libbluetooth-dev libcap2-bin
# grant the python executable permission to access raw socket data
 * sudo setcap 'cap_net_raw,cap_net_admin+eip' "$(readlink -f "$(which python3)")"
 * pip3 install beacontools[scan]


Testing
------------------------
 * Run 'python3 beacon_scanner.py'

Author
------------------------
* Yatin Baluja
