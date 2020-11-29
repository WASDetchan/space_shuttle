import pygame
import os
import random

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
surface = pygame.display.get_surface()
pygame.display.set_caption('Space race', '\\pics\\test.png')
icon = pygame.image.load(os.getcwd() + '\\pics\\test.png')
pygame.display.set_icon(icon)
screen.fill([48, 5, 89])
pygame.display.flip()
width = surface.get_width()
height = surface.get_height()
bullets = pygame.sprite.Group()
meteors = pygame.sprite.Group()
st = {}
for star in range(random.randint(10, 20)):
    st[star] = [random.randint(0, width-32), random.randint(0, height-32)]


# function to check key events
def eventcheck():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return 'space'
            elif event.key == pygame.K_ESCAPE:
                return 'esc'
            elif event.key == pygame.K_UP:
                return 'up'
            elif event.key == pygame.K_DOWN:
                return 'down'
            elif event.key == pygame.K_RIGHT:
                return 'right'
            elif event.key == pygame.K_LEFT:
                return 'left'
            elif event.key == pygame.K_LSHIFT:
                return 'shift'
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                return 'spaced'
            elif event.key == pygame.K_UP:
                return 'upd'
            elif event.key == pygame.K_DOWN:
                return 'downd'
            elif event.key == pygame.K_RIGHT:
                return 'rightd'
            elif event.key == pygame.K_LEFT:
                return 'leftd'
        else:
            return 'NoEvent'


class BulletClass(pygame.sprite.Sprite):
    def __init__(self, bullet_file, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(bullet_file)
        self.rect = self.image.get_rect()
        self.rect.left = x + 400
        self.rect.top = y + 90

    def move(self):
        self.rect = self.rect.move(20, 0)

    def IsOutOfScreen(self):
        if self.rect.left > width:
            return True
        else:
            return False


class MeteorClass(pygame.sprite.Sprite):
    def __init__(self, w, h):
        self.hp = random.randint(1, 5)
        self.speed = random.randint(3, 7)
        self.size = random.choice(['s', 's', 's', 'm', 'm', 'm', 'm', 'm', 'l'])
        pygame.sprite.Sprite.__init__(self)
        if self.size == 's':
            self.image = pygame.image.load(os.getcwd() + '\\pics\\meteors.png')
            self.rect = self.image.get_rect()
            self.rect.top = random.randint(0, h - 32)
        if self.size == 'm':
            self.image = pygame.image.load(os.getcwd() + '\\pics\\meteorm.png')
            self.rect = self.image.get_rect()
            self.rect.top = random.randint(0, h - 64)
        if self.size == 'l':
            self.image = pygame.image.load(os.getcwd() + '\\pics\\meteorl.png')
            self.rect = self.image.get_rect()
            self.rect.top = random.randint(0, h - 256)
        self.rect.left = w + 1

    def move(self):
        self.rect.left -= self.speed

    def IsDamaged(self, hp):
        for bullet in bullets:
            pygame.sprite.spritecollide(self, bullets, True)


def maincycle(w, h, stars):
    y = h // 2 - 76
    x = width//7
    clock = pygame.time.Clock()
    startexture = pygame.image.load(os.getcwd() + '\\pics\\star.png')
    shuttletexture = pygame.image.load(os.getcwd() + '\\pics\\shuttle5.png')
    bullettexture = os.getcwd() + '\\pics\\bullet.png'
    cooldown = 0
    up = False
    down = False
    right = False
    left = False
    shoot = False
    while True:
        screen.fill([48, 5, 89])
        if up:
            if y > 22:
                y -= 22
        if down:
            if y < h - 152 - 22:
                y += 22
        if right:
            if x < w - 400 - 30:
                x += 30
        if left:
            if x > 30:
                x -= 30
        if random.randint(0, 40) == 0:
            meteor = MeteorClass(width, height)
            meteors.add(meteor)
        if shoot:
            cooldown += 1
            if cooldown == 10:
                cooldown = 0
                bullet = BulletClass(bullettexture, x, y)
                bullets.add(bullet)
        for i in stars:
            star = stars[i]
            screen.blit(startexture, [star[0], star[1]])
        for meteor in meteors:
            meteor.move()
            screen.blit(meteor.image, [meteor.rect.left, meteor.rect.top])
        for bullet in bullets:
            bullet.move()
            if bullet.IsOutOfScreen():
                bullets.remove(bullet)
                pygame.sprite.Sprite.kill(bullet)
            screen.blit(bullet.image, bullet.rect)
        screen.blit(shuttletexture, [x, y])
        pygame.display.flip()
        clock.tick(60)
        event = eventcheck()
        if event == 'esc':
            pygame.quit()
            return
        elif event == 'shift':
            shoot = True
        elif event == 'space':
            shoot = True
        elif event == 'up':
            up = True
        elif event == 'down':
            down = True
        elif event == 'right':
            right = True
        elif event == 'left':
            left = True
        elif event == 'spaced':
            shoot = False
        elif event == 'upd':
            up = False
        elif event == 'downd':
            down = False
        elif event == 'rightd':
            right = False
        elif event == 'leftd':
            left = False


maincycle(width, height, st)
