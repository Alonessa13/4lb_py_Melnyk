import tkinter as tk
from tkinter import messagebox
def button_click(symbol):
    """Додає символ до поля введення"""
    entry_field.insert(tk.END, symbol)
def clear_field():
    """Очищає поле введення"""
    entry_field.delete(0, tk.END)
def calculate():
    """Обчислює введений вираз"""
    try:
        expression = entry_field.get()
        result = eval(expression)
        entry_field.delete(0, tk.END)
        entry_field.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Помилка", "Невірний вираз")
# Створюємо головне вікно
root = tk.Tk()
root.title("Калькулятор")
# Поле введення
entry_field = tk.Entry(root, width=25, font=('Arial', 16))
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# Кнопки
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]
# Створюємо кнопки в циклі
row = 1
col = 0
for button in buttons:
    if button == 'C':
        action = clear_field
    elif button == '=':
        action = calculate
    else:
        action = lambda x=button: button_click(x)
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 14), command=action) \
        .grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1
# Запуск вікна
root.mainloop()
