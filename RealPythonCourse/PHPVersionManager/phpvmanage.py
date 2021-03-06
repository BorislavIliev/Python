import os
import sys
import getopt


# print(os.curdir)
# print(os.listdir("."))
# cwd = os.getcwd()
# print(cwd)
# os.chdir("/Applications/MAMP/htdocs/Python/")
# cwd = os.getcwd()
# print(cwd)
# print(os.stat("/Applications/MAMP/htdocs/Python/"))
def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print 'No such option. Please use: test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print'Input file is ', inputfile
    print'Output file is ', outputfile


if __name__ == "__main__":
    main(sys.argv[1:])


def fn1():
    print 'fn1 selected'


def fn2():
    print 'fn2 selected'


php_versions = {
    "x-httpd-php52": 5.2,
    "x-httpd-php53": 5.3,
    "x-httpd-php54": 5.4,
    "x-httpd-php55": 5.5,
    "x-httpd-php56": 5.6,
    "x-httpd-php70": 7.0,
    "x-httpd-php71": 7.0,
}


def htaccess_exist():
    files = os.listdir(".")
    if ".htaccess" in files:
        print(".htaccess exists !")
    else:
        file = open('.htaccess', 'w+')
        file.close()


def check_version():
    words = ['AddHandler']
    with open('.htaccess', 'r') as ht_file:
        array = []
        for line in ht_file:
            array.append(line.strip('\n'))
        print(array)
        php_ver = array[0][23:36]
        if php_ver in php_versions:
            print(php_versions[php_ver])
        ht_file.close()


def cache_reader():
    with open('cpane-cache', 'r') as cachefile:
        for line in cachefile:
            line_arr = line.split()
            if "espressapp.link:" in line.split():
                line_arr2 = line_arr[1].split("==")
                print(line_arr2)
                doc_root = line_arr2[4]
                print("The Doc_Root is {}:", doc_root+"/")
                try:
                    os.stat(doc_root)
                except OSError:
                    print("Directory does not exist!")
        # cachefile.close()


#htaccess_exist()
#check_version()
#cache_reader()
