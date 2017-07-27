import socket
import sys

#create UDP socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print "Failed to create socket"
	sys.exit(1)

print "connection complete!"

host = '127.0.0.1'
port = 8888

#initial message
message = ''
message = raw_input("Enter your message: ")

#send the message and receive replies from the server
access = 1
while (access == 1):
	s.sendto(message, (host,port))
	if message == 'terminate':
		print "terminated the server, disconnecting"
		access = 0
		sys.exit(1)
	d = s.recvfrom(1024)
	print 'Received from server: ' + str(d[0])
	message = raw_input(" Enter your message: ")
s.close()
