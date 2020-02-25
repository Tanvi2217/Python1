import pygame
#from pygame.locals import *

pygame.init()

width = 953
height = 500

screen = pygame.display.set_mode((width,height))

black = 0,0,0
white = 255,255,255
blue = 0,0,255


fontpath = "assets/SeasideResortNF/SEASRN__.ttf"
bgImage = pygame.image.load("assets/bkgd.jpg")
def mainpage():
    font = pygame.font.Font(fontpath,100)
    text = font.render("...WELCOME...",True,white)

    font_1 = pygame.font.Font(fontpath,30)
    text_1 = font_1.render("PRESS ENTER TO CONTINUE",True,white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    game()

        screen.blit(bgImage,(0,0))
        screen.blit(text,(100,100))
        screen.blit(text_1,(250,250))
        pygame.display.update()

def showTimer(seconds):
    font_2 = pygame.font.Font(fontpath, 30)
    text_2 = font_2.render("Time Left: "+str(seconds), True, white)
    screen.blit(text_2, (700,300))

def win():
    font_3 = pygame.font.Font(fontpath,100)
    text_3 = font_3.render("...YOU WON...",True,white)
    screen.blit(bgImage,(0,0))
    screen.blit(text_3,(100,100))

def game():
    rectwidth = 150
    rectheight = 20
    rectx = width/2 - rectwidth/2
    recty = height - 20

    xmove = 0
    ymove = 0

    ballx = int(rectx+rectwidth/2)
    bally = (height - rectheight - 10)
    ballmovex = 0
    ballmovey = 0

    boxlist = []

    box = pygame.image.load("assets/rectangle3.png")
    box_width = box.get_width()
    box_height = box.get_height()


    columns = int(width/box_width)
    print(columns)


    for i in range(3):
        for j in range(columns):
            boxlist.append(pygame.Rect(box_width * j ,box_height * i , box_width , box_height ))

    clock = pygame.time.Clock()
    FPS = 100
    seconds = 60
    pygame.time.set_timer(USEREVENT,1000)

    sound  = pygame.mixer.Sound("assets/theme.ogg")
    sound.play()
    hitsound = pygame.mixer.Sound("assets/hit.wav")
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == USEREVENT:
                seconds -= 1
                if seconds == 0:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    xmove = 6
                    ymove = 0
                elif event.key == pygame.K_LEFT:
                    xmove = -6
                    ymove = 0
                elif event.key == pygame.K_SPACE:
                    ballmovex = 5
                    ballmovey = -5
            elif event.type == pygame.KEYUP:
                xmove = 0
                ymove = 0

        screen.fill(black)
        rect = pygame.draw.rect(screen, white, [rectx,recty,rectwidth,rectheight])

        ball = pygame.draw.circle(screen,blue,[ballx,bally],10)
        ballrect = pygame.Rect(ballx,bally,20,20)

        for i in range(len(boxlist)):
            screen.blit(box,(boxlist[i].x,boxlist[i].y))


        rectx += xmove

        if rectx > width - 150:
            xmove = 0
        elif rectx < 0 :
            xmove = 0

        ballx += ballmovex
        bally += ballmovey

        if ballx > width - 10:
            ballmovex = -5
            hitsound.play()
        elif ballx < 0:
            ballmovex = 5
            hitsound.play()
        '''elif bally > height - rectheight - 10:
            ballmovey = -3'''
        if bally < 0:
            ballmovey = 5
            hitsound.play()
        elif bally > height + 10:
            pygame.quit()
            quit()

        if ballrect.colliderect(rect):
            if ballx > width - 10:
                ballmovex = -5
                hitsound.play()
            if ballx < 0:
                ballmovex = 5
                hitsound.play()
            elif bally > height - rectheight - 10:
                ballmovey = -5
                hitsound.play()
            elif bally < 0:
                ballmovey = 5
                hitsound.play()

        for j in range(len(boxlist)):
            if ballrect.colliderect(boxlist[j]):
                boxlist.pop(j)
                ballmovey  = 3
                break

        if len(boxlist) == 0:
             win()

        showTimer(seconds)
        pygame.display.update()
        clock.tick(FPS)
mainpage()
