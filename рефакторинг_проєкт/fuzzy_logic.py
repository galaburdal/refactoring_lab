# fuzzy_logic.py - Логіка нечітких обчислень

import numpy as np
import skfuzzy as fuzz

# Константи
TEMPERATURE_RANGE = np.arange(0, 101, 1)
VALVE_ANGLE_RANGE = np.arange(-90, 91, 1)


class FuzzySystem:
    def __init__(self):
        self._define_membership_functions()
        self.rules = self._define_rules()

    def _define_membership_functions(self):
        self.temperature_functions = {
            "cold": fuzz.trapmf(TEMPERATURE_RANGE, [0, 0, 10, 30]),
            "warm": fuzz.trimf(TEMPERATURE_RANGE, [20, 50, 80]),
            "hot": fuzz.trapmf(TEMPERATURE_RANGE, [60, 90, 100, 100])
        }

        self.valve_functions = {
            "big_left": fuzz.trapmf(VALVE_ANGLE_RANGE, [-90, -90, -60, -30]),
            "no_change": fuzz.trimf(VALVE_ANGLE_RANGE, [-10, 0, 10]),
            "big_right": fuzz.trapmf(VALVE_ANGLE_RANGE, [30, 60, 90, 90])
        }

    def _define_rules(self):
        return {
            "cold": self.valve_functions["big_left"],
            "warm": self.valve_functions["no_change"],
            "hot": self.valve_functions["big_right"]
        }

    def compute_truths(self, temperature_value):
        return {key: fuzz.interp_membership(TEMPERATURE_RANGE, func, temperature_value)
                for key, func in self.temperature_functions.items()}

    def mamdani_defuzzify(self, temperature_value):
        truths = self.compute_truths(temperature_value)
        activated_rules = [np.fmin(truths[key], self.rules[key]) for key in truths]
        aggregated = np.fmax.reduce(activated_rules)
        return fuzz.defuzz(VALVE_ANGLE_RANGE, aggregated, 'centroid')
