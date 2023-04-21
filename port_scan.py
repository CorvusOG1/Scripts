import subprocess
import re

IP = input("IP: ")
machine = input("File Name: ")

# Run RustScan to scan for open ports
rustscan_output = subprocess.check_output(["rustscan", "-a", IP, "-g"])

#put contest of rustscan into a file
ports1 = rustscan_output
with open(machine, 'w') as f:
    f.write(str(ports1))

###### takes out the unwanted characters
with open(machine, "r") as f:
    contents = f.read()

match = re.search(r"\[(.*?)\]", contents)

if match:
    ports_string = match.group(1)
    ports = [int(port.strip()) for port in ports_string.split(",")]
####### takes out the unwanted characters


####### converts integer ports to str
output = ""

for i, port in enumerate(ports):
    output += str(port)
    if i < len(ports) - 1:
        output += ","

separator = ","

output = separator.join(str(x) for x in ports)
###### converts integer ports to string

rm_file = ("rm", machine)
subprocess.run(rm_file)

#subprocess.check_output(["rm", machine])


nmap_command = ("nmap", "-sV", "-sC", "-p", output, IP)
subprocess.run(nmap_command)
