"""
This file demonstrates common uses for the Python unittest module
https://docs.python.org/3/library/unittest.html
"""
import unittest
import student as student_class
import scholarship_eligibility


class TestValidStudents(unittest.TestCase):
    """These tests focus on students who are eligible for scholarships."""

    def test_student1(self):
        student = student_class.Student(18, 2, 6, 0, 0, 0)
        expected_output = 1
        actual_output = scholarship_eligibility.determine_eligibility(student)
        self.assertEqual(expected_output, actual_output)


class TestInvalidStudents(unittest.TestCase):
    """These tests focus on students who are not eligible for scholarships."""


class TestRedirectedStudents(unittest.TestCase):
    """These tests focus on students who are to be redirected to the dean."""


if __name__ == '__main__':
    unittest.main()
