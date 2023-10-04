from pico2d import *
import random


class Grass():
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class BigBall():
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = (random.randint(50, 750), 599)

    def draw(self):
        self.image.draw(self.x, self.y)


class SmallBall():
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = (random.randint(50, 750), 599)

    def draw(self):
        self.image.draw(self.x, self.y)


def reset_world():
    global running
    global grass
    global big_ball, small_ball

    running = True
    grass = Grass()
    big_ball = [BigBall() for i in range(1, random.randint(1, 20))]
    small_ball = [SmallBall() for i in range(1, 20 - len(big_ball))]


def handle_events():
    global running

    for event in get_events():
        if (event.type == SDL_QUIT):
            running = False
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            running = False


def update_world():
    pass


def render_world():
    clear_canvas()
    grass.draw()
    for i in range(len(big_ball)):
        big_ball[i].draw()
        print("BIG")
    for i in range(len(small_ball)):
        small_ball[i].draw()
        print("SMALL")
    update_canvas()


open_canvas()
reset_world()

while (running):
    handle_events()
    update_world()
    render_world()

    delay(10)
