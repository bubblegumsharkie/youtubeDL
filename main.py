import shlex

from pytubefix import YouTube
from pytubefix.cli import on_progress

from ffmconverter import convert_webm_to_mp4, merge_audio_to_mp4
from service import get_youtube_videos
from utils import delete_temp_current_video_folder, move_to_output_folder
from downloader import download
from pytubefix import Channel
from const import TEMP_FOLDER, DOWNLOADED_AUDIO
from xlswriter import download_video_from_xls, save_videos_to_xls

# mode = input("Select mode: (v)ideo / (p)laylist: ")
# if mode == "v":
#     link = input("Enter YouTube video URL: ")
#     download(link)
# if mode == "p":
#     print("ok")
# else:
#     print("I quit")
save_videos_to_xls("")
download_video_from_xls()