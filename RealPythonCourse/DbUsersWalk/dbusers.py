import os
import sys
import fnmatch
import glob
from os import walk
import re

for root, subFolders, files in os.walk('/home/borislav/'):
	wp_files = []
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
						print m.groups()[0]
										
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
