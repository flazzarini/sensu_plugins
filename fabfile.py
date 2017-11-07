import fabric.api as fab
from os.path import exists


@fab.task
def develop():
    if not exists("env/"):
        fab.local("virtualenv env")
    fab.local("./env/bin/python setup.py develop")
