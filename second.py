a = int(input("Enter A: "))
b = int(input("Enter B: "))

print("1)+")
print("2)-")
print("3)*")
print("4)/")
print("6)%")
print("7)//")

case = int(input("Enter your case: "))

def swith():
    if case == 1:
        print(a+b)
    elif case == 2:
        print(a-b)
    elif case == 3:
        print(a*b)
    elif case == 4:
        print(a/b)
    elif case == 5:
        print(a%b)
    else :
        print(a//b)
    
swith()        