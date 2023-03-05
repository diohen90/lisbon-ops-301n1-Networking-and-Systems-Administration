#Print "Hello World!" to the screen
echo "Hello World!"

#Ask user input
echo "Insert a number between 1 and 2"
read number

#If user input is correct show pings, if user input is incorrect do not show ping
if [ "$number" -lt 2 ]; then
echo "Good job, here is your Ping"
#Ping self (Loopback address)
ping -c 4 127.0.0.1

else
echo "Try again!"
exit

#IP Info (Print Network adapter from this computer)
ip link show wlp1s0

fi