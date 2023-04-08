#!/usr/bin/python3

import os

# Run the "whoami" command and capture the output
whoami_output = os.popen('whoami').read().strip()

# Run the "ip a" command and capture the output
ip_output = os.popen('ip a').read().strip()

# Run the "lshw -short" command and capture the output
lshw_output = os.popen('lshw -short').read().strip()

# Print the output of the three commands
print("Output of 'whoami' command:")
print(whoami_output)

print("Output of 'ip a' command:")
print(ip_output)

print("Output of 'lshw -short' command:")
print(lshw_output)