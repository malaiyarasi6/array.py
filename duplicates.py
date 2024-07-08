def IntersecOfSets(arr1, arr2, arr3):
    result = []
    for i in arr1:
        if i in arr2 and i in arr3:
            result.append(i)
    print(list(set(result)))
     
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
 
common = IntersecOfSets(arr1, arr2, arr3)