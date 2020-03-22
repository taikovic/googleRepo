#!/usr/bin/env python3

import sys
import re
import os


def error_search(log_file):
	error = input("what is the error? ")
	returned_errors=[]
	with open(log_file,'r',encoding='UTF-8')as file:
		for log in file.readlines():
			error_patterns=["error"]
			for i in range(len(error.split(' '))):
				error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
			if all(re.search(error_pattern,log.lower()) for error_pattern in error_patterns ):
				returned_errors.append(log)
		file.close()
	return returned_errors

log_file='/home/taikovic/work/Prog/Learning/Learn_python/Python_courses/Google_Certif/Data/fishy.log'
returned_errors=error_search(log_file)
print(returned_errors)
