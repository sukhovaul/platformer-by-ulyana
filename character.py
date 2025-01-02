import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pg.image.load()