from turtle import *
from math import *
from random import randint

#Constants
dt=0.01
K=1
damp=0.5
mass=2
x=10
velocity=0
useColours=False

time=list()
xValues=list()
velocityValues=list()
accelerationValues=list()


def calculateAcceleration(index):
    return (-K*xValues[index]-damp*velocityValues[index])/mass

def calculateX(index):
    oldX=xValues[index-1]
    oldvelocity=velocityValues[index-1]
    newvelocity=velocityValues[index]
    return ((oldvelocity+newvelocity)/2)*dt+oldX

def calculatevelocity(index):
    oldvelocity=velocityValues[index-1]
    oldA=accelerationValues[index-1]
    return oldvelocity+oldA*dt

#Initial values
time.append(0)
xValues.append(x)
velocityValues.append(velocity)
accelerationValues.append(calculateAcceleration(0)) #initial value


#Calculations 
for i in range(1,10000):
    time.append(i*dt)
    velocityValues.append(calculatevelocity(i))
    xValues.append(calculateX(i))
    accelerationValues.append(calculateAcceleration(i))


#GRAPHICS SETUP
speed(0)
penup()
back(500)
pendown()
colours=["red","green","purple","blue"]

for i in range(1,10000,10):
    #COLOURS
    if useColours==True:
        num=randint(0,len(colours)-1)
        color(colours[num])
    #ACTUAL DRAWING
    lastX=xValues[i-1]
    left(degrees(atan((xValues[i]-lastX)/dt)))
    forward((sqrt(dt**2+(xValues[i]-lastX)**2))*200)
    right(degrees(atan((xValues[i]-lastX)/dt)))

