max=int(input("enter size of st"))
s=[]
def popd():
    if(len(s)==0):
        print("no elments  ")

    else:
        print( f"popped item is {s.pop()}")
def push():
    if(len(s)>max-1):
        print("overflow")
    else:
        b=int(input("enter element to insert  " ))
        s.append(b)
       
def disp():
    if(len(s)==0):
        print("no elments")
    else:
         print("elments of stack are")
         s.sort(reverse=True)
         for i in s:
             print(f"{i}")
while(1):
    print("1.insert 2. delete 3.display any other ")
    ch=int(input("enter your choice  "))
    match(ch):
        case 1: push()
        case 2:popd()
        case 3:disp()
        case _:exit(0)