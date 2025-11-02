import tkinter as tk

# تابع‌ها برای کار دکمه‌ها
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "خطا")

# پنجره اصلی
root = tk.Tk()
root.title("ماشین حساب")

entry = tk.Entry(root, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

# دکمه‌ها
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, command=clear)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: click(t))
    btn.grid(row=row, column=col)
root.mainloop()
