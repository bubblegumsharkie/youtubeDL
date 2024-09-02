import os
import subprocess
from openpyxl import Workbook, load_workbook

from const import TEMP_FOLDER, OUTPUT_FOLDER


def delete_temp_current_video_folder():
    print('🟡 clearing temp folder')
    for file in os.listdir(TEMP_FOLDER):
        print(file)
        os.remove(TEMP_FOLDER + file)
    print('✅ all temp files are gone')


def move_to_output_folder(filename: str):
    print('🟡 moving to output folder started')
    print(filename)
    command_rename = "mv " + TEMP_FOLDER + "output.mp4 " + OUTPUT_FOLDER + filename + ".mp4"
    print(command_rename)
    subprocess.run(command_rename, shell=True)
    print('✅ moved to output folder')
