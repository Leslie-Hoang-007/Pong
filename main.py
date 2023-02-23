import pygame, sys, random

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screenWidth, screenHeight = 1000, 800
ballSize = 30

screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Pong')

# Game assets
ball = pygame.Rect(screenWidth/2-ballSize/2,screenHeight/2-ballSize/2,ballSize,ballSize)
player = pygame.Rect(0,screenHeight/2 -50, 10,100)
opponent = pygame.Rect(screenWidth-10, screenHeight/2 -50, 10, 100)

backgroundColor = pygame.Color('black')
assetsColor = pygame.Color('white')




ballSpeedX = 5
ballSpeedY = 5

# animations

def ballAnimations():
    global ballSpeedX, ballSpeedY
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    if ball.top <=0 or ball.bottom >= screenHeight:
        ballSpeedY = -ballSpeedY
    if ball.left <=0 or ball.right >= screenWidth:
        ballRestart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ballSpeedX = -ballSpeedX
def playerAnimation():
    if player.top <=0:
        player.top =0
    if player.bottom >=screenHeight:
        player.bottom= screenHeight

def opponentAnimation():
    if opponent.top < ball.y:
        opponent.top += 5
    if opponent.bottom> ball.y:
        opponent.bottom -=5
    if opponent.top <=0:
        opponent.top =0
    if opponent.bottom >=screenHeight:
        opponent.bottom= screenHeight

def ballRestart():
    global ballSpeedY,ballSpeedX
    ball.center =(screenWidth/2, screenHeight/2)
    ballSpeedX *= random.choice((1,-1))
    ballSpeedY *= random.choice((1,-1))

playerSpeed = 0

while True:
    #handeling game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed +=7
            if event.key == pygame.K_UP:
                playerSpeed -=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed -=7
            if event.key == pygame.K_UP:
                playerSpeed +=7

    # animations

    ballAnimations()
    player.y += playerSpeed

    playerAnimation()
    opponentAnimation()
    #Drawing
    screen.fill(backgroundColor)
    pygame.draw.rect(screen,assetsColor,player)
    pygame.draw.rect(screen,assetsColor,opponent)
    pygame.draw.ellipse(screen,assetsColor,ball)




    pygame.draw.aaline(screen, assetsColor,(screenWidth/2,0), (screenWidth/2,screenHeight))
    # updating the Window
    pygame.display.flip()
    clock.tick(60)