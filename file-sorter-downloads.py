import os

def list_upper(var):
    var = [i.upper() for i in var]
    return var

baseDir = os.path.join(os.path.expanduser('~'), 'Downloads')

image_extensions = ["jpg", "jpeg", "png", "gif", "svg", "webp", "bmp", "tif", "tiff", "raw", "psd"]
aud_vid_extensions = ["mp4", "mp3", "webm", "mov", "wmv", "wav", "avi", "mkv", "m4v", "rm", "rmvb", "aac", "flac", "m4a", "wma"]
installer_extensions = ["exe", "msi", "dmg", "pkg", "mpkg","app", "sh"]
document_extensions = ["pdf", "doc", "docx", "ppt", "pptx", "xls", "xlsx", "txt", "rtf", "csv", "odt", "odp", "ods"]
comp_arch_extensions = ["zip", "rar", "7z", "tar", "gz", "bs2", "xz", "tgz", "tar.gz", "tbz", "tar.bz2", "tbx", "tar.xz"]
disk_img_extensions = ["iso"]

other_dir = os.path.join(baseDir, "Other")

for i in os.listdir(baseDir):
    fileName, fileExtension = os.path.splitext(i)
    ext = fileExtension[1:]

    if ext == "ini" or ext == "":
        continue

    elif ext in image_extensions or ext in list_upper(image_extensions):
        dirPath = os.path.join(baseDir, "Images")

    elif ext in installer_extensions or ext in list_upper(installer_extensions):
        dirPath = os.path.join(baseDir, "Program Installers")  

    elif ext in aud_vid_extensions or ext in list_upper(aud_vid_extensions):
        dirPath = os.path.join(baseDir, "Audio-Video")

    elif ext in document_extensions or ext in list_upper(document_extensions):
        dirPath = os.path.join(baseDir, "Documents")

    elif ext in comp_arch_extensions or ext in list_upper(comp_arch_extensions):
        dirPath = os.path.join(baseDir, "Compressed Archives")

    elif ext in disk_img_extensions or ext in list_upper(disk_img_extensions):
        dirPath = os.path.join(baseDir, "Disk Images")   

    else:
        if not os.path.exists(other_dir):
            os.mkdir(other_dir)
        dirPath = other_dir
    if not os.path.exists(dirPath):
        os.mkdir(dirPath)
    os.replace(os.path.join(baseDir, i), os.path.join(dirPath, i))