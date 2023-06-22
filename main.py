import pygame
import os
pygame.init()

def file_path(filename ):
    folder = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder, filename)
    return path

WIN_WIDTH = 900
WIN_HEIGHT = 600
FPS = 40

pygame.mixer.music.load(file_path(r"music\fon_music.mp3"))
pygame.mixer.music.set_volume(0.07)
pygame.mixer.music.play(-1)

fon = pygame.image.load(file_path(r"images\fon.png"))
fon = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT))
image_win = pygame.image.load(file_path(r"images\winner.png"))
image_win = pygame.transform.scale(image_win, (WIN_WIDTH, WIN_HEIGHT))
image_lose = pygame.image.load(file_path(r"images\loser.png"))
image_lose = pygame.transform.scale(image_lose, (WIN_WIDTH, WIN_HEIGHT))


window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(file_path(image))
        self.image = pygame.transform.scale(self.image, (width, height))

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, x, y, width, height, image, speed_x, speed_y):
        super().__init__(x, y, width, height, image)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.direction = "left"
        self.image_l = self.image
        self.image_r = pygame.transform.flip(self.image, True, False)
        

    def update(self):
        if self.speed_x < 0 and self.rect.left > 0 or self.speed_x > 0 and self.rect.right < WIN_WIDTH:
            self.rect.x += self.speed_x
        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.speed_x > 0:
            for wall in walls_touched:
                self.rect.right = min(self.rect.right, wall.rect.left)
        if self.speed_x < 0:
            for wall in walls_touched:
                self.rect.left = max(self.rect.left, wall.rect.right)
        
        if self.speed_y < 0 and self.rect.top > 0 or self.speed_y > 0 and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speed_y
        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.speed_y < 0:
            for wall in  walls_touched:
                self.rect.top = max(self.rect.top, wall.rect.bottom)
        if self.speed_y > 0:
            for wall in  walls_touched:
                self.rect.bottom = min(self.rect.bottom, wall.rect.top)
    
player = Player(80, 400, 60,60, r"images\mouse.png", 0, 0)
enemy1 = GameSprite(300, 100, 70, 70, r"images\angry_cat1.png")
finish = GameSprite(600, 400, 100, 100, r"images\cheese.png")



walls = pygame.sprite.Group()
wall1 = GameSprite(60, 50, 12, 400, r"images\bloks.png")
walls.add(wall1)
wall2 = GameSprite(60, 50, 770, 12, r"images\bloks.png")
walls.add(wall2)
wall3 = GameSprite(820, 50, 12, 397, r"images\bloks.png")
walls.add(wall3)
wall4 = GameSprite(60, 180, 250, 12, r"images\bloks.png")
walls.add(wall4)
wall5 = GameSprite(310, 132, 12, 60, r"images\bloks.png")
walls.add(wall5)
wall6 = GameSprite(160, 130, 162, 12, r"images\bloks.png")
walls.add(wall6)
wall7 = GameSprite(200, 435, 382, 12, r"images\bloks.png")
walls.add(wall7)
wall8 = GameSprite(330, 310, 12, 130, r"images\bloks.png")
walls.add(wall8)
wall9 = GameSprite(570, 340, 12, 95, r"images\bloks.png")
walls.add(wall9)
wall10 = GameSprite(720, 435, 105, 12, r"images\bloks.png")
walls.add(wall10)
wall11 = GameSprite(570, 330, 110, 12, r"images\bloks.png")
walls.add(wall11)
wall12 = GameSprite(720, 415, 12, 30, r"images\bloks.png")
walls.add(wall12)
wall13 = GameSprite(668, 260, 12, 70, r"images\bloks.png")
walls.add(wall13)
wall14 = GameSprite(520, 260, 160, 12, r"images\bloks.png")
walls.add(wall14)
wall15 = GameSprite(520, 260, 12, 40, r"images\bloks.png")
walls.add(wall15)
wall16 = GameSprite(452, 300, 80, 12, r"images\bloks.png")
walls.add(wall16)
wall17 = GameSprite(452, 250, 12, 50, r"images\bloks.png")
walls.add(wall17)
wall18 = GameSprite(400, 250, 55, 12, r"images\bloks.png")
walls.add(wall18)
wall19 = GameSprite(190, 330, 140, 12, r"images\bloks.png")
walls.add(wall19)
wall20 = GameSprite(190, 280, 12, 60, r"images\bloks.png")
walls.add(wall20)
wall21 = GameSprite(700, 130, 130, 12, r"images\bloks.png")
walls.add(wall21)
wall22 = GameSprite(580, 200, 12, 70, r"images\bloks.png")
walls.add(wall22)
wall23 = GameSprite(700, 130, 12, 60, r"images\bloks.png")
walls.add(wall23)
wall24 = GameSprite(420, 50, 12, 100, r"images\bloks.png")
walls.add(wall24)
wall25 = GameSprite(420, 150, 80, 12, r"images\bloks.png")
walls.add(wall25)
wall26 = GameSprite(488, 120, 12, 30, r"images\bloks.png")
walls.add(wall26)
wall27 = GameSprite(488, 110, 110, 12, r"images\bloks.png")
walls.add(wall27)
wall28 = GameSprite(420, 370, 12, 70, r"images\bloks.png")
walls.add(wall28)
wall29 = GameSprite(420, 370, 80, 12, r"images\bloks.png")
walls.add(wall29)
wall30 = GameSprite(270, 180, 12, 70, r"images\bloks.png")
walls.add(wall30)




level = 1
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if level == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.speed_x = -5
                    player.direction = "left"
                    player.image = player.image_l
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.speed_x = 5
                    player.direction = "right"
                    player.image = player.image_r
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.speed_y = -5
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.speed_y = 5
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.speed_x = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.speed_x = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.speed_y = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.speed_y = 0
                


    if level == 1:
        window.blit(fon, (0, 0))
        walls.draw(window)
        player.show()
        player.update()
        enemy1.show()
        finish.show()

        if pygame.sprite.collide_rect(player, finish):
            level = 10
            pygame.mixer.music.stop()
            pygame.mixer.music.load(file_path(r"music\victory_music.mp3"))
            pygame.mixer.music.play(-1)
    elif level == 10:
        window.blit(image_win, (0, 0))


    clock.tick(FPS)
    pygame.display.update()



