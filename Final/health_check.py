#!/usr/bin/env python3
import shutil
import psutil
import emails
import os
import socket


user = os.environ.get('USER')

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    df = du.free/du.total * 100
    return df > 20
def check_cpu_usage(time):
    cu=psutil.cpu_percent(time)
    return cu < 80
def check_memory_usage():
    mu=round(psutil.virtual_memory().available/1024/1024)
    return mu > 500
def check_localhost_resolution():
    return socket.gethostbyname('localhost') == '127.0.0.1'




if __name__ == "__main__":
    if not check_cpu_usage(1):
        subject_line = "Error - CPU usage is over 80%"
    elif not check_disk_usage("/"):
        subject_line = "Error - Available disk space is less than 20%"
    elif not check_memory_usage():
        subject_line = "Error - Available memory is less than 500MB"
    elif not check_resolve_hostname():
        subject_line = "Error - localhost cannot be resolved to 127.0.0.1"

    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_error_report("automation@example.com", "{}@example.com".format(user), subject_line,body)
    emails.send_email(message)
