import pygame as pg

class Moving_platforms():
    def __init__(self, tiles, images, move_range, speed):
        self.tiles = tiles
        self.move_range = move_range
        self.images = images
        self.speed = speed
        self.direction = 1  # 1 - вправо/вниз, -1 - влево/вверх
        self.moved_distance = 0.0
        self.fractional_movement = 0.0

    def update(self):
        self.fractional_movement += self.speed * self.direction
        move_step = int(self.fractional_movement)

        if move_step != 0:  # Двигаем только если накопился хотя бы 1 пиксель
            for tile in self.tiles:
                tile.x += move_step
            self.fractional_movement = 0

        self.moved_distance += abs(move_step)

        if self.moved_distance >= self.move_range:
            self.direction *= -1
            self.moved_distance = 0.0

    def draw(self, screen):
        for i in range(len(self.tiles)):
            screen.blit(self.images[i], (self.tiles[i].x, self.tiles[i].y))