import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

media_extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif",".tiff"],
    "Videos": [".mp4", ".avi", ".mkv",".mov",".flv",".avchd"],
    "Audio": [".mp3",".m4a",".wav", ".flac"],
    "Document":[".txt",".doc",".docx",".docm",".pdf",".xls",".xlsx",".xlsm",".csv",".odt",".ppt",".pptx",".pptm",".odp"],
    "Programming files":[".html",".htm",".css",".js",".bat"],
    "Software":[".exe",".war",".app",".bin",".jar",".ear",".zip",".apk",".7z",".rar"]
}
directory = input("Enter the directory path to monitor: ")
class MediaFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        for media_type, extensions in media_extensions.items():
            if any(event.src_path.lower().endswith(ext) for ext in extensions):
                target_dir = os.path.join(directory, media_type)
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(event.src_path, os.path.join(target_dir, os.path.basename(event.src_path)))
                print(f"Moved {event.src_path} to {target_dir}")
event_handler = MediaFileHandler()
observer = Observer()
observer.schedule(event_handler, path=directory, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
