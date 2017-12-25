import game_framework
import game_stage1
from pico2d import *

image = None
screen_bgm=None


def enter():
    global image, screen_bgm
    image = load_image('resource\\stage1.png')
    screen_bgm=load_music('resource\\screen_bgm.wav')

    screen_bgm.set_volume(100)
    screen_bgm.repeat_play()

def exit():
    global image,screen_bgm
    del(image)
    del(screen_bgm)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(game_stage1)

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update():
    pass


def pause():
    pass


def resume():
    pass