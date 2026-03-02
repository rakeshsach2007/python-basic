iUserInput = int(input("Please enter a number:"))

#prime number
#1,2,3,5,7,11,13,17,19....

bIsPrime = True

if iUserInput <=1 :
    bIsPrime =  False
else:
    for i in range(2,iUserInput):
        if iUserInput % i == 0:
            bIsPrime = False
            break

if bIsPrime:
    print(f"Enter number {iUserInput} is a prime number")
else:
    print(f"Enter number {iUserInput} is NOT a prime number")