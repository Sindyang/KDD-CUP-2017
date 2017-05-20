# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Objective:Format

"""

# import necessary modules
import math
from datetime import *

file_suffix = '.csv'
def format(in_file):
	#step 1: read data
	out_file = 'testing_phase1_final_format'
	in_file_name = 'E:/KDD-CUP-2017/dataSets/testing_phase1/'+in_file+file_suffix
	out_file_name = 'E:/KDD-CUP-2017/dataSets/testing_phase1/' + out_file +file_suffix
	fr = open(in_file_name,'r')
	fr.readline()
	data = fr.readlines()
	fr.close()

	#step 2: format
	fw = open(out_file_name,'w')
	for i in range(len(data)):
		each_data = data[i].replace('"','').strip().split(',')
		avg_travel_time = each_data[-1]

		intersection_id = each_data[0]
		if intersection_id == 'A':
			intersection_id = '0'
		elif intersection_id == 'B':
			intersection_id = '1'
		elif intersection_id == 'C':
			intersection_id = '2'

		start_time_window = each_data[2]
		start_time_window = datetime.strptime(start_time_window, "%Y-%m-%d %H:%M:%S")
		start_time = 60 * start_time_window.hour + start_time_window.minute

		end_time_window = each_data[3]
		end_time_window = datetime.strptime(end_time_window, "%Y-%m-%d %H:%M:%S")
		end_time = 60 * end_time_window.hour + end_time_window.minute

		outline = avg_travel_time +' '+' '.join(['0'+':'+intersection_id,'1'+':'+each_data[1],'2'+':'+str(start_time),'3'+':'+str(end_time),'4'+':'+each_data[4],
			'5'+':'+each_data[5],'6'+':'+each_data[6],'7'+':'+each_data[7],'8'+':'+each_data[8],'9'+':'+each_data[9],'10'+':'+each_data[10]])+'\n'
		fw.writelines(outline)
	fw.close()


def main():
	in_file = 'testing_20min_avg_travel_time_weather'
	format(in_file)

if __name__ == '__main__':
    main()