import os
import sys
import re

usersList = [
'pipi_adsn1',
'pipi_adsn2',
'pipi_adsn3',
'pipi_adsn4',
'pipi_bezplat',
'pipi_bgmobile',
'pipi_blog',
'pipi_dir',
'pipi_flux',
'pipi_gllr1',
'pipi_gllr2',
'pipi_imga1',
'pipi_jo151',
'pipi_joom1',
'pipi_mamb1',
'pipi_master',
'pipi_mobio',
'pipi_mvmimoti',
'pipi_pesho',
'pipi_phpb1',
'pipi_phpb2',
'pipi_pipi',
'pipi_sait',
'pipi_script',
'pipi_sport',
'pipi_wrdp6'
]

cpaneluser = 'borislav'

def searchphp():
    cp_path = os.path.join('/home/', cpaneluser)
    if not os.stat(cp_path):
        print'No such dir.'
    else:
        for root, subFolders, files in os.walk(cp_path):
            for file in files:
                if file.endswith('.php'):
                    phpfilepath = os.path.join(root, file)
                    with open(phpfilepath, 'r'):
                        for line in file:
                            for i in usersList:
                                if i in line:
                                    print line
                                    fpath = os.path.join(root, file)
                                    print fpath


