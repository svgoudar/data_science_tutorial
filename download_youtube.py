from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=zJBzuqdjz50")
yt.streams.get_highest_resolution().download
# yt = yt.get('mp4', '720p')
# yt.download('.')