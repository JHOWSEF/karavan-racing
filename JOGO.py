import graphics as gf
import random
import time

win = gf.GraphWin("Jogo de Carro", 900, 900)
win.setBackground("green")
img_background = gf.Image(gf.Point(0,600), "fundo_grama.gif")
img_background.draw(win)

#estrada
road = gf.Rectangle(gf.Point(200, 0), gf.Point(700, 645))
road.setFill("black")
road.draw(win)
#traçado da estrada
line = gf.Line(gf.Point(460,0),gf.Point(460,100))
line.setFill("yellow")
line.draw(win)
line2 = gf.Line(gf.Point(460,110),gf.Point(460,210))
line2.setFill("yellow")
line2.draw(win)
line3 = gf.Line(gf.Point(460,220),gf.Point(460,320))
line3.setFill("yellow")
line3.draw(win)
line4 = gf.Line(gf.Point(460,330),gf.Point(460,430))
line4.setFill("yellow")
line4.draw(win)
line5 = gf.Line(gf.Point(460,440),gf.Point(460,540))
line5.setFill("yellow")
line5.draw(win)
line6 = gf.Line(gf.Point(460,550),gf.Point(460,650))
line6.setFill("yellow")
line6.draw(win)
line7 = gf.Line(gf.Point(460,660),gf.Point(460,760))
line7.setFill("yellow")
line7.draw(win)
line8 = gf.Line(gf.Point(460,770),gf.Point(460,870))
line8.setFill("yellow")
line8.draw(win)

player = gf.Rectangle(gf.Point(280, 500), gf.Point(320, 550))
player.setFill("blue")
player.draw(win)

player_speed = 20  

cars = []
car_speed = 5
spawn_timer = 0  
spawn_interval = 25  
score = 0


score_text = gf.Text(gf.Point(367, 840), f"Points: {score}")
score_text.setSize(18)
ft = gf.Image(gf.Point(460,790), "ft.png")
ft.draw(win)
score_text.draw(win)


while True:
    time.sleep(0.03)  
    key = win.checkKey()
    
    if key.upper() == "A" and player.getP1().getX() > 205:
        player.move(-player_speed, 0)
    elif key.upper() == "D" and player.getP2().getX() < 695:
        player.move(player_speed, 0)
    elif key.upper() == "W" and player.getP1().getY() > 0:
        player.move(0, -player_speed)
    elif key.upper() == "S" and player.getP2().getY() < 630:
        player.move(0, player_speed)
    elif key == "Escape":
        win.close()
        print("fechou o game burrao")

    
    spawn_timer += 1
    if spawn_timer >= spawn_interval:
        spawn_timer = 0

        
        x = random.randint(220, 660)
        
        car = gf.Rectangle(gf.Point(x, -40), gf.Point(x+40, 0))
        car.setFill("red")
        car.draw(win)
        cars.append(car)

#loop para mover os inimigos
    for car in cars:
        car.move(0, car_speed)
        
        
        if car.getP1().getY() > 600:
            car.undraw()
            cars.remove(car)
            print("sumiu")
            score += 1
            score_text.setText(score)