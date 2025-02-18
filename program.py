import io
import pygame

from yandex_map_library import *


class MapApp:
    def __init__(self, size):
        self.screen = pygame.display.set_mode(size)
        bytes_img = get_static_map(ll='123,45', z=5)
        img = pygame.image.load(io.BytesIO(bytes_img))
        self.screen.blit(img, (0, 0))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

            pygame.display.flip()


if __name__ == '__main__':
    app = MapApp((600, 450))
    app.run()