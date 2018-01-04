dt<-0.01
mass_star<-50000
mass_planet<-100000
time<-c()
time[1]<-0

#X star
x_star<-c()
x_star[1]<-0

x_velocity_star<-c()
x_velocity_star[1]<-0

x_acceleration_star<-c()

#X planet
x_planet<-c()
x_planet[1]<-200

x_velocity_planet<-c()
x_velocity_planet[1]<-0

x_acceleration_planet<-c()

#Y star
y_star<-c()
y_star[1]<-0

y_velocity_star<-c()
y_velocity_star[1]<- -2

y_acceleration_star<-c()

#Y planet
y_planet<-c()
y_planet[1]<-30

y_velocity_planet<-c()
y_velocity_planet[1]<-11

y_acceleration_planet<-c()

#R
r<-c()

#functions:
calculateAcceleration<-function(otherX,X,R,otherMass){
  return (otherMass*(otherX-X)/R**3)
}
calculateVelocity<-function(oldXVelocity,oldXAcceleration){
  return(oldXVelocity+oldXAcceleration*dt)
}
calculatePosition<-function(oldX,oldXVelocity,XVelocity){
  return (oldX+(oldXVelocity+XVelocity)/2*dt)
}
calculateR<-function(xStar,xPlanet,yStar,yPlanet){
  return(sqrt((xStar-xPlanet)**2+(yStar-yPlanet)**2))
}

#init acceleration:
r[1]<-(calculateR(x_star[1],x_planet[1],y_star[1],y_planet[1]))
x_acceleration_star[1]<-(calculateAcceleration(x_planet[1],x_star[1],r[1],mass_planet))
x_acceleration_planet[1]<-(calculateAcceleration(x_star[1],x_planet[1],r[1],mass_star))
y_acceleration_star[1]<-(calculateAcceleration(y_planet[1],y_star[1],r[1],mass_planet))
y_acceleration_planet[1]<-(calculateAcceleration(y_star[1],y_planet[1],r[1],mass_star))

for(i in 2:100000){
  time[i]<-(dt*i)
  x_velocity_star[i]<-(calculateVelocity(x_velocity_star[i-1],x_acceleration_star[i-1]))
  x_velocity_planet[i]<-(calculateVelocity(x_velocity_planet[i-1],x_acceleration_planet[i-1]))
  y_velocity_star[i]<-(calculateVelocity(y_velocity_star[i-1],y_acceleration_star[i-1]))
  y_velocity_planet[i]<-(calculateVelocity(y_velocity_planet[i-1],y_acceleration_planet[i-1]))
  
  x_star[i]<-(calculatePosition(x_star[i-1],x_velocity_star[i-1],x_velocity_star[i]))
  x_planet[i]<-(calculatePosition(x_planet[i-1],x_velocity_planet[i-1],x_velocity_planet[i]))
  y_star[i]<-(calculatePosition(y_star[i-1],y_velocity_star[i-1],y_velocity_star[i]))
  y_planet[i]<-(calculatePosition(y_planet[i-1],y_velocity_planet[i-1],y_velocity_planet[i]))
  
  r[i]<-(calculateR(x_star[i],x_planet[i],y_star[i],y_planet[i]))
  
  x_acceleration_star[i]<-(calculateAcceleration(x_planet[i],x_star[i],r[i],mass_planet))
  x_acceleration_planet[i]<-(calculateAcceleration(x_star[i],x_planet[i],r[i],mass_star))
  y_acceleration_star[i]<-(calculateAcceleration(y_planet[i],y_star[i],r[i],mass_planet))
  y_acceleration_planet[i]<-(calculateAcceleration(y_star[i],y_planet[i],r[i],mass_star))
}

plot(x_planet,y_planet,pch='.',col="red",xlab="X",ylab="Y")
lines(x_star,y_star,col="green")