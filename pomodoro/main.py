import tkinter as tk

import time
import math
from tkinter import *
import pygame

pygame.mixer.init()
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
ROYALBLUE = "#4169E1"
LIGHTSEAGREEN = "#20B2AA"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
counting = True
continue_time = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global counting
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", bg=YELLOW)
    check_marks.config(text="")
    start_button.config(state=tk.NORMAL)
    window.config(bg=YELLOW)
    start_button.config(bg=YELLOW)
    canvas.config(bg=YELLOW)
    show_history_button.config(bg=YELLOW)
    reset_button.config(bg=YELLOW)
    stop_resume_button.config(bg=YELLOW)
    listbox.config(bg=YELLOW)
    complete_task_button.config(bg=YELLOW)
    add_button.config(bg=YELLOW)
    remove_button.config(bg=YELLOW)
    stop_resume_button.config(text="Stop", state=tk.DISABLED)
    counting = True
    global reps
    reps = 0
    stopMusic()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    stop_resume_button.config(state=tk.NORMAL)
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED, bg=LIGHTSEAGREEN)
        window.config(bg=LIGHTSEAGREEN)
        start_button.config(bg=LIGHTSEAGREEN)
        show_history_button.config(bg=LIGHTSEAGREEN)
        canvas.config(bg=LIGHTSEAGREEN)
        reset_button.config(bg=LIGHTSEAGREEN)
        stop_resume_button.config(bg=LIGHTSEAGREEN)
        listbox.config(bg=LIGHTSEAGREEN)
        check_marks.config(bg=LIGHTSEAGREEN)
        complete_task_button.config(bg=LIGHTSEAGREEN)
        add_button.config(bg=LIGHTSEAGREEN)
        remove_button.config(bg=LIGHTSEAGREEN)

    if reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK, bg=ROYALBLUE)
        window.config(bg=ROYALBLUE)
        start_button.config(bg=ROYALBLUE)
        canvas.config(bg=ROYALBLUE)
        show_history_button.config(bg=ROYALBLUE)
        reset_button.config(bg=ROYALBLUE)
        stop_resume_button.config(bg=ROYALBLUE)
        check_marks.config(bg=ROYALBLUE)
        listbox.config(bg=ROYALBLUE)
        complete_task_button.config(bg=ROYALBLUE)
        add_button.config(bg=ROYALBLUE)
        remove_button.config(bg=ROYALBLUE)

    else:
        count_down(work_sec)
        title_label.config(text="Working", fg=GREEN, bg=YELLOW)
        window.config(bg=YELLOW)
        start_button.config(bg=YELLOW)
        canvas.config(bg=YELLOW)
        show_history_button.config(bg=YELLOW)
        reset_button.config(bg=YELLOW)
        stop_resume_button.config(bg=YELLOW)
        check_marks.config(bg=YELLOW)
        listbox.config(bg=YELLOW)
        complete_task_button.config(bg=YELLOW)
        add_button.config(bg=YELLOW)
        remove_button.config(bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global counting, continue_time
    if counting:
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"

        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            start_button.config(state=tk.DISABLED)
            if counting:
                global timer
                timer = window.after(1000, count_down, count - 1)
                continue_time = count - 1
        else:
            playMusic()
            start_timer()
            mark = ""
            work_sessions = math.floor(reps / 2)
            for _ in range(work_sessions):
                mark += "✔"
                check_marks.config(text=mark)


# ---------------------------- STOP RESUME ------------------------------- #
def stop_resume_timer():
    global counting
    counting = not counting
    stopMusic()
    if counting:
        stop_resume_button.config(text="stop")
        count_down(continue_time)
    else:
        stop_resume_button.config(text="resume")


# ---------------------------- add task ------------------------------- #
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


# ---------------------------- remove task ------------------------------- #
def remove_item():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)


# ---------------------------- complete task ------------------------------- #
def complete_task():
    pass


# ---------------------------- sound ------------------------------- #

def playMusic():
    pygame.mixer.music.load("countingstar.mp3")
    pygame.mixer.music.play(loops=0)


def stopMusic():
    pygame.mixer.music.stop()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)
window.resizable(False, False)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"), width=12, height=2)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"),
                      command=start_timer, width=7, height=1)
start_button.grid(column=0, row=2)

stop_resume_button = Button(text="Stop", highlightthickness=0, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"),
                            command=stop_resume_timer, width=7, height=1)
stop_resume_button.grid(column=3, row=2)

reset_button = Button(text="Reset", highlightthickness=0, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"),
                      command=reset_timer, width=7, height=1)
reset_button.grid(column=3, row=3)

show_history_button = Button(text="History", highlightthickness=0, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"),
                             width=10, height=1)
show_history_button.grid(column=1, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_marks.grid(column=0, row=4)

listbox = Listbox(window, selectmode=tk.SINGLE, bg=YELLOW, width=30, height=6)
listbox.grid(column=1, row=3)

entry = tk.Entry(window, bg=YELLOW)
entry.grid(column=1, row=5)

add_button = tk.Button(window, text="Add task", highlightthickness=0, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "bold"),
                       command=add_task, width=10, height=1)
add_button.grid(column=3, row=5)

remove_button = tk.Button(window, text="Remove task", highlightthickness=0, fg=GREEN, bg=YELLOW,
                          font=(FONT_NAME, 14, "bold"), command=remove_item, width=10, height=1)
remove_button.grid(column=3, row=6)

complete_task_button = tk.Button(window, text="Finish task", highlightthickness=0, fg=GREEN, bg=YELLOW,
                                 font=(FONT_NAME, 14, "bold"), command=complete_task, width=10, height=1)
complete_task_button.grid(column=3, row=4)

window.mainloop()
