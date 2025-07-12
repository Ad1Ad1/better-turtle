def eval_preset(t,PRESET,NAME):
    for l in range(0, PRESET[NAME][2]):
        t.forward(PRESET[NAME][1])
        t.left(PRESET[NAME][0])
def advanced_eval(t,PRESET,NAME,Subcommandlvl=0):
    instruct=PRESET[NAME].split()
    print(f"List of commands for program {NAME}. Subcommand level #{Subcommandlvl}: ")
    print(instruct)
    temp=""
    prev=""
    prev_2=""
    repeats=[]
    markdown=False
    isturtle=0
    isturtle2=0
    PASS_TOKENS=["[","]"]
    TOKENS=["forward", "width", "call","[", "]","color","left","right","repeat","backward","beginfill","endfill","up","down"]
    for x in range(0, len(instruct)):
        if instruct[x] not in TOKENS and isturtle==0:
            temp=int(eval(instruct[x]))
            if prev=="repeat":
                times=temp
            elif prev=="forward":
                t.forward(temp)
            elif prev=="left":
                t.left(temp)
            elif prev=="right":
                t.right(temp)
            elif prev=="backward":
                t.backward(temp)
            elif prev=="color":
                t.color(int(instruct[x])/255,int(instruct[x+1])/255,int(instruct[x+2])/255)
                isturtle=3
            elif prev=="width":
                t.width(temp)
            elif prev.isnumeric() and not isturtle>0:
                print("PARSER ERROR: Invalid input. Type 'num' cannot be followed by type 'num'")
            elif prev in PASS_TOKENS:
                pass
            else:
                print("PARSER ERROR: Invalid input. Invalid command")
        elif instruct[x]=="up":
            t.up()
        elif instruct[x]=="down":
            t.down()
        elif instruct[x]=="beginfill":
            t.begin_fill()
        elif instruct[x]=="endfill":
            t.end_fill()
        elif instruct[x]=="call":
            isturtle=2
            advanced_eval(t,PRESET,instruct[x+1],Subcommandlvl+1)
        if instruct[x]=="[":
            markdown=True
        if instruct[x]=="]":
            markdown=False
            for y in range(1,times):
                for z in range(0, len(repeats)):
                    if repeats[z] not in TOKENS and isturtle2==0:
                        temp=int(eval(repeats[z]))
                        if prev_2=="forward":
                            t.forward(temp)
                        elif prev_2=="left":
                            t.left(temp)
                        elif prev_2=="right":
                            t.right(temp)
                        elif prev_2=="backward":
                            t.backward(temp)
                        elif prev_2=="color":
                            t.color(int(repeats[z])/255,int(repeats[z+1])/255,int(repeats[z+2])/255)
                            isturtle2=3
                        elif prev_2.isnumeric():
                            print("PARSER ERROR: Invalid input. Type 'num' cannot be followed by type 'num'")
                        else:
                            print("PARSER ERROR: Invalid input. Invalid command")
                    elif repeats[z]=="up":
                        t.up()
                    elif repeats[z]=="down":
                        t.down()
                    elif repeats[z]=="beginfill":
                        t.begin_fill()
                    elif repeats[z]=="endfill":
                        t.end_fill()
                    elif instruct[x]=="call":
                        isturtle2=2
                        advanced_eval(t,PRESET,repeats[z+1], Subcommandlvl+1)
                    if isturtle2>0:
                        isturtle2=isturtle2-1
                    prev_2=repeats[z]
            repeats=[]
        if markdown and not (instruct[x]=="[" or instruct[x]=="]"):
            repeats.append(instruct[x])
        if isturtle>0:
            isturtle=isturtle-1
        prev=instruct[x]
