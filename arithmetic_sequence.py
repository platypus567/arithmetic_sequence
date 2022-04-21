print("Enter your first number and your last number and the ratio: ")
firstnum = input("First Num: \n")
secondnum = input("Second Num: \n")
ratio = input("Ratio: \n")
between = (secondnum - firstnum)
finalnum = 0

def sum():
    finalnum = firstnum
    adding = 0
    for num in range(between + 1):
        adding += ratio
        finalnum += adding
        print(finalnum-1)



sum()
