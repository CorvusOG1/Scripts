import os
import subprocess

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing: {command}\n{e}")
        exit(1)

def main():
    tools_dir = os.path.expanduser('~/tools')
    os.makedirs(tools_dir, exist_ok=True)

    # Download pspy64
    pspy_url = "https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64"
    pspy_path = os.path.join(tools_dir, "pspy64")
    run_command(f"curl {pspy_url} -o {pspy_path}")

    # Install feroxbuster
    run_command("sudo apt install -y feroxbuster")

    # Download rustscan
    rustscan_url = "https://github.com/RustScan/RustScan/releases/download/2.0.1/rustscan_2.0.1_amd64.deb"
    rustscan_path = os.path.join(tools_dir, "rustscan_2.0.1_amd64.deb")
    run_command(f"curl {rustscan_url} -o {rustscan_path}")

    # Install rustscan
    run_command(f"sudo dpkg -i {rustscan_path}")

    # Download linpeas.sh
    linpeas_url = "https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/linpeas.sh"
    linpeas_path = os.path.join(tools_dir, "linpeas.sh")
    run_command(f"curl {linpeas_url} -o {linpeas_path}")

    # Download winPEASx64.exe
    winpeas_url = "https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/winPEASx64.exe"
    winpeas_path = os.path.join(tools_dir, "winpeas64.exe")
    run_command(f"curl {winpeas_url} -o {winpeas_path}")

if __name__ == "__main__":
    main()
