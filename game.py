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

# pygame on Fedora 32 doesn't support mp3. Use OGG format music.
# https://patrickdearteaga.com/royalty-free-music/
pygame.mixer.music.load('TheBiggestDiscovery.ogg')
pygame.mixer.music.play(-1)

def hamster():
    s.blit(playerImg, (playerX, playerY))

clock=pygame.time.Clock()
font=pygame.freetype.SysFont(None, 34)
font.origin=True


class Maze:
    def __init__(self):
        self.M = 10
        self.N = 8
        self.maze = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
                     1, 0, 1, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 1, 0, 1, 1, 1, 1, 0, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]

    def draw(self, display_surf, image_surf):
        bx = 0
        by = 0
        for i in range(0, self.M * self.N):
            if self.maze[bx + (by * self.M)] == 1:
                display_surf.blit(image_surf, (bx * 44, by * 44))

            bx = bx + 1
            if bx > self.M - 1:
                bx = 0
                by = by + 1

maze = Maze();

_block_surf = pygame.image.load("wall.png").convert()

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
    maze.draw(s, _block_surf)
    # pygame.display.flip()

    hamster()
    pygame.display.update()
    clock.tick(60)