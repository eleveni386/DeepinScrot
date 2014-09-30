#!/usr/bin/evn python
#coding=utf8
#Author : eleven.i386
#Email  : eleven.i386@gmail.com
#Site   : eleveni386.7axu.com
#Date   : 14-04-20
#DES	:

import subprocess
import requests

proxy = {'http':'http://127.0.0.1:8080'}

pic_bed = 'http://eleveni386.7axu.com/Image/'
tmp_filename = '/tmp/tmp_eleveni386.png'

def share():
    post_data = {'mypic':open(tmp_filename).read()}
    r = requests.post(pic_bed,files=post_data)
    cmd = ('echo {0} |xsel -i -b'.format(r.text.replace('\n','')))
    subprocess.Popen(cmd,shell=True)
    tipContent = '发布成功,使用Ctrl+V'
    subprocess.Popen('python tipswindow.py {0}'.format(tipContent),shell=True)


if __name__ == '__main__':
    share()
