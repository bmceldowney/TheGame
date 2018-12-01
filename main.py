import sys, pygame
from ball import Ball
pygame.init()

size = width, height = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)

image = pygame.image.load("assets/intro_ball.gif")
balls = [
    Ball(image),
    Ball(image),
    Ball(image),
    Ball(image),
    Ball(image),
    Ball(image),
    Ball(image),
    Ball(image),
    Ball(image)
    ]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    for ball in balls:
        ball.move(width, height)
        screen.blit(ball.image, ball.rect)

    pygame.display.flip()
