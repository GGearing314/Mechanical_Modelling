from math import sqrt
from turtle import *

dt=0.01
mass_star=50000
mass_planet=10000
time=list()
time.append(0)

#X star
x_star=list()
x_star.append(0)

x_velocity_star=list()
x_velocity_star.append(0)

x_acceleration_star=list()

#X planet
x_planet=list()
x_planet.append(200)

x_velocity_planet=list()
x_velocity_planet.append(0)

x_acceleration_planet=list()

#Y star
y_star=list()
y_star.append(0)

y_velocity_star=list()
y_velocity_star.append(-2)

y_acceleration_star=list()

#Y planet
y_planet=list()
y_planet.append(30)

y_velocity_planet=list()
y_velocity_planet.append(11)

y_acceleration_planet=list()

#R
r=list()


def calculateAcceleration(otherX,X,R,otherMass):
    return otherMass*(otherX-X)/R**3

def calculateVelocity(oldXVelocity,oldXAcceleration):
    return oldXVelocity+oldXAcceleration*dt

def calculatePosition(oldX,oldXVelocity,XVelocity):
    return oldX+(oldXVelocity+XVelocity)/2*dt

def calculateR(xStar,xPlanet,yStar,yPlanet):
    return sqrt((xStar-xPlanet)**2+(yStar-yPlanet)**2)

#init acceleration:
r.append(calculateR(x_star[0],x_planet[0],y_star[0],y_planet[0]))
x_acceleration_star.append(calculateAcceleration(x_planet[0],x_star[0],r[0],mass_planet))
x_acceleration_planet.append(calculateAcceleration(x_star[0],x_planet[0],r[0],mass_star))
y_acceleration_star.append(calculateAcceleration(y_planet[0],y_star[0],r[0],mass_planet))
y_acceleration_planet.append(calculateAcceleration(y_star[0],y_planet[0],r[0],mass_star))

print(x_acceleration_star[0])
print(x_acceleration_planet[0])
print(y_acceleration_star[0])
print(y_acceleration_planet[0])
for i in range(1,10000):
    time.append(dt*i)
    x_velocity_star.append(calculateVelocity(x_velocity_star[i-1],x_acceleration_star[i-1]))
    x_velocity_planet.append(calculateVelocity(x_velocity_planet[i-1],x_acceleration_planet[i-1]))
    y_velocity_star.append(calculateVelocity(y_velocity_star[i-1],y_acceleration_star[i-1]))
    y_velocity_planet.append(calculateVelocity(y_velocity_planet[i-1],y_acceleration_planet[i-1]))

    x_star.append(calculatePosition(x_star[i-1],x_velocity_star[i-1],x_velocity_star[i]))
    x_planet.append(calculatePosition(x_planet[i-1],x_velocity_planet[i-1],x_velocity_planet[i]))
    y_star.append(calculatePosition(y_star[i-1],y_velocity_star[i-1],y_velocity_star[i]))
    y_planet.append(calculatePosition(y_planet[i-1],y_velocity_planet[i-1],y_velocity_planet[i]))

    r.append(calculateR(x_star[i],x_planet[i],y_star[i],y_planet[i]))

    x_acceleration_star.append(calculateAcceleration(x_planet[i],x_star[i],r[i],mass_planet))
    x_acceleration_planet.append(calculateAcceleration(x_star[i],x_planet[i],r[i],mass_star))
    y_acceleration_star.append(calculateAcceleration(y_planet[i],y_star[i],r[i],mass_planet))
    y_acceleration_planet.append(calculateAcceleration(y_star[i],y_planet[i],r[i],mass_star))
    
    
for i in range(1,10000,20):
    setpos(x_star[i]*2,y_star[i]*2)
    pendown()
    forward(1)
    penup()
    setpos(x_planet[i]*2,y_planet[i]*2)
    pendown()
    forward(1)
    penup()
