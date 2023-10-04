from pico2d import *
import random


class Grass():
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class BigBall():
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = (random.randint(50, 750), 599)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= 1


class SmallBall():
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = (random.randint(50, 750), 599)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= 1


def reset_world():
    global running
    global grass
    global big_ball, small_ball
    global balls

    running = True

    grass = Grass()
    big_ball = [BigBall() for i in range(1, random.randint(1, 19))]
    small_ball = [SmallBall() for i in range(1, 20 - len(big_ball))]

    balls = []
    balls = balls + big_ball + small_ball


def handle_events():
    global running

    for event in get_events():
        if (event.type == SDL_QUIT):
            running = False
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            running = False


def update_world():
    for o in balls:
        o.update()


def render_world():
    clear_canvas()
    grass.draw()
    for o in balls:
        o.draw()
    update_canvas()


open_canvas()
reset_world()

while (running):
    handle_events()
    update_world()
    render_world()
