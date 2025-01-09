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
    def event(self):
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                exit()
    def update(self):
        self.player.move()
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