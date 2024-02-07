#COBINATION OF SEARCH FILE AND FILE 
import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Search for files containing a keyword
def search_files(directory, keyword, extensions):
    matches = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    if keyword in content:
                        matches.append(file_path)
    return matches

# Organize files based on extensions
def organize_files(directory, media_extensions):
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

# Main code
search_directory = input("Enter the directory path to search: ")
keyword = input("Enter the keyword to search for: ")
search_extensions = (".txt", ".html", ".css", ".py", ".pdf", ".mp4")

organize_directory = input("Enter the directory path to monitor: ")
media_extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".tiff"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".flv", ".avchd"],
    "Audio": [".mp3", ".m4a", ".wav", ".flac"],
    "Document": [".txt", ".doc", ".docx", ".docm", ".pdf", ".xls", ".xlsx", ".xlsm", ".csv", ".odt", ".ppt", ".pptx", ".pptm", ".odp"],
    "Programming files": [".html", ".htm", ".css", ".js", ".bat"],
    "Software": [".exe", ".war", ".app", ".bin", ".jar", ".ear", ".zip", ".apk", ".7z", ".rar"]
}

# Perform file search
search_matches = search_files(search_directory, keyword, search_extensions)
if search_matches:
    print("Files containing the keyword:")
    for file in search_matches:
        print(file)
else:
    print("NO matching file found")

# Organize files
organize_files(organize_directory, media_extensions)
