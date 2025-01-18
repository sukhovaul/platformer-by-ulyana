import pygame as pg
import pytmx
from character import Player
from buttons import draw_button

pg.init()

SCREEN_WIDTH=800
SCREEN_HEIGHT=600

font_path = 'fonts/Dudka Bold.ttf'
font_main = pg.font.Font(font_path, 30)

new_game_rect = pg.Rect(250, 200, 300, 100)
continue_game_rect = pg.Rect(250, 350, 300, 100)
light_brown = (191,157,123)

class Game():
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption('платформер')

        self.current_menu = 'main_menu'

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
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.current_menu == 'main_menu':
                    if new_game_rect.collidepoint(event.pos):
                        self.current_menu = 'game_menu'

        keys = pg.key.get_pressed()
        self.player.move(keys)

        # Определяем номер тайла, на котором находится игрок
        tile_gid = self.get_current_tile_gid(self.tmx_map)
        if tile_gid == 75:
            print("Игрок на воде!")
        elif tile_gid in [1, 2, 3]:
            print("Игрок на платформе!")
        elif tile_gid == 74:
            self.player.is_jumping = False
            self.player.x = 0
            self.player.y = 0
        else:
            print("Игрок в воздухе или на неизвестном тайле!", tile_gid)
    def update(self):
        self.player.jump()
    def draw(self):
        self.screen.fill('light blue')

        if self.current_menu == 'main_menu':
            self.screen.fill('black')

            draw_button(self.screen, new_game_rect, 'начать новую игру', light_brown, 'brown', 0, font_main)
            draw_button(self.screen, continue_game_rect, 'продолжить игру', light_brown, 'brown', 0, font_main)

        elif self.current_menu == 'game_menu':
            for layer in self.tmx_map:
                for x,y,gid in layer:
                    tile = self.tmx_map.get_tile_image_by_gid(gid)

                    if tile:
                        self.screen.blit(tile, (x*self.tmx_map.tilewidth, y*self.tmx_map.tileheight))

            self.screen.blit(self.player.image, self.player.rect)

        pg.display.flip()

if __name__=="__main__":
    game1=Game() #создали объект класса Game()