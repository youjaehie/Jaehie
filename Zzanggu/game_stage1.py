import random
import json
from pico2d import *
import game_framework
import game_title
import stage2_screen
import stage3_screen
import game_fail
import time

from stage1_class import *

zzanggu = None
first_stage = None
background = None
enemy = None
friends = None
stone = None
item = None
item2 = None
hp = None
play_bgm=None

def enter():
    global zzanggu, background, first_stage, enemy, friends, stone, item, item2,play_bgm
    zzanggu = Zzanggu()
    background = BackGround()
    first_stage = First_stage()
    enemy = Enemy()
    friends = Friends()
    stone = Stone()
    item = Item()
    item2 = Item2()
    play_bgm=load_music('resource\\play_bgm.wav')

    play_bgm.set_volume(100)
    play_bgm.repeat_play()
    pass

def exit():
    global zzanggu, background, first_stage, enemy, friends, stone, item, item2,play_bgm
    del(zzanggu)
    del(background)
    del(first_stage)
    del(enemy)
    del(friends)
    del(stone)
    del(item)
    del(item2)
    del(play_bgm)
    pass


def pause():
    pass

def resume():
    pass

def handle_events():
    global zzanggu
    events = get_events()
    for event in events:
        if event.key == SDLK_1:
            pass
        if event.key == SDLK_2:
            game_framework.push_state(stage2_screen)
        if event.key == SDLK_3:
            game_framework.push_state(stage3_screen)
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and zzanggu.state == zzanggu.RUN:
            if event.key == SDLK_RIGHT:
                zzanggu.keycheckright = True
            elif event.key == SDLK_UP:
                zzanggu.state = 1
                zzanggu.jump_frame = 0
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                zzanggu.keycheckright = False


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def update():
     global zzanggu, background, first_stage, enemy, friends, stone, item, item2
     background.update()
     zzanggu.update()
     first_stage.update()
     enemy.update()
     friends.update()
     stone.update()
     item.update()
     item2.update()
     if collide(zzanggu, item):
         zzanggu.state = 2
         zzanggu.Shoot = zzanggu.x
         item.look = 0
     if zzanggu.Shoot <= enemy.ZzangaX:
         enemy.ZzangaX -= 1
     if collide(zzanggu, item2):
         item2.look2 = 0
         enemy.erase2 = 0
     if collide(zzanggu, stone):
         zzanggu.state = 3
         if stone.eat == 1:
             zzanggu.Hp -= 1
             zzanggu.hurt_bgm.play(1)
             play_bgm.play()
         if zzanggu.Hp <= 0:
             game_framework.push_state(game_fail)
         stone.eat=0
     if collide(zzanggu, enemy):
         enemy.erase=0
         game_framework.push_state(game_fail)
     if zzanggu.x >= (friends.x - 60):
         game_framework.push_state(stage2_screen)
     pass

def draw():
    global zzanggu, background, first_stage, enemy, friends, stone, item, item2
    clear_canvas()
    background.draw()
    zzanggu.draw()
    first_stage.draw()
    enemy.draw()
    friends.draw()
    stone.draw()
    item.draw()
    item2.draw()
#    zzanggu.draw_bb()
#    item.draw_bb()
#    item2.draw_bb()
#    stone.draw_bb()
#    enemy.draw_bb()
    delay(0.05)
    update_canvas()
    pass