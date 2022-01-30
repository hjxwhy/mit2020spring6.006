from collections import namedtuple


def direct_access_sort(A):
    u = 1 + max([x.key for x in A])
    D = [None] * u
    for x in A:
        D[x.key] = x
    i = 0
    for key in range(u):
        if D[key] is not None:
            A[i] = D[key]
            i += 1


def tuple_sort(A):
    key_tuples = []
    n = len(A)
    for a in A:
        key_tuple = divmod(a, n)
        key_tuples.append(key_tuple)
    keys = [str(t[0]) + str(t[1]) for t in key_tuples]
    keys = sorted(keys, key=lambda x: x[-1])
    keys = sorted(keys, key=lambda x: x[0])
    print(keys)


A = [17, 3, 24, 22, 12]


# tuple_sort(A)


# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.

def countingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


# Method to do Radix Sort
def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 1:
        countingSort(arr, exp)
        exp *= 10


# Driver code
arr = [170, 45, 75, 90, 802, 24, 2, 66]

# Function Call
radixSort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")


