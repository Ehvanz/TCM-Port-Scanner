#!/bin/python3

import sys #System sprcific parameters
import socket #Used for communication
from datetime import datetime

#Define our target
if len(sys.argv) == 2: #Amount of arguments we are giving when we call the script
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPV4

else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("=" * 50)
print("Scanning target " + target)
print("Time Started: " + str(datetime.now()))
print("=" * 50)

try:
	for port in range(50,85):
		#Gather the IPV4 Address and the Port we are trying to connect to
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#If we dont get a response in 1sec we will move on
		socket.setdefaulttimeout(1)
		#Connect to our target supplied by us defined by sys.argv[1]
		#The port will be the range of 50 - 85
		#If port is open, s.connect_ex will return a 0 then print the open port
		result = s.connect_ex((target, port))
		if result == 0:
			#Prints open port then loops 
			print("Port {} is open".format(port))
			#If the port returns a 1, we close the socket connection
			#on that specific port
		s.close()

#If we ctrl + c while running
except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit()

#If the host isnt up
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

#If we cant connect
except socket.error:
	print("Could not connect to server.")
	sys.exit()
