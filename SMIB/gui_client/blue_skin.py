# -*- coding:utf-8 -*-
'''
Created on 16.09.2021

@author: dedal
'''

import sys
import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet import clock
import json
import log
from pymemcache.client.base import PooledClient as mem_Client
import os
import gettext
import time
import pyglet.gl

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))


def DebugOptions():
    return BASE_DIR == '/home/dedal/Colibri/SMIB/2_1'


DEBUG = DebugOptions()


def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2


def json_deserializer(key, value, flags):
    if flags == 1:
        return value.decode()
    if flags == 2:
        return json.loads(value)
    print("Unknown serialization format")


# if DEBUG is True:
#     CLIENT = mem_Client(('192.168.1.11', 11211), serializer=json_serializer, deserializer=json_deserializer)
#     LOGO_NAME = 'colibri-logo.png'
# else:
CLIENT = mem_Client(('127.0.0.1', 11211), serializer=json_serializer, deserializer=json_deserializer)

locale_folder = BASE_DIR + '/locale'
gettext.install('messages', locale_folder, names=['ugettext'], codeset='utf-8')
# gettext.install('messages', locale_folder, unicode=True, names=['ugettext'], codeset='utf-8')
if DEBUG is False:
    LANG = None
    while LANG == None:
        LANG = CLIENT.get('USE_LANGUAGE')
        time.sleep(2)
    lang = gettext.translation('messages', 'locale', fallback=True, languages=[LANG])
else:
    lang = gettext.translation('messages', 'locale', fallback=True, languages=['bg'])
lang.install()

SIZE = CLIENT.get('DISPLAY_SIZE')
# if DEBUG is False:
#     LOGO_NAME = None
#     while LOGO_NAME == None:
#         LOGO_NAME = CLIENT.get('LOGO_NAME')
#     # if LOGO_NAME == 'BREAK':
#     #     sys.exit()
# else:
LOGO_NAME = 'colibri-logo.png'

pyglet.options['debug_gl'] = True
pyglet.options['double_buffer'] = True
pyglet.options['xsync'] = True
pyglet.options['vsync'] = False
# pyglet.options['audio'] = ('openal', 'silent')
platform = pyglet.canvas.get_display()
display = platform.get_screens()
screen = platform.get_default_screen()
screen_width = screen.width
screen_height = screen.height
if DEBUG is False:
    window = pyglet.window.Window(fullscreen=True)
    window.set_mouse_visible(False)
    if SIZE==5:
        font_name = 18
        font_button = 18
        font_text = 18
        count_text = 16
        won_text = 18
    else:
        font_name = 14
        font_button = 14
        font_text = 14
        count_text = 12
        won_text = 14
else:
    window = pyglet.window.Window(screen_width, screen_height)
    font_name = 30
    font_button = 30
    font_text = 22
    count_text = 20
    won_text = 50

fps_display = pyglet.clock.Clock()
# batch = pyglet.graphics.Batch()

background = pyglet.graphics.Group(0)
logo = pyglet.graphics.Group(1)
menu = pyglet.graphics.Group(2)
button = pyglet.graphics.Group(3)
text = pyglet.graphics.Group(4)
bonus_group = pyglet.graphics.Group(2)

USE_ANIME = None
ANIME_NIM = None
MY_RANGE = None
if DEBUG is False:
    while USE_ANIME == None:
        USE_ANIME = CLIENT.get('use_anime')
    while ANIME_NIM == None:
        ANIME_NIM = CLIENT.get('anime_num')
    while MY_RANGE == None:
        MY_RANGE = CLIENT.get('anime_range')

else:
    USE_ANIME = True
    ANIME_NIM = '8'
    MY_RANGE = [0, 2]
if DEBUG is False:
    VIDEO = []
    for i in range(MY_RANGE[0], MY_RANGE[1]):
        VIDEO.append(pyglet.resource.image('video/%s/image%s.%s' % (ANIME_NIM, str(i), 'jpg')))
    if ANIME_NIM == '1':
        for i in VIDEO:
            i.width = int(screen_width)
            if SIZE == 5:
                i.height = int(screen_height + screen_height * 0.45)
            else:
                i.height = int(screen_height + screen_height * 0.35)
        ANIME = pyglet.image.Animation.from_image_sequence(VIDEO, duration=0.1, loop=True)
        ANIME_SPRITE = pyglet.sprite.Sprite(ANIME, group=text)
        ANIME_SPRITE.position = (0, -50, 0)
    elif ANIME_NIM == '2' or ANIME_NIM == '8':
        for i in VIDEO:
            i.width = int(screen_width)
            i.height = int(screen_height)
        ANIME = pyglet.image.Animation.from_image_sequence(VIDEO, duration=0.1, loop=True)
        ANIME_SPRITE = pyglet.sprite.Sprite(ANIME, group=text)
        # ANIME_SPRITE.position = (7, 0)
    elif ANIME_NIM == '3':
        for i in VIDEO:
            i.width = int(screen_width)
            i.height = int(screen_height)
        ANIME = pyglet.image.Animation.from_image_sequence(VIDEO, duration=0.1, loop=True)
        ANIME_SPRITE = pyglet.sprite.Sprite(ANIME, group=text)
    elif ANIME_NIM == '4':
        for i in VIDEO:
            i.width = int(screen_width)
            i.height = int(screen_height)
        ANIME = pyglet.image.Animation.from_image_sequence(VIDEO, duration=0.1, loop=True)
        ANIME_SPRITE = pyglet.sprite.Sprite(ANIME, group=text)
    elif ANIME_NIM == '5' or ANIME_NIM == '6' or ANIME_NIM == '7':
        for i in VIDEO:
            i.width = int(screen_width)
            i.height = int(screen_height)
        ANIME = pyglet.image.Animation.from_image_sequence(VIDEO, duration=0.1, loop=True)
        ANIME_SPRITE = pyglet.sprite.Sprite(ANIME, group=text)
    else:
        ANIME_SPRITE = None
        USE_ANIME = False
