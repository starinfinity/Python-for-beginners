def merge(arr1, arr2, len1, len2):


    arr3 = [0]*(len1+len2)
    i = 0
    j = 0
    count = 0
    while i < len1 and j < len2:
        if arr1[i] < arr2[j] :
            arr3[count] = arr1[i]
            count = count + 1
            i = i + 1
        else:
            arr3[count] = arr2[j]
            count = count + 1
            j = j + 1

    while i < len1:
        arr3[count] = arr1[i]
        count = count + 1
        i = i + 1

    while j < len2:
        arr3[count] = arr2[j]
        count = count + 1
        j = j + 1
    print(str(arr3))

arr1 = [2, 5, 7, 9]
arr2 = [1, 3, 5, 8]
len1 = len(arr1)
len2 = len(arr2)
print(merge(arr1, arr2, len1, len2))
