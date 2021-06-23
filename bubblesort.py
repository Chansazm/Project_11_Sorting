def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


# Driver function
numbers = [1, 8, 5, 7]
bubble_sort(numbers)
print(numbers)
