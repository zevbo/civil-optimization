import platform 

IS_MAC = platform.system() == 'Darwin'
FOLDER_SEP = "/" if IS_MAC else "\\"
COPY_CMD = "cp" if IS_MAC else "copy"