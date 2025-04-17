max=int(input("enter size que"))
d=0
s=[]
def cins():
    global d
    if(d>max-1):
        print("full")
    else:
        c=int(input("enter elemnte"))
        s.append(c)
        c+=1
        d+=1
def cpop():
    global d
    if(d==0):
        print(" no elments")
    else:
        i=0
        print(f"elment poped is {s[i]}")
        del s[i]
        d-=1
def disp():
    if(d==0):
        print("no elments")
    else:
         print("contemts are")
         for i in s:
             print(f" {i}")
while(1):
    print("1.insert 2. delete 3.display any other ")
    ch=int(input("enter your choice  "))
    match(ch):
        case 1: cins()
        case 2:cpop()
        case 3:disp()
        case _:exit(0)