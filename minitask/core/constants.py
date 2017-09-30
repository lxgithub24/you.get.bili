# -*- coding:utf-8 -*-

# UPPER_LIST = [
#     '影视大魔王',
#     '谷阿莫',
#     'TEDed',
#     '日食记',
#     '一人食',
#     '硬糖视频',
#     '军武次位面',
#     '大旅行家的故事']


UPPER_LIST = [
    'ForwardFit毛毛',
    '从零开始健身',
    '黄博士爱健康',
    'NowFitness',
    '周六野Zoey',
    '小辣妈coco',
    'Fit健身',
    '舞哩',
    'lana酱好纠结',
    '口袋舞蹈',
    'GH5舞蹈工作室',
    'ZekoSay',
    '优舞团',
    '瑞得心理',
    'nya酱的一生',
    'Daily-TED',
    '一刻talks',
    '白花恋诗·彩',
    '偶搭App',
    '蘑菇街官方',
    '时尚博主MAGICYANG',
    '仿佛是一条咸鱼',
    'Crewkicks',
    '我是球球菌',
    'KALINKAY',
    '杨小空爱吃鸡',
    '阿布的自我修养',
    'KIKO熊熊',
    '二更',
    '打卡Doka',
    '梨视频'
]

BILIBILI_URL = 'https://search.bilibili.com/all?keyword=%s&page=1&order=totalrank'

# WORKING_DIRECTORY = '/home/liuxianga/test/download_bilibili'
WORKING_DIRECTORY = '/usr/local/var/www'

HOST = 'localhost'
USER = 'root'
PWD = 'liuxiang'
DB = 'minitask'

# MYSQL_DEFINE = 'mysql+pymysql://root:liuxiang@127.0.0.1:3306/minitask?charset=utf8mb4'
MYSQL_DEFINE = 'mysql+pymysql://root:root@127.0.0.1:3306/minitask?charset=utf8mb4'

PRE_MAX = 33
END_MAX = 16

print '\n'.join([''.join([('liuxiang'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else '')for x in range(-30,30)])for y in range(15,-15,-1)])
