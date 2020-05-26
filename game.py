import pygame.freetype

pygame.init()
s = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption("Hamster escape")

i = pygame.image.load('./hamster.png')
pygame.display.set_icon(i)

# Player
playerImg = pygame.image.load('hamster.png')

# pygame on Fedora 32 doesn't support mp3. Use OGG format music.
# https://patrickdearteaga.com/royalty-free-music/
pygame.mixer.music.load('Intergalactic Odyssey.ogg')


clock = pygame.time.Clock()
font = pygame.freetype.SysFont(None, 34)
font.origin = True

icon_size = 32

won_game = False

exit_value = 3

class Maze:
    def __init__(self):
        self.column = 36
        self.row = 18
        self.player_x = 1
        self.player_y = 1
        self.maze = [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1,
            1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1,
            1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1,
            exit_value, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
            exit_value,
        ]

    def draw(self, display_surf, block_image, exit_image):
        bx = 0
        by = 0
        for i in range(0, self.column * self.row):
            if self.maze[bx + (by * self.column)] == 1:
                display_surf.blit(block_image, (bx * icon_size, by * icon_size))

            if self.maze[bx + (by * self.column)] == exit_value:
                display_surf.blit(exit_image, (bx * icon_size, by * icon_size))

            if bx == self.player_x and by == self.player_y:
                display_surf.blit(playerImg, (bx * icon_size, by * icon_size))

            bx = bx + 1
            if bx > self.column - 1:
                bx = 0
                by = by + 1

    def down(self):
        if self.player_y + 1 < self.row and self.maze[(self.player_y + 1) * self.column + self.player_x] != 1:
            self.player_y = self.player_y + 1

    def up(self):
        if self.player_y - 1 >= 0 and self.maze[(self.player_y - 1) * self.column + self.player_x] != 1:
            self.player_y = self.player_y - 1

    def left(self):
        if self.player_x - 1 >= 0 and self.maze[self.player_y * self.column + self.player_x - 1] != 1:
            self.player_x = self.player_x - 1

    def right(self):
        if self.player_x + 1 < self.column and self.maze[self.player_y * self.column + self.player_x + 1] != 1:
            self.player_x = self.player_x + 1

    def check_win(self):
        #print("current x is {}, current y is {}".format(self.player_x, self.player_y))
        if self.player_x == self.column - 1 and self.player_y == self.row - 1:
            return True
        return False


maze = Maze()

_block_surf = pygame.image.load("cage32.png").convert()
_exit_surf = pygame.image.load("exit.png").convert()

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
            pygame.mixer.music.stop()
            pygame.display.quit()
            break

        # if keystroke is pressed check whether its right or left
        if not won_game and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                maze.left()
            if event.key == pygame.K_RIGHT:
                maze.right()
            if event.key == pygame.K_UP:
                maze.up()
            if event.key == pygame.K_DOWN:
                maze.down()

    if not won_game:
        s.fill((192, 192, 192))

        ticks = pygame.time.get_ticks()
        millis = ticks % 1000
        seconds = int(ticks / 1000 % 60)
        minutes = int(ticks / 60000 % 24)
        out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        font.render_to(s, (1000, 800), out, pygame.Color('dodgerblue'))

        maze.draw(s, _block_surf, _exit_surf)
        pygame.display.update()

        won_game = maze.check_win()
        if won_game:
            pygame.mixer.music.load('Ship.ogg')
            pygame.mixer.music.play(-1)
        # clock.tick(60)
