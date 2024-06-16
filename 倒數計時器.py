import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

if __name__ == "__main__":
    seconds = int(input("Enter the time in seconds: "))
    countdown_timer(seconds)
    
import tkinter as tk
from tkinter import messagebox

def countdown_timer(count):
    mins, secs = divmod(count, 60)
    timer = f'{mins:02d}:{secs:02d}'
    label.config(text=timer)
    if count > 0:
        root.after(1000, countdown_timer, count-1)
    else:
        messagebox.showinfo("Time's up", "倒數計時結束！")

def start_timer():
    try:
        time_in_seconds = int(entry.get())
        countdown_timer(time_in_seconds)
    except ValueError:
        messagebox.showwarning("Invalid input", "請輸入一個有效的數字")

root = tk.Tk()
root.title("倒數計時器")

label = tk.Label(root, font=('Helvetica', 48), text="00:00")
label.pack(pady=20)

entry = tk.Entry(root, font=('Helvetica', 24))
entry.pack(pady=20)

start_button = tk.Button(root, text="開始", command=start_timer)
start_button.pack(pady=20)

root.mainloop()
