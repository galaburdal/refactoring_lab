import numpy as np
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 1. Завантаження даних
data = pd.read_csv('C:\\Users\\ASUS\\Desktop\\3 курс 1 сем\\fuzex1trnData.dat', delim_whitespace=True)

# Витягування вхідних і вихідних даних
X1 = data['X1'].values
X2 = data['X2'].values
Y = data['Y'].values

# 2. Визначення змінних
x1 = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'X1')
x2 = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'X2')
y = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'Y')

# 3. Визначення функцій приналежності
x1['low'] = fuzz.trimf(x1.universe, [0, 0, 0.5])
x1['medium'] = fuzz.trimf(x1.universe, [0, 0.5, 1])
x1['high'] = fuzz.trimf(x1.universe, [0.5, 1, 1])

x2['low'] = fuzz.trimf(x2.universe, [0, 0, 0.5])
x2['medium'] = fuzz.trimf(x2.universe, [0, 0.5, 1])
x2['high'] = fuzz.trimf(x2.universe, [0.5, 1, 1])

y['low'] = fuzz.trimf(y.universe, [0, 0, 0.5])
y['medium'] = fuzz.trimf(y.universe, [0, 0.5, 1])
y['high'] = fuzz.trimf(y.universe, [0.5, 1, 1])

# 4. Правила
rule1 = ctrl.Rule(x1['low'] & x2['low'], y['low'])
rule2 = ctrl.Rule(x1['low'] & x2['medium'], y['low'])
rule3 = ctrl.Rule(x1['low'] & x2['high'], y['medium'])
rule4 = ctrl.Rule(x1['medium'] & x2['low'], y['low'])
rule5 = ctrl.Rule(x1['medium'] & x2['medium'], y['medium'])
rule6 = ctrl.Rule(x1['medium'] & x2['high'], y['high'])
rule7 = ctrl.Rule(x1['high'] & x2['low'], y['medium'])
rule8 = ctrl.Rule(x1['high'] & x2['medium'], y['high'])
rule9 = ctrl.Rule(x1['high'] & x2['high'], y['high'])

# 5. Система керування
control_system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
control_simulation = ctrl.ControlSystemSimulation(control_system)

# 6. Тестування системи
results = []
for i in range(len(X1)):
    control_simulation.input['X1'] = X1[i]
    control_simulation.input['X2'] = X2[i]
    control_simulation.compute()
    results.append(control_simulation.output['Y'])

# Вивід результатів
print("Вихідні результати:", results)

# 7. Візуалізація
plt.figure(figsize=(10, 6))

# Сортування значень для кращого вигляду графіка
sorted_indices = np.argsort(X1)
X1_sorted = X1[sorted_indices]
Y_sorted = Y[sorted_indices]
results_sorted = np.array(results)[sorted_indices]

plt.scatter(X1_sorted, Y_sorted, color='blue', label='Данні (Y)', s=50)

# Додавання лінії для виходу
plt.plot(X1_sorted, results_sorted, color='red', label='Виходи (Нечітка нейромережа)', linewidth=2)

# Додавання міток до точок
for i in range(len(X1_sorted)):
    plt.text(X1_sorted[i], Y_sorted[i], f'{Y_sorted[i]:.2f}', fontsize=8, ha='right')

plt.xlabel('X1')
plt.ylabel('Y')
plt.title('Вихідні значення за допомогою нечіткої нейромережі')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
