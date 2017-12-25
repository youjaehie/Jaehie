import game_framework
import stage1_screen
from pico2d import *

name = "TitleState"

image = None
start_bgm=None

def enter():
    global image,start_bgm
    image = load_image('resource\\title.png')
    start_bgm=load_music('resource\\start_bgm.mp3')

    start_bgm.set_volume(100)
    start_bgm.repeat_play()

def exit():
    global image, start_bgm
    del(image)
    del(start_bgm)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(stage1_screen)

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