# SWEETMON-client

An client for ```sweetmon``` project based on python.

The sweetmon is an fuzzer monitoring system based on python+django+apache2.

## Installation

### Dependency

##### SWEETMON

Please Check the http://github.com/sweetchipsw/sweetmon project.

You should install sweetmon first.

##### Python Package

You need to install several packages before use sweetmon-client

- requests



### Clone project

You don't have to install using setup.py. just download this project.

```shell
git clone http://github.com/sweetchipsw/sweetmon-client
```

## Files

* config.py : Configuration file.
* install.py : Install dependencies and regist to the fuzzer.
* sweetmon.py : Core script / API
* fuzz.py : Fuzzer script.
* test_testcase.py : Triage slow(or OOM) testcase. 
* triage.py : 

# API

### (Class) Fuzzer

* InitFuzzer() : Gathering fuzzer's information (OS, IP, … ) and send to server.
  * I recommend to use this function when you start fuzzer.
* Ping() : For checking SLA. (Send ping to server)
* Testtestcase() : 
* Upload() : Upload file to the server


* ​

