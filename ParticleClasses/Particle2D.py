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
