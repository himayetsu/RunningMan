import pygame
import mySprites
import random
pygame.init()
pygame.mixer.init()

# Initial global variables
level = 1
score = 0
remaining = 0

def start():
  screen = pygame.display.set_mode((640, 480))
  background = pygame.image.load("start screen.png")
  background = background.convert()
  clock = pygame.time.Clock()
  keepGoing = True
  while keepGoing:
    clock.tick(30)
    pygame.transform.scale(background,(40,80))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        keepGoing = False
    print(pygame.mouse.get_pos())

    if pygame.mouse.get_pos()[0]<=222 and pygame.mouse.get_pos()[0]>=124 and pygame.mouse.get_pos()[1]<=277 and pygame.mouse.get_pos()[1]>=247:
      while(pygame.mouse.get_pos()[0]<=222 and pygame.mouse.get_pos()[0]>=124 and pygame.mouse.get_pos()[1]<=277 and pygame.mouse.get_pos()[1]>=247):
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            main()

    if pygame.mouse.get_pos()[0]<=222 and pygame.mouse.get_pos()[0]>=124 and pygame.mouse.get_pos()[1]<=342 and pygame.mouse.get_pos()[1]>=310:
      while(pygame.mouse.get_pos()[0]<=222 and pygame.mouse.get_pos()[0]>=124 and pygame.mouse.get_pos()[1]<=342 and pygame.mouse.get_pos()[1]>=310):
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            tips()
    if pygame.mouse.get_pos()[0]<=222 and pygame.mouse.get_pos()[0]>=124 and pygame.mouse.get_pos()[1]<=407 and pygame.mouse.get_pos()[1]>=376:
      while(pygame.mouse.get_pos()[0]<=222 and pygame.mouse.get_pos()[0]>=124 and pygame.mouse.get_pos()[1]<=407 and pygame.mouse.get_pos()[1]>=376):
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            about()
    screen.blit(background,(0,0))
    pygame.display.flip()
  pygame.quit()


def about():
  screen = pygame.display.set_mode((640, 480))
  background = pygame.image.load("About.png")
  background = background.convert()
  clock = pygame.time.Clock()
  keepGoing = True
  while keepGoing:
    clock.tick(30)
    print(pygame.mouse.get_pos())
    pygame.transform.scale(background,(40,80))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        keepGoing = False
    if(pygame.mouse.get_pos()[0]>=28 and pygame.mouse.get_pos()[1]>=420 and pygame.mouse.get_pos()[0]<=173 and pygame.mouse.get_pos()[1]<=468):
      while(pygame.mouse.get_pos()[0]>=28 and pygame.mouse.get_pos()[1]>=420 and pygame.mouse.get_pos()[0]<=173 and pygame.mouse.get_pos()[1]<=468):
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
              start()
    screen.blit(background,(0,0))
    pygame.display.flip()
  pygame.quit()




