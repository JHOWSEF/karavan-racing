import graphics as gf

def showLeaderboard(win, difficulty):
    y = 90 #Posição X onde vão começar a aparecer as pontuações
    num = 1
    topScoreTxt = ''
    previousScores = []
    with open('leaderboard.txt','r+') as file:
        fileContent = file.read() #Le o arquivo de pontuação
        if len(fileContent) > 1: #Verifica se já existem scores registrados
            scoreDict = eval(fileContent) #Faz o dicionário lido ser funcional 
            scoreDict[difficulty].sort(reverse=True) #Deixa o dicionário lido em ordem decrescente

            topScoreTxt = gf.Text(gf.Point(800,50), "Top Scores :")
            topScoreTxt.setTextColor("black")
            topScoreTxt.setSize(20)
            topScoreTxt.draw(win)

            if len(scoreDict[difficulty]) >= 5: #Verifica se já existem no mínimo 5 scores
                c = 5
            else: #Se não existirem 5 pontuações, mostra apenas as que já existem
                c = len(scoreDict[difficulty])

            for i in range(c): #Pega o os tops do leaderboard
                text = gf.Text(gf.Point(800,y),f"{num}º {scoreDict[difficulty][i]}")
                text.setTextColor("black")
                text.setSize(15)
                text.draw(win)
                previousScores.append(text)
                y+= 37.5 #não é febre / Espaçamento entre cada pontuação
                num+=1
        
            return topScoreTxt, previousScores
        return topScoreTxt, previousScores #Sinal que é a primeira vez abrindo o jogo -> não vai aparecer nada nos top scores
        

    