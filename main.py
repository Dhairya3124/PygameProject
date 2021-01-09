import pygame
import os
pygame.init()
WIDTH,HEIGHT = 900,500
WHITE = (255,255,255)
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40
FPS = 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Shooting Game")

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.scale(
    RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))




def draw_window():
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP_IMAGE,(300,100))
    pygame.display.update()
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    
    pygame.quit()

if __name__ == "__main__":
    main()
