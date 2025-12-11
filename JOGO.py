import graphics as gf
import random

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

def moveTraffic(traffic,trafficSpeed):
    #loop para mover os inimigos
    for trafficHitbox,trafficSprite in traffic:
        trafficHitbox.move(0, trafficSpeed)
        trafficSprite.move(0,trafficSpeed)

def updateScore(score,scoreText):
    
    scoreText.setText(score)

def genRoad(win,score):       
    #estrada
    dirtRoadColor = gf.color_rgb(82,57,47)
    dirtRoad = gf.Rectangle(gf.Point(200, 0), gf.Point(700, 800))
    dirtRoad.setFill(dirtRoadColor)
    dirtRoad.draw(win)    
    roadColor = gf.color_rgb(53,53,53)
    road = gf.Rectangle(gf.Point(200, 0), gf.Point(700, 800))
    road.setFill(roadColor)
    road.draw(win)
    return road,dirtRoad

def changeRoad(road,win):
    changeToDirtRoad = False
    #Muda para a estrada de terra
    if road.getP1().getY() < 900:
        while road.getP1().getY() < 900:
            road.move(0,2)
            win.update()
            changeToDirtRoad = True
        return changeToDirtRoad
    #Muda para a estrada de asfalto
    else:
        while road.getP1().getY() > 0:
            road.move(0,-2)
            win.update()
            changeToDirtRoad = False
        return changeToDirtRoad

def genLines(win):
    #traçado da estrada
    lines = []
    y1 = 0
    y2 = 40
    x1 = 300
    x2 = 300
    for i in range(4):
        for i in range(20):
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

def moveLines(lines):
    speed = 6
    for line in lines:
        line.move(0, speed)
        if line.getP1().getY() > 600:  
            dy = -600  # sobe tudo de volta
            line.move(0, dy)

def createRpmBar(win):
    rpmBarBackground = gf.Rectangle(gf.Point(235, 685), gf.Point(615, 715))
    rpmBarBackground.setFill("darkgrey")
    rpmBarBackground.draw(win)

    rpmBar = gf.Rectangle(gf.Point(240, 710), gf.Point(240, 720))
    rpmBar.setFill("yellow")
    rpmBar.draw(win)

    return rpmBar

def updateRpmBar(win, rpmBar, rpmValue):
    start = 240 #Onde a barra de rpm começa
    maxRpm = 615 #Ponto limite da barra de rpm

    x = start + (maxRpm - start) * rpmValue  # Cálculo da posição final da barra de rpm 

    # Apaga barra antiga
    rpmBar.undraw()

    # Cria a barra nova
    newRpmBar = gf.Rectangle(gf.Point(start, 685), gf.Point(x, 715))
    newRpmBar.setFill("yellow")
    newRpmBar.draw(win)

    return newRpmBar

def shakeKaravan(karavanHitBox,karavanSprite,shakeInterval,shakeRight,shakeTimer):

    if shakeTimer >= shakeInterval:
        shakeTimer = 0

        if shakeRight == True:
            karavanHitBox.move(7, 0)
            karavanSprite.move(7, 0)
            shakeRight = False
        else:
            karavanHitBox.move(-7, 0)
            karavanSprite.move(-7, 0)
            shakeRight = True
        
    return shakeRight, shakeTimer
    
def drawGrass(win):
    count=100
    grassList = []
    for i in range(count):
        x = random.randint(0, 900)
        y = random.randint(0, 700)
        size = random.randint(4, 10)

        for i in range(10):
            line = gf.Line(
                gf.Point(x, y),
                gf.Point(x + random.randint(-size, size), y - random.randint(3, size))
            )
            line.setWidth(1)
            greens = ["#228b22", "#006400", "#32cd32", "#00aa44"] 
            line.setFill(random.choice(greens))
            grassList.append(line)
            line.draw(win)
    return grassList 

def addNewScore(newScore):
    previousScores = []
    output = ''
    with open('leaderboard.csv', 'r') as file:
        previousScores = [score for score in file.read().strip().split(';') if score]
        # print(previousScores)
        previousScores.append(str(newScore))
        previousScores.sort(reverse=True, key=str)
        output = ';'.join(previousScores)
    with open('leaderboard.csv', 'w+') as file:
        file.write(output)

