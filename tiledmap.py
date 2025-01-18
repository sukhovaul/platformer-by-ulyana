import pytmx

class TiledMap:
    def __init__(self, tmx_file):
        """
        tmx_file: путь к файлу .tmx, например: "levels/map1.tmx".
        """
        # 1) Загружаем tmx-файл через pytmx
        self.tmx_data = pytmx.load_pygame(tmx_file, pixelalpha=True)

        # 2) Размер карты в тайлах (ширина и высота в "клетках")
        self.map_width = self.tmx_data.width
        self.map_height = self.tmx_data.height

        # 3) Размер одного тайла в пикселях
        self.tile_width = self.tmx_data.tilewidth
        self.tile_height = self.tmx_data.tileheight

        # 4) Задаём набор "твёрдых" GID (см. ниже объяснение)
        #    Здесь просто примерные значения, нужно подогнать под свои реальные GID.
        #    Посмотри, какие GID в твоём CSV несут роль стен/земли/блоков, которые
        #    НЕпроходимы.
        self.SOLID_GIDS = {1, 2, 3, 4, 5, 6, 8, 9, 10, 15, 16, 17, 32, 33, 34, 36, 37, 50, 66, 67, 73, 74, 75}

    def is_solid(self, px, py):
        """
        Проверяем, является ли точка (px, py) (в пикселях) "твёрдым" тайлом.
        Возвращаем True, если там препятствие; False, если пусто.
        """
        # 1) Вычисляем, в какой тайл (по X и Y) попадает эта пиксельная координата
        tile_x = px // self.tile_width
        tile_y = py // self.tile_height

        # 2) Проверяем, не вышли ли мы за границы карты
        if (tile_x < 0 or tile_x >= self.map_width or
                tile_y < 0 or tile_y >= self.map_height):
            # Если за пределами карты, считаем стеной (чтобы не выходить)
            return True

        # 3) У тебя один слой, значит просто берём этот слой
        #    Иногда в pytmx можно сделать: layer = self.tmx_data.layers[0]
        #    (если мы знаем точно, что нужный слой — первый).
        #    Но можно и пробежаться по visible_layers и найти тот, у которого name="Слой тайлов 1".
        layer = self.tmx_data.layers[0]  # предполагаем, что это тот самый единственный слой

        # 4) Берём GID тайла в координатах [tile_y][tile_x]
        gid = layer.data[tile_y][tile_x]

        # 5) Смотрим, входит ли этот gid в список "SOLID_GIDS"
        if gid in self.SOLID_GIDS:
            return True
        else:
            return False