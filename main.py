import pygame as pg
from time import clock as cl
from logic import Game
from bacterium import BacteriumOne, BacteruimTwo, BacteruimThree, BacteruimFive, BacteruimFour, ImprovedBacterium

successes, failures = pg.init()
print("{0} successes and {1} failures".format(successes, failures))

join = cl()
new_mode = Game()
time = new_mode.time
score = new_mode.score
money = new_mode.money


baterials_icons = {
    1: BacteriumOne().body,
    2: BacteruimTwo().body,
    3: BacteruimThree().body,
    4: BacteruimFour().body,
    5: BacteruimFive().body,
    # 6: ImprovedBacterium().body
}

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
fon_renderer = pg.font.Font('./PTS76F.ttf', 20)
names = [
    fon_renderer.render("XP: {}, $: {}".format(BacteriumOne().XP, BacteriumOne().price), 1, (30, 50, 40)),
    fon_renderer.render("XP: {}, $: {}".format(BacteruimTwo().XP, BacteruimTwo().price), 1, (30, 50, 40)),
    fon_renderer.render("XP: {}, $: {}".format(BacteruimThree().XP, BacteruimThree().price), 1, (30, 50, 40)),
    fon_renderer.render("XP: {}, $: {}".format(BacteruimFour().XP, BacteruimFour().price), 1, (30, 50, 40)),
    fon_renderer.render("XP: {}, $: {}".format(BacteruimFive().XP, BacteruimFive().price), 1, (30, 50, 40)),
]

flaticons = {
    'time': pg.transform.scale(pg.image.load("./img/icon/hourglass.png"), (40, 40)),
    'money': pg.transform.scale(pg.image.load("./img/icon/coin.png"), (40, 40)),
    'score': pg.transform.scale(pg.image.load("./img/icon/scoreboard.png"), (50, 50)),
}

rendering = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
}


def generate(type, num):
    if type:
        rendering[num].append([baterials_icons[num], (type.x, type.y)])


def render(x, y, click):
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
        startx, starty = 775, 210
        for i in range(1, 6):
            screen.blit(pg.transform.scale(baterials_icons[i], (30, 30)), (startx, starty, 0, 0))
            screen.blit(names[i - 1], (startx + 40, starty))
            starty += 30
        if 765 <= x <= 960 and 210 <= y <= 240 and click:
            generate(new_mode.buy(BacteriumOne), 1)
        elif 765 <= x <= 960 and 240 <= y <= 270 and click:
            generate(new_mode.buy(BacteruimTwo), 2)
        elif 765 <= x <= 960 and 270 <= y <= 300 and click:
            generate(new_mode.buy(BacteruimThree), 3)
        elif 765 <= x <= 960 and 300 <= y <= 330 and click:
            generate(new_mode.buy(BacteruimFour), 4)
        elif 765 <= x <= 960 and 330 <= y <= 360 and click:
            generate(new_mode.buy(BacteruimFive), 5)
    for i in range(1, 6):
        for _ in rendering[i]:
            screen.blit(_[0], _[1])

    screen.blit(icon_settings, (10, 7))
    pg.display.update()
    clock.tick(FPS)

view = False
click = False

while running:
    money = new_mode.money
    time = int(cl() - join)
    new_mode.time = time
    score = new_mode.score
    text = [
        font_renderer.render(f"{money}", 1, (33, 46, 40)),
        font_renderer.render(f"{time}", 1, (33, 46, 40)),
        font_renderer.render(f"{score}", 1, (33, 46, 40))

    ]

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit(0)
        elif event.type == pg.MOUSEBUTTONUP:
            click = True

    mousex, mousey = pg.mouse.get_pos()
    mouse_tap = pg.mouse.get_pressed()
    if new_mode.time == 5:
        rendering = new_mode.wave(rendering)
        join = cl()
        new_mode.alive(rendering)
    if view and (765 <= mousex <= 960 and 150 <= mousey <= 465):
        coord = (0, 0, 195, 315)
    elif (930 <= mousex <= 960
            and 150 <= mousey <= 465):
            view = True
    else:
        coord = (175, 0, 20, 315)
        view = False
    if new_mode.start and not new_mode.finish:
        screen.blit(background, background_rect)
        texty = pg.font.Font('./PTS76F.ttf', 50)
        texty = texty.render("YOU LOSt", 1, (33, 46, 40))
        screen.blit(texty, (400, 400))
    else:
        render(mousex, mousey, click)
    click = False

