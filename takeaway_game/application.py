import pygame


class TakeawayGame(object):
    def __init__(self):
        pygame.init()

        self.width = 640
        self.height = 480
        self.size = (self.width, self.height)

        self.screen = pygame.display.set_mode(self.size)

        self.ball = pygame.image.load("./resources/ball.gif")
        self.ball_rect = self.ball.get_rect()

        self.black = (0, 0, 0)
        self._speed = [5, 5]
        self._momentum = 1

    @property
    def speed(self):
        return [self._speed[0] * self._momentum, self._speed[1] * self._momentum]

    @speed.setter
    def speed(self, new_speed):
        self._speed = new_speed

    def collision(self):
        self._momentum *= 0.99

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True

            self.ball_rect = self.ball_rect.move(self.speed)

            if self.ball_rect.left < 0:
                self._speed[0] = 5
                self.collision()
            elif self.ball_rect.right > self.width:
                self._speed[0]  = -5
                self.collision()

            if self.ball_rect.top < 0:
                self._speed[1] = 5
                self.collision()
            elif self.ball_rect.bottom > self.height:
                self._speed[1] =-5
                self.collision()

            self.screen.fill(self.black)
            self.screen.blit(self.ball, self.ball_rect)

            pygame.display.flip()

            # time.sleep(0.01)
