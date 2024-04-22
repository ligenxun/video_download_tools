# -*- coding: utf-8 -*-
# @Time : 2024/2/23 13:22 
# @Author : cys
# @Email : ligenxun@foxmail.com
# @File : downloadPopup

import tkinter as tk
from tkinter import filedialog,ttk
import downloads_tools.down_video as down_video
import os

def get_default_download_path():
    # 获取用户的家目录
    home_directory = os.path.expanduser('~')
    # Windows系统中的默认下载目录通常在用户的家目录下的"Downloads"文件夹
    download_path = os.path.join(home_directory, "Downloads")
    return download_path

# 保存路径
def ph():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    return path

class CustomEntry(tk.Entry):
    def __init__(self, master, placeholder):
        super().__init__(master)
        self.placeholder = placeholder
        self.insert(0, self.placeholder)
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

    def on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)

    def on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)

class downloadPopup:
    def __init__(self):
        # self.videoSavePath = './'
        self.videoSavePath = get_default_download_path()
        self.downloadType = 'yt_dlp'

        self.ytm = tk.Tk()  # 创建Tk对象
        self.ytm.title("下载")  # 设置窗口标题

        # 计算屏幕宽度和高度
        screen_width = self.ytm.winfo_screenwidth()
        screen_height = self.ytm.winfo_screenheight()

        # 设置弹窗大小为屏幕宽度的1/5和屏幕高度的1/3
        popup_width = screen_width // 3
        popup_height = screen_height // 3
        self.ytm.geometry(f"{popup_width}x{popup_height}")

        # 创建一个Frame用于布局
        self.frame_d = tk.Frame(self.ytm)
        self.frame_d.pack(padx=12, pady=12)  # 设置Frame的边距

        self.l1 = tk.Label(self.frame_d, text="下载：")  # 链接标签
        self.l1.pack(side=tk.LEFT)  # 指定包管理器放置组件

        self.dropdown_var = tk.StringVar()  # 创建一个Tkinter变量，用于保存下拉框的选项
        # 创建下拉框选项
        options = ["yt_dlp", "you-get", "youtube-dl"]
        # 创建下拉框选择器，并绑定变量和选项
        self.dropdown = ttk.OptionMenu(self.frame_d, self.dropdown_var, options[0], *options)
        # 设置下拉框选择器的位置
        self.dropdown.pack(side=tk.LEFT)

        # self.url_text = tk.Entry(self.frame_d)  # 创建文本框
        self.url_text = CustomEntry(self.frame_d, "请输入下载地址")  # 创建文本框
        self.url_text.pack(side=tk.LEFT)

    def ss(self):
        path = ph()
        print(path)
        self.videoSavePath = path
        tk.Label(self.ytm, text='保存地址 = ' + path).pack()

    def down(self, url):
        tk.Label(self.ytm, text='下载中……').pack()
        down_video.down_video(url, self.videoSavePath, 'yt_dlp')
        tk.Label(self.ytm, text='%s:下载完成！' % url).pack()

    def geturl(self):
        url = self.url_text.get()  # 获取文本框内容
        print(url)
        self.down(str(url))
        # quit()

    def on_option_changed(self, *args):
        print("你的下载方式为："+self.dropdown_var.get())
        print("注意，如果发现下载失败，请尝试更换下载方式！")
        self.downloadType = self.dropdown_var.get()

    def start_soft(self):

        self.dropdown_var.trace('w', self.on_option_changed) # 绑定下拉框的选择事件到函数on_option_changed

        bt = tk.Button(self.frame_d, text="选择下载地址", command=self.ss)
        bt2 = tk.Button(self.frame_d, text="下载", command=self.geturl)  # command绑定获取下载地址方法
        bt.pack(side=tk.LEFT)
        bt2.pack(side=tk.LEFT)

        tk.Label(self.ytm, text='默认保存地址 = ' + self.videoSavePath).pack()
        tk.Label(self.ytm, text='注意，如果需要使用到cookies来下载\n，那么请使用yt_dlp，并且在软件运行的文件夹下，\n创建名为cookies.txt的文件，软件会自动尝试读取cookies，\n如果无法读取，那么会尽量识别电脑中chrome浏览器里的cookies').pack()


        self.ytm.mainloop()  # 进入主循环


if __name__ == "__main__":
    handler = downloadPopup()
    handler.start_soft()
