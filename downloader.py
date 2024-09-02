import shlex
import sys

from pytubefix import YouTube
from pytubefix.cli import on_progress

from ffmconverter import convert_webm_to_mp4, merge_audio_to_mp4
from service import get_youtube_videos
from utils import delete_temp_current_video_folder, move_to_output_folder

def download(link):
    yt = YouTube(link, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True)
    try:
        filename = yt.title
        filename = filename.replace("'", "")
        filename = filename.replace(":", " ")
        filename = filename.replace("/", " ")
        filename = shlex.quote(filename)
    except:
        filename = input("Exception while accessing title was caught, please enter filename manually: ")

    get_youtube_videos(yt)
    convert_webm_to_mp4()
    merge_audio_to_mp4()

    move_to_output_folder(filename)
    delete_temp_current_video_folder()
    # except Exception as error:
    #     print("🔴🔴🔴🔴🔴🔴🔴 Error while working with " + filename + " 🔴🔴🔴🔴🔴🔴🔴")
    #     print(error)
    #     sys.exit(1)
