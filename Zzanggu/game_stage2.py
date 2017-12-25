import random
import json
from pico2d import *
import game_framework
import game_title
import stage3_screen
import game_fail

from stage2_class import *

zzanggu = None
second_stage = None
background = None
enemy = None
house = None
stone = None
stone2=None
item = None
item2 = None
play_bgm=None

def enter():
    global zzanggu, background, second_stage, enemy, house, stone, item, item2,play_bgm,stone2
    zzanggu = Zzanggu()
    background = BackGround()
    second_stage= Second_stage()
    enemy = Enemy()
    house = House()
    stone = Stone()
    stone2 = Stone2()
    item = Item()
    item2 = Item2()
    play_bgm=load_music('resource\\play_bgm.wav')

    play_bgm.set_volume(100)
    play_bgm.repeat_play()
    pass

def exit():
    global zzanggu, background, second_stage, enemy, house, stone, item, item2,play_bgm,stone2
    del(zzanggu)
    del(background)
    del(second_stage)
    del(enemy)
    del(house)
    del(stone)
    del(item)
    del(item2)
    del(play_bgm)
    del(stone2)
    pass


def pause():
    pass

def resume():
    pass

def handle_events():
    global zzanggu
    events = get_events()
    for event in events:
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
    global zzanggu, background, second_stage, enemy, house, stone, item, item2, stone2
    background.update()
    zzanggu.update()
    second_stage.update()
    enemy.update()
    house.update()
    stone.update()
    item.update()
    item2.update()
    stone2.update()
    if collide(zzanggu, item):
        zzanggu.state = 2
        zzanggu.Shoot = zzanggu.x
        item.look = 0
    if zzanggu.Shoot <= enemy.OsuX:
        enemy.OsuX -= 1
    if collide(zzanggu, item2):
        item2.look2 = 0
        enemy.erase2 = 0
    if collide(zzanggu, stone):
        zzanggu.state = 3
        if stone.eat == 1:
            zzanggu.Hp -= 1
            zzanggu.hurt_bgm.play()
        if zzanggu.Hp <= 0:
            game_framework.push_state(game_fail)
        stone.eat=0
    if collide(zzanggu, stone2):
        zzanggu.state = 3
        if stone2.eat2 == 1:
            zzanggu.Hp -= 1
            zzanggu.hurt_bgm.play()
        if zzanggu.Hp <= 0:
            game_framework.push_state(game_fail)
        stone.eat=0
    if collide(zzanggu, enemy):
        enemy.erase=0
        game_framework.push_state(game_fail)
    if zzanggu.x >= (house.x - 60):
        game_framework.push_state(stage3_screen)
    pass

def draw():
    global zzanggu, background, second_stage, enemy, house, stone, item, item2,stone2
    clear_canvas()
    background.draw()
    zzanggu.draw()
    second_stage.draw()
    enemy.draw()
    house.draw()
    stone.draw()
    item.draw()
    item2.draw()
    stone2.draw()
    #     zzanggu.draw_bb()
    #     item.draw_bb()
    #     item2.draw_bb()
    #     stone.draw_bb()
    #    enemy.draw_bb()
    #stone2.draw_bb()
    delay(0.05)
    update_canvas()
    pass