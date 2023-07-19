import os
import shutil

os.chdir("C:/Users/vedan/OneDrive/Desktop/RANDOM TEST")

# Create folders if they don't exist
folders = ["audio", "video", "image", "utils", "zips", "docs"]
for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)

audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")
util = (".exe")
zips = (".zip", ".rar")
pdf = (".pdf", '.docx')


def is_audio(file):
    return os.path.splitext(file)[1] in audio


def is_video(file):
    return os.path.splitext(file)[1] in video


def is_image(file):
    return os.path.splitext(file)[1] in img


def is_util(file):
    return os.path.splitext(file)[1] in util


def is_zips(file):
    return os.path.splitext(file)[1] in zips


def is_pdf(file):
    return os.path.splitext(file)[1] in pdf


count = 0
for item in os.listdir():
    if os.path.isfile(item):
        if is_audio(item):
            shutil.move(item, "C:/Users/vedan/OneDrive/Desktop/RANDOM TEST/audio")
            count += 1
        elif is_video(item):
            shutil.move(item, "C:/Users/vedan/OneDrive/Desktop/RANDOM TEST/video")
            count += 1
        elif is_image(item):
            shutil.move(item, "C:/Users/vedan/OneDrive/Desktop/RANDOM TEST/image")
            count += 1
        elif is_zips(item):
            shutil.move(item, "C:/Users/vedan/OneDrive/Desktop/RANDOM TEST/zips")
            count += 1
        elif is_pdf(item):
            shutil.move(item, "C:/Users/vedan/OneDrive/Desktop/RANDOM TEST/docs")
            count += 1
        elif is_util(item):
            pass  # Skip moving files with .exe extension
        else:
            shutil.move(item, "C:/Users/vedan/OneDrive/Desktop/RANDOM TEST/utils")
            count += 1

print("Successfully moved:", count, "files and folders.")
