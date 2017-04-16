from config import *
import requests


##########################################################
# Define URL
##########################################################
URL = GLOBALINFO["SERVER_PROTOCOL"] + GLOBALINFO["SERVER_URL"]
URL_FUZZ = URL+"/fuzz"
URL_UPLOAD = URL+"/upload"
URL_PING = URL+"/ping"

##########################################################
# Define Fuzzer Class
##########################################################

class Fuzzer:
	"""
		Fuzzing Fuzzing Fuzzing!

	"""
	def __init__(self, FUZZERINFO):
		# Init Fuzzer

		self.FUZZERINFO = FUZZERINFO
		self.__numTestcase__ = 0;
		self.__numCrashes__ = 0;
		self.initComplete = False; # Check init status.

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

	def GetTestcaseCount(self):
		return self.__numTestcase__

	def GetCrashCount(self):
		return self.__numCrashes__

	def SetFUZZERINFO(self, NEWFUZZERINFO):
		self.FUZZERINFO = NEWFUZZERINFO
	
	def SendMachineInfo(self):
		self.FUZZERINFO

		return 1;

	def Ping(self):
		post = {"token" : self.__token}
		result = requests.post(URL_PING, post).text
		if result == "success":
			return True;
		return False;

	def RunPingThread(self):
		return True

	def UploadCrash(self):
		req = requests.post(URL_UPLOAD)
		return 1;


if __name__ == '__main__':
	main()