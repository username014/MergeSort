def merge_sort(l):
    if len(l) < 2:
        return l
    arr = l
    result = []
    i, j = 0, 0
    if len(arr)%2==0:
        while i < len(arr)//2 and j < len(arr)//2:
            if i >= len(arr)//2 or arr[i] >= arr[j]:
                result.append(arr[j])
                j += 1
            elif j >= len(arr)//2 or arr[i] < arr[j]:
                result.append(arr[i])
                i += 1
        return result
    else:
        while i < len(arr) // 2 and j < len(arr) // 2 + 1:
            if i >= len(arr) // 2 or arr[i] >= arr[j]:
                result.append(arr[j])
                j += 1
            elif j >= len(arr) // 2 + 1 or arr[i] < arr[j]:
                result.append(arr[i])
                i += 1
        return result

arr = [1, 2]
print(merge_sort(arr))