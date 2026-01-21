#Objective 1
# Design a CPU interpreter in python that interprets the data transfer instructio/n

# Simple CPU instruction interpreter. Direct instruction interpretation.

# Class 0: no operand NOP
# Class 1: register,literal LDRL r2,1
# Class 2: register,register, MOV r1,r2
# Class 3: register,[register] LDRI r1,[r2]

sFile = ['LDRL r2,1','LDRL r0,4','NOP','STRI r0,[r2]','LDRI r3,[r2]', 'MOV r1,r2','STOP'] # Source program for testing

codes = {'NOP':[0],'STOP':[0],'LDRL':[1],'MOV':[2],'LDRI':[3],'STRI':[3]}
reg1 = {'r0':0,'r1':1,'r2':2,'r3':3}                    # Legal registers
reg2 = {'[r0]':0,'[r1]':1,'[r2]':2,'[r3]':3}            # Legal pointer registers
r = [0] * 4                                             # Four registers
r[0],r[1],r[2],r[3] = 1,2,3,4                           # Preset registers for testing
m = [0] * 8                                             # Eight memory locations
pc = 0                                                  # Program counter initialize to 0
go = 1                                                  # go is the run control (1 to run)
z = 0                                                   # z is the zero flag. Set/cleared by SUB, DEC, CMP
while go == 1:                                          # Repeat execute fetch and execute loop
    thisLine = sFile[pc]                                # Get current instruction
    pc = pc + 1                                         # Increment pc
    pcOld = pc                                          # Remember pc value for this cycle
    temp = thisLine.replace(',',' ')                    # Remove commas: ADD r1,r2,r3 to ADD r1 r2 r3
    print(temp)
    tokens = temp.split(' ')                            # Tokenize:  ADD r1 r2 r3 to ['ADD','r1','r2','r3']
    mnemonic = tokens[0]                                # Extract first token, the mnemonic
    opClass = codes[mnemonic][0]                        # Extract instruction class
    print(f'opcode Class:{opClass}')
    # Process the current instruction and analyze it
    rD,rDval,rS1,rS1val,rS2,rS2val,lit,rPnt,rPntV = 0,0,0,0,0,0,0,0,0  # Clear all parameters
    if opClass in [0]: pass                                            # If class 0, nothing to be done (simple opcode only)
    if opClass in [1,2,3]:                                             # Look for ops with destination register rD
        rD = reg1[tokens[1]]                                           # Get token 1 and use it to get register number as rD
        print(f'Destination Register:{rD}')
        rDval = r[rD]                                                  # Get contents of register rD
    if opClass in [1]:                                                 # Look at instructions with first source register rS1
        lit = int(tokens[-1])                                          # Get the literal
        print(f'literal is:{lit}')
    if opClass in [2]:                                                 # If class 6, it's got three registers. Extract rS2
        rS1 = reg1[tokens[2]]                                          # Get rS1 register number and then contents
        print(rS1)
        rS1val = r[rS1]
    if opClass in [3]:                                                 # Class 7 involves register indirect addressing
        rPnt = reg2[tokens[2]]                                         # Get the pointer (register) and value of the pointer
        rPntV = r[rPnt]                                                # Get the register number
    if mnemonic == 'STOP':                                             # Now execute instructions. If STOP, clear go and exit
        go = 0
        print('Program terminated')
    elif mnemonic == 'NOP': pass                                       # NOP does nothing. Just drop to end of loop
    elif mnemonic == 'MOV': r[rD] = rS1val                             # Move, load, and store operations
    elif mnemonic == 'LDRL': r[rD] = lit
    elif mnemonic == 'LDRI': r[rD] = m[rPntV]
    elif mnemonic == 'STRI': m[rPntV] = rDval
    regs = ' '.join('%02x' % b for b in r)                             # Format memory locations hex
    mem = ' '.join('%02x' % b for b in m)                              # Format registers hex
    print('pc =','{:<3}'.format(pcOld), '{:<14}'.format(thisLine),'Regs =',regs, 'Mem =',mem, 'z =', z)
    x = input('>>> ')                                                  # Request keyboard input before dealing with next instruction

