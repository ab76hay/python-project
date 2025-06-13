import tkinter as tk
from tkinter import messagebox
import threading
import time
from datetime import datetime

reminders = []

# Function to check reminders in background
def check_reminders():
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        for reminder in reminders:
            if reminder['datetime'] == now and not reminder['notified']:
                messagebox.showinfo("Reminder", f"⏰ {reminder['title']}")
                reminder['notified'] = True
        time.sleep(30)

# Function to add reminder
def add_reminder():
    title = title_entry.get()
    date = date_entry.get()
    time_str = time_entry.get()

    try:
        reminder_datetime = f"{date} {time_str}"
        datetime.strptime(reminder_datetime, "%Y-%m-%d %H:%M")  # Validate format

        reminders.append({'title': title, 'datetime': reminder_datetime, 'notified': False})
        reminder_listbox.insert(tk.END, f"{title} at {reminder_datetime}")
        title_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter date as YYYY-MM-DD and time as HH:MM")

# GUI setup
root = tk.Tk()
root.title("🗓️ Calendar Reminder App")
root.geometry("400x400")

tk.Label(root, text="Reminder Title:").pack()
title_entry = tk.Entry(root, width=40)
title_entry.pack()

tk.Label(root, text="Date (YYYY-MM-DD):").pack()
date_entry = tk.Entry(root, width=40)
date_entry.pack()

tk.Label(root, text="Time (HH:MM in 24hr):").pack()
time_entry = tk.Entry(root, width=40)
time_entry.pack()

tk.Button(root, text="Add Reminder", command=add_reminder).pack(pady=10)

tk.Label(root, text="Your Reminders:").pack()
reminder_listbox = tk.Listbox(root, width=50)
reminder_listbox.pack(pady=10)

# Start background reminder checker
threading.Thread(target=check_reminders, daemon=True).start()

root.mainloop()
