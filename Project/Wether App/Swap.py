list=[1,2,3,5,6,4]
print(list)
pos1=int(input("Enter index: "))
pos2=int(input("Enter index: "))

list[pos1],list[pos2]=list[pos2],list[pos1]

print(list)



