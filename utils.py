import os
import subprocess

from const import TEMP_FOLDER, OUTPUT_FOLDER


def delete_temp_current_video_folder():
    print('🟡 clearing temp folder')
    for file in os.listdir(TEMP_FOLDER):
        print(file)
        os.remove(TEMP_FOLDER + file)
    print('✅ all temp files are gone')


def move_to_output_folder(filename: str):
    print('🟡 moving to output folder started')
    command_rename = "mv " + TEMP_FOLDER + "output.mp4 " + OUTPUT_FOLDER + filename + ".mp4"
    subprocess.run(command_rename, shell=True)
    print('✅ moved to output folder')
