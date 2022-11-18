import subprocess

BASE_FOLDER = "downloads/"
CONVERTED_FOLDER = "converted/"


def convert_webm_to_mp4(filename):
    # ffmpeg -i /downloads/test.webm /downloads/test.mp4
    command = 'ffmpeg -i ' + BASE_FOLDER + filename + '.webm ' + BASE_FOLDER + filename + '.mp4'
    subprocess.run(command, shell=True)


def merge_audio_to_mp4(filename):
    # ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4
    # command = "ffmpeg -i test.mp4 -i audio_test.mp4 -c:v copy -c:a aac output.mp4"
    command = "ffmpeg -i " + BASE_FOLDER + "video.mp4 -i " + BASE_FOLDER + "audio.mp4 -c:v copy -c:a aac output.mp4"
    subprocess.run(command, shell=True)
