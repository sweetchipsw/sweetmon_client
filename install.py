from config import *
from sweetmon import *
import socket
import getpass

##########################################################
# Check Dependencies
##########################################################
try:
    import requests
except ImportError, e:
    print "ImportError: %s" % (e)
    print "Did you try installing rsa package?"
    print "Try : sudo pip install requests"
    exit()

##########################################################
# Register
##########################################################
if FUZZERINFO["TOKEN"] == None:
	F = Fuzzer(FUZZERINFO)
	print("[*] Input password to access SWEETMON.. ")
	password = getpass.getpass()

	newToken = F.Register(password)
	if newToken == False:
		print("[-] Could not register on server.")
		exit(-1)
	else:
		FUZZERINFO["TOKEN"] = newToken
		F.SetFUZZERINFO(FUZZERINFO)
		SaveConfig(FUZZERINFO)
else:
	print("[*] You've installed fuzzer. If you want to reset config, please remove "+fConfigFile)
	exit(1)