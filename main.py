from pathlib import Path # find path
import shutil # move files
import watchdog.observers # watch folder
import watchdog.events # event handler


# main paths
home_dir = Path.home() # find home directory, C:\Users\gusta
gustavo_dir = home_dir / 'OneDrive' / 'Documentos' / 'a Gustavo'
downloads_dir = home_dir / 'Downloads' 


# creates directories if they don't exist
(gustavo_dir / 'Certificados e Diplomas').mkdir(parents=True, exist_ok=True)
(gustavo_dir / 'aa Facul atividades exercícios').mkdir(parents=True, exist_ok=True)
(gustavo_dir / 'Currículo').mkdir(parents=True, exist_ok=True)
(gustavo_dir / 'ISOs e servidores').mkdir(parents=True, exist_ok=True)
(home_dir / 'Música').mkdir(parents=True, exist_ok=True)
(home_dir / 'Vídeos').mkdir(parents=True, exist_ok=True)
(home_dir / 'Imagens' / 'movidos download').mkdir(parents=True, exist_ok=True)
(home_dir / 'Downloads' / 'executáveis').mkdir(parents=True, exist_ok=True)
(home_dir / 'Downloads' / 'jogos torrent').mkdir(parents=True, exist_ok=True)

# extension filters:
doc_extensions = ['.pdf', '.doc', '.docx', '.ppt', '.pptx']
image_extensions = ['.jpg', '.jpeg', '.png']
music_extensions = ['.mp3', '.wav', '.flac']
video_extensions = ['.mp4', '.avi', '.mkv']
iso_extensions = ['.iso']
executables_extensions = ['.exe']
torrent_extensions = ['.torrent']


# 'certificado', 'diploma', 'cv' filters:
def move_by_keyword(file_path: Path, file_name_lower: str) -> bool:
    if 'certificado' in  file_name_lower or 'diploma' in file_name_lower:
        shutil.move(file_path, gustavo_dir/'Certificados e Diplomas')
        return True
    
    if 'cv' in file_name_lower:
        shutil.move(file_path, gustavo_dir/'Currículo')
        return True
    
    if 'exercicios' in file_name_lower or 'exercicio' in file_name_lower or 'atividade' in file_name_lower:
        shutil.move(file_path, gustavo_dir/'aa Facul atividades exercícios')
        return True
    
    return False


# moves files:
for f in downloads_dir.iterdir():
    if not f.is_file():
        continue # skip directories

    suffix = f.suffix.lower() # gets file extension
    file_name_lower = f.name.lower() # gets file name in lower case to compare

    if suffix in doc_extensions:
        if move_by_keyword(f, file_name_lower):
            continue
        else:
            shutil.move(f, gustavo_dir)

    elif suffix in image_extensions:
        if move_by_keyword(f, file_name_lower):
            continue
        shutil.move(f, home_dir/'Imagens'/'movidos download')
    
    elif suffix in music_extensions:
        shutil.move(f, home_dir/'Música')
    
    elif suffix in video_extensions:
        shutil.move(f, home_dir/'Vídeos')
    
    elif suffix in iso_extensions:
        shutil.move(f, gustavo_dir/'ISOs e servidores')

    elif suffix in executables_extensions:
        shutil.move(f, downloads_dir/'executáveis')

    elif suffix in torrent_extensions:
        shutil.move(f, donwloads_dir / 'jogos torrent')