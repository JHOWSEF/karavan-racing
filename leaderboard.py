import graphics as gf

def showLeaderboard(win):
    y = 90 #Posição X onde vão começar a aparecer as pontuações
    num = 1
    previousScores = []
    with open('leaderboard.csv','r') as file:
        f = file.read() #Le o arquivo de pontuação
        scoreSplited = f.split(';') #Pontuações estão divididas por ; no arquivo
        for i in range(len(scoreSplited)):
            scoreSplited[i] = int(scoreSplited[i]) #Converte a pontuação de string para inteiro
        scoreSplited.sort(reverse=True) #Deixa a lista em ordem decrescente

        topScoreTxt = gf.Text(gf.Point(800,50), "Top Scores :")
        topScoreTxt.setTextColor("black")
        topScoreTxt.setSize(20)
        topScoreTxt.draw(win)

        if len(scoreSplited) >= 5: #Verifica se já existem no mínimo 5 scores
            c = 5
        else:
            c = len(scoreSplited)

        for i in range(c): #Pega o os tops do leaderboard
            text = gf.Text(gf.Point(800,y),f"{num}º {scoreSplited[i]}")
            text.setTextColor("black")
            text.setSize(15)
            text.draw(win)
            previousScores.append(text)
            y+= 37.5 #não é febre / Espaçamento entre cada pontuação
            num+=1
        
        return topScoreTxt, previousScores
    