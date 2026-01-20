#Name- Amrendra Kumar
#Regd. No.- 24E111B52
#Objective No.- 1(b)

mem=[0]*16
pc=0
mem[0]=0b00010000001010
mem[1]=0b00100000000111
mem[2]=0b01100000001001
mem[3]=0b01111100000000
mem[7]=8

def fetch(memory):
    global pc
    mar=pc
    pc+=1
    mbr=memory[mar]
    ir=mbr
    cu=ir>>8
    address=ir&0xFF
    print("\n=== Instruction Cycle ===")
    print(f"[FETCH] PC={pc-1}, MAR={mar}, MBR={mbr}, IR={ir}")
    return cu,address

opCode,address=fetch(mem)
print('[DECODE] PC=',pc-1,'op-code =',opCode,'Operand =',address)

opCode,address=fetch(mem)
print('[DECODE] PC=',pc-1,'op-code =',opCode,'Operand =',address)

opCode,address=fetch(mem)
print('[DECODE] PC=',pc-1,'op-code =',opCode,'Operand =',address)

opCode,address=fetch(mem)
print('[DECODE] PC=',pc-1,'op-code =',opCode,'Operand =',address)





