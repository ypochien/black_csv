# coding=UTF-8
# __author__ == ypochien

from distutils.core import setup
import py2exe

setup(
    options={'py2exe': {'bundle_files': 1}} ,
    console=[{'script': 'csv2report.py'}] ,
    zipfile=None
)
