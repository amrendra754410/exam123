#Name- Amrendra Kumar
#Regd. No.- 24E111B52
#Objective No.- 2(a)
#To implement the Fetch, Decode and Execute cycles of a simple instruction processing
#system using Python
memory={0:"LOAD A",1:"ADD B",2:"STORE C",3:"HALT"}
data={"A":28,"B":8,"C":9}

PC=0
MAR=0
MDR=""
IR=""
ACC=0

while True:
    MAR=PC
    MDR=memory[MAR]
    IR=MDR
    PC+=1
    print(f"\n[FETCH] PC={PC-1}, IR={IR}")

    parts=IR.split()
    opcode=parts[0]
    operand=parts[1] if len(parts)>1 else None
    print(f"[DECODE] Opcode={opcode}, Operand={operand}")

    if opcode=="LOAD":
        ACC=data[operand]
        print(f"[EXECUTE] ACC <- {operand} ({ACC})")
    elif opcode=="STORE":
        data[operand]=ACC
        print(f"[EXECUTE] {operand} <- ACC ({ACC})")
    elif opcode=="ADD":
        ACC+=data[operand]
        print(f"[EXECUTE] ACC <- ACC + {operand} ({ACC})")
    elif opcode=="HALT":
        print("[EXECUTE] HALT encountered. Stopping execution.")
        break

print("\nFinal Data Memory:",data)
print("Final ACC:",ACC)


