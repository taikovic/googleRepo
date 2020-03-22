#!/usr/bin/env python3
import re

def rearrange_name(name):
	# full words use of: \b....\b
	result = re.search(r"^([\w .]*), ([\w .]*)$", name)
	#print(result.groups())
	if result == None:
		return name
	return "{} {}".format(result[2],result[1])

