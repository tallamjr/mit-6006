import unittest
from solve_tilt     import solve_tilt, move, board_str

# Change to True to visualize output
verbose = False

tests = (
    (
        (
            (
                ('#', '#', '.', '.', '.'),
                ('.', 'o', '#', '.', '.'),
                ('.', '.', 'o', '.', '.'),
                ('.', '.', '.', '.', '.'),
                ('#', '#', '#', '.', '.'),
            ),
            (4, 3),
        ),
        ('down', 'right')
    ),
    (
        (
            (
                ('.', '.', '.', '.', '.'),
                ('.', '.', 'o', '.', 'o'),
                ('.', '.', '.', '#', '#'),
                ('.', '.', '#', '#', '.'),
                ('.', '.', '#', '.', '#'),
            ),
            (1, 3),
        ),
        ('down', 'left', 'down', 'right')
    ),
    (
        (
            (
                ('.', '.', '.', '.', '.'),
                ('.', '.', '.', '.', '.'),
                ('.', '#', '#', '.', '.'),
                ('#', '.', '.', '.', 'o'),
                ('#', '#', '.', '#', 'o'),
            ),
            (1, 0),
        ),
        ('up', 'left', 'down', 'right', 'up', 'left')
    ),
    (
        (
            (
                ('o', '#', '.', '.', '.'),
                ('.', '#', '.', '.', '.'),
                ('.', '.', '.', '.', '.'),
                ('.', '.', '.', '.', '.'),
                ('o', '.', '#', '.', '.')
            ),
            (2, 2),
        ),
        ('down', 'right', 'up', 'right', 'up', 'left', 'down')
    ),
    (
        (
            (
                ('.', '.', '.', '.', '.', '.', '#'),
                ('.', '.', '.', '.', '.', '#', '.'),
                ('.', '.', '.', '.', '.', '#', '#'),
                ('.', '.', '.', '.', '.', '#', '#'),
                ('.', 'o', 'o', 'o', '.', '.', '.'),
                ('#', '#', '#', '.', '.', '.', '.'),
                ('#', '#', '#', 'o', '.', '.', '.'),
            ),
            (3, 3),
        ),
        ('up', 'left', 'down', 'right', 'up', 'right', 'up', 'left', 'down', 'right')
    ),
)

def check(test):
    (B, t), staff_sol = test
    student_sol = solve_tilt(B, t)
    if len(staff_sol) != len(student_sol):
        return False
    if verbose: 
        print('\n\n' + board_str(B))
    for d in student_sol:
        B = move(B, d)
        if verbose: 
            print('Move %s\n%s' % (d, board_str(B)))
    if verbose:
        print('target %s\n' % str(t))
    x, y = t
    return B[y][x] == 'o'

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
