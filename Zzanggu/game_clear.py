import game_framework
import game_stage3
from pico2d import *

image = None
clear_bgm=None


def enter():
    global image,clear_bgm
    image = load_image('resource\\clear.png')
    clear_bgm=load_music('resource\\clear_bgm.mp3')

    clear_bgm.set_volume(100)
    clear_bgm.repeat_play()

def exit():
    global image,clear_bgm
    del(image)
    del(clear_bgm)

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