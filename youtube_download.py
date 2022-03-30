from pytube import YouTube

def on_complete(stream, filepath):
    print('download completed')
    print(filepath)

def on_progress(stream, chunk, bytes_remaining):
    pass

link = input("Youtube video link: ")
video_object = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)

# video information
print(f'title: {video_object.title}')
print(f'length: {round(video_object.length/60, 2)} minutes')
print(f'views: {round(video_object.views/1000000, 2)} million')
print(f'author:  {video_object.views}')

# download
print(f'download: (b)est | (w)orst | (a)udio only | exit')
download_choice = input('choice: ')

match download_choice:
    case 'b':
        video_object.streams.get_highest_resolution().download('downloads')
    case 'w':
        video_object.streams.get_lowest_resolution().download('downloads')
    case 'a':
        video_object.streams.get_audio_only().download('downloads')

