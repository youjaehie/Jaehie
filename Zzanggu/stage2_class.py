import random
import json
from pico2d import *
from game_stage1 import  *

class BackGround:
    image = None ;
    def __init__(self):
        self.BackScroll = 0
        self.x = 0
        if self.image == None:
            self.image = load_image('resource\\background2.png')
    def draw(self):
        self.image.draw(400 - self.BackScroll,300)
        self.image.draw(1200 - self.BackScroll,300)
        if self.BackScroll == 800 :
            self.BackScroll = 0
    def update(self):
        self.BackScroll+=10
        self.BackScroll%=800

class Second_stage:
    image = None ;
    def __init__(self):
        if self.image == None:
            self.image = load_image('resource\\second_stage.png')
        self.TileScroll = 0
    def draw(self):
        self.image.draw(400-self.TileScroll,30)
        self.image.draw(1200-self.TileScroll,30)
        if self.TileScroll == 390 :
            self.TileScroll = 0
    def update(self):
        self.TileScroll += 15
        self.TileScroll%=1000

class House:
    image=None
    def __init__(self):
        if House.image == None:
            self.image=load_image('resource\\house.png')
        self.x= 1150
        self.y= 120
        self.frame=0
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        self.frame=(self.frame+1)
        self.x-=1
        if self.x <750:
            self.x=750

class Enemy:
    Osu_RIGHT_RUN = 4
    RIGHT_DIR ,LEFT_DIR = 1,-1

    Osuimage = None
    Whitedogimage = None

    OsuX = -70
    OsuY = 105
    Osustate = Osu_RIGHT_RUN
    Osuframe = 0

    timer = 0
    def __init__(self):
        self.erase = 1
        self.erase2 = 1
        self.hide = 1
        self.frame=0
        if Enemy.Osuimage ==None:
            Enemy.Osuimage = load_image('resource\\Osu.png')
        if Enemy.Whitedogimage == None:
            Enemy.Whitedogimage = load_image('resource\\Whitedog.png')
        self.dir = self.RIGHT_DIR

    def handle_right_run(self):
        self.OsuX += (self.dir*1)/1.5
        if (self.OsuX > 1200):
            self.OsuX = 0

    handle_state ={
        Osu_RIGHT_RUN : handle_right_run,
    }

    def draw(self):
        if self.erase == 1:
            self.Osuimage.clip_draw(self.frame * 210, 0, 210, 210, self.OsuX, self.OsuY)
        if self.erase2 == 0:
            self.Whitedogimage.draw(self.OsuX+80, self.OsuY-10)

    def update(self):
        self.timer += 1
        self.hide += 1
        self.frame += 1
        if self.frame == 5:
            self.frame = 0
        if self.timer == 100:
            self.Osuframe = (self.Osuframe + 1) % 6
            self.timer = 0
        self.handle_state[self.Osustate](self)
        if self.hide > 80:
            self.erase2 = 1
            self.hide = 0
            self.OsuX += (self.dir * 1) / 1.5

    def get_bb(self):
        return self.OsuX - 70, self.OsuY - 44, self.OsuX + 70, self.OsuY + 44

#    def draw_bb(self):
#        draw_rectangle(*self.get_bb())

