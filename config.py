########################################################
# PROJECT SWEETMON CLIENT
# Optimized Libfuzzer
########################################################
import json
import requests
import platform
import getpass
import socket
import os

# STATIC CONFIG
########################################################################
fConfigFile = "config.json"
########################################################################

# User Define Status
########################################################################
FUZZER_NAME = "TESTFUZZ"
FUZZING_TARGET = "TESTTARGET"
BINARY = ""
########################################################################


# Fuzzer Information
########################################################################
# YOU CAN MODIFY GLOBAL INFO
GLOBALINFO = {
	"SERVER_URL" : "sweetfuzz.sweetchip.kr", # Sweetmon
	"SERVER_PROTOCOL" : "https://", # Protocol, Default
	"TIME_PING" : 60, # Sec (Seconds)
	"TIME_MAXTIME" : 70, # MS (MiliSeconds)
	"MAXMEM" : 70, # MB (For Libfuzzer)
}

# DO NOT MODIFY FUZZERINFO
FUZZERINFO = {
	# Fill Automatic
	"FUZZERNAME":FUZZER_NAME,
	"TARGET":FUZZING_TARGET,
	"OWNER":"",
	"CURRENT_DIR":"",
	"TOKEN":"",
	"BINARY":BINARY,
	"MACHINE" : {
		"OS" : None,
		"IP_PUB" : "",
		"IP_PRI" : "",
	},
}

INFO = {"GLOBALINFO" : GLOBALINFO, "FUZZERINFO" : FUZZERINFO }

########################################################################


class Machine:
	"""
		Filling information of Machine
			OS, IP(Public, Private), Current Path, User Name
	"""
	def __init__(self, FUZZERINFO):
		self.os = None
		self.pubIp = None
		self.priIp = None
		self.currentPath = None
		self.userName = None
		self.FUZZERINFO = FUZZERINFO
		self.token = None

	def __GetOS(self):
		# Expected Result : Windows 10
		self.os = platform.system() + " " + platform.release()
		return True

	def __GetPubIP(self):
		HOST = "http://httpbin.org/ip"
		try:
			req = requests.get(HOST).text
			pubIp = json.loads(req)['origin']
			self.pubIp = pubIp
		except Exception as e:
			print "Could not get IP from "+HOST+" (Check your internet connection)"
			return False
		return True

	def __GetPriIP(self):
		HOST = "httpbin.org"
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((HOST, 80))
			priIp = s.getsockname()[0]
			s.close()
		except Exception as e:
			print("Could not get Private IP address from %s" % HOST)
		self.priIp = priIp
		return True

	def __GetCurrentPath(self):
		result = os.path.dirname(os.path.abspath(__file__))
		self.currentPath = result
		return True

	def __GetUserName(self):
		result = getpass.getuser()
		self.userName = result
		return True

	def __GetTokenFromServer(self):
		currentToken = self.FUZZERINFO["TOKEN"]
		# If already has token..
		if currentToken != "":
			self.token = currentToken
			return True
		# Get New token
		self.token = "TEMPTOKEN"
		return True


	def Update(self):
		# Update Information
		self.__GetOS()
		self.__GetPubIP()
		self.__GetPriIP()
		self.__GetUserName()
		self.__GetCurrentPath()
		self.__GetTokenFromServer()

		# Fill it to dictionary
		self.FUZZERINFO["OWNER"] = self.userName
		self.FUZZERINFO["CURRENT_DIR"] = self.currentPath
		self.FUZZERINFO["MACHINE"]["OS"] = self.os
		self.FUZZERINFO["MACHINE"]["IP_PUB"] = self.pubIp
		self.FUZZERINFO["MACHINE"]["IP_PRI"] = self.priIp
		self.FUZZERINFO["TOKEN"] = self.token
		return FUZZERINFO

	def Export(self):
		return self.FUZZERINFO
		

# Configuration Files
def LoadConfig():
	# Load configuration file from 'fConfigFile'
	f = open(fConfigFile, "rb")
	result = f.read()
	f.close()

	objDict = json.loads(result)
	
	return objDict

def SaveConfig(dictionary):
	strDict = json.dumps(dictionary)
	f = open(fConfigFile, "wb")
	f.write(strDict)
	f.close()

	return True

def CreateConfig():
	SaveConfig(INFO)
	return True

# Tools
def CHECKNULL(*args):
	for arg in args:
		if arg == "" or arg == None:
			raise
	return True

if __name__ == '__main__':
	# Check Config file

	# Load config file

	# Check config variable

	# Update Info
	env = Machine(FUZZERINFO)
	env.Update()
	FUZZERINFO = env.Export()

	print(FUZZERINFO)

