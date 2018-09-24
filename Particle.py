class Particle():
    #Constructor
    def __init__(self,mass,velocity,acceleration,x,y,direction):
        self.mass=mass
        self.velocity=0
        self.velocityOld=velocity
        self.acceleration=0
        self.accelerationOld=acceleration
        self.x=x
        self.y=y
        self.direction=direction

    #Used to separately set the graphic properties of the particle
    def setGraphics(self,fill,radius):
        self.fill=fill
        self.radius=radius

    #Draws circle in ocordance with graphic data and init data
    def draw_ball(self):                        #draw oval
        self.current_shape=c.create_oval(self.x-self.radius,self.y-self.radius,self.x+self.radius,self.y+self.radius,fill=self.fill,outline="")

    #Destroys the current shape object
    def clear_current(self):
        c.delete(self.current_shape)
        del self.current_shape

    #Returns x and y coords of the particle
    def get_coords(self):
        coords=c.coords(self.current_shape)
        x=(coords[0]+coords[2])/2
        y=(coords[1]+coords[3])/2
        return x,y

    #Updates class data about position
    def refresh(self):
        i,j=self.get_coords()
        self.x=i
        self.y=j
        



