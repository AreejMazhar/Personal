def BubbleSortingASC(SortArray):
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

def BubbleSortingDESC(SortArray):
    Maxsize = len(SortArray)
    Swap = False

    while (Swap == False):
        Swap=True
        for i in range(0,Maxsize-1):
            if SortArray[i] < SortArray[i + 1]:
                Temp = SortArray[i]
                SortArray[i] = SortArray[i+1]
                SortArray[i+1] = Temp
                Swap = False

        Maxsize = (Maxsize - 1)
    return (SortArray)

Tosort = []
print("Hello user! Welcome to the bubble sort program.")
n= int(input("Please enter the size of your list: "))

choice1 = input("Would you like to sort (N)umbers or (W)ords?")
if choice1 == "N" or choice1 == "n":
    for i in range(0, n):
        print("Enter the number at the index", i, ": ")
        num = int(input())
        Tosort.append(num)
elif choice1 == "W" or choice1 == "w":
    for i in range(0, n):
        print("Enter the word at the index", i, ": ")
        word = input()
        Tosort.append(word)

print ("Your current list is: ", Tosort)

choice2 = input("Would you like to sort in (asc)ending or (desc)ending order?")
if choice2 == "asc":
    BubbleSortingASC(Tosort)
elif choice2 == "desc":
    BubbleSortingDESC(Tosort)

sortedresult = Tosort
print("Here is your sorted list: ")
print(sortedresult)
