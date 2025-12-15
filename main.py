import graphics as gf
import traffic
import leaderboard
import score
import road
import karavan
import rpmBar
import menu

#Tela
win = gf.GraphWin("Karavan Racing - The Game", 900, 900, autoflush=False)
winColor = gf.color_rgb(255, 178, 102) #Cor do deserto
win.setBackground(winColor)

           
def game(karavanAcceleration, trafficSpawnInterval, trafficSpeed):
    #gameOver
    gameOver = False
    
    topScoreTxt,previousScores = leaderboard.showLeaderboard(win)
    newRoad,dirtRoad = road.genRoad(win,0)
    lines = road.genLines(win)
    
    #Cria a antiga FT e o Score que vai aparecer na tela
    currentScore = 0
    scoreText = gf.Text(gf.Point(262, 835), f"{currentScore}")
    scoreText.setTextColor('white')
    scoreText.setSize(18)
    ft = gf.Image(gf.Point(455,775), "img/ft/ft700.png")
    ft.draw(win)

    scoreText.draw(win)

    #Configurações default da Karavan
    karavanSpriteList = ['img/karavan/karavan-left.png','img/karavan/karavan-right.png','img/karavan/karavan-pop.png']  
    karavanSprite = gf.Image(gf.Point(450, 510), 'img/karavan/karavan.png')
    karavanHitBox = gf.Rectangle(gf.Point(440, 530), gf.Point(460, 570))
    karavanDisacceleration = 4
    karavanHitBox.draw(win)
    currentKaravanSprite = 0

    #Configurações default do tráfego
    trafficList = []
    spawn_timer = 0  
    #trafficSpawnInterval = 100 #Mais dificil => menor trafficSpawnInterval 


    rpmValue = 0.0
    rpmSpeedUp = 0.04
    rpmSpeedDown = 0.01

    newRpmBar = rpmBar.createRpmBar(win)

    shakeTimer = 0

    shakeInterval = 20 #Intervalo entre as trepidações da karavan -> (20 passadas de while)

    shakeRight = True #Verifica se é possivel trepidar para a direita -> Se for FALSE - Então ele trepida para a esquerda

    isDirtRoad = False #Começa com a rodovia

    
    while not gameOver:
        
        karavanX1 = karavanHitBox.getP1().getX() #Posição X da hitbox da Karavan
        karavanY1 = karavanHitBox.getP1().getY() #Posição Y da hitbox da Karavan

        karavanSprite.undraw()

        karavanSprite = gf.Image(gf.Point(karavanX1 + 10, karavanY1 + 20), karavanSpriteList[currentKaravanSprite])
        karavanSprite.draw(win)
        currentKaravanSprite += 1
        if currentKaravanSprite > 2:
            currentKaravanSprite = 0

        key = win.checkKey()

        if key.upper() == "A" and karavanHitBox.getP1().getX() > 205:
            karavanHitBox.move(-karavanAcceleration, 0)
            karavanSprite.move(-karavanAcceleration, 0)

        elif key.upper() == "D" and karavanHitBox.getP2().getX() < 695:
            karavanHitBox.move(karavanAcceleration, 0)
            karavanSprite.move(karavanAcceleration, 0)

        elif key.upper() == "W" and karavanHitBox.getP1().getY() > 0:
            karavanHitBox.move(0, -karavanAcceleration)
            karavanSprite.move(0, -karavanAcceleration)
            rpmValue += rpmSpeedUp
            if rpmValue > 1:
                rpmValue = 1
            newRpmBar = rpmBar.updateRpmBar(win, newRpmBar, rpmValue)

        elif key.upper() == "S" and karavanHitBox.getP2().getY() < 630:
            karavanHitBox.move(0, karavanDisacceleration)
            karavanSprite.move(0, karavanDisacceleration)
            rpmValue -= rpmSpeedDown
            if rpmValue<0:
                rpmValue=0
            newRpmBar = rpmBar.updateRpmBar(win, newRpmBar, rpmValue)

        elif key == "Escape":
            gameOver = True
            win.close()

        #Trepidação da Karavan
        shakeTimer += 1
        if isDirtRoad == True:
            shakeRight, shakeTimer = karavan.shakeKaravan(karavanHitBox, karavanSprite,shakeInterval, shakeRight, shakeTimer)
            for line in lines:
                line.setFill(gf.color_rgb(101, 67, 33))
        else:
            for line in lines:
                line.setFill('white')
            shakeTimer = 0        

        spawn_timer += 1
        if spawn_timer >= trafficSpawnInterval:
            spawn_timer = 0
            traffic.genTraffic(trafficList,win)

        #Função para mover o tráfego
        traffic.moveTraffic(trafficList,trafficSpeed) 

        #Função para mover as linhas da rodovia
        road.moveLines(lines)  
        
         
        #Reseta o tráfego quando atingir o limite vertical da tela
        if traffic.resetTraffic(trafficList,trafficSpeed):
            currentScore +=1 
            if currentScore % 50 == 0: #A cada 40 pontos, troca a estrada
                isDirtRoad = road.changeRoad(newRoad, win) 
                            
            score.updateScore(currentScore,scoreText)
     

        #Verifica a colisão da Karavan com os carros da rodovia
        if karavan.karavanHasCrashed(trafficList,karavanHitBox):
            print('Karavan Crashed')
            addNewScore = score.addNewScore(currentScore)
            menu.undrawAll(ft,scoreText,karavanSprite,karavanHitBox,newRpmBar,newRoad,dirtRoad,lines,trafficList,topScoreTxt,previousScores)
            playAgain = menu.genEndGameButtons(win,currentScore)
            if playAgain:
                karavanAcceleration, trafficSpawnInterval, trafficSpeed = menu.chooseGameDifficult(win)
                game(karavanAcceleration, trafficSpawnInterval, trafficSpeed)
            
            #chooseGameDifficult(win)
            
            gameOver = True

karavanAcceleration, trafficSpawnInterval, trafficSpeed = menu.chooseGameDifficult(win)

game(karavanAcceleration, trafficSpawnInterval, trafficSpeed)
