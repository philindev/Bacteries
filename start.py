import pygame as pg
# from nt import startfile

successes, failures = pg.init()
print("{0} successes and {1} failures".format(successes, failures))

screen = pg.display.set_mode((960, 640), 0, 32)
clock = pg.time.Clock()
running = True
background = pg.Surface((960, 640))
background_rect = background.get_rect()
background.fill((0, 0, 0))
FPS = 60

pg.font.init()
color = (255, 255, 255)
font_renderer = pg.font.Font('./PTS76F.ttf', 40)
label = font_renderer.render(
    "START",
    1,
    color)

pg.draw.rect(background, color, (410, 297, 5, 40))
check = False

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        elif event.type == pg.MOUSEBUTTONUP:
            check = True

    key = pg.key.get_pressed()
    mousex, mousey = pg.mouse.get_pos()
    mouse_buttons = pg.mouse.get_pressed()
    if (410 <= mousex <= 540
                and 295 <= mousey <= 335
                and mouse_buttons):
        color = (100, 100, 100)
        pg.draw.rect(background, color, (410, 297, 5, 40))
        pg.font.init()
        font_renderer = pg.font.Font('./PTS76F.ttf', 40)
        label = font_renderer.render(
            "START",
            1,
            color)

    if check:
        if (410 <= mousex <= 540
                and 295 <= mousey <= 335
                and mouse_buttons):
            running = False

    screen.blit(background, background_rect)
    screen.blit(label, (430, 290))
    check = False

    color = (255, 255, 255)
    pg.draw.rect(background, color, (410, 297, 5, 40))
    pg.font.init()
    font_renderer = pg.font.Font('./PTS76F.ttf', 40)
    label = font_renderer.render(
        "START",
        1,
        color)

    pg.display.update()
import main
