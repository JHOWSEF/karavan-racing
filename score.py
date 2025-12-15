def updateScore(score,scoreText):
    scoreText.setText(score)
    return score



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


