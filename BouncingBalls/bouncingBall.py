#Bouncing Ball Model | GGearing | 15/09/2018

from tkinter import *
from time import sleep,time

class Particle():
    def __init__(self,mass,velocity,acceleration,x,y,direction):
        self.mass=mass
        self.velocity=velocity
        self.acceleration=acceleration
        self.x=x
        self.y=y
        self.direction=direction

    def setGraphics(self,fill,radius):
        self.fill=fill
        self.radius=radius
    
    def draw_ball(self):                        #draw oval
        self.current_shape=c.create_oval(self.x-self.radius,self.y-self.radius,self.x+self.radius,self.y+self.radius,fill=self.fill,outline="")

    def clear_current(self):
        c.delete(self.current_shape)
        del self.current_shape
        
    def get_coords(self):
        coords=c.coords(self.current_shape)
        x=(coords[0]+coords[2])/2
        y=(coords[1]+coords[3])/2
        return x,y
    def refresh(self):
        i,j=self.get_coords()
        self.x=i
        self.y=j
    def reset(self):
        self.x1=self.orig_x1
        self.y1=self.orig_y1
        self.x2=self.orig_x2
        self.y2=self.orig_y2
        self.clear_current()
        self.draw_ball()

#GUI setup:
HEIGHT=500
WIDTH=500
window=Tk()
window.title("Bouncing Ball")
c=Canvas(window,width=WIDTH,height=HEIGHT,bg="white")
c.pack()

#Constants:
E=0.9
GRAVITY=9.81
DT=0.01

#Ball setup:
ball=Particle(100,0,GRAVITY,WIDTH/2,20,1)
ball.setGraphics("blue",20)
ball.draw_ball()

def calculations():
    ball.velocity+=GRAVITY*DT
    c.move(ball.current_shape,0,ball.velocity)
    sleep(DT)
    ball.refresh()
    window.update()
    
while True:
    while ball.y+20<500:
       calculations()
    #Collision:
    ball.velocity=-1*(ball.velocity*E) #e=speed of separation/speed of approach
    c.move(ball.current_shape,0,ball.velocity)
    ball.refresh()
    window.update()
    while ball.y+20>500:    #Handles glitch
        calculations()    
    
        
        
