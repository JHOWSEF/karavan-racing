def updateScore(score,scoreText):
    scoreText.setText(score) #Atualiza o score que aparece na tela
    return score



def addNewScore(newScore, difficulty):

    with open('leaderboard.txt', 'r+') as file:
        fileContent = file.read() #Lê o arquivo de leaderboard

        if len(fileContent) < 1: #Se o arquivo de leaderboard estiver vazio (primeira vez executando o jogo)
            defaultScoreDict = {
                'easy': [],
                'medium': [],
                'hard': [],
            }
            defaultScoreDict[difficulty].append(newScore)
            dictToString = str(defaultScoreDict)
            file.write(dictToString)
            #print(f'leaderboard estava vazio')
        else:
            with open('leaderboard.txt', 'w+') as file:
                newDict = eval(fileContent) #Pega o dicionário do leaderboard e faz ele ser funcional
                newDict[difficulty].append(newScore) #Adiciona a pontuação atual na lista de acordo com a dificuldade escolhida no inicio do jogo
                #print(newDict)
                file.write(str(newDict)) #Reescreve o arquivo


