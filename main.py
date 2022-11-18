from pytube import YouTube
from pytube.cli import on_progress

from ffmconverter import convert_webm_to_mp4

# link = input("Enter YouTube video URL: ")

link = "https://youtu.be/MToMx6RCW-M"

yt = YouTube(link, on_progress_callback=on_progress)

# for stream in yt.streams: 
#     print(stream)

print(yt.title)
ytVideoDownload = yt.streams.order_by('resolution').desc().first()
ytAudioDownload = yt.streams.get_audio_only()


print('Video downloading started 🟡')
# ytVideoDownload.download(output_path="./downloads/")
print('Video downloaded ✅')

print('Audio downloading started 🟡')
# ytAudioDownload.download(output_path="./downloads/", filename_prefix='audio_')
print('Audio downloaded ✅')

convert_webm_to_mp4(r'test.webm', r'test.mp4')
print('.webm to .mp4 converted ✅')
