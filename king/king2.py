#!/usr/bin/python

import socket
import sys

def checkPort(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((ip,int(port)))
	if result == 0:
		return True
	else:
		return False

def printData(ips):
	print("")
	print("")
	print("")
	print("====================NEW UPDATE====================")
	red = 0
	white = 0
	black = 0
	blue = 0
	green = 0
	yellow = 0
	for x in ips:
		score = 1
		if checkPort(x, 21):
			score += 1
		if checkPort(x, 22):
			score += 1
		if checkPort(x, 80):
			score += 1
		print(str(x) + ": " + str(ips[x]))
		if(ips[x] == "red"):
			red += score
		elif(ips[x] == "white"):
			white += score
		elif(ips[x] == "black"):
			black += score
		elif(ips[x] == "blue"):
			blue += score
		elif(ips[x] == "green"):
			green += score
		elif(ips[x] == "yellow"):
			yellow += score
	print("Red: " + str(red))
	print("White: " + str(white))
	print("Black: " + str(black))
	print("Blue: " + str(blue))
	print("Green: " + str(green))
	print("Yellow: " + str(yellow))
	print("====================END UPDATE====================")
	print("")
	print("")
	print("")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ips = {}
s.bind(("0.0.0.0", 8000))
s.listen(1000)

while True:
	try:
		conn, addr = s.accept()
		data = conn.recv(1024)
		team = data.split("team=")[1].split(",")[0]
		ip = data.split("ip=")[1]
		#print(team)
		#print(ip)

		if(ip in ips):
			if(ips[ip] != team):
				#new team!
				ips[ip] = team
				printData(ips)
				conn.send("Shocker! You've taken a machine from another team!\n")
			else:
				printData(ips)
				conn.send("Alrighty there mate, we've already got you in our system!\n")

		else:
			#not in dictionary yet, add it
			ips[ip] = team
			printData(ips)
			conn.send("Thank yee kindly, you've claimed your machine for the first time!\n")

		
		conn.close()
	except KeyboardInterrupt:
		printData(ips)
		print("Have a lovely day.")
		s.shutdown(socket.SHUT_RDWR)
		s.close()
		sys.exit()
	except :
		print("whoops")
