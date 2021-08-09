import psutil
import time
from statistics import median

cpu_percent_0 = psutil.cpu_percent()
virtual_memory_0 = psutil.virtual_memory()[2]
print(cpu_percent_0)
print(virtual_memory_0)
input("press when the execution starts")
cpu_percent = []
virtual_memory = []
while True:
    cpu_percent.append(psutil.cpu_percent() - cpu_percent_0)
    virtual_memory.append(psutil.virtual_memory()[2] - virtual_memory_0)
    print("cpu percent:", median(cpu_percent))
    print("memory percent: ", median(virtual_memory))
    time.sleep(10)
