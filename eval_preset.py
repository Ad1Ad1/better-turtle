def eval_preset(t,PRESET,NAME):
    for l in range(0, PRESET[NAME][2]):
        t.forward(PRESET[NAME][1])
        t.left(PRESET[NAME][0])
