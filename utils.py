import os


def delete_temp_current_video_folder(folder: str):
    for file in os.listdir(folder):
        os.remove(file)
