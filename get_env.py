import platform
import psutil

import json

uname = platform.uname()
cpu = psutil.cpu_freq()
mem = psutil.virtual_memory()

environment = {'os':uname.system,'os_release':uname.release,'os_version':uname.version,'machine':uname.machine,'processor':uname.processor,'cpu_freq':cpu.current,'memory':mem.total}

f = open('env_info.json','w')
if f.mode == 'w':
    f.write(json.dumps(environment))
    f.close()