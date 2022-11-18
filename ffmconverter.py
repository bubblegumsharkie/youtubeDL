import shlex
import subprocess

from const import TEMP_FOLDER, OUTPUT_FOLDER
from utils import delete_temp_current_video_folder


def convert_webm_to_mp4():
    # ffmpeg -i /downloads/test.webm /downloads/test.mp4
    command = 'ffmpeg -i ' + TEMP_FOLDER + 'video.webm ' + TEMP_FOLDER + 'video.mp4'
    subprocess.run(command, shell=True)


def merge_audio_to_mp4(filename: str):
    print(filename)
    filename = shlex.quote(filename)
    print(filename)
    # ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4
    command = "ffmpeg -i " + TEMP_FOLDER + "video.mp4 -i " \
              + TEMP_FOLDER + "audio.mp4 -c:v copy -c:a aac " + TEMP_FOLDER + "output.mp4"
    subprocess.run(command, shell=True)
    command_rename = "mv " + TEMP_FOLDER + "output.mp4 " + OUTPUT_FOLDER + filename + ".mp4"
    subprocess.run(command_rename, shell=True)
    delete_temp_current_video_folder(TEMP_FOLDER)
