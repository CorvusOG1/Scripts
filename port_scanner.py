import subprocess
import re

IP = input("IP: ")
ulimit = str(5000)

# Run RustScan to scan for open ports
rustscan_output = subprocess.check_output(["rustscan", "-a", IP, "-g", "--ulimit", ulimit])

match = re.search(r"\[(.*?)\]", str(rustscan_output))

if match:
    # takes out the unwanted characters
    ports_string = match.group(1)
    ports = [port.strip() for port in ports_string.split(",")]

nmap_command = ("nmap", "-sV", "-sC", "-p", ports_string, IP)
subprocess.run(nmap_command)
