import graphics as gf
import random

def genTraffic(trafficList,win):
        trafficCarsImg = ['img/traffic/f1_enemy.png','img/traffic/whiteCar_enemy.png','img/traffic/yellowCar_enemy.png','img/traffic/playerCar60x60.png','img/traffic/redCar_enemy.png','img/traffic/blueCar_enemy.png','img/traffic/bugattiCar_enemy.png','img/traffic/greenCar_enemy.png','img/traffic/greyMercedesTraffic.png']
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
        trafficList.append((trafficHitbox,trafficSprite))

def resetTraffic(trafficList,score):
    for trafficHitbox,trafficSprite in trafficList:
        if trafficHitbox.getP1().getY() > 600: #Se atingir o limite vertical da tela
            trafficHitbox.undraw()
            trafficSprite.undraw()
            trafficList.remove((trafficHitbox,trafficSprite))
            return True

def moveTraffic(trafficList,trafficSpeed):
    #loop para mover os inimigos
    for trafficHitbox,trafficSprite in trafficList:
        trafficHitbox.move(0, trafficSpeed)
        trafficSprite.move(0,trafficSpeed)