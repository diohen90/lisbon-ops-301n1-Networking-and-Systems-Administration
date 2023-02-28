#!/bin/bash

#copies /var/log/syslog to current working directory

cp -r /var/log/journal/a3845a9813ed4f069d8b2c692e838cd2/system.journal /home/diogo/$(date +%d-%m-%Y_%H:%M:%S)

echo "Done"
