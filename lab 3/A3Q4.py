#Objective No.- 4
#Write a Python program Stack Simulation Using Memory


stack=[0]*5
TOP=-1
def push(v):
    global TOP
    if TOP<4:
        TOP+=1
        stack[TOP]=v
    else:
        print("Stack Overflow")
def pop():
    global TOP
    if TOP>=0:
        print("Popped",stack[TOP])
        TOP-=1
    else:
        print("Stack Underflow")
while True:
    print("1.Push 2.Pop 3.Peek 4.Display 5.Exit")
    ch=int(input())
    if ch==1:
        val=int(input("Value: "))
        push(val)
    elif ch==2:
        pop()
    elif ch==3:
        if TOP>=0:
            print(stack[TOP])
        else:
            print("Empty")
    elif ch==4:
        print(stack)
    else:
        break


    
