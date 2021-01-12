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
ships = pygame.sprite.Group()
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


class ShipClass(pygame.sprite.Sprite):
    def __init__(self, w, h):
        pygame.sprite.Sprite.__init__(self)
        ships.add(self)
        self.texture1 = pygame.image.load(os.getcwd() + '\\pics\\shuttle6animation\\0.png')
        self.texture2 = pygame.image.load(os.getcwd() + '\\pics\\shuttle6animation\\1.png')
        self.texture3 = pygame.image.load(os.getcwd() + '\\pics\\shuttle6animation\\2.png')
        self.texture4 = pygame.image.load(os.getcwd() + '\\pics\\shuttle6animation\\3.png')
        self.texture5 = pygame.image.load(os.getcwd() + '\\pics\\shuttle6animation\\4.png')
        self.texture6 = pygame.image.load(os.getcwd() + '\\pics\\shuttle6animation\\5.png')
        self.texture7 = pygame.image.load(os.getcwd() + '\\pics\\shuttle6animation\\6.png')
        self.texture8 = pygame.image.load(os.getcwd() + '\\pics\\shuttle6animation\\7.png')
        self.image = self.texture1
        self.rect = self.image.get_rect()
        self.rect.left = w//7
        self.rect.top = h//2 - 76
        self.texturetimer = 0

    def textureupdate(self):
        if self.texturetimer == 10:
            self.image = self.texture1
        elif self.texturetimer == 20:
            self.image = self.texture2
        elif self.texturetimer == 30:
            self.image = self.texture3
        elif self.texturetimer == 40:
            self.image = self.texture4
        elif self.texturetimer == 50:
            self.image = self.texture5
        elif self.texturetimer == 60:
            self.image = self.texture6
        elif self.texturetimer == 70:
            self.image = self.texture7
        elif self.texturetimer == 80:
            self.image = self.texture8
            self.texturetimer = 1



    def up(self):
        self.rect.top -= 22

    def down(self):
        self.rect.top += 22

    def right(self):
        self.rect.left += 30

    def left(self):
        self.rect.left -= 30


class BulletClass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd() + '\\pics\\bullet.png')
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
        self.hp = random.randint(1, 2)
        self.speed = random.uniform(0.5, 1.5)
        self.size = random.choice(['s', 'm', 'm', 'm', 'm', 'm', 'l', 'l'])
        pygame.sprite.Sprite.__init__(self)
        if self.size == 's':
            self.image = pygame.image.load(os.getcwd() + '\\pics\\meteors.png')
            self.rect = self.image.get_rect()
            self.rect.top = random.randint(130, h - 256)
        if self.size == 'm':
            self.image = pygame.image.load(os.getcwd() + '\\pics\\meteorm.png')
            self.rect = self.image.get_rect()
            self.rect.top = random.randint(130, h - 256)
        if self.size == 'l':
            self.image = pygame.image.load(os.getcwd() + '\\pics\\meteorl.png')
            self.rect = self.image.get_rect()
            self.rect.top = random.randint(130, h - 256)
        self.rect.left = w + 1
        self.floatx = self.rect.left

    def move(self):
        self.floatx -= self.speed
        self.rect.left = int(self.floatx)
        if self.rect.left < -256:
            pygame.sprite.Sprite.kill(self)

    def IsDamaged(self, hp):
        if pygame.sprite.spritecollide(self, bullets, True):
            pygame.sprite.Sprite.kill(self)
        if pygame.sprite.spritecollide(self, ships, True):
            a = 1


def maincycle(w, h, stars):
    ship = ShipClass(w, h)
    clock = pygame.time.Clock()
    startexture = pygame.image.load(os.getcwd() + '\\pics\\star.png')
    cooldown = 0
    up = False
    down = False
    right = False
    left = False
    shoot = False
    while True:
        screen.fill([48, 5, 89])
        if up:
            if ship.rect.top > 22:
                ship.up()
        if down:
            if ship.rect.top < h - 22 - 152:
                ship.down()
        if right:
            if ship.rect.left < w - 400 - 30:
                ship.right()
        if left:
            if ship.rect.left > 30:
                ship.left()
        if random.randint(0, 20) == 0:
            meteor = MeteorClass(width, height)
            meteors.add(meteor)
        if shoot:
            cooldown += 10
            if cooldown == 10:
                cooldown = 0
                bullet = BulletClass(ship.rect.left, ship.rect.top)
                bullets.add(bullet)
        for i in stars:
            star = stars[i]
            screen.blit(startexture, [star[0], star[1]])
        for meteor in meteors:
            meteor.move()
            screen.blit(meteor.image, [meteor.rect.left, meteor.rect.top])
            meteor.IsDamaged(1)
        for bullet in bullets:
            bullet.move()
            if bullet.IsOutOfScreen():
                bullets.remove(bullet)
                pygame.sprite.Sprite.kill(bullet)
            screen.blit(bullet.image, bullet.rect)
        ship.texturetimer += 1
        ship.textureupdate()
        screen.blit(ship.image, [ship.rect.left, ship.rect.top])
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
