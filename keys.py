#Allows you to write a file anywhere. Used for writing ssh keys.

import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 55153))
s.listen(1000)

while True:
	conn, addr = s.accept()
	try:
		conn.sendall("This program allows you to save a file with any contents.\n")
		conn.sendall("Please enter the location of where you want to save the file: \n")
		location = conn.recv(1024)[:-1]
		conn.sendall("Great! Now enter the contents of your file:\n")
		data = conn.recv(1024)
		conn.sendall("Writing your file...\n") 
		text_file = open(location, "w")
		text_file.write(data)
		text_file.close()
		conn.sendall("Terminating your connection\n")
		conn.close()

	except:
		print "Whoops"
