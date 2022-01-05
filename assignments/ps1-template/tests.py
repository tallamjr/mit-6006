import unittest
from Doubly_Linked_List_Seq  import Doubly_Linked_List_Seq

# Change to True to visualize output
verbose = False

tests = (
    (
        [('insert_last', 3), ('insert_first', 2), ('insert_last', 8), ('insert_first', 2), ('insert_last', 9), ('insert_first', 7), ('delete_last',), ('delete_last',), ('delete_first',), ('splice/remove', 1, 2), ('splice/remove', 1, 2), ('splice/remove', 1, 2), ('splice/remove', 1, 2), ('splice/remove', 1, 2)],
        [9, 8, 7, (2, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3)],
    ),
    (
        [('insert_first', 11), ('insert_first', 7), ('insert_first', 11), ('insert_last', 10), ('insert_first', 18), ('insert_first', 9), ('insert_last', 5), ('insert_first', 25), ('insert_first', 11), ('insert_first', 12), ('delete_first',), ('delete_first',), ('delete_last',), ('delete_last',), ('delete_first',), ('splice/remove', 2, 2), ('splice/remove', 3, 2), ('splice/remove', 1, 2), ('splice/remove', 1, 2), ('splice/remove', 1, 2)],
        [12, 11, 5, 10, 25, (9, 18, 0, 1, 0, 1, 0, 1, 11, 0, 0, 1, 1, 7, 11)],
    ),
    (
        [('insert_first', 39), ('insert_first', 59), ('insert_last', 59), ('insert_first', 52), ('insert_first', 21), ('insert_last', 53), ('insert_first', 61), ('insert_first', 58), ('insert_last', 49), ('insert_last', 30), ('insert_last', 19), ('insert_first', 25), ('insert_first', 59), ('insert_last', 33), ('insert_first', 33), ('insert_last', 42), ('delete_last',), ('delete_last',), ('delete_first',), ('delete_last',), ('delete_first',), ('delete_first',), ('delete_last',), ('delete_last',), ('splice/remove', 2, 4), ('splice/remove', 5, 4), ('splice/remove', 6, 4), ('splice/remove', 1, 4), ('splice/remove', 6, 4)],
        [42, 33, 33, 19, 59, 25, 30, 49, (58, 61, 0, 1, 2, 3, 21, 0, 1, 2, 3, 0, 1, 2, 0, 0, 1, 2, 3, 1, 2, 3, 3, 52, 59, 39, 59, 53)],
    ),
    (
        [('insert_first', 64), ('insert_last', 45), ('insert_last', 10), ('insert_first', 70), ('insert_last', 25), ('insert_first', 48), ('insert_first', 26), ('insert_last', 27), ('insert_last', 96), ('insert_last', 90), ('insert_last', 64), ('insert_last', 8), ('insert_first', 65), ('insert_first', 34), ('insert_last', 20), ('insert_last', 31), ('insert_last', 84), ('insert_last', 76), ('insert_last', 73), ('insert_last', 39), ('delete_first',), ('delete_last',), ('delete_last',), ('delete_first',), ('delete_last',), ('delete_first',), ('delete_last',), ('delete_first',), ('delete_first',), ('delete_last',), ('splice/remove', 4, 5), ('splice/remove', 2, 5), ('splice/remove', 7, 5), ('splice/remove', 7, 5), ('splice/remove', 4, 5)],
        [34, 39, 73, 65, 76, 26, 84, 48, 70, 31, (64, 45, 10, 0, 1, 0, 1, 2, 3, 4, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 25, 27, 0, 1, 2, 3, 4, 96, 90, 64, 8, 20)],
    ),
    (
        [('insert_last', 105), ('insert_first', 105), ('insert_first', 142), ('insert_last', 130), ('insert_last', 83), ('insert_last', 75), ('insert_last', 78), ('insert_last', 83), ('insert_last', 82), ('insert_first', 49), ('insert_first', 117), ('insert_last', 75), ('insert_last', 122), ('insert_first', 99), ('insert_first', 14), ('insert_last', 6), ('insert_first', 17), ('insert_last', 103), ('insert_last', 101), ('insert_last', 142), ('insert_last', 62), ('insert_last', 85), ('insert_first', 47), ('insert_last', 82), ('delete_first',), ('delete_first',), ('delete_last',), ('delete_last',), ('delete_first',), ('delete_first',), ('delete_last',), ('delete_last',), ('delete_first',), ('delete_first',), ('delete_last',), ('delete_first',), ('splice/remove', 6, 6), ('splice/remove', 9, 6), ('splice/remove', 10, 6), ('splice/remove', 8, 6), ('splice/remove', 2, 6)],
        [47, 17, 82, 85, 14, 99, 62, 142, 117, 49, 101, 142, (105, 105, 130, 0, 1, 2, 3, 4, 5, 83, 75, 78, 83, 0, 1, 0, 1, 2, 3, 4, 5, 2, 0, 0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 3, 4, 5, 82, 75, 122, 6, 103)],
    ),
)

def run_test(ops):
    DS = Doubly_Linked_List_Seq()
    ans = []
    if verbose:
        print(DS)
    for op in ops:
        if verbose:
            print(*op)
        if op[0] == "insert_first":
            x = op[1]
            DS.insert_first(x)
        if op[0] == "insert_last":
            x = op[1]
            DS.insert_last(x)
        if op[0] == "delete_first":
            ans.append(DS.delete_first())
        if op[0] == "delete_last":
            ans.append(DS.delete_last())
        if (op[0] == "splice/remove") and DS.head:
            i, n = op[1], op[2]
            L = Doubly_Linked_List_Seq()
            L.build(range(n))
            if verbose:
                print('L: ', L)
            x1 = DS.head.later_node(i)
            x2 = x1.next
            DS.splice(x1, L)
            assert x2 != None
            for _ in range(n):
                L = DS.remove(x1.next, x2.prev)
                x2 = x1.next
                DS.splice(x1, L)
        if verbose:
            print(DS)
    ans.append(tuple([x for x in DS]))
    return ans

def check(test):
    ops, staff_sol = test
    student_sol = run_test(ops)
    n1 = len(staff_sol)
    n2 = len(student_sol)
    if n1 != n2: return False
    for i in range(n1):
        if staff_sol[i] != student_sol[i]: return False
    return True

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
