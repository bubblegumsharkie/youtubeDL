from pytube import YouTube

from const import TEMP_FOLDER


def get_youtube_videos(yt: YouTube):
    yt_video_download = yt.streams.order_by('resolution').desc().first()
    yt_audio_download = yt.streams.get_audio_only()

    print('🟡 Video downloading started')
    print(yt.title)
    yt_video_download.download(output_path=TEMP_FOLDER, filename="video.webm")
    print('✅ Video downloaded')

    print('🟡 Audio downloading started')
    # yt.streams.filter(type='audio').order_by('abr').desc().first()
    yt_audio_download.download(output_path=TEMP_FOLDER, filename="audio.mp4")
    print('✅ Audio downloaded')
