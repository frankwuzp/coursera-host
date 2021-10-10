#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   frankwuzp
@Contact :   me@wuzhiping.top
@Github  :   [frankwuzp](https://github.com/frankwuzp)
@Time    :   2021/10/10 13:48:40
@Version :   1.0
@License :   Copyright © 2017-2020 liuyuqi. All Rights Reserved.
@Desc    :   get ip of 'coursera.org' automaticly
@Credits ：  [jianboy](https://github.com/jianboy)
'''

import shutil
import os,sys,ctypes
import datetime
import get_ip_utils
import platform

# 需要获取ip的网址
sites = [
    "coursera.org",
    "d3c33hcgiwev3.cloudfront.net",
    "d3njjcbhbojbot.cloudfront.net",
]

addr2ip = {}
hostLocation = r"hosts"

def dropDuplication(line):
    flag = False
    if "#*******" in line:
        return True
    for site in sites:
        if site in line:
            flag = flag or True
        else:
            flag = flag or False
    return flag

# 更新host, 并刷新本地DNS
def updateHost():
    # 不显示时分秒的方法 => today = datetime.date.today()
	today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for site in sites:
        trueip=get_ip_utils.getIpFromipapi(site)
        if trueip != None:
            addr2ip[site] = trueip
            print(site + "\t" + trueip)
    with open(hostLocation, "r") as f1:
        f1_lines = f1.readlines()
        with open("temphost", "w") as f2:
            for line in f1_lines:                       # 为了防止 host 越写用越长，需要删除之前更新的含有github相关内容
                if dropDuplication(line) == False:
                    f2.write(line)
            f2.write("# Coursera Start\n")
            f2.write("# From https://github.com/frankwuzp/coursera-host\n")
			f2.write("# Update Time: " + str(today) "\n")
            for key in addr2ip:
                f2.write(addr2ip[key] + "\t" + key + "\n")
			f2.write("# Coursera End\n")
    os.remove(hostLocation)
    os.rename("temphost",hostLocation)

if __name__ == "__main__":
    updateHost()
