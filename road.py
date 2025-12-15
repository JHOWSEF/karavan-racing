import graphics as gf

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