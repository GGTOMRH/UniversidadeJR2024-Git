# Example file showing a circle moving on screen
import pygame
import time
import random

# pygame setup/variaveis
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0
v = 200
vE = v/1.45
vBE = v/1.5
coin_exis = True
menu = True
score = 0
spawned = True
highscore = 16
raio = 12
aum = True
aum2 = True
aum3 = True

#localização
coin_pos = pygame.Vector2(random.randint(300,1600), random.randint(300, 700))
big_enemy_pos = pygame.Vector2(random.randint(300,1600), 100)
enemy_pos = pygame.Vector2(random.randint(300,1600), 980)
player_pos = pygame.Vector2(screen.get_width() / 2, 500)
bg = pygame.image.load("./run.jpg").convert_alpha()


#funçoes
def create_enemy():
    if score < 10:
     pygame.draw.circle(screen, "green", enemy_pos, raio)
    elif score >= 10 and score < 15:
        pygame.draw.circle(screen, "orange", enemy_pos, raio)
    elif score >= 15:
       pygame.draw.circle(screen, "red", enemy_pos, raio)
def create_big_enemy():
    if score < 5:
     pygame.draw.circle(screen, "blue", big_enemy_pos, raio)
    elif score >= 5 and score < 15:
      pygame.draw.circle(screen, "purple", big_enemy_pos, raio)
    elif score >= 15:
       pygame.draw.circle(screen, "red", big_enemy_pos, raio)
def create_coin():
    pygame.draw.circle(screen, "yellow", coin_pos, 10)

pygame.display.toggle_fullscreen()
while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    screen.blit(bg, (0, 0))
    #paredes
    pygame.draw.line(screen, "red", (25, 25), (1895, 25), 15)
    pygame.draw.line(screen, "red", (25, 25), (25, 1055), 15)
    pygame.draw.line(screen, "red", (25, 1055), (1895, 1055), 15)
    pygame.draw.line(screen, "red", (1895, 25), (1895, 1055), 15)
    pygame.draw.circle(screen, "red", (25, 25), 6)
    pygame.draw.circle(screen, "red", (1895, 25), 6)
    pygame.draw.circle(screen, "red", (25, 1055), 6)
    pygame.draw.circle(screen, "red", (1895, 1055), 6)
    pygame.display.set_caption("RUN")

    #player/enemysds
    pygame.draw.circle(screen, "white", player_pos, 12)

    create_enemy()
    create_coin()
    create_big_enemy()
    if player_pos.x < (coin_pos.x + 20) and player_pos.x > (coin_pos.x - 20) and player_pos.y < (coin_pos.y + 20) and player_pos.y > (coin_pos.y - 20):
       coin_exis = False
       score += 1
    if coin_exis == False:
        coin_pos = pygame.Vector2(random.randint(100,1800), random.randint(100, 900))
        create_coin()
        v += 10
        vBE += 10
        vE += 10
        coin_exis = True
    if player_pos.x < (enemy_pos.x + (raio*1.7)) and player_pos.x > (enemy_pos.x - (raio*1.7)) and player_pos.y < (enemy_pos.y + (raio*1.7)) and player_pos.y > (enemy_pos.y - (raio*1.7)) or player_pos.x < (big_enemy_pos.x + (raio*1.7)) and player_pos.x > (big_enemy_pos.x - (raio*1.7)) and player_pos.y < (big_enemy_pos.y + (raio*1.7)) and player_pos.y > (big_enemy_pos.y - (raio*1.7)):
       running = False
       break
    if aum:
        if score >= 5:
            raio += 2
            aum = False
    if aum2:
       if score >= 10:
          raio += 2
          aum2 = False
    if aum3:
       if score >= 15:
          raio +=2
          aum3 = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player_pos.y > 48:
         player_pos.y -= v * dt
    if keys[pygame.K_s]:
        if player_pos.y < 1035:
         player_pos.y += v * dt
    if keys[pygame.K_a]:
        if player_pos.x > 48:
         player_pos.x -= v * dt
    if keys[pygame.K_d]:
        if player_pos.x < 1876:
         player_pos.x += v * dt
    if score < 10:
        if enemy_pos.x < player_pos.x:
         enemy_pos.x += vE * dt
        if enemy_pos.x > player_pos.x:
            enemy_pos.x -= vE * dt
        if enemy_pos.y < player_pos.y:
            enemy_pos.y += vE* dt
        if enemy_pos.y > player_pos.y:
            enemy_pos.y -= vE* dt
    elif score >= 10 and score < 15:
        if enemy_pos.x < player_pos.x:
         enemy_pos.x += vE * dt
        if enemy_pos.x > player_pos.x:
            enemy_pos.x -= vE * dt
        if enemy_pos.y < player_pos.y:
            enemy_pos.y += vE*1.05* dt
        if enemy_pos.y > player_pos.y:
            enemy_pos.y -= vE* 1.05 * dt
    elif score >= 15:
        if enemy_pos.x < player_pos.x:
         enemy_pos.x += vE *1.1* dt
        if enemy_pos.x > player_pos.x:
            enemy_pos.x -= vE *1.1* dt
        if enemy_pos.y < player_pos.y:
            enemy_pos.y += vE*1.1* dt
        if enemy_pos.y > player_pos.y:
            enemy_pos.y -= vE* 1.1 * dt
        
    if score < 5:
        if big_enemy_pos.x < player_pos.x:
            big_enemy_pos.x += vBE * dt
        if big_enemy_pos.x > player_pos.x:
            big_enemy_pos.x -= vBE * dt
        if big_enemy_pos.y < player_pos.y:
            big_enemy_pos.y += vBE* dt
        if big_enemy_pos.y > player_pos.y:
            big_enemy_pos.y -= vBE* dt
    elif score >= 5 and score < 15:
        if big_enemy_pos.x < player_pos.x:
            big_enemy_pos.x += vBE * 1.1 * dt
        if big_enemy_pos.x > player_pos.x:
            big_enemy_pos.x -= vBE * 1.1 * dt
        if big_enemy_pos.y < player_pos.y:
            big_enemy_pos.y += vBE* dt
        if big_enemy_pos.y > player_pos.y:
            big_enemy_pos.y -= vBE* dt
    elif score >= 15:
        if big_enemy_pos.x < player_pos.x:
            big_enemy_pos.x += vBE * 1.1 * dt
        if big_enemy_pos.x > player_pos.x:
            big_enemy_pos.x -= vBE * 1.1 * dt
        if big_enemy_pos.y < player_pos.y:
            big_enemy_pos.y += vBE* 1.1* dt
        if big_enemy_pos.y > player_pos.y:
            big_enemy_pos.y -= vBE*1.1* dt


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
print(" ")
print(" ")
if score > highscore:
    highscore = score
    print("New highscore")
