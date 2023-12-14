import os
import json
import sys

file = open('hosts.json')
data = json.load(file)
unreachables = []
if len(sys.argv) > 1:
    arg_vlan = sys.argv[1]
else:
    arg_vlan = None


for item in data["hosts"]:
    rackNumber = item["rackNumber"]
    leaf = item["leaf"]
    vlan = item["vlan"]
    hosts = item["hosts"]

    for ip in hosts:
        if arg_vlan is not None:
            if vlan == int(arg_vlan):
                response = os.popen(f"ping -c 30 -i 0.2 {ip}").read()

                if "30 received" in response:
                    print(f"Rack:{rackNumber} || Leafs:{leaf} || Vlan:{vlan} || IP: {ip} || Status: Reachable")
                else:
                    print(f"Rack:{rackNumber} || Leafs:{leaf} || Vlan:{vlan} || IP: {ip} || Status: Unreachable")
                    unreachables.append({"rack": rackNumber, "leaf": leaf, "vlan": vlan, "ip": ip})
        else:
            response = os.popen(f"ping -c 30 -i 0.2 {ip}").read()

            if "30 received" in response:
                print(f"Rack:{rackNumber} || Leafs:{leaf} || Vlan:{vlan} || IP: {ip} || Status: Reachable")
            else:
                print(f"Rack:{rackNumber} || Leafs:{leaf} || Vlan:{vlan} || IP: {ip} || Status: Unreachable")
                unreachables.append({"rack": rackNumber, "leaf": leaf, "vlan": vlan, "ip": ip})
            
print("\n")
print("::::::::::::::::::::::::: REPORT :::::::::::::::::::::::::\n")
for item in unreachables:
    print(f"Rack:{item['rack']} || Leaf:{item['leaf']} || Vlan:{item['vlan']} || IP:{item['ip']} || Status: Unreachable")
total_unreachables = len(unreachables)
print(f"Total unreachables = {total_unreachables}")