class Zzanggu:
    global i
    RUN, JUMP, Ullaulla, Hurt = 0, 1, 2, 3
    hurt_bgm=None

    def handle_run(self):
        self.run_frame = (self.run_frame + 1)
        if self.keycheckright == True:
            self.x += 1.5

    def handle_jump(self):
        self.y -= (self.jump_frame - 3) * 20
        self.jump_frame += 1
        # delay(0.03)
        if self.jump_frame == 7:
            self.state = self.RUN
            #self.run_frame = 0

    def handle_ullaulla(self):
        self.jump_frame += 1
        # delay(0.03)
        if self.jump_frame >= 7:
            if self.jump_frame > 15:
                self.state = self.RUN
            self.y = 100
            pass
        else:
            self.y -= (self.jump_frame - 3) * 20
            #self.run_frame = 0

    def handle_hurt(self):
        if self.run_frame > 1:
            self.state = self.RUN

    handle_state = {
        RUN: handle_run,
        JUMP: handle_jump,
        Ullaulla : handle_ullaulla,
        Hurt : handle_hurt
    }

    def update(self):
        self.handle_state[self.state](self)  # if가 없어짐 -> 처리속도,수정이 빠름
        self.frame += 1
        if self.frame == 5:
            self.frame = 0
        if self.state == 2:
            self.Shoot -= 40
        else :
            self.Shoot = self.x

    def __init__(self):
        self.x, self.y = 70, 100
        self.Hp = 5
        self.Shoot = 5
        self.frame=0
        self.run_frame, self.jump_frame, self.ullaulla_frame = (0, 0, 0)
        self.run = load_image('resource\\Zzanggu.png')
        self.jump = load_image('resource\\Zzanggu_jump.png')
        self.ullaulla = load_image('resource\\Zzanggu_ullaulla.png')
        self.hurt = load_image('resource\\Zzanggu_hurt.png')
        self.bump = load_image('resource\\Zzanggu_bump.png')
        self.hp = load_image('resource\\Zzanggu_hp.png')
        self.bump = load_image('resource\\Zzanggu_bump.png')
        self.shoot = load_image('resource\\Zzanggu_shoot.png')
        self.keycheckright, self.keycheckup = (False, False)
        self.state = self.RUN
        if Zzanggu.hurt_bgm==None:
            Zzanggu.hurt_bgm = load_music('resource\\hurt_bgm.mp3')
            Zzanggu.hurt_bgm.set_volume(80)
            Zzanggu.hurt_bgm.repeat_play()


    def draw(self):
        if self.state == 0:
            self.run.clip_draw(self.frame*87,0,87,87,self.x,self.y)
        elif self.state == 1:
            self.jump.draw(self.x, self.y)
        elif self.state == 2:
            self.ullaulla.draw(self.x, self.y)
            self.shoot.draw(self.Shoot, self.y)
        elif self.state == 3:
            self.hurt.draw(self.x, self.y+10)

        for i in range(0,self.Hp):
            self.hp.draw(730-(i*45),480)
        for i in range(self.Hp,5):
            self.bump.draw(730-(i*45),480)

    def get_bb(self):
        return self.x - 33, self.y - 40, self.x + 10, self.y + 40

        #     def draw_bb(self):
        #         draw_rectangle(*self.get_bb())

class Stone:
    image = None ;
    def __init__(self):
        self.x, self.y = 1000, 72
        self.eat = 1
        if self.image == None:
            self.image = load_image('resource\\stone.png')
        self.x = 0

    def draw(self):
        if self.eat == 1:
            self.image.draw(self.x,72)

    def update(self):
        self.x -= 15
        self.x %= 1100
        if self.x >= 850:
            self.eat = 1

    def get_bb(self):
        return self.x - 10, self.y - 14, self.x + 10, self.y + 14

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Stone2:
    image = None ;
    def __init__(self):
        self.x, self.y = 1200,75
        self.eat2=1
        if self.image == None:
            self.image = load_image('resource\\stone2.png')
        self.x= 0

    def draw(self):
        if self.eat2==1:
            self.image.draw(self.x,75)

    def update(self):
        self.x -= 10
        self.x%= 1000
        if self.x >= 850:
            self.eat2 = 1

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Item:
    image = None ;

    def __init__(self):
        self.x, self.y = 1200, 220
        self.look = 1
        if self.image == None:
            self.image = load_image('resource\\item.png')
        self.x = 0
    def draw(self):
        if self.look == 1:
            self.image.draw(self.x,220)

    def update(self):
        self.x -= 15
        self.x %= 1000
        if self.x >= 850:
            self.look = 1

    def get_bb(self):
        return self.x - 20, self.y - 24, self.x + 20, self.y + 24

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Item2:
    image = None ;
    def __init__(self):
        self.x2, self.y2 = 1400, 200
        self.look2 = 1

        if self.image == None:
            self.image = load_image('resource\\item2.png')
        self.x2 = 0
    def draw(self):
        if self.look2 == 1:
            self.image.draw(self.x2,200)

    def update(self):
        self.x2 -= 10
        self.x2 %=1200
        if self.x2 >= 850:
            self.look2 = 1

    def get_bb(self):
        return self.x2 - 20, self.y2 - 19, self.x2 + 20, self.y2 + 19

        #     def draw_bb(self):
        #        draw_rectangle(*self.get_bb())

