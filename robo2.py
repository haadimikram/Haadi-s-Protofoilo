from turtle import *
bgcolor("sky blue")
setup(700,700)

# rocket ship
seth(-90)
pu()
fd(200)
pd()



def rocket():
    width(1)
    color("yellow")
    begin_fill()
    circle(100, 90)
    lt(120)
    circle(-100, 60)
    lt(120)
    fd(100)
    end_fill()

    color("red")
    begin_fill()
    rt(90)
    fd(50)
    rt(90)
    fd(100)
    rt(45)
    fd(70)
    rt(135)
    fd(200)
    rt(135)
    fd(70)
    end_fill()



    color("gray")
    lt(45)
    begin_fill()
    fd(400)
    rt(45)
    fd(70)
    rt(90)
    fd(70)
    rt(45)
    fd(400)
    end_fill()
    color("dark blue")
    pu()
    rt(90)
    fd(10)
    rt(90)
    fd(140)




    for i in range(3) :
        pd()
        begin_fill()
        circle(40)
        end_fill()
        pu()
        fd(110)

    

rocket()
#travel
speed("fastest")
clear()
bgcolor("black")
seth(-30)
pu()
goto(100, -200)
pd()
rocket()

#Draw Stars
color("white")
width(10)
def jumpto(x, y):
    pu()
    goto(x, y)
    pd()

def star(size):
    for  point in range (5):
            fd(size)
            rt(144)
      
            
        
def star_at(x, y,  size) :        
    jumpto(x , y)
    star(size)
star_at(-200 ,200 , 20)
star_at(-250 ,-250 , 25)
star_at(-50 ,100 , 30)
star_at(250 ,50 , 20)
star_at(250 ,-250 , 20)
        
for point in range(5):
    fd(20)
    rt(144)


pu()
goto(240, 150)
pd()
seth(30)

#Planet
def planet(planet_radius,  ring_radius,  ring_color,  planet_color):
    #planet_radius = 100
    planet_diameter = planet_radius * 2
    #ring_radius = 25
    #ring_color = "orange"
    #planet_color = "red"
    #draw back of ring
    width(ring_radius)
    color(ring_color)
    circle(ring_radius, 180)
    fd(planet_diameter)
    circle(ring_radius,  180)
    #draw planet
    pu()
    rt(90)
    bk(ring_radius)
    pd()
    width(1)
    color(planet_color)
    begin_fill()
    circle(planet_radius)
    end_fill()
    #draw front of ring
    pu()
    fd(ring_radius)
    lt(90)
    pd()
    width(ring_radius)
    color(ring_color)
    fd(planet_diameter)
    #planet sighting

    
pu()
goto(240, 150)
pd()
seth(-30)
planet(100, 25,  "orange", "red" )

pu()
goto(-10, -280)
pd()
seth(-30)
planet(80, 20,  "pink", "blue" )

#what that
# Alien body and legs
jumpto(-200, -200)
seth(-45)
color('green')
begin_fill()
for i in range(2):
    circle(55, 90)
    circle(27, 90)
end_fill()

# Eyes
pu()
lt(45)
fd(10)
lt(90)
fd(10)
rt(90)

for i in range(3):
    color("white")
    begin_fill()
    circle(9)
    end_fill()
    color("black")
    begin_fill()
    circle(5)
    end_fill()
    fd(30)

# Move to legs starting point
pu()
bk(60)
lt(90)
fd(40)


color("purple")
lt(128)
bk(170)
rt(78)
pd()

#left foot
circle(-10, -90)
begin_fill()
circle(-10, 180)
end_fill()
circle(-10, -90)
fd(30)

#right foot
circle(-10, -90)
begin_fill()
circle(-10, 180)
end_fill()
circle(-10, -90)






    
        

 
    
    
    




    
    


