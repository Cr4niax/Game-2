import tkinter as tk
import mysql.connector as sqltor
import turtle
import math
import random
import winsound
import time

from datetime import date
bulletstate = 'ready'
score = 0
score1 = 0
c = 'a'
e = 0

# login screen
mycon = sqltor.connect(host='localhost', user='root',
                       passwd='tiger', database='prac', charset='utf8')
a = 'create table if not exists score(name varchar(100),score int(50),attempts int(100),passwd varchar(100),date varchar(40),scorewar int(100),attemptwar int(100),datewar varchar(100))'
cut = mycon.cursor()
cut.execute(a)
mycon.commit()


def ifnot():
    return 'your username password is wrong'


def ifyes():
    return 'successfull'


def login():
    def login1(a, b):

        name = a
        passwd = b
        # mysql statement
        q = 'select name from score'
        cursor = mycon.cursor()
        cursor.execute(q)
        data = cursor.fetchall()

        l1 = []
        l1.append(name)
        l2 = []
        l2.append(passwd)
        tuple1 = tuple(l1)
        tuple2 = tuple(l2)
        e = 0
        # to check its id
        if tuple1 in data:
            w = 'select passwd from score where name="{}"'.format(name)
            cursor.execute(w)
            data1 = cursor.fetchall()
            if tuple2 in data1:

                def game():
                    root6.destroy()
                    winsound.PlaySound(
                        'Halo Theme Song Original.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
                    sc = turtle.Screen()
                    sc.title('SPACE INVADER')
                    turtle.setup(1366, 768)
                    sc.bgcolor('black')
                    sc.tracer(0)
                    sc.update()

                    sc.bgpic('rsz_3rsz_space4.png')

                    # draw score

                    Tl = turtle.Turtle()
                    Tl.speed(0)
                    Tl.color('yellow')
                    Tl.penup()
                    Tl.setposition(0, 80)
                    text34 = 'Are You Ready Captain {} ?'.format(name)
                    Tl.write(text34, False, align='center',
                             font=('Comic Sans MS', 20, 'normal'))
                    Tl.hideturtle()
                    TR = turtle.Turtle()
                    TR.speed(0)
                    TR.color('yellow')
                    TR.penup()
                    TR.setposition(0, 0)
                    TR.write('START', False, align='center',
                             font=('Comic Sans MS', 30, 'normal'))
                    TR.hideturtle()

                    TA = turtle.Turtle()
                    TA.speed(0)
                    TA.color('yellow')
                    TA.penup()
                    TA.setposition(0, -50)
                    TA.write('SCORE', False, align='center',
                             font=('Comic Sans MS', 30, 'normal'))
                    TA.hideturtle()

                    TB = turtle.Turtle()
                    TB.speed(0)
                    TB.color('yellow')
                    TB.penup()
                    TB.setposition(0, -110)
                    TB.write('EXIT', False, align='center',
                             font=('Comic Sans MS', 30, 'normal'))
                    TB.hideturtle()
                    bulletstate = 'ready'

                    def game1():
                        global e
                        global c
                        c = mycon.cursor()
                        global score
                        global bulletstate
                        # define bullet state
                        # ready - ready to fire
                        # fire - bullet is firing
                        bulletstate = 'ready'
                        # main screen
                        wn = turtle.Screen()
                        wn.title('SPACE INVADER')
                        wn.bgcolor('black')
                        wn.title('Space invaders')
                        wn.bgpic('space_invaders_background.gif')
                        wn.tracer(0)

                        # register the shapes
                        turtle.register_shape('pl.gif')
                        turtle.register_shape('invader.gif')
                        # Draw Borders
                        bd1 = turtle.Turtle()
                        bd1.speed(0)
                        bd1.color('white')
                        bd1.penup()
                        bd1.setposition(-300, 270)
                        bd1.pensize(3)
                        bd1.pendown()
                        for side in range(1):
                            bd1.fd(600)
                        bd1.hideturtle()

                        bd = turtle.Turtle()
                        bd.speed(0)
                        bd.color('white')
                        bd.penup()
                        bd.setposition(-300, -300)
                        bd.pensize(3)
                        bd.pendown()
                        for side in range(4):
                            bd.fd(600)
                            bd.lt(90)
                        bd.hideturtle()

                        score3 = turtle.Turtle()
                        score3.speed(0)
                        score3.color('white')
                        score3.penup()
                        score3.hideturtle()
                        score3.setposition(-170, 280)
                        e = 'select attempts from score where name="{}"'.format(
                            name)
                        cursor.execute(e)
                        data8 = cursor.fetchall()
                        for row in data8:
                            for i in row:
                                e = i+1
                        r = 'update score set attempts={} where name="{}"'.format(
                            e, name)
                        cursor.execute(r)
                        mycon.commit()
                        scorestr = 'Attempts:%s' % e
                        score3.write(scorestr, True, font=(
                            'Comic Sans MS', 10, 'bold'))
                        score_p1 = turtle.Turtle()
                        score_p1.speed(0)
                        score_p1.color('white')
                        score_p1.penup()
                        score_p1.setposition(-40, 280)
                        it = 'select score from score where name="{}"'.format(
                            name)
                        c.execute(it)
                        dt = c.fetchall()
                        for i in dt:
                            scorestr = "Your Max Score : %s" % i
                            score_p1.write(scorestr, False, align='left', font=(
                                'Comic Sans MS', 10, 'bold'))
                        score_p1.hideturtle()

                        # set the score to 0
                        score = 0
                        # draw a score
                        score_pen = turtle.Turtle()

                        score_pen.speed(0)
                        score_pen.color('white')
                        score_pen.penup()
                        score_pen.setposition(-290, 280)
                        scorestring = "Score : %s" % score
                        score_pen.write(scorestring, False, align='left', font=(
                            'Comic Sans MS', 14, 'bold'))
                        score_pen.hideturtle()

                        score_p = turtle.Turtle()

                        score_p.speed(0)
                        score_p.color('white')
                        score_p.penup()
                        score_p.setposition(150, 280)
                        it = 'select max(score) from score'
                        c.execute(it)
                        dt = c.fetchall()
                        for i in dt:
                            scorestr = "Highest score : %s" % i
                            score_p.write(scorestr, False, align='left', font=(
                                'Comic Sans MS', 10, 'bold'))
                        score_p.hideturtle()

                        # create a player
                        player = turtle.Turtle()
                        player.speed(0)
                        player.color('blue')
                        player.shape('pl.gif')
                        player.penup()
                        player.setposition(0, -250)
                        player.setheading(90)

                        playerspeed = 15

                        # create enemy
                        # no. of enemies
                        number_of_enemies = 7
                        # create list
                        enemies = []
                        for i in range(number_of_enemies):
                            enemies.append(turtle.Turtle())
                        for enemy in enemies:
                            enemy.color('red')
                            enemy.shape('invader.gif')
                            enemy.speed(0)
                            enemy.penup()
                            x = random.randint(-200, 200)
                            y = random.randint(100, 250)
                            enemy.setposition(x, y)
                        enemyspeed = 1
                        '0.45'

                        # create a bullet

                        bullet = turtle.Turtle()
                        bullet.color('yellow')
                        bullet.shape('triangle')
                        bullet.speed(0)
                        bullet.penup()
                        bullet.setheading(90)
                        bullet.setposition(-200, 250)
                        bullet.shapesize(0.5, 0.5)
                        bullet.hideturtle()
                        bulletspeed = 3

                        # Move player left and right

                        def moveleft():
                            x = player.xcor()
                            x -= playerspeed
                            if x < -280:
                                x = -280
                            player.setx(x)

                        def moveright():
                            x = player.xcor()
                            x += playerspeed
                            if x > 280:
                                x = 280
                            player.setx(x)
                        # bullet movements

                        def firebullet():
                            # declare bullet as global
                            global bulletstate
                            if bulletstate == 'ready':
                                winsound.PlaySound(
                                    'laser.wav', winsound.SND_ASYNC)
                                bulletstate = 'fire'
                               # move the bullet to just above the player
                                x = player.xcor()
                                y = player.ycor()+10
                                bullet.setposition(x, y)
                                bullet.showturtle()

                        def iscollision(t1, t2):
                            distance = math.sqrt(
                                math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(), 2))
                            if distance < 15:
                                return True
                            else:
                                return False

                        def btnclick1(t1, t2):
                            y = t2.ycor()
                            if y < -240:
                                return True
                            else:
                                return False

                        # create keyboard binding

                        turtle.listen()
                        turtle.onkey(moveleft, 'Left')
                        turtle.onkey(moveright, 'Right')
                        turtle.onkey(firebullet, 'space')

                        # main game loop

                        while True:
                            wn.update()
                            for enemy in enemies:
                               # move the enemy
                                x = enemy.xcor()
                                x += enemyspeed
                                enemy.setx(x)

                                # move  all enemies
                                if enemy.xcor() > 280:
                                    for e in enemies:
                                        y = e.ycor()
                                        y -= 35
                                        e.sety(y)
                                    enemyspeed *= -1
                                if enemy.xcor() < -280:
                                    for e in enemies:
                                        y = e.ycor()
                                        y -= 35
                                        e.sety(y)
                                    enemyspeed *= -1
                                 # check for collision between the bullet and the enemy
                                if iscollision(bullet, enemy):
                                    winsound.PlaySound(
                                        'invaderkilled.wav', winsound.SND_ASYNC)
                                    # reset the bullet
                                    bullet.hideturtle()
                                    bulletstate = 'ready'
                                    bullet.setposition(0, -400)
                                    # reset the enemy
                                    x = random.randint(-200, 200)
                                    y = random.randint(100, 250)
                                    enemy.setposition(x, y)
                                    # update the score
                                    score += 10
                                    scorestring = 'Score: %s' % score
                                    score_pen.clear()
                                    score_pen.write(scorestring, False, align='left', font=(
                                        'Arial', 14, 'normal'))

                                if btnclick1(player, enemy):
                                    player.hideturtle()
                                    enemy.hideturtle()
                                    break

                            if btnclick1(player, enemy):
                                player.hideturtle()
                                enemy.hideturtle()

                                break

                            # move the bullet
                            if bulletstate == 'fire':
                                y = bullet.ycor()
                                y += bulletspeed
                                bullet.sety(y)

                            # check to see if the bullet has gone to top
                            if bullet.ycor() > 275:
                                bullet.hideturtle()
                                bulletstate = 'ready'
                        winsound.PlaySound('explosion.wav', winsound.SND_ASYNC)
                        for enemy in enemies:
                            enemy.hideturtle()

                        wn.clear()
                        st = turtle.Screen()
                        st.title('SPACE INVADER')
                        st.bgpic('game over.png')
                        st.bgcolor('black')
                        winsound.PlaySound(
                            'Halo Theme Song Original.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
                        ks = turtle.Turtle()
                        ks.speed(0)
                        ks.color('Yellow')
                        ks.penup()
                        ks.setposition(0, 250)
                        ks.write(' %s Scored:%s' % (name, score), False,
                                 align='center', font=('Comic Sans MS', 18, 'bold'))
                        ks.hideturtle()
                        score_pen.clear()
                        score_p.clear()
                        bd.clear()
                        tks = turtle.Turtle()
                        tks.speed(0)
                        tks.color('Yellow')
                        tks.penup()
                        tks.setposition(0, 150)
                        tks.write(''' THANK YOU FOR PLAYING I HOPE YOU LIKED IT ( - : 
                                             Your Progress Will Be atomatically saved if your score is more
                                             Click Below to close the game''', False, align='center', font=('Comic Sans MS', 18, 'bold'))
                        tks.hideturtle()

                        def btnclick1(x, y):

                            if y >= -294 and y <= -272 and x <= 496 and x >= 435:
                                winsound.PlaySound(
                                    'btcl.wav', winsound.SND_ASYNC)
                                st.clear()
                                game1()

                            if y >= -294 and y <= -272 and x >= -496 and x <= -435:
                                winsound.PlaySound(
                                    'btcl.wav', winsound.SND_ASYNC)
                                wn.exitonclick()
                            if y >= -253 and y <= -232 and x >= 392 and x <= 556:
                                def yourdetail():

                                    mycon = sqltor.connect(
                                        host='localhost', user='root', passwd='tiger', database='prac', charset='utf8')
                                    c = mycon.cursor()
                                    ro = tk.Toplevel()
                                    ro.title('Detailed score')
                                    canvas = tk.Canvas(
                                        ro, height=400, width=600)
                                    canvas.pack()
                                    bg = tk.PhotoImage(file='Nebula.png')
                                    bg_label = tk.Label(ro, image=bg)
                                    bg_label.place(
                                        x=0, y=0, relwidth=1, relheight=1)
                                    ro.resizable(False, False)
                                    frame = tk.Frame(ro, bg='#80c1ff', bd=10)
                                    frame.place(
                                        relx=0.5, rely=0.1, relwidth=0.9, relheight=0.9, anchor='n')
                                    label = tk.Label(frame, bg='#FFE4C4', font=(
                                        'Comic Sans MS', 10, 'bold'))
                                    label.place(relheight=1, relwidth=1)
                                    label1 = tk.Label(label, text='Player', font=(
                                        'Comic Sans MS', 15, 'bold')).place(relx=0.2)
                                    e = 'select name,attempts,score,date from score where name="{}"'.format(
                                        name)
                                    c.execute(e)
                                    data1 = c.fetchall()

                                    for i in data1:

                                        u = i[1]
                                        y = i[2]
                                    c.execute('select max(score) from score')
                                    data2 = c.fetchall()
                                    for e in data2:
                                        a = e[0]

                                    label2 = tk.Label(label, text='{}'.format(name), font=(
                                        'Comic Sans MS', 15, 'bold')).place(relx=0.7)
                                    label3 = tk.Label(label, text=' You Scored', font=(
                                        'Comic Sans MS', 15, 'bold')).place(relx=0.2, rely=0.25)
                                    label4 = tk.Label(label, text='{}'.format(score1), font=(
                                        'Comic Sans MS', 15, 'bold')).place(relx=0.7, rely=0.25)
                                    label5 = tk.Label(label, text='Your high score', font=(
                                        'Comic Sans MS', 15, 'bold')).place(relx=0.2, rely=0.5)
                                    label6 = tk.Label(label, text='{}'.format(y), font=(
                                        'Comic Sans MS', 15, 'bold')).place(relx=0.7, rely=0.5)
                                    label7 = tk.Label(label, text='Server High score', font=(
                                        'Comic Sans MS', 15, 'bold')).place(relx=0.2, rely=0.75)
                                    label8 = tk.Label(label, text='{}'.format(a), font=(
                                        'Comic Sans MS', 15, 'bold')).place(relx=0.7, rely=0.75)

                                    ro.mainloop()
                                yourdetail()
                            if y >= -213 and y <= -191 and x >= 390 and x <= 559:
                                def scoretable():
                                    mycon = sqltor.connect(
                                        host='localhost', user='root', passwd='tiger', database='prac', charset='utf8')
                                    c = mycon.cursor()
                                    ro = tk.Toplevel()
                                    ro.title('Server Score')
                                    canv = tk.Canvas(
                                        ro, height=768, width=1366)
                                    canv.pack()
                                    bg = tk.PhotoImage(file='Nebula.png')
                                    bg_label = tk.Label(ro, image=bg)
                                    bg_label.place(
                                        x=0, y=0, relwidth=1, relheight=1)
                                    frame = tk.Frame(ro, bg='#80c1ff', bd=10)
                                    frame.place(relx=0.05, rely=0.05,
                                                relwidth=0.9, relheight=0.85)

                                    label = tk.Label(frame, bg='#FFE4C4')
                                    label.place(relheight=1, relwidth=0.25)
                                    label1 = tk.Label(frame, bg='#FFE4C4')
                                    label1.place(
                                        relheight=1, relwidth=0.25, relx=0.25)
                                    label2 = tk.Label(frame, bg='#FFE4C4')
                                    label2.place(
                                        relheight=1, relwidth=0.25, relx=0.5)
                                    label3 = tk.Label(frame, bg='#FFE4C4')
                                    label3.place(
                                        relheight=1, relwidth=0.25, relx=0.75)
                                    list1 = tk.Listbox(label, bg='#FFE4C4', font=(
                                        'Comic Sans MS', 15, 'bold'))
                                    list1.insert(1, 'Name')
                                    list1.insert(
                                        2, "________________________________")
                                    c.execute('select name from score')
                                    n = 3
                                    for i in c.fetchall():

                                        list1.insert(n, i[0])
                                        n = n+1
                                    list1.place(relheight=1, relwidth=1)

                                    list2 = tk.Listbox(label1, bg='#FFE4C4', font=(
                                        'Comic Sans MS', 15, 'bold'))
                                    list2.insert(1, 'Score')
                                    list2.insert(
                                        2, "_____________________________________")
                                    c.execute('select score from score')
                                    n = 3
                                    for j in c.fetchall():
                                        list2.insert(n, j[0])
                                        n = n+1
                                    list2.place(relheight=1, relwidth=1)

                                    list3 = tk.Listbox(label2, bg='#FFE4C4', font=(
                                        'Comic Sans MS', 15, 'bold'))
                                    list3.insert(1, 'Attempt')
                                    list3.insert(
                                        2, "______________________________________")
                                    c.execute('select attempts from score')
                                    n = 3
                                    for j in c.fetchall():
                                        list3.insert(n, j[0])
                                        n = n+1
                                    list3.place(relheight=1, relwidth=1)

                                    list4 = tk.Listbox(label3, bg='#FFE4C4', font=(
                                        'Comic Sans MS', 15, 'bold'))
                                    list4.insert(1, 'date')
                                    list4.insert(
                                        2, "____________________________________")
                                    c.execute('select date from score')
                                    n = 3
                                    for j in c.fetchall():
                                        list4.insert(n, j[0])
                                        n = n+1
                                    list4.place(relheight=1, relwidth=1)
                                    ro.mainloop()
                                scoretable()

                        turtle.onscreenclick(btnclick1, 1)

                        tkt = turtle.Turtle()
                        tkt.speed(0)
                        tkt.color('Yellow')
                        tkt.penup()
                        tkt.setposition(-470, -300)
                        tkt.write(''' EXIT''', False, align='center',
                                  font=('Comic Sans MS', 18, 'bold'))
                        tkt.hideturtle()

                        tkl = turtle.Turtle()
                        tkl.speed(0)
                        tkl.color('Yellow')
                        tkl.penup()
                        tkl.setposition(470, -300)
                        tkl.write(''' PLAY AGAIN''', False, align='center', font=(
                            'Comic Sans MS', 18, 'bold'))
                        tkl.hideturtle()

                        tka = turtle.Turtle()
                        tka.speed(0)
                        tka.color('Yellow')
                        tka.penup()
                        tka.setposition(470, -260)
                        tka.write(''' Detailed score''', False, align='center', font=(
                            'Comic Sans MS', 18, 'bold'))
                        tka.hideturtle()

                        tky = turtle.Turtle()
                        tky.speed(0)
                        tky.color('Yellow')
                        tky.penup()
                        tky.setposition(470, -220)
                        tky.write(''' SCORE TABLE''', False, align='center', font=(
                            'Comic Sans MS', 18, 'bold'))
                        tky.hideturtle()

                        def updatescore():
                            global score1
                            global a
                            global c
                            score1 = score

                            mycon = sqltor.connect(
                                host="localhost", user="root", passwd="tiger", database="prac", charset="utf8")
                            c = mycon.cursor()

                            e = 'select score from score where name="{}"'.format(
                                name)
                            c.execute(e)
                            data1 = c.fetchall()

                            for i in data1:
                                t = i[0]

                                if score1 > t:

                                    q = 'update score set score={} where name="{}"'.format(
                                        score1, name)
                                    fd = 'update score set date="{}" where name="{}"'.format(
                                        date, name)
                                    c.execute(q)
                                    c.execute(fd)
                                    mycon.commit()
                        updatescore()

                    def btnclick(x, y):

                        if y >= 11 and y <= 42 and x >= -68 and x <= 68:
                            winsound.PlaySound('btcl.wav', winsound.SND_ASYNC)
                            sc.clear()

                            TR.clear()
                            TA.clear()
                            TB.clear()
                            game1()
                        if y >= -40 and y <= -7 and x >= -67 and x <= 65:
                            winsound.PlaySound('btcl.wav', winsound.SND_ASYNC)
                            winsound.PlaySound(
                                'Halo Theme Song Original.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
                            tkr = turtle.Turtle()
                            tkr.speed(0)
                            tkr.color('Yellow')
                            tkr.penup()
                            tkr.setposition(470, 310)
                            tkr.write('''PLAY GAME''', False, align='center', font=(
                                'Comic Sans MS', 18, 'bold'))
                            tkr.hideturtle()

                            def btnclick2(x, y):

                                if y >= 319 and y <= 339 and x >= 401 and x <= 538:
                                    winsound.PlaySound(
                                        'btcl.wav', winsound.SND_ASYNC)
                                    s.clear()
                                    st.clear()
                                    s1.clear()
                                    s2.clear()
                                    s3.clear()
                                    s4.clear()
                                    s5.clear()
                                    s6.clear()
                                    s7.clear()
                                    tkr.clear()
                                    game1()

                            turtle.onscreenclick(btnclick2, 1)
                            TR.clear()
                            TA.clear()
                            TB.clear()
                            Tl.clear()
                            scr = turtle.Screen()
                            scr.title('SPACE INVADER')
                            turtle.setup(1366, 768)
                            turtle.screensize(1366, 768)
                            scr.bgpic('space1.png')
                            mycon = sqltor.connect(
                                host="localhost", user="root", passwd="tiger", database="prac", charset="utf8")
                            c = mycon.cursor()
                            d = 'select name from score'
                            l = 'select attempts from score'
                            u = 'select score from score'
                            w = 'select date from score'
                            c.execute(d)
                            data = c.fetchall()
                            c.execute(l)
                            data1 = c.fetchall()
                            c.execute(u)
                            data2 = c.fetchall()
                            c.execute(w)
                            data3 = c.fetchall()

                            st = turtle.Turtle()
                            st.speed(0)
                            st.color('Yellow')
                            st.penup()
                            st.setposition(0, 280)
                            st.write('SCORE TABLE', False, align='center',
                                     font=('Comic Sans MS', 18, 'bold'))
                            st.hideturtle()

                            s1 = turtle.Turtle()
                            s1.speed(0)
                            s1.color('Yellow')
                            s1.penup()
                            s1.setposition(-500, 250)
                            s1.write('Name', False, align='center',
                                     font=('Arial', 15, 'normal'))
                            s1.hideturtle()

                            s4 = turtle.Turtle()
                            s4.speed(0)
                            s4.color('Yellow')
                            s4.penup()
                            s4.setposition(-200, 250)
                            s4.write('Attempts', False, align='center',
                                     font=('Arial', 15, 'normal'))
                            s4.hideturtle()

                            s2 = turtle.Turtle()
                            s2.speed(0)
                            s2.color('Yellow')
                            s2.penup()
                            s2.setposition(200, 250)
                            s2.write('Score', False, align='center',
                                     font=('Arial', 15, 'normal'))
                            s2.hideturtle()

                            s3 = turtle.Turtle()
                            s3.speed(0)
                            s3.color('Yellow')
                            s3.penup()
                            s3.setposition(500, 250)
                            s3.write('Date', False, align='center',
                                     font=('Arial', 15, 'normal'))
                            s3.hideturtle()

                            s = turtle.Turtle()
                            s.speed(0)
                            s.color('Yellow')
                            s.penup()
                            s.setposition(-500, 220)
                            for row in data:
                                i = row[0]
                                s.write(i, False, align='center',
                                        font=('Arial', 15, 'normal'))

                                y = s.ycor()
                                y -= 20
                                s.sety(y)

                            s.hideturtle()
                            s5 = turtle.Turtle()
                            s5.speed(0)
                            s5.color('Yellow')
                            s5.penup()
                            s5.setposition(-200, 220)
                            for row in data1:
                                i = row[0]
                                s5.write(i, False, align='center',
                                         font=('Arial', 15, 'normal'))

                                y = s5.ycor()
                                y -= 20
                                s5.sety(y)

                            s5.hideturtle()
                            s6 = turtle.Turtle()
                            s6.speed(0)
                            s6.color('Yellow')
                            s6.penup()
                            s6.setposition(200, 220)
                            for row in data2:
                                i = row[0]
                                s6.write(i, False, align='center',
                                         font=('Arial', 15, 'normal'))

                                y = s6.ycor()
                                y -= 20
                                s6.sety(y)

                            s6.hideturtle()
                            s7 = turtle.Turtle()
                            s7.speed(0)
                            s7.color('Yellow')
                            s7.penup()
                            s7.setposition(500, 220)
                            for row in data3:
                                i = row[0]
                                s7.write(i, False, align='center',
                                         font=('Arial', 15, 'normal'))

                                y = s7.ycor()
                                y -= 20
                                s7.sety(y)

                            s7.hideturtle()
                        if y >= -99 and y <= -68 and x >= -51 and x <= 52:
                            winsound.PlaySound('btcl.wav', winsound.SND_ASYNC)
                            sc.exitonclick()
                        score1 = score

                    turtle.onscreenclick(btnclick, 1)
                    turtle.listen()
                    turtle.done()

                def game2():
                    root6.destroy()
                    winsound.PlaySound(
                        'apex.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
                    cursor = mycon.cursor()
                    sc = turtle.Screen()
                    sc.title('SPACE WAR')
                    turtle.setup(1366, 768)
                    sc.bgcolor('black')
                    sc.tracer(0)
                    sc.update()

                    sc.bgpic('spacewar.png')

                    # draw score

                    Tl = turtle.Turtle()
                    Tl.speed(0)
                    Tl.color('yellow')
                    Tl.penup()
                    Tl.setposition(0, 80)
                    text34 = 'Are You Ready Captain {}?'.format(name)
                    Tl.write(text34, False, align='center',
                             font=('Comic Sans MS', 20, 'normal'))
                    Tl.hideturtle()
                    TR = turtle.Turtle()
                    TR.speed(0)
                    TR.color('yellow')
                    TR.penup()
                    TR.setposition(0, 0)
                    TR.write('START', False, align='center',
                             font=('Comic Sans MS', 30, 'bold'))
                    TR.hideturtle()

                    TA = turtle.Turtle()
                    TA.speed(0)
                    TA.color('yellow')
                    TA.penup()
                    TA.setposition(0, -50)
                    TA.write('SCORE', False, align='center',
                             font=('Comic Sans MS', 30, 'bold'))
                    TA.hideturtle()

                    TB = turtle.Turtle()
                    TB.speed(0)
                    TB.color('yellow')
                    TB.penup()
                    TB.setposition(0, -110)
                    TB.write('EXIT', False, align='center',
                             font=('Comic Sans MS', 30, 'bold'))
                    TB.hideturtle()
                    e = 0
                    bulletstate = 'ready'
                    playerspeed = 1.2
                    playerlives = 3
                    score = 0
                    enemyspeed = 1.5
                    allyspeed = 1
                    score1 = 0

                    def game1():
                        global e
                        global bulletstate
                        global playerspeed
                        global playerlives
                        global score
                        global enemyspeed
                        global allyspeed
                        wn = turtle.Screen()
                        wn.bgcolor('black')
                        wn.bgpic('space1.png')
                        wn.title('SPACE WAR')
                        wn.tracer(0)
                        wn.setup(width=1366, height=768)

                        turtle.register_shape('invader.gif')

                        player = turtle.Turtle()
                        player.color('white')
                        player.shape('triangle')
                        player.shapesize(
                            stretch_wid=0.6, stretch_len=1.1, outline=None)
                        player.speed(0)
                        player.setposition(0, 0)
                        player.penup()
                        playerspeed = 1.2
                        playerlives = 3
                        score = 0
                        # draw a score
                        score_pen = turtle.Turtle()
                        score_pen.speed(0)
                        score_pen.color('white')
                        score_pen.penup()
                        score_pen.setposition(-290, 320)
                        scorestring = "Score : %s" % score
                        score_pen.write(scorestring, False, align='left', font=(
                            'Comic Sans MS', 10, 'bold'))
                        score_pen.hideturtle()

                        lives = turtle.Turtle()
                        lives.speed(0)
                        lives.color('white')
                        lives.penup()
                        lives.setposition(-200, 320)
                        livestring = "life  : %s" % playerlives
                        lives.write(livestring, False, align='left',
                                    font=('Comic Sans MS', 10, 'bold'))
                        lives.hideturtle()

                        enemies = []
                        for i in range(3):
                            enemies.append(turtle.Turtle())
                        for enemy in enemies:
                            enemy.color('red')
                            enemy.shape('invader.gif')
                            enemy.speed(0)
                            enemy.penup()
                            enemy.setposition(
                                random.randint(-250, 250), random.randint(-250, 250))
                            enemy.setheading(random.randint(0, 360))
                        enemyspeed = 1.5

                        allies = []
                        for i in range(2):
                            allies.append(turtle.Turtle())
                        for ally in allies:
                            ally.color('blue')
                            ally.shape('square')
                            ally.speed(0)
                            ally.penup()
                            ally.setposition(
                                random.randint(-250, 250), random.randint(-250, 250))
                            ally.setheading(random.randint(0, 360))
                        allyspeed = 1

                        bullet = turtle.Turtle()
                        bullet.color('yellow')
                        bullet.shape('triangle')
                        bullet.speed(0)
                        bullet.penup()
                        bullet.setposition(-1000, -1000)
                        bullet.shapesize(0.3, 0.3)

                        bullet.hideturtle()
                        bulletspeed = 5
                        bulletstate = 'ready'

                        # border
                        bd = turtle.Turtle()
                        bd.speed(0)
                        bd.color('white')
                        bd.penup()
                        bd.setposition(-300, -300)
                        bd.pensize(3)
                        bd.pendown()
                        for side in range(4):
                            bd.fd(600)
                            bd.lt(90)
                        bd.hideturtle()

                        score3 = turtle.Turtle()
                        score3.speed(0)
                        score3.color('white')
                        score3.penup()
                        score3.hideturtle()
                        score3.setposition(-100, 320)
                        e = 'select attemptwar from score where name="{}"'.format(
                            name)
                        cursor.execute(e)
                        data8 = cursor.fetchall()
                        for row in data8:
                            for i in row:
                                e = i+1
                        r = 'update score set attemptwar={} where name="{}"'.format(
                            e, name)
                        cursor.execute(r)
                        mycon.commit()
                        scorestr = 'Attempts:%s' % e
                        score3.write(scorestr, True, font=(
                            'Comic Sans MS', 10, 'bold'))
                        score_p1 = turtle.Turtle()
                        score_p1.speed(0)
                        score_p1.color('white')
                        score_p1.penup()
                        score_p1.setposition(0, 320)
                        it = 'select scorewar from score where name="{}"'.format(
                            name)
                        cursor.execute(it)
                        dt = cursor.fetchall()
                        for i in dt:
                            scorestr = "Your Max Score : %s" % i
                            score_p1.write(scorestr, False, align='left', font=(
                                'Comic Sans MS', 10, 'bold'))
                        score_p1.hideturtle()

                        score_p = turtle.Turtle()

                        score_p.speed(0)
                        score_p.color('white')
                        score_p.penup()
                        score_p.setposition(150, 320)
                        it = 'select max(scorewar) from score'
                        cursor.execute(it)
                        dt = cursor.fetchall()
                        for i in dt:
                            scorestr = "Highest score : %s" % i
                            score_p.write(scorestr, False, align='left', font=(
                                'Comic Sans MS', 10, 'bold'))
                        score_p.hideturtle()

                        # movements

                        def turn_left():
                            player.lt(45)

                        def turn_right():
                            player.rt(45)

                        def accelerate():
                            global playerspeed
                            playerspeed += 0.2

                        def decelerate():
                            global playerspeed
                            playerspeed -= 0.2

                        def is_collision(t1, t2):
                            x = t1.distance(t2)
                            if x < 15:
                                return True
                            else:
                                return False

                        def fire():
                            global bulletstate
                            if bulletstate == 'ready':
                                winsound.PlaySound(
                                    'laser.wav', winsound.SND_ASYNC)
                                bulletstate = 'shoot'
                                x = player.xcor()
                                y = player.ycor()+10
                                bullet.setheading(player.heading())
                                bullet.setposition(x, y)
                                bullet.showturtle()

                        # keyboard bindings
                        turtle.onkey(turn_left, 'Left')
                        turtle.onkey(turn_right, 'Right')
                        turtle.onkey(accelerate, 'Up')
                        turtle.onkey(decelerate, 'Down')
                        turtle.onkey(fire, 'space')
                        turtle.listen()

                        # Main Game loop
                        while True:
                            wn.update()

                            player.fd(playerspeed)

                            if player.xcor() > 290:
                                player.setx(290)
                                player.rt(60)
                            if player.xcor() < -290:
                                player.setx(-290)
                                player.rt(60)
                            if player.ycor() > 290:
                                player.sety(290)
                                player.rt(60)
                            if player.ycor() < -290:
                                player.sety(-290)
                                player.rt(60)
                            for enemy in enemies:
                                if enemy.xcor() > 290:
                                    enemy.setx(290)
                                    enemy.rt(60)
                                if enemy.xcor() < -290:
                                    enemy.setx(-290)
                                    enemy.rt(60)
                                if enemy.ycor() > 290:
                                    enemy.sety(290)
                                    enemy.rt(60)
                                if enemy.ycor() < -290:
                                    enemy.sety(-290)
                                    enemy.rt(60)
                                enemy.fd(enemyspeed)
                            for ally in allies:
                                if ally.xcor() > 290:
                                    ally.setx(290)
                                    ally.lt(60)
                                if ally.xcor() < -290:
                                    ally.setx(-290)
                                    ally.lt(60)
                                if ally.ycor() > 290:
                                    ally.sety(290)
                                    ally.lt(60)
                                if ally.ycor() < -290:
                                    ally.sety(-290)
                                    ally.lt(60)
                                ally.fd(allyspeed)
                            for enemy in enemies:
                                if is_collision(player, enemy):
                                    x = random.randint(-250, 250)
                                    y = random.randint(-250, 250)
                                    winsound.PlaySound(
                                        'explosion.wav', winsound.SND_ASYNC)
                                    enemy.goto(x, y)
                                    player.goto(0, 0)
                                    if score != 0:
                                        score -= 10
                                        scorestring = 'Score: %s' % score
                                        score_pen.clear()
                                        score_pen.write(scorestring, False, align='left', font=(
                                            'Arial', 14, 'normal'))
                                    if playerlives != 0:
                                        playerlives -= 1
                                        lt = 'life: %s' % playerlives
                                        lives.clear()
                                        lives.write(lt, False, align='left', font=(
                                            'Arial', 14, 'normal'))
                            if playerlives == 0:
                                break

                            if bulletstate == 'shoot':
                                bullet.fd(bulletspeed)
                            if bullet.xcor() > 290:
                                bulletstate = 'ready'
                                bullet.goto(-1000, -1000)

                            if bullet.xcor() < -290:
                                bulletstate = 'ready'
                                bullet.goto(-1000, -1000)
                            if bullet.ycor() > 290:
                                bulletstate = 'ready'
                                bullet.goto(-1000, -1000)
                            if bullet.ycor() < -290:
                                bulletstate = 'ready'
                                bullet.goto(-1000, -1000)
                            for enemy in enemies:
                                if is_collision(bullet, enemy):
                                    winsound.PlaySound(
                                        'invaderkilled.wav', winsound.SND_ASYNC)
                                    x = random.randint(-250, 250)
                                    y = random.randint(-250, 250)
                                    enemy.goto(x, y)
                                    score += 10
                                    scorestring = 'Score: %s' % score
                                    score_pen.clear()
                                    score_pen.write(scorestring, False, align='left', font=(
                                        'Arial', 14, 'normal'))

                            for ally in allies:
                                if is_collision(bullet, ally):
                                    winsound.PlaySound(
                                        'explosion.wav', winsound.SND_ASYNC)
                                    x = random.randint(-250, 250)
                                    y = random.randint(-250, 250)
                                    ally.goto(x, y)
                                    if score != 0:
                                        score -= 10
                                        scorestring = 'Score: %s' % score
                                        score_pen.clear()
                                        score_pen.write(scorestring, False, align='left', font=(
                                            'Arial', 14, 'normal'))
                        wn.clear()
                        st = turtle.Screen()
                        st.bgpic('game over.png')
                        st.title('SPACE WAR')
                        st.bgcolor('black')
                        winsound.PlaySound(
                            'apex.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
                        ks = turtle.Turtle()
                        ks.speed(0)
                        ks.color('white')
                        ks.penup()
                        ks.setposition(0, 250)
                        ks.write(' %s Scored:%s' % (name, score), False,
                                 align='center', font=('Comic Sans MS', 18, 'bold'))
                        ks.hideturtle()
                        tks = turtle.Turtle()
                        tks.speed(0)
                        tks.color('white')
                        tks.penup()
                        tks.setposition(0, 150)
                        tks.write(''' THANK YOU FOR PLAYING I HOPE YOU LIKED IT ( - : 
                                             Your Progress Will Be automatically saved if your score is more
                                             Click Below to close the game''', False, align='center', font=('Comic Sans MS', 18, 'bold'))
                        tks.hideturtle()

                        tka = turtle.Turtle()
                        tka.speed(0)
                        tka.color('Yellow')
                        tka.penup()
                        tka.setposition(470, -260)
                        tka.write(''' Detailed score''', False, align='center', font=(
                            'Comic Sans MS', 18, 'bold'))
                        tka.hideturtle()

                        tky = turtle.Turtle()
                        tky.speed(0)
                        tky.color('Yellow')
                        tky.penup()
                        tky.setposition(470, -220)
                        tky.write(''' SCORE TABLE''', False, align='center', font=(
                            'Comic Sans MS', 18, 'bold'))
                        tky.hideturtle()

                        def btnclick1(x, y):

                            if y >= -294 and y <= -272 and x <= 496 and x >= 435:
                                winsound.PlaySound(
                                    'btcl.wav', winsound.SND_ASYNC)
                                st.clear()
                                game1()

                            if y >= -294 and y <= -272 and x >= -496 and x <= -435:
                                winsound.PlaySound(
                                    'btcl.wav', winsound.SND_ASYNC)
                                wn.exitonclick()
                            if y >= -253 and y <= -232 and x >= 392 and x <= 556:
                                def yourdetail():

                                    mycon = sqltor.connect(
                                        host='localhost', user='root', passwd='tiger', database='prac', charset='utf8')
                                    c = mycon.cursor()
                                    ro = tk.Toplevel()
                                    ro.title('Detailed score')
                                    canvas = tk.Canvas(
                                        ro, height=400, width=600)
                                    canvas.pack()
                                    bg = tk.PhotoImage(file='Nebula.png')
                                    bg_label = tk.Label(ro, image=bg)
                                    bg_label.place(
                                        x=0, y=0, relwidth=1, relheight=1)
                                    ro.resizable(False, False)
                                    frame = tk.Frame(ro, bg='#80c1ff', bd=10)
                                    frame.place(
                                        relx=0.5, rely=0.1, relwidth=0.9, relheight=0.9, anchor='n')
                                    label = tk.Label(frame, bg='#FFE4C4', font=(
                                        'Comic Sans MS', 10, 'bold'))
                                    label.place(relheight=1, relwidth=1)
                                    label1 = tk.Label(label, text='Player', font=(
                                        'Comic Sans MS', 15, 'bold')).place(relx=0.2)
                                    e = 'select name,attemptwar,scorewar,datewar from score where name="{}"'.format(
                                        name)
                                    c.execute(e)
                                    data1 = c.fetchall()

                                    for i in data1:

                                        u = i[1]
                                        y = i[2]
                                    c.execute(
                                        'select max(scorewar) from score')
                                    data2 = c.fetchall()
                                    for e in data2:
                                        a = e[0]

                                    label2 = tk.Label(label, text='{}'.format(name), font=(
                                        'Comic Sans MS', 15, 'bold')).place(relx=0.7)
                                    label3 = tk.Label(label, text=' You Scored', font=(
                                        'Comic Sans MS', 15, 'bold')).place(relx=0.2, rely=0.25)
                                    label4 = tk.Label(label, text='{}'.format(score), font=(
                                        'Comic Sans MS', 15, 'bold')).place(relx=0.7, rely=0.25)
                                    label5 = tk.Label(label, text='Your high score', font=(
                                        'Comic Sans MS', 15, 'bold')).place(relx=0.2, rely=0.5)
                                    label6 = tk.Label(label, text='{}'.format(y), font=(
                                        'Comic Sans MS', 15, 'bold')).place(relx=0.7, rely=0.5)
                                    label7 = tk.Label(label, text='Server High score', font=(
                                        'Comic Sans MS', 15, 'bold')).place(relx=0.2, rely=0.75)
                                    label8 = tk.Label(label, text='{}'.format(a), font=(
                                        'Comic Sans MS', 15, 'bold')).place(relx=0.7, rely=0.75)

                                    ro.mainloop()
                                yourdetail()
                            if y >= -213 and y <= -191 and x >= 390 and x <= 559:
                                def scoretable():
                                    mycon = sqltor.connect(
                                        host='localhost', user='root', passwd='tiger', database='prac', charset='utf8')
                                    c = mycon.cursor()
                                    ro = tk.Toplevel()
                                    ro.title('Server Score')
                                    canv = tk.Canvas(
                                        ro, height=768, width=1366)
                                    canv.pack()
                                    bg = tk.PhotoImage(file='Nebula.png')
                                    bg_label = tk.Label(ro, image=bg)
                                    bg_label.place(
                                        x=0, y=0, relwidth=1, relheight=1)
                                    frame = tk.Frame(ro, bg='#80c1ff', bd=10)
                                    frame.place(relx=0.05, rely=0.05,
                                                relwidth=0.9, relheight=0.85)

                                    label = tk.Label(frame, bg='#FFE4C4')
                                    label.place(relheight=1, relwidth=0.25)
                                    label1 = tk.Label(frame, bg='#FFE4C4')
                                    label1.place(
                                        relheight=1, relwidth=0.25, relx=0.25)
                                    label2 = tk.Label(frame, bg='#FFE4C4')
                                    label2.place(
                                        relheight=1, relwidth=0.25, relx=0.5)
                                    label3 = tk.Label(frame, bg='#FFE4C4')
                                    label3.place(
                                        relheight=1, relwidth=0.25, relx=0.75)
                                    list1 = tk.Listbox(label, bg='#FFE4C4', font=(
                                        'Comic Sans MS', 15, 'bold'))
                                    list1.insert(1, 'Name')
                                    list1.insert(
                                        2, "________________________________")
                                    c.execute('select name from score')
                                    n = 3
                                    for i in c.fetchall():

                                        list1.insert(n, i[0])
                                        n = n+1
                                    list1.place(relheight=1, relwidth=1)

                                    list2 = tk.Listbox(label1, bg='#FFE4C4', font=(
                                        'Comic Sans MS', 15, 'bold'))
                                    list2.insert(1, 'Score')
                                    list2.insert(
                                        2, "_____________________________________")
                                    c.execute('select scorewar from score')
                                    n = 3
                                    for j in c.fetchall():
                                        list2.insert(n, j[0])
                                        n = n+1
                                    list2.place(relheight=1, relwidth=1)

                                    list3 = tk.Listbox(label2, bg='#FFE4C4', font=(
                                        'Comic Sans MS', 15, 'bold'))
                                    list3.insert(1, 'Attempt')
                                    list3.insert(
                                        2, "______________________________________")
                                    c.execute('select attemptwar from score')
                                    n = 3
                                    for j in c.fetchall():
                                        list3.insert(n, j[0])
                                        n = n+1
                                    list3.place(relheight=1, relwidth=1)

                                    list4 = tk.Listbox(label3, bg='#FFE4C4', font=(
                                        'Comic Sans MS', 15, 'bold'))
                                    list4.insert(1, 'date')
                                    list4.insert(
                                        2, "____________________________________")
                                    c.execute('select datewar from score')
                                    n = 3
                                    for j in c.fetchall():
                                        list4.insert(n, j[0])
                                        n = n+1
                                    list4.place(relheight=1, relwidth=1)
                                    ro.mainloop()
                                scoretable()

                        turtle.onscreenclick(btnclick1, 1)
                        tkt = turtle.Turtle()
                        tkt.speed(0)
                        tkt.color('Yellow')
                        tkt.penup()
                        tkt.setposition(-470, -300)
                        tkt.write(''' EXIT''', False, align='center',
                                  font=('Comic Sans MS', 18, 'bold'))
                        tkt.hideturtle()
                        tkl = turtle.Turtle()
                        tkl.speed(0)
                        tkl.color('Yellow')
                        tkl.penup()
                        tkl.setposition(470, -300)
                        tkl.write(''' PLAY AGAIN''', False, align='center', font=(
                            'Comic Sans MS', 18, 'bold'))
                        tkl.hideturtle()

                        def updatescore():

                            global score1
                            global a
                            global c
                            score1 = score

                            mycon = sqltor.connect(
                                host="localhost", user="root", passwd="tiger", database="prac", charset="utf8")
                            c = mycon.cursor()

                            e = 'select scorewar from score where name="{}"'.format(
                                name)
                            c.execute(e)
                            data1 = c.fetchall()

                            for i in data1:
                                t = i[0]

                                if score1 > t:

                                    q = 'update score set scorewar={} where name="{}"'.format(
                                        score1, name)
                                    fd = 'update score set datewar="{}" where name="{}"'.format(
                                        date, name)
                                    c.execute(q)
                                    c.execute(fd)
                                    mycon.commit()
                        updatescore()

                    def btnclick(x, y):

                        if y >= 11 and y <= 42 and x >= -68 and x <= 68:
                            winsound.PlaySound('btcl.wav', winsound.SND_ASYNC)
                            sc.clear()

                            TR.clear()
                            TA.clear()
                            TB.clear()
                            game1()
                        if y >= -40 and y <= -7 and x >= -67 and x <= 65:
                            winsound.PlaySound('btcl.wav', winsound.SND_ASYNC)
                            winsound.PlaySound(
                                'apex.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
                            tkr = turtle.Turtle()
                            tkr.speed(0)
                            tkr.color('Yellow')
                            tkr.penup()
                            tkr.setposition(470, 300)
                            tkr.write('''PLAY GAME''', False, align='center', font=(
                                'Comic Sans MS', 18, 'bold'))
                            tkr.hideturtle()

                            def btnclick2(x, y):

                                if y >= 307 and y <= 330 and x >= 401 and x <= 538:
                                    winsound.PlaySound(
                                        'btcl.wav', winsound.SND_ASYNC)
                                    s.clear()
                                    st.clear()
                                    s1.clear()
                                    s2.clear()
                                    s3.clear()
                                    s4.clear()
                                    s5.clear()
                                    s6.clear()
                                    s7.clear()
                                    tkr.clear()
                                    game1()

                            turtle.onscreenclick(btnclick2, 1)
                            TR.clear()
                            TA.clear()
                            TB.clear()
                            Tl.clear()
                            scr = turtle.Screen()
                            turtle.setup(1366, 768)
                            turtle.screensize(1366, 768)
                            scr.bgpic('space1.png')
                            scr.title('SPACE WAR')
                            mycon = sqltor.connect(
                                host="localhost", user="root", passwd="tiger", database="prac", charset="utf8")

                            c = mycon.cursor()
                            d = 'select name from score'
                            l = 'select attemptwar from score'
                            u = 'select scorewar from score'
                            w = 'select datewar from score'
                            c.execute(d)
                            data = c.fetchall()
                            c.execute(l)
                            data1 = c.fetchall()
                            c.execute(u)
                            data2 = c.fetchall()
                            c.execute(w)
                            data3 = c.fetchall()

                            st = turtle.Turtle()
                            st.speed(0)
                            st.color('Yellow')
                            st.penup()
                            st.setposition(0, 280)
                            st.write('SCORE TABLE', False, align='center',
                                     font=('Comic Sans MS', 18, 'bold'))
                            st.hideturtle()

                            s1 = turtle.Turtle()
                            s1.speed(0)
                            s1.color('Yellow')
                            s1.penup()
                            s1.setposition(-500, 250)
                            s1.write('Name', False, align='center',
                                     font=('Arial', 15, 'normal'))
                            s1.hideturtle()

                            s4 = turtle.Turtle()
                            s4.speed(0)
                            s4.color('Yellow')
                            s4.penup()
                            s4.setposition(-200, 250)
                            s4.write('Attempts', False, align='center',
                                     font=('Arial', 15, 'normal'))
                            s4.hideturtle()

                            s2 = turtle.Turtle()
                            s2.speed(0)
                            s2.color('Yellow')
                            s2.penup()
                            s2.setposition(200, 250)
                            s2.write('Score', False, align='center',
                                     font=('Arial', 15, 'normal'))
                            s2.hideturtle()

                            s3 = turtle.Turtle()
                            s3.speed(0)
                            s3.color('Yellow')
                            s3.penup()
                            s3.setposition(500, 250)
                            s3.write('Date', False, align='center',
                                     font=('Arial', 15, 'normal'))
                            s3.hideturtle()

                            s = turtle.Turtle()
                            s.speed(0)
                            s.color('Yellow')
                            s.penup()
                            s.setposition(-500, 220)
                            for row in data:
                                i = row[0]
                                s.write(i, False, align='center',
                                        font=('Arial', 15, 'normal'))

                                y = s.ycor()
                                y -= 20
                                s.sety(y)

                            s.hideturtle()
                            s5 = turtle.Turtle()
                            s5.speed(0)
                            s5.color('Yellow')
                            s5.penup()
                            s5.setposition(-200, 220)
                            for row in data1:
                                i = row[0]
                                s5.write(i, False, align='center',
                                         font=('Arial', 15, 'normal'))

                                y = s5.ycor()
                                y -= 20
                                s5.sety(y)

                            s5.hideturtle()
                            s6 = turtle.Turtle()
                            s6.speed(0)
                            s6.color('Yellow')
                            s6.penup()
                            s6.setposition(200, 220)
                            for row in data2:
                                i = row[0]
                                s6.write(i, False, align='center',
                                         font=('Arial', 15, 'normal'))

                                y = s6.ycor()
                                y -= 20
                                s6.sety(y)

                            s6.hideturtle()
                            s7 = turtle.Turtle()
                            s7.speed(0)
                            s7.color('Yellow')
                            s7.penup()
                            s7.setposition(500, 220)
                            for row in data3:
                                i = row[0]
                                s7.write(i, False, align='center',
                                         font=('Arial', 15, 'normal'))

                                y = s7.ycor()
                                y -= 20
                                s7.sety(y)

                            s7.hideturtle()
                        if y >= -99 and y <= -68 and x >= -51 and x <= 52:
                            winsound.PlaySound('btcl.wav', winsound.SND_ASYNC)
                            sc.exitonclick()

                    turtle.onscreenclick(btnclick, 1)
                    turtle.listen()
                    turtle.done()

                def how1():
                    root10 = tk.Toplevel()
                    root10.title('instruction space invader')
                    height = 768
                    width = 1366
                    canvasll = tk.Canvas(root10, height=height, width=width)
                    canvasll.pack()
                    bgll = tk.PhotoImage(file='Nebula.png')
                    text = '''CONTROLS
Move left-- Left Arrow
Move right-- Right Arrow
Fire SPACE



Instructions

Kill enemies using your weapon
1 enemy killed =10 points
if enemy is approaching closer then you should
quickly kill them
if they reach you Game Over i.e Earth has been captured
By Aliens'''
                    bg_labelll = tk.Label(root10, image=bgll)
                    bg_labelll.place(x=0, y=0, relwidth=1, relheight=1)

                    framell = tk.Frame(bg_labelll, bg='#80c1ff', bd=10)
                    framell.place(relx=0.5, rely=0.1, relwidth=0.8,
                                  relheight=0.8, anchor='n')

                    bg_labell = tk.Label(framell, text=text, font=(
                        'Comic Sans MS', 12, 'bold'))
                    bg_labell.pack(fill='both', expand='True')
                    root10.mainloop()

                def how2():
                    root11 = tk.Toplevel()
                    root11.title('instruction space war')
                    height = 768
                    width = 1366
                    canvasl2 = tk.Canvas(root11, height=height, width=width)
                    canvasl2.pack()
                    bgl2 = tk.PhotoImage(file='Nebula.png')
                    textl2 = '''CONTROLS
Move left --Left Arrow
Move right-- Right Arrow
Increasing Speed --Up arrow
Decreasing Speed -- Down Arrow
Fire Space



Instructions

Kill enemies using your weapon
1 enemy killed =10 points
Be Careful Green One's are enemies
and blue one's are your allies
if you kill your allies or get crashed to
enemies point gets decreased by 10
You Have Total Of 3 life
which gets depleted after every collisions
with enemy
If  life =0 then Game Over and You were
failed to help your allies'''
                    bg_labell2 = tk.Label(root11, image=bgl2)
                    bg_labell2.place(x=0, y=0, relwidth=1, relheight=1)

                    framel2 = tk.Frame(bg_labell2, bg='#80c1ff', bd=10)
                    framel2.place(relx=0.5, rely=0.1, relwidth=0.8,
                                  relheight=0.8, anchor='n')
                    bg_label2 = tk.Label(framel2, text=textl2, font=(
                        'Comic Sans MS', 12, 'bold'))
                    bg_label2.pack(fill='both', expand='True')
                    root11.mainloop()

                root2.destroy()
                root.destroy()
                height = 768
                width = 1366
                root6 = tk.Tk()
                root6.title('choose game')
                canvas5 = tk.Canvas(root6, height=height, width=width)
                canvas5.pack()
                bg6 = tk.PhotoImage(file='Nebula.png')
                bg_label6 = tk.Label(root6, image=bg6)
                bg_label6.place(x=0, y=0, relwidth=1, relheight=1)
                frame6 = tk.Frame(root6, bg='#80c1ff', bd=10)
                frame6.place(relx=0.5, rely=0.15, relwidth=0.75,
                             relheight=0.75, anchor='n')
                frame16 = tk.Frame(root6, bg='#FF4500', bd=15)
                frame16.place(relx=0.5, rely=0.02, relwidth=0.75,
                              relheight=0.08, anchor='n')
                g1 = tk.PhotoImage(file='BeFunky-photo.png')
                g2 = tk.PhotoImage(file='BeFunky-photo(4).png')

                frame18 = tk.Frame(root6, bg='#FF4500', bd=15)
                frame18.place(relx=0.03, rely=0.15,
                              relwidth=0.08, relheight=0.75)
                frame21 = tk.Frame(root6, bg='#FF4500', bd=15)
                frame21.place(relx=0.89, rely=0.15,
                              relwidth=0.08, relheight=0.75)
                label6 = tk.Label(frame16, text='Earth is now in war with Aliens , Protect Earth by choosing following two paths',
                                  bg='#FFE4C4', font=('Comic Sans MS', 10, 'bold'))
                label6.place(relheight=1, relwidth=1)
                text10 = '''How
to
Fight
Space
Invader
'''
                button23 = tk.Button(frame18, text=text10, bg='#FFE4C4', font=(
                    'Comic Sans MS', 10, 'bold'), command=how1)
                button23.place(relheight=1, relwidth=1)
                text21 = '''How
To
Fight
Space
War'''
                button24 = tk.Button(frame21, text=text21, justify='center', bg='#FFE4C4', font=(
                    'Comic Sans MS', 10, 'bold'), command=how2)
                button24.place(relheight=1, relwidth=1)
                text6 = '''SPACE INVADER

Invaders are here
Be a Hero
and
Protect Earth
'''
                button6 = tk.Button(frame6, text=text6, bg='#FFE4C4', image=g1, font=(
                    'Comic Sans MS', 16, 'bold'), command=game)
                button6.place(relheight=1, relwidth=0.5)
                text16 = '''SPACE WAR

While your friend
protecting the earth
be a hero
and help him
by stoping
enemies ships
from
reaching  '''
                button16 = tk.Button(frame6, text=text16, justify='center', bg='#FFE4C4', image=g2, font=(
                    'Comic Sans MS', 16, 'bold'), command=game2)
                button16.place(relheight=1, relwidth=0.5, relx=0.5)
                root6.mainloop()

            else:
                label8 = tk.Label(frame7, text=ifnot(),
                                  bg='#FFE4C4', font=('Comic Sans MS', 14))
                label8.pack(expand='true')

        else:
            label8 = tk.Label(frame7, text=ifnot(),
                              bg='#FFE4C4', font=('Comic Sans MS', 14))
            label8.pack(expand='true')

    height = 768
    width = 1366
    root2 = tk.Toplevel()
    root2.title('login')
    canvas1 = tk.Canvas(root2, height=height, width=width)
    canvas1.pack()
    bg2 = tk.PhotoImage(file='Nebula.png')
    label2 = tk.Label(root2, image=bg2)
    label2.place(x=0, y=0, relwidth=1, relheight=1)

    def tick():
        global date
        date = date.today()
        tick2 = time.strftime("%H:%M:%S")
        clock.config(text='''{}
    {}'''.format(date, tick2))
        clock.after(200, tick)
    frame123 = tk.Frame(root2, bg='#80c1ff', bd=10)
    frame123.place(relx=0.075, rely=0.001, relwidth=0.09,
                   relheight=0.1, anchor='n')
    clock = tk.Label(frame123, font=('Comic Sans MS', 8, 'bold'))
    clock.place(relheight=1, relwidth=1)
    tick()
    frame3 = tk.Frame(root2, bg='#FF4500', bd=15)
    frame3.place(relx=0.14, rely=0.3, relwidth=0.75, relheight=0.08)
    frame4 = tk.Frame(root2, bg='#FF4500', bd=15)
    frame4.place(relx=0.14, rely=0.45, relwidth=0.75, relheight=0.08)
    frame5 = tk.Frame(root2, bg='#FF4500', bd=15)
    frame5.place(relx=0.14, rely=0.6, relwidth=0.75, relheight=0.08)
    label5 = tk.Label(frame3, text='Name', bg='#FFE4C4',
                      font=('Comic Sans MS', 14, 'bold'))
    label5.place(relheight=1, relwidth=0.25)
    label6 = tk.Label(frame4, text='Password', bg='#FFE4C4',
                      font=('Comic Sans MS', 14, 'bold'))
    label6.place(relheight=1, relwidth=0.25)
    entry7 = tk.Entry(frame3, font=('Comic Sans MS', 14, 'bold'))
    entry7.place(relheight=1, relwidth=0.75, relx=0.25)
    entry8 = tk.Entry(frame4, show='*', font=('Comic Sans MS', 14, 'bold'))
    entry8.place(relheight=1, relwidth=0.75, relx=0.25)
    button2 = tk.Button(frame5, text='login account', bg='#FFE4C4', font=(
        'Comic Sans MS', 15, 'bold'), command=lambda: login1(entry7.get(), entry8.get()))
    button2.place(relheight=1, relwidth=0.3, relx=0.35)
    frame7 = tk.Frame(root2, bg='white', bd=15)
    frame7.place(relx=0.14, rely=0.75, relwidth=0.75, relheight=0.08)
    root2.mainloop()


def ift():
    return 'entered username already exists'


def register():
    # start from here create register
    def register1(a, b):

        cursor = mycon.cursor()
        name1 = a
        passwd1 = b
        q = 'select name from score'
        cursor = mycon.cursor()
        cursor.execute(q)
        data = cursor.fetchall()

        l1 = []
        l1.append(name1)
        l2 = []
        l2.append(passwd1)
        tuple1 = tuple(l1)
        tuple2 = tuple(l2)
        if tuple1 not in data:
            t = 'insert into score values("{}",0,0,"{}","NOT PLAYED",0,0,"NOT PLAYED")'.format(
                name1, passwd1)
            cursor.execute(t)
            mycon.commit()
            roo.destroy()
        else:
            label20 = tk.Label(fram7, text=ift(), bg='#FFE4C4',
                               font=('Comic Sans MS', 14))
            label20.pack(expand='true')
    height = 768
    width = 1366
    roo = tk.Toplevel()
    roo.title('register')
    canva = tk.Canvas(roo, height=height, width=width)
    canva.pack()
    b = tk.PhotoImage(file='Nebula.png')
    labe = tk.Label(roo, image=b)
    labe.place(x=0, y=0, relwidth=1, relheight=1)

    def tick():
        global date
        date = date.today()
        tick2 = time.strftime("%H:%M:%S")
        clock.config(text='''{}
    {}'''.format(date, tick2))
        clock.after(200, tick)
    frame123 = tk.Frame(roo, bg='#80c1ff', bd=10)
    frame123.place(relx=0.075, rely=0.001, relwidth=0.09,
                   relheight=0.1, anchor='n')
    clock = tk.Label(frame123, font=('Comic Sans MS', 8, 'bold'))
    clock.place(relheight=1, relwidth=1)
    tick()
    fram = tk.Frame(roo, bg='#FF4500', bd=15)
    fram.place(relx=0.14, rely=0.3, relwidth=0.75, relheight=0.08)

    fram4 = tk.Frame(roo, bg='#FF4500', bd=15)
    fram4.place(relx=0.14, rely=0.45, relwidth=0.75, relheight=0.08)

    fram5 = tk.Frame(roo, bg='#FF4500', bd=15)
    fram5.place(relx=0.14, rely=0.6, relwidth=0.75, relheight=0.08)

    labe5 = tk.Label(fram, text='Name', bg='#FFE4C4',
                     font=('Comic Sans MS', 14, 'bold'))
    labe5.place(relheight=1, relwidth=0.25)

    labe6 = tk.Label(fram4, text='Password', bg='#FFE4C4',
                     font=('Comic Sans MS', 14, 'bold'))
    labe6.place(relheight=1, relwidth=0.25)

    entr7 = tk.Entry(fram, font=('Comic Sans MS', 14, 'bold'))
    entr7.place(relheight=1, relwidth=0.75, relx=0.25)

    entr8 = tk.Entry(fram4, show='*', font=('Comic Sans MS', 14, 'bold'))
    entr8.place(relheight=1, relwidth=0.75, relx=0.25)

    butto2 = tk.Button(fram5, text='create account', bg='#FFE4C4', font=(
        'Comic Sans MS', 15, 'bold'), command=lambda: register1(entr7.get(), entr8.get()))
    butto2.place(relheight=1, relwidth=0.3, relx=0.35)

    fram7 = tk.Frame(roo, bg='white', bd=15)
    fram7.place(relx=0.14, rely=0.75, relwidth=0.75, relheight=0.08)
    roo.mainloop()


height = 768
width = 1366
root = tk.Tk()
root.title('login or register')
canvas = tk.Canvas(root, height=height, width=width)
winsound.PlaySound('perfecttime.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
canvas.pack()
bg = tk.PhotoImage(file='Nebula.png')
bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


def tick():
    global date
    date = date.today()
    tick2 = time.strftime("%H:%M:%S")
    clock.config(text='''{}
{}'''.format(date, tick2))
    clock.after(200, tick)


frame123 = tk.Frame(root, bg='#80c1ff', bd=10)
frame123.place(relx=0.075, rely=0.02, relwidth=0.09, relheight=0.1, anchor='n')
clock = tk.Label(frame123, font=('Comic Sans MS', 9, 'bold'))
clock.place(relheight=1, relwidth=1)
tick()
frame = tk.Frame(root, bg='#80c1ff', bd=10)
frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.75, anchor='n')
frame1 = tk.Frame(root, bg='#FF4500', bd=15)
frame1.place(relx=0.5, rely=0.02, relwidth=0.75, relheight=0.08, anchor='n')
g1 = tk.PhotoImage(file='BeFunky-photo(1).png')
g2 = tk.PhotoImage(file='BeFunky-photo(2).png')
label = tk.Label(frame1, text='Welcome Gamers Wanna Play? Then just login Or Register And Play as much you want',
                 bg='#FFE4C4', font=('Comic Sans MS', 10, 'bold'))
label.place(relheight=1, relwidth=1)

text = '''login
Already Have
an Account
'''
button = tk.Button(frame, text=text, image=g1, bg='#FFE4C4',
                   font=('Comic Sans MS', 17, 'bold'), command=login)
button.place(relheight=1, relwidth=0.5)
text1 = '''Register
Don't Have an
Account
Then Create
 '''
button1 = tk.Button(frame, text=text1, image=g2, justify='center',
                    bg='#FFE4C4', font=('Comic Sans MS', 17, 'bold'), command=register)
button1.place(relheight=1, relwidth=0.5, relx=0.5)
