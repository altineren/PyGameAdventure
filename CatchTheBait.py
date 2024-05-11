import pygame
import random
pygame.init()
width, height = 800,600
screen = pygame.display.set_mode((width,height))

#background music
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1,0,0)
eatSound = pygame.mixer.Sound("eating.wav")
gameOverSound = pygame.mixer.Sound("gameover.wav")



speed = 5
monster=pygame.image.load("monster.png")
monsterCoordinat = monster.get_rect()
monsterCoordinat.topleft=(width/2,height/2)

bait = pygame.image.load("bait.png")
baitCoordinat = bait.get_rect()
baitCoordinat.topleft=(100,100)

backGround = pygame.image.load("underwater.png")

#font settings
FONT=pygame.font.SysFont("consolas",30)

#score
score=0

fps = 60
clock = pygame.time.Clock()


condition = True
while condition:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            condition = False
    button=pygame.key.get_pressed()
    if button[pygame.K_LEFT] and monsterCoordinat.left>0:
        monsterCoordinat.x-=speed
    elif button[pygame.K_RIGHT] and monsterCoordinat.right<width:
        monsterCoordinat.x+=speed
    elif button[pygame.K_UP] and monsterCoordinat.top>40:
        monsterCoordinat.y-=speed
    elif button[pygame.K_DOWN] and monsterCoordinat.bottom<height:
        monsterCoordinat.y+=speed
    screen.fill((0,0,0,0))
    pygame.draw.rect(screen,(120,74,48),monsterCoordinat,1)
    pygame.draw.rect(screen,(120,74,48),baitCoordinat,1)
    if monsterCoordinat.colliderect(baitCoordinat):
        eatSound.play()
        baitCoordinat.x=random.randint(0,width-32)
        baitCoordinat.y=random.randint(0,height-32)
        score+=1
        if score>5:
            monster=pygame.image.load("biggerMonster.png")


    screen.blit(backGround,(0,0))
    screen.blit(monster,monsterCoordinat)
    screen.blit(bait,baitCoordinat)
    skorFont = FONT.render("Score: " +str(score),True,(200,10,67))
    skorFontCoordinat=skorFont.get_rect()
    skorFontCoordinat.topleft=(20,10)

    gameName = FONT.render("CATCH THE BAIT",True,(200,10,67))
    gameNameCoordinat=gameName.get_rect()
    gameNameCoordinat.midtop=(width/2,10)
    screen.blit(gameName,gameNameCoordinat)
    screen.blit(skorFont,skorFontCoordinat)
    pygame.draw.line(screen,(140,0,70),(0,40),(width,40))

    pygame.display.update()
    clock.tick(fps)
pygame.quit()

