# -*- coding: utf-8 -*-
# @Time : 2024/2/23 15:04 
# @Author : cys
# @Email : ligenxun@foxmail.com
# @File : main
import downloads_tools.downloadPopup as dp

# 指定ffmpeg的路径
try:
    import sys
    import os

    if getattr(sys, 'frozen', False):
        os.environ['PATH'] += os.pathsep + sys._MEIPASS
except Exception as e:
    print(e)
if __name__ == '__main__':
    main_soft = dp.downloadPopup()
    main_soft.start_soft()
