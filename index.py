import pygame
from interface import Interface
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))


screen = pygame.display.set_mode((960, 640), 0, 32)
clock = pygame.time.Clock()
interface = Interface()
main_color = (168, 255, 157)
background = pygame.Surface((960, 640))
rect = background.get_rect()
background.fill(main_color)
interface.footer(background)
interface.magazine(background)
pygame.draw.rect(background, (255, 100, 40), (800, 0, 120, 40))

flaticon = {
    "settings":  interface.icon(58, 58, "./img/icon/settings-gears.png")
}
FPS = 60
pygame.font.init()
score = 0
money = 100
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = (myfont.render(f'Score: {score}', False, (0, 0, 0)),
               myfont.render(f'$ {money}', False, (0, 0, 0)))


def index():
    Quit = False
    while not Quit:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.blit(background, rect)
        screen.blit(flaticon["settings"], (10, 582, 64, 64))
        screen.blit(textsurface[0], (805, 10))
        screen.blit(textsurface[1], (700, 600))
        pygame.display.update()


if __name__ == "__main__":
    index()
