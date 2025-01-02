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
        self.gravity = 2
        self.is_jumping = False
        self.map_width = map_width
        self.map_height = map_height