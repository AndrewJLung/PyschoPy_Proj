import time
import sys
import os
import random
from psychopy import visual,event,core,gui

from helper import select_picture, random_emotion

win = visual.Window([900,900],color="gray", units='pix',checkTiming=False)
instruction_left = "Please cover your left eye and name the emotion you see on the screen."
instruction_right = "Please cover your right eye and name the emotion you see on the screen."
instruction = visual.TextStim(win,text=instruction_left, height=20, color="black",pos=[0,-200],autoDraw=True)
feedback_too_slow = visual.TextStim(win,text="Too slow. Press 'a' to continue", height=40, color="black",pos=[0,0])
feedback_received = visual.TextStim(win,text="Feedback received. Press 'a' to continue.", height=40, color="black",pos=[0,0])
valid_response_keys = ['a', 'q']

instruction.draw()
win.flip()
core.wait(5.0)
response_timer = core.Clock() # set response timer clock

while(True):
    r_emotion = random_emotion()
    image_stim = visual.ImageStim(win, ".\\emotions\\" + r_emotion + "\\" + select_picture(r_emotion), size=(100, 100))
    image_stim.draw()
    win.flip()

    response_timer.reset()
    key_pressed = event.waitKeys(keyList=valid_response_keys,maxWait=5)
    rt = round(response_timer.getTime()*1000,0)
    
    print("Response time: %d", rt)

    if not key_pressed:
        feedback_too_slow.draw()
        win.flip()
        core.wait(1.0)
    elif key_pressed[0] == 'q':
        break
    elif key_pressed[0] == 'a':
        feedback_received.draw()
        win.flip()

    key_pressed = event.waitKeys(keyList=valid_response_keys)
    if (key_pressed[0] == 'a'):
        pass
    elif (key_pressed[0] == 'q'):
        break