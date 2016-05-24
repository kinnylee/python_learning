#!/usr/bin/env python

import json
import os
from collections import defaultdict
from collections import Counter
from pandas import DataFrame, Series

#parser json file to records
def paser_json_file(path):
	if not os.path.exists(path):		
		return []
	else:
		records = [json.loads(line) for line in open(path)]
		return records

#get time_zone
def get_timezone(records):
	return [rec['tz'] for rec in records if 'tz' in rec]

#counter
def get_counts(sequence):
	counts = {} 
	for x in sequence:
		if x in counts:
			counts[x] += 1;
		else:
			counts[x] = 1;
	return counts

def get_counts2(sequence):
	counts = defaultdict(int) # all 0
	for x in sequence:
		counts[x] += 1
	return counts

def top_counts(count_dict, n = 10):
	value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
	value_key_pairs.sort()
	return value_key_pairs[-n:]

path = '../data/data.txt'
records =  paser_json_file(path)
time_zones = get_timezone(records)
#print time_zones
counts = get_counts2(time_zones)
print '---total:', len(counts), '-----'
#print counts

#print top_counts(counts)

print Counter(time_zones)

#frame = DataFrame(records)
#print frame
