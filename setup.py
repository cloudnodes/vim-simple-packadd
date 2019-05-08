# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from epita.command import epita_install


version = re.search(
        '^__version__\s*=\s*"(.*)"',
        open('packadd/packadd.py').read(),
        re.M
    ).group(1)


with open('README.md', "r") as fh:
    long_description = fh.read()


setup(
    name = 'vim-packadd',
    version = version,
    author = 'Antoine Dray',
    author_email = 'antoine.dray@epita.fr',
    description = 'Package manager for Vim8.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/antoinedray/vim-packadd',
    license = 'MIT',
    packages = [ 'packadd' ],
    cmdclass = { 'epita_install': epita_install },
    entry_points = {
        'console_scripts': [ 'packadd = packadd.packadd:main' ],
    },
    data_files = [ ('epita', [ '*.sh' ]) ],
    install_requires = [ 'gitpython' ],
    test_suite = 'packadd.tests',
)
