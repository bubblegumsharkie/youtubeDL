from pytube import YouTube
from pytube.cli import on_progress

from const import TEMP_FOLDER
from ffmconverter import convert_webm_to_mp4, merge_audio_to_mp4

# link = input("Enter YouTube video URL: ")
link = "https://youtu.be/MToMx6RCW-M"

yt = YouTube(link, on_progress_callback=on_progress)
filename = yt.title
print(filename)

ytVideoDownload = yt.streams.order_by('resolution').desc().first()
ytAudioDownload = yt.streams.get_audio_only()

# print('🟡 Video downloading started')
# ytVideoDownload.download(output_path=TEMP_FOLDER, filename="video.webm")
# print('✅ Video downloaded')

# print('🟡 Audio downloading started')
# ytAudioDownload.download(output_path=TEMP_FOLDER, filename="audio.mp4")
# print('✅ Audio downloaded')

# print('🟡 .webm to .mp4 conversion started')
# convert_webm_to_mp4()
# print('✅ .webm to .mp4 converted')

print('🟡 merging audio started')
merge_audio_to_mp4(filename)
print('✅ audio merged')