print(" ")
print(" ")
if score > 9:
    print ("--------------------------")
    print("|Your score was " + str(score) + "       |")
    print("|The highest score was " + str(highscore)+"|")     
    print("|Thanks for playing RUN  |")
    print("--------------------------")
else:
    print ("--------------------------")
    print("|Your score was " + str(score) + "        |")
    print("|The highest score was " + str(highscore)+"|")     
    print("|Thanks for playing RUN  |")
    print("--------------------------")
print(" ")
print(" ")
print(" ")
print(" ")
# Example file showing a circle moving on screen
import pygame
import time
import random

# pygame setup/variaveis
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0
v = 200
vE = v/1.45
vBE = v/1.5
coin_exis = True
menu = True
score = 0
spawned = True
highscore = 16
raio = 12
aum = True
aum2 = True
aum3 = True

#localização
coin_pos = pygame.Vector2(random.randint(300,1600), random.randint(300, 700))
big_enemy_pos = pygame.Vector2(random.randint(300,1600), 100)
enemy_pos = pygame.Vector2(random.randint(300,1600), 980)
player_pos = pygame.Vector2(screen.get_width() / 2, 500)
bg = pygame.image.load("./run.jpg").convert_alpha()


#funçoes
def create_enemy():
    if score < 10:
     pygame.draw.circle(screen, "green", enemy_pos, raio)
    elif score >= 10 and score < 15:
        pygame.draw.circle(screen, "orange", enemy_pos, raio)
    elif score >= 15:
       pygame.draw.circle(screen, "red", enemy_pos, raio)
def create_big_enemy():
    if score < 5:
     pygame.draw.circle(screen, "blue", big_enemy_pos, raio)
    elif score >= 5 and score < 15:
      pygame.draw.circle(screen, "purple", big_enemy_pos, raio)
    elif score >= 15:
       pygame.draw.circle(screen, "red", big_enemy_pos, raio)
def create_coin():
    pygame.draw.circle(screen, "yellow", coin_pos, 10)

