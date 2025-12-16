import graphics as gf

def chooseGameDifficulty(win): #Gera todo o menu de escolha de dificuldade
    backgroundMenuImg = gf.Image(gf.Point(450,450),'img/menu/menuImg.png')
    backgroundMenuImg.draw(win)
    selectDifficultyText = gf.Text(gf.Point(440,270), "Selecionar Dificuldade : ")
    selectDifficultyText.setSize(30)
    selectDifficultyText.setTextColor('white')
    selectDifficultyText.draw(win)
    easyDifficultyText = gf.Text(gf.Point(430,350), "Fácil")
    easyDifficultyText.setTextColor("white")
    easyDifficultyImg = gf.Image(gf.Point(430,350), "img/menu/easybutton.png")
    easyDifficultyImg.draw(win)
    easyDifficultyText.draw(win)

    mediumDifficultyText = gf.Text(gf.Point(430,420), "Normal")
    mediumDifficultyText.setTextColor("white")
    mediumDifficultyImg = gf.Image(gf.Point(430,420), "img/menu/mediumbutton.png")
    mediumDifficultyImg.draw(win)
    mediumDifficultyText.draw(win)

    hardDifficultyText = gf.Text(gf.Point(430,490), "Dificil")
    hardDifficultyText.setTextColor("white")
    hardDifficultyImg = gf.Image(gf.Point(430,490), "img/menu/hardbutton.png")
    hardDifficultyImg.draw(win)
    hardDifficultyText.draw(win)

    

    
    while True:
        
        click = win.getMouse()
        print(click.getX(), click.getY())
        if (click.getX() in range(280,580) and click.getY() in range(325,370)): #Área do botão de dificuldade fácil
            karavanAcceleration = 25 #Mais dificil -> maior velocidade da karavan
            trafficSpawnInterval = 60
            trafficSpeed = 2
            difficulty = 'easy'
            easyDifficultyImg.undraw()
            easyDifficultyText.undraw()
            mediumDifficultyImg.undraw()
            mediumDifficultyText.undraw()
            hardDifficultyImg.undraw()
            hardDifficultyText.undraw()
            selectDifficultyText.undraw()
            backgroundMenuImg.undraw()
            return karavanAcceleration, trafficSpawnInterval, trafficSpeed, difficulty

        elif (click.getX() in range(280,580) and click.getY() in range(395,445)): #Área do botão de dificuldade média
            karavanAcceleration = 20 #Mais dificil -> maior velocidade da karavan
            trafficSpawnInterval = 50
            trafficSpeed = 3
            difficulty = 'medium'
            easyDifficultyImg.undraw()
            easyDifficultyText.undraw()
            mediumDifficultyImg.undraw()
            mediumDifficultyText.undraw()
            hardDifficultyImg.undraw()
            hardDifficultyText.undraw()
            selectDifficultyText.undraw()
            backgroundMenuImg.undraw()
            return karavanAcceleration, trafficSpawnInterval, trafficSpeed, difficulty
        elif (click.getX() in range(280,580) and click.getY() in range(465,515)): #Área do botão de dificuldade dificil
            karavanAcceleration = 15 #Mais dificil -> maior velocidade da karavan
            trafficSpawnInterval = 25
            trafficSpeed = 3.5
            difficulty = 'hard'
            easyDifficultyImg.undraw()
            easyDifficultyText.undraw()
            mediumDifficultyImg.undraw()
            mediumDifficultyText.undraw()
            hardDifficultyImg.undraw()
            hardDifficultyText.undraw()
            selectDifficultyText.undraw()
            backgroundMenuImg.undraw()
            return karavanAcceleration, trafficSpawnInterval, trafficSpeed, difficulty
        

        
    

def genEndGameButtons(win,score): #Gera os botões quando o jogo termina

    backgroundMenuImg = gf.Image(gf.Point(450,450),'img/menu/menuImg.png')
    backgroundMenuImg.draw(win)

    finalScoreText = gf.Text(gf.Point(430,225), f'Sua pontuação foi : {score}')
    finalScoreText.setTextColor("white")
    finalScoreText.setSize(20)
    finalScoreBackground = gf.Rectangle(gf.Point(250, 200), gf.Point(615, 250))
    finalScoreBackground.setFill('darkgrey')
    finalScoreBackground.draw(win)
    finalScoreText.draw(win)

    leaveGameText = gf.Text(gf.Point(325,425), f'Sair') # Entre 400 e 450
    leaveGameText.setTextColor("white")
    leaveGameBackground = gf.Rectangle(gf.Point(250, 400), gf.Point(400, 450))
    leaveGameBackground.setFill('red')
    leaveGameBackground.draw(win)
    leaveGameText.draw(win)

    playAgainText = gf.Text(gf.Point(545,425), f'Jogar Novamente')
    playAgainText.setTextColor("white")
    playAgainBackground = gf.Rectangle(gf.Point(465, 400), gf.Point(615, 450))
    playAgainBackground.setFill('darkgrey')
    playAgainBackground.draw(win)
    playAgainText.draw(win)

    while True:

        click = win.getMouse()

        if (click.getX() in range(465,615) and click.getY() in range(400,450)):
            finalScoreBackground.undraw()
            finalScoreText.undraw()
            leaveGameBackground.undraw()
            leaveGameText.undraw()
            playAgainBackground.undraw()
            playAgainText.undraw()
            backgroundMenuImg.undraw()
            return True
            #chooseGameDifficulty(win)
        elif (click.getX() in range(250,400) and click.getY() in range(400,450)):
            break
    win.close()



def undrawAll(ft,scoreText,karavanSprite,karavanHitBox,rpmBar,road,dirtRoad,lines,trafficList,topScoreTxt,previousScores):
    ft.undraw()
    scoreText.undraw()
    karavanSprite.undraw()
    karavanHitBox.undraw()
    rpmBar.undraw()
    road.undraw()
    dirtRoad.undraw()
    
    for score in previousScores:
        score.undraw()
    for line in lines:
        line.undraw()
    for carShape,carImg in trafficList:
        carShape.undraw()
        carImg.undraw()
    if topScoreTxt != '': #Se não for a primeira vez que está sendo executado - leaderboard.txt não vai estar vazio
        topScoreTxt.undraw()