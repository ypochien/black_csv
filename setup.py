# coding=UTF-8
# __author__ == ypochien

from distutils.core import setup

setup(
    options={'py2exe': {'bundle_files': 1}} ,
    console=[{'script': 'csv2report.py'}] ,
    zipfile=None
)
