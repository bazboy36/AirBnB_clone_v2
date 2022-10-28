#!/usr/bin/python3
'''A Fabric script that distributes an archive to web servers'''

from fabric.api import run
from fabric.decorators import runs_once


env.hosts = ['100.25.47.182', '100.25.153.250']
env.user = ['ubuntu']

def do_deploy(archive_path):
    '''Returns True if all operations have been done correctly, 
    otherwise returns False'''
    put('archive_path', '/tmp')
    no_tgz = archive_path[9:-4]
    tgz = archive_path[9:]
    data_path = ('/data/web_static/releases/{}'.format(no_tgz))
    run('mkdir -p {}'.format(data_path))
    check = run('tar -xzf /tmp/{} -C {}'.format(tgz, data_path))
    if check.failed:
        return False
    run('rm /tmp/{}'.format(tgz))
    run('rm -rf /data/web_static/current')
    check_2 = run('ln -s {} /data/web_static/current'.format(data_path))
    if check_2.failed:
        return False
    return True
