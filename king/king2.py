#!/usr/bin/python

import socket
import sys
import time
from threading import Thread
import operator


def checkPort(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(0.5)
	result = sock.connect_ex((ip,int(port)))
	if result == 0:
		return True
	else:
		return False

scores = {"red": 0.0, "white": 0.0, "black": 0.0, "blue": 0.0, "green": 0.0, "yellow": 0.0, "purple": 0.0, "orange": 0.0}
ips = {}

def printData():
	global ips
	global scores
	multiplier = 1
	lastPrinted = 0	
	while True:
		if(time.time() > lastPrinted + 15):
			print("")
			print("")
			print("")
			print("======NEW UPDATE======")
			print ""
			for x in ips:
				score = 0
				if checkPort(x, 21):
					score += 1
				if checkPort(x, 22):
					score += 1
				if checkPort(x, 80):
					score += 1
				print(str(x) + ": " + str(ips[x]) + " - " + str(score) + " services running")
				score *= multiplier
				if(ips[x] == "red"):
					scores["red"] += score
				elif(ips[x] == "white"):
					scores["white"] += score
				elif(ips[x] == "black"):
					scores["black"] += score
				elif(ips[x] == "blue"):
					scores["blue"] += score
				elif(ips[x] == "green"):
					scores["green"] += score
				elif(ips[x] == "yellow"):
					scores["yellow"] += score
				elif(ips[x] == "purple"):
					scores["purple"] += score
				elif(ips[x] == "orange"):
					scores["orange"] += score
			print ""
			sorted_ips = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
			for ip, score in sorted_ips:
				print(str(ip) + ": " + str(score))
			print ""
			print("======END UPDATE======")
			print("")
			print("")
			print("")
			lastPrinted = time.time()
			multiplier += multiplier * .01
			print(multiplier)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8001))
s.listen(1000)

lastUpdate = {}
thread1 = Thread(target=printData, args=())
thread1.start()
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
				if(time.time() > lastUpdate[ip] + 2):
					ips[ip] = team
					conn.send("Shocker! You've taken a machine from another team!\n")
				else:
					conn.send("You're too quick there son, try waiting for a bit longer!\n")
			else:
				if(time.time() > lastUpdate[ip] + 60):
					conn.send("Alrighty there mate, we've already got you in our system!\n")
				else:
					conn.send("Seems unfair that you can just keep claiming your own machine... NAY! Just for that, I'll reset your timer for you. You're gonna have to wait for a while now!")

		else:
			#not in dictionary yet, add it
			ips[ip] = team
			conn.send("Thank yee kindly, you've claimed your machine for the first time!\n")

		lastUpdate[ip] = time.time()
		
		conn.close()
	except KeyboardInterrupt:
		print("Have a lovely day.")
		s.shutdown(socket.SHUT_RDWR)
		s.close()
		thread1.join()
		sys.exit()
	except Exception as e:
		print e
		print("whoops")
