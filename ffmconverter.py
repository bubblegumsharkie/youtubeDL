import subprocess

from const import TEMP_FOLDER, DOWNLOADED_FILE, DOWNLOADED_AUDIO,CONVERTED_VIDEO, OUTPUT_FILE


def convert_webm_to_mp4():
    print('🟡 .webm to .mp4 conversion started')
    command = 'ffmpeg -i ' + TEMP_FOLDER + DOWNLOADED_FILE + ' -crf 21 -c:v libx264 ' + TEMP_FOLDER + CONVERTED_VIDEO
    # command = 'ffmpeg -i ' + TEMP_FOLDER + DOWNLOADED_FILE + ' -c:v hevc_videotoolbox -q:v 65 -tag:v hvc1 ' + TEMP_FOLDER + CONVERTED_VIDEO
    subprocess.run(command, shell=True)
    print('✅ .webm to .mp4 converted')


def merge_audio_to_mp4():
    print('🟡 merging audio started')
    # ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4
    command = "ffmpeg -i " + TEMP_FOLDER + CONVERTED_VIDEO + " -i " \
              + TEMP_FOLDER + DOWNLOADED_AUDIO + " -c:v copy -c:a aac " + TEMP_FOLDER + OUTPUT_FILE
    subprocess.run(command, shell=True)
    print('✅ audio merged')
