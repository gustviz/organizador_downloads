from pathlib import Path # find path
import shutil # move files


home_dir = Path.home() #find home directory
downloads_dir = home_dir / "Downloads" #find downloads directory


for f in downloads_dir.iterdir():
    if f.is_file():
        suffix = f.suffix.lower() #get file extension
        if suffix in ['.pdf', '.doc', '.docx']:
            if f.name.glob("*certificado*"):
                shutil.move(str(f), str(downloads_dir / "Documentos" / "aa gustavo" / "Certificados"))
            else:
                shutil.move(str(f), str(downloads_dir / "Documentos" / "aa gustavo"))

        if suffix in ['.jpg', '.jpeg', '.png']:
            shutil.move(str(f), str(downloads_dir / "Imagens"))
        
        if suffix in ['.iso']:
            shutil.move(str(f), str(downloads_dir / 'Documentos' / 'aa gustavo' / 'ISOs'))