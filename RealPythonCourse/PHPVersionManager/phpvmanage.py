import os
import csv

# print(os.curdir)
# print(os.listdir("."))
# cwd = os.getcwd()
# print(cwd)
# os.chdir("/Applications/MAMP/htdocs/Python/")
# cwd = os.getcwd()
# print(cwd)
# print(os.stat("/Applications/MAMP/htdocs/Python/"))


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

htaccess_exist()
check_version()
cache_reader()
