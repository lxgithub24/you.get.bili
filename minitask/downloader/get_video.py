# -*- coding:utf-8 -*-
import subprocess
from ..core import constants


def download(video_dict,j):
    site_url = video_dict.get('site_src')
    try:
        getvideo_cmd = 'you-get -O {} --format=mp4 {}'.format(j,site_url)
        print(getvideo_cmd)
        p = subprocess.Popen(
            getvideo_cmd,
            shell=True,
            cwd=constants.WORKING_DIRECTORY)
        p.wait()
    except BaseException:
        print("download failed & BaseException out")
    return video_dict
