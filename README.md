# SWEETMON-client

This project is a python module to interact with '[SWEETMON](https://github.com/sweetchipsw/sweetmon)' project.

Fuzz testers can adapt their fuzzer easily.

## Fast Install & Usage

### Prerequirement

- You should install sweetmon first to use this project. 
- Sweetmon : https://github.com/sweetchipsw/sweetmon
- Install Python3
  - Download python3 at http://python.org/ on Windows
  - ```apt-get install python3``` on Linux.
- Install Python package
  - ```pip3 install requests```

### Clone project

- ```git clone https://github.com/sweetchipsw/sweetmon_client.git```



### Get token from sweetmon

1. Please fill the contents in config.py. (Important)

   ```python
   FUZZER_NAME = "" # AWESOMEFUZZER
   FUZZING_TARGET = "" # Weak_application
   BINARY = "" # your_fuzzer
   SERVER_URL = "" # sub.domain.com / 127.0.0.1
   SERVER_PROTOCOL = "https://" # or http://
   ```

2. Run install.py

3. ```shell
   $ python install.py
   [*] Create new Configuration file
   [*] Input your userkey to access SWEETMON.. (You can find your key at your profile)
   Password:
   [*] Success, Your token is : d9a93042e67459df842c3b429a742790b805c056
   ```

4. Now you can adapt sweetmon-client for your fuzzer.



## Example

1. Simple Test

   ```python
   from sweetmon import *

   # Init
   F = Fuzzer()

   # F.Ping()
   print("PING Test", F.Ping()) # Ping to server

   # Upload("Title string", "Log string", "/Crash/location")
   print("Upload Test", F.Upload("AddressSanitizer: heap-buffer-overflow ...", "LOG Contents", "./sweetfuzz/crash/crash1"))

   print("END OF TEST..")
   ```

   ​

## Files

* config.py : Configuration file.
* install.py : Install dependencies and regist fuzzer to the server.
* sweetmon.py : Core script / API 



### Information

```json
# YOU CAN MODIFY GLOBAL INFO
GLOBALINFO = {
	"SERVER_URL" : SERVER_URL, # Sweetmon
	"SERVER_PROTOCOL" : SERVER_PROTOCOL, # Protocol, Default
	"TIME_PING" : 60 # Sec (Seconds)
}

# DO NOT MODIFY FUZZERINFO
FUZZERINFO = {
	# Fill Automatic
	"FUZZERNAME":FUZZER_NAME,
	"TARGET":FUZZING_TARGET,
	"OWNER":"",
	"CURRENT_DIR":"",
	"TOKEN":"",
	"MACHINE" : {
		"OS" : None,
		"IP_PUB" : "",
		"IP_PRI" : "",
	},
}
```

 