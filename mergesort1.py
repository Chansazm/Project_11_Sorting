def mergesort(dataset):
    
    #Divide the array
    if len(dataset) > 1:
        mid = len(dataset)//2
        leftarray = dataset[:mid]
        rightarray = dataset[mid:]

    # Conquer Recursively on each half

    mergesort(leftarray)
    mergesort(rightarray)
    # Merge the arrays
    i = 0
    j = 0
    k = 0
    
    while i < len(leftarray) and j < len(rightarray):
        if leftarray[i] > rightarray[j]:
            dataset[k] = leftarray[i]
            i += 1
        
        else: 
            leftarray[i] < rightarray[j]
            dataset[k] = leftarray[i]
            i += 1
        k += 1

# TODO: if left array still has values
        while i < len(leftarray):
            dataset[k] = leftarray[i]
            i += 1
            k += 1

# TODO: if right array still has values

        while j < len(rightarray):
            dataset[k] = rightarray[j]
            j += 1
            k += 1
items = [1, 5, 9, 7, 3, 2, 1, 9, 8, 3, 7]
mergesort(items)
print(items)
        
        
