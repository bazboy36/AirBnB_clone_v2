#!/usr/bin/python3
'''A Fabric script that creates and distributes an archive to web servers, \
        using the function deploy:'''

from fabric.api import local, put, run, env
from fabric.decorators import runs_once
import datetime
import os
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


""" def do_pack():
    '''creates a .tgz archive from the contents of web_static folder'''
    local('mkdir -p versions')
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    path = ('versions/web_static_{}.tgz'.format(date))
    result = local('tar -cvzf {} web_static'.format(path))

    if result.failed:
        return None
    return path
"""

env.hosts = ['ubuntu@100.25.47.182', 'ubuntu@100.25.153.250']


"""def do_deploy(archive_path):
    Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success"""


def deploy():
    path = do_pack()
    if path is None:
        return False
    result = do_deploy(path)
    return result
