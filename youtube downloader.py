from pytube import YouTube
print('enter the link = ')
link = input()
print(link)
yt = YouTube(link)

yd = yt.streams.get_highest_resolution()
yd.download(r"D:\youtube downloads")
print('finished download')

