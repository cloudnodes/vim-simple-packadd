# -*- coding: utf-8 -*-


"""bind: defines the epita fix script."""


import os
import pip
#import sys
import site
import subprocess as sp


def isInstalled():
    with os.scandir(site.USER_SITE) as d:
        for entry in d:
            if 'vim-packadd' in str(entry):
                return True
    return False


def pipInstall(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


def main():
    if not isInstalled():
        print('Reinstalling')
        pipInstall('vim-packadd --user')
    process = sp.Popen(sys.argv, stdout=PIPE)
    #for line in process.stdout.readlines():
    #    print line
    #    sys.stdout.flush()
