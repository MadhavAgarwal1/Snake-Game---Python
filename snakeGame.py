import turtle
import random
import time

delay = 0.1
score =0
highscore=0
#snakebodies
bodies=[]

#creating screen/canvas
s= turtle.Screen()
s.title("Snake Game using Turtle Module")
s.bgcolor("gray")
s.setup(width=600,height=600)

#creating Snake head
head = turtle.Turtle()         #Creates and returns a new turtle object
head.speed(0)       
head.shape('circle')      

head.resizemode("user")

head.color("white")
head.fillcolor("red")
head.penup()            #Pull the pen up -- no drawing when moving
head.goto(0,0)
head.direction="khelKthm"    

#creating Snake food
food = turtle.Turtle()
food.speed(0)          
food.shape("square")
food.color("black")
food.fillcolor("yellow")
food.penup()
food.goto(0,200)      #setting initial food position

#score board
sb= turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()             
sb.goto(195,270)
sb.write("Score: 0 ",font="Courier 12 italic",)

def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"
def movekhelKthm():
    head.direction = "khelKthm"    
def move():
    if head.direction=="up":
        y=head.ycor()       
        head.sety(y+20)     
    if head.direction=="down":
        y=head.ycor()           
        head.sety(y-20)     
    if head.direction=="left":
        x=head.xcor()   
        head.setx(x-20)      
    if head.direction=="right":
        x=head.xcor()       
        head.setx(x+20)  

#event handling - key mapping
s.listen()
s.onkey(moveup,"Up")      
s.onkey(movedown,"Down")        
s.onkey(moveleft,"Left")      
s.onkey(moveright,"Right")        
s.onkey(movekhelKthm,"space")     # set terminating key as "spacekey"    

#main loop
while True:
    s.update()       
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

    if head.distance(food) < 20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        # incerase length of the snake's body
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)       #appending new body of snake to the bodies list

        #increase score
        score+=10
        #change delay
        delay-=0.001
        #update highscore
        if score > highscore:
            highscore =score
        sb.clear()
        sb.write(f"Score: {score} ",font="Courier 12 bold")

    #move snake bodies
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()     
        y=bodies[index-1].ycor()     
        bodies[index].goto(x,y)

    #replace 1st body place to head place 
    if len(bodies) > 0:
        x=head.xcor()    
        y=head.ycor()    
        bodies[0].goto(x,y)
    move()
    sb.goto(195,270)


    #check collision with its body
    for body in bodies:
        if body.distance(head)<20:     
            time.sleep(1)
            head.goto(0,0)
            head.direction="khelKthm"   

            #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()
            delay=0.1

            #update scoreboard
            sb.clear()
            sb.goto(0,260)
            sb.write(f"Score: {score} | Highscore: {highscore}",font="Courier 16 bold",align="center")
            score=0

    time.sleep(delay)
