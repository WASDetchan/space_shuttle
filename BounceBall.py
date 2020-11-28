import pygame, random

pygame.init()
screen = pygame.display.set_mode([1000, 500])
pygame.display.set_caption('Random ball', 'beach_ball.ico')
screen.fill([255, 255, 255])
ball = pygame.image.load("beach_ball.png")
x = 50
y = 50
# screen.blit(ball, [x, y])
pygame.display.flip()
touch = 'start'
xgo = 0
ygo = 0


def move():
    go = True
    global x, y, touch, xgo, ygo
    listOfGoes = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    #print(ygo, xgo, touch)
    if touch == 'start':
        xgo = random.choice(listOfGoes)
        ygo = random.choice(listOfGoes)
    if touch == 'x':
        xgo = -xgo
    if touch == 'y':
        ygo = -ygo
    while go:

        pygame.draw.rect(screen, [255, 255, 255], [x, y, 140, 140], 0)
        x += xgo
        y += ygo
        screen.blit(ball, [x, y])
        pygame.time.delay(5)
        pygame.display.flip()

        if x > 860 or x < 1:
            touch = 'x'
            go = False
        if y > 360 or y < 1:
            touch = 'y'
            go = False


run = True
while run:
    pygame.time.delay(10)
    move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
