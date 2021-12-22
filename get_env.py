from platform import uname
from json import dumps

try:
  from psutil import cpu_freq, cpu_count, virtual_memory
except:
  raise Exception("\x1b[1;31mpsutil isn't installed yet. You should be able to run \"pip3 install psutil\" to install it.\x1b[0m")

def main():
  u_name = uname()
  cpu = cpu_freq()
  cores = cpu_count()
  mem = virtual_memory()

  environment = {'cores':cores,'os':u_name.system,'os_release':u_name.release,'os_version':u_name.version,'machine':u_name.machine,'processor':u_name.processor,'cpu_freq':cpu.current,'memory':mem.total}

  with open('env_info.json','w') as env_file:
    env_file.write(dumps(environment))

if __name__ == '__main__':
  main()