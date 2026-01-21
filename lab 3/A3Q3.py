#Objective No.- 3
#Write a Python program for the Memory Simulator with Arithmetic Operations

memory=[0]*6
memory[0]=int(input("Enter value at memory[0]: "))
memory[1]=int(input("Enter value at memory[1]: "))
memory[2]=memory[0]+memory[1]
memory[3]=memory[0]-memory[1]
memory[4]=memory[0]*memory[1]
memory[5]=memory[0]/memory[1]
print(memory)


