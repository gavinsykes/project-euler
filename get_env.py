import platform
import json

try:
  import psutil
except:
  raise Exception("\x1b[1;31mpsutil isn't installed yet. You should be able to run \"pip3 install psutil\" to install it.\x1b[0m")

uname = platform.uname()
cpu = psutil.cpu_freq()
cores = psutil.cpu_count()
mem = psutil.virtual_memory()

environment = {'os':uname.system,'os_release':uname.release,'os_version':uname.version,'machine':uname.machine,'processor':uname.processor,'cpu_freq':cpu.current,'memory':mem.total}

with open('env_info.json','w') as env_file:
  env_file.write(json.dumps(environment))