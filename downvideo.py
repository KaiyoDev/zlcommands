from pytube import YouTube

link = "https://www.youtube.com/watch?v=w9TcErzdoTg"

yt = YouTube(link)  

try:
    yt.streams.filter(progressive = True, 
file_extension = "mp4").first().download(output_path = "C:\codde", 
filename = "Reiner and Bertholdt Transformation scene")
except:
    print("Some Error!")
print('Task Completed!')