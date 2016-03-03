'''

Compile dbf2csv into a single executable file,
simply run:
    python setup.py

'''

from distutils.core import setup
import py2exe, sys, os

# Show current python version
print (sys.version)

sys.argv.append('py2exe')

setup(
    console=['dbf2csv.py'],
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    zipfile = None,
)
