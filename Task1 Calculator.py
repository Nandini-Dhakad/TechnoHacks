"Nandini Dhakad"
"TechnoHacks"
"Task 1 : Calculator"

def add():
    a = int(input("enter a="))
    b = int(input("enter b="))
    return a+b

def sub():
    a = int(input("enter a="))
    b = int(input("enter b="))
    return a-b

def mul():
    a = int(input("enter a="))
    b = int(input("enter b="))
    return a*b

def div():
    a = int(input("enter a="))
    b = int(input("enter b="))
    return a/b

print("Enter your choice: +,-,*,/")
i=input("calculate=")
if i=="+":
    print(add())
elif i=="-":
    print(sub())
elif i=="*":
    print(mul())
elif i=="/":
    print(div())
