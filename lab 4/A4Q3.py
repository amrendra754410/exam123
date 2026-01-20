#Name- Amrendra Kumar
#Regd. No.- 24E111B52
#Objective No.- 3

mem=[0]*12
pc=0
mem[0]=0b000100000001
mem[1]=0b001100000011
mem[2]=0b010000000110
mem[3]=0b011100000000
mem[6]=0b111100000000
mem[7]=9
def fetch(memory):
    global pc
    ir=memory[pc]
    pc+=1
    return (ir>>8),(ir&0xFF)

z=0
run=1
r0=0

while run==1:
    pcOld=pc
    opCode,address=fetch(mem)

    if opCode==0b1111:
        run=0

    elif opCode==0b0001:
        r0=address

    elif opCode==0b0010:
        r0=r0+mem[address]

    elif opCode==0b0011:
        r0=r0-mem[address]
        if r0==0: z=1
        else: z=0

    elif opCode==0b0100:
        if z==1: pc=address

    print('pc =',pcOld,'opCode =',opCode,'Register r0 =',r0,'z =',z)

    
