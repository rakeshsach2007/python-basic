import time

startTime = time.perf_counter()

lUserList = ["apple","mango","apple","banana"]

temp= []

for i in lUserList:
    bFound = False
    for j in temp:
        if j == i:
            #duplicate found
            bFound = True
            print(f"{j} is repeated in org list")

    if not bFound:
        temp.append(i)
    

lUserList = temp

print("Org list:")
print(lUserList)

endTime = time.perf_counter()

print(f"program executed in {endTime-startTime:.6f} seconds")