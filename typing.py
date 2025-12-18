import tkinter as tk
from tkinter import ttk
import random
import difflib
from timeit import default_timer

# Words List
WORDS = [
    'We are developing Python project',
    'This is Windows OS',
    'We are Hiring',
    'Let’s Play a game',

    'Python is a programming language',
    'We love Coding',
    'This is an amazing Article',
    'I am an Intern',
    'Let’s check the Output',
    'We are Compiling this program'
]

current_word = random.choice(WORDS)


root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("620x450")
#root.resizable(, )
root.configure(bg="#1e1e1e")

#####################################
title_font = ("Segoe UI", 24, "bold")
word_font = ("Segoe UI", 18, "bold")
text_font = ("Segoe UI", 14)
result_font = ("Segoe UI", 13, "bold")
#####################################

title = tk.Label(root, text="⏱ Typing Speed Test", font=title_font, fg="white", bg="#1e1e1e")
title.pack(pady=15)


word_frame = tk.Frame(root, bg="#252526", bd=4, relief="ridge")
word_frame.pack(pady=10)

display_word = tk.Label(word_frame, text=current_word, font=word_font, fg="#00d7ff", bg="#252526", wraplength=580)
display_word.pack(padx=10, pady=10)


input_label = tk.Label(root, text="Type the above sentence:", font=text_font, fg="white", bg="#1e1e1e")
input_label.pack(pady=5)

typed_text = tk.StringVar()
input_box = tk.Entry(root, textvariable=typed_text, font=("Consolas", 16), width=45, bd=3, relief="solid")
input_box.pack(pady=5)


btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

def style_button(btn):
    btn.bind("<Enter>", lambda e: btn.config(bg="#0b84d4"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#0078d7"))


start_time = None

def start_test():
    global start_time, current_word
    typed_text.set("")
    input_box.focus()
    start_time = default_timer()

def check_result():
    if start_time is None:
        return

    user_input = typed_text.get()
    end_time = default_timer()

    total_time = round(end_time - start_time, 2)
    speed = round(len(current_word.split()) * 60 / total_time, 2)

    if user_input == current_word:
        accuracy = 100.0
    else:
        accuracy = round(difflib.SequenceMatcher(None, current_word, user_input).ratio() * 100, 2)

    result_time.config(text=f"Time Taken: {total_time} sec")
    result_acc.config(text=f"Accuracy: {accuracy}%")
    result_speed.config(text=f"Typing Speed: {speed} WPM")

def reset_test():
    global current_word
    current_word = random.choice(WORDS)
    display_word.config(text=current_word)
    typed_text.set("")
    result_time.config(text="")
    result_acc.config(text="")
    result_speed.config(text="")
    start_test()



btn_start = tk.Button(btn_frame, text="Start", font=text_font, width=10, bg="#0078d7", fg="white",
                      command=start_test)
btn_start.grid(row=0, column=0, padx=10)
style_button(btn_start)

btn_check = tk.Button(btn_frame, text="Check", font=text_font, width=10, bg="#0078d7", fg="white",
                      command=check_result)
btn_check.grid(row=0, column=1, padx=10)
style_button(btn_check)

btn_reset = tk.Button(btn_frame, text="Reset", font=text_font, width=10, bg="#0078d7", fg="white",
                      command=reset_test)
btn_reset.grid(row=0, column=2, padx=10)
style_button(btn_reset)


result_frame = tk.Frame(root, bg="#1e1e1e")
result_frame.pack(pady=20)

result_time = tk.Label(result_frame, text="", font=result_font, fg="#ffd700", bg="#1e1e1e")
result_time.pack()

result_acc = tk.Label(result_frame, text="", font=result_font, fg="#00ff88", bg="#1e1e1e")
result_acc.pack()

result_speed = tk.Label(result_frame, text="", font=result_font, fg="#ffa0ff", bg="#1e1e1e")
result_speed.pack()

root.mainloop()
