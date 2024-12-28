import pygame as pg
import pytmx

pg.init()

SCREEN_WIDTH=800
SCREEN_HEIGHT=600

class Game():
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption('платформер')

        self.tmx_map = pytmx.load_pygame('levels/map1.tmx')

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
        ...
    def draw(self):
        self.screen.fill('light blue')

        for layer in self.tmx_map:
            for x,y,gid in layer:
                tile = self.tmx_map.get_tile_image_by_gid(gid)

                if tile:
                    self.screen.blit(tile, (x*self.tmx_map.tilewidth, y*self.tmx_map.tileheight))

        pg.display.flip()

if __name__=="__main__":
    game1=Game() #создали объект класса Game()