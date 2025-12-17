import graphics as gf


def createRpmBar(win):

    rpmBar = gf.Rectangle(gf.Point(235, 685), gf.Point(270, 715))
    rpmBar.setFill("yellow")
    rpmBar.draw(win)
    return rpmBar



def updateRpmBar(win, rpmBar, rpmValue):
    start = 235 #Onde a barra de rpm começa
    maxRpm = 615 #Ponto limite da barra de rpm
    x = start + (maxRpm - start) * rpmValue  # Cálculo da posição da barra de rpm 
    # Apaga barra antiga
    rpmBar.undraw()
    # Cria a barra nova
    newRpmBar = gf.Rectangle(gf.Point(start, 685), gf.Point(x, 715))
    newRpmBar.setFill("yellow")
    newRpmBar.draw(win)

    return newRpmBar