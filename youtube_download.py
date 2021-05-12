from pytube import YouTube

link = input("enter Youtube url: ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))
# list all the format 
for i in video: 
	print(i)	# print all the available format of video

print("Available Downloading formats:")
dn_option = int(input("enter the option: "))
dn_video = videos[dn_option]
dn_video.download()

print("download successfully!")