#This program is vulnerable to command injection.
#It simply echoes back input. To inject your own code, end the echo with a semicolon (;), then write your own code. 
#It listens on port 55152 for someone to listen to.
import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 55152))
s.listen(1000)

while True:
	conn, addr = s.accept()
	try:
		conn.sendall("This program echoes back any input!\n")
		while True:
			data = conn.recv(1024)
			proc = subprocess.Popen(["echo " + data], stdout=subprocess.PIPE, shell=True)
			out = proc.stdout.read()
			conn.sendall(out)
	except:
		print "Whoops"



