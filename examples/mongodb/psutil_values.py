import psutil
import time
from statistics import median

cpu_percent = []
virtual_memory = []
disk_usage = []
input("press when the execution starts")
while True:
    for proc in psutil.process_iter():
        if "mongod.exe" in proc.name().lower():
            io_counters = proc.io_counters()
            disk_usage.append(io_counters[2] + io_counters[3])
            cpu_percent.append(proc.cpu_percent())
            virtual_memory.append(proc.memory_info().rss)
    print("cpu percent:", median(cpu_percent))
    print("memory usage: ", median(virtual_memory))
    if len(disk_usage) > 2:
        print("disk usage: ", max([x - disk_usage[0] for x in disk_usage[1:]]))
    time.sleep(1)
