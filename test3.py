import pygame

pygame.init()
screen = pygame.display.set_mode([1000, 500])
screen.fill([255, 255, 255])
ball = pygame.image.load("beach_ball.png")
x = 50
y = 50
# screen.blit(ball, [x, y])
pygame.display.flip()


def move(xgo, ygo, coor, s, tsec):
    global screen, ball
    for i in range(99):
        speed = s / (tsec * 100)
        pygame.draw.rect(screen, [255, 255, 255], [int(xgo), int(ygo), 140, 140], 0)
        screen.blit(ball, [int(xgo), int(ygo)])
        pygame.time.delay(10)

        if coor == 'x':
            xgo += 10 * speed
        elif coor == 'y':
            ygo += 10 * speed
        pygame.display.flip()


# pygame.time.delay(2000)
# pygame.draw.rect(screen, [255, 255, 255], [300, 100, 440, 240], 0)
# screen.blit(ball, [100, 100])
# pygame.display.flip()


move(50, 50, 'x', 300, 10)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
