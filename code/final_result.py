# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Objective:Get final result

"""
import math
from datetime import *

file_suffix = '.csv'

def get_result(in_file2):
	in_file2_name = 'E:/KDD-CUP-2017/dataSets/submit/' + in_file2 + file_suffix

	fr = open(in_file2_name,'r')
	result = fr.readlines()
	fr.close()
	return result

def get_final_result(in_file1,result):
	in_file1_name = 'E:/KDD-CUP-2017/dataSets/submit/' + in_file1 + file_suffix
	fr = open(in_file1_name,'r')
	fr.readline()
	infor = fr.readlines()
	fr.close()

	out_file = 'final_result_20170523'
	out_file_name = 'E:/KDD-CUP-2017/dataSets/submit/' + out_file + file_suffix

	fw = open(out_file_name,'w')
	fw.writelines(','.join(['intersection_id','tollgate_id','time_window','avg_travel_time'])+'\n')
	if(len(infor) == len(result)):
		for i in range(len(infor)):
			each_infor = infor[i].replace('"','').strip().split(',')
			intersection_id = each_infor[0]
			tollgate_id = each_infor[1]
			start_time_window = each_infor[2]
			end_time_window = each_infor[3]
			avg_travel_time = result[i]
			out_line = ','.join([intersection_id,tollgate_id,'"['+start_time_window+','+end_time_window+')"',str(avg_travel_time)])
			fw.writelines(out_line)
		fw.close()
	


def main():
	in_file1 = 'submit_20min_avg_travel_time'
	in_file2 = 'result'
	result = get_result(in_file2)
	get_final_result(in_file1,result)


if __name__ == '__main__':
    main()