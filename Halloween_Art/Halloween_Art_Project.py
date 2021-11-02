import turtle as trtl
wn = trtl.Screen()

wn.addshape('bugbug2.gif')


wn.bgpic("halloween-pusheen.gif.gif")

import random as rand

bubble = trtl.Turtle()
bubble.shape('bugbug2.gif')

def change_position():
  new_xpos = rand.randint(-250,250)
  new_ypos = rand.randint(-75,250)
  bubble.goto(new_xpos, new_ypos)


def bubble_clicked(x,y):
  bubble.hideturtle()
  bubble.penup()
  change_position()
  new_xpos = rand.randint(-250,250)
  new_ypos = rand.randint(-75,250)
  bubble.goto(new_xpos, new_ypos)
  bubble.showturtle()


bubble.onclick(bubble_clicked)

wn.mainloop()
