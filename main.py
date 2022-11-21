import shlex

from pytube import YouTube
from pytube.cli import on_progress

from ffmconverter import convert_webm_to_mp4, merge_audio_to_mp4
from service import get_youtube_videos
from utils import delete_temp_current_video_folder, move_to_output_folder

link = input("Enter YouTube video URL: ")
yt = YouTube(link, on_progress_callback=on_progress)
filename = shlex.quote(yt.title)

# get_youtube_videos(yt)
convert_webm_to_mp4()
merge_audio_to_mp4()

move_to_output_folder(filename)
delete_temp_current_video_folder()
