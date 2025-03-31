import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        x = float(entry_x.get().replace(',', '.'))
        y = float(entry_y.get().replace(',', '.'))
        
        denominator = (2 * x - x**2 * y)
        if denominator == 0:
            raise ZeroDivisionError("Ділення на нуль! Оберіть інші значення x і y.")
        
        a = (x**2 + 2*x*y - y**2) / denominator
        result_label.config(text=f"Результат: a = {a:.4f}")
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректні числові значення для x і y (наприклад, 2.5 або 3,7).")
    except ZeroDivisionError as e:
        messagebox.showerror("Помилка", str(e))

def run_tests():
    test_cases = [
        (1, 2), (3.5, 4.2), (0, 1), (-2.8, -3.1), (2, -2), (5.5, 0), (2.3, 1.7)
    ]
    results = []
    for x, y in test_cases:
        try:
            denominator = (2 * x - x**2 * y)
            if denominator == 0:
                results.append(f"Тест ({x}, {y}): Ділення на нуль")
            else:
                a = (x**2 + 2*x*y - y**2) / denominator
                results.append(f"Тест ({x}, {y}): a = {a:.4f}")
        except Exception as e:
            results.append(f"Тест ({x}, {y}): Помилка {e}")
    
    messagebox.showinfo("Результати тестування", "\n".join(results))

root = tk.Tk()
root.title("Обчислення рівняння")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Введіть x:").grid(row=0, column=0)
entry_x = tk.Entry(frame)
entry_x.grid(row=0, column=1)

tk.Label(frame, text="Введіть y:").grid(row=1, column=0)
entry_y = tk.Entry(frame)
entry_y.grid(row=1, column=1)

calc_button = tk.Button(frame, text="Обчислити", command=calculate)
calc_button.grid(row=2, column=0, columnspan=2, pady=5)

test_button = tk.Button(frame, text="Запустити тести", command=run_tests)
test_button.grid(row=3, column=0, columnspan=2, pady=5)

result_label = tk.Label(frame, text="Результат: ")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
