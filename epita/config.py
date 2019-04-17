# -*- coding: utf-8 -*-


"""epita.config: provides packadd install configurations."""


import os
import site
import platform


class Colors:
    HEADER = '\033[95m'
    INFO = '\033[94m'
    OK = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[31m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Paths:
    BASHFILE = ('.bash_profile', '.bashrc')[platform.system() == 'Linux']
    BASHRC = os.environ['HOME'] + '/' + BASHFILE
    PATCH = os.environ['HOME'] + '/afs/.pip/packadd-fix.sh'
    PIP = os.environ['HOME'] + '/afs/.pip'
    VIM = os.environ['HOME'] + '/.vim'
    START = os.environ['HOME'] + '/.vim/pack/packadd/start/'
    OPT = os.environ['HOME'] + '/.vim/pack/packadd/opt/'


class Aliases:
    COMMENT = '\n# Setup for Vim Packadd, do not remove\n'
    LINKSCRIPT = "alias packadd='/bin/sh ~/afs/.pip/packadd-fix.sh'"
    PATH_TO_BIN = site.USER_BASE + '/bin'
    PY_BIN = 'export PY_BIN=$(' + PATH_TO_BIN + ')'
    PATH = "export PATH=$PY_BIN:$PATH"
    FULL = COMMENT + LINKSCRIPT + '\n' + PY_BIN + '\n' + PATH + '\n'
