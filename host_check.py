import os
import json

file = open('hosts.json')
data = json.load(file)
unreachables = []

for item in data["hosts"]:
    rackNumber = item["rackNumber"]
    leaf = item["leaf"]
    vlan = item["vlan"]
    hosts = item["hosts"]

    for ip in hosts:
        response = os.popen(f"ping -c 30 -i 0.2 {ip}").read()

        if "30 received" in response:
            print(f"Rack:{rackNumber} || Leafs:{leaf} || Vlan:{vlan} || IP:{ip} || Status: Reachable")
        else:
            print(f"Rack:{rackNumber} || Leafs:{leaf} || Vlan:{vlan} || IP:{ip} || Status: Unreachable")
            unreachables.append({"rack": rackNumber, "leaf": leaf, "vlan": vlan, "ip": ip})
print("\n")
print("::::::::::::::::::::::::: REPORT :::::::::::::::::::::::::\n")
for item in unreachables:
    print(f"Rack:{item['rack']} || Leaf:{item['leaf']} || Vlan:{item['vlan']} || IP:{item['ip']} || Status: Unreachable")
total_unreachables = len(unreachables)
print(f"Total unreachables = {total_unreachables}")
