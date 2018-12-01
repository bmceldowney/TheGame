import random
class Ball(object):
    def __init__(self, image):
        self.speed = [random.randint(1, 5), random.randint(1, 5)]
        self.image = image
        self.rect = image.get_rect()

    def move(self, screen_width, screen_height):
        self.rect = self.rect.move(self.speed)

        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.speed[1] = -self.speed[1]