else:
    VIDEO = []
    for i in range(MY_RANGE[0], MY_RANGE[1]):
        VIDEO.append(pyglet.resource.image('video/%s/image%s.%s' % (ANIME_NIM, str(i), 'jpg')))
    for i in VIDEO:
        i.width = int(screen_width)
        i.height = int(screen_height + screen_height * 0.35)
    ANIME = pyglet.image.Animation.from_image_sequence(VIDEO, duration=0.1, loop=True)
    ANIME_SPRITE = pyglet.sprite.Sprite(ANIME, group=text)
    ANIME_SPRITE.position = (0, -50, 0)

USE_SAS_AFT = CLIENT.get('use_sas_aft')
SHOW_OUT_BUTTON = CLIENT.get('SHOW_OUT_BUTTON')
MAKE_IN_OUT = CLIENT.get('MAKE_IN_OUT')
MONY_BACK_SHOW = CLIENT.get('SHOW_MONYBACK_PAY')

class BackGround():
    def __init__(self):
        global background
        global logo
        global button
        global USE_ANIME
        self.batch = pyglet.graphics.Batch()
        self.background_group = background
        self.logo_group = logo
        self.button_group = button
        self.background = pyglet.resource.image('img/abstract-blue-backgrounds-6.jpg')
        self.background.width = int(screen_width)
        self.background.height = int(screen_height)
        # if not USE_ANIME:
        self.logo = pyglet.resource.image('img/colibri-logo.png')
        self.logo.width = int(screen_width // 2)
        self.logo.height = int(screen_height // 2)
        self.background_sprite = pyglet.sprite.Sprite(self.background, batch=self.batch, group=self.background_group)
        # if not USE_ANIME:
        self.logo_sprite = pyglet.sprite.Sprite(self.logo, batch=self.batch, group=self.button_group)
        self.logo_sprite.position = (screen_width * 0.68, screen_height - (screen_height * 0.95), 0)

    def new_batch(self):
        self.batch = pyglet.graphics.Batch()

    # def change_background(self):


class SetMenu():
    def __init__(self):
        global menu
        global button
        global text
        global SHOW_OUT_BUTTON
        global MONY_BACK_SHOW

        self.batch = pyglet.graphics.Batch()
        self.menu_group = menu
        self.button_group = button
        self.text_group = text

        self.menu = pyglet.resource.image('img/Screen1_prize-field-empty.png')
        self.menu.width = int(screen_width * 0.2)
        self.menu.height = int(screen_height*0.96)

        self.menu_text = pyglet.resource.image('img/Screen1_prize-field-empty_vertical.png')
        self.menu_text.width = int(screen_width * 0.8)
        self.menu_text.height = int(screen_height+(screen_height*0.02))

        self.button_bonus = pyglet.resource.image('img/imgbin_arrow-statistical-graphics-png.png')
        self.button_bonus.width = int(screen_width * 0.15)
        self.button_bonus.height = int(screen_height * 0.25)

        if SHOW_OUT_BUTTON:
            self.out_bonus = pyglet.resource.image('img/in_out.png')
            self.out_bonus.width = int(screen_width * 0.20)
            self.out_bonus.height = int(screen_height * 0.28)
        if MONY_BACK_SHOW:
            self.monyback_bonus = pyglet.resource.image('img/cache_back.png')
            self.monyback_bonus.width = int(screen_width * 0.16)
            self.monyback_bonus.height = int(screen_height * 0.22)
        # self.button_tikcet = pyglet.resource.image('img/NicePng_raffle-ticket-png_2461085.png')
        # self.button_tikcet.width = int(screen_width * 0.135)
        # self.button_tikcet.height = int(screen_height * 0.15)

        self.button_home = pyglet.resource.image('img/home-button-icon-29.jpg')
        self.button_home.width = int(screen_width * 0.14)
        self.button_home.height = int(screen_height * 0.22)

        self.menu_line = pyglet.resource.image('img/pngkit_lighting-png_21468.png')
        self.menu_line.width = int(screen_width * 0.8)
        self.menu_line.height = int(screen_height * 0.65)

        self.menu_sprite = pyglet.sprite.Sprite(self.menu, batch=self.batch, group=self.menu_group)
        self.menu_sprite.position = (0, screen_height - (screen_height * 0.97), 0)
        self.menu_text_sprite = pyglet.sprite.Sprite(self.menu_text, batch=self.batch, group=self.menu_group)
        self.menu_text_sprite.position = (screen_width * 0.20, screen_height - (screen_height), 0)
        self.menu_line_sprite = pyglet.sprite.Sprite(self.menu_line, batch=self.batch, group=self.text_group)
        self.menu_line_sprite.position = (screen_width * 0.205, screen_height - (screen_height * 0.7), 0)

        self.button_home_sprite = pyglet.sprite.Sprite(self.button_home, batch=self.batch, group=self.button_group)
        self.button_home_sprite.position = (screen_width * 0.030, screen_height * 0.73, 0)

        self.button_bonus_sprite = pyglet.sprite.Sprite(self.button_bonus, batch=self.batch, group=self.button_group)
        self.button_bonus_sprite.position = (screen_width * 0.025, screen_height * 0.48, 0)

        if SHOW_OUT_BUTTON:
            self.out_sprite = pyglet.sprite.Sprite(self.out_bonus, batch=self.batch, group=self.button_group)
            self.out_sprite.position = (screen_width * 0.001, screen_height * 0.02, 0)
        if MONY_BACK_SHOW:
            self.monyback_bonus_sprite = pyglet.sprite.Sprite(self.monyback_bonus, batch=self.batch, group=self.button_group)
            self.monyback_bonus_sprite.position = (screen_width * 0.032, screen_height * 0.28, 0)
        # self.button_rko = pyglet.resource.image('img/12png_chart-of-accounts-accounting-service-expense.png')
        # self.button_rko.width = int(screen_width * 0.12)
        # self.button_rko.height = int(screen_height * 0.20)



    # def set_menu(self):


    def new_batch(self):
        self.batch = pyglet.graphics.Batch()

    # def set_button(self):


        # self.button_ticket_sprite = pyglet.sprite.Sprite(self.button_tikcet, batch=self.batch, group=self.button_group)
        # self.button_ticket_sprite.position = (screen_width * 0.035, screen_height * 0.32)
        #
        # self.button_rko_sprite = pyglet.sprite.Sprite(self.button_rko, batch=self.batch, group=self.button_group)
        # self.button_rko_sprite.position = (screen_width * 0.035, screen_height * 0.08)


class SetNavi():
    def __init__(self):
        global menu
        global button
        global text
        self.button_group = button
        self.batch = pyglet.graphics.Batch()

        self.buton_1 = pyglet.resource.image('img/imgbin_arrow-statistical-graphics-png.png')
        self.buton_1.width = int(screen_width * 0.23)
        self.buton_1.height = int(screen_height * 0.40)

        self.button_2= pyglet.resource.image('img/home-button-icon-29.jpg')
        self.button_2.width = int(screen_width * 0.16)
        self.button_2.height = int(screen_height * 0.25)

        self.in_nra = pyglet.resource.image('img/security-low.png')
        self.in_nra.width = int(screen_width * 0.50)
        self.in_nra.height = int(screen_height * 0.85)
        self.in_nra_val = False

        # self.logo = pyglet.resource.image('img/colibri-logo.png')
        # self.logo.width = int(screen_width // 2)
        # self.logo.height = int(screen_height // 2)

        # self.button_3 = pyglet.resource.image('img/NicePng_raffle-ticket-png_2461085.png')
        # self.button_3.width = int(screen_width * 0.15)
        # self.button_3.height = int(screen_height * 0.17)
        #
        # self.button_4 = pyglet.resource.image('img/12png_chart-of-accounts-accounting-service-expense.png')
        # self.button_4.width = int(screen_width * 0.16)
        # self.button_4.height = int(screen_height * 0.28)


    def new_batch(self):
        self.batch = pyglet.graphics.Batch()

    def set_navi(self, count=1):
        self.new_batch()
        # self.logo_sprite = pyglet.sprite.Sprite(self.logo, batch=self.batch, group=self.button_group)
        # self.logo_sprite.position = (screen_width * 0.68, screen_height - (screen_height * 0.90))
        if self.in_nra_val is True:
            if count == 1:
                self.buton_sprite = pyglet.sprite.Sprite(self.button_2, batch=self.batch, group=self.button_group)
                self.buton_sprite.position = (screen_width * 0.82, screen_height * 0.68, 0)
            elif count == 2:
                self.buton_sprite = pyglet.sprite.Sprite(self.buton_1, batch=self.batch, group=self.button_group)
                self.buton_sprite.position = (screen_width * 0.78, screen_height * 0.63, 0)
            self.in_nra_sprite = pyglet.sprite.Sprite(self.in_nra, batch=self.batch, group=self.button_group)
            self.in_nra_sprite.position = (screen_width * 0.30, screen_height * 0.08, 0)
        else:
            if count == 1:
                self.buton_sprite = pyglet.sprite.Sprite(self.button_2, batch=self.batch, group=self.button_group)
                self.buton_sprite.position = (screen_width * 0.82, screen_height * 0.68, 0)
            elif count == 2:
                self.buton_sprite = pyglet.sprite.Sprite(self.buton_1, batch=self.batch, group=self.button_group)
                self.buton_sprite.position = (screen_width * 0.78, screen_height * 0.63, 0)
        # elif count == 3:
        #     self.buton_sprite = pyglet.sprite.Sprite(self.button_3, batch=self.batch, group=self.button_group)
        #     self.buton_sprite.position = (screen_width * 0.84, screen_height * 0.75)
        # elif count == 4:
        #     self.buton_sprite = pyglet.sprite.Sprite(self.button_4, batch=self.batch, group=self.button_group)
        #     self.buton_sprite.position = (screen_width * 0.82, screen_height * 0.68)

class SetText():
    def __init__(self):
        global text
        self.text_group = text
        self.batch = pyglet.graphics.Batch()
        self.set_menu_name = [_(u'Текущо!'), _(u'Статистика!')]


    def add_name(self):
        self.name = pyglet.text.Label(
            u'',
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=font_name,
            x=screen_width * 0.25,
            y=screen_height * 0.68,
            group=self.text_group,
            batch=self.batch,
            # color=(153, 153, 0, 255)
        )


    def clean_all_text(self):
        self.name.text = u''
        self.menu_name.text = u''
        self.row_1.text = u''
        self.row_2.text = u''
        self.row_3.text = u''
        self.row_4.text = u''
        self.row_5.text = u''
        self.row_6.text = u''
        self.row_7.text = u''

    def add_menu_text(self):
        self.menu_name = pyglet.text.Label(
            u'',
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=font_button,
            x=screen_width * 0.25,
            y=screen_height * 0.90,
            group=self.text_group,
            batch=self.batch,
            # color=(153, 153, 0, 255)
        )

        self.row_1 = pyglet.text.Label(
            u'',
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=font_text,
            x=screen_width * 0.25,
            y=screen_height * 0.52,
            group=self.text_group,
            batch=self.batch,
            # color=(153, 153, 0, 255)
        )

        self.row_2 = pyglet.text.Label(
            u'',
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=font_text,
            x=screen_width * 0.25,
            y=screen_height * 0.44,
            group=self.text_group,
            batch=self.batch,
            # color=(153, 153, 0, 255)
        )
        self.row_3 = pyglet.text.Label(
            u'',
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=font_text,
            x=screen_width * 0.25,
            y=screen_height * 0.36,
            group=self.text_group,
            batch=self.batch,
            # color=(153, 153, 0, 255)
        )
        self.row_4 = pyglet.text.Label(
            u'',
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=font_text,
            x=screen_width * 0.25,
            y=screen_height * 0.26,
            group=self.text_group,
            batch=self.batch,
            # color=(153, 153, 0, 255)
        )

        self.row_5 = pyglet.text.Label(
            u'',
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=font_text,
            x=screen_width * 0.25,
            y=screen_height * 0.18,
            group=self.text_group,
            batch=self.batch,
            # color=(153, 153, 0, 255)
        )

        self.row_6 = pyglet.text.Label(
            u'',
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=font_text,
            x=screen_width * 0.25,
            y=screen_height * 0.10,
            group=self.text_group,
            batch=self.batch,
            # color=(153, 153, 0, 255)
        )

        self.row_7 = pyglet.text.Label(
            u'',
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=font_text,
            x=screen_width * 0.25,
            y=screen_height * 0.04,
            group=self.text_group,
            batch=self.batch,
            # color=(153, 153, 0, 255)
        )

    def new_batch(self):
        self.batch = pyglet.graphics.Batch()


class Bonus():
    def __init__(self):
        #         global batch
        global button
        global text

        self.batch = pyglet.graphics.Batch()
        self.box_group = button
        self.box = pyglet.resource.image('img/treasure-chest-36270.png')
        self.box.width = int(screen_width * 0.40)
        self.box.height = int(screen_height * 0.55)
        self.bonus_init = []
        self.won = None
        self.box_1_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
        self.box_1_sprite.position = (screen_width * 0.00, screen_height * 0.50, 0)

        self.box_2_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
        self.box_2_sprite.position = (screen_width * 0.325, screen_height * 0.50, 0)

        self.box_3_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
        self.box_3_sprite.position = (screen_width * 0.65, screen_height * 0.50, 0)
        #
        self.box_6_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
        self.box_6_sprite.position = (screen_width * 0.15, screen_height * 0.05, 0)

        self.box_7_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
        self.box_7_sprite.position = (screen_width * 0.48, screen_height * 0.03, 0)

    def new_batch(self):
        self.batch = pyglet.graphics.Batch()

    # def add_box(self):



#         self.box_8_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
#         self.box_8_sprite.position = (screen_width*0.70, screen_height*0.30)
#
#         self.box_9_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
#         self.box_9_sprite.position = (screen_width*0.05, screen_height*0.01)
#
#         self.box_10_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
#         self.box_10_sprite.position = (screen_width*0.37, screen_height*0.01)
#
#         self.box_11_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
#         self.box_11_sprite.position = (screen_width*0.70, screen_height*0.01)

class BonusWonNoButton():
    def __init__(self):
        global count_text
        global button
        global text
        global menu
        global font_name
        global USE_SAS_AFT

        # self.batch = batch
        self.text_group = text

        self.batch = pyglet.graphics.Batch()
        self.box_group = menu
        self.counter_group = button
        self.box = pyglet.resource.image('img/winner.png')
        self.box.width = int(screen_width * 0.40)
        self.box.height = int(screen_height * 0.88)

        # self.button_yes = pyglet.resource.image('img/yes.png')
        # self.button_yes.width = int(screen_width * 0.25)
        # self.button_yes.height = int(screen_height * 0.30)
        #
        # self.button_no = pyglet.resource.image('img/no.png')
        # self.button_no.width = int(screen_width * 0.25)
        # self.button_no.height = int(screen_height * 0.30)

        self.field_for_count = pyglet.resource.image('img/Screen1_prize-field-empty_vertical.png')
        self.field_for_count.width = int(screen_width * 0.185)
        self.field_for_count.height = int(screen_height * 0.09)

        self.count_field_sprite = pyglet.sprite.Sprite(self.field_for_count, batch=self.batch, group=self.counter_group)
        self.count_field_sprite.position = (screen_width * 0.41, screen_height * 0.562, 0)

        self.box_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
        self.box_sprite.position = (screen_width * 0.30, screen_height * 0.11, 0)

        # self.button_sprite = pyglet.sprite.Sprite(self.button_yes, batch=self.batch, group=self.box_group)
        # self.button_sprite.position = (screen_width * 0.75, screen_height * 0.76)
        #
        # self.button_sprite_2 = pyglet.sprite.Sprite(self.button_no, batch=self.batch, group=self.box_group)
        # self.button_sprite_2.position = (screen_width * 0.005, screen_height * 0.75)
        if USE_SAS_AFT is False:
            self.press_start = pyglet.text.Label(
            u'Press START bitton',
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=won_text,
            x=screen_width * 0.15,
            y=screen_height * 0.06,
            group=self.text_group,
            batch=self.batch, anchor_x='center', anchor_y='center')

        self.won_text = pyglet.text.Label(
            u'00.00',
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=won_text,
            x=screen_width * 0.5,
            y=screen_height * 0.61,
            group=self.text_group,
            batch=self.batch, anchor_x='center', anchor_y='center'
            #                                       color=(153,153,0,255)
        )

    # def new_batch(self):
    #     self.batch = pyglet.graphics.Batch()
    #
    def mony(self, mony):
        self.won_text.text = "{:.2f}".format(mony)


class BonusWon():
    def __init__(self):
        global count_text
        global button
        global text
        global menu
        global font_name

        # self.batch = batch
        self.text_group = text

        self.batch = pyglet.graphics.Batch()
        self.box_group = menu
        self.counter_group = button
        self.box = pyglet.resource.image('img/winner.png')
        self.box.width = int(screen_width * 0.40)
        self.box.height = int(screen_height * 0.88)

        self.button_yes = pyglet.resource.image('img/yes.png')
        self.button_yes.width = int(screen_width * 0.25)
        self.button_yes.height = int(screen_height * 0.32)

        self.button_no = pyglet.resource.image('img/no.png')
        self.button_no.width = int(screen_width * 0.25)
        self.button_no.height = int(screen_height * 0.32)

        self.field_for_count = pyglet.resource.image('img/Screen1_prize-field-empty_vertical.png')
        self.field_for_count.width = int(screen_width * 0.185)
        self.field_for_count.height = int(screen_height*0.09)

        self.count_field_sprite = pyglet.sprite.Sprite(self.field_for_count, batch=self.batch, group=self.counter_group)
        self.count_field_sprite.position = (screen_width*0.41, screen_height*0.562, 0)

        self.box_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
        self.box_sprite.position = (screen_width * 0.30, screen_height * 0.11, 0)

        self.button_sprite = pyglet.sprite.Sprite(self.button_yes, batch=self.batch, group=self.box_group)
        self.button_sprite.position = (screen_width * 0.75, screen_height * 0.72, 0)

        self.button_sprite_2 = pyglet.sprite.Sprite(self.button_no, batch=self.batch, group=self.box_group)
        self.button_sprite_2.position = (screen_width * 0.005, screen_height * 0.72, 0)

        self.won_text = pyglet.text.Label(
            u'00.00',
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=won_text,
            x=screen_width * 0.5,
            y=screen_height * 0.61,
            group=self.text_group,
            batch=self.batch,anchor_x='center', anchor_y='center'
            #                                       color=(153,153,0,255)
        )

    def mony(self, mony):
        self.won_text.text = "{:.2f}".format(mony)

class RedPoint():
    def __init__(self):
        global text
        self.redpoint_group = text
        self.batch = pyglet.graphics.Batch()

        self.point_red = pyglet.resource.image('img/Gnome-Emblem-Important-32.png')
        self.point_red.width = int(screen_width * 0.05)
        self.point_red.height = int(screen_height * 0.07)
        self.red_point_sprite = pyglet.sprite.Sprite(self.point_red, batch=self.batch, group=self.redpoint_group)
        self.red_point_sprite.position = (screen_width * 0.90, screen_height * 0.1, 0)

    # def show_red_point(self):


class SetBonusWarning():
    def __init__(self):
        # global batch
        global bonus_group
        self.batch = pyglet.graphics.Batch()
        self.button_group = text
        # self.bonus_image = pyglet.resource.image('img/pngegg.png')
        # self.bonus_image.width = int(screen_width * 0.55)
        # self.bonus_image.height = int(screen_height * 0.45)
        self.bonus_image = pyglet.resource.image('img/pngwing.com.png')
        self.bonus_image.width = int(screen_width * 0.35)
        self.bonus_image.height = int(screen_height * 0.22)
        self.bonus_image_sprite = pyglet.sprite.Sprite(self.bonus_image, batch=self.batch, group=self.button_group)
        # self.bonus_image_sprite.position = (screen_width * 0.40, screen_height * 0.02)
        self.bonus_image_sprite.position = (screen_width * 0.65, screen_height * 0.12, 0)

    def new_batch(self):
        self.batch = pyglet.graphics.Batch()

    # def show_bonus_warning(self):


BACKGROUND = BackGround()
# BACKGROUND.change_background()
MENU = SetMenu()
# MENU.set_menu()
# MENU.set_button()
NAV = SetNavi()
NAV.set_navi(1)
TEXT = SetText()
TEXT.add_name()
TEXT.add_menu_text()
RED_POINT = RedPoint()
# RED_POINT.show_red_point()
SET_BONUS_WARNING = SetBonusWarning()
# SET_BONUS_WARNING.show_bonus_warning()
BONUS = Bonus()
BONUSWON = BonusWon()
BUNUSWONNOBUTTON = BonusWonNoButton()

PLAYER = False
ON_KEY_IS_PRESS = 1
BONUS.bonus_init = []
BONUS.won = None

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ENTER:
        CLIENT.set('HALT', True)
    if symbol == key.ESCAPE and DEBUG is True:
        sys.exit()
    if symbol == key.ESCAPE and DEBUG is False:
        return True

HIDE_NAME = True

@window.event
def on_mouse_press(x, y, button, modifiers):
    global ON_KEY_IS_PRESS
    global PLAYER
    global BONUS
    global HIDE_NAME
    if PLAYER is not False and PLAYER != None:
        if x > screen_width * 0.18 and x < screen_width * 0.9 and y > screen_height * 0.60 and y < screen_height * 0.78 and BONUS.bonus_init == [] and BONUS.won == None:
            if HIDE_NAME is True:
                HIDE_NAME = False
            else:
                HIDE_NAME = True
        if BONUS.bonus_init == [] and BONUS.won == None:
            if x > screen_width * 0.038 and x < screen_width * 0.162 and y < screen_height * 0.96 and y > screen_height * 0.75:
                ON_KEY_IS_PRESS = 1
            elif x > screen_width * 0.038 and x < screen_width * 0.162 and y < screen_height * 0.72 and y > screen_height * 0.48:
                ON_KEY_IS_PRESS = 2
            elif x > screen_width * 0.038 and x < screen_width * 0.160 and y < screen_height * 0.45 and y > screen_height * 0.28 and MONY_BACK_SHOW is True:
                CLIENT.set('MONY_BACK_PAY', True)
            elif x > screen_width * 0.038 and x < screen_width * 0.160 and y < screen_height * 0.25 and y > screen_height * 0.10 and SHOW_OUT_BUTTON is True:
                CLIENT.set('MAKE_IN_OUT', True)
                # print 1
            #print y, screen_height * 0.49, screen_height * 0.36
        elif BONUS.bonus_init != [] and BONUS.won == None:
            if x > screen_width * 0.045 and x < screen_width * 0.35 and y > screen_height * 0.58 and y < screen_height * 0.92:
                BONUS.won = BONUS.bonus_init[0]
                BONUS.bonus_init = []
                CLIENT.set('PLAYER_BONUS_INIT', BONUS.bonus_init)
                CLIENT.set('PLAYER_WON_BONUS', BONUS.won)
            elif x > screen_width * 0.36 and x < screen_width * 0.67 and y > screen_height * 0.58 and y < screen_height * 0.92:
                BONUS.won = BONUS.bonus_init[1]
                BONUS.bonus_init = []
                CLIENT.set('PLAYER_BONUS_INIT', BONUS.bonus_init)
                CLIENT.set('PLAYER_WON_BONUS', BONUS.won)
            elif x > screen_width * 0.70 and x < screen_width and y > screen_height * 0.58 and y < screen_height * 0.92:
                BONUS.won = BONUS.bonus_init[2]
                BONUS.bonus_init = []
                CLIENT.set('PLAYER_BONUS_INIT', BONUS.bonus_init)
                CLIENT.set('PLAYER_WON_BONUS', BONUS.won)
            elif x > screen_width * 0.20 and x < screen_width * 0.48 and y < screen_height * 0.53 and y > screen_height * 0.15:
                BONUS.won = BONUS.bonus_init[3]
                BONUS.bonus_init = []
                CLIENT.set('PLAYER_BONUS_INIT', BONUS.bonus_init)
                CLIENT.set('PLAYER_WON_BONUS', BONUS.won)
            elif x > screen_width * 0.52 and x < screen_width * 0.92 and y < screen_height * 0.53 and y > screen_height * 0.15:
                BONUS.won = BONUS.bonus_init[4]
                BONUS.bonus_init = []
                CLIENT.set('PLAYER_BONUS_INIT', BONUS.bonus_init)
                CLIENT.set('PLAYER_WON_BONUS', BONUS.won)
        elif BONUS.bonus_init == [] and BONUS.won != None:
            if y < screen_height and y > screen_height * 0.80 and x > screen_width * 0.02 and x < screen_width * 0.35:
                CLIENT.set('PLAYER_GET_BONUS', (False, BONUS.won))
                CLIENT.set('PLAYER_WON_BONUS', None)
                BONUS.won = None
            elif y < screen_height and y > screen_height * 0.80 and x > screen_width * 0.65 and x < screen_width * 0.98:
                CLIENT.set('PLAYER_GET_BONUS', (True, BONUS.won))
                CLIENT.set('PLAYER_WON_BONUS', None)
                BONUS.won = None


@window.event
def on_draw():
    global PLAYER
    global BACKGROUND
    global USE_ANIME
    global ANIME_SPRITE
    global MENU
    global NAV
    global ON_KEY_IS_PRESS
    global TEXT
    global BONUS
    global RED_POINT
    global HIDE_NAME
    time.sleep(0.05)
    window.clear()
    try:
        PLAYER = CLIENT.get('PLAYER')
        NAV.in_nra_val = CLIENT.get('PLAYER_IN_NRA')
        # log.stdout_logger.debug('PLAYER: %s', PLAYER)
        BONUS.bonus_init = CLIENT.get('PLAYER_BONUS_INIT')
        if BONUS.bonus_init == None:
            BONUS.bonus_init = []
        client_get_bonus = CLIENT.get('PLAYER_GET_BONUS')

        if client_get_bonus == None:
            client_get_bonus = []
        if not PLAYER:
            BONUS.bonus_init = []
            BONUS.won = None
            ON_KEY_IS_PRESS = 1
            HIDE_NAME = True
            client_get_bonus = []
            if USE_ANIME is True and ANIME_SPRITE:
                ANIME_SPRITE.draw()
            else:
                # BACKGROUND.new_batch()
                # BACKGROUND.change_background()
                BACKGROUND.batch.draw()
        elif PLAYER:
            if PLAYER['forbiden'] is True:
                PLAYER = False
                BONUS.bonus_init = []
                BONUS.won = None
                ON_KEY_IS_PRESS = 1
                if USE_ANIME is True and ANIME_SPRITE:
                    ANIME_SPRITE.draw()
                else:
                    # BACKGROUND.new_batch()
                    # BACKGROUND.change_background()
                    BACKGROUND.batch.draw()
            else:
                if NAV.in_nra_val is True:
                    BONUS.won = CLIENT.get('PLAYER_WON_BONUS')
                    # BACKGROUND.new_batch()
                    # BACKGROUND.change_background()
                    BACKGROUND.batch.draw()
                    NAV.new_batch()
                    NAV.set_navi(ON_KEY_IS_PRESS)
                    # MENU.new_batch()
                    MENU.batch.draw()
                    NAV.batch.draw()
                    TEXT.clean_all_text()
                elif BONUS.bonus_init == [] and BONUS.won == None and client_get_bonus == []:
                    BONUS.won = CLIENT.get('PLAYER_WON_BONUS')
                    # BACKGROUND.new_batch()
                    # BACKGROUND.change_background()
                    BACKGROUND.batch.draw()
                    NAV.new_batch()
                    NAV.set_navi(ON_KEY_IS_PRESS)
                    # MENU.new_batch()
                    MENU.batch.draw()
                    NAV.batch.draw()
                    TEXT.clean_all_text()
                    if HIDE_NAME is False:
                        TEXT.name.text = PLAYER['name']
                    else:
                        TEXT.name.text = PLAYER['cart_id']
                    TEXT.menu_name.text = TEXT.set_menu_name[ON_KEY_IS_PRESS - 1]
                    if CLIENT.get('PLAYER_BONUS_WARNING') is True:
                        SET_BONUS_WARNING.batch.draw()
                    if ON_KEY_IS_PRESS == 1:
                        if PLAYER['mony_back_use'] is False:
                            TEXT.row_2.text = u''
                        else:
                            if 'new_meter' in PLAYER and 'old_meter' in PLAYER:
                                if CLIENT.get('MONY_BACK_PAY') == False:
                                    if PLAYER['new_meter']['bet'] >= PLAYER['old_meter']['bet']:
                                        mony_back = ("{:.2f}".format(
                                            round((PLAYER['new_meter']['bet'] - PLAYER['old_meter']['bet']) * PLAYER['mony_back_pr'],
                                                  2)))
                                        if PLAYER['mony_back_min_pay'] > 0:
                                            if float(mony_back) + PLAYER['total_mony_back'] <= PLAYER['mony_back_min_pay']:
                                                TEXT.row_2.text = _(u'Мънибек: %s') % (mony_back)
                                            else:
                                                TEXT.row_2.text = _(u'Мънибек: %s') % ("{:.2f}".format(PLAYER['mony_back_min_pay']))
                                        else:
                                            TEXT.row_2.text = _(u'Мънибек: %s') % (mony_back)
                                    else:
                                        TEXT.row_2.text = _(u'Мънибек: %s') % ('0.00')
                                else:
                                    TEXT.row_2.text = _(u'Мънибек: Изчакайте!')
                            else:
                                TEXT.row_2.text = _(u'Мънибек: %s') % ('0.00')
                        if PLAYER['tombola_use'] is False:
                            TEXT.row_3.text = u''
                        else:
                            if 'new_meter' in PLAYER and 'old_meter' in PLAYER:
                                if PLAYER['tombola_on_in'] is False:
                                    if PLAYER['new_meter']['bet'] >= PLAYER['old_meter']['bet']:
                                        tombula = ("{:.2f}".format(round(
                                            ((PLAYER['new_meter']['bet'] - PLAYER['old_meter']['bet']) * PLAYER[
                                                'tombola_coef']) * 0.01,
                                            2)))
                                        tombula = _(u'Точки: %s') % (tombula)
                                    else:
                                        tombula = _(u'Точки: %s') % ('0.00')
                                else:
                                    tombula = (PLAYER['new_meter']['in'] - PLAYER['old_meter']['in']) - (PLAYER['new_meter']['out'] - PLAYER['old_meter']['out'])
                                    if PLAYER['new_meter']['in'] >= PLAYER['old_meter']['in']:
                                        tombula = ("{:.2f}".format(round(
                                                (tombula * PLAYER['tombola_coef']) * 0.01, 2)))
                                        tombula = _(u'Точки: %s') % (tombula)
                                    else:
                                        tombula = _(u'Точки: %s') % ('0.00')
                                TEXT.row_3.text = tombula
                            else:
                                TEXT.row_3.text = _(u'Точки: %s') % ('0.00')
                        # TEXT.row_3.text = _(u'Пари по карта: %s') % ("{:.2f}".format(PLAYER['curent_mony']))

                        # TEXT.row_5.text = _(u'Всяко поставяне на карта започва с 0 точки!')
                        # TEXT.row_6.text = _(u'За прехвърляне на точки извадете карта!')
                        # TEXT.row_7.text = _(u'ИЗПЛАЩАТ СЕ САМО ТОЧКИ ПРЕХВЪРЛЕНИ В СТАТИСТИКА!')
                    elif ON_KEY_IS_PRESS == 2:
                        BONUS.won = CLIENT.get('PLAYER_WON_BONUS')
                        if PLAYER['mony_back_use'] is False:
                            TEXT.row_2.text = u''
                        else:
                            if CLIENT.get('MONY_BACK_PAY') == False:
                                mony_back = "{:.2f}".format(PLAYER['total_mony_back'])
                                TEXT.row_2.text = _(u'Мънибек: %s') % (mony_back)
                            else:
                                TEXT.row_2.text = _(u'Мънибек: Изчакайте!')
                        if PLAYER['tombola_use'] is True:
                            tombula = "{:.2f}".format(PLAYER['total_tombula'])
                            TEXT.row_3.text = _(u'Точки: %s') % (tombula)
                        else:
                            TEXT.row_3.text = u''
                        # TEXT.row_5.text = _(u'ЗА ИЗПЛАЩАНЕ НА ТЕКУЩО НАТРУПАНИТЕ ТОЧКИ')
                        # TEXT.row_6.text = _(u'МОЛЯ ИЗВАДЕТЕ КАРТАТА!')
                    my_revert_by_bet = CLIENT.get('PLAYER_BONUS_REVERT')
                    if my_revert_by_bet == None:
                        TEXT.row_4.text = u''
                    else:
                        if 'new_meter' in PLAYER and 'old_meter' in PLAYER:
                            if type(my_revert_by_bet) == list:
                                if my_revert_by_bet[0] == 0:
                                    # if my_revert_by_bet[1] != 0:
                                    #     revert_by_bet = 1
                                    # else:
                                    revert_by_bet = 0
                                else:
                                    tmp = round(PLAYER['new_meter']['bet'] - my_revert_by_bet[1])
                                    try:
                                        # print revert_by_bet[0], tmp, round((revert_by_bet[0]/tmp)*100, 2)
                                        revert_by_bet = round((tmp / my_revert_by_bet[0]) * 100, 2)
                                        if revert_by_bet >= 100:
                                            # CLIENT.set('PLAYER_BONUS_REVERT', [0, 0])
                                            revert_by_bet = 0
                                    except ZeroDivisionError:
                                        revert_by_bet = 0.01
                            else:
                                revert_by_bet = my_revert_by_bet
                                # if revert_by_bet is None:
                                #     revert_by_bet = 0
                                # if PLAYER['new_meter']['curent credit'] >= revert_by_bet:
                                #     revert_by_bet = 0
                        else:
                            revert_by_bet = 0
                        if revert_by_bet > 0:
                            if type(my_revert_by_bet) == list:
                                TEXT.row_4.text = _(u'Кешаут на: %s') % ("{:.0f}".format(revert_by_bet) + u' %')
                            else:
                                TEXT.row_4.text = _(u'Кешаут на: %s') % ("{:.2f}".format(revert_by_bet))
                        else:
                            TEXT.row_4.text = u''
                    if SHOW_OUT_BUTTON:
                        if CLIENT.get('MAKE_IN_OUT'):
                            TEXT.row_1.text = _(u'Изчакайте!')
                        else:
                            TEXT.row_1.text = _(u'Пари по карта: %s') % ("{:.2f}".format(PLAYER['curent_mony']))
                    else:
                        TEXT.row_1.text = u''
                    TEXT.batch.draw()

                elif BONUS.bonus_init != [] and BONUS.won == None and client_get_bonus == []:
                    # BACKGROUND.change_background()
                    # BACKGROUND.batch.draw()
                    # BONUS.add_box()
                    BONUS.batch.draw()
                elif PLAYER is not False and PLAYER != None and BONUS.bonus_init == [] and BONUS.won != None and client_get_bonus == []:
                    # BACKGROUND.change_background()
                    # BACKGROUND.batch.draw()
                    BONUSWON.mony(BONUS.won)
                    BONUSWON.batch.draw()
                elif PLAYER is not False and PLAYER != None and client_get_bonus != []:
                    if client_get_bonus[0] is True:
                        BUNUSWONNOBUTTON.mony(client_get_bonus[1])
                        BUNUSWONNOBUTTON.batch.draw()

        else:
            HIDE_NAME = True
            if USE_ANIME and ANIME_SPRITE:
                ANIME_SPRITE.draw()
            else:
                # BACKGROUND.new_batch()
                # BACKGROUND.change_background()
                BACKGROUND.batch.draw()
        if CLIENT.get('PLAYER_PLAY_BONUS_MONY') != None:
            RED_POINT.batch.draw()
        # SET_BONUS_WARNING.batch.draw()
    except Exception as e:
        log.stdout_logger.critical(e, exc_info=True)
        time.sleep(0.5)

# pyglet.clock.schedule_interval(on_draw, 1 * 0.17)

if __name__ == '__main__':
    pyglet.app.run()

