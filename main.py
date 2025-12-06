from pathlib import Path # find path
import shutil # move files


home_dir = Path.home()
downloads_dir = home_dir / "Downloads"


for f in downloads_dir.iterdir():
    if f.is_file():
        suffix = f.suffix.lower()
        if suffix in ['.pdf', '.doc', '.docx']:
            shutil.move(str(f), str(downloads_dir / "Documentos"))        

        if suffix in ['.jpg', '.jpeg', '.png']:
            shutil.move(str(f), str(downloads_dir / "Imagens"))
        