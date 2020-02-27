#!/usr/bin/env python3
"""
This module determines the scholarship eligibility of a student.
"""

__author__ = "Zelin Cai, Patrick Silvestre"
__version__ = "0.1.0"
__license__ = "MIT"


def determine_eligibility(student):
    if student.age < 18 or student.age > 24:
        return 0
    if student.years_lived_in_california < 2:
        if student.years_parents_paid_state_tax < 1:
            return 0
    if student.months_worked_part_time < 6:
        if student.income_per_year < 5000:
            return "Dean for consideration"
        if not student.volunteered_for_cause:
            return 0

    return 1
