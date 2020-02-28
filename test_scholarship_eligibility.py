"""
This file demonstrates common uses for the Python unittest module
https://docs.python.org/3/library/unittest.html
"""
import unittest
import student as student_class
import scholarship_eligibility


class TestValidStudents(unittest.TestCase):
    """These tests focus on students who are eligible for scholarships."""

    """ Test case: a, c, e, h, k, m, p, r, t"""

    def test_case6(self):
        student = student_class.Student(19, 10, 5, 2, 1, 15000)
        expected_output = 1
        actual_output = scholarship_eligibility.determine_eligibility(student)
        self.assertEqual(expected_output, actual_output)

    """ Test case: a, c, e, h, k, n, t"""

    def test_case7(self):
        student = student_class.Student(24, 12, 40, 0, 0, 0)
        expected_output = 1
        actual_output = scholarship_eligibility.determine_eligibility(student)
        self.assertEqual(expected_output, actual_output)


class TestInvalidStudents(unittest.TestCase):
    """These tests focus on students who are not eligible for scholarships."""

    """ Test case: a, b, f, l, s"""

    def test_case1(self):
        student = student_class.Student(17, 0, 0, 0, 0, 0)
        expected_output = 0
        actual_output = scholarship_eligibility.determine_eligibility(student)
        self.assertEqual(expected_output, actual_output)

    """ Test case: a, c, d, f, l, s"""

    def test_case2(self):
        student = student_class.Student(25, 0, 0, 0, 0, 0)
        expected_output = 0
        actual_output = scholarship_eligibility.determine_eligibility(student)
        self.assertEqual(expected_output, actual_output)

    """ Test case: a, c, e, g, i, l, s"""

    def test_case3(self):
        student = student_class.Student(20, 1, 0, 0, 0, 0)
        expected_output = 0
        actual_output = scholarship_eligibility.determine_eligibility(student)
        self.assertEqual(expected_output, actual_output)

    """ Test case: a, c, e, g, j, k, m, p, q, s"""

    def test_case5(self):
        student = student_class.Student(21, 0, 2, 5, 0, 10000)
        expected_output = 0
        actual_output = scholarship_eligibility.determine_eligibility(student)
        self.assertEqual(expected_output, actual_output)


class TestRedirectedStudents(unittest.TestCase):
    """These tests focus on students who are to be redirected to the dean."""

    """ Test case: a, c, e, h, k, m, o"""

    def test_case4(self):
        student = student_class.Student(22, 3, 4, 0, 0, 1000)
        expected_output = "Dean for consideration"
        actual_output = scholarship_eligibility.determine_eligibility(student)
        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
