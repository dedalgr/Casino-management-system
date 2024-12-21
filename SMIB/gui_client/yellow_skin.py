# -*- coding:utf-8 -*-
'''
Created on 27.02.2019

@author: dedal
'''
import sys
import pyglet
from pyglet.window import key
from pyglet.window import mouse
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
batch = pyglet.graphics.Batch()

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
    ANIME_NIM = '6'
    MY_RANGE = [0, 199]

if DEBUG is False:
    VIDEO = []
    for i in range(MY_RANGE[0], MY_RANGE[1]):
        VIDEO.append(pyglet.resource.image('video/%s/image%s.%s' % (ANIME_NIM, str(i), 'jpg')))
    if ANIME_NIM == '1':
        for i in VIDEO:
            i.width = int(screen_width)
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
SHOW_OUT_BUTTON = CLIENT.get('SHOW_OUT_BUTTON')
MAKE_IN_OUT = CLIENT.get('MAKE_IN_OUT')
USE_SAS_AFT = CLIENT.get('use_sas_aft')

class BaskGround():
    def __init__(self):
        #         global batch
        global background
        global logo
        global LOGO_NAME

        self.batch = pyglet.graphics.Batch()
        self.background_group = background
        self.logo_group = logo
        #         self.change_background(fon)
        #         self.fon = pyglet.image.SolidColorImagePattern((255,255,255,255)).create_image(screen_width, screen_height)
        #        try:
        self.pic = pyglet.resource.image('img/5178.png')
        self.pic.width = int(screen_width)
        self.pic.height = int(screen_height)
        #        except Exception as e:
        #            print e
        # LOGO_NAME = '5178.png'
        # self.pic = pyglet.resource.image('img/' + LOGO_NAME)
        # self.pic.width = int(screen_width)
        # self.pic.height = int(screen_height)
        # if LOGO_NAME == '5178.png':
        try:
            self.logo = pyglet.resource.image('img/' + LOGO_NAME)
            self.logo.width = int(screen_width // 2)
            self.logo.height = int(screen_height // 2)
        except Exception as e:
            print(e)
            LOGO_NAME = 'colibri-logo.png'
            self.logo = pyglet.resource.image('img/colibri-logo.png')
            self.logo.width = int(screen_width // 2)
            self.logo.height = int(screen_height // 2)

        #         self.sprite = pyglet.sprite.Sprite(self.pic, batch=self.batch, group=self.background)
        #         self.batch = batch
        self.change_background()
        # if LOGO_NAME == '5178.png':
        self.set_logo()
        # self.show_red_point()

    def new_batch(self):
        self.batch = pyglet.graphics.Batch()

    def change_background(self):
        #         self.fon.blit(0, 0)
        self.background_sprite = pyglet.sprite.Sprite(self.pic, batch=self.batch, group=self.background_group)

    def set_logo(self):
        self.logo_sprite = pyglet.sprite.Sprite(self.logo, batch=self.batch, group=self.logo_group)


class RedPoint():
    def __init__(self):
        global text
        self.redpoint_group = text
        self.batch = pyglet.graphics.Batch()

        self.point_red = pyglet.resource.image('img/Gnome-Emblem-Important-32.png')
        self.point_red.width = int(screen_width * 0.05)
        self.point_red.height = int(screen_height * 0.07)

    def show_red_point(self):
        self.red_point_sprite = pyglet.sprite.Sprite(self.point_red, batch=self.batch, group=self.redpoint_group)
        self.red_point_sprite.position = (screen_width * 0.90, screen_height * 0.1, 0)


class SetBonusWarning():
    def __init__(self):
        # global batch
        global bonus_group
        self.batch = pyglet.graphics.Batch()
        self.button_group = bonus_group
        # self.bonus_image = pyglet.resource.image('img/pngegg.png')
        # self.bonus_image.width = int(screen_width * 0.55)
        # self.bonus_image.height = int(screen_height * 0.45)
        self.bonus_image = pyglet.resource.image('img/pngwing.com.png')
        self.bonus_image.width = int(screen_width * 0.35)
        self.bonus_image.height = int(screen_height * 0.22)

    def new_batch(self):
        self.batch = pyglet.graphics.Batch()

    def show_bonus_warning(self):
        self.bonus_image_sprite = pyglet.sprite.Sprite(self.bonus_image, batch=self.batch, group=self.button_group)
        # self.bonus_image_sprite.position = (screen_width * 0.40, screen_height * 0.02)
        self.bonus_image_sprite.position = (screen_width * 0.65, screen_height * 0.12, 0)

class ButonSet():
    def __init__(self):
        global batch
        global button
        global text

        self.batch = batch
        self.button_group = button
        self.text_group = text

        self.vertical_line = pyglet.resource.image('img/vertical-line.png')
        self.vertical_line.width = int(screen_width * 0.04)
        self.vertical_line.height = int(screen_height * 0.6)
        self.count = 4
        self.name = False
        self.hide_name = True

        #         self.horizontal_line = pyglet.resource.image('img/horizontal_line.png')
        #         self.horizontal_line.width = int(screen_width*0.30)
        #         self.horizontal_line.height = int(screen_height*0.4)

        self.menu_button = pyglet.resource.image('img/menu_button_1.png')
        self.menu_button.width = int(screen_width * 0.30)
        self.menu_button.height = int(screen_height * 0.20)

    # def new_batch(self):
    #     self.batch = pyglet.graphics.Batch()

    def name_text_obj(self):
        self.name = pyglet.text.Label(
            _(u'Приятна игра: '),
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=font_name,
            x=self.name_button.width * 0.28,
            y=screen_height * 0.838,
            group=self.text_group,
            batch=self.batch,
            color=(153, 153, 0, 255)
        )

    def set_button_text(self, count=4):
        self.count = count
        if self.count >= 1:
            self.button_tex_1 = pyglet.text.Label(
                _(u'Текущ'),
                font_name='Arial',
                bold=True,
                italic=True,
                font_size=font_button,
                x=self.name_button.width * 0.162,
                y=screen_height * 0.685,
                group=self.text_group,
                batch=self.batch,
                #                                       color=(139,0,0,255)
            )
        if self.count >= 2:
            self.button_tex_2 = pyglet.text.Label(
                _(u'Баланс'),
                font_name='Arial',
                bold=True,
                italic=True,
                font_size=font_button,
                x=self.name_button.width * 0.162,
                y=screen_height * 0.49,
                group=self.text_group,
                batch=self.batch,
                #                                       color=(0,0,255,255)
            )
        if self.count >= 3 and SHOW_OUT_BUTTON is True:
            self.button_tex_3 = pyglet.text.Label(
                _(u'IN/OUT'),
                font_name='Arial',
                bold=True,
                italic=True,
                font_size=font_button,
                x=self.name_button.width * 0.162,
                y=screen_height * 0.28,
                group=self.text_group,
                batch=self.batch,
                #                                       color=(0,0,255,255)
            )
        if self.count >= 4:
            self.button_tex_4 = pyglet.text.Label(
                _(u'Изход'),
                font_name='Arial',
                bold=True,
                italic=True,
                font_size=font_button,
                x=self.name_button.width * 0.162,
                y=screen_height * 0.15,
                group=self.text_group,
                batch=self.batch,
                #                                       color=(0,0,255,255)
            )

    def show_name(self, name=None):
        self.name_button = pyglet.resource.image('img/cust_name.png')
        self.name_button.width = int(screen_width * 0.8)
        self.name_button.height = int(screen_height // 5)
        if name == None:
            name = ''
        else:
            name = name
        if not self.name:
            self.name_text_obj()
        self.name_sprite = pyglet.sprite.Sprite(self.name_button, batch=self.batch, group=self.button_group)
        self.name_sprite.position = (screen_width * 0.15, screen_height * 0.75, 0)
        self.name.text = name

    def show_line(self):
        self.line_sprite = pyglet.sprite.Sprite(self.vertical_line, batch=self.batch, group=self.button_group)
        self.line_sprite.position = (screen_width * 0.35, screen_height * 0.15, 0)

    def show_menu_buton(self, count=4):
        self.count = count
        if self.count >= 1:
            self.menu_button_1_sprite = pyglet.sprite.Sprite(self.menu_button, batch=self.batch,
                                                             group=self.button_group)
            self.menu_button_1_sprite.position = (screen_width * 0.01, screen_height * 0.60, 0)

        if self.count >= 2:
            self.menu_button_2_sprite = pyglet.sprite.Sprite(self.menu_button, batch=self.batch,
                                                             group=self.button_group)
            self.menu_button_2_sprite.position = (screen_width * 0.01, screen_height * 0.40, 0)

        if self.count >= 3 and SHOW_OUT_BUTTON is True:
            self.menu_button_3_sprite = pyglet.sprite.Sprite(self.menu_button, batch=self.batch,
                                                             group=self.button_group)
            self.menu_button_3_sprite.position = (screen_width * 0.01, screen_height * 0.20, 0)

        if self.count >= 4:
            self.menu_button_4_sprite = pyglet.sprite.Sprite(self.menu_button, batch=self.batch,
                                                             group=self.button_group)
            self.menu_button_4_sprite.position = (screen_width * 0.01, screen_height * 0.06, 0)

    def set_menu(self, name=None, count=4):
        self.show_name(name)
        self.show_line()
        self.show_menu_buton(count)
        self.set_button_text(count)


class RightText():
    def __init__(self):
        global batch
        global text
        global button
        self.batch = batch
        self.text_group = text
        self.line_group = button
        self.horizontal_line = pyglet.resource.image('img/horizontal-line.png')
        self.horizontal_line.width = int(screen_width * 0.48)
        self.horizontal_line.height = int(screen_height * 0.3)

        self.in_menu = False
        self.bet = False
        # self.game_pleed = False
        self.mony_back_total = False
        self.mony_back = False
        self.tombula = False
        self.game_pleed = False

    def in_menu_obj(self):
        self.in_menu = pyglet.text.Label(
            _(u'Текущ:'),
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=font_text,
            x=screen_width * 0.43,
            y=screen_height * 0.60,
            group=self.text_group,
            batch=self.batch,
            #                                       color=(153,153,0,255)
        )

    def set_bet(self):
        self.bet = pyglet.text.Label(
            u'',
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=count_text,
            x=screen_width * 0.43,
            y=screen_height * 0.20,
            group=self.text_group,
            batch=self.batch,
            #                                       color=(153,153,0,255)
        )

    def set_game_played(self):
        self.game_pleed = pyglet.text.Label(
                                          _(u'Пари по карта: 0'),
                                          font_name='Arial',
                                          bold=True,
                                          italic=True,
                                          font_size=count_text,
                                          x=screen_width*0.43,
                                          y=screen_height*0.50,
                                          group=self.text_group,
                                          batch = self.batch,
    #                                       color=(153,153,0,255)
                                          )
    def set_mony_back(self):
        self.mony_back = pyglet.text.Label(
            u'',
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=count_text,
            x=screen_width * 0.43,
            y=screen_height * 0.40,
            group=self.text_group,
            batch=self.batch,
            #                                       color=(153,153,0,255)
        )

    def set_tombula(self):
        self.tombula = pyglet.text.Label(
            u'',
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=count_text,
            x=screen_width * 0.43,
            y=screen_height * 0.30,
            group=self.text_group,
            batch=self.batch,
            #                                       color=(153,153,0,255)
        )

    def set_line(self):

        self.line_sprite = pyglet.sprite.Sprite(self.horizontal_line, batch=self.batch, group=self.line_group)
        self.line_sprite.position = (screen_width * 0.4, screen_height * 0.55, 0)

    def set_in_menu(self, name=None, curent_monyback=0, tombula_count=0, use_mony_back=False, tombula_use=False, bet=0, mony_on_cart=0):
        if not self.in_menu:
            self.in_menu_obj()
        if not self.game_pleed:
            self.set_game_played()
        else:
            if SHOW_OUT_BUTTON:
                self.game_pleed.text = _(u'Пари по карта: %s') % ("{:.0f}".format(mony_on_cart))
            else:
                self.game_pleed.text = u''

        if not self.bet:
            self.set_bet()
        else:
            if bet > 0:
                if type(CLIENT.get('PLAYER_BONUS_REVERT')) == list:
                    self.bet.text = _(u'Процент: %s') % ("{:.0f}".format(bet)) + '%'
                else:
                    self.bet.text = _(u'Кешаут на: %s') % ("{:.2f}".format(bet))
            else:
                self.bet.text = u''
        # if not self.game_self.set_bet(pleed:
        #     self.set_game_played()
        if name == None:
            name = _(u'Текущ:')
        if not self.tombula:
            self.set_tombula()
        if tombula_use is True:
            if tombula_count != None:
                self.tombula.text = tombula_count
        else:
            self.tombula.text = u''

        if not self.mony_back:
            self.set_mony_back()
        if use_mony_back is True:
            if curent_monyback != None:
                self.mony_back.text = curent_monyback
        else:
            self.mony_back.text = u''

        # if bet > 0:
        #     self.bet = bet
        self.in_menu.text = name
        # if credit != None:
        #     self.curent_credit.text =  credit
        # else:
        #     self.curent_credit.text =  u''

        # if game_played != None:
        #     self.game_pleed.text = game_played
        # else:
        #     self.game_pleed.text = u''


class Bonus():
    def __init__(self):
        #         global batch
        global button
        global text

        self.batch = pyglet.graphics.Batch()
        self.box_group = button
        self.box = pyglet.resource.image('img/closed-box.png')
        self.box.width = int(screen_width * 0.40)
        self.box.height = int(screen_height * 0.55)
        self.bonus_init = []
        self.won = None

    def add_box(self):
        self.box_1_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
        self.box_1_sprite.position = (screen_width * 0.00, screen_height * 0.50, 0)

        self.box_2_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
        self.box_2_sprite.position = (screen_width * 0.325, screen_height * 0.50, 0)

        self.box_3_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
        self.box_3_sprite.position = (screen_width * 0.65, screen_height * 0.50, 0)
        #
        self.box_6_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
        self.box_6_sprite.position = (screen_width * 0.15, screen_height * 0.10, 0)

        self.box_7_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
        self.box_7_sprite.position = (screen_width * 0.48, screen_height * 0.10, 0)


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
        global font_name
        global USE_SAS_AFT

        self.batch = batch
        self.text_group = text

        self.batch = pyglet.graphics.Batch()
        self.box_group = button
        self.box = pyglet.resource.image('img/open_box.png')
        self.box.width = int(screen_width * 0.50)
        self.box.height = int(screen_height * 0.60)

        self.box_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
        self.box_sprite.position = (screen_width * 0.20, screen_height * 0.20, 0)

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
            x=screen_width * 0.30,
            y=screen_height * 0.63,
            group=self.text_group,
            batch=self.batch,
            #                                       color=(153,153,0,255)
        )

    def mony(self, mony):
        self.won_text.text = "{:.2f}".format(mony)


class BonusWon():
    def __init__(self):
        global count_text
        global button
        global text
        global font_name

        self.batch = batch
        self.text_group = text

        self.batch = pyglet.graphics.Batch()
        self.box_group = button
        self.box = pyglet.resource.image('img/open_box.png')
        self.box.width = int(screen_width * 0.50)
        self.box.height = int(screen_height * 0.60)

        self.box_sprite = pyglet.sprite.Sprite(self.box, batch=self.batch, group=self.box_group)
        self.box_sprite.position = (screen_width * 0.20, screen_height * 0.20, 0)

        self.button_not_get_text = pyglet.text.Label(
            _(u'Отложи'),
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=font_name,
            x=screen_width * 0.06,
            y=screen_height * 0.88,
            group=self.text_group,
            batch=self.batch,
            color=(153, 153, 0, 255)
        )

        self.button_get_text = pyglet.text.Label(
            _(u'Приеми'),
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=font_name,
            x=screen_width * 0.76,
            y=screen_height * 0.88,
            group=self.text_group,
            batch=self.batch,
            color=(153, 153, 0, 255)
        )

        self.won_text = pyglet.text.Label(
            u'00.00',
            font_name='Arial',
            bold=True,
            italic=True,
            font_size=won_text,
            x=screen_width * 0.30,
            y=screen_height * 0.63,
            group=self.text_group,
            batch=self.batch,
            #                                       color=(153,153,0,255)
        )

    def mony(self, mony):
        self.button = pyglet.resource.image('img/cust_name.png')
        self.button.width = int(screen_width * 0.35)
        self.button.height = int(screen_height * 0.2)
        self.button_sprite = pyglet.sprite.Sprite(self.button, batch=self.batch, group=self.box_group)
        self.button_sprite.position = (screen_width * 0.65, screen_height * 0.8, 0)

        self.button_sprite_2 = pyglet.sprite.Sprite(self.button, batch=self.batch, group=self.box_group)
        self.button_sprite_2.position = (screen_width * 0.01, screen_height * 0.8, 0)
        self.won_text.text = "{:.2f}".format(mony)


BACKGROUND = BaskGround()
BUTTON = ButonSet()
RIGHTTEXT = RightText()
BONUS = Bonus()
BONUSWON = BonusWon()
PLAYER = False
BUNUSWONNOBUTTON = BonusWonNoButton()
SET_BONUS_WARNING = SetBonusWarning()
RED_POINT = RedPoint()
RED_POINT.show_red_point()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ENTER:
        CLIENT.set('HALT', True)
    if symbol == key.ESCAPE and DEBUG is True:
        sys.exit()
    if symbol == key.ESCAPE and DEBUG is False:
        return True


CONF_IS_CLICK = False
PLAYER_INIT = False


@window.event
def on_mouse_press(x, y, button, modifiers):
    global PLAYER
    global BONUS
    global CONF_IS_CLICK
    if PLAYER is not False and PLAYER != None:
        if BONUS.bonus_init == [] and BONUS.won == None:
            if BUTTON.count >= 1 and x > screen_width * 0.01 and x < screen_width * 0.30 and y < screen_height * 0.65 + screen_height * 0.15 and y > screen_height * 0.60:
                if PLAYER['tombola_use'] is True:
                    if PLAYER['tombola_on_in'] is False:
                        if PLAYER['new_meter']['bet'] >= PLAYER['old_meter']['bet']:
                            tombula = _(u'Точки: %s') % ("{:.2f}".format(round(
                            ((PLAYER['new_meter']['bet'] - PLAYER['old_meter']['bet']) * PLAYER['tombola_coef']) * 0.01,
                            2)))
                    else:
                        ins = PLAYER['new_meter']['in'] - PLAYER['old_meter']['in']
                        out = PLAYER['new_meter']['out'] - PLAYER['old_meter']['out']
                        total = ins - out
                        # if ins <= 0:
                        #     total = 0
                        if PLAYER['new_meter']['in'] >= PLAYER['old_meter']['in']:
                            tombula = _(u'Точки: %s') % (
                            "{:.2f}".format(round(((total) * PLAYER['tombola_coef']) * 0.01, 2)))
                else:
                    tombula = u''
                if PLAYER['mony_back_use'] is False:
                    mony_back = _(u'Мънибек: %s') % ('0.00')
                else:
                    if PLAYER['new_meter']['bet'] >= PLAYER['old_meter']['bet']:
                        mony_back = _(u'Мънибек: %s') % ("{:.2f}".format(
                        round((PLAYER['new_meter']['bet'] - PLAYER['old_meter']['bet']) * PLAYER['mony_back_pr'], 2)))
                my_revert_by_bet = CLIENT.get('PLAYER_BONUS_REVERT')
                if my_revert_by_bet == None:
                    revert_by_bet = 0
                else:
                    if type(my_revert_by_bet) == list:
                        if my_revert_by_bet[0] == 0:
                            revert_by_bet = 0
                        else:
                            tmp = round(PLAYER['new_meter']['bet'] - my_revert_by_bet[1])
                            try:
                                revert_by_bet = round((tmp / my_revert_by_bet[0]) * 100, 2)
                            except ZeroDivisionError:
                                revert_by_bet = 0.01
                            if revert_by_bet >= 100:
                                CLIENT.set('PLAYER_BONUS_REVERT', [0, 0])
                                revert_by_bet = 0
                    else:
                        revert_by_bet = my_revert_by_bet
                        if PLAYER['new_meter']['curent credit'] >= revert_by_bet:
                            revert_by_bet = 0
                    # bet = revert_by_bet
                RIGHTTEXT.set_in_menu(_(u'Текущ:'),
                                      curent_monyback=mony_back,
                                      tombula_count=tombula,
                                      use_mony_back=PLAYER['mony_back_use'],
                                      tombula_use=PLAYER['tombola_use'],
                                      bet=revert_by_bet,
                                      mony_on_cart=PLAYER['curent_mony']
                                      )
                CONF_IS_CLICK = False
            if BUTTON.count >= 2 and x > screen_width * 0.01 and x < screen_width * 0.30 and y < screen_height * 0.45 + screen_height * 0.15 and y > screen_height * 0.40:
                RIGHTTEXT.set_in_menu(_(u'Баланс:'),
                                      curent_monyback=_(u'Натрупан Мънибек: %s') % (
                                          "{:.2f}".format(PLAYER['total_mony_back'])),
                                      tombula_count=_(u'Натрупани точки: %s') % (
                                          "{:.2f}".format(PLAYER['total_tombula'])),
                                      use_mony_back=PLAYER['mony_back_use'],
                                      tombula_use=PLAYER['tombola_use'],
                                      mony_on_cart=PLAYER['curent_mony']
                                      )
                CONF_IS_CLICK = True
            if BUTTON.count >= 3 and x > screen_width * 0.01 and x < screen_width * 0.30 and y < screen_height * 0.26 + screen_height * 0.15 and y > screen_height * 0.26 and SHOW_OUT_BUTTON is True:
                CLIENT.set('MAKE_IN_OUT', True)
            if BUTTON.count >= 4 and x > screen_width * 0.01 and x < screen_width * 0.30 and y < screen_height * 0.09 + screen_height * 0.15 and y > screen_height * 0.09:
                PLAYER = False
            #                 pass
            #                 window.clear()
            if x > screen_width * 0.15 and x < screen_width * 0.9 and y < screen_height * 0.75 + screen_height // 5 and y > screen_height * 0.75:
                if BUTTON.hide_name is True:
                    BUTTON.show_name(name=_(u'Приятна игра: %s') % (PLAYER['cart_id']))
                    BUTTON.hide_name = False
                elif BUTTON.hide_name is False:
                    BUTTON.show_name(name=_(u'Приятна игра: %s') % (PLAYER['name']))
                    BUTTON.hide_name = True
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

    return True


BACKGROUND.change_background()
# if LOGO_NAME == '5178.png':
BACKGROUND.set_logo()
SET_BONUS_WARNING.show_bonus_warning()

COUNT = 0

@window.event
def on_draw():
    # global MENU_LOAD
    global PLAYER_INIT
    global batch
    global CONF_IS_CLICK
    global PLAYER
    global BONUS
    global RED_POINT
    global COUNT
    global ANIME_SPRITE
    global USE_ANIME
    time.sleep(0.05)
    window.clear()

    # if DEBUG is False:
    #     if CLIENT.get('PLAYER_PLAY_BONUS_MONY') != None:
    #         # OLD_PLAYER = CLIENT.get('PLAYER_PLAY_BONUS_MONY')
    #         RED_POINT.batch.draw()
    #     # if OLD_PLAYER != None and CLIENT.get('PLAYER_PLAY_BONUS_MONY') == None:
    #     #     OLD_PLAYER = None
    #     #     BACKGROUND.new_batch()
    #     #     BACKGROUND.change_background()
    #     #     BACKGROUND.set_logo()
    #
    # else:
    #     pass
    # if DEBUG is False:
    #     if CLIENT.get('PLAYER_BONUS_WARNING') is True:
    #         SET_BONUS_WARNING.batch.draw()
    # else:
    #     pass
    try:
        PLAYER = CLIENT.get('PLAYER')
        in_nra_val = CLIENT.get('PLAYER_IN_NRA')
        BONUS.bonus_init = CLIENT.get('PLAYER_BONUS_INIT')
        client_get_bonus = CLIENT.get('PLAYER_GET_BONUS')
        if client_get_bonus == None:
            client_get_bonus = []
        if PLAYER:
            if PLAYER['forbiden'] is True:
                PLAYER = False
                CONF_IS_CLICK = False
                if USE_ANIME is True and ANIME_SPRITE:
                    ANIME_SPRITE.draw()
                else:
                    BACKGROUND.batch.draw()
            else:
                BACKGROUND.batch.draw()
                if CLIENT.get('PLAYER_BONUS_WARNING') is True:
                    SET_BONUS_WARNING.batch.draw()
                if CLIENT.get('PLAYER_PLAY_BONUS_MONY') != None:
                    RED_POINT.batch.draw()
        else:
            # print time.time()
            if USE_ANIME is True and ANIME_SPRITE:
                ANIME_SPRITE.draw()
            else:
                BACKGROUND.batch.draw()
            # time.sleep(5)
            # ANIME_SPRITE.on_animation_end()

        if PLAYER == None:
            PLAYER = False
            CONF_IS_CLICK = False
        elif PLAYER is False:
            CONF_IS_CLICK = False
        elif 'new_meter' not in PLAYER and 'old_meter' not in PLAYER:
            PLAYER = False
            CONF_IS_CLICK = False
        elif None in PLAYER['new_meter'].values():
            pass
        elif None in PLAYER['old_meter'].values():
            pass

        elif PLAYER_INIT is False and PLAYER is not False and BONUS.won == None and client_get_bonus == []:
            PLAYER_INIT = True
            BUTTON.set_menu(name=_(u'Приятна игра: %s') % (PLAYER['cart_id']), count=3)
            RIGHTTEXT.set_line()
            RIGHTTEXT.set_in_menu(_(u'Текущ:'))
        elif PLAYER is not False and PLAYER_INIT is True and CONF_IS_CLICK is False and BONUS.won == None and client_get_bonus == []:
            BONUS.won = CLIENT.get('PLAYER_WON_BONUS')
            if PLAYER['new_meter'] != None:
                PLAYER['total_game'] = PLAYER['new_meter']['games played'] - PLAYER['old_meter']['games played']
                if PLAYER['tombola_use'] is True:
                    if PLAYER['tombola_on_in'] is False:
                        if PLAYER['new_meter']['bet'] >= PLAYER['old_meter']['bet']:
                            tombula = _(u'Точки: %s') % ("{:.2f}".format(round(
                                ((PLAYER['new_meter']['bet'] - PLAYER['old_meter']['bet']) * PLAYER['tombola_coef']) * 0.01,
                                2)))
                    else:
                        tombula = (PLAYER['new_meter']['in'] - PLAYER['old_meter']['in']) - (
                                    PLAYER['new_meter']['out'] - PLAYER['old_meter']['out'])
                        # if PLAYER['new_meter']['in'] >= PLAYER['old_meter']['in']:
                        tombula = ("{:.2f}".format(round((tombula * PLAYER['tombola_coef']) * 0.01, 2)))
                        tombula = _(u'Точки: %s') % (tombula)
                        # if PLAYER['new_meter']['in'] >= PLAYER['old_meter']['in']:
                        #     tombula = _(u'Точки: %s') % ("{:.2f}".format(round(
                        #     ((PLAYER['new_meter']['in'] - PLAYER['old_meter']['in']) * PLAYER['tombola_coef']) * 0.01,
                        #     2)))
                else:
                    tombula = u''
                if PLAYER['mony_back_use'] is False:
                    mony_back = u''
                else:
                    if PLAYER['new_meter']['bet'] >= PLAYER['old_meter']['bet']:
                        mony_back = _(u'Мънибек: %s') % ("{:.2f}".format(
                            round((PLAYER['new_meter']['bet'] - PLAYER['old_meter']['bet']) * PLAYER['mony_back_pr'], 2)))
                my_revert_by_bet = CLIENT.get('PLAYER_BONUS_REVERT')
                if type(my_revert_by_bet) == list:
                    if my_revert_by_bet[0] == 0:
                        revert_by_bet = 0
                    else:
                        tmp = round(PLAYER['new_meter']['bet'] - my_revert_by_bet[1])
                        try:
                            # print revert_by_bet[0], tmp, round((revert_by_bet[0]/tmp)*100, 2)
                            revert_by_bet = round((tmp / my_revert_by_bet[0]) * 100, 2)
                            if revert_by_bet >= 100:
                                CLIENT.set('PLAYER_BONUS_REVERT', [0, 0])
                                revert_by_bet = 0
                        except ZeroDivisionError:
                            revert_by_bet = 0.01
                else:
                    revert_by_bet = my_revert_by_bet
                    if PLAYER['new_meter']['curent credit'] >= revert_by_bet:
                        revert_by_bet = 0

                    # bet = revert_by_bet
                RIGHTTEXT.set_in_menu(_(u'Текущ:'),
                                      curent_monyback=mony_back,
                                      tombula_count=tombula,
                                      use_mony_back=PLAYER['mony_back_use'],
                                      tombula_use=PLAYER['tombola_use'],
                                      bet=revert_by_bet,
                                      mony_on_cart=PLAYER['curent_mony']
                                      )
        elif PLAYER is not False and PLAYER_INIT is True and CONF_IS_CLICK is True and client_get_bonus == []:
            RIGHTTEXT.set_in_menu(_(u'Баланс:'),
                                  curent_monyback=_(u'Натрупан Мънибек: %s') % (
                                      "{:.2f}".format(PLAYER['total_mony_back'])),
                                  tombula_count=_(u'Натрупани точки: %s') % ("{:.2f}".format(PLAYER['total_tombula'])),
                                  use_mony_back=PLAYER['mony_back_use'],
                                  tombula_use=PLAYER['tombola_use'],
                                  mony_on_cart=PLAYER['curent_mony']
                                  )
        if PLAYER is False or PLAYER == None:
            PLAYER_INIT = False
            BONUS.bonus_init = []
            BONUS.won = None
            client_get_bonus = []
        if PLAYER is not False and PLAYER != None and BONUS.bonus_init == [] and BONUS.won == None and client_get_bonus == []:
            batch.draw()
        elif PLAYER is not False and PLAYER != None and BONUS.bonus_init != [] and BONUS.won == None and client_get_bonus == [] and in_nra_val != True:
            BONUS.add_box()
            BONUS.batch.draw()
        elif PLAYER is not False and PLAYER != None and BONUS.bonus_init == [] and BONUS.won != None and client_get_bonus == [] and in_nra_val != True:
            BONUSWON.mony(BONUS.won)
            BONUSWON.batch.draw()
        elif PLAYER is not False and PLAYER != None and client_get_bonus != [] and in_nra_val != True:
            if client_get_bonus[0] is True:
                BUNUSWONNOBUTTON.mony(client_get_bonus[1])
                BUNUSWONNOBUTTON.batch.draw()
    except Exception as e:
        log.stdout_logger.critical(e, exc_info=True)
        time.sleep(0.5)

# pyglet.clock.schedule_interval(on_draw, 1 * 0.17)

if __name__ == '__main__':
    pyglet.app.run()
