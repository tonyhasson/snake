import turtle
import time
import random
import shelve

count_time = 0
check_speed = 0
game = True
score_collect = []
times_played = 0
high_score=0





d = shelve.open('hs_snake.txt')
high_score = d['score']
hs_name=d['name']

d.close()
name=""

while game:

    i = 0
    while i < len(score_collect):
        if score_collect[i] > high_score:
            high_score = score_collect[i]
            d = shelve.open('hs_snake.txt')
            hs_name=name
            d.close()
        i += 1
    d = shelve.open('hs_snake.txt')  # here you will save the score variable
    d['score'] = high_score # thats all, now it is saved on disk.
    d['name'] = hs_name
    d.close()

    score = 0
    extra_speed = 0.05
    delay = 0.085
    tail = []
    count_minus=0
    count_time_portal=0
    bool_portal=False
    ##creating the screen
    window = turtle.Screen()
    window.bgcolor("green")
    window.setup(width=600, height=600)
    window.tracer(0)
    if times_played==0:
         name = input("enter your name!: ")
    window.title("hello " + str(name) + "!  numbers of time played: " + str(times_played))



    ##creating the head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"

    ##creating the food
    food = turtle.Turtle()
    food.color("red")
    food.shape("circle")
    food.penup()
    food.goto(0, 100)

    ##creating score
    text = turtle.Turtle()
    text.speed(0)
    text.penup()
    text.shape("square")
    text.color("yellow")
    text.hideturtle()
    text.goto(-240, 260)
    text.write("Score:" + str(score) + "  High score:" + str(high_score)+" "+str(hs_name), font=14)



    ##creating extra speed food
    esf = turtle.Turtle()
    esf.penup()
    esf.color("blue")
    esf.shape("triangle")
    esf.speed(0)
    esf.hideturtle()
    esf.goto(400, 400)

    ##creating pause text
    pause_text = turtle.Turtle()
    pause_text.color("purple")
    pause_text.hideturtle()
    pause_text.penup()
    pause_text.speed(0)
    pause_text.shape("square")
    pause_text.goto(400, 400)
    pause_text.write("Game Paused,click any arrow key to continue!", font=14)

    ##creating mines
    image_mines=r"C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\mine.gif"
    window.addshape(image_mines)
    mines = turtle.Turtle()
    mines.penup()
    mines.shape(image_mines)
    mines.speed(0)
    mines.goto(400,400)
    mines.hideturtle()
    mine_list=[]

    ##creating mine deleters
    image_minus5=r"C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\minus_5.gif"
    image_minus3 = r"C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\minus_3.gif"
    window.addshape(image_minus5)
    window.addshape(image_minus3)
    minus5=turtle.Turtle()
    minus3 = turtle.Turtle()
    minus5.penup()
    minus3.penup()
    minus3.shape(image_minus3)
    minus5.shape(image_minus5)
    minus5.speed(0)
    minus3.speed(0)
    minus3.goto(400,400)
    minus5.goto(400, 400)
    minus3.hideturtle()
    minus5.hideturtle()







    ##creating portals
    image_up=r"C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\up.gif"
    image_down=r"C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\down.gif"
    image_left=r"C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\left.gif"
    image_right=r"C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\right.gif"
    count_portal=0

    window.addshape(image_down)
    window.addshape(image_up)
    window.addshape(image_left)
    window.addshape(image_right)

    portal_up=turtle.Turtle()
    portal_down = turtle.Turtle()
    portal_left= turtle.Turtle()
    portal_right = turtle.Turtle()

    portal_up.shape(image_up)
    portal_down.shape(image_down)
    portal_left.shape(image_left)
    portal_right.shape(image_right)

    portal_up.penup()
    portal_down.penup()
    portal_left.penup()
    portal_right.penup()

    portal_up.goto(400,400)
    portal_down.goto(400,400)
    portal_left.goto(400,400)
    portal_right.goto(400,400)

    portal_up.hideturtle()
    portal_down.hideturtle()
    portal_left.hideturtle()
    portal_right.hideturtle()






    ##functions
    def go_up():
        if was_pause != "pause":
            if head.direction != "down":
                head.direction = "up"
        if was_pause == "pause":
            if past_goto != "down":
                head.direction = "up"




    def go_down():
       if was_pause != "pause":
           if head.direction != "up":
               head.direction = "down"
       if was_pause=="pause":
            if  past_goto!="up":
                head.direction="down"





    def go_right():
        if was_pause != "pause":
            if head.direction != "left":
                head.direction = "right"
        if was_pause == "pause":
            if past_goto != "left":
                head.direction = "right"


    def go_left():
        if was_pause != "pause":
            if head.direction != "right":
                head.direction = "left"
        if was_pause == "pause":
            if past_goto != "right":
                head.direction = "left"


    def pause():
        head.direction = "pause"

    def portal(num):
        portal_up.hideturtle()
        portal_right.hideturtle()
        portal_left.hideturtle()
        portal_down.hideturtle()

        portal_up.goto(400, 400)
        portal_down.goto(400, 400)
        portal_left.goto(400, 400)
        portal_right.goto(400, 400)

        if num==1:
            portal_up.setx(random.randint(-250,250))
            portal_up.sety(random.randint(50,250))
            for index in range(0, len(mine_list), 1):

                if portal_up.distance(mine_list[index]) < 60:
                    portal(num)
            portal_up.showturtle()
            num2=random.randint(1,3)
            x2=portal_up.xcor()
            y2=portal_up.ycor()

            if num2==1:
                portal_down.setx(random.randint(-250, 250))
                portal_down.sety(random.randint(-250, -50))
                for index in range(0, len(mine_list), 1):

                    if portal_down.distance(mine_list[index]) < 60:
                        portal(num)
                x = portal_down.xcor()
                y = portal_down.ycor()
                portal_down.showturtle()
                return x,y,"down",x2,y2,"up"

            if num2==2:
                portal_left.setx(random.randint(-250, 250))
                portal_left.sety(random.randint(-250, -50))
                for index in range(0, len(mine_list), 1):

                    if portal_left.distance(mine_list[index]) < 60:
                        portal(num)
                x = portal_left.xcor()
                y = portal_left.ycor()
                portal_left.showturtle()
                return x, y,"left",x2,y2,"up"
            if num2==3:
                portal_right.setx(random.randint(-250, 250))
                portal_right.sety(random.randint(-250, -50))
                for index in range(0, len(mine_list), 1):

                    if portal_right.distance(mine_list[index]) < 60:
                        portal(num)
                x = portal_right.xcor()
                y = portal_right.ycor()
                portal_right.showturtle()
                return x, y,"right",x2,y2,"up"

        if num==2:
            portal_down.setx(random.randint(-250,250))
            portal_down.sety(random.randint(50,250))
            for index in range(0, len(mine_list), 1):

                if portal_down.distance(mine_list[index]) < 60:
                    portal(num)
            portal_down.showturtle()
            num2=random.randint(1,3)
            x2 = portal_down.xcor()
            y2 = portal_down.ycor()
            if num2==1:
                portal_up.setx(random.randint(-250, 250))
                portal_up.sety(random.randint(-250, -50))
                for index in range(0, len(mine_list), 1):

                    if portal_up.distance(mine_list[index]) < 60:
                        portal(num)
                x = portal_up.xcor()
                y = portal_up.ycor()
                portal_up.showturtle()
                return x, y,"up",x2,y2,"down"
            if num2==2:
                portal_left.setx(random.randint(-250, 250))
                portal_left.sety(random.randint(-250, -50))
                for index in range(0, len(mine_list), 1):

                    if portal_left.distance(mine_list[index]) < 60:
                        portal(num)
                x = portal_left.xcor()
                y = portal_left.ycor()
                portal_left.showturtle()
                return x, y,"left",x2,y2,"down"
            if num2==3:
                portal_right.setx(random.randint(-250, 250))
                portal_right.sety(random.randint(-250, -50))
                for index in range(0, len(mine_list), 1):

                    if portal_right.distance(mine_list[index]) < 60:
                        portal(num)
                x = portal_right.xcor()
                y = portal_right.ycor()
                portal_right.showturtle()
                return x, y,"right",x2,y2,"down"

        if num==3:
            portal_left.setx(random.randint(-250,250))
            portal_left.sety(random.randint(50,250))
            for index in range(0, len(mine_list), 1):

                if portal_left.distance(mine_list[index]) < 60:
                    portal(num)
            portal_left.showturtle()
            num2=random.randint(1,3)
            x2 = portal_left.xcor()
            y2 = portal_left.ycor()
            if num2==1:
                portal_up.setx(random.randint(-250, 250))
                portal_up.sety(random.randint(-250, -50))
                for index in range(0, len(mine_list), 1):

                    if portal_up.distance(mine_list[index]) < 60:
                        portal(num)
                x = portal_up.xcor()
                y = portal_up.ycor()
                portal_up.showturtle()
                return x, y,"up",x2,y2,"left"
            if num2==2:
                portal_down.setx(random.randint(-250, 250))
                portal_down.sety(random.randint(-250, -50))
                for index in range(0, len(mine_list), 1):

                    if portal_down.distance(mine_list[index]) < 60:
                        portal(num)
                x = portal_down.xcor()
                y = portal_down.ycor()
                portal_down.showturtle()
                return x, y,"down",x2,y2,"left"
            if num2==3:
                portal_right.setx(random.randint(-250, 250))
                portal_right.sety(random.randint(-250, -50))
                for index in range(0, len(mine_list), 1):

                    if portal_right.distance(mine_list[index]) < 60:
                        portal(num)
                x = portal_right.xcor()
                y = portal_right.ycor()
                portal_right.showturtle()
                return x, y,"right",x2,y2,"left"

        if num==4:
            portal_right.setx(random.randint(-250,250))
            portal_right.sety(random.randint(50,250))
            for index in range(0, len(mine_list), 1):

                if portal_right.distance(mine_list[index]) < 60:
                    portal(num)
            portal_right.showturtle()
            num2=random.randint(1,3)
            x2 = portal_right.xcor()
            y2 = portal_right.ycor()
            if num2==1:
                portal_up.setx(random.randint(-250, 250))
                portal_up.sety(random.randint(-250, -50))
                for index in range(0, len(mine_list), 1):

                    if portal_up.distance(mine_list[index]) < 60:
                        portal(num)
                x = portal_up.xcor()
                y = portal_up.ycor()
                portal_up.showturtle()
                return x, y,"up",x2,y2,"right"
            if num2==2:
                portal_left.setx(random.randint(-250, 250))
                portal_left.sety(random.randint(-250, -50))
                for index in range(0, len(mine_list), 1):

                    if portal_left.distance(mine_list[index]) < 60:
                        portal(num)
                x = portal_left.xcor()
                y = portal_left.ycor()
                portal_left.showturtle()
                return x, y,"left",x2,y2,"right"
            if num2==3:
                portal_down.setx(random.randint(-250, 250))
                portal_down.sety(random.randint(-250, -50))
                for index in range(0, len(mine_list), 1):

                    if portal_down.distance(mine_list[index]) < 60:
                        portal(num)
                x=portal_down.xcor()
                y=portal_down.ycor()
                portal_down.showturtle()
                return x, y,"down",x2,y2,"right"








    def move():
        if head.direction == "pause":
            pause_text.goto(-180, 60)
            pause_text.write("Game Paused,click any arrow key to continue!", font=14)
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)
            pause_text.clear()
        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
            pause_text.clear()
        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)
            pause_text.clear()
        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)
            pause_text.clear()


    def food_pos():
        food.setx(random.randint(-290, 290))
        food.sety(random.randint(-290, 290))
        for index in range(0, len(mine_list), 1):

            if food.distance(mine_list[index]) < 80:
                food_pos()
        if food.distance(portal_right)<80 or food.distance(portal_up)<80 or food.distance(portal_down)<80 or food.distance(portal_left)<80 :
            food_pos()

    def add_speed():
        esf.setx(random.randint(-280, 280))
        esf.sety(random.randint(-280, 280))
        for index in range(0,len(mine_list),1):

            if esf.distance(mine_list[index])<80:
                add_speed()
        if esf.distance(portal_right)<80 or esf.distance(portal_up)<80 or esf.distance(portal_down)<80 or esf.distance(portal_left)<80:
            add_speed()
        esf.showturtle()

    def delete_mine(num):
        if num==1:
            minus3.setx((random.randint(-280,280)))
            minus3.sety((random.randint(-280, 280)))
            for index in range(0, len(mine_list), 1):

                if minus3.distance(mine_list[index]) < 80:
                    delete_mine(num)
            if minus3.distance(portal_right) < 80 or minus3.distance(portal_up) < 80 or minus3.distance(portal_down) < 80 or minus3.distance(portal_left) < 80:
                delete_mine(num)
            minus3.showturtle()

        if num==2:
            minus5.setx((random.randint(-280, 280)))
            minus5.sety((random.randint(-280, 280)))
            for index in range(0, len(mine_list), 1):

                if minus5.distance(mine_list[index]) < 80:
                    delete_mine(num)
            if minus5.distance(portal_right) < 80 or minus5.distance(portal_up) < 80 or minus5.distance(portal_down) < 80 or minus5.distance(portal_left) < 80:
                delete_mine(num)
            minus5.showturtle()


    def add_mine():
        image = r"C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\mine.gif"
        window.addshape(image)
        mines = turtle.Turtle()
        mines.penup()
        mines.shape(image)
        mines.speed(0)
        mines.setx(random.randint(-280, 280))
        mines.sety(random.randint(-280, 280))
        if mines.distance(esf)<80 or mines.distance(food)<80 or mines.distance(portal_up)<80 or mines.distance(portal_down)<80 or mines.distance(portal_left)<80 or mines.distance(portal_right)<80:
            add_mine()
        else:
            mines.showturtle()
            mine_list.append(mines)




    ##key bindings
    window.listen()
    window.onkeypress(go_up, 'Up')
    window.onkeypress(go_down, 'Down')
    window.onkeypress(go_right, 'Right')
    window.onkeypress(go_left, 'Left')
    window.onkeypress(go_up, 'w')
    window.onkeypress(go_down, 's')
    window.onkeypress(go_right, 'd')
    window.onkeypress(go_left, 'a')
    window.onkeypress(pause, 'p')

    bool = True
    bool_speed = False
    was_pause="x"
    while bool:
        window.update()
        if head.direction!="pause":
            past_goto=head.direction

        if head.direction=="pause":
            was_pause="pause"
        if count_time_portal==120:
            bool_portal=False
            count_time_portal=0
        if count_time == 155:
            bool_speed = False
            count_time = 0
            check_speed = 0
        if score > 10:
            if random.randint(0, 250) == 25 and check_speed == 0 and count_time == 0:
                add_speed()
                check_speed += 1
            if random.randint(0,200)==50:
                add_mine()
            if random.randint(0,250)==78 and count_time_portal==0:
                rnd=random.randint(1,4)
                if rnd==1:
                    portalx,portaly,portal_dir,portalx2,portaly2,portal_dir2=portal(1)
                    bool_portal=True

                if rnd==2:
                    portalx,portaly,portal_dir,portalx2,portaly2,portal_dir2=portal(2)
                    bool_portal = True

                if rnd==3:
                    portalx,portaly,portal_dir,portalx2,portaly2,portal_dir2=portal(3)
                    bool_portal = True

                if rnd==4:
                    portalx,portaly,portal_dir,portalx2,portaly2,portal_dir2=portal(4)
                    bool_portal = True
            if len(mine_list)>10 and count_minus==0:
                if random.randint(0,130)==70:
                    delete_mine(random.randint(1,2))
                    count_minus+=1


        ##taking the extra speed
        if head.distance(esf) < 20:
            bool_speed = True
            esf.goto(400, 400)
            esf.hideturtle()
        ##taking a mine deleter
        if head.distance(minus3)<20:
            i=0
            while i<3:
                mine_list[len(mine_list)-1-i].goto(400,400)
                mine_list.pop(len(mine_list)-1-i)

                i+=1
            minus3.goto(400,400)
            minus3.hideturtle()
            count_minus=0
        if head.distance(minus5)<20:
            i=0
            while i<5:
                mine_list[len(mine_list) - 1 - i].goto(400, 400)
                mine_list.pop(len(mine_list)-1-i)
                i+=1
            minus5.goto(400,400)
            minus5.hideturtle()
            count_minus = 0


        ##going through a portal:


        if head.distance(portal_up)<20 and head.direction==portal_dir2:
            head.setx(portalx)
            head.sety(portaly)
            head.direction=portal_dir



        elif head.distance(portal_down)<20 and head.direction==portal_dir2:
            head.setx(portalx)
            head.sety(portaly)
            head.direction=portal_dir


        elif head.distance(portal_left)<20 and head.direction==portal_dir2:
            head.setx(portalx)
            head.sety(portaly)
            head.direction=portal_dir


        elif head.distance(portal_right)<20 and head.direction==portal_dir2:
            head.setx(portalx)
            head.sety(portaly)
            head.direction=portal_dir


        elif head.distance(portal_up)<20 and head.direction==portal_dir:
            head.setx(portalx2)
            head.sety(portaly2)
            head.direction=portal_dir2


        elif head.distance(portal_down)<20 and head.direction==portal_dir:
            head.setx(portalx2)
            head.sety(portaly2)
            head.direction=portal_dir2


        elif head.distance(portal_right)<20 and head.direction==portal_dir:
            head.setx(portalx2)
            head.sety(portaly2)
            head.direction=portal_dir2


        elif head.distance(portal_left)<20 and head.direction==portal_dir:
            head.setx(portalx2)
            head.sety(portaly2)
            head.direction=portal_dir2






        ##hitting a mine
        for index in range(0,len(mine_list),1):

            if head.distance(mine_list[index])<20:
                 time.sleep(delay)
                 bool=False

        ##going through the wall
        if head.xcor() > 290:
            head.setx(-290)

        elif head.xcor() < -290:
            head.setx(290)

        elif head.ycor() > 290:
            head.sety(-290)

        elif head.ycor() < -290:
            head.sety(290)

        ##creating tail after eating food
        if head.distance(food) < 20:
            food_pos()
            if check_speed == 0:
                score += 10
            if check_speed > 0:
                score += 20
            text.clear()
            text.goto(-240, 260)
            text.write("Score:" + str(score) + "  High score:" + str(high_score)+" "+str(hs_name), font=14)

            new_tail = turtle.Turtle()
            new_tail.speed(0)
            new_tail.color("grey")
            new_tail.shape("square")
            new_tail.penup()
            tail.append(new_tail)
        if head.direction != "pause":

            for index in range(len(tail) - 1, 0, -1):
                x = tail[index - 1].xcor()
                y = tail[index - 1].ycor()
                tail[index].goto(x, y)

            if len(tail) > 0:
                xzero = tail[0].xcor()
                yzero = tail[0].ycor()
                tail[0].goto(head.xcor(), head.ycor())

        move()
        if head.direction != "pause":
            if len(tail) == 1:
                if head.xcor() == xzero and head.ycor() == yzero:
                    bool = False
            i = 0

            while i < len(tail):
                if head.distance(tail[i]) < 20:
                    bool = False
                i += 1

        if bool_speed == False:
            time.sleep(delay)
        if bool_speed == True:
            time.sleep(extra_speed)
            count_time += 1
        if bool_portal==True:
            count_time_portal+=1

    window.clear()
    times_played += 1
    score_collect.append(score)
    count_time = 0
    check_speed = 0


window.mainloop()
