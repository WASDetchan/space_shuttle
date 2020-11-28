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


def move():
    go = True
    global x, y, touch
    listOfGoes = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    if touch == 'start':
        xgo = random.choice(listOfGoes)
        ygo = random.choice(listOfGoes)
    if touch == 'xr':
        xgo = random.choice([-5, -4, -3, -2, -1])
        ygo = random.choice(listOfGoes)
    if touch == 'xl':
        xgo = random.choice([1, 2, 3, 4, 5])
        ygo = random.choice(listOfGoes)
    if touch == 'yd':
        xgo = random.choice(listOfGoes)
        ygo = random.choice([-5, -4, -3, -2, -1])
    if touch == 'yu':
        xgo = random.choice(listOfGoes)
        ygo = random.choice([1, 2, 3, 4, 5])
    while go:
        if x > 860:
            touch = 'xr'
            go = False
        if x < 1:
            touch = 'xl'
            go = False
        if y > 360:
            touch = 'yd'
            go = False
        if y < 1:
            touch = 'yu'
            go = False
        pygame.draw.rect(screen, [255, 255, 255], [x, y, 140, 140], 0)
        x += xgo
        y += ygo
        screen.blit(ball, [x, y])
        pygame.time.delay(5)
        pygame.display.flip()

run = True
while run:
    pygame.time.delay(10)
    move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
