import turtle as trtl
tr = trtl.Turtle()
wn = trtl.Screen()
wn.addshape('halloween-pusheen.gif')
tr.shape('halloween-pusheen.gif')
wn.mainloop()
import random as rand

#-----game configuration----
bubble_color = "green"
bubble_size = int(2)
bubble_shape = "circle"
a=0
b=400
c=0
d=300

#-----initialize turtle-----
bubble = trtl.Turtle()

#-----game functions--------
bubble.fillcolor(bubble_color)
bubble.shapesize(bubble_size)
bubble.shape(bubble_shape)

def change_position ():
  new_xpos = rand.randint(a,b)
  new_ypos = rand.randint(c,d)
  bubble.goto(new_xpos, new_ypos)

def bubble_clicked(x,y):
  bubble.hideturtle()
  bubble.penup()
  change_position()
  bubble.showturtle()
#-----events----------------
bubble.onclick(bubble_clicked)

#bubble.bgpic('halloween-pusheen.gif')
wn=trtl.Screen ()
wn.mainloop ()