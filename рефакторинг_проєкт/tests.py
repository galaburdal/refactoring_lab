# tests.py - Модульні тести для FuzzySystem

import pytest
import numpy as np
from fuzzy_logic import FuzzySystem

# Фікстура для створення системи
@pytest.fixture
def fuzzy_system():
    return FuzzySystem()

def test_membership_functions(fuzzy_system):
    assert len(fuzzy_system.temperature_functions) == 3
    assert len(fuzzy_system.valve_functions) == 3

@pytest.mark.parametrize("temp", [0, 25, 50, 75, 100])
def test_mamdani_defuzzify(fuzzy_system, temp):
    result = fuzzy_system.mamdani_defuzzify(temp)
    assert -90 <= result <= 90

def test_large_input_performance(fuzzy_system):
    large_input = np.linspace(0, 100, 1000)
    results = [fuzzy_system.mamdani_defuzzify(temp) for temp in large_input]
    assert len(results) == 1000
