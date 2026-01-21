#Objective No.- 2
#Write a menu-driven interactive Python program to create, read, and write memory.

memory=[0]*10
while True:
    print("1.Create 2.Read 3.Write 4.Display 5.Exit")
    ch=int(input())
    if ch==1:
        n=int(input("Enter size: "))
        memory=[0]*n
    elif ch==2:
        a=int(input("Address: "))
        print(memory[a])
    elif ch==3:
        a=int(input("Address: "))
        v=int(input("Value: "))
        memory[a]=v
    elif ch==4:
        for i in range(len(memory)):
            print("Address",i,":",memory[i])
    else:
        break



    
