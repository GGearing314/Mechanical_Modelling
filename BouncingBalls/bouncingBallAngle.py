#Bouncing Ball @ Angle Model | GGearing | 15/09/2018

from tkinter import *
from time import sleep,time
from math import *

class Particle():
    def __init__(self,mass,velocityX,velocityY,accelerationX,accelerationY,x,y,direction):
        self.mass=mass
        self.velocityX=velocityX
        self.velocityY=velocityY
        self.accelerationX=accelerationX
        self.accelerationY=accelerationY
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
WIDTH=1000
window=Tk()
window.title("Bouncing Ball")
c=Canvas(window,width=WIDTH,height=HEIGHT,bg="white")
c.pack()

#Constants:
E=0.5 #coefficient of restitution
GRAVITY=9.81
DT=0.01 #time step
ANGLE=radians(20)   
Vt=6 #init velocity

#Ball setup:
ball=Particle(100,Vt*sin(ANGLE),Vt*cos(ANGLE),0,GRAVITY,0,20,1)
ball.setGraphics("blue",20)
ball.draw_ball()

def calculations():
    ball.velocityY+=GRAVITY*DT
    c.move(ball.current_shape,ball.velocityX,ball.velocityY)
    sleep(DT)
    ball.refresh()
    window.update()
    
while True:
    while ball.y+20<500:
       calculations()
    #Collision:
    ball.velocityY=-1*(ball.velocityY*E) #e=speed of separation/speed of approach
    c.move(ball.current_shape,ball.velocityX,ball.velocityY)
    ball.refresh()
    window.update()
    while ball.y+20>500:    #Handles glitch
        calculations()    
    
        
        
