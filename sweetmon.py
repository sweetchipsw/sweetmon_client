from config import *
import requests
import json
import inspect

##########################################################
# Define URL
##########################################################
URL = GLOBALINFO["SERVER_PROTOCOL"] + GLOBALINFO["SERVER_URL"]
URL_FUZZ = URL+"/fuzz"
URL_UPLOAD = URL+"/fuzz/crash"
URL_PING = URL+"/fuzz/ping"
URL_MACHINE = URL+"/machine"
URL_REGISTER = URL+"/fuzz/register"

##########################################################
# Define REQUESTS
##########################################################
# To prevent blocking by CSRF protection in Django.
DEFAULTHEADER = {"Cookie" : "csrftoken=sweetfuzz", "X-CSRFTOKEN":"sweetfuzz", "Referer":URL}

def POST(url, data, header=DEFAULTHEADER, **kwargs):
	# Wrap requests.post method
	# url : Str, data : Dict, header : Dict
	req = requests.post(url, headers=header, data=data, **kwargs)
	result = req
	return result

##########################################################
# Define Fuzzer Class
##########################################################
class Fuzzer:
	"""
		Fuzzing Fuzzing Fuzzing!

	"""
	def __init__(self, FUZZERINFO):

		self.FUZZERINFO = FUZZERINFO
		self.__initComplete = False; # Check init status.

		self.__numTestcase__ = 0;
		self.__numCrashes__ = 0;
		
		# Values comes frome FUZZERINFO
		self.__token = None
		self.__binary = None
		self.__currentdir = None

		self.__ParseInfo__() # Init Essential info

	def __ParseInfo__(self):
		# Parse Machine Information from FUZZERINFO
		# Token, Binary name, Current Directory
		fuzzerInfo = self.FUZZERINFO
		self.__token = fuzzerInfo["TOKEN"]
		self.__binary = fuzzerInfo["BINARY"]
		self.__currentdir = fuzzerInfo["CURRENT_DIR"]
		self.__initComplete = True
		return 1;

	#################################################################
	# Get / Set variable
	#################################################################
	def GetTestcaseCount(self):
		return self.__numTestcase__

	def GetCrashCount(self):
		return self.__numCrashes__

	def SetFUZZERINFO(self, NEWFUZZERINFO):
		self.FUZZERINFO = NEWFUZZERINFO
		self.__ParseInfo__()
		return True

	#################################################################
	# Interaction with server
	#################################################################
	def SendMachineInfo(self):
		strFuzzerInfo = json.dumps(self.FUZZERINFO)
		data = {"INFO" : self.FUZZERINFO}
		req = POST(URL_MACHINE, data)
		return 1;

	def Ping(self):
		data = {"token" : self.__token}
		try:
			result = POST(URL_PING, data).text
		except Exception as e:
			print("[*] Error at %s" % inspect.stack()[0][3], e)
		if result == "Done!":
			return True;
		return False;

	def RunPingThread(self):
		return True

	def Upload(self, title, crashLog, fname):
		data = {"token" : self.__token, "crashlog" : crashLog, "title":title}
		fdata = {'file': open(fname,'rb')}
		req = POST(URL_UPLOAD, data=data, files=fdata)
		return True;

	def Register(self, password):
		fuzzerInfo = self.FUZZERINFO
		
		data = { "password" : password, "fuzzer_name" : fuzzerInfo["FUZZERNAME"],
		"pub_ip" : fuzzerInfo["MACHINE"]["IP_PUB"],
		"pri_ip":fuzzerInfo["MACHINE"]["IP_PRI"], "target":fuzzerInfo["TARGET"]}

		result = POST(URL_REGISTER, data).text

		if len(result) == 40:
			print("[*] Success, Your token is : "+result)
			return result
		
		return False
