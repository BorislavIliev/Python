import os
import sys
import re
import MySQLdb
import string
import random
import getopt
import subprocess

wp_users = dict()
def main(argv):
    cpaneluser = ''
    cms = ''

    def mysql_connection(dbuser, dbpass):
        try:
            db = MySQLdb.connect(host='localhost', user=dbuser, passwd=dbpass)
            db.close()
            return 1
        # Check if connection was successful
        except MySQLdb.Error, e:
            try:
                print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
                return None
            except IndexError:
                print "MySQL Error: %s" % str(e)
                return None
        except TypeError, e:
            print(e)

    def shell_mysql_connection(dbuser, dbpass):
        pass


#    def random_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + '@#?%^&*$!-_)({}[]+<>'):
#        print ''.join(random.choice(chars) for _ in range(1, 15))


    def wp_change_passwords():
        cp_path = os.path.join('/home/', cpaneluser)
        if not os.stat(cp_path):
            print'No such dir.'
        else:
            for root, subFolders, files in os.walk(cp_path):
                wp_files = []
                if 'wp-config.php' in files:
                    print(os.path.join(root, 'wp-config.php'))
                    wp_file_path = os.path.join(root, 'wp-config.php')
                    wp_files.append(wp_file_path)

                for file1 in wp_files:
                    with open(file1, 'r') as wp_file:
                        for line in wp_file:
                            if 'define(\'DB_USER\'' in line:
                                new_line = line.strip('\n')
                                if (re.match('define.*DB_USER.*\'(.*)\'', new_line)):
                                    m = re.match('define.*DB_USER.*\'(.*)\'', new_line)
                                    dbuser = m.groups()[0]
                                    #print'DB_USERNAME: ',dbuser
                            # elif 'define(\'DB_NAME\'' in line:
                            #     new_line = line.strip('\n')
                            #     if (re.match('define.*DB_NAME.*\'(.*)\'', new_line)):
                            #         m = re.match('define.*DB_NAME.*\'(.*)\'', new_line)
                            #         dbname = m.groups()[0]
                            #         print dbname
                            elif 'define(\'DB_PASSWORD\'' in line:
                                new_line = line.strip('\n')
                                if (re.match('define.*DB_PASSWORD.*\'(.*)\'', new_line)):
                                    m = re.match('define.*DB_PASSWORD.*\'(.*)\'', new_line)
                                    dbpass = m.groups()[0]
                                    #print'DB_PASSWORD:',dbpass
                                # print mysql_connection(dbuser, dbuser, dbpass)
                                conn_result = mysql_connection(dbuser, dbpass)
                                if conn_result == 1:
                                    print "Change"
                                    wp_users.update({dbuser: dbpass})
                                else:
                                    pass
                                    #print "No change"
		        print'Found users: \n',wp_users
	return wp_users
    try:
        opts, args = getopt.getopt(argv, "hc:p:", ["cpanel=", "cms="])
    except getopt.GetoptError:
        print 'You are using an invalid option.'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'dbusers.py -c <cpaneluser> -cms <platform>'
            sys.exit()
        elif opt in ("-c", "--cpanel"):
            cpaneluser = arg
        elif opt in ("-p", "--cms"):
            cms = arg
    if cms == 'wordpress':
        print'Wordpress'
        wp_change_passwords()
    print'Cpanel user is ', cpaneluser
    print'CMS type: ', cms
    print'All users: \n',wp_users


if __name__ == "__main__":
    main(sys.argv[1:])

# for root, subFolders, files in os.walk('/home/borislav/'):
#	joomla_files = []
#       	if 'configuration.php' in files:
#               	file_path = os.path.join(root, 'configuration.php')
#		if 'components' not in file_path:
#			print file_path<>
#			joomla_files.append(file_path)	
# for root, subFolders, files in os.walk('/home/borislav/'):
#       	if 'config.php' in files:
#               	print(os.path.join(root, 'config.php'))
