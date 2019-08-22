# Raspberry-Pi-DHT-11-logger
Python script that logs temperature and humidity from a DHT 11

Functions in this script:
make_filename - creates the log filenames
check_if_temp_file_exists - checks if the filename created exists, if not, the file is created
read_sensor - this function reads the dht1 sensor
save_sensor - function taht saves the temp and humidity
make_s1_temp_diagram - uses matlab to make a bar graph
upload_files - this function copies the graphfiles with scp.

You'll need to make yourself an id_rsa.pub key and upload it the the remote server, in order to get scp to work without asking for password.