def showLeaderboard(win):
    y = 90
    num = 1
    with open('leaderboard.csv','r') as file:
        f = file.read()
        scoreSplited = f.split(';')
        for i in range(len(scoreSplited)):
            scoreSplited[i] = int(scoreSplited[i])
        scoreSplited.sort(reverse=True)

        title = gf.Text(gf.Point(800,50), "Top Scores :")
        title.setTextColor("black")
        title.setSize(20)
        title.draw(win)

        for i in range(5):
            text = gf.Text(gf.Point(800,y),f"{num}º {scoreSplited[i]}")
            text.setTextColor("black")
            text.setSize(15)
            text.draw(win)
            y+= 37.5 #não é febre
            num+=1


           
def main():
    #gameOver
    gameOver = False
    
    # grass = drawGrass(win)
    showLeaderboard(win)
    road,dirtRoad = genRoad(win,0)
    print(road)
    genLines(win)
    lines = genLines(win)
    
    #Cria a antiga FT e o Score que vai aparecer na tela
    score = 0
    scoreText = gf.Text(gf.Point(262, 835), f"{score}")
    scoreText.setTextColor('white')
    scoreText.setSize(18)
    ft = gf.Image(gf.Point(455,775), "ft700.png")
    ft.draw(win)

    scoreText.draw(win)

    #Configurações default da Karavan
    karavanSpriteList = ['karavan-left.png','karavan-right.png','karavan-pop.png']  
    karavanSprite = gf.Image(gf.Point(450, 510), 'playerCar60x60.png')
    karavanHitBox = gf.Rectangle(gf.Point(440, 530), gf.Point(460, 570))
    karavanAcceleration = 20 #Mais dificil -> maior velocidade da karavan
    karavanDisacceleration = 4
    karavanHitBox.draw(win)
    currentKaravanSprite = 0

    #Configurações default do tráfego
    traffic = []
    trafficSpeed = 2
    spawn_timer = 0  
    spawn_interval = 100 #Mais dificil => menor spawn_interval 


    rpmValue = 0.0
    rpm_speed_up = 0.04
    rpm_speed_down = 0.01

    rpmBar = createRpmBar(win)

    shakeTimer = 0
    shakeInterval = 20 #Intervalo entre as trepidações da karavan
    shakeRight = True

    isDirtRoad = False

    
    while not gameOver:

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
            rpmValue += rpm_speed_up
            if rpmValue > 1:
                rpmValue = 1
            rpmBar = updateRpmBar(win, rpmBar, rpmValue)

        elif key.upper() == "S" and karavanHitBox.getP2().getY() < 630:
            karavanHitBox.move(0, karavanDisacceleration)
            karavanSprite.move(0, karavanDisacceleration)
            rpmValue -= rpm_speed_down
            if rpmValue<0:
                rpmValue=0
            rpmBar = updateRpmBar(win, rpmBar, rpmValue)

        elif key == "Escape":
            gameOver = True
            win.close()

        #Trepidação da Karavan
        shakeTimer += 1
        if isDirtRoad == True:
            shakeRight, shakeTimer = shakeKaravan(karavanHitBox, karavanSprite,shakeInterval, shakeRight, shakeTimer)
        else:
            shakeTimer = 0        

        spawn_timer += 1
        if spawn_timer >= spawn_interval:
            spawn_timer = 0
            genTraffic(traffic)

        #Função para mover o tráfego
        moveTraffic(traffic,trafficSpeed) 

        #Função para mover as linhas da rodovia  
        moveLines(lines)
         
        #Reseta o tráfego quando atingir o limite vertical da tela
        if resetTraffic(traffic,trafficSpeed):
            score +=1 
            if score % 10 == 0:
                isDirtRoad = changeRoad(road, win)
                

                #changeRoad(road,win)
            updateScore(score,scoreText)
     

        #Verifica a colisão da Karavan com os carros da rodovia
        if karavanHasCrashed(traffic,karavanHitBox):
            print('Karavan Crashed')
            win.getMouse()
            gameOver = True
            newScore = addNewScore(score)



main()
