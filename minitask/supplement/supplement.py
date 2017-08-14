# -*- coding:utf-8 -*-
import subprocess
from minitask.core import constants
from minitask.models.ORM import Video_info

def get_site_url():
    for i in range(0,524):
        site_src = Video_info.query(i)[0].site_src
        get_site_src_cmd = 'you-get -O {} --format=mp4 {}'.format(i,site_src)
        try:
            p = subprocess.Popen(get_site_src_cmd,shell=True,cwd=constants.WORKING_DIRECTORY)
            p.wait()
        except:
            print('download failed')

if __name__ == '__main__':
    get_site_url()