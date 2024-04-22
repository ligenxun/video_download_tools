# -*- coding: utf-8 -*-
# @Time : 2024/2/23 13:22 
# @Author : cys
# @Email : ligenxun@foxmail.com
# @File : downloadPopup

import tkinter as tk
from tkinter import filedialog, ttk
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

        # 创建一个 日志打印窗口 组件
        # self.log_show = tk.Text(self.ytm, height=10, width=40)
        self.log_show = tk.Text(self.ytm)
        self.log_show.pack()

    def log_show_input(self, string):
        # 日志打印
        self.log_show.insert(tk.END, string + '\n')  # 输入字符串
        self.ytm.update_idletasks()  # 更新 Text 组件

    def ss(self):
        path = ph()
        print(path)
        self.videoSavePath = path

        self.log_show_input(f'$$$$$$$$$\n保存地址修改为 = {path}\n$$$$$$$$$')

    def down(self, url):
        # 下载
        self.log_show_input('==========下载中……=============')
        down_video.down_video(url, self.videoSavePath, 'yt_dlp')
        self.log_show_input('%s:下载完成！\n======================' % url)

    def geturl(self):
        url = self.url_text.get()  # 获取文本框内容
        print(url)
        self.down(str(url))
        # quit()

    def on_option_changed(self, *args):
        print("你的下载方式为：" + self.dropdown_var.get())
        print("注意，如果发现下载失败，请尝试更换下载方式！")
        self.log_show_input("################\n你的下载方式为：" + self.dropdown_var.get())
        self.log_show_input("注意，如果发现下载失败，请尝试更换下载方式！\n#################")
        self.downloadType = self.dropdown_var.get()

    def start_soft(self):
        self.dropdown_var.trace('w', self.on_option_changed)  # 绑定下拉框的选择事件到函数on_option_changed

        bt = tk.Button(self.frame_d, text="选择下载地址", command=self.ss)
        bt2 = tk.Button(self.frame_d, text="下载", command=self.geturl)  # command绑定获取下载地址方法
        bt.pack(side=tk.LEFT)
        bt2.pack(side=tk.LEFT)

        # tk.Label(self.ytm, text='默认保存地址 = ' + self.videoSavePath).pack()
        # tk.Label(self.ytm, text='注意，如果需要使用到cookies来下载，\n那么请使用yt_dlp，并且在软件运行的文件夹下，\n创建名为cookies.txt的文件，软件会自动尝试读取cookies，\n如果读取读取，那么会尽量识别电脑中chrome浏览器里的cookies（首先得有cookies.txt这个文件，才会认为需要使用到cookies，尝试取浏览器中的cookies）').pack()
        self.log_show_input("日志显示启动……")
        self.log_show_input('默认保存地址 = ' + self.videoSavePath)
        self.log_show_input(
            '注意：如果需要使用到cookies来下载（例如b站下载高清视频），那么请使用yt_dlp，并且在软件运行的同级文件夹下，创建名为cookies.txt的文件。\n================\n软件会自动尝试读取cookies，如果读取失败，那么会尽量识别电脑中chrome浏览器里的cookies（首先得有cookies.txt这个文件，才会认为需要使用到cookies，尝试取浏览器中的cookies。只要chrome浏览器内登录过b站即可正确使用（仅支持chrome）。\n================\n')

        self.ytm.mainloop()  # 进入主循环


if __name__ == "__main__":
    handler = downloadPopup()
    handler.start_soft()
