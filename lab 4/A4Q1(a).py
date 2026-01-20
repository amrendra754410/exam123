#Name- Amrendra Kumar
#Regd. No.- 24E111B52
#Objective No.- 1(a)

memory={0:"LDRL 10",1:"ADD 7",2:"STORE 9",3:"STOP"}
PC=0
MAR=0
MDR=""
IR=""

while True:
    print("\n=== Instruction Cycle ===")
    MAR=PC
    MDR=memory[MAR]
    IR=MDR
    PC+=1
    print(f"[FETCH] PC={PC-1}, MAR={MAR}, MDR={MDR}, IR={IR}")

    parts=IR.split()
    opcode=parts[0]
    operand=parts[1] if len(parts)>1 else None
    print(f"[DECODE] Opcode={opcode}, Operand={operand}")

    if opcode=="STOP":
        print("\nHALT instruction fetched. Stopping simulation.")
        break


