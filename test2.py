import pygame, random
from time import sleep

pygame.init()
screen = pygame.display.set_mode([1000, 500])
screen.fill([255, 255, 255])

for i in range(100):
    x = random.randint(0, 1000)
    y = random.randint(0, 500)
    width = random.randint(0, 1000-x)
    height = random.randint(0, 500-y)
         #"speed": random.randint(1000, 500),
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    line = random.randint(1, 10)
    pygame.draw.rect(screen, color, (x, y, width, height), line)
    pygame.display.flip()
    sleep(0.1)



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
