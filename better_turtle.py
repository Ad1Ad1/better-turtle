from turtle import *
from eval_preset import eval_preset, advanced_eval
import sys
import math
sys.path.append("./presets/")
from default_presets import AVAILABLE_FILE_PRESETS
a=AVAILABLE_FILE_PRESETS
from user_presets import AVAILABLE_FILE_PRESETS
b=AVAILABLE_FILE_PRESETS
AVAILABLE_FILE_PRESETS=a|b
t=Pen()
t.up()
t.goto(0,-300)
t.down()
def draw_figure(tm,degree=0,repeat_times=0,PRESET=None,PRESET_SHAPE=None,SPEED=10):
    t.speed(SPEED)
    if PRESET==None:
        for x in range(0,repeat_times):
            tm.forward(100)
            tm.left(degree)
    else:
        if PRESET in AVAILABLE_FILE_PRESETS:
            if PRESET_SHAPE in AVAILABLE_FILE_PRESETS[PRESET]:
                advanced_eval(t,AVAILABLE_FILE_PRESETS[PRESET],PRESET_SHAPE)
            else:
                print("PRESET ERROR: No such name in preset")
        else:
            print("PRESET ERROR: INVALID PRESET. No such available preset specified in current preset file.")
def n_gon(tm,n,scale,SPEED=10):
    t.speed(SPEED)
    k=n*math.pi
    for x in range(0,n):
        tm.forward(scale*(100/k))
        tm.left(360/n)
draw_figure(t,PRESET="test",PRESET_SHAPE="test")
