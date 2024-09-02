from pytubefix import YouTube

from const import TEMP_FOLDER, DOWNLOADED_FILE, DOWNLOADED_AUDIO
from utils import delete_temp_current_video_folder
# from youtubelistreciver import get_list_of_video_ids, get_playlist_name
# from xlswriter import save_videos_to_xls, download_video_from_xls


def get_youtube_videos(yt: YouTube):
    delete_temp_current_video_folder()
    # yt.bypass_age_gate()
    yt_video_download = yt.streams.order_by('resolution').desc().first()
    yt_audio_download = yt.streams.get_audio_only()

    print('🟡 Video downloading started')
    print(yt.title)
    yt_video_download.download(output_path=TEMP_FOLDER, filename=DOWNLOADED_FILE)
    print('✅ Video downloaded')

    print('🟡 Audio downloading started')
    # yt.streams.filter(type='audio').order_by('abr').desc().first()
    yt_audio_download.download(output_path=TEMP_FOLDER, filename=DOWNLOADED_AUDIO)
    print('✅ Audio downloaded')

# def save_playlist(playlist_id):
#     all_videos = get_list_of_video_ids(playlist_id)
#     name = get_playlist_name(playlist_id)
#     save_videos_to_xls(playlist_id)
#     download_video_from_xls()