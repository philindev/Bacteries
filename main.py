import pygame as pg
from logic import Game

successes, failures = pg.init()
print("{0} successes and {1} failures".format(successes, failures))

new_mode = Game()
time = "00:00"
score = new_mode.score
money = new_mode.money

screen = pg.display.set_mode((960, 640), 0, 32)
clock = pg.time.Clock()
FPS = 60
colors = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
}
menu_color = (64, 128, 91)
running = True
background = pg.Surface((960, 640))
background_rect = background.get_rect()
header = pg.Surface((960, 50))
header_rect = header.get_rect()
icon_settings = pg.image.load("./img/icon/settings-gears.png")
icon_settings = pg.transform.scale(icon_settings, (40, 40))
navbar = pg.Surface((195, 315))
navbar_rect = (765, 150, 20, 315)
coord = (175, 0, 20, 315)
pg.font.init()
font_renderer = pg.font.Font('./PTS76F.ttf', 30)
label = font_renderer.render(
    "Shop:",
    1,
    (33, 46, 40))
text = [
    font_renderer.render(f"{money}", 1, (33, 46, 40)),
    font_renderer.render(f"{time}", 1, (33, 46, 40)),
    font_renderer.render(f"{score}", 1, (33, 46, 40))

]
flaticons = {
    'time': pg.transform.scale(pg.image.load("./img/icon/hourglass.png"), (40, 40)),
    'money': pg.transform.scale(pg.image.load("./img/icon/coin.png"), (40, 40)),
    'score': pg.transform.scale(pg.image.load("./img/icon/scoreboard.png"), (50, 50)),
}


def render():

    background.fill((163, 204, 181))
    screen.blit(background, background_rect)
    header.fill(colors["BLACK"])
    header.set_alpha(100)
    screen.blit(header, header_rect)
    navbar.fill((163, 204, 181))
    navbar.set_alpha(100)
    pg.draw.rect(navbar, menu_color, coord)
    screen.blit(navbar, navbar_rect)
    screen.blit(flaticons["money"], (300, 7))
    screen.blit(flaticons["time"], (800, 7))
    screen.blit(text[0], (340, 7))
    screen.blit(text[1], (840, 7))
    if coord == (0, 0, 195, 315):
        screen.blit(label, (790, 160))
        screen.blit(flaticons["score"], (770, 400))
        screen.blit(text[2], (823, 408))
    screen.blit(icon_settings, (10, 7))
    pg.display.update()
    clock.tick(FPS)


while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit(0)

    mousex, mousey = pg.mouse.get_pos()
    mouse_tap = pg.mouse.get_pressed()
    if (930 <= mousex <= 960
            and 150 <= mousey <= 465):
            coord = (0, 0, 195, 315)

    render()
    coord = (175, 0, 20, 315)
