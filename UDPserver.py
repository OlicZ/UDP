import socket
import sys

host = ''
port = 8888

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	print "Socket Created"
except socket.error:
	print "Failed to create socket"
	sys.exit(1)

try:
	s.bind((host,port))
except socket.error:
	print "Binding Failed"
	sys.exit(1)

print "Socket Binding Complete!"

access = ''
Pass = raw_input("Enter your password: ")
if (Pass == 'olic'):
	access = 1
	
while (access == 1):
	print 'Waiting for response'
	d = s.recvfrom(1024)
	if d[0] == 'terminate':
		print "Terminated by user"
		access = 0
	data = d[0]
	addr = d[1]

	if not data:
		break
	reply = 'HI'

	s.sendto(reply, addr)
	print 'Message from[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()

s.close
