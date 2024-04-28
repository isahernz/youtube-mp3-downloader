from pytube import YouTube

path_downloads = 'Your Path to Downloads Folder'

video_url = str(input("Enter the URL of the YouTube Video: "))

def my_callback(stream, file_handle):
    print("Download Completed Satifactorily!")
    print("Saving to:", file_handle)

# Get Video of YouTube
yt = YouTube(video_url, on_complete_callback=my_callback)
stream = yt.streams.filter(type="audio").order_by('abr').desc().first()
stream.download(path_downloads, filename=yt.title.title()+".mp3")