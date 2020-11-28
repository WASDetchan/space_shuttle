import pygame, random

pygame.init()
width, height = 1000, 500
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Random ball', 'beach_ball.ico')
screen.fill([255, 255, 255])
x = 50
y = 50
# screen.blit(ball, [x, y])
pygame.display.flip()
touch = 'start'
xgo = 0
ygo = 0
image_file = "beach_ball.png"


class BallClass(pygame.sprite.Sprite):
    def __init__(self, ball_file, location, ballspeed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(ball_file)

        self.rect = self.image.get_rect()


        self.rect.left = location['x']
        self.rect.top = location['y']
        self.speed = ballspeed

    def move(self):  # передвижение
        self.rect = self.rect.move(self.speed['x'], self.speed['y'])

        if self.rect.top > (height - 140) or self.rect.top < 0:  # проверка отскока по y
            self.speed['y'] = -self.speed['y']

        if self.rect.right > width or self.rect.left < 0:  # проверка отскока по x
            self.speed['x'] = -self.speed['x']


def animate(group):
    screen.fill([255, 255, 255])
    for balls in group:
        group.remove(balls)
        if pygame.sprite.spritecollide(balls, group, False):
            balls.speed['x'], balls.speed['y'] = -balls.speed['x'], -balls.speed['y']
        group.add(balls)
        balls.move()
        screen.blit(balls.image, balls.rect)
    pygame.display.flip()
    pygame.time.delay(20)


group = pygame.sprite.Group()
listOfGoes = [-5, -4, 4, 5]
for row in range(1, 3):
    for column in range(1, 3):
        coor = {'x': 150 * column, 'y': 150 * row}
        speed = {'x': random.choice(listOfGoes), 'y': random.choice(listOfGoes)}
        ball = BallClass(image_file, coor, speed)
        group.add(ball)
    # move = {'x':random.choice(listOfGoes), 'y':random.choice(listOfGoes)}


run = True
while run:  # основной цикл
    pygame.time.delay(10)
    # move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    screen.fill([255, 255, 255])
    animate(group)
