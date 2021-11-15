# Sequence Interface: sequence maintain a collection of items in an extrinsic order (such as fist, second, last),
# where each item stored has a rank in the sequence.

class ArraySeq:
    '''
    fix size of chunk, if you need to insert or delete an item, the array need to reallocate memory chunk so it need O(n)
    time, but set or get an item need O(1)
    '''

    def __init__(self):
        self.A = []
        self.size = 0

    def build(self, X):
        self.A = [a for a in X]  # O(n)
        self.size = len(self.A)

    def __len__(self):
        return self.size

    def __iter__(self):
        yield from self.A

    def get_at(self, i):
        return self.A[i]

    def set_at(self, i, x):
        self.A[i] = x

    def _copy_forward(self, i, n, A, j):
        '''
        reallocate memory chunk and forward copy element
        :param i: begin element of self.A for copy
        :param n: number of element need to copy
        :param A: new memory chunk to store
        :param j: begin element of A for copy
        '''
        for k in range(n):
            A[j + k] = self.A[i + k]

    # inverse like _copy_forward
    def _copy_backward(self, i, n, A, j):
        for k in range(n - 1, -1, -1):
            A[j + k] = self.A[i + k]

    def insert_at(self, i, x):
        n = len(self)
        A = [None] * (n + 1)
        self._copy_forward(0, i, A, 0)
        A[i] = x
        self._copy_forward(i, n - i, A, i + 1)
        self.build(A)

    def delete_at(self, i):
        n = len(self)
        A = [None] * (n - 1)
        self._copy_forward(0, i, A, 0)
        x = self.A[i]
        self._copy_forward(i + 1, n - i - 1, A, i)
        return x

    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        return self.delete_at(0)

    def insert_last(self, x):
        self.insert_at(len(self), x)

    def delete_last(self):
        return self.delete_at(len(self) - 1)


class ListNode:
    def __init__(self, x):
        self.item = x
        self.next = None

    def later_node(self, i):
        if i == 0:
            return self
        assert self.next
        # recursive
        return self.next.later_node(i - 1)


class LinkedListSeq:
    def __init__(self):
        # this head may have a little different from C++ list head,
        # as my knowledge, C++ list head is a None pointer to the fist element,
        # this head is the head as the name, new node insert fist head.
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, X):
        for x in reversed(X):
            self.insert_fist(x)

    def insert_fist(self, x):
        new_node = ListNode(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def get_at(self, i):
        node = self.head.later_node(i)
        return node

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def delete_fist(self):
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x

    def insert_at(self, i, x):
        if i == 0:
            self.insert_fist(x)
            return
        new_node = ListNode(x)
        node = self.head.later_node(i - 1)
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def delete_at(self, i):
        if i == 0:
            return self.delete_fist()
        node = self.head.later_node(i - 1)
        x = node.next.item
        node.next = node.next.next
        self.size -= 1
        return x

    def delete_last(self):
        return self.delete_at(len(self) - 1)

    def insert_last(self, x):
        self.insert_at(len(self), x)


class DynamicArraySeq(ArraySeq):
    def __init__(self, r=2):
        super().__init__()
        self.size = 0
        self.r = r
        self._compute_bounds()
        self._resize(0)

    def __len__(self):
        return self.size

    def __iter__(self):
        for i in range(len(self)):
            yield self.A[i]

    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = len(self.A) // (self.r * self.r)

    def _copy_forward(self, i, n, A, j):
        '''
        reallocate memory chunk and forward copy element
        :param i: begin element of self.A for copy
        :param n: number of element need to copy
        :param A: new memory chunk to store
        :param j: begin element of A for copy
        '''
        for k in range(n):
            A[j + k] = self.A[i + k]

    # inverse like _copy_forward
    def _copy_backward(self, i, n, A, j):
        for k in range(n - 1, -1, -1):
            A[j + k] = self.A[i + k]

    def _resize(self, n):
        if (self.lower < n < self.upper):
            return
        m = max(n, 1) * self.r
        A = [None] * m
        self._copy_forward(0, self.size, A, 0)
        self.A = A
        self._compute_bounds()

    def insert_last(self, x):
        self._resize(self.size + 1)
        self.A[self.size] = x
        self.size += 1

    def delete_last(self):
        x = self.A[self.size - 1]
        self.size[self - 1] = None
        self.size -= 1
        self._resize(self.size - 1)
        return x

    def insert_at(self, i, x):
        self.insert_last(None)  # amazing method
        self._copy_backward(i, self.size - 1 - i, self.A, i + 1)
        self.A[i] = x

    def delete_at(self, i):
        x = self.A[i]
        self._copy_backward(i + 1, self.size - 1 - i, self.A, i)
        self.delete_last()
        return x

    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        self.delete_at(0)

    def build(self, X):
        for x in X:
            self.insert_last(x)


def set_from_seq(seq):
    class Set_From_Seq:
        def __init__(self):
            self.S = seq()

        def __len__(self):
            return len(self.S)

        def __iter__(self):
            yield from self.S

        def insert(self, x):
            for i in range(len(self.S)):
                if self.S.get_at(i).key == x.key:
                    self.S.set_at(i, x)
                    return
            self.S.insert_last(x)

        def delete(self, k):
            for i in range(len(self.S)):
                if self.S.get_at(i).key == k:
                    return self.S.delete_at(k)

        def find(self, k):
            for x in self:
                if x.key == k: return x
            return None

        def find_min(self):
            out = None
            for x in self:
                if out is None or x.key < out.key:
                    out = x
            return out

        def find_max(self):
            out = None
            for x in self:
                if out is None or x.key > out.key:
                    out = x
            return out

        def find_next(self, k):
            out = None
            for x in self:
                if x.key > k:
                    if (out is None) or x.key < out.key:
                        out = x
            return out


        def find_prev(self, k):
            out = None
            for x in self:
                if x.key < k:
                    if (out is None) or x.key > out.key:
                        out = x
            return out

        def iter_ord(self):
            x = self.find_min()
            while x:
                yield x
                x = self.find_next(x.key)
    return Set_From_Seq



if __name__ == '__main__':
    seq = ArraySeq()
    seq.build([1, 2, 3])
    print(seq.delete_at(0))
    seq.insert_at(3, 4)
    print(seq.A)
