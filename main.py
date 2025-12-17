import graphics as gf
import traffic
import leaderboard
import score
import road
import karavan
import rpmBar
import menu
import config

#Tela
win = gf.GraphWin("Karavan Racing - The Game", 900, 900, autoflush=False)
winColor = gf.color_rgb(255, 178, 102) #Cor do deserto
win.setBackground(winColor)

           
def game(karavanAcceleration, trafficSpawnInterval, trafficSpeed, difficulty):
    #gameOver
    gameOver = False
    
    topScoreTxt,previousScores = leaderboard.showLeaderboard(win,difficulty)
    newRoad,dirtRoad = road.genRoad(win,0)
    lines = road.genLines(win) #Gera as linhas da rodovia
    
    #Cria a antiga FT e o Score que vai aparecer na tela
    currentScore = 0 #Inicia o score
    scoreText = gf.Text(gf.Point(262, 835), f"{currentScore}")
    scoreText.setTextColor('white')
    scoreText.setSize(18)
    

    ft = gf.Image(gf.Point(455,775), "img/ft/ft700.png") #Gera a FT
    ft.draw(win)
    
    scoreText.draw(win)

    #Configurações default da Karavan
    karavanSpriteList = config.KARAVANSPRITELIST  
    karavanSprite = config.KARAVANSPRITE
    karavanHitBox = config.KARAVANHITBOX
    karavanDisacceleration = config.KARAVANDESACCELERATION #O quanto a karavan vai desacelerar quando 'S' for pressionado
    karavanHitBox.draw(win) 
    currentKaravanSprite = 0

    #Configurações default do tráfego
    trafficList = []
    trafficSpawnTimer = 0  
    #trafficSpawnInterval = 100 #Mais dificil => menor trafficSpawnInterval 

    rpmValue = 0.0 # Rpm começa em 0
    rpmSpeedUp = 0.04 # Decimal de quanto o que o rpm vai subir ao clicar em W
    rpmSpeedDown = 0.01 # Decima de quanto o rpm vai descer ao clicar em S

    newRpmBar = rpmBar.createRpmBar(win)

    shakeKaravanTimer = config.SHAKEKARAVANTIMER #Variável que vai ser incrementada durante a execução do while

    shakeKaravanInterval = config.SHAKEKARAVANINTERVAL #Intervalo entre as trepidações da karavan -> (20 passadas de while)

    canKaravanShakeRight = True #Verifica se é possivel trepidar para a direita -> Se for FALSE - Então ele trepida para a esquerda

    isDirtRoad = False #Começa com a rodovia

    
    while not gameOver:
        
        karavanX1 = karavanHitBox.getP1().getX() #Posição X da hitbox da Karavan
        karavanY1 = karavanHitBox.getP1().getY() #Posição Y da hitbox da Karavan

        karavanSprite.undraw()

        karavanSprite = gf.Image(gf.Point(karavanX1 + 10, karavanY1 + 20), karavanSpriteList[currentKaravanSprite])
        karavanSprite.draw(win)

        currentKaravanSprite += 1 #Sprite atual da Karavan
        if currentKaravanSprite > 2: #Se chegar ao limite da lista de sprites, volta a 0 -> Tornando essa lista cíclica
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
        shakeKaravanTimer += 1
        if isDirtRoad == True: #Se a estrada for de terra, a karavan começa a trepidar
            canKaravanShakeRight, shakeKaravanTimer = karavan.shakeKaravan(karavanHitBox, karavanSprite,shakeKaravanInterval, canKaravanShakeRight, shakeKaravanTimer)
            for line in lines:
                line.setFill(gf.color_rgb(101, 67, 33)) #Muda a cor das linhas da pista para marrom
        else:
            for line in lines:
                line.setFill('white') #Mantém a cor original das linhas da rodovia
            shakeKaravanTimer = 0        

        trafficSpawnTimer += 1 
        if trafficSpawnTimer >= trafficSpawnInterval: #Mais dificil => menor trafficSpawnInterval = mais carros 
            trafficSpawnTimer = 0
            traffic.genTraffic(trafficList,win) #Gera a posição de spawn do carro 

        #Função para mover o tráfego
        traffic.moveTraffic(trafficList,trafficSpeed) 

        #Função para mover as linhas da rodovia
        road.moveLines(lines)  
        
         
        #Reseta o tráfego quando atingir o limite vertical da tela
        if traffic.resetTraffic(trafficList,trafficSpeed):
            currentScore +=1 #Incrementa 1 na pontuação a cada carro que chega no limite da tela
            if currentScore % 50 == 0: #A cada 50 pontos, troca a estrada
                isDirtRoad = road.changeRoad(newRoad, win) 
                            
            score.updateScore(currentScore,scoreText)
     

        #Verifica a colisão da Karavan com os carros da rodovia
        if karavan.karavanHasCrashed(trafficList,karavanHitBox):
            print('Karavan Crashed')
            addNewScore = score.addNewScore(currentScore, difficulty) #Grava o score no arquivo de leaderboard
            menu.undrawAll(ft,scoreText,karavanSprite,karavanHitBox,newRpmBar,newRoad,dirtRoad,lines,trafficList,topScoreTxt,previousScores) #Limpa todos os elementos 
            playAgain = menu.genEndGameButtons(win,currentScore) #Gera a opção de jogar novamente ou sair e exibe a pontuação
            if playAgain:
                karavanAcceleration, trafficSpawnInterval, trafficSpeed, difficulty = menu.chooseGameDifficulty(win) #Exibe o menu de escolha de dificuldade
                game(karavanAcceleration, trafficSpawnInterval, trafficSpeed, difficulty) #Inicia o jogo



karavanAcceleration, trafficSpawnInterval, trafficSpeed, difficulty = menu.chooseGameDifficulty(win)

game(karavanAcceleration, trafficSpawnInterval, trafficSpeed, difficulty)
