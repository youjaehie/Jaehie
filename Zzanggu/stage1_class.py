import random
import json
from pico2d import *
from game_stage1 import  *

class Pause:
    image=None
    def __init__(self):
        if Pause.image == None:
            Pause.image = load_image('resource\\pause.png')
        self.pressed=False
    def draw(self):
        if self.pressed == True:
            self.image.clip_draw_to_origin(0,0,1366,350,300,300,1000,300)

class BackGround:
    image = None ;
    def __init__(self):
        self.BackScroll = 0
        self.x = 0
        if self.image == None:
            self.image = load_image('resource\\background.png')
    def draw(self):
        self.image.draw(400 - self.BackScroll,300)
        self.image.draw(1200 - self.BackScroll,300)
        if self.BackScroll == 800 :
            self.BackScroll = 0
    def update(self):
        self.BackScroll+=10
        self.BackScroll%=800

class First_stage:
    image = None ;
    def __init__(self):
        if self.image == None:
            self.image = load_image('resource\\first_stage.png')
        self.TileScroll = 0
    def draw(self):
        self.image.draw(400-self.TileScroll,30)
        self.image.draw(1200-self.TileScroll,30)
        if self.TileScroll == 390 :
            self.TileScroll = 0
    def update(self):
        self.TileScroll += 15
        self.TileScroll%=1000

class Friends:
    image=None
    def __init__(self):
        if Friends.image == None:
            self.image=load_image('resource\\friends.png')
        self.x= 1050
        self.y= 140
        self.frame=0
    def draw(self):
        self.image.draw(self.x, self.y)
        #self.image.clip_draw_to_origin(55*self.frame,0,55,43,self.x,self.y,80,60)
    def update(self):
        self.frame=(self.frame+1)
        self.x-=1
        if self.x <650:
            self.x=650

class Enemy:
    Zzanga_RIGHT_RUN = 4
    RIGHT_DIR = 1

    Zzangaimage = None
    Whitedogimage = None

    ZzangaX = -20
    ZzangaY = 95
    Zzangastate = Zzanga_RIGHT_RUN
    Zzangaframe = 0

    timer = 0
    def __init__(self):
        self.erase = 1
        self.erase2 = 1
        self.hide = 1
        if Enemy.Zzangaimage ==None:
            Enemy.Zzangaimage = load_image('resource\\Zzanga.png')
        if Enemy.Whitedogimage == None:
            Enemy.Whitedogimage = load_image('resource\\Whitedog.png')

        self.dir = self.RIGHT_DIR

    def handle_right_run(self):
        self.ZzangaX += (self.dir*1)/2
        if (self.ZzangaX > 1200):
            self.ZzangaX = 0

    handle_state ={
        Zzanga_RIGHT_RUN : handle_right_run,
    }

    def draw(self):
        if self.erase == 1:
            self.Zzangaimage.draw(self.ZzangaX, self.ZzangaY)
        if self.erase2 == 0:
            self.Whitedogimage.draw(self.ZzangaX+80, self.ZzangaY-10)


    def update(self):
        self.timer += 1
        self.hide += 1
        if self.timer == 100:
            self.Zzangaframe = (self.Zzangaframe + 1) % 6
            self.timer = 0
        self.handle_state[self.Zzangastate](self)
        if self.hide > 80:
            self.erase2 = 1
            self.hide = 0
            self.ZzangaX += (self.dir * 1) / 2

    def get_bb(self):
        return self.ZzangaX - 40, self.ZzangaY - 44, self.ZzangaX + 40, self.ZzangaY + 44

#    def draw_bb(self):
#        draw_rectangle(*self.get_bb())


class Zzanggu:
    global i
    RUN, JUMP, Ullaulla, Hurt= 0, 1, 2, 3
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
        if self.state == 2:
            self.Shoot -= 40
        else :
            self.Shoot = self.x

    def __init__(self):
        self.x, self.y = 70, 100
        self.Hp = 5
        self.Shoot = 5
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
            self.run.draw(self.x, self.y)
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

#    def draw_bb(self):
#        draw_rectangle(*self.get_bb())

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
        self.x %= 1200
        if self.x >= 850:
            self.eat = 1

    def get_bb(self):
        return self.x - 10, self.y - 14, self.x + 10, self.y + 14

#    def draw_bb(self):
#        draw_rectangle(*self.get_bb())


class Item:
    Itemimage = None;

    def __init__(self):
        self.x, self.y = 1200, 220
        self.look = 1
        if self.Itemimage == None:
            self.Itemimage = load_image('resource\\item.png')
        self.x = 0
    def draw(self):
        if self.look == 1:
            self.Itemimage.draw(self.x,220)

    def update(self):
        self.x -= 15
        self.x %= 1000
        if self.x >= 850:
            self.look = 1

    def get_bb(self):
        return self.x - 20, self.y - 24, self.x + 20, self.y + 24

#    def draw_bb(self):
#        draw_rectangle(*self.get_bb())

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

#    def draw_bb(self):
#        draw_rectangle(*self.get_bb())
