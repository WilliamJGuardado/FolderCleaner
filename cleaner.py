# -*- coding: utf-8 -*-
"""
Created on Sun May 12 17:50:38 2024

@author: William
"""
import logging
from os import scandir, rename
from os.path import exists, join, splitext
from shutil import move

# Setup logging
logging.basicConfig(level=logging.INFO, filename='file_operations.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')


# ! FILL IN BELOW
# source_dir = ""
# dest_dir_sfx = ""
# dest_dir_music = ""
# dest_dir_video = ""
# dest_dir_image = ""
#dest_dir_documents = ""


# Define directories
source_dir = r"C:/Users/William/Downloads"
dest_dir_sfx = r"C:/Users/William/Downloads/Sound"
dest_dir_music = r"C:/Users/William/Downloads/Music"
dest_dir_video = r"C:/Users/William/Downloads/Video"
dest_dir_image = r"C:/Users/William/Downloads/Images"
dest_dir_documents = r"C:/Users/William/Downloads/Documents"
dest_dir_zip = r"C:/Users/William/Downloads/Zip"
dest_dir_csv = r"C:/Users/William/Downloads/CSV"


# Define supported file extensions
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
document_extensions = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
zip_extensions = [".zip"]
csv_extensions = [".csv"]
def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    unique_name = f"{filename}({counter}){extension}"
    while exists(join(dest, unique_name)):
        counter += 1
        unique_name = f"{filename}({counter}){extension}"
    return unique_name

def move_file(dest, entry, name):
    full_dest_path = join(dest, name)
    try:
        if exists(full_dest_path):
            unique_name = make_unique(dest, name)
            rename(full_dest_path, join(dest, unique_name))
        move(entry.path, full_dest_path)
        logging.info(f"Moved file {name} to {dest}")
    except Exception as e:
        logging.error(f"Error moving file {name}: {str(e)}")

def on_cleaner():
    with scandir(source_dir) as entries:
        for entry in entries:
            if entry.is_file():
                check_files(entry)

def check_files(entry):
    name = entry.name
    lower_name = name.lower()
    for category, extensions in (('audio', audio_extensions), ('video', video_extensions), ('image', image_extensions), ('document', document_extensions), ('zip', zip_extensions), ('csv', csv_extensions)):
        if any(lower_name.endswith(ext) for ext in extensions):
            if category == 'audio':
                dest = dest_dir_sfx if entry.stat().st_size < 10_000_000 or "SFX" in name else dest_dir_music
            elif category == 'video':
                dest = dest_dir_video
            elif category == 'image':
                dest = dest_dir_image
            elif category == 'document':
                dest = dest_dir_documents
            elif category == 'zip':
                dest = dest_dir_zip
            elif category == 'csv':
                dest = dest_dir_csv
            move_file(dest, entry, name)
            break


# Call the cleaner function
on_cleaner()
