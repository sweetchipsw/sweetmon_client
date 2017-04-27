from config import *
from sweetmon import *
import uuid
# Test PING
F = Fuzzer(FUZZERINFO)
print F.Ping()

print F.Upload(uuid.uuid1(), "here\nis_l0g", "/etc/passwd")