pygame.display.toggle_fullscreen()
while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    screen.blit(bg, (0, 0))
    #paredes
    pygame.draw.line(screen, "red", (25, 25), (1895, 25), 15)
    pygame.draw.line(screen, "red", (25, 25), (25, 1055), 15)
    pygame.draw.line(screen, "red", (25, 1055), (1895, 1055), 15)
    pygame.draw.line(screen, "red", (1895, 25), (1895, 1055), 15)
    pygame.draw.circle(screen, "red", (25, 25), 6)
    pygame.draw.circle(screen, "red", (1895, 25), 6)
    pygame.draw.circle(screen, "red", (25, 1055), 6)
    pygame.draw.circle(screen, "red", (1895, 1055), 6)
    pygame.display.set_caption("RUN")

    #player/enemysds
    pygame.draw.circle(screen, "white", player_pos, 12)

    create_enemy()
    create_coin()
    create_big_enemy()
    if player_pos.x < (coin_pos.x + 20) and player_pos.x > (coin_pos.x - 20) and player_pos.y < (coin_pos.y + 20) and player_pos.y > (coin_pos.y - 20):
       coin_exis = False
       score += 1
    if coin_exis == False:
        coin_pos = pygame.Vector2(random.randint(100,1800), random.randint(100, 900))
        create_coin()
        v += 10
        vBE += 10
        vE += 10
        coin_exis = True
    if player_pos.x < (enemy_pos.x + (raio*1.7)) and player_pos.x > (enemy_pos.x - (raio*1.7)) and player_pos.y < (enemy_pos.y + (raio*1.7)) and player_pos.y > (enemy_pos.y - (raio*1.7)) or player_pos.x < (big_enemy_pos.x + (raio*1.7)) and player_pos.x > (big_enemy_pos.x - (raio*1.7)) and player_pos.y < (big_enemy_pos.y + (raio*1.7)) and player_pos.y > (big_enemy_pos.y - (raio*1.7)):
       running = False
       break
    if aum:
        if score >= 5:
            raio += 2
            aum = False
    if aum2:
       if score >= 10:
          raio += 2
          aum2 = False
    if aum3:
       if score >= 15:
          raio +=2
          aum3 = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player_pos.y > 48:
         player_pos.y -= v * dt
    if keys[pygame.K_s]:
        if player_pos.y < 1035:
         player_pos.y += v * dt
    if keys[pygame.K_a]:
        if player_pos.x > 48:
         player_pos.x -= v * dt
    if keys[pygame.K_d]:
        if player_pos.x < 1876:
         player_pos.x += v * dt
    if score < 10:
        if enemy_pos.x < player_pos.x:
         enemy_pos.x += vE * dt
        if enemy_pos.x > player_pos.x:
            enemy_pos.x -= vE * dt
        if enemy_pos.y < player_pos.y:
            enemy_pos.y += vE* dt
        if enemy_pos.y > player_pos.y:
            enemy_pos.y -= vE* dt
    elif score >= 10 and score < 15:
        if enemy_pos.x < player_pos.x:
         enemy_pos.x += vE * dt
        if enemy_pos.x > player_pos.x:
            enemy_pos.x -= vE * dt
        if enemy_pos.y < player_pos.y:
            enemy_pos.y += vE*1.05* dt
        if enemy_pos.y > player_pos.y:
            enemy_pos.y -= vE* 1.05 * dt
    elif score >= 15:
        if enemy_pos.x < player_pos.x:
         enemy_pos.x += vE *1.1* dt
        if enemy_pos.x > player_pos.x:
            enemy_pos.x -= vE *1.1* dt
        if enemy_pos.y < player_pos.y:
            enemy_pos.y += vE*1.1* dt
        if enemy_pos.y > player_pos.y:
            enemy_pos.y -= vE* 1.1 * dt
        
    if score < 5:
        if big_enemy_pos.x < player_pos.x:
            big_enemy_pos.x += vBE * dt
        if big_enemy_pos.x > player_pos.x:
            big_enemy_pos.x -= vBE * dt
        if big_enemy_pos.y < player_pos.y:
            big_enemy_pos.y += vBE* dt
        if big_enemy_pos.y > player_pos.y:
            big_enemy_pos.y -= vBE* dt
    elif score >= 5 and score < 15:
        if big_enemy_pos.x < player_pos.x:
            big_enemy_pos.x += vBE * 1.1 * dt
        if big_enemy_pos.x > player_pos.x:
            big_enemy_pos.x -= vBE * 1.1 * dt
        if big_enemy_pos.y < player_pos.y:
            big_enemy_pos.y += vBE* dt
        if big_enemy_pos.y > player_pos.y:
            big_enemy_pos.y -= vBE* dt
    elif score >= 15:
        if big_enemy_pos.x < player_pos.x:
            big_enemy_pos.x += vBE * 1.1 * dt
        if big_enemy_pos.x > player_pos.x:
            big_enemy_pos.x -= vBE * 1.1 * dt
        if big_enemy_pos.y < player_pos.y:
            big_enemy_pos.y += vBE* 1.1* dt
        if big_enemy_pos.y > player_pos.y:
            big_enemy_pos.y -= vBE*1.1* dt


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
print(" ")
print(" ")
if score > highscore:
    highscore = score
    print("New highscore")
print(" ")
print(" ")
if score > 9:
    print ("--------------------------")
    print("|Your score was " + str(score) + "       |")
    print("|The highest score was " + str(highscore)+"|")     
    print("|Thanks for playing RUN  |")
    print("--------------------------")
else:
    print ("--------------------------")
    print("|Your score was " + str(score) + "        |")
    print("|The highest score was " + str(highscore)+"|")     
    print("|Thanks for playing RUN  |")
    print("--------------------------")
print(" ")
print(" ")
print(" ")
print(" ")
