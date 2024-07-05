bubbleSort = [12 ,100, 2, 1, 3, 4, 6, 2, 4, 6, 5, 7 ,8, 6, 5,10 , 2, 5 ,6, 7, 14, 150]
bubblesortextra = 0

for i in range((len(bubbleSort)-1)):
    for i in range((len(bubbleSort)-1)):
        if  bubbleSort[i] > bubbleSort[i+1]:
            bubblesortextra = bubbleSort[i]
            bubbleSort[i] = bubbleSort[i+1]
            bubbleSort[i+1] = bubblesortextra

print(bubbleSort)