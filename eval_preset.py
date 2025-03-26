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
    prev_2=""
    repeats=[]
    markdown=False
    for x in range(0, len(instruct)):
        if instruct[x].isnumeric():
            temp=int(instruct[x])
            if prev=="repeat":
                times=int(instruct[x])
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
        if instruct[x]=="[":
            markdown=True
        if instruct[x]=="]":
            markdown=False
            for y in range(1,times):
                for z in range(0, len(repeats)):
                    if repeats[z].isnumeric():
                        temp=int(repeats[z])
                        if prev_2=="forward":
                            t.forward(temp)
                        elif prev_2=="left":
                            t.left(temp)
                        elif prev_2=="right":
                            t.right(temp)
                        elif prev_2=="backward":
                            t.backward(temp)
                        elif prev_2.isnumeric():
                            print("PARSER ERROR: Invalid input. Type 'num' cannot be followed by type 'num'")
                        else:
                            print("PARSER ERROR: Invalid input. Invalid command")
                    prev_2=repeats[z]
            repeats=[]
        if markdown and not (instruct[x]=="[" or instruct[x]=="]"):
            repeats.append(instruct[x])
        prev=instruct[x]
