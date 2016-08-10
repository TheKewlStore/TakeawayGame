import pygame

clock = pygame.time.Clock()


class Ball(object):
    def __init__(self):
        self.image = pygame.image.load("./resources/ball.gif")
        self.rect = self.image.get_rect()

        self._speed = [500.0, 500.0]
        self._horizontal_momentum = 0.0
        self._vertical_momentum = 0.0

    @property
    def speed(self):
        return [self._speed[0] * self._horizontal_momentum, self._speed[1] * self._vertical_momentum]

    @speed.setter
    def speed(self, new_speed):
        self._speed = new_speed

    @property
    def momentum(self):
        return (self._horizontal_momentum, self._vertical_momentum)

    @momentum.setter
    def momentum(self, new_momentum):
        try:
            self._horizontal_momentum = new_momentum[0]
            self._vertical_momentum = new_momentum[1]
        except IndexError:
            raise ValueError("Momentum given did not include both horizontal and vertical components.")

    @property
    def center(self):
        width = self.rect.right - self.rect.left
        height = self.rect.top - self.rect.bottom
        horizontal_center = self.rect.left + (width / 2)
        vertical_center = self.rect.bottom + (height / 2)
        return (horizontal_center, vertical_center)

    def move(self, time):
        horizontal_offset = self.speed[0] * time
        vertical_offset = self.speed[1] * time

        self.rect = self.rect.move(horizontal_offset, vertical_offset)

    def collide(self, right, bottom):
        if self.rect.left < 0:
            self._speed[0] = -self._speed[0]
            self._horizontal_momentum -= 0.001
        elif self.rect.right > right:
            self._speed[0]  = -self._speed[0]
            self._horizontal_momentum -= 0.001

        if self.rect.top < 0:
            self._speed[1] = -self._speed[1]
            self._vertical_momentum -= 0.001
        elif self.rect.bottom > bottom:
            self._speed[1] = -self._speed[1]
            self._vertical_momentum -= 0.001

    def clamp(self, rect):
        self.rect = self.rect.clamp(rect)

    def blit(self, screen):
        return screen.blit(self.image, self.rect)

    def add_momentum(self, source_location, momentum_to_add=0.25):
        self._horizontal_momentum += 0.25
        self._vertical_momentum += 0.25


class TakeawayGame(object):
    def __init__(self):
        pygame.init()

        self.fps = 60
        self.width = 640
        self.height = 480
        self.size = (self.width, self.height)

        self.screen = pygame.display.set_mode(self.size)

        self.ball = Ball()

        self.black = (0, 0, 0)

    def run(self):
        while True:
            elapsed = clock.tick(60)
            seconds = elapsed/1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.ball.add_momentum(event.pos)
                    elif event.button == 3:
                        self.ball.add_momentum(event.pos)

            self.screen.fill(self.black)

            self.ball.move(seconds)
            self.ball.collide(self.width, self.height)
            self.ball.clamp(self.screen.get_rect())
            self.ball.blit(self.screen)

            pygame.display.flip()
