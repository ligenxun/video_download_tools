# -*- coding: utf-8 -*-
# @Time : 2024/2/23 13:28 
# @Author : cys
# @Email : ligenxun@foxmail.com
# @File : down_video

def down_video(url, videoSavePath, downloadType='yt_dlp'):
    if downloadType == 'you-get':
        from you_get.extractors import youtube
        youtube.any_download(url, merge=True, output_dir=videoSavePath)

    if downloadType == 'youtube-dl':
        import youtube_dl

        # 配置youtube-dl
        # '/path/to/your/download/directory/%(title)s-%(id)s.%(ext)s'
        ydl_opts = {
            'outtmpl': f'{videoSavePath}/%(title)s-%(id)s.%(ext)s',  # 输出文件名模板和目录
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',  # 视频和音频质量
            'merge-output-format': 'mp4',  # 合并视频和音频为mp4格式
        }

        # 使用youtube-dl下载视频
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    if downloadType == 'yt_dlp':
        import yt_dlp

        # 配置yt-dlp
        ydl_opts = {
            'outtmpl': f'{videoSavePath}/%(title)s-%(id)s.%(ext)s',  # 输出文件名模板和目录
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',  # 视频和音频质量
            'merge-output-format': 'mp4',  # 合并视频和音频为mp4格式
        }

        # 使用yt-dlp下载视频
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
