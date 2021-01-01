

def selection_sort(numbers):

    for i in range(len(numbers)):
        minposition = i
        for j in range(len(numbers)):
            if numbers[j] > numbers[minposition]:
                minposition = j


                
                temp = numbers[i]
                numbers[i]= numbers[minposition]
                numbers[minposition] = temp
                
                #print(numbers)


numbers = [1,5,9,7,3,2,1,9,8,3,7]
selection_sort(numbers)





            
