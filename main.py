from pathlib import Path # find path
import shutil # move files
import watchdog.observers # watch folder
import watchdog.events # event handler


# main paths
home_dir = Path.home() # find home directory, C:\Users\YourUsername
downloads_dir = home_dir / 'Downloads' 


# creates directories if they don't exist
(home_dir / 'Downloads' / 'executables').mkdir(parents=True, exist_ok=True)
(home_dir / 'Downloads' / 'Downloads torrent').mkdir(parents=True, exist_ok=True)
(home_dir / 'Documents' / 'ISOs ans servers').mkdir(parents=True, exist_ok=True)
(home_dir / 'Documents'/ 'moved download').mkdir(parents=True, exist_ok=True)
(home_dir / 'Images' / 'moved download').mkdir(parents=True, exist_ok=True)
(home_dir / 'Music'/ 'moved download').mkdir(parents=True, exist_ok=True)
(home_dir / 'Videos'/ 'moved download').mkdir(parents=True, exist_ok=True)

# extension filters:
doc_extensions = ['.pdf', '.doc', '.docx', '.ppt', '.pptx']
image_extensions = ['.jpg', '.jpeg', '.png']
music_extensions = ['.mp3', '.wav', '.flac']
video_extensions = ['.mp4', '.avi', '.mkv']
iso_extensions = ['.iso']
executables_extensions = ['.exe']
torrent_extensions = ['.torrent']

# moves files:
for f in downloads_dir.iterdir():
    if not f.is_file():
        continue # skip directories

    suffix = f.suffix.lower() # gets file extension
    file_name_lower = f.name.lower() # gets file name in lower case to compare

    if suffix in executables_extensions:
        shutil.move(f, home_dir/'Downloads'/'executables')

    elif suffix in torrent_extensions:
        shutil.move(f, downloads_dir/'Downloads torrent')

    elif suffix in iso_extensions:
        shutil.move(f, home_dir/'Documents'/'ISOs ans servers')

    elif suffix in doc_extensions:
        shutil.move(f, home_dir/'Documents'/'moved download')

    elif suffix in image_extensions:
        shutil.move(f, home_dir/'Images'/'moved download')
    
    elif suffix in music_extensions:
        shutil.move(f, home_dir/'Music'/'moved download')
    
    elif suffix in video_extensions:
        shutil.move(f, home_dir/'Videos'/'moved download')
