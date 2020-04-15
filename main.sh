

#!/bin/bash
# Bash Menu Script Example


mkdir "~SSM_WORKDIR"
PS3='Please pick the correct one.: '
options=("Ubuntu 64bit" "RHEL/AWS/CENTOS 64bit" "Pi")
select opt in "${options[@]}"
do
    case $opt in
        "Ubuntu 64bit")
            echo "Downloading the SSM agent for Ubuntu 64"
            wget -O ~SSM_WORKDIR/ssm.deb https://s3.ca-central-1.amazonaws.com/amazon-ssm-ca-central-1/latest/debian_386/amazon-ssm-agent.deb; break
            ;;
        "RHEL/AWS/CENTOS 64bit")
            echo "Downloading the SSM agent for RHEL 64"
            wget -O ~SSM_WORKDIR/ssm.rpm https://s3.ca-central-1.amazonaws.com/amazon-ssm-ca-central-1/latest/linux_amd64/amazon-ssm-agent.rpm; break
            ;;
        "Pi")
            echo "Downloading the SSM agent for pi (arm)"
            wget -O ~SSM_WORKDIR/ssm-pi.deb https://s3.ca-central-1.amazonaws.com/amazon-ssm-ca-central-1/latest/debian_arm/amazon-ssm-agent.deb; break
       
            ;;
            
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done





rm -rf "~SSM_WORKDIR"