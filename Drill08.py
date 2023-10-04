from pico2d import *


def load_resources():
    pass


def reset_world():
    global running

    running = True

    open_canvas()


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
    pass


while (running):
    handle_events()
    update_world()
    render_world()
