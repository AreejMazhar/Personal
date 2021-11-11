def BubbleSorting(SortArray):
    Maxsize = len(SortArray)
    Swap = False

    while (Swap == False):
        Swap=True
        for i in range(0,Maxsize-1):
            if SortArray[i] > SortArray[i + 1]:
                Temp = SortArray[i]
                SortArray[i] = SortArray[i+1]
                SortArray[i+1] = Temp
                Swap = False

        Maxsize = (Maxsize - 1)
    return (SortArray)

Tosort = []
print("Hello user! Welcome to the bubble sort program.")
n = int(input("Please enter the size of your list: "))

for i in range(0, n):
    print("Enter the number at the index", i, ": ")
    num = int(input())
    Tosort.append(num)

print("Your current list is ", Tosort)

BubbleSorting(Tosort)

sortedresult = ToSort
print("Here is your sorted list in ascending order:")
print(sortedresult)
