import pygame as pg
import pytmx #импортируем библиотеку для работы с картами tmx
from character import Player
from buttons import draw_button

pg.init()

SCREEN_WIDTH=800
SCREEN_HEIGHT=600

font_path = 'fonts/Dudka Bold.ttf'
font_main = pg.font.Font(font_path, 30)

#прямоугольники кнопки
new_game_rect = pg.Rect(250, 200, 300, 100)
continue_game_rect = pg.Rect(250, 350, 300, 100)

#rgb цвета
light_brown = (191,157,123) #тип данных tuple - кортеж

class Game():
    def __init__(self): #конструктор класса
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption('платформер')

        self.current_menu = 'main_menu'
        self.objects = []

        self.tmx_map = pytmx.load_pygame('levels/map1.tmx') #загружаем tmx карту
        self.player = Player(SCREEN_WIDTH,SCREEN_HEIGHT) #создаем объект класса player



        for layer in self.tmx_map: #проходим по всем слоям карты
            if isinstance(layer, pytmx.TiledObjectGroup):  # проверка является ли слой слоем объектов

                #проверяем условие для слоя с блоками коллизии - ПЕРЕДВИЖЕНИЯ
                if layer.name == "hit block":

                    #проверяем каждый объект слоя
                    for obj in layer:
                        new_object = pg.Rect(obj.x, obj.y, obj.width, obj.height) #создаем объект rect для каждого объекта
                        self.objects.append(new_object) #добавляем объект в список с объектами

        self.run() #запускаем основной цикл программы
    def run(self): #метод для главных игровых процессов
        while True:
            self.event() #обработка событий и нажатий кнопок
            self.update() #
            self.draw()

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

    def update(self):
        self.player.jump()

        for obj in self.objects:
            if pg.Rect(obj.x, obj.y, obj.width, obj.height).colliderect(self.player.rect) == True:
                print("YOU HIT THE RED BLOCK!!")
                self.player.is_jumping = False
                self.player.gravity = 0
            else:
                self.player.gravity = 0.5
    def draw(self):
        self.screen.fill('light blue')

        if self.current_menu == 'main_menu':
            self.screen.fill('black')

            #создаем и отображаем кнопки на экране
            draw_button(self.screen, new_game_rect, 'начать новую игру', light_brown, 'brown', 0, font_main)
            draw_button(self.screen, continue_game_rect, 'продолжить игру', light_brown, 'brown', 0, font_main)

        elif self.current_menu == 'game_menu':
            #
            for layer in self.tmx_map:
                if isinstance(layer, pytmx.TiledTileLayer): #проверка является ли слой слоем тайлов
                    for x,y,gid in layer:
                        tile = self.tmx_map.get_tile_image_by_gid(gid)

                        if tile:
                            self.screen.blit(tile, (x*self.tmx_map.tilewidth, y*self.tmx_map.tileheight))


                if isinstance(layer, pytmx.TiledObjectGroup): #проверка является ли слой слоем объектов
                    if layer.name == "hit block":
                        for obj in self.objects:
                            if pg.Rect(obj.x, obj.y, obj.width, obj.height).colliderect(self.player.rect) == True:
                                print("YOU HIT THE RED BLOCK!!")
                                self.player.is_jumping = False
                                self.player.gravity = 0
                    if layer.name == 'dead block':
                        for obj in layer:
                            if pg.Rect(obj.x, obj.y, obj.width, obj.height).colliderect(self.player.rect) == True:
                                print('dead block')
                                self.player.rect.x = 70
                                self.player.rect.y = 300

            self.screen.blit(self.player.image, self.player.rect)

        pg.display.flip()

if __name__=="__main__":
    game1=Game() #создали объект класса Game()