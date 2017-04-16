from config import *
import requests
import json
import inspect

##########################################################
# Define URL
##########################################################
URL = GLOBALINFO["SERVER_PROTOCOL"] + GLOBALINFO["SERVER_URL"]
URL_FUZZ = URL+"/fuzz"
URL_UPLOAD = URL+"/upload"
URL_PING = URL+"/ping"
URL_MACHINE = URL+"/machine"
URL_REGISTER = URL+"/fuzz/register"


##########################################################
# Define REQUESTS
##########################################################
# To prevent blocking by CSRF Token in Django.
DEFAULTHEADER = {"Cookie" : "csrftoken=sweetfuzz", "X-CSRFTOKEN":"sweetfuzz", "Referer":URL}

def POST(url, data, header=DEFAULTHEADER):
	# Wrap requests.post method
	# url : Str, data : Dict, header : Dict
	req = requests.post(url, headers=header, data=data)
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
		self.initComplete = False; # Check init status.

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
		self.initComplete = True
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
		post = {"INFO" : self.FUZZERINFO}
		req = POST(URL_MACHINE, post)
		return 1;

	def Ping(self):
		post = {"token" : self.__token}
		try:
			result = POST(URL_PING, post).text
		except Exception as e:
			print("[*] Error at %s" % inspect.stack()[0][3], e)
		if result == "success":
			return True;
		return False;

	def RunPingThread(self):
		return True

	def UploadCrash(self):
		post = {}
		req = POST(URL_UPLOAD, post)
		return 1;

	def Register(self, password):
		fuzzerInfo = self.FUZZERINFO
		
		post = { "password" : password, "fuzzer_name" : fuzzerInfo["FUZZERNAME"],
		"pub_ip" : fuzzerInfo["MACHINE"]["IP_PUB"],
		"pri_ip":fuzzerInfo["MACHINE"]["IP_PRI"], "target":fuzzerInfo["TARGET"] }

		result = POST(URL_REGISTER, post).text

		if len(result) == 40:
			print("[*] Success, Your token is : "+result)
			return result
		
		return False


# if __name__ == '__main__':
# 	main()