def tips():
  screen = pygame.display.set_mode((640, 480))
  background = pygame.image.load("start screen.png")
  background = background.convert()
  clock = pygame.time.Clock()
  keepGoing = True
  pagenum = 0;
  while keepGoing:
    clock.tick(30)
    print(pygame.mouse.get_pos())
    pygame.transform.scale(background,(40,80))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        keepGoing = False
    if(pagenum==0):
      background = pygame.image.load("tip0.png")
      background = background.convert()
      if pygame.mouse.get_pos()[0]>=522 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[0]<=614 and pygame.mouse.get_pos()[1]<=65:
        while(pygame.mouse.get_pos()[0]>=522 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[0]<=614 and pygame.mouse.get_pos()[1]<=65):
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
              pagenum += 1

      
    if(pagenum==1):
      background = pygame.image.load("tip1.png")
      background = background.convert()
      if pygame.mouse.get_pos()[0]>=522 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[0]<=614 and pygame.mouse.get_pos()[1]<=65:
        while(pygame.mouse.get_pos()[0]>=522 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[0]<=614 and pygame.mouse.get_pos()[1]<=65):
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
              pagenum += 1

      if pygame.mouse.get_pos()[0]>=29 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[0]<=122 and pygame.mouse.get_pos()[1]<=65:
        while(pygame.mouse.get_pos()[0]>=29 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[0]<=122 and pygame.mouse.get_pos()[1]<=65):
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
              pagenum -= 1
          
      
    if(pagenum==2):
      background = pygame.image.load("tip2.png")
      background = background.convert()
      if pygame.mouse.get_pos()[0]>=522 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[0]<=614 and pygame.mouse.get_pos()[1]<=65:
        while(pygame.mouse.get_pos()[0]>=522 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[0]<=614 and pygame.mouse.get_pos()[1]<=65):
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
              pagenum += 1

      if pygame.mouse.get_pos()[0]>=29 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[0]<=122 and pygame.mouse.get_pos()[1]<=65:
        while(pygame.mouse.get_pos()[0]>=29 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[0]<=122 and pygame.mouse.get_pos()[1]<=65):
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
              pagenum -= 1

    if(pagenum==3):
      background = pygame.image.load("tip3.png")
      background = background.convert()  
      if pygame.mouse.get_pos()[0]>=522 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[0]<=614 and pygame.mouse.get_pos()[1]<=65:
        while(pygame.mouse.get_pos()[0]>=522 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[0]<=614 and pygame.mouse.get_pos()[1]<=65):
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
              pagenum += 1

      if pygame.mouse.get_pos()[0]>=29 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[0]<=122 and pygame.mouse.get_pos()[1]<=65:
        while(pygame.mouse.get_pos()[0]>=29 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[0]<=122 and pygame.mouse.get_pos()[1]<=65):
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
              pagenum -= 1

    if(pagenum==4):
      background = pygame.image.load("tip4.png")
      background = background.convert()
      if pygame.mouse.get_pos()[0]>=29 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[0]<=122 and pygame.mouse.get_pos()[1]<=65:
        while(pygame.mouse.get_pos()[0]>=29 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[0]<=122 and pygame.mouse.get_pos()[1]<=65):
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
              pagenum -= 1

    if(pygame.mouse.get_pos()[0]>=28 and pygame.mouse.get_pos()[1]>=420 and pygame.mouse.get_pos()[0]<=173 and pygame.mouse.get_pos()[1]<=468):
      while(pygame.mouse.get_pos()[0]>=28 and pygame.mouse.get_pos()[1]>=420 and pygame.mouse.get_pos()[0]<=173 and pygame.mouse.get_pos()[1]<=468):
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
              start()
    screen.blit(background,(0,0))
    pygame.display.flip()
  pygame.quit()

