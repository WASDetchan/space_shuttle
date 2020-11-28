import pygame

pygame.init()
screen = pygame.display.set_mode([1000, 500])
screen.fill([255, 255, 255])

s = {"x": 200,
     "y": 200,
     "width": 40,
     "height": 40,
     "speed": 5,
     "color": [0, 0, 255],
     "line": 0}

pygame.draw.rect(screen, (s["color"]), (s["x"], s["y"], s["width"], s["height"]), s["line"])
ball = pygame.image.load("beach_ball.png")
screen.blit(ball, [500, 100])
pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

