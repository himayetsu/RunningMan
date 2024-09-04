import pygame
import math
class Character(pygame.sprite.Sprite):
    charx = 0
    chary = 0
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0,0,0))
        self.image = pygame.image.load("Character test.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = 320
        self.rect.centery = 240
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0
        self.speed = 5
        Character.charx = self.rect.centerx
        Character.chary = self.rect.centery
    def go_up(self, mode): 
      if mode:
        self.up = self.speed
      else:
        self.up = 0
    def go_down(self, mode):
      if mode:
        self.down = self.speed
      else:
        self.down = 0
    def go_left(self, mode):
      if mode:
        self.left = self.speed
      else:
        self.left = 0
    def go_right(self, mode):
      if mode:
        self.right = self.speed
      else:
        self.right = 0
    def update(self):
      self.rect.centerx += self.right - self.left
      self.rect.centery += self.down - self.up
      if(self.rect.centerx < 17.5):
        self.rect.centerx = 17.5
      if(self.rect.centery < 22.5):
        self.rect.centery = 22.5
      if(self.rect.centerx > 622.5):
        self.rect.centerx = 622.5
      if(self.rect.centery > 457.5):
        self.rect.centery = 457.5
      Character.charx = self.rect.centerx
      Character.chary = self.rect.centery
      

class Cursor(pygame.sprite.Sprite):
    mousex = 0;
    mousey = 0;
    def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      Cursor.mousex = pygame.mouse.get_pos()[0]
      Cursor.mousey = pygame.mouse.get_pos()[1]
      self.image = pygame.Surface((50, 50))
      self.image = pygame.image.load("Cursor.png")
      self.rect = self.image.get_rect()
      self.rect.center = Cursor.mousex,Cursor.mousey
    def update(self):
      Cursor.mousex = pygame.mouse.get_pos()[0]
      Cursor.mousey = pygame.mouse.get_pos()[1]
      self.rect.center = Cursor.mousex,Cursor.mousey

      

class Enemy(pygame.sprite.Sprite):
    speed = 3
    def __init__(self, x, y,character):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0,0,0))
        self.image = pygame.image.load("Enemy test.png")    
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
    def update(self):

        # my own algorithm to find the shortest path to the player while still maintaining constant speed
        charposx = Character.charx
        charposy = Character.chary
        xdiff = charposx - self.rect.centerx
        ydiff = charposy - self.rect.centery
        dist = math.sqrt(math.pow(xdiff, 2) + math.pow(ydiff, 2))
        speed = Enemy.speed
        increments = dist/speed
        xspeed = xdiff/increments
        yspeed = ydiff/increments
        self.rect.centerx += xspeed
        self.rect.centery += yspeed

          
        



class Bullet(pygame.sprite.Sprite):
    speed = 10
    xspeed = 0
    yspeed = 0
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        bullposx = self.rect.left
        bullposy = self.rect.top
        xdiff = Cursor.mousex - bullposx
        ydiff = Cursor.mousey - bullposy
        dist = math.sqrt(math.pow(xdiff, 2) + math.pow(ydiff, 2))
        speed = Bullet.speed
        increments = dist/speed
        Bullet.xspeed = xdiff/increments
        Bullet.yspeed = ydiff/increments
    def update(self):
        self.rect.centerx += Bullet.xspeed
        self.rect.centery += Bullet.yspeed
        if(self.rect.centerx < 15):
          Bullet.kill(self)
        if(self.rect.centery < 15):
          Bullet.kill(self)
        if(self.rect.centerx > 625):
          Bullet.kill(self)
        if(self.rect.centery > 465):
          Bullet.kill(self)



class Label(pygame.sprite.Sprite):
    def __init__(self, message, x_y_center):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", 12)
        self.text = message
        self.center = x_y_center
     	
    def setText(self, message):
        self.text = message
             	
    def update(self):
        self.image = self.font.render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center
