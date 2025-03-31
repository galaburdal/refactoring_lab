import tkinter as tk
from tkinter import messagebox

def area(x1, y1, x2, y2, x3, y3):
    """Обчислення площі трикутника за координатами його вершин"""
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)

def is_inside_triangle(x1, y1, x2, y2, x3, y3, x, y):
    """Перевіряє, чи лежить точка (x, y) всередині трикутника"""
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)

    return abs(A - (A1 + A2 + A3)) < 1e-6  

def check_point():
    try:
        x1, y1 = float(entry_x1.get().replace(',', '.')), float(entry_y1.get().replace(',', '.'))
        x2, y2 = float(entry_x2.get().replace(',', '.')), float(entry_y2.get().replace(',', '.'))
        x3, y3 = float(entry_x3.get().replace(',', '.')), float(entry_y3.get().replace(',', '.'))
        px, py = float(entry_px.get().replace(',', '.')), float(entry_py.get().replace(',', '.'))

        if is_inside_triangle(x1, y1, x2, y2, x3, y3, px, py):
            result_label.config(text="Точка знаходиться всередині трикутника", fg="green")
        else:
            result_label.config(text="Точка знаходиться ЗА межами трикутника", fg="red")

    except ValueError:
        messagebox.showerror("Помилка", "Введіть числові координати!")

def run_tests():
    test_cases = [
        ((0, 0, 5, 0, 2.5, 5), (2, 2), True),   # Всередині
        ((0, 0, 5, 0, 2.5, 5), (5, 5), False),  # Ззовні
        ((-3, -3, 3, -3, 0, 3), (0, 0), True),  # Всередині
        ((-3, -3, 3, -3, 0, 3), (3, 3), False), # Ззовні
        ((1, 1, 4, 1, 2.5, 4), (2.5, 2), True), # Всередині
    ]

    results = []
    for (x1, y1, x2, y2, x3, y3), (px, py), expected in test_cases:
        result = is_inside_triangle(x1, y1, x2, y2, x3, y3, px, py)
        status = "✅ Успіх" if result == expected else "❌ Помилка"
        results.append(f"Точка ({px}, {py}) -> {status}")

    messagebox.showinfo("Результати тестування", "\n".join(results))

root = tk.Tk()
root.title("Перевірка точки в трикутнику")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Координати трикутника:").grid(row=0, column=0, columnspan=2)

tk.Label(frame, text="X1:").grid(row=1, column=0)
entry_x1 = tk.Entry(frame)
entry_x1.grid(row=1, column=1)

tk.Label(frame, text="Y1:").grid(row=2, column=0)
entry_y1 = tk.Entry(frame)
entry_y1.grid(row=2, column=1)

tk.Label(frame, text="X2:").grid(row=3, column=0)
entry_x2 = tk.Entry(frame)
entry_x2.grid(row=3, column=1)

tk.Label(frame, text="Y2:").grid(row=4, column=0)
entry_y2 = tk.Entry(frame)
entry_y2.grid(row=4, column=1)

tk.Label(frame, text="X3:").grid(row=5, column=0)
entry_x3 = tk.Entry(frame)
entry_x3.grid(row=5, column=1)

tk.Label(frame, text="Y3:").grid(row=6, column=0)
entry_y3 = tk.Entry(frame)
entry_y3.grid(row=6, column=1)

tk.Label(frame, text="Координати точки:").grid(row=7, column=0, columnspan=2)

tk.Label(frame, text="Px:").grid(row=8, column=0)
entry_px = tk.Entry(frame)
entry_px.grid(row=8, column=1)

tk.Label(frame, text="Py:").grid(row=9, column=0)
entry_py = tk.Entry(frame)
entry_py.grid(row=9, column=1)

check_button = tk.Button(frame, text="Перевірити точку", command=check_point)
check_button.grid(row=10, column=0, columnspan=2, pady=5)

test_button = tk.Button(frame, text="Запустити тести", command=run_tests)
test_button.grid(row=11, column=0, columnspan=2, pady=5)

result_label = tk.Label(frame, text="Результат: ")
result_label.grid(row=12, column=0, columnspan=2)

root.mainloop()
