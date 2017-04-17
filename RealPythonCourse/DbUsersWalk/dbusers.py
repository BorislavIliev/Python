import os
import sys
import re
import MySQLdb
import string
import random
import getopt
import subprocess
import itertools


def main(argv):
    cpaneluser = ''
    cms = ''
    mysql = ''
    wp_users = dict()
    softa = ''

    wpDefaultFiles = (
    'index.php',
    'license.txt',
    'readme.html',
	'wp-activate.php',
	'wp-app.php',
	'wp-blog-header.php',
	'wp-comments-post.php',
	'wp-config-sample.php',
    'wp-config.php',
	'wp-cron.php',
	'wp-links-opml.php',
	'wp-load.php',
	'wp-login.php',
	'wp-mail.php',
	'wp-pass.php',
	'wp-register.php',
	'wp-settings.php',
	'wp-signup.php',
	'wp-trackback.php',
	'xmlrpc.php',
                          )

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

    def shell_mysql_connection():
        for key, value in wp_users.iteritems():
            cmd = 'whmapi1 set_mysql_password user={0} password=\'{1}\' cpuser={2}'.format(key, value, cpaneluser)
            subprocess.call(cmd, shell=True)

    def random_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + '@#?%^&*$!-_)({}[]+<>'):
        print ''.join(random.choice(chars) for _ in range(1, 15))

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
                                    print'DB_USERNAME: ', dbuser
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
                                    print'DB_PASSWORD:', dbpass
                                # print mysql_connection(dbuser, dbuser, dbpass)
                                conn_result = mysql_connection(dbuser, dbpass)
                                if conn_result == 1:
                                    # print "Change"
                                    wp_users.update({dbuser: dbpass})
                                else:
                                    pass
                                    # print "No change"
                                    # print'Found users: \n',wp_users
        return wp_users

    def jooma_change_passwords():
        cp_path = os.path.join('/home/', cpaneluser)
        for root, subFolders, files in os.walk(cp_path):
            joomla_files = []
            if 'configuration.php' in files:
                file_path = os.path.join(root, 'configuration.php')
                if 'components' not in file_path:
                    print file_path
                    joomla_files.append(file_path)

    def softaculous():
        userDirs = []
        userUrls = []
        softaFile = ('/home/{0}/.softaculous/installations.php'.format(cpaneluser))
        with open(softaFile, 'r') as softaculousFile:
            softInstalls = softaculousFile.read().replace("\n", '')
            m = re.match('^[\'"]?(?:\/[^\/]+)*[\'"]?$', softInstalls)
            split_arr = re.split(": |\"", softInstalls)
            for i in split_arr:
                if re.match('^[\'"]?(?:\/[^\/]+)*[\'"]?$', i):
                    m = re.match('^[\'"]?(?:\/[^\/]+)*[\'"]?$', i)
                    print m.group()
                    userDirs.append(m.group())
                if re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', i):
                    n = re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', i)
                    userUrls.append(m.group())
                    print n.group()
            for n in userDirs, userUrls:
                print userDirs[n], ":", userUrls[n]
                # dirFiles = os.listdir(userDirs[n])
                # if 'wp-config.php' in dirFiles:
                #     print '{0} - Wordpress'.format(userUrls[n])



    try:
        opts, args = getopt.getopt(argv, "hc:p:m:s:", ["cpanel=", "cms=", "mysql=", "softaculous="])
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
        elif opt in ("-m", "--mysql"):
            mysql = arg
        elif opt in ("-s", "--softaculous"):
            softa = arg
    if cms == 'wordpress':
        print'Wordpress'
        wp_change_passwords()
        print'All users: \n', wp_users
    if cms == 'joomla':
        print'Joomla'
        jooma_change_passwords()
    if mysql == 'change':
        shell_mysql_connection()
    if softa == 'read':
        softaculous()
    print'Cpanel user is ', cpaneluser
    print'CMS type: ', cms


if __name__ == "__main__":
    main(sys.argv[1:])
