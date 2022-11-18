from pytube import YouTube
from pytube.cli import on_progress

# link = input("Enter YouTube video URL: ")

link = "https://youtu.be/MToMx6RCW-M"

yt = YouTube(link, on_progress_callback=on_progress)

print(yt.title)
ytVideoDownload = yt.streams.order_by('resolution').desc().first()
ytAudioDownload = yt.streams.get_audio_only()

ytVideoDownload.download(output_path="./downloads/")
print("Video downloaded ✅")

ytAudioDownload.download(output_path="./downloads/", filename_prefix='audio_')
print("Audio downloaded ✅")