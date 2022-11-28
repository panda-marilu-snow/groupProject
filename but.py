import pygame,os

os.environ['SDL_VIDEODRIVER']='dummy'


pygame.init()

#MAKE A SCREEN FOR THE PLAYER TO SEE
screen = pygame.display.set_mode((800, 400))


screen.fill((255,255,255))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((255,255,255))
    pygame.display.update()