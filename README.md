# SWEETMON-client

This project is a python module to interact with '[SWEETMON](https://github.com/sweetchipsw/sweetmon)' project.

Fuzz testers can adapt their fuzzer easily.



## Fast Install & Usage

### Prerequirement

- You should install sweetmon first to use this project. 
- Sweetmon : https://github.com/sweetchipsw/sweetmon



### Installation

1. Install Python3
   - Download python3 at http://python.org/ on Windows
   - ```apt-get install python3``` on Linux.
2. Install Python package
   - ```pip3 install requests```
3. Clone sweetmon-client
   - ```git clone http://github.com/sweetchipsw/sweetmon-client```
4. See example



- ​

##### SWEETMON (Important)

- Please Check the http://github.com/sweetchipsw/sweetmon project.
- You should install sweetmon first.

##### Python Package

You need to install several packages before use sweetmon-client.

- requests
- and
- the
- other


위 모듈들은 아래와 같이 다운로드 할 수 있습니다. (Linux, Mac)

```shell
sudo pip install requests
```

만약 윈도우 사용자라면 아래와 같이 다운로드 할 수 있습니다.

``` powershell
pip.exe install requests
```


### Clone project

You don't have to install using 'setup.py' just download this project.

setup.py를 이용하여 설치하지 않고 clone 후 바로 이용가능합니다.

```shell
git clone http://github.com/sweetchipsw/sweetmon-client
```

## How to use (Linux, Windows, Mac)

1. Please fill the contents in config.py. (Important)

   ```python
   FUZZER_NAME = "" # AWESOMEFUZZER
   FUZZING_TARGET = "" # Weak_application
   BINARY = "" # your_fuzzer
   SERVER_URL = "" # sub.domain.com
   SERVER_PROTOCOL = "https://" # or http://
   ```

2. Run install.py

3. ```shell
   $ python install.py
   [*] Create new Configuration file
   [*] Input password to access SWEETMON..
   Password:
   [*] Success, Your token is : 836a596**********************...
   ```

4. Now you can make your fuzzer. (Please check the example field.)

## Example





## Files

* config.py : Configuration file.
* install.py : Install dependencies and regist fuzzer to the server.
* sweetmon.py : Core script / API
* fuzz.py : Fuzzer script.
* test_testcase.py : Triage slow(or OOM) testcase. 
* triage.py : 

# API

### (Class) Fuzzer

Purpose : Manage and Interact with server

* InitFuzzer() : Gathering fuzzer's information (OS, IP, … ) and send to server.
  * I recommend to use this function when you start fuzzer.
* Ping() : For checking SLA. (Send ping to server)
* Testtestcase() : 
* Upload() : Upload file to the server


* ​


### (Class) Machine

​	Purpose : Manage machine's information

### Information

```json
# YOU CAN MODIFY GLOBAL INFO
GLOBALINFO = {
	"SERVER_URL" : SERVER_URL,
	"SERVER_PROTOCOL" : SERVER_PROTOCOL,
	"TIME_PING" : 60, # Sec (Seconds)
	"TIME_MAXTIME" : 70, # MS (MiliSeconds)
	"MAXMEM" : 70, # MB (For Libfuzzer)
}

# DO NOT MODIFY FUZZERINFO
FUZZERINFO = {
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
```

 