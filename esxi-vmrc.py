
import pysphere
import requests

requests.packages.urllib3.disable_warnings()

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

from pysphere import VIServer

server = VIServer()
HOST = "172.17.11.74"
LOGIN = "root"
PASSWORD = "password"
server.connect(HOST, LOGIN, PASSWORD)

oc = []
oc.append(server._retrieve_properties_traversal(obj_type='VirtualMachine'))

power = []
machines = server.get_registered_vms()

for machine in server.get_registered_vms():
    power.append(server.get_vm_by_path(machine).get_status())

zindex = -1

for elem in oc:
    for b in elem:
        s = (b)
        zindex = zindex + 1
        print "vmrc://" + LOGIN + ":" + PASSWORD + "@" + HOST + ":443/?moid=" + s.Obj, machines[zindex], power[zindex]

server.disconnect()