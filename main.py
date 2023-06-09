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

fon = pygame.image.load(file_path(r"images\fon.png"))
fon = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT))


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

player = GameSprite(80, 400, 100, 100, r"images\mouse.png")
enemy1 = GameSprite(300, 100, 100, 100, r"images\angry_cat1.png")
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
        window.blit(fon, (0, 0))
        walls.draw(window)
        player.show()
        enemy1.show()
        finish.show()

    clock.tick(FPS)
    pygame.display.update()



