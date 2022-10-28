#!/usr/bin/python3
""" Write a Fabric script that generates a .tgz archive from the contents \
        of the web_static folder of your AirBnB Clone repo, \
        using the function do_pack. """

from fabric.api import *
import datetime


def do_pack():
    """ creates a tar.tgz compressed file """
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    arg = 'versions/web_static_{}.tgz'.format(date)
    result = local(f'mkdir -p versions && tar -cvzf {arg} web_static')
    if result.return_code == 0:
        return arg
    else:
        return None
