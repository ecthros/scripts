#!/usr/bin/python

import socket

def printData(ips):
	print("")
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
		print(str(x) + ": " + str(ips[x]))
		if(ips[x] == "red"):
			red += 1
		elif(ips[x] == "white"):
			white += 1
		elif(ips[x] == "black"):
			black += 1
		elif(ips[x] == "blue"):
			blue += 1
		elif(ips[x] == "green"):
			green += 1
		elif(ips[x] == "yellow"):
			yellow += 1
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
	print("")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ips = {}
s.bind(("0.0.0.0", 8000))
s.listen(1000)

while True:
	conn, addr = s.accept()
	try:
		data = conn.recv(1024)
		team = data.split("team=")[1].split(",")[0]
		ip = data.split("ip=")[1]
		print(team)
		print(ip)

		if(ip in ips):
			if(ips[ip] != team):
				#new team!
				ips[ip] = team
				printData(ips)
			else:
				pass

		else:
			#not in dictionary yet, add it
			ips[ip] = team
			printData(ips)

		conn.send("Got it, thanks\n")
		conn.close()
	except :
		print("whoops")
