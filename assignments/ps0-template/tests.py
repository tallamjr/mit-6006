import unittest
from count_long_subarray import count_long_subarray

tests = (
    (
        (2, 2, 4, 1, 4),
        2,
    ),
    (
        (7, 8, 5, 7, 7, 3, 2, 8),
        3,
    ),
    (
        (7, 7, 9, 1, 2, 11, 9, 6, 2, 8, 9),
        2,
    ),
    (
        (4, 18, 10, 8, 13, 16, 18, 1, 9, 6, 11, 13, 12, 5, 7, 17, 13, 3),
        1,
    ),
    (
        (11, 16, 10, 19, 20, 18, 3, 19, 2, 1, 8, 17, 7, 13, 1, 11, 1, 18, 19, 9, 7, 19, 24, 2, 12),
        4,
    ),
)

def check(test):
    A, staff_sol = test
    student_sol = count_long_subarray(A)
    return staff_sol == student_sol

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
