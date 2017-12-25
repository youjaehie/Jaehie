import game_framework
import game_stage1
import game_stage2
import game_stage3
from pico2d import *

image = None
fail_bgm=None


def enter():
    global image,fail_bgm
    image = load_image('resource\\fail.png')
    fail_bgm=load_music('resource\\fail_bgm.wav')

    fail_bgm.set_volume(100)
    fail_bgm.repeat_play()

def exit():
    global image,fail_bgm
    del(image)
    del(fail_bgm)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

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