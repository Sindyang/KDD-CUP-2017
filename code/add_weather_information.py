# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Objective:
Add weather information

"""

# import necessary modules
import math
from datetime import *

file_suffix = '.csv'

def set_Weather_Information(in_file_weather):
	in_file_name = 'E:/KDD-CUP-2017/dataSet_phase2/'+ in_file_weather + file_suffix
	#step 1:读入天气信息
	fr = open(in_file_name,'r')
	fr.readline()
	weather_data = fr.readlines()
	fr.close()

	#step 2: process information
	weather_information = {}
	for i in range(len(weather_data)):
		each_weather = weather_data[i].replace('"','').strip().split(',')
		date = each_weather[0]
		if date not in weather_information:
			weather_information[date] = {}

		hour = each_weather[1]
		pressure = each_weather[2]
		sea_pressure = each_weather[3]
		wind_direction = each_weather[4]
		wind_speed = each_weather[5]
		temperature = each_weather[6]
		rel_humidity = each_weather[7]
		precipitation = each_weather[8]

		if hour not in weather_information[date].keys():
			weather_information[date][hour] = [pressure,sea_pressure,wind_direction,wind_speed,temperature,rel_humidity,precipitation]
	return weather_information

def add_Weather_Information(in_file_travel_time, weather_information):

	in_file_name = 'E:/KDD-CUP-2017/dataSet_phase2/'+ in_file_travel_time + file_suffix
	out_file = 'submit_20min_avg_travel_time_weather'
	out_file_name = 'E:/KDD-CUP-2017/dataSet_phase2/' + out_file + file_suffix
	#step 1: 读入时间信息
	fr = open(in_file_name, 'r')
	fr.readline()
	traj_data = fr.readlines()
	fr.close()

	#step 2:add weather information and print
	fw = open(out_file_name,'w')
	fw.writelines(','.join(['intersection_id','tollgate_id','week','time_window','pressure','sea_pressure','wind_direction','wind_speed','temperature','rel_humidity','precipitation','avg_travel_time'])+'\n')
	for i in range(len(traj_data)):
		each_infor = traj_data[i].replace('"','').strip().split(',')
		intersection_id = each_infor[0]
		tollgate_id = each_infor[1]
		start_time_window = each_infor[2]
		end_time_window = each_infor[3]
		start_time_window = datetime.strptime(start_time_window,'%Y-%m-%d %H:%M:%S')
		today = date(start_time_window.year, start_time_window.month, start_time_window.day)
		week = today.weekday()
		hour = start_time_window.hour
		hour = int(math.floor(hour / 3) * 3)

		#得到天气信息
		if str(today) in weather_information.keys():
			hours = weather_information[str(today)].keys()
			if str(hour) in hours:
				wea_list = list(weather_information[str(today)][str(hour)])
				pressure = wea_list[0]
		        sea_pressure = wea_list[1]
		        wind_direction = wea_list[2]
		        wind_speed = wea_list[3]
		        temperature = wea_list[4]
		        rel_humidity = wea_list[5]
		        precipitation = wea_list[6]

		avg_travel_time = each_infor[-1]
		out_line = ','.join(['"' + intersection_id + '"','"'+tollgate_id+'"','"'+str(week)+'"','"'+str(start_time_window)+','+str(end_time_window)+'"','"'+pressure+'"','"'+sea_pressure+'"','"'+wind_direction+'"','"'+wind_speed+'"','"'+temperature+'"','"'+rel_humidity+'"','"'+str(precipitation)+'"','"'+str(avg_travel_time)+'"'])+'\n'
		fw.writelines(out_line)
	fw.close()


def main():
    in_file_weather = 'weather (table 7)_2'
    in_file_travel_time = 'submit_20min_avg_travel_time'
    weather_information = set_Weather_Information(in_file_weather)
    add_Weather_Information(in_file_travel_time, weather_information)

if __name__ == '__main__':
    main()