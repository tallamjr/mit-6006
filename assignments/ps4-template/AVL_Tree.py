def height(A):
    if A:   return A.height
    else:   return -1

class AVL_Node:
    def __init__(A, x):                     # O(1)
        A.item   = x
        A.left   = None
        A.right  = None
        A.parent = None
        A.subtree_update()

    def subtree_update(A):                  # O(1)
        A.height = 1 + max(height(A.left), height(A.right))

    def skew(A):                            # O(1)
        return height(A.right) - height(A.left)

    def subtree_iter(A):                    # O(n)
        if A.left:   yield from A.left.subtree_iter()
        yield A
        if A.right:  yield from A.right.subtree_iter()

    def subtree_first(A):                   # O(log n)
        if A.left:  return A.left.subtree_first()
        else:       return A

    def subtree_last(A):                    # O(log n)
        if A.right: return A.right.subtree_last()
        else:       return A

    def successor(A):                       # O(log n)
        if A.right: return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent

    def predecessor(A):                     # O(log n)
        if A.left:  return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent

    def subtree_insert_before(A, B):        # O(log n)
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left,  B.parent = B, A
        A.maintain()

    def subtree_insert_after(A, B):         # O(log n)
        if A.right:
            A = A.right.subtree_first()
            A.left,  B.parent = B, A
        else:
            A.right, B.parent = B, A
        A.maintain()

    def subtree_delete(A):                 # O(log n)
        if A.left or A.right:
            if A.left:  B = A.predecessor()
            else:       B = A.successor()
            A.item, B.item = B.item, A.item
            return B.subtree_delete()
        if A.parent:
            if A.parent.left is A:  A.parent.left  = None
            else:                   A.parent.right = None
            A.parent.maintain()
        return A

    def subtree_rotate_right(D):            # O(1)
        assert D.left
        B, E = D.left, D.right
        A, C = B.left, B.right
        D, B = B, D
        D.item, B.item = B.item, D.item
        B.left, B.right = A, D
        D.left, D.right = C, E
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()

    def subtree_rotate_left(B):              # O(1)
        assert B.right
        A, D = B.left, B.right
        C, E = D.left, D.right
        B, D = D, B
        B.item, D.item = D.item, B.item
        D.left, D.right = B, E
        B.left, B.right = A, C
        if A: A.parent = B
        if E: E.parent = D              
        B.subtree_update()
        D.subtree_update()

    def rebalance(A):                       # O(1)
        if A.skew() == 2:
            if A.right.skew() < 0:
                A.right.subtree_rotate_right()
            A.subtree_rotate_left()
        elif A.skew() == -2:
            if A.left.skew() > 0:
                A.left.subtree_rotate_left()
            A.subtree_rotate_right()

    def maintain(A):                        # O(log n)
        A.rebalance()
        A.subtree_update()
        if A.parent: A.parent.maintain()

    def __str__(A):                          # O(n log^2 n)
        s = str(A.item)
        SL = str(A.left).split("\n")  if A.left  else [""]
        SR = str(A.right).split("\n") if A.right else [""]
        wl, ws, wr = len(SL[0]), len(s), len(SR[0])
        lpad, spad, rpad = [" " * w for w in (wl, ws, wr)]
        cl, cr = len(SL[0].lstrip(" _")), len(SR[0].rstrip(" _"))
        S = [" "*(wl - cl) + "_"*cl + s + "_"*cr + " "*(wr - cr)]
        for i in range(max(len(SL), len(SR))):
            l = SL[i] if i < len(SL) else lpad
            r = SR[i] if i < len(SR) else rpad
            S.append(l + spad + r)
        return "\n".join(S)

class AVL_Tree:
    def __init__(T, Node_Type):
        T.root = None
        T.size = 0
        T.Node_Type = Node_Type

    def __str__(T): return str(T.root)
    def __len__(T): return T.size
    def __iter__(T): 
        if T.root: 
            for A in T.root.subtree_iter():
                yield A.item
