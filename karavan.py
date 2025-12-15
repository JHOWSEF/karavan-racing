import graphics as gf

def karavanHasCrashed(trafficList,karavanHitBox):
        for trafficHitbox,trafficSprite in trafficList:
            if (karavanHitBox.getP1().getX() <= trafficHitbox.getP2().getX() and karavanHitBox.getP2().getX() >= trafficHitbox.getP1().getX()) and (karavanHitBox.getP1().getY() <= trafficHitbox.getP2().getY() and karavanHitBox.getP2().getY() >= trafficHitbox.getP1().getY()):
                return True
            

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