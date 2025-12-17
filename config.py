import graphics as gf

#Configurações default da Karavan
KARAVANSPRITELIST = ['img/karavan/karavan-left.png','img/karavan/karavan-right.png','img/karavan/karavan-pop.png']  
KARAVANSPRITE = gf.Image(gf.Point(450, 510), 'img/karavan/karavan.png')
KARAVANHITBOX = gf.Rectangle(gf.Point(440, 530), gf.Point(460, 570))
#karavanAcceleration = 20 #Mais dificil -> maior velocidade da karavan
KARAVANDESACCELERATION = 4
SHAKEKARAVANTIMER = 0
SHAKEKARAVANINTERVAL = 20