#!/usr/bin/env python3

import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    df = du.free/du.total * 100
    return df > 20

def check_cpu_usage(time):
    cu=psutil.cpu_percent(time)
    return cu < 75

if not check_disk_usage("/") and not check_cpu_usage(1):
    print("ERROR!")
else:
    print("Everything is OK!")
    
