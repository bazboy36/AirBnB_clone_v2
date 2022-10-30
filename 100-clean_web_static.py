#!/usr/bin/python3
""" Fabric script that deletes unneded achrived"""
from fabric.api import run, local, cd, env


env.hosts = env.hosts = ['ubuntu@100.25.47.182', 'ubuntu@100.25.153.250']


def do_clean(number=0):
    """ number is the number of the archives,
    including the most recent, to keep.
    If number is 0 or 1, keep only the most recent version of archive.
    if number is 2, keep the most recent,
    and second most recent versions of your archive.
    etc."""
    if number == 0 or number == 1:
        with cd('/AirBnB_clone_v2/versions'):
            local("ls -t | awk 'NR>1' | xargs rm -f")
        with cd('/data/web_static/releases'):
            run("ls -t / | awk 'NR>1' | xargs rm -rf")
    else:
        with cd('/AirBnB_clone_v2/versions'):
            local("ls -t | awk 'NR>{}' | xargs rm -f".format(
                  number))
        with cd('/data/web_static/releases'):
            run("ls -t | awk 'NR>{}' | xargs rm -rf".format(number))
