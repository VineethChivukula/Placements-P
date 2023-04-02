from pytube import YouTube
url='https://www.youtube.com/watch?v=sdZr2G2sjS0'
my_video=YouTube(url)
'''
for stream in my_video.streams:
    print(stream)
'''
my_video=my_video.streams.get_highest_resolution()
my_video.download()