import os
import sys
import fnmatch
import glob
from os import walk
import re
import MySQLdb

def mysql_connection(dbuser, dbname, dbpass):
	db = MySQLdb.connect(host = 'localhost', user = dbuser, passwd = dbpass, db = dbname)

# Check if connection was successful
	if (db):
    # Carry out normal procedure
		#print "Connection successful"
  		return 1
	else:
    # Terminate
    		#print "Connection unsuccessful"
		return 0

for root, subFolders, files in os.walk('/home/borislav/'):
	wp_files = []
	wp_users = dict()
	if 'wp-config.php' in files:
		print(os.path.join(root, 'wp-config.php'))
		wp_file_path = os.path.join(root, 'wp-config.php')
		wp_files.append(wp_file_path)
	
	for file in wp_files:
		with open(file, 'r') as wp_file:
			for line in wp_file:
				if 'define(\'DB_USER\'' in line:
					new_line = line.strip('\n')
                                        if(re.match('define.*DB_USER.*\'(.*)\'', new_line)):
                                                m = re.match('define.*DB_USER.*\'(.*)\'', new_line)
                                                dbuser = m.groups()[0]
						print dbuser
				elif 'define(\'DB_NAME\'' in line:
                                        new_line = line.strip('\n')
                                        if(re.match('define.*DB_NAME.*\'(.*)\'', new_line)):
                                                m = re.match('define.*DB_NAME.*\'(.*)\'', new_line)
                                                dbname = m.groups()[0]
						print dbname
				elif 'define(\'DB_PASSWORD\'' in line:
                                        new_line = line.strip('\n')
                                        if(re.match('define.*DB_PASSWORD.*\'(.*)\'', new_line)):
                                                m = re.match('define.*DB_PASSWORD.*\'(.*)\'', new_line)
                                                dbpass = m.groups()[0]
						print dbpass
#					print mysql_connection(dbuser, dbuser, dbpass)
					conn_result = mysql_connection(dbuser, dbuser, dbpass)
					if conn_result == 1:
						print "Change"
					else:
						print "No change"

#for root, subFolders, files in os.walk('/home/borislav/'):
#	joomla_files = []
#       	if 'configuration.php' in files:
#               	file_path = os.path.join(root, 'configuration.php')
#		if 'components' not in file_path:
#			print file_path
#			joomla_files.append(file_path)	
#for root, subFolders, files in os.walk('/home/borislav/'):
#       	if 'config.php' in files:
#               	print(os.path.join(root, 'config.php'))
