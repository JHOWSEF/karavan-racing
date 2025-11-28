import graphics as gf
import random
import time

#Tela
win = gf.GraphWin("Jogo de Carro", 900, 900, autoflush=False)
win.setBackground("green")

def karavanHasCrashed(traffic,karavanHitBox):
        for trafficHitbox,trafficSprite in traffic:
            if (karavanHitBox.getP1().getX() <= trafficHitbox.getP2().getX() and karavanHitBox.getP2().getX() >= trafficHitbox.getP1().getX()) and (karavanHitBox.getP1().getY() <= trafficHitbox.getP2().getY() and karavanHitBox.getP2().getY() >= trafficHitbox.getP1().getY()):
                return True 
            
def genTraffic(traffic):
        trafficCarsImg = ['f1_enemy.png','whiteCar_enemy.png','yellowCar_enemy.png','playerCar60x60.png','redCar_enemy.png','blueCar_enemy.png','bugattiCar_enemy.png','greenCar_enemy.png']
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
    road = gf.Rectangle(gf.Point(200, 0), gf.Point(700, 900))
    road.setFill(road_color)
    road.draw(win)

def genlines(win):
    #traçado da estrada
    lines = []
    y1 = 0
    y2 = 40
    x1 = 300
    x2 = 300
    for _ in range(4):
        for _ in range(20):
            line = gf.Line(gf.Point(x1,y1),gf.Point(x2,y2))
            line.setWidth(2)
            line.setFill("white")
            lines.append(line)
            line.draw(win)
            y1 += 60
            y2 += 60
        y1 = 0
        y2 = 40
        x1+=100
        x2+=100
    return lines

def movelines(lines):
    speed = 6
    for line in lines:
        line.move(0, speed)
        if line.getP1().getY() > 600:  
            dy = -600  # sobe tudo de volta
            line.move(0, dy)

def create_rpm_bar(win):
    rpmBarBackground = gf.Rectangle(gf.Point(240, 710), gf.Point(615, 720))
    rpmBarBackground.setFill("darkgrey")
    rpmBarBackground.draw(win)

    rpmBar = gf.Rectangle(gf.Point(240, 710), gf.Point(240, 720))
    rpmBar.setFill("yellow")
    rpmBar.draw(win)

    return rpmBar


def update_rpm_bar(win, rpmBar, rpm_value):
    start = 240
    end_max = 615

    x = start + (end_max - start) * rpm_value  # cálculo da posição final

    # apaga barra antiga
    rpmBar.undraw()

    # cria barra nova
    newRpmBar = gf.Rectangle(gf.Point(start, 710), gf.Point(x, 720))
    newRpmBar.setFill("yellow")
    newRpmBar.draw(win)

    return newRpmBar

def shakeKaravan(karavanHitBox,karavanSprite,shakeinterval,shakeright,shaketimer):

    if shaketimer >= shakeinterval:
        shaketimer = 0

        if shakeright == True:
            karavanHitBox.move(7, 0)
            karavanSprite.move(7, 0)
            shakeright = False
        else:
            karavanHitBox.move(-7, 0)
            karavanSprite.move(-7, 0)
            shakeright = True
        
    return shakeright, shaketimer

           
def main():
    #gameOver
    gameOver = False

    genlines(win)
    lines = genlines(win)

    #karavanHitBox.setFill("blue") #Cor da hitbox
    #karavan config

    
    karavanSpriteList = ['karavan-left.png','karavan-right.png','karavan-pop.png']  
    karavanSprite = gf.Image(gf.Point(450, 510), 'playerCar60x60.png')
    karavanHitBox = gf.Rectangle(gf.Point(440, 530), gf.Point(460, 570))
    karavanAcceleration = 20 #Mais dificil -> maior velocidade da karavan
    karavanDisacceleration = 4
    karavanHitBox.draw(win)


    #carros inimigos
    traffic = []
    car_speed = 1
    spawn_timer = 0  
    spawn_interval = 100 #Mais dificil => menor spawn_interval 

    #score create
    score = 0
    score_text = gf.Text(gf.Point(367, 840), f"Points: {score}")
    score_text.setSize(18)
    ft = gf.Image(gf.Point(460,790), "ft700.png")
    ft.draw(win)
    score_text.draw(win)
    
    rpm_value = 0.0
    rpm_speed_up = 0.04
    rpm_speed_down = 0.01

    rpmBar = create_rpm_bar(win)

    currentKaravanSprite = 0

    shakeright = True
    shaketimer = 0
    shakeinterval = 20
    while not gameOver:
        #time.sleep(0.001)
        key = win.checkKey()

        karavanX1 = karavanHitBox.getP1().getX()
        karavanY1 = karavanHitBox.getP1().getY()

        karavanSprite.undraw()

        karavanSprite = gf.Image(gf.Point(karavanX1 + 10, karavanY1 + 20), karavanSpriteList[currentKaravanSprite])
        karavanSprite.draw(win)
        currentKaravanSprite += 1
        if currentKaravanSprite > 2:
            currentKaravanSprite = 0
        
        if key.upper() == "A" and karavanHitBox.getP1().getX() > 205:
            karavanHitBox.move(-karavanAcceleration, 0)
            karavanSprite.move(-karavanAcceleration, 0)

        elif key.upper() == "D" and karavanHitBox.getP2().getX() < 695:
            karavanHitBox.move(karavanAcceleration, 0)
            karavanSprite.move(karavanAcceleration, 0)

        elif key.upper() == "W" and karavanHitBox.getP1().getY() > 0:
            karavanHitBox.move(0, -karavanAcceleration)
            karavanSprite.move(0, -karavanAcceleration)
            rpm_value += rpm_speed_up
            if rpm_value > 1:
                rpm_value = 1
            rpmBar = update_rpm_bar(win, rpmBar, rpm_value)

        elif key.upper() == "S" and karavanHitBox.getP2().getY() < 630:
            karavanHitBox.move(0, karavanDisacceleration)
            karavanSprite.move(0, karavanDisacceleration)
            rpm_value -= rpm_speed_down
            if rpm_value<0:
                rpm_value=0
            rpmBar = update_rpm_bar(win, rpmBar, rpm_value)

        elif key == "Escape":
            gameOver = True
            win.close()

        #shake karavan
        shaketimer += 1
        shakeright,shaketimer = shakeKaravan(karavanHitBox,karavanSprite,shakeinterval,shakeright,shaketimer)

        spawn_timer += 1
        if spawn_timer >= spawn_interval:
            spawn_timer = 0
            genTraffic(traffic)

        #Move o tráfego
        moveTraffic(traffic,car_speed) 

        #move as linhas  
        movelines(lines)

        if resetTraffic(traffic,car_speed):
            score +=1
            updateScore(score,score_text)

        #Colisão com os carros da rodovia
        if karavanHasCrashed(traffic,karavanHitBox):
            print('Karavan Crashed')
            win.getMouse()
            gameOver = True


genRoad(win)
main()
