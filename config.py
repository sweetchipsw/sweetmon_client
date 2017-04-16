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
isDebug = True
########################################################################

# User Define Status
########################################################################
FUZZER_NAME = "TESTFUZZ"
FUZZING_TARGET = "TESTTARGET"
BINARY = "TESTBINARY"
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

	def GetToken(self):
		return self.token

	def SetToken(self, newToken):
		# Note that you should run Update() method after run this method.
		self.token = newToken
		self.Update()
		return True

	def __CheckToken(self):
		if self.token == None:
			print("[*] You should register on SWEETMON before running fuzzer.")

	def Update(self):
		# Update Information
		self.__GetOS()
		self.__GetPubIP()
		self.__GetPriIP()
		self.__GetUserName()
		self.__GetCurrentPath()

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

def CreateConfig(FUZZERINFO):
	SaveConfig(FUZZERINFO)
	return True

# Tools
def CHECKNULL(*args):
	for arg in args:
		if arg == "" or arg == None:
			print("Please fill variable first.")
			raise Exception
	return True

def DBGPRINT(*args):
	if isDebug == True:
		print(args)

#######################################################################
# MAIN
#######################################################################
# Check config variable
checkList = [FUZZER_NAME, FUZZING_TARGET, BINARY]
for element in checkList:
	CHECKNULL(element)

# Check Config file
if os.path.exists(fConfigFile) == False:
	print("[*] Create new Configuration file")

	machine = Machine(FUZZERINFO)
	machine.Update()
	FUZZERINFO = machine.Export()

	CreateConfig(FUZZERINFO)
else:
	FUZZERINFO = LoadConfig()

DBGPRINT("[*] Config file loaded.")
