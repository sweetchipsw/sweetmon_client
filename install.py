#!/bin/python3
from config import *
import socket

try:
    import requests
except ImportError, e:
    print "ImportError: %s" % (e)
    print "Did you try installing rsa package?"
    print "Try : sudo pip install requests"
    exit()

DEFAULTHEAD = {"Cookie" : "csrftoken=sweetfuzz", "X-CSRFTOKEN":"sweetfuzz"}

def SendPostResult(url, data, header=DEFAULTHEAD):
	data = data
	req = requests.post(url, header=header, data=data)
	result = req.json()

password = ""
ip_pub = ""
print([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
# print(GetPriIP())