
iNumList = []

while 1 :
    temp = int(input("Please enter number to add in list. Enter 0 to exit loop :"))
    if temp == 0 :
        break
    else:
        iNumList.append(temp)

print(iNumList)

temp = 0

for i in iNumList:
    if i > temp:
        temp = i

print(f"Maximum number from the list is :{temp}")