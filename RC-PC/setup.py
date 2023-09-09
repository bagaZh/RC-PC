import os, tkinter
import sys
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    user_path = os.path.expanduser('~') # Путь к папке пользователя
    Thisfile = sys.argv[0]
    Thisfile_name = os.path.basename(Thisfile) # Название файла без пути
    tf=Thisfile.replace(Thisfile_name, "pyupdate.exe")
    token = input("Введите токен бота (Его можно получить в тг у https://t.me/BotFather):")
    usid=input("Введите ваш телеграмм id (Его можно получить у https://t.me/username_to_id_bot, пример '1234567890'):")
    f = open(f"{user_path}\\AppData\\Roaming\\temp.txt",'w')
    f.write(str(f"{usid}\n"))
    f.write(str(token))

    f.close()
    a=input("Бот запущен, вы можете закрыть это окно через 15 секунд, после перезагрузки ваш бот автоматически заработает\n MADE BY L baga")
    os.system(tf)
    tkinter.messagebox.showinfo(title="Информация", message="Полсе перезагрузки можно будет удалить все скаченные, бот автоматически заработает")
else:
    if sys.version_info[0]==3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)



