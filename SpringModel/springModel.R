dt <- 0.01
K <- 2
damp <- 0.5
mass <- 3
x <- 10
velocity <- 0

time <- c()
xValues <- c()
velocityValues <- c()
accelerationValues <- c()

time[1] <- 0
xValues[1] <- x
velocityValues[1] <- velocity

calculateAcceleration <- function(index){
  return((-K*xValues[index]-damp*velocityValues[index])/mass)
}

calculateX <- function(index){
  oldX <- xValues[index-1]
  oldVelocity <- velocityValues[index-1]
  newVelocity <- velocityValues[index]
  return(((oldVelocity+newVelocity)/2)*dt+oldX)
}

calculateVelocity <- function(index){
  oldVelocity <- velocityValues[index-1]
  oldA <- accelerationValues[index-1]
  return(oldVelocity+oldA*dt)
}

accelerationValues[1] <- calculateAcceleration(1) #initial value, r doesnt start from

for(i in 2:10000){  #starts from second element
  time <- c(time,i*dt)
  velocityValues <- c(velocityValues,calculateVelocity(i))
  xValues <- c(xValues,calculateX(i))
  accelerationValues <- c(accelerationValues,calculateAcceleration(i))

}

#Draws graph
plot(time,xValues,pch='.')




