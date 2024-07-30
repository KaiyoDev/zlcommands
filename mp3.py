from moviepy.editor import *
def convert():
	mp4_file = "video.mp4"

	mp3_file = "audio.mp3"

	videoClip = VideoFileClip(mp4_file)

	audioclip = videoClip.audio

	audioclip.write_audiofile(mp3_file)

	audioclip.close()
