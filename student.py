#!/usr/bin/env python3
"""
This module represents a student.
"""

__author__ = "Zelin Cai, Patrick Silvestre"
__version__ = "0.1.0"
__license__ = "MIT"


class Student:
    def __init__(self, age, years_lived_in_california, months_worked_part_time,
                 years_parents_paid_state_tax, volunteered_for_cause,
                 income_per_year):
        self.age = age
        self.years_lived_in_california = years_lived_in_california
        self.months_worked_part_time = months_worked_part_time
        self.years_parents_paid_state_tax = years_parents_paid_state_tax
        self.volunteered_for_cause = volunteered_for_cause
        self.income_per_year = income_per_year
