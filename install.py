from config import *
from sweetmon import *
import socket
import getpass

##########################################################
# Check Dependencies
##########################################################
try:
    import requests
except ImportError as e:
    print("ImportError: %s" % (e))
    print("Please install the requests")
    exit()

##########################################################
# Register
##########################################################
if FUZZERINFO["TOKEN"] == None:
	F = Fuzzer(FUZZERINFO)
	print("[*] Input your key to access SWEETMON.. (You can find your key in your profile)")
	password = getpass.getpass()

	newToken = F.Register(password)
	if not newToken:
		print("[-] Could not register on server.")
		exit(-1)
	else:
		FUZZERINFO["TOKEN"] = newToken
		F.SetFUZZERINFO(FUZZERINFO)
		SaveConfig(FUZZERINFO)
else:
	print("[*] You've already installed the fuzzer. If you want to reset your configuration, please remove "+fConfigFile)
	exit(1)
