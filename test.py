from config import *
from sweetmon import *
import uuid

# Test PING
print("START TEST / LOAD CONFIG")

F = Fuzzer(FUZZERINFO)

print("TEST PING", F.Ping())
print("TEST UPLOAD", F.Upload(uuid.uuid1(), "here\nis_l0g", "/etc/passwd"))
print("END OF TEST..")
