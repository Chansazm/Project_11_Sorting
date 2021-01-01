# Bubble sort algorithm


def bubble_sort(data):
    # using the array length and then decreamenting
    for i in range(len(data)-1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp


# Test our bubble sort
numbers = [1, 8, 5, 7]
bubble_sort(numbers)
print(numbers)
