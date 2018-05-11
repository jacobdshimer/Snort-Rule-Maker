#!/usr/bin/python3

# import only system from os
from os import system, name

# define our clear function
def clear():

# for windows
	if name == 'nt':
		_ = system('cls')

# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

def interactive():
	clear()
	rule = ""
	print("What would you like this rule to do?")
	print("\t1) Alert")
	print("\t2) Reject")
	print("\t3) Drop")
	action = input(">> ")
	if action == "1":
		rule = "alert "
	elif action == "2":
		rule = "reject "
	elif action == "3":
		rule = "drop "
	clear()

	print("What is the protocol used?")
	print("\t1) TCP")
	print("\t2) UDP")
	print("\t3) ICMP")
	protocol = input(">> ")
	if protocol == "1":
		rule = str(rule) + "tcp "
	elif protocol == "2":
		rule = str(rule) + "udp "
	elif protocol == "3":
		rule = str(rule) + "icmp "
	clear()

	print("What is the source address and source port for the rule? Type them as address:port")
	print("You can group addresses together by typing them like this:")
	print("[192.168.1.1,192.168.1.2,192.168.1.3]")
	print("192.168.1.0/24 for the address block of 255.255.255.0")
	print("To exclude an IP address (i.e. tell the rule to apply to all IP addresses except the specified one) you can type this:")
	print("!192.168.1.1")
	print("This can be grouped with the above mentioned grouping to specify multiple IP addresses to ignore.")
	print("If specifing a range of ports, you can type them as address:port:port")
	source = input(">> ")
	source = source.split(":")
	if len(source) > 2:
		rule = rule + str(source[0]) + " " + str(source[1]) + ":" + str(source[2])
	else:
		rule = rule + str(source[0]) + " " + str(source[1])
	clear()

	print("What direction is the rule being applied to?")
	print("\t1) Source to Destination?")
	print("\t2) Desetination to Source")
	print("\t3) Bidirectional")
	direction = input(">> ")
	if direction == "1":
		rule = str(rule) + "-> "
	elif direction == "2":
		rule = str(rule) + "<- "
	elif direction == "3":
		rule = str(rule) + "<> "
	clear()

	print("What is the destination address and destination port for the rule? Type them as address:port")
	print("You can group addresses together by typing them like this:")
	print("[192.168.1.1,192.168.1.2,192.168.1.3]")
	print("192.168.1.0/24 for the address block of 255.255.255.0")
	print("To exclude an IP address (i.e. tell the rule to apply to all IP addresses except the specified one) you can type this:")
	print("!192.168.1.1")
	print("This can be grouped with the above mentioned grouping to specify multiple IP addresses to ignore.")
	print("If specifing a range of ports, you can type them as address:port:port")
	destination = input(">> ")
	destination = destination.split(":")
	if len(destination) > 2:
		rule = rule + str(destination[0]) + " " + str(destination[1]) + ":" + str(destination[2])
	else:
		rule = rule + str(destination[0]) + " " + str(destination[1])
	clear()

	rule = rule + "()"
	print(rule)

if __name__ == "__main__":
	interactive()
	  
