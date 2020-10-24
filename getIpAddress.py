import socket
import os
from time import strftime,gmtime
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
now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
f = open('readme.txt','w')
#f.seek(0)
#f.truncate()
f.write(ip+" "now+"\n")
f.close()
