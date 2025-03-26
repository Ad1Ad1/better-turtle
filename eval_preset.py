def eval_preset(t,PRESET,NAME):
    for l in range(0, PRESET[NAME][2]):
        t.forward(PRESET[NAME][1])
        t.left(PRESET[NAME][0])
def advanced_eval(t,PRESET,NAME):
    instruct=PRESET[NAME].split()
    print("List of commands: ")
    print(instruct)
    temp=""
    prev=""
    for x in range(0, len(instruct)):
        if instruct[x].isnumeric():
            temp=int(instruct[x])
            if prev=="forward":
                t.forward(temp)
            elif prev=="left":
                t.left(temp)
            elif prev=="right":
                t.right(temp)
            elif prev=="backward":
                t.backward(temp)
            elif prev.isnumeric():
                print("PARSER ERROR: Invalid input. Type 'num' cannot be followed by type 'num'")
            else:
                print("PARSER ERROR: Invalid input. Invalid command")
        prev=instruct[x]
