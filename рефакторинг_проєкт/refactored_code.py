# refactored_code.py - Використання нечіткої логіки

import numpy as np
import matplotlib.pyplot as plt
from fuzzy_logic import FuzzySystem

# Створення системи
fuzzy_system = FuzzySystem()
temperature_values = np.arange(0, 101, 1)
mamdani_results = [fuzzy_system.mamdani_defuzzify(temp) for temp in temperature_values]

# Візуалізація
plt.figure(figsize=(10, 6))
plt.plot(temperature_values, mamdani_results, label='Мамдані', color='dodgerblue')
plt.fill_between(temperature_values, mamdani_results, color='lightblue', alpha=0.5)
plt.xlabel('Температура води (°C)')
plt.ylabel('Кут повороту крана (°)')
plt.title('Регулювання потоку води')
plt.legend()
plt.grid()
plt.show()
