import requests
import os
from pathlib import Path
def write_and_install(url, filename, install, service_cycle):
    # Works for pi
    print("Downloading package")
    r = requests.get(url)
    
    with open(f"{Path.home()}/.SSM_WORKDIR/" + filename, 'wb') as f:
        f.write(r.content)

    for i in install.split('\n'):
        print(i)
        os.system(i)

    activation_code = input("Whats the activation code: ")
    activation_id = input("Whats the activationd id : ")
    region_name = input("Which region are we in   : ")
    print("Registration: ")
    os.system(f'sudo amazon-ssm-agent -register -code "{activation_code}" -id "{activation_id}" -region "{region_name}"')
    
    for i in service_cycle.split('\n'):
        os.system(i)
    
def teardown(teardown_cmd):
    for i in teardown_cmd.split('\n'):
        os.system(i)
    

print("1. Ubuntu\n2. RHEL\n3. Pi")

url_map = {
    1: {
        "url":"sudo snap install amazon-ssm-agent --classic",
        "install": "sudo snap install amazon-ssm-agent --classic\nsudo systemctl start snap.amazon-ssm-agent.amazon-ssm-agent.service\nsudo systemctl status snap.amazon-ssm-agent.amazon-ssm-agent.service\nsudo snap services amazon-ssm-agent"
    },
    2: {
        "url":"https://s3.ca-central-1.amazonaws.com/amazon-ssm-ca-central-1/latest/debian_arm/amazon-ssm-agent.deb",
        "install": ""
    },
    3: {
        "url":"https://s3.ca-central-1.amazonaws.com/amazon-ssm-ca-central-1/latest/debian_arm/amazon-ssm-agent.deb",
        "filename": "amazon-ssm-agent.deb",
        "install": "sudo dpkg -i ~/.SSM_WORKDIR/amazon-ssm-agent.deb\nsudo systemctl status amazon-ssm-agent",
        "service_cycle": "sudo systemctl restart amazon-ssm-agent\nsudo systemctl status amazon-ssm-agent | grep -i active",
        "teardown_cmd": "sudo systemctl stop amazon-ssm-agent\nsudo dpkg --remove amazon-ssm-agent"
    }
}

operating_system = int(input("Please choose your os: "))

url = url_map[operating_system]['url']
filename = url_map[operating_system]['filename']
install = url_map[operating_system]['install']
service_cycle = url_map[operating_system]['service_cycle']
teardown_cmd = url_map[operating_system]['teardown_cmd']
print(service_cycle)


write_and_install(url, filename, install, service_cycle)

input("Please hit enter once the work has been completed . . . ")

input("You sure? [hit enter again]: ")

teardown(teardown_cmd)
os.system("rm -rf ~/.SSM_WORKDIR")
