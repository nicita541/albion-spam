import time
import pyautogui
import pyperclip
import keyboard
import tkinter as tk
import pygetwindow as gw  # Установи: pip install pygetwindow

SPAM_INTERVAL = 120  # Интервал между сообщениями (в секундах)
GAME_WINDOW_TITLE = "Albion Online"  # Название окна игры (поменяй, если нужно)

def focus_game():
    """Переключает активное окно на Albion Online."""
    windows = gw.getWindowsWithTitle(GAME_WINDOW_TITLE)
    if windows:
        windows[0].activate()
        time.sleep(1)  # Ждем переключения
    else:
        print("Окно игры не найдено!")

def send_message():
    """Отправляет сообщение в чат игры."""
    global last_send_time

    focus_game()  # Переключаемся на игру

    text = "(УРОН)ESPADA(УРОН)ЧИЛ PVP/PVE Нет КТА. Набираем НОВИЧКОВ обучаем/прокачиваем. Выдаём сеты на кач. Заявки в ДС !"

    pyautogui.press('enter')
    time.sleep(0.01)

    pyperclip.copy(text)
    time.sleep(0.01)

    keyboard.press_and_release("ctrl+v")
    time.sleep(0.01)

    pyautogui.press('enter')

    last_send_time = time.time()  # Запоминаем время отправки
    update_timer()  # Обновляем таймер

def update_timer():
    """Обновляет таймер на экране."""
    elapsed = time.time() - last_send_time
    remaining = max(0, SPAM_INTERVAL - elapsed)
    timer_label.config(text=f"До спама: {int(remaining)} сек")

    if remaining == 0:
        send_message()

    root.after(1000, update_timer)  # Обновляем каждую секунду

# Создание окна
root = tk.Tk()
root.title("Спамер Альбион")
root.geometry("200x100")
root.attributes('-topmost', True)  # Окно всегда поверх

timer_label = tk.Label(root, text="До спама: 0 сек", font=("Arial", 14))
timer_label.pack(expand=True)

last_send_time = time.time() - SPAM_INTERVAL  # Чтобы первый запуск был сразу
update_timer()

root.mainloop()
