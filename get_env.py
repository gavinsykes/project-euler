import platform
try:
    import psutil
except:
    raise Exception("\x1b[1;31mpsutil isn't installed yet. You should be able to run \"pip3 install psutil\" to install it.\x1b[0m")

import json

uname = platform.uname()
cpu = psutil.cpu_freq()
mem = psutil.virtual_memory()

environment = {'os':uname.system,'os_release':uname.release,'os_version':uname.version,'machine':uname.machine,'processor':uname.processor,'cpu_freq':cpu.current,'memory':mem.total}

f = open('env_info.json','w')
if f.mode == 'w':
    f.write(json.dumps(environment))
    f.close()