import os
import sys
import re
import MySQLdb
import string
import random
import getopt
import subprocess
import itertools
import json


def main(argv):
    cpaneluser = ''
    cms = ''
    mysql = ''
    wp_users = dict()
    softa = ''
    mode = ''
    source = ''

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

    drupalDefaultFiles = (
    'authorize.php',
    'cgi-bin',
    'CHANGELOG.txt',
    'COPYRIGHT.txt',
    'cron.php',
    '.editorconfig',
    '.gitignore',
    '.htaccess',
    'includes',
    'index.php',
    'INSTALL.mysql.txt',
    'INSTALL.pgsql.txt',
    'INSTALL.sqlite.txt',
    'INSTALL.txt',
    'LICENSE.txt',
    'MAINTAINERS.txt',
    'misc',
    'modules',
    'profiles',
    'README.txt',
    'robots.txt',
    'scripts',
    'sites',
    'themes',
    'update.php',
    'UPGRADE.txt',
    'web.config',
    'xmlrpc.php',
    )

    def mysql_connection(dbuser, dbpass):
        try:
            db = MySQLdb.connect(host='localhost', user=dbuser, passwd=dbpass)
            db.close()
            print 'Sucessful Connection!'
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

    def whpapiChangePass(usr, password):
        cmd = 'whmapi1 set_mysql_password user={0} password=\'{1}\' cpuser={2}'.format(usr, password, cpaneluser)
        print cmd
        subprocess.call(cmd, shell=True)


    def random_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + '@#?%^&*$!-_)([]'):
        passwd = ''.join(random.choice(chars) for _ in range(1, 15))
        return passwd

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
        usersList = []
        if not source == '':
            cp_path = os.path.join('/home/', cpaneluser)
            mysqlUsersFile = os.path.join(cp_path, 'mysqlusers.txt')
            if not os.stat(cp_path):
                print('No such dir.')
            else:
                with open(mysqlUsersFile, 'r') as usersFile:
                    for line in usersFile:
                        newLine = line.strip('\n')
                        usersList.append(newLine)
        userDirs = []
        userUrls = []
        softaFile = ('/home/{0}/.softaculous/installations.php'.format(cpaneluser))
        with open(softaFile, 'r') as softaculousFile:
            softInstalls = softaculousFile.read().replace("\n", '')
            m = re.match('^[\'"]?(?:\/[^\/]+)*[\'"]?$', softInstalls)
            split_arr = re.split(": |\"", softInstalls)
            for n in split_arr:
                if re.match('^\;[a-z]\:[0-9]+\:$', n):
                    split_arr.remove(n)
                elif re.match('^.[a-z]', n):
                    split_arr.remove(n)
            for i in split_arr:
                if re.match('^[\'"]?(?:\/[^\/]+)*[\'"]?$', i):
                    m = re.match('^[\'"]?(?:\/[^\/]+)*[\'"]?$', i)
                    userDirs.append(m.group())
                if re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', i):
                    n = re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', i)
                    userUrls.append(n.group())
            # for k,j in itertools.izip(userDirs, userUrls):
            #     dirFiles = os.listdir(k)
            #     if 'wp-config.php' in dirFiles:
            #         print '{0} - Wordpress !'.format(j)
            #     if (set(dirFiles).intersection(drupalDefaultFiles)) == 31:
            #         print '{0} - Drupal !'.format(j)
            indicesUsers = [i for i, x in enumerate(split_arr) if x == "softdbuser"]
            usersArr = []
            dbsArr = []
            passwordsArr = []
            for k in indicesUsers:
                if cpaneluser in split_arr[k + 1]:
                    usersArr.append(split_arr[k + 1])
                elif cpaneluser in split_arr[k + 2]:
                    usersArr.append(split_arr[k + 2])
                else:
                    print'Can\'t find such user'
            indicesDbs = [i for i, x in enumerate(split_arr) if x == "softdb"]
            for k in indicesDbs:
                dbsArr.append(split_arr[k + 1])
            indicesPasswords = [i for i, x in enumerate(split_arr) if x == "softdbpass"]
            for k in indicesPasswords:
                passwordsArr.append(split_arr[k + 1])
            dbCollection = dict()
            for i, m, n in zip(dbsArr, usersArr, passwordsArr):
                if not source == '':
                    if usersList and i in usersList:
                        dbCollection.update({i: {'dbuser': m, 'dbpass': n}})
                        print dbCollection
                else:
                    dbCollection.update({i: {'dbuser': m, 'dbpass': n}})
            print dbCollection
            jsondb = json.dumps(dbCollection)
            print jsondb
            for keys, values in dbCollection.iteritems():
                if mysql == 'change':
                    if mysql_connection(values['dbuser'], values['dbpass']):
                            whpapiChangePass(values['dbuser'], values['dbpass'])
                            print values['dbuser'], '-', values['dbpass']
                else:
                    print 'Done. Not changing passwords.'


    def phponly():
        usersList = []
        foundUsers = []
        cp_path = os.path.join('/home/', cpaneluser)
        mysqlUsersFile = os.path.join(cp_path, 'mysqlusers.txt')
        exclude_prefixes = ['.softaculous', 'www', '.trash']
        if not os.stat(cp_path):
            print('No such dir.')
        else:
            with open(mysqlUsersFile, 'r') as usersFile:
                for line in usersFile:
                    newLine = line.strip('\n')
                    usersList.append(newLine)
            for root, subFolders, files in os.walk(cp_path):
                subFolders[:] = [d for d in subFolders if d not in exclude_prefixes]
                for file in files:
                    if file.endswith('.php') or file.endswith('.yml'):
                        phpfilepath = os.path.join(root, file)
                        with open(phpfilepath, 'r') as phpfile:
                            for line in phpfile:
                                new_line = line.strip('\n')
                                for i in usersList:
                                    if i in new_line:
                                        fpath = os.path.join(root, file)
                                        print fpath, '<->', line,
                                        foundUsers.append(i)
        notFound = list(set(usersList) - set(foundUsers))
        print'Users not found:', notFound
        newPass = random_generator()
        for i in notFound:
            whpapiChangePass(i, newPass)
            print i, '-', newPass


    try:
        opts, args = getopt.getopt(argv, "hc:p:m:s:f:i", ["cpanel=", "cms=", "mysql=", "softaculous=", "files=", "input="])
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
        elif opt in ("-f", "--files"):
            mode = arg
        elif opt in ("-i", "--input"):
            source = arg
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
    if mode == 'php':
        phponly()
    print'Cpanel user is ', cpaneluser
    print'CMS type: ', cms


if __name__ == "__main__":
    main(sys.argv[1:])
