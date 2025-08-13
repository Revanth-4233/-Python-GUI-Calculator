# calculator_improved.py
import tkinter as tk
import re

def press(ch):
    entry_text.set(entry_text.get() + str(ch))

def backspace():
    entry_text.set(entry_text.get()[:-1])

def clear():
    entry_text.set("")

def safe_eval(expr):
    # allow only digits, operators, parentheses, decimal point and spaces
    if not re.fullmatch(r'[\d+\-*/%(). ]*', expr):
        raise ValueError("Invalid characters in expression")
    # eval is used here for arithmetic. Do NOT expose this to untrusted users.
    return eval(expr)

def equal_press():
    expr = entry_text.get()
    try:
        result = safe_eval(expr)
        # show integer without trailing .0
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        entry_text.set(str(result))
    except Exception:
        entry_text.set("Error")

def on_key(event):
    # handle keyboard typing
    ch = event.char
    if ch in '0123456789.+-*/%()':
        press(ch)
    elif event.keysym == 'Return':
        equal_press()
    elif event.keysym == 'BackSpace':
        backspace()
    # ignore other keys

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 20), justify="right", bd=8)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

buttons = [
    ('C', clear), ('⌫', backspace), ('(', lambda: press('(')), (')', lambda: press(')')),
    ('7', lambda: press('7')), ('8', lambda: press('8')), ('9', lambda: press('9')), ('/', lambda: press('/')),
    ('4', lambda: press('4')), ('5', lambda: press('5')), ('6', lambda: press('6')), ('*', lambda: press('*')),
    ('1', lambda: press('1')), ('2', lambda: press('2')), ('3', lambda: press('3')), ('-', lambda: press('-')),
    ('0', lambda: press('0')), ('.', lambda: press('.')), ('=', equal_press), ('+', lambda: press('+'))
]

row = 1
col = 0
for (text, cmd) in buttons:
    btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=cmd)
    btn.grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

# bind keyboard events (typing, Enter, Backspace)
root.bind('<Key>', on_key)

root.mainloop()
