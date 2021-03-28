# @Md_sahil_kaif

# Install pytube using command: pip install pytube
import pytube

# Store the youtube link in a variable
lnk = "video link"

# Attach the link with pytube and store in a variable
yt = pytube.YouTube(lnk)

# Stream the video
video = yt.streams.first()

# Download the video
video.download()
