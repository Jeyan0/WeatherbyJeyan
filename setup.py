from setuptools import setup

APP = ['weather_gui.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['requests'],
    'excludes': ['pkg_resources'], 
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
