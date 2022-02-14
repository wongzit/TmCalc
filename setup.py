"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['tmcalc_v_2_0_1_src.py']
DATA_FILES = ['./assets']
OPTIONS = {'iconfile': './assets/tmcalc.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)