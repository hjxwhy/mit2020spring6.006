import random

from lecture2.data_structures import LinkedListSeq, set_from_seq


class DirectAccessArray:
    def __init__(self, u):
        self.A = [None] * u

    def find(self, k):
        return self.A[k]

    def insert(self, x):
        self.A[x.key] = x

    def delete(self, k):
        self.A[k] = None

    def find_next(self, k):
        for i in range(k + 1, len(self.A)):
            if self.A[i] is not None:
                return self.A[i]

    def find_max(self):
        for i in range(len(self.A) - 1, -1, -1):
            if self.A[i] is not None:
                return self.A[i]

    def delete_max(self):
        for i in range(len(self.A) - 1, -1, -1):
            x = self.A[i]
            if self.A[i] is not None:
                self.A[i] = None
                return x


class Hash_Table_Set:
    def __init__(self, r=200):
        self.chain_set = set_from_seq(LinkedListSeq)
        self.A = []
        self.size = 0
        self.r = r
        self.p = 2 ** 31 - 1
        self.a = random.randint(1, self.p - 1)
        self._compute_bounds()
        self._resize(0)

    def __len__(self):
        return self.size

    def __iter__(self):
        for X in self.A:
            yield from X

    def build(self, X):  # O(n)e
        for x in X:
            self.insert(x)

    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = len(self.A) // (self.r * self.r)

    def _hash(self, k, m):
        return ((self.a * k) % self.p) % m

    def _resize(self, n):
        if (self.lower < n < self.upper):
            return
        f = self.r // 100
        if self.r % 100:
            f += 1  # ceil(self.r / 100)

        m = max(n, 1) * f
        A = [self.chain_set() for _ in range(m)]
        for x in self:
            h = self._hash(x.key, m)
            A[h].insert(x)
        self.A = A
        self._compute_bounds()

    def find(self, k):
        h = self._hash(k, len(self.A))
        return self.A[h].find(k)

    def insert(self, x):
        self._resize(self.size + 1)
        h = self._hash(x.key, len(self.A))
        added = self.A[h].insert(x)
        if added:
            self.size += 1
        return added

    def delete(self, k):  # O(1)ae
        assert len(self) > 0
        h = self._hash(k, len(self.A))
        x = self.A[h].delete(k)
        self.size -= 1
        self._resize(self.size)
        return x

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

class Data:
    def __init__(self, data):
        self.key, self.value = data


hash_table = Hash_Table_Set()
s = [Data([1,1])]
hash_table.build(s)
