#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import os, datetime
from src import crontab, crontab_run

# main
if __name__ == '__main__':
    
    executor='python3'
    # executor='python'
    script1 = 'tools.py'
    # 每天07点30分10秒运行一次'executor script1'
    crontab.every('day').at(hour=7, minute=30, second=00).execute(script1,executor)
    

    crontab_run(debug = False)