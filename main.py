import subprocess

'''
class Device:
    def __init__(self,name,id):
        self.name = name
        self.id = id

'''
command = subprocess.run(["kdeconnect-cli","-l","--id-name-only"],capture_output=True,text=True)
devices_list = {x.partition(" ")[0]:x.partition(" ")[2] for x in str(command.stdout).split("\n") if x}
print("All devices:-")
for i in devices_list:
    print(devices_list[i])
print()

command = subprocess.run(["kdeconnect-cli","-a","--id-name-only"],capture_output=True,text=True)
online_list = [x.partition(" ")[0] for x in str(command.stdout).split("\n") if x]
print("Connected / Online devices:-")
for i in online_list:
    print(devices_list[i])
print()
