#space invaders
#set up the screen
#python
import turtle
import os
import math
import random

#set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("space invaders")
wn.bgpic=("space_invaders_background.gif")

#register the shae
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")


#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()
#set score to 0
score = 0

#draw score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring=  "score: %s" %score
score_pen.write(scorestring, False , align="left", font=("Arial", 12, "normal"))
score_pen.hideturtle()
#create the player turtle
player= turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed()
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

#choose a number of enemies
number_of_enemies = 5
#create an empty list of eneemies
enemies=[]

#addd  enemies to the list
for i in range(number_of_enemies):
    #create the enemy
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(1, 250)
    enemy.setposition(x, y)
    
enemyspeed=2    
    
#create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#define bullet state
#ready -ready to fire
#fire - bullet is firing
bulletstate= "ready"

#move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x<-280:
        x=-280
    player.setx(x)

def move_right():
    x= player.xcor()
    x+= playerspeed
    if x>280:
        x=280
    player.setx(x)

def fire_bullet():
    #declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        #move the bullet  just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

def iscollision(t1, t2):
    distance= math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 30 :
        return True
    else:
        return False

#create keybooard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#main game loop
while True:
    for enemy in enemies :
        #move the enemy
        x= enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Move the enemy back and down
        if enemy.xcor()>280:
            for e in enemies:
                y = e.ycor()
                y-=40
                e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() <-280 :
            for e in enemies:
                y = e.ycor()
                y-=40
                e.sety(y)
            enemyspeed *=-1
        #check for the collision
        if iscollision(bullet,enemy):
            #reset the bullet
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0, -400)
            #reset the enemey
            x=random.randint(-200,200)
            y=random.randint(1, 250)
            enemy.setposition(x, y)
            #update the score
            score +=10
            scorestring="score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False , align="left", font=("Arial", 12, "normal"))
            
        if iscollision(enemy,player):
            player.hideturtle()
            enemy.hideturtle()
            print("game over")
            break
        #move the bullet
        if bulletstate == "fire":
            y= bullet.ycor()
            y+=bulletspeed
            bullet.sety(y)

        #check to see if the bullet has gone on the top
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate="ready"
    
        



