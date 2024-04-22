# -*- coding: utf-8 -*-
# @Time : 2024/2/23 13:28 
# @Author : cys
# @Email : ligenxun@foxmail.com
# @File : down_video

import http.cookiejar
import os


def check_file(filename='cookies.txt'):
    # 获取当前工作目录
    current_directory = os.getcwd()

    # 构建完整的文件路径
    file_path = os.path.join(current_directory, filename)

    # 检查文件是否存在
    if os.path.exists(file_path):
        print("存在cookies文件！转为使用cookies模式。")
        return True
    else:
        return False


def load_cookies_from_file(cookie_file='cookies.txt'):
    # 创建一个MozillaCookieJar对象
    cookie_jar = http.cookiejar.MozillaCookieJar(cookie_file)
    # 加载cookies.txt文件
    cookie_jar.load()
    # 将cookie_jar转换为字典
    cookies_dict = {}
    for cookie in cookie_jar:
        cookies_dict[cookie.name] = cookie.value
    print(cookies_dict)
    return cookies_dict


def down_video(url, videoSavePath, downloadType='yt_dlp', definition="best"):
    is_cookies = check_file()
    if is_cookies:
        cookies = load_cookies_from_file()
    else:
        cookies = {}

    if downloadType == 'you-get':
        from you_get.extractors import youtube
        youtube.any_download(url, merge=True, output_dir=videoSavePath, cookies=cookies)

    if downloadType == 'youtube-dl':
        import youtube_dl

        # 配置youtube-dl
        # '/path/to/your/download/directory/%(title)s-%(id)s.%(ext)s'
        if is_cookies:
            ydl_opts = {
                'outtmpl': f'{videoSavePath}/%(title)s-%(id)s.%(ext)s',  # 输出文件名模板和目录
                'format': f'bestvideo[ext=mp4]+bestaudio[ext=m4a]/{definition}',  # 视频和音频质量
                'merge-output-format': 'mp4',  # 合并视频和音频为mp4格式
                'cookiefile': 'cookies.txt'  # 指定cookies.txt文件路径
            }
        else:
            ydl_opts = {
                'outtmpl': f'{videoSavePath}/%(title)s-%(id)s.%(ext)s',  # 输出文件名模板和目录
                'format': f'bestvideo[ext=mp4]+bestaudio[ext=m4a]/{definition}',  # 视频和音频质量
                'merge-output-format': 'mp4',  # 合并视频和音频为mp4格式
            }

        # 使用youtube-dl下载视频
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    if downloadType == 'yt_dlp':
        import yt_dlp

        # 配置yt-dlp
        if is_cookies:
            if cookies == {}:
                ydl_opts = {
                    'outtmpl': f'{videoSavePath}/%(title)s-%(id)s.%(ext)s',  # 输出文件名模板和目录
                    'format': f'bestvideo[ext=mp4]+bestaudio[ext=m4a]/{definition}',  # 视频和音频质量
                    'merge-output-format': 'mp4',  # 合并视频和音频为mp4格式
                    # 'cookiefile': 'cookies.txt',  # 指定cookies.txt文件路径
                    'cookiesfrombrowser': ['chrome'],  # 指定cookies.txt文件路径
                }
            else:
                ydl_opts = {
                    'outtmpl': f'{videoSavePath}/%(title)s-%(id)s.%(ext)s',  # 输出文件名模板和目录
                    'format': f'bestvideo[ext=mp4]+bestaudio[ext=m4a]/{definition}',  # 视频和音频质量
                    'merge-output-format': 'mp4',  # 合并视频和音频为mp4格式
                    'cookiefile': 'cookies.txt',  # 指定cookies.txt文件路径
                    # 'cookiesfrombrowser': ['chrome'],  # 指定cookies.txt文件路径
                }
        else:
            ydl_opts = {
                'outtmpl': f'{videoSavePath}/%(title)s-%(id)s.%(ext)s',  # 输出文件名模板和目录
                'format': f'bestvideo[ext=mp4]+bestaudio[ext=m4a]/{definition}',  # 视频和音频质量
                'merge-output-format': 'mp4',  # 合并视频和音频为mp4格式
            }

        # 使用yt-dlp下载视频
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

if __name__ == '__main__':

    # url = 'https://www.bilibili.com/video/BV1G34y1j7HJ/?spm_id_from=333.337.search-card.all.click&vd_source=63a3d835ff158c110166be27fa52e69a'
    url = 'https://www.bilibili.com/video/BV17a411x7aV'
    down_video(url,'./',"yt_dlp")