#Name- Amrendra Kumar
#Regd. No.- 24E111B52
#Objective No.- 2(b)

mem=[0]*12
pc=0
mem[0]=0b0001001100
mem[1]=0b0010000111
mem[2]=0b0110001001
mem[3]=0b0111100000
mem[7]=8
def fetch(memory):
    global pc
    if pc<0 or pc>=len(memory):
        raise IndexError(f"PC out of range: PC={pc}, memory size={len(memory)}")
    ir=memory[pc]
    pc+=1
    print(f"\n[FETCH] PC={pc-1}, IR={ir}")
    return (ir>>8),(ir&0xFF)
run=1
r0=0

while run==1:
    try:
        opcode,operand=fetch(mem)
    except IndexError as e:
        print("Fetch error:",e)
        break

    print(f"[DECODE] Opcode={opcode}, Operand={operand}")

    if opcode==0b1111:
        print("[EXECUTE] HALT encountered. Stopping execution.")
        run=0
    elif opcode==0b0001:
        r0=operand
        print(f"[EXECUTE] r0 <- {operand} ({r0})")
    elif opcode==0b0010:
        mar=operand
        if mar<0 or mar>=len(mem):
            print("Memory address out of range:",mar); break
        mbr=mem[mar]
        r0=mbr+r0
        print(f"[EXECUTE] r0 <- r0 + mem[{mar}] ({mbr}) -> {r0}")
    elif opcode==0b0110:
        if operand<0 or operand>=len(mem):
            print("Memory address out of range:",operand); break
        mem[operand]=r0
        print(f"[EXECUTE] mem[{operand}] <- r0 ({r0})")

print("Final mem:",mem)




