import socket
import os
# def get_host_ip():
# 	try:
#		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#		s.connect(('8.8.8.8', 80))
#		ip = s.getsockname()[0]
#	finally:
#		s.close()
#
#	return ip
#
#if __name__ == '__main__':
#
#get_host_ip()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
ip = s.getsockname()[0]
s.close()
f = os.open('readme.txt','w')
f.write(ip)
f.close()
