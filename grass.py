from pico2d import load_image

import game_world


class Grass:
    def __init__(self, depth):
        self.depth = depth
        self.image = load_image('grass.png')

    def draw(self):
        if self.depth == 0:
            self.image.draw(400, 45)
        elif self.depth == 1:
            self.image.draw(400, 30)

    def update(self):
        pass
