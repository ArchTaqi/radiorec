#!/usr/bin/env bash

## SECRET
export ACCESS_TOKEN=''
export TARGET_DIR='/radiorec'
export RECORD_NOW=1
export RECORD_NOW_DURATION=0.1

## CRON JOBS

#01 02 * * * ubuntu echo 'cd /home/ubuntu/radiorec; python3 /home/ubuntu/radiorec/src/main.py' | /bin/bash
#10 04 * * * ubuntu echo 'cd /home/ubuntu/radiorec; python3 /home/ubuntu/radiorec/src/main.py' | /bin/bash
#01 12 * * * ubuntu echo 'cd /home/ubuntu/radiorec; python3 /home/ubuntu/radiorec/src/main.py' | /bin/bash
#01 21 * * * ubuntu echo 'cd /home/ubuntu/radiorec; python3 /home/ubuntu/radiorec/src/main.py' | /bin/bash



#sudo apt-get install python3 python3-pip
#virtualenv -p python3 venv
#virtualenv --python=/usr/local/bin/python3 venv