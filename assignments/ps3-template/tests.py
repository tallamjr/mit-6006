import unittest
from count_anagram_substrings   import count_anagram_substrings

tests = (
    (
        (
            'esleastealaslatet',
            ('tesla',),
        ),
        (3,),
    ),
    (
        (
            'lrldrrrllddrrlllrddd',
            ('ldl', 'rld'),
        ),
        (1, 3),
    ),
    (
        (
            'kkkkkvvuvkvkkkvuuvkuukkuvvkukkvkkvuvukuk',
            ('vkuk', 'uvku', 'kukk'),
        ),
        (5, 6, 1),
    ),
    (
        (
            'trhtrthtrthhhrtthrtrhhhtrrrhhrthrrrttrrttrthhrrrrtrtthhhhrrrtrtthrttthrthhthrhrh',
            ('rrrht', 'tttrr', 'rttrr', 'rhrrr'),
        ),
        (6, 5, 6, 1),
    ),
    (
        (
            'hjjijjhhhihhjjhjjhijjihjjihijiiihhihjjjihjjiijjijjhhjijjiijhjihiijjiiiijhihihhiihhiiihhiijhhhiijhijj',
            ('jihjhj', 'hhjiii', 'ihjhhh', 'jjjiji'),
        ),
        (10, 6, 2, 2),
    ),
)

def check(test):
    args, staff_sol = test
    student_sol = count_anagram_substrings(*args)
    return staff_sol == student_sol

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
