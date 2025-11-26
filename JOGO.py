import graphics as gf
import random
import time

#Tela
win = gf.GraphWin("Jogo de Carro", 900, 900)
win.setBackground("green")

def karavanHasCrashed(traffic,karavanHitbox):
        for trafficHitbox,trafficSprite in traffic:
            if (karavanHitbox.getP1().getX() <= trafficHitbox.getP2().getX() and karavanHitbox.getP2().getX() >= trafficHitbox.getP1().getX()) and (karavanHitbox.getP1().getY() <= trafficHitbox.getP2().getY() and karavanHitbox.getP2().getY() >= trafficHitbox.getP1().getY()):
                return True 
            
def genTraffic(traffic):
        trafficCarsImg = ['f1_enemy.png','whiteCar_enemy.png','yellowCar_enemy.png','playerCar60x60.png','redCar_enemy.png']
        largSprite = 30
        altSprite = 30
        x1 = random.randint(220, 660 - largSprite )
        y1 = (0 - altSprite)
        x2 = x1 + largSprite
        y2 = y1 + altSprite
        trafficHitbox = gf.Rectangle(gf.Point(x1, y1), gf.Point(x2, y2))
        #trafficHitbox.setFill("red") cor da hitbox do traffic
        #trafficHitbox.draw(win)
        trafficSprite = gf.Image(gf.Point((x1 + x2) / 2, (y1 + y2) /2), random.choice(trafficCarsImg))
        trafficSprite.draw(win)
       
        traffic.append((trafficHitbox,trafficSprite))

def resetTraffic(traffic,score):
    for trafficHitbox,trafficSprite in traffic:
        if trafficHitbox.getP1().getY() > 600: #Se atingir o limite vertical da tela
            trafficHitbox.undraw()
            trafficSprite.undraw()
            traffic.remove((trafficHitbox,trafficSprite))
            return True

def moveTraffic(traffic,car_speed):
    #loop para mover os inimigos
    for trafficHitbox,trafficSprite in traffic:
        trafficHitbox.move(0, car_speed)
        trafficSprite.move(0,car_speed)

def updateScore(score,score_text):
    score += 1
    score_text.setText(score)

def genRoad(win):
    #estrada
    road_color = gf.color_rgb(54,54,54)
    road = gf.Rectangle(gf.Point(200, 0), gf.Point(700, 645))
    road.setFill(road_color)
    road.draw(win)                   
    lines = []
    #traçado da estrada
    y1 = 0
    y2 = 90
    x1 = 300
    x2 = 300
    for _ in range(4):
        for _ in range(6):
            line = gf.Line(gf.Point(x1,y1),gf.Point(x2,y2))
            line.setWidth(5)
            line.setFill("yellow")
            lines.append(line)
            line.draw(win)
            y1 += 110
            y2 += 110
        y1 = 0
        y2 = 90
        x1+=100
        x2+=100


def main():
    #GameOver
    GameOver = False

    #Player Sprites
    karavanSprite = gf.Image(gf.Point(450,550),'karavan.png')

    #Player Hitboxes
    karavanHitbox = gf.Rectangle(gf.Point(440, 530), gf.Point(460, 570))
    #karavanHitbox.setFill("blue") #Cor da hitbox
    karavan_speed = 20 #Mais dificil -> maior velocidade da karavan

    karavanHitbox.draw(win)
    karavanSprite.draw(win)

    #carros inimigos
    traffic = []
    car_speed = 5
    spawn_timer = 0  
    spawn_interval = 15 #Mais dificil => menor spawn_interval  

    

    #score create
    score = 0
    score_text = gf.Text(gf.Point(367, 840), f"Points: {score}")
    score_text.setSize(18)
    ft = gf.Image(gf.Point(460,790), "ft.png")
    ft.draw(win)
    score_text.draw(win)


    while not GameOver:
        time.sleep(1/120)

        

        key = win.checkKey()
        
        if key.upper() == "A" and karavanHitbox.getP1().getX() > 205:
            karavanHitbox.move(-karavan_speed, 0)
            karavanSprite.move(-karavan_speed, 0)
        elif key.upper() == "D" and karavanHitbox.getP2().getX() < 695:
            karavanHitbox.move(karavan_speed, 0)
            karavanSprite.move(karavan_speed, 0)
        elif key.upper() == "W" and karavanHitbox.getP1().getY() > 0:
            karavanHitbox.move(0, -karavan_speed)
            karavanSprite.move(0, -karavan_speed)
        elif key.upper() == "S" and karavanHitbox.getP2().getY() < 630:
            karavanHitbox.move(0, karavan_speed)
            karavanSprite.move(0, karavan_speed)
        elif key == "Escape":
            GameOver = True
            win.close()

        spawn_timer += 1
        if spawn_timer >= spawn_interval:
            spawn_timer = 0
            genTraffic(traffic)

        #Move o tráfego
        moveTraffic(traffic,car_speed)   

        if resetTraffic(traffic,car_speed):
            score +=1
            updateScore(score,score_text)

        #Colisão com os carros da rodovia
        if karavanHasCrashed(traffic,karavanHitbox):
            print('Karavan Crashed')
            win.getMouse()
            GameOver = True

genRoad(win)
main()



    
    