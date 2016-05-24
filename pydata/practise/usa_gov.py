#!/usr/bin/env python

import json
import os

def paser_json_file(path):
	if not os.path.exists(path):		
		return []
	else:
		records = [json.loads(line) for line in open(path)]
		return records

path = '../data/data.txt'
records =  paser_json_file(path)
print records[0]['tz']


