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
YELLOW = (255, 187, 45)
ORANGE = (255, 61, 19)
DARK_ORANGE = (255, 104, 18)
BROWN = (124, 77, 21)
WHITE = (255, 255, 255)


pygame.mixer.music.load(file_path(r"music\start_music.mp3"))
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

pygame.display.set_icon(pygame.image.load(file_path(r"images\icon.png"))) 

music_shoot = pygame.mixer.Sound(file_path(r"music\shoot_music.wav"))
music_shoot.set_volume(0.5)


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
    
    def shoot(self):
        if self.direction == "right":
            bullet = Bullet(self.rect.right, self.rect.centery, 30, 30, r"images\bullet.png", 8)
        elif self.direction == "left":
            bullet = Bullet(self.rect.left - 30, self.rect.centery, 30, 30, r"images\bullet.png", -8)
        bullets.add(bullet)



class Enemy(GameSprite):
    def __init__(self, x, y, width, height, image, direction, min_coord, max_coord, speed):
        super().__init__(x, y, width, height, image)
        self.direction = direction
        self.min_coord = min_coord
        self.max_coord = max_coord
        self.speed = speed

        if self.direction == "left":
            self.image_l = self.image
            self.image_r = pygame.transform.flip(self.image, True, False)
        elif self.direction == "right":
            self.image_r = self.image
            self.image_l = pygame.transform.flip(self.image, True, False)


    def update(self):
        if self.direction == "left" or self.direction == "right":
            if self.direction == "left":
                self.rect.x -= self.speed
            elif self.direction == "right":
                self.rect.x += self.speed
            
            if self.rect.right >= self.max_coord:
                self.direction = "left"
                self.image = self.image_r
            if self.rect.left <= self.min_coord:
                self.direction = "right"
                self.image = self.image_l
            
        elif self.direction == "up" or self.direction == "down":
            if self.direction == "up":
                self.rect.y -= self.speed
            elif self.direction == "down":
                self.rect.y += self.speed

            if self.rect.top <= self.min_coord:
                self.direction = "down"
            if self.rect.bottom >= self.max_coord:
                self.direction = "up"


class Bullet(GameSprite):
    def __init__(self, x, y, width, height, image, speed):
        super().__init__(x, y, width, height, image)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.right >= WIN_WIDTH or self.rect.left <= 0:
            self.kill()

class Button():
    def __init__(self, x, y, width, height, color1, color2, text, text_color, text_x, text_y):
        self.rect = pygame.Rect(x, y, width, height)
        self.color1 = color1
        self.color2 = color2
        self.color = color1
        shrift = pygame.font.SysFont("Times New Roman", 70)
        self.text = shrift.render(text, True, text_color)
        self.text_x = text_x
        self.text_y = text_y

    def show(self):
        pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.text, (self.rect.x + self.text_x, self.rect.y + self.text_y))



player = Player(80, 400, 50,50, r"images\mouse.png", 0, 0)

enemys = pygame.sprite.Group() 
enemy1 = Enemy(340, 100, 70, 70, r"images\angry_cat1.png", "down", 50, 240, 2)
enemys.add(enemy1)
enemy2 = Enemy(150, 310, 70, 70, r"images\angry_cat3.png", "right", 20, 170, 2)
enemys.add(enemy2)
enemy3 = Enemy(750, 170, 70, 70, r"images\angry_cat4.png", "left", 710, 880, 2)
enemys.add(enemy3)
enemy4 = Enemy(345, 380, 70, 70, r"images\angry_cat2.png", "up", 300, 430, 2)
enemys.add(enemy4)
enemy5 = Enemy(800, 320, 70, 70, r"images\angry_cat1.png", "left", 700, 870, 2)
enemys.add(enemy5)
enemy6 = Enemy(240, 525, 70, 70, r"images\angry_cat4.png", "right", 240, 470, 2)
enemys.add(enemy6)

finish = GameSprite(600, 400, 70, 70, r"images\cheese.png")

bullets = pygame.sprite.Group()


walls = pygame.sprite.Group()
wall1 = GameSprite(80, 0, 12, 90, r"images\bloks.png")
walls.add(wall1)
wall2 = GameSprite(660, 0, 12, 60, r"images\bloks.png")
walls.add(wall2)
wall3 = GameSprite(600, 50, 120, 12, r"images\bloks.png")
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
wall31 = GameSprite(0, 280, 60, 12, r"images\bloks.png")
walls.add(wall31)
wall32 = GameSprite(800, 280, 100, 12, r"images\bloks.png")
walls.add(wall32)
wall33 = GameSprite(170, 50, 100, 12, r"images\bloks.png")
walls.add(wall33)
wall34 = GameSprite(170, 520, 12, 80, r"images\bloks.png")
walls.add(wall34)
wall35 = GameSprite(100, 520, 120, 12, r"images\bloks.png")
walls.add(wall35)
wall36 = GameSprite(420, 440, 12, 70, r"images\bloks.png")
walls.add(wall36)
wall37 = GameSprite(420, 510, 100, 12, r"images\bloks.png")
walls.add(wall37)
wall38 = GameSprite(520, 510, 12, 90, r"images\bloks.png")
walls.add(wall38)
wall39 = GameSprite(630, 530, 100, 12, r"images\bloks.png")
walls.add(wall39)
wall40 = GameSprite(730, 510, 12, 100, r"images\bloks.png")
walls.add(wall40)





btn_start = Button(300, 300, 300, 100, ORANGE, DARK_ORANGE, "START", WHITE, 50, 10)
btn_exit = Button(300, 420, 300, 100, ORANGE, DARK_ORANGE, "EXIT", WHITE, 70, 10)
game_name = pygame.font.SysFont("Times New Roman", 70, 1).render("KING OF CHEESE", True, WHITE) 

level = 0
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
                if event.key == pygame.K_SPACE:
                    player.shoot()
                    music_shoot.play()
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.speed_x = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.speed_x = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.speed_y = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.speed_y = 0

        elif level == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if btn_start.rect.collidepoint(x, y):
                    level = 1
                    pygame.mixer.music.load(file_path(r"music\fon_music.mp3"))
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)

                elif btn_exit.rect.collidepoint(x, y):
                    game = False

            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if btn_start.rect.collidepoint(x, y):
                    btn_start.color = btn_start.color2

                elif btn_exit.rect.collidepoint(x, y):
                    btn_exit.color = btn_exit.color2

                else:
                    btn_start.color = btn_start.color1
                    btn_exit.color = btn_exit.color1
                
    

    if level == 1:
        window.blit(fon, (0, 0))
        walls.draw(window)
        player.show()
        player.update()
        enemys.draw(window)
        enemys.update()
        finish.show()
        bullets.draw(window)
        bullets.update()

        if pygame.sprite.collide_rect(player, finish):
            level = 10
            pygame.mixer.music.stop()
            pygame.mixer.music.load(file_path(r"music\victory_music.mp3"))
            pygame.mixer.music.play(-1)

        if pygame.sprite.spritecollide(player, enemys, False):
            level = 11
            pygame.mixer.music.stop()
            pygame.mixer.music.load(file_path(r"music\loser_music.wav"))
            pygame.mixer.music.play(-1)

        pygame.sprite.groupcollide(bullets, walls, True, False)
        pygame.sprite.groupcollide(bullets, enemys, True, True)
    elif level == 10:
        window.blit(image_win, (0, 0))

    elif level == 11:
        window.blit(image_lose, (0, 0))

    elif level == 0:
        window.fill(YELLOW)
        btn_start.show()
        btn_exit.show()
        window.blit(game_name, (170, 150))





    clock.tick(FPS)
    pygame.display.update()



