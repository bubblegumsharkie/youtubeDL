import subprocess
BASE_FOLDER = "downloads/"


def convert_webm_to_mp4(input_file, output_file):
    # ffmpeg -i /downloads/test.webm /downloads/test.mp4
    # try:
    command = 'ffmpeg -i ' + BASE_FOLDER + ' ' + input_file + ' ' + BASE_FOLDER + ' ' + output_file
    subprocess.run(command, shell=True)


def merge_audio_to_mp4(input_file, output_file):
    # ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4
    command = "ffmpeg -i test.mp4 -i audio_test.mp4 -c:v copy -c:a aac output.mp4"
    subprocess.run(command, shell=True)
