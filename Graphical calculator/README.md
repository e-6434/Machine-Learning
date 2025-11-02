## فرا خواندن کتابخانه گرافیکی


```
import tkinter as tk
```
## تابعی که مقدار ورودی را به انتهای پنجره ماشین حساب اضافه میکند
```
def click(value):
      entry.insert(tk.END, value)
```
## تابعی که محتوای پنجره را صفر میکند
```
def clear():
    entry.delete(0, tk.END)
```
 ## تابعی که مسئول انجام محاسبات است با این ترتیب که اول ورودی را گرفته و محاسبه میکند سپس محتوای پنچره را خالی میکند تا تداخل ایجاد نشد حالا موقع افزودن نتیجه به پنجره است.
```
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "خطا")
```
## ساخت پنجره اصلی
 ```
root = tk.Tk()
root.title("ماشین حساب")
```
## ساخت پنجره ورودی و تعداد سطر و ستون های مورد نیاز و مشخص نمودن مختصات دکمه درون تاپل
```
entry = tk.Entry(root, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)
]
```
## ساخت دکمه ها با استفاده از حلقه
```
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, command=clear)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: click(t))
    btn.grid(row=row, column=col)
```
## زنده نگه داشتن برنامه
```
root.mainloop()

```
