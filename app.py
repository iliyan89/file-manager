# This is my file manager project

import os
import shutil

main_file = "app.py"

#directory paths
source = "/home/hades/Documents/security-analyst/file-manager"

audio_dir = "/home/hades/Documents/security-analyst/file-manager/audio"

video_dir = "/home/hades/Documents/security-analyst/file-manager/videos"

images_dir = "/home/hades/Documents/security-analyst/file-manager/images"

programming_dir = "/home/hades/Documents/security-analyst/file-manager/programming"

text_dir = "/home/hades/Documents/security-analyst/file-manager/text"

files = os.listdir(source)

# file formats list
audio_file_formats = ['mp3', 'wav']
doc_file_formats = ['doc', 'docx']
text_file_formats = ['txt']
video_file_formats = ['mp4', 'mkv']
programming_file_formats = ['py', 'js', 'cpp']
images_file_formats = ['png', 'jpg']

# ignore the main_file
if main_file in files:
    get_file_index = files.index(main_file)
    del files[get_file_index]

for file in files:

    file_ext = file.split('.')[-1]

    if file_ext in audio_file_formats:
        shutil.move(file, audio_dir)

    if file_ext in doc_file_formats:
        shutil.move(file, text_dir)

    if file_ext in text_file_formats:
        shutil.move(file, text_dir)

    if file_ext in video_file_formats:
        shutil.move(file, video_dir)

    if file_ext in programming_file_formats:
        shutil.move(file, programming_dir)

    if file_ext in images_file_formats:
        shutil.move(file, images_dir)