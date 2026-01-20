#Name- Rishit Swain
#Regd. No.- 24E119F02
#Objective No.- 6

program=[("LOAD","X"),("ADD","Y"),("STORE","SUM"),("HLT",None)]
memory={"X":5,"Y":10,"SUM":0}
ACC=0
for op,var in program:
    if op=="LOAD":
        ACC=memory[var]
    elif op=="ADD":
        ACC+=memory[var]
    elif op=="STORE":
        memory[var]=ACC
    elif op=="HLT":
        break
print(memory)


