#!/usr/bin/python3

# IMPORTS
import Adafruit_DHT
import time
import requests
import os
from datetime import datetime

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

# SOME GLOBAL DEFINITIONS AND VARAIBLES
local_path 	= '/home/pi/Python/DHT-11/diagram/'
remote_path = '/var/www/html/fortuna/diagram'
remote_user = 'pi'
remote_host = 'nerdegutta.org'

# In order do make the scp command in the upload functions to work,
# you need to run "ssh-keygen -t rsa"
# This makes two files in the ~/.ssh/ dir
# id_rsa and id_rsa.pub
# The id_rsa.pub key needs to be copied to the server you want to log on to
# without using password. You'll need to rename it to "authorized_keys" as well

# FUNCTIONS
# This function reads the sensor that is connected to pin9/ GPIO 4
def read_sensor_1():
	global humid_0
	global temp_0
	humid_0, temp_0 = Adafruit_DHT.read_retry(11,4)
	time.sleep(2)

# This functions makes the filname of the log file
def make_filename():
	global sensor1_t_filename
	global sensor1_h_filename
	global minute
	global hour
	global date
	global dom
	global month
	now = datetime.now()
	minute = now.strftime('%M')	
	hour = now.strftime('%H')
	date = now.strftime('%d')
	dom = now.strftime('%A')
	month = now.strftime('%B')
	s1t_filename = now.strftime('%d-%m-%y')
	s1h_filename = now.strftime('%d-%m-%y')
	sensor1_t_filename = 's1t-'+s1t_filename
	sensor1_h_filename = 's1h-'+s1h_filename

# This function saves the temperature from Sensor 1
def save_sensor1_t():	
	log_file = open(local_path+sensor1_t_filename+'.txt', 'a')	
	log_file.write(hour)
	log_file.write(',{0:0.0f}\n'.format(temp_0))
	log_file.close()

# This function saves the humidity from Sensor 1
def save_sensor1_h():	
	log_file = open(local_path+sensor1_h_filename+'.txt', 'a')	
	log_file.write(hour)
	log_file.write(',{0:0.0f}\n'.format(humid_0))
	log_file.close()

# This dunction makes the temperature diagram
def make_s1_temp_diagram():
	x, y = np.loadtxt(local_path + sensor1_t_filename+'.txt',
		unpack = True,
		delimiter = ',')
	plt.bar(x,y, color='g', align='center')
	plt.title('Temperature '+dom+' '+date+'. '+month)
	plt.ylabel('Temperature')
	plt.xlabel('Hour')
	plt.savefig(local_path + sensor1_t_filename+'.png')

# This function makes the humidity diagram
def make_s1_humid_diagram():
	x, y = np.loadtxt(local_path + sensor1_h_filename+'.txt',
		unpack = True,
		delimiter = ',')
	plt.bar(x,y, color='r', align='center')
	plt.title('Humidity '+dom+' '+date+'. '+month)
	plt.ylabel('Humidity')
	plt.xlabel('Hour')
	plt.savefig(local_path + sensor1_h_filename+'.png')	

# This function uploads both diagrams
def upload_files():
	print ('Upload')
	temp_path = local_path + sensor1_t_filename + '.png'	
	output = os.popen("scp %s %s@%s:%s" % (temp_path,remote_user,remote_host,remote_path))
	temp_path = local_path + sensor1_h_filename + '.png'	
	output = os.popen("scp %s %s@%s:%s" % (temp_path,remote_user,remote_host,remote_path))	
	print ('Done upload')

# This function checks if the temperature file exists
def check_if_temp_file_exists():
	check_file = local_path+sensor1_t_filename+'.txt'
	print (check_file)
	try:
		f = open(check_file)
		f.close()
		print ('File found.')
	except FileNotFoundError:
		print('File not found. Let\'s make it.')
		temp_file = open(check_file, 'w')

# This function checks if the humidity file exists
def check_if_humid_file_exists():
	check_file = local_path+sensor1_h_filename+'.txt'
	print (check_file)
	try:
		f = open(check_file)
		f.close()
		print ('File found.')
	except FileNotFoundError:
		print('File not found. Let\'s make it.')
		temp_file = open(check_file, 'w')		

# This is the main function	
def main():
	make_filename()
	check_if_temp_file_exists()
	check_if_humid_file_exists()

	read_sensor_1()	
	print ('Sensor 0: Temp={0:0.0f}*C Humidity={1:0.0f}%'.format(temp_0, humid_0))
	print (sensor1_t_filename)
	print (sensor1_h_filename)
	save_sensor1_t()
	save_sensor1_h()
	make_s1_temp_diagram()
	make_s1_humid_diagram()
	upload_files()

# By adding this, the entire file can be used as a module
if __name__ == "__main__":
	main()

# If these lines are uncommented the program can 	
#	while True:
#		if counter < 1800:
#			counter += 1;
#			time.sleep(1)
#			print (counter)
#		else:
#			main()
#			counter = 0
	#	time.sleep(300)

