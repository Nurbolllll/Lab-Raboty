# test_main.py

import unittest
from main import calculate_average, determine_grade_letter, student_report

class TestGrades(unittest.TestCase):

    def test_calculate_average(self):
        self.assertEqual(calculate_average([100, 80, 90]), 90)
        self.assertEqual(calculate_average([]), 0)
        self.assertAlmostEqual(calculate_average([1, 2, 3]), 2)

    def test_determine_grade_letter(self):
        self.assertEqual(determine_grade_letter(95), 'A')
        self.assertEqual(determine_grade_letter(85), 'B')
        self.assertEqual(determine_grade_letter(75), 'C')
        self.assertEqual(determine_grade_letter(65), 'D')
        self.assertEqual(determine_grade_letter(40), 'F')

    def test_student_report(self):
        report = student_report("Ivan", [100, 80, 90])
        self.assertIn("Ivan", report)
        self.assertIn("90.00", report)
        self.assertIn("A", report)


if __name__ == '__main__':
    unittest.main()