def main():
  pygame.mouse.set_visible(False)
  global level
  global score
  global remaining
  bullets = []
  enemies = []
  game_over = False
  screen = pygame.display.set_mode((640, 480))
  background = pygame.image.load("Background.png")
  character = mySprites.Character(screen)
  cursor = mySprites.Cursor()
  
  for i in range((level*5)+5):
    entrance = random.randint(0,3)
    if(entrance==0):
      enemies.append(mySprites.Enemy(random.randint(261,379),-10,character))
    if(entrance==1):
      enemies.append(mySprites.Enemy(-10,random.randint(190,305),character))
    if(entrance==2):
      enemies.append(mySprites.Enemy(random.randint(261,379),490,character))
    if(entrance==3):
      enemies.append(mySprites.Enemy(650,random.randint(190,305),character))

  levelstr = mySprites.Label("Level: "+str(level), (50,30))
  enemynumstr = mySprites.Label("Enemies: "+str((level*5)+5), (580,30))
  scorestr = mySprites.Label("Score: "+str(score),(320,200))
  enemyGroup = pygame.sprite.OrderedUpdates(enemies)
  bulletGroup = pygame.sprite.OrderedUpdates()
  cursorSprite = pygame.sprite.OrderedUpdates(cursor)
  scoreSprite = pygame.sprite.OrderedUpdates(scorestr)
  allSprites = pygame.sprite.OrderedUpdates(character,enemies,levelstr,enemynumstr)

  clock = pygame.time.Clock()
  keepGoing = True

  while keepGoing:
    clock.tick(30)
    pygame.transform.scale(background,(40,80))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        keepGoing = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            character.go_up(True)
        if event.key == pygame.K_a:
            character.go_left(True)
        if event.key == pygame.K_s:
            character.go_down(True)
        if event.key == pygame.K_d:
            character.go_right(True)
            
      if event.type == pygame.MOUSEBUTTONDOWN:
          bullets.append(mySprites.Bullet(character.rect.centerx, character.rect.centery))
          bulletGroup.add(bullets[-1])
          allSprites.add(bullets[-1])

      if event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
            character.go_up(False)
        if event.key == pygame.K_a:
            character.go_left(False)
        if event.key == pygame.K_s:
            character.go_down(False)
        if event.key == pygame.K_d:
            character.go_right(False)

    if not enemyGroup:
        # Update
        level += 1
        mySprites.Enemy.speed += 0.1

        bullets = []
        enemies = []
        for i in range((level*5)+5):
          entrance = random.randint(0,3)
          if(entrance==0):
            enemies.append(mySprites.Enemy(random.randint(261,379),-10,character))
          if(entrance==1):
            enemies.append(mySprites.Enemy(-10,random.randint(190,305),character))
          if(entrance==2):
            enemies.append(mySprites.Enemy(random.randint(261,379),490,character))
          if(entrance==3):
            enemies.append(mySprites.Enemy(650,random.randint(190,305),character))

        levelstr = mySprites.Label("Level: "+str(level), (50,30))
        enemynumstr = mySprites.Label("Enemies: "+str((level*5)+5), (350,30))
        scorestr = mySprites.Label("Score: "+str(score),(320,200))
        enemyGroup = pygame.sprite.OrderedUpdates(enemies)
        bulletGroup = pygame.sprite.OrderedUpdates()
        cursorSprite = pygame.sprite.OrderedUpdates(cursor)
        scoreSprite = pygame.sprite.OrderedUpdates(scorestr)
        allSprites = pygame.sprite.OrderedUpdates(character,enemies,levelstr,enemynumstr)

    if pygame.sprite.spritecollide(character, enemyGroup, True):
        game_over = True


    enemycountold = len(enemyGroup.sprites())
    for bullet in bullets:
      if pygame.sprite.spritecollide(bullet, enemyGroup, True):
        bullet.kill()

    enemycountnew = len(enemyGroup.sprites())

    if(enemycountold>0):
      score += enemycountold-enemycountnew
    else:
      score += 1
    scorestr = mySprites.Label("Score: "+str(score),(320,200))
    scoreSprite = pygame.sprite.OrderedUpdates(scorestr)

    if(game_over):
      screen.blit(pygame.image.load("gameover.png"),(0,0))
      allSprites.draw(screen)
      scoreSprite.update()
      scoreSprite.draw(screen)
      cursorSprite.update()
      cursorSprite.draw(screen)
      font = pygame.font.SysFont('Ariel',20)
      restext = font.render('Restart' , True , (255,255,255))
      quitext = font.render('Quit' , True , (255,255,255))
      pygame.draw.rect(screen,(34,34,34),[150,250,100,30])
      pygame.draw.rect(screen,(34,34,34),[400,250,100,30])
      screen.blit(restext , (177,257))
      screen.blit(quitext , (435,257))
      if pygame.mouse.get_pos()[0]<=250 and pygame.mouse.get_pos()[0]>=150 and pygame.mouse.get_pos()[1]<=280 and pygame.mouse.get_pos()[1]>=250:
        while(pygame.mouse.get_pos()[0]<=250 and pygame.mouse.get_pos()[0]>=150 and pygame.mouse.get_pos()[1]<=280 and pygame.mouse.get_pos()[1]>=250):
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
              level = 1
              score = 0
              remaining = 0
              mySprites.Enemy.speed = 3
              main()
          screen.blit(pygame.image.load("gameover.png"),(0,0))
          allSprites.draw(screen)
          scoreSprite.update()
          scoreSprite.draw(screen)
          cursorSprite.update()
          cursorSprite.draw(screen)
          font = pygame.font.SysFont('Ariel',20)
          restext = font.render('Restart' , True , (255,255,255))
          quitext = font.render('Quit' , True , (255,255,255))
          pygame.draw.rect(screen,(34,34,34),[150,250,100,30])
          pygame.draw.rect(screen,(34,34,34),[400,250,100,30])
          screen.blit(restext , (177,257))
          screen.blit(quitext , (435,257))
          cursorSprite.update()
          cursorSprite.draw(screen)
          pygame.display.flip()


      if pygame.mouse.get_pos()[0]<=500 and pygame.mouse.get_pos()[0]>=400 and pygame.mouse.get_pos()[1]<=280 and pygame.mouse.get_pos()[1]>=250:
        while(pygame.mouse.get_pos()[0]<=500 and pygame.mouse.get_pos()[0]>=400 and pygame.mouse.get_pos()[1]<=280 and pygame.mouse.get_pos()[1]>=250):
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
              exit()
          screen.blit(pygame.image.load("gameover.png"),(0,0))
          allSprites.draw(screen)
          scoreSprite.update()
          scoreSprite.draw(screen)
          cursorSprite.update()
          cursorSprite.draw(screen)
          font = pygame.font.SysFont('Ariel',20)
          restext = font.render('Restart' , True , (255,255,255))
          quitext = font.render('Quit' , True , (255,255,255))
          pygame.draw.rect(screen,(34,34,34),[150,250,100,30])
          pygame.draw.rect(screen,(34,34,34),[400,250,100,30])
          screen.blit(restext , (177,257))
          screen.blit(quitext , (435,257))
          cursorSprite.update()
          cursorSprite.draw(screen)
          pygame.display.flip()

    else:
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
    cursorSprite.update()
    cursorSprite.draw(screen)
    pygame.display.flip()
  pygame.quit()

start()

# main()

