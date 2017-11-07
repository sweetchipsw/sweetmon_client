from config import *
from sweetmon import *
import uuid

# Test PING
print("START TEST / LOAD CONFIG")

F = Fuzzer()
# print("TEST AUTO PING", F.RunPingThread())
print("TEST PING", F.Ping())
print("TEST UPLOAD", F.Upload("test", "here\nis_l0g", "/etc/hostconfig"))
print("END OF TEST..")
