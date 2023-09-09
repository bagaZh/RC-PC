import os, wget, zipfile, requests, getpass, sys
user_path = os.path.expanduser('~') 
USER_NAME = getpass.getuser()
Thisfile = sys.argv[0] # Полный путь к файлу, включая название и расширение
Thisfile_name = os.path.basename(Thisfile) # Название файла без пути
tfn=Thisfile.replace(Thisfile_name, "")
user_path = os.path.expanduser('~') # Путь к папке пользователя
if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
    os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')
if not os.path.exists(f"{user_path}\\AppData\\Roaming\\RC-PC.exe"):
    os.system(f'copy "{tfn}RC-PC.exe" "{user_path}\\AppData\\Roaming\\RC-PC.exe"')
result = requests.get("https://raw.githubusercontent.com/bagaZh/RC-PC/main/RC-PC/version.txt")
last_ver = result.content.decode("utf-8")
a = open(f"{user_path}\\AppData\\Roaming\\version.txt", "r")
current_ver = a.read()
a.close()
if "RX" in last_ver: iadm=0
else: iadm=1
if last_ver != current_ver:
    os.rmdir(f"{user_path}\\AppData\\Roaming\\RC-PC")
    os.mkdir(f"{user_path}\\AppData\\Roaming\\RC-PC")
    url='https://github.com/bagaZh/RC-PC/raw/main/RC-PC/RC-PC.exe'
    wget.download(url, out=f"{user_path}\\AppData\\Roaming\\RC-PC")
    url='https://raw.githubusercontent.com/bagaZh/RC-PC/main/RC-PC/version.txt'

    wget.download(url, out=f"{user_path}\\AppData\\RC-PC")

    
os.system(f"{user_path}\\AppData\\Roaming\\RC-PC.exe", )