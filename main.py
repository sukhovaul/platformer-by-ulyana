import pygame as pg
import pytmx
from character import Player

pg.init()

SCREEN_WIDTH=800
SCREEN_HEIGHT=600

class Game():
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption('платформер')

        self.tmx_map = pytmx.load_pygame('levels/map1.tmx')
        self.player = Player(SCREEN_WIDTH,SCREEN_HEIGHT)

        self.run()
    def run(self):
        while True:
            self.event()
            self.update()
            self.draw()

    def get_current_tile_gid(self, tmx_map):
        # Получаем координаты игрока
        player_x = self.player.rect.centerx  # Центр игрока по X
        player_y = self.player.rect.bottom  # Нижняя часть игрока по Y (стоит на тайле)

        # Вычисляем номер тайла (в строках и столбцах)
        tile_x = player_x // tmx_map.tilewidth
        tile_y = player_y // tmx_map.tileheight

        # Проверяем каждый слой карты, чтобы найти gid
        for layer in tmx_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):  # Только тайловые слои
                gid = layer.data[tile_x][tile_y]
                return gid  # Возвращаем номер тайла

        return None  # Если тайл не найден
    def event(self):
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                exit()

        keys = pg.key.get_pressed()
        self.player.move(keys)

        # Определяем номер тайла, на котором находится игрок
        tile_gid = self.get_current_tile_gid(self.tmx_map)
        if tile_gid == 75:
            print("Игрок на воде!")
        elif tile_gid in [1, 2, 3]:
            print("Игрок на платформе!")
        else:
            print("Игрок в воздухе или на неизвестном тайле!", tile_gid)
    def update(self):
        self.player.jump()
    def draw(self):
        self.screen.fill('light blue')

        for layer in self.tmx_map:
            for x,y,gid in layer:
                tile = self.tmx_map.get_tile_image_by_gid(gid)

                if tile:
                    self.screen.blit(tile, (x*self.tmx_map.tilewidth, y*self.tmx_map.tileheight))

        self.screen.blit(self.player.image, self.player.rect)

        pg.display.flip()

if __name__=="__main__":
    game1=Game() #создали объект класса Game()