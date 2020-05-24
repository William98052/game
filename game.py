import pygame
import pygame.freetype

pygame.init()
s=pygame.display.set_mode((800,600))
pygame.display.set_caption("Hamster escape")

i=pygame.image.load('./hamster.png')
pygame.display.set_icon(i)

# Player
playerImg = pygame.image.load('hamster64.png')
playerX = 370
playerY = 480

pygame.mixer.music.load('BS.mp3')
pygame.mixer.music.play(-1)
def hamster():
    s.blit(playerImg, (playerX, playerY))

clock=pygame.time.Clock()
font=pygame.freetype.SysFont(None, 34)
font.origin=True

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
            break
    
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX = playerX - 35
            if event.key == pygame.K_RIGHT:
                playerX = playerX + 35
                
                # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY = playerY - 35
            if event.key == pygame.K_DOWN:
                playerY = playerY + 35
    
    s.fill((192,192,192))
    ticks=pygame.time.get_ticks()
    millis=ticks%1000
    seconds=int(ticks/1000 % 60)
    minutes=int(ticks/60000 % 24)
    out='{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
    font.render_to(s, (100, 100), out, pygame.Color('dodgerblue'))
    
    hamster()
    pygame.display.update()
    clock.tick(60)