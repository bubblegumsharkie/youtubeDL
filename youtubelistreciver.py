from googleapiclient.discovery import build
from secret import API_KEY

# https://www.youtube.com/playlist?list=PLTkaTWWaR2jje1EGNJezHlvdktJNjcoB5

# Вставьте свой API ключ
api_key = API_KEY

def get_list_of_video_ids(playlist_id):
    # Идентификатор плейлиста (можно взять из URL плейлиста)
    # Создаем объект YouTube API
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Пустой список для хранения всех видео
    all_videos = []

    list_of_playlist_ids = [
                            '', #playlist_name
                            ]
    
    for playlist_id in list_of_playlist_ids:
        print("current playlist id: " + playlist_id)
        next_page_token = None

        # Цикл для получения всех страниц результатов
        while True:
            playlist_items = youtube.playlistItems().list(
                part='snippet',
                playlistId=playlist_id,
                maxResults=50,  # Максимальное количество видео для получения на одной странице
                pageToken=next_page_token
            ).execute()

            # Добавляем видео из текущей страницы в общий список
            all_videos.extend(playlist_items['items'])

            # Проверяем наличие следующей страницы
            next_page_token = playlist_items.get('nextPageToken')

            # Если следующей страницы нет, выходим из цикла
            if not next_page_token:
                break

        # Выводим названия и идентификаторы всех видео
        for video in all_videos:
            video_title = video['snippet']['title']
            video_id = video['snippet']['resourceId']['videoId']
            print(f"Video Title: {video_title}, Video ID: {video_id}")
    
    return all_videos

def get_playlist_name(playlist_id):

    # Идентификатор плейлиста (можно взять из URL плейлиста)
    playlist_id = 'PLiCpP_44QZBy9V4WHYLXOE2cshGdgk8AQ' # AcademeG - ЭлектроВолга

    # Создаем объект YouTube API
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Выполняем запрос к API для получения информации о плейлисте
    playlist_request = youtube.playlists().list(
        part='snippet',
        id=playlist_id
    )
    response = playlist_request.execute()

    # Получаем название плейлиста из ответа
    playlist_title = response['items'][0]['snippet']['title']
    print(f"Название плейлиста: {playlist_title}")
