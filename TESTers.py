from random import randint
from Quick_sort import quick_sort
from Merge import merge_sort

n = randint(100, 1000)

arr1 = [j for j in range(n)]
arr2 = [2 for j in range(n)]
arr3 = [j for j in range(n-1, 0, -1)]
arr4 = [randint(0, 99) for j in range(n)]

def Qui(arr1, arr2, arr3, arr4):
    assert(quick_sort(arr1, 0, len(arr1)-1)==sorted(arr1))
    assert(quick_sort(arr2, 0, len(arr2)-1)==sorted(arr2))
    assert(quick_sort(arr3, 0, len(arr3)-1)==sorted(arr3))
    assert(quick_sort(arr4, 0, len(arr4)-1)==sorted(arr4))

def Mer(arr1, arr2, arr3, arr4):
    assert(merge_sort(arr1)==sorted(arr1))
    assert(merge_sort(arr2)==sorted(arr2))
    assert(merge_sort(arr3)==sorted(arr3))
    assert(merge_sort(arr4)==sorted(arr4))

Mer(arr1, arr2, arr3, arr4)
Qui(arr1, arr2, arr3, arr4)