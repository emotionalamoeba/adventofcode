ADD = 0x1
MULTIPLY = 0x2
END = 0x63

finished = False
programCounter = 0
program = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,9,23,1,23,5,27,2,6,27,31,1,31,5,35,1,35,5,39,2,39,6,43,2,43,10,47,1,47,6,51,1,51,6,55,2,55,6,59,1,10,59,63,1,5,63,67,2,10,67,71,1,6,71,75,1,5,75,79,1,10,79,83,2,83,10,87,1,87,9,91,1,91,10,95,2,6,95,99,1,5,99,103,1,103,13,107,1,107,10,111,2,9,111,115,1,115,6,119,2,13,119,123,1,123,6,127,1,5,127,131,2,6,131,135,2,6,135,139,1,139,5,143,1,143,10,147,1,147,2,151,1,151,13,0,99,2,0,14,0]

def end():
    global finished
    finished = True

def add(args):
    a = readFromMemoryAddress(args[0])
    b = readFromMemoryAddress(args[1])
    writeToMemoryAddress(args[2], a + b)

def multiply(args):
    a = readFromMemoryAddress(args[0])
    b = readFromMemoryAddress(args[1])
    writeToMemoryAddress(args[2], a * b)

def performOperation(opcode, args):
    return {
        END: lambda args: end(),
        ADD: lambda args: add(args),
        MULTIPLY: lambda args: multiply(args)
    }.get(opcode)(args)

def opcodeArgCount(opcode):
    return {
        MULTIPLY: 3,
        ADD: 3,
        END: 0
    }.get(opcode)
                           
def consumeInt():
    global programCounter
    global program

    value = program[programCounter]
    programCounter +=1
    return value

def readFromMemoryAddress(address):
    global program
    return program[address]

def writeToMemoryAddress(address, value):
    program[address] = value

def extractArguments(argCount):
    args = []

    if argCount is not None:
        for x in range(argCount):
            args.append(consumeInt())

    return args

while not finished:
    opcode = consumeInt()
    argCount = opcodeArgCount(opcode)
    args = extractArguments(argCount)
    performOperation(opcode, args)

print(', '.join(map(str, program)))