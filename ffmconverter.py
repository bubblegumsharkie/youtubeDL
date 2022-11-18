import subprocess

from const import TEMP_FOLDER


def convert_webm_to_mp4():
    print('🟡 .webm to .mp4 conversion started')
    # ffmpeg -i /downloads/test.webm /downloads/test.mp4
    command = 'ffmpeg -i ' + TEMP_FOLDER + 'video.webm -crf 9 -c:v libx264 ' + TEMP_FOLDER + 'video.mp4'
    subprocess.run(command, shell=True)
    print('✅ .webm to .mp4 converted')


def merge_audio_to_mp4():
    print('🟡 merging audio started')
    # ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4
    command = "ffmpeg -i " + TEMP_FOLDER + "video.mp4 -i " \
              + TEMP_FOLDER + "audio.mp4 -c:v copy -c:a aac " + TEMP_FOLDER + "output.mp4"
    subprocess.run(command, shell=True)
    print('✅ audio merged')
