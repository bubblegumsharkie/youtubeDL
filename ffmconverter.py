import subprocess


def convert_webm_to_mp4(input_file, output_file):
    # ffmpeg -i test.webm test.mp4
    # try:
    command = "ffmpeg -i test.webm test.mp4" #+ input_file + ' ' + output_file
    subprocess.run(command, shell=True)
