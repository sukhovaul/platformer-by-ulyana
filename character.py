import pygame as pg

class Player(pg.sprite.Sprite): #класс player наследует класс sprite
    def __init__(self, map_width, map_height, image_path = None):
        super(Player, self).__init__()

        if image_path:
            self.image = pg.image.load(image_path).convert_alpha()
            self.image = pg.transform.scale(self.image, (50,50))
        else:
            self.image = pg.Surface((50,50)) #создаем прямоугольник размерами 50 на 50
            self.image.fill("red")

        self.rect = self.image.get_rect() #получаем рпрямоугольник из изображения
        self.rect.center = (200,100) #устанавливаем начальное положение игрока

        self.velocity_x=0
        self.velocity_y=0
        self.gravity = 0.5
        self.is_jumping = False
        self.map_width = map_width
        self.map_height = map_height

    def move(self, keys):

        if keys[pg.K_LEFT]:
            self.velocity_x=-1
        elif keys[pg.K_RIGHT]:
            self.velocity_x=1
        elif keys[pg.K_UP]:
            self.velocity_y=-1
        elif keys[pg.K_DOWN]:
            self.velocity_y=1
        else:
            self.velocity_x=0
            self.velocity_y=0

        new_x=self.rect.x+self.velocity_x
        if 0<=new_x<=self.map_width - self.rect.width:
            self.rect.x=new_x

        new_y=self.rect.y+self.velocity_y
        if 0<=new_y<=self.map_height - self.rect.height:
            self.rect.y=new_y

    def jump(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_SPACE]:
            self.is_jumping=True

        if not self.is_jumping:
            new_y = self.rect.y+self.gravity
            if 0 <= new_y <= self.map_height - self.rect.height:
                self.rect.y = new_y
        if self.is_jumping:
            new_y = self.rect.y - 2
            if 0 <= new_y <= self.map_height - self.rect.height:
                self.rect.y = new_y
            self.is_jumping=False