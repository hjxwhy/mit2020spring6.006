from lecture2.data_structures import ArraySeq


def selection_sort(A):
    for i in range(len(A) - 1, 0, -1):
        m = i
        for j in range(i):
            if A[m] < A[j]:
                m = j
        A[m], A[i] = A[i], A[m]


def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            A[j - 1], A[j] = A[j], A[j - 1]
            j = j - 1


def merge_sort(A, a, b=None):
    if b is None:
        b = len(A)
    if b - a > 1:
        c = (a + b + 1) // 2
        merge_sort(A, a, c)
        merge_sort(A, c, b)
        L, R = A[a:c], A[c:b]
        i, j = 0, 0
        while a < b:
            if (j >= len(R)) or (i < len(L)) and L[i] < R[j]:
                A[a] = L[i]
                i += 1
            else:
                A[a] = R[j]
                j += 1
            a += 1


class Sorted_Array_Set:
    '''
    sorted array set put the smallest number in the position of 0, and the largest number was put in the last position
    '''

    def __init__(self):
        self.A = ArraySeq()

    def __len__(self):
        return len(self.A)

    def __iter__(self):
        yield from self.A

    def iter_order(self):
        yield from self

    def build(self, X):
        self.A.build(X)
        self._sort()

    def _sort(self):
        merge_sort(self.A.A, 0, len(self))

    def _binary_search(self, k, i, j):
        if i >= j: return i
        m = (i + j) // 2
        x = self.A.get_at(m)
        if x.key > k: return self._binary_search(k, i, m - 1)
        if x.key < k: return self._binary_search(k, m + 1, j)
        return m

    def find_min(self):
        if len(self) > 0:
            return self.A.get_at(0)
        else:
            return None

    def find_max(self):
        if len(self) > 0:
            return self.A.get_at(len(self) - 1)
        else:
            return None

    def find(self, k):
        if len(self) == 0: return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key == k:
            return x
        else:
            return None

    def find_next(self, k):
        if len(self) == 0: return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key > x: return x
        if (i + 1) < len(self): return self.A.get_at(i + 1)

    def find_prev(self, k):
        if len(self) == 0: return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key < x: return x
        if (i - 1) > 0: return self.A.get_at(i - 1)

    def insert(self, x):
        if len(self) == 0: self.A.insert_first(x)
        i = self._binary_search(x.key, 0, len(self) - 1)
        k = self.A.get_at(i).key
        if k == x.key:
            self.A.set_at(k, x)  # recover the source data
            return False
        if x.key < k:
            self.A.insert_at(i, x)
        else:
            self.A.insert_at(i + 1, x)
        return True

    def delete(self, k):
        i = self._binary_search(k, 0, len(self.A) - 1)
        assert k == self.A.get_at(i).key
        return self.A.delete_at(i)


if __name__=='__main__':
    sas= Sorted_Array_Set()
    s = {'a':1, 'l':2, 'g':3, 's':4}
    sas.build(s)
    print(sas.A.A)
