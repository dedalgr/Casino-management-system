# -*- coding:utf-8 -*-
import pyglet
import time
import resources
import config
# platform = pyglet.canvas.get_display()
# display = platform.get_screens()
# screen = platform.get_default_screen()
SCREEN_WIDTH = resources.SCREEN_WIDTH
SCREEN_HEIGHT = resources.SCREEN_HEIGHT
BET_IN_FIELD = True

class StopGroup():
    def __init__(self):
        self.batch = resources.FIELD_BATCH
        self.group = resources.STOP_GROUP
        self.img = resources.STOP
        self.img.width = int(SCREEN_WIDTH * 0.5)
        self.img.height = int(SCREEN_HEIGHT * 0.8)
        self.sprites = None

    def reset(self):
        if self.sprites:
            self.sprites.delete()
            self.sprites = None

    def show(self):
        self.sprites = pyglet.sprite.Sprite(self.img, batch=self.batch, group=self.group)
        self.sprites.position = (SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.08, 0)

class GroupConfig():
    def __init__(self):
        self.group = resources.COUNT_GROUP
        self.batch = resources.FIELD_BATCH

        self.runner_img = resources.RUNER_FLAG
        self.play_with_cart_img = resources.PLAY_WITH_CART
        self.mega_activ = False
        self.grand_activ = False
        self.major_activ = False
        self.minor_activ = False
        self.mini_activ = False
        self.x2_img = resources.X2
        self.x2_img.width = int(SCREEN_WIDTH * 0.04)
        self.x2_img.height = int(SCREEN_HEIGHT * 0.08)

        self.play_with_cart_img.width = int(SCREEN_WIDTH * 0.055)
        self.play_with_cart_img.height = int(SCREEN_HEIGHT * 0.08)

        self.runner_img.width = int(SCREEN_WIDTH * 0.08)
        self.runner_img.height = int(SCREEN_HEIGHT * 0.12)
        self.sprite = []

    def reset(self):

        for i in self.sprite:
            try:
                i.delete()
                i = None
            except AttributeError:
                pass
        self.sprite = []

    def one_show(self, x2=[], runner=[], play_with_cart=[]):
        if 1 in runner:
            self.runner_mega_sprite = pyglet.sprite.Sprite(self.runner_img, batch=self.batch, group=self.group)
            self.runner_mega_sprite.position = (SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.60, 0)
            self.sprite.append(self.runner_mega_sprite)
        if 1 in x2:
            self.x2_mega_sprite = pyglet.sprite.Sprite(self.x2_img, batch=self.batch, group=self.group)
            self.x2_mega_sprite.position = (SCREEN_WIDTH * 0.65, SCREEN_HEIGHT * 0.745, 0)
            self.sprite.append(self.x2_mega_sprite)
        if 1 in play_with_cart:
            self.play_with_cart_mega_sprite = pyglet.sprite.Sprite(self.play_with_cart_img, batch=self.batch,
                                                                   group=self.group)
            self.play_with_cart_mega_sprite.position = (SCREEN_WIDTH * 0.02, SCREEN_HEIGHT * 0.715, 0)
            self.sprite.append(self.play_with_cart_mega_sprite)

    def tow_show(self, x2=[], runner=[], play_with_cart=[]):
        if 1 in runner:
            self.runner_mega_sprite = pyglet.sprite.Sprite(self.runner_img, batch=self.batch, group=self.group)
            self.runner_mega_sprite.position = (SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.60, 0)
            self.sprite.append(self.runner_mega_sprite)
        if 1 in x2:
            self.x2_mega_sprite = pyglet.sprite.Sprite(self.x2_img, batch=self.batch, group=self.group)
            self.x2_mega_sprite.position = (SCREEN_WIDTH * 0.65, SCREEN_HEIGHT * 0.745, 0)
            self.sprite.append(self.x2_mega_sprite)
        if 1 in play_with_cart:
            self.play_with_cart_mega_sprite = pyglet.sprite.Sprite(self.play_with_cart_img, batch=self.batch,
                                                                   group=self.group)
            self.play_with_cart_mega_sprite.position = (SCREEN_WIDTH * 0.02, SCREEN_HEIGHT * 0.715, 0)
            self.sprite.append(self.play_with_cart_mega_sprite)

        if 2 in runner:
            self.runner_grand_sprite = pyglet.sprite.Sprite(self.runner_img, batch=self.batch, group=self.group)
            self.runner_grand_sprite.position = (SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.335, 0)
            self.sprite.append(self.runner_grand_sprite)
        if 2 in x2:
            self.x2_grand_sprite = pyglet.sprite.Sprite(self.x2_img, batch=self.batch, group=self.group)
            self.x2_grand_sprite.position = (SCREEN_WIDTH * 0.63, SCREEN_HEIGHT * 0.48, 0)
            self.sprite.append(self.x2_grand_sprite)
        if 2 in play_with_cart:
            self.play_with_cart_grand_sprite = pyglet.sprite.Sprite(self.play_with_cart_img, batch=self.batch,
                                                                    group=self.group)
            self.play_with_cart_grand_sprite.position = (SCREEN_WIDTH * 0.13, SCREEN_HEIGHT * 0.45, 0)
            self.sprite.append(self.play_with_cart_grand_sprite)


    def free_show(self, x2=[], runner=[], play_with_cart=[]):
        if 1 in runner:
            self.runner_mega_sprite = pyglet.sprite.Sprite(self.runner_img, batch=self.batch, group=self.group)
            self.runner_mega_sprite.position = (SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.60, 0)
            self.sprite.append(self.runner_mega_sprite)
        if 1 in x2:
            self.x2_mega_sprite = pyglet.sprite.Sprite(self.x2_img, batch=self.batch, group=self.group)
            self.x2_mega_sprite.position = (SCREEN_WIDTH * 0.65, SCREEN_HEIGHT * 0.745, 0)
            self.sprite.append(self.x2_mega_sprite)
        if 1 in play_with_cart:
            self.play_with_cart_mega_sprite = pyglet.sprite.Sprite(self.play_with_cart_img, batch=self.batch,
                                                                   group=self.group)
            self.play_with_cart_mega_sprite.position = (SCREEN_WIDTH * 0.02, SCREEN_HEIGHT * 0.715, 0)
            self.sprite.append(self.play_with_cart_mega_sprite)

        if 2 in runner:
            self.runner_grand_sprite = pyglet.sprite.Sprite(self.runner_img, batch=self.batch, group=self.group)
            self.runner_grand_sprite.position = (SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.335, 0)
            self.sprite.append(self.runner_grand_sprite)
        if 2 in x2:
            self.x2_grand_sprite = pyglet.sprite.Sprite(self.x2_img, batch=self.batch, group=self.group)
            self.x2_grand_sprite.position = (SCREEN_WIDTH * 0.63, SCREEN_HEIGHT * 0.48, 0)
            self.sprite.append(self.x2_grand_sprite)
        if 2 in play_with_cart:
            self.play_with_cart_grand_sprite = pyglet.sprite.Sprite(self.play_with_cart_img, batch=self.batch,
                                                                    group=self.group)
            self.play_with_cart_grand_sprite.position = (SCREEN_WIDTH * 0.13, SCREEN_HEIGHT * 0.45, 0)
            self.sprite.append(self.play_with_cart_grand_sprite)

        if 3 in runner:
            self.runner_major_sprite = pyglet.sprite.Sprite(self.runner_img, batch=self.batch, group=self.group)
            self.runner_major_sprite.position = (SCREEN_WIDTH * 0.725, SCREEN_HEIGHT * 0.06, 0)
            self.sprite.append(self.runner_major_sprite)
        if 3 in x2:
            self.x2_major_sprite = pyglet.sprite.Sprite(self.x2_img, batch=self.batch, group=self.group)
            self.x2_major_sprite.position = (SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.21, 0)
            self.sprite.append(self.x2_major_sprite)
        if 3 in play_with_cart:
            self.play_with_cart_major_sprite = pyglet.sprite.Sprite(self.play_with_cart_img, batch=self.batch,
                                                                   group=self.group)
            self.play_with_cart_major_sprite.position = (SCREEN_WIDTH * 0.18, SCREEN_HEIGHT * 0.18, 0)
            self.sprite.append(self.play_with_cart_major_sprite)

    def for_show(self, x2=[], runner=[], play_with_cart=[]):
        if 1 in runner:
            self.runner_mega_sprite = pyglet.sprite.Sprite(self.runner_img, batch=self.batch, group=self.group)
            self.runner_mega_sprite.position = (SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.60, 0)
            self.sprite.append(self.runner_mega_sprite)
        if 1 in x2:
            self.x2_mega_sprite = pyglet.sprite.Sprite(self.x2_img, batch=self.batch, group=self.group)
            self.x2_mega_sprite.position = (SCREEN_WIDTH * 0.65, SCREEN_HEIGHT * 0.745, 0)
            self.sprite.append(self.x2_mega_sprite)
        if 1 in play_with_cart:
            self.play_with_cart_mega_sprite = pyglet.sprite.Sprite(self.play_with_cart_img, batch=self.batch,
                                                                   group=self.group)
            self.play_with_cart_mega_sprite.position = (SCREEN_WIDTH * 0.02, SCREEN_HEIGHT * 0.715, 0)
            self.sprite.append(self.play_with_cart_mega_sprite)

        if 2 in runner:
            self.runner_grand_sprite = pyglet.sprite.Sprite(self.runner_img, batch=self.batch, group=self.group)
            self.runner_grand_sprite.position = (SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.335, 0)
            self.sprite.append(self.runner_grand_sprite)
        if 2 in x2:
            self.x2_grand_sprite = pyglet.sprite.Sprite(self.x2_img, batch=self.batch, group=self.group)
            self.x2_grand_sprite.position = (SCREEN_WIDTH * 0.63, SCREEN_HEIGHT * 0.48, 0)
            self.sprite.append(self.x2_grand_sprite)
        if 2 in play_with_cart:
            self.play_with_cart_grand_sprite = pyglet.sprite.Sprite(self.play_with_cart_img, batch=self.batch,
                                                                    group=self.group)
            self.play_with_cart_grand_sprite.position = (SCREEN_WIDTH * 0.13, SCREEN_HEIGHT * 0.45, 0)
            self.sprite.append(self.play_with_cart_grand_sprite)

        if 3 in runner:
            self.runner_major_sprite = pyglet.sprite.Sprite(self.runner_img, batch=self.batch, group=self.group)
            self.runner_major_sprite.position = (SCREEN_WIDTH * 0.43, SCREEN_HEIGHT * 0.06, 0)
            self.sprite.append(self.runner_major_sprite)
        if 3 in x2:
            self.x2_major_sprite = pyglet.sprite.Sprite(self.x2_img, batch=self.batch, group=self.group)
            self.x2_major_sprite.position = (SCREEN_WIDTH * 0.335, SCREEN_HEIGHT * 0.208, 0)
            self.sprite.append(self.x2_major_sprite)
        if 3 in play_with_cart:
            self.play_with_cart_major_sprite = pyglet.sprite.Sprite(self.play_with_cart_img, batch=self.batch,
                                                                    group=self.group)
            self.play_with_cart_major_sprite.position = (SCREEN_WIDTH * 0.0001, SCREEN_HEIGHT * 0.18, 0)
            self.sprite.append(self.play_with_cart_major_sprite)

        if 4 in runner:
            self.runner_minor_sprite = pyglet.sprite.Sprite(self.runner_img, batch=self.batch, group=self.group)
            self.runner_minor_sprite.position = (SCREEN_WIDTH * 0.932, SCREEN_HEIGHT * 0.06, 0)
            self.sprite.append(self.runner_minor_sprite)
        if 4 in x2:
            self.x2_minor_sprite = pyglet.sprite.Sprite(self.x2_img, batch=self.batch, group=self.group)
            self.x2_minor_sprite.position = (SCREEN_WIDTH * 0.835, SCREEN_HEIGHT * 0.208, 0)
            self.sprite.append(self.x2_minor_sprite)
        if 4 in play_with_cart:
            self.play_with_cart_minor_sprite = pyglet.sprite.Sprite(self.play_with_cart_img, batch=self.batch,
                                                                   group=self.group)
            self.play_with_cart_minor_sprite.position = (SCREEN_WIDTH * 0.495, SCREEN_HEIGHT * 0.18, 0)
            self.sprite.append(self.play_with_cart_minor_sprite)

    def five_show(self, x2=[], runner=[], play_with_cart=[]):
        if 1 in runner:
            self.runner_mega_sprite = pyglet.sprite.Sprite(self.runner_img, batch=self.batch, group=self.group)
            self.runner_mega_sprite.position = (SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.60, 0)
            self.sprite.append(self.runner_mega_sprite)
        if 1 in x2:
            self.x2_mega_sprite = pyglet.sprite.Sprite(self.x2_img, batch=self.batch, group=self.group)
            self.x2_mega_sprite.position = (SCREEN_WIDTH * 0.65, SCREEN_HEIGHT * 0.745, 0)
            self.sprite.append(self.x2_mega_sprite)
        if 1 in play_with_cart:
            self.play_with_cart_mega_sprite = pyglet.sprite.Sprite(self.play_with_cart_img, batch=self.batch,
                                                                   group=self.group)
            self.play_with_cart_mega_sprite.position = (SCREEN_WIDTH * 0.02, SCREEN_HEIGHT * 0.715, 0)
            self.sprite.append(self.play_with_cart_mega_sprite)

        if 2 in runner:
            self.runner_grand_sprite = pyglet.sprite.Sprite(self.runner_img, batch=self.batch, group=self.group)
            self.runner_grand_sprite.position = (SCREEN_WIDTH * 0.43, SCREEN_HEIGHT * 0.33, 0)
            self.sprite.append(self.runner_grand_sprite)
        if 2 in x2:
            self.x2_grand_sprite = pyglet.sprite.Sprite(self.x2_img, batch=self.batch, group=self.group)
            self.x2_grand_sprite.position = (SCREEN_WIDTH * 0.34, SCREEN_HEIGHT * 0.48, 0)
            self.sprite.append(self.x2_grand_sprite)
        if 2 in play_with_cart:
            self.play_with_cart_grand_sprite = pyglet.sprite.Sprite(self.play_with_cart_img, batch=self.batch,
                                                                    group=self.group)
            self.play_with_cart_grand_sprite.position = (SCREEN_WIDTH * 0.0001, SCREEN_HEIGHT * 0.45, 0)
            self.sprite.append(self.play_with_cart_grand_sprite)

        if 3 in runner:
            self.runner_major_sprite = pyglet.sprite.Sprite(self.runner_img, batch=self.batch, group=self.group)
            self.runner_major_sprite.position = (SCREEN_WIDTH * 0.932, SCREEN_HEIGHT * 0.33, 0)
            self.sprite.append(self.runner_major_sprite)
        if 3 in x2:
            self.x2_major_sprite = pyglet.sprite.Sprite(self.x2_img, batch=self.batch, group=self.group)
            self.x2_major_sprite.position = (SCREEN_WIDTH * 0.845, SCREEN_HEIGHT * 0.48, 0)
            self.sprite.append(self.x2_major_sprite)
        if 3 in play_with_cart:
            self.play_with_cart_major_sprite = pyglet.sprite.Sprite(self.play_with_cart_img, batch=self.batch,
                                                                    group=self.group)
            self.play_with_cart_major_sprite.position = (SCREEN_WIDTH * 0.495, SCREEN_HEIGHT * 0.45, 0)
            self.sprite.append(self.play_with_cart_major_sprite)

        if 4 in runner:
            self.runner_minor_sprite = pyglet.sprite.Sprite(self.runner_img, batch=self.batch, group=self.group)
            self.runner_minor_sprite.position = (SCREEN_WIDTH * 0.43, SCREEN_HEIGHT * 0.06, 0)
            self.sprite.append(self.runner_minor_sprite)
        if 4 in x2:
            self.x2_minor_sprite = pyglet.sprite.Sprite(self.x2_img, batch=self.batch, group=self.group)
            self.x2_minor_sprite.position = (SCREEN_WIDTH * 0.335, SCREEN_HEIGHT * 0.208, 0)
            self.sprite.append(self.x2_minor_sprite)
        if 4 in play_with_cart:
            self.play_with_cart_minor_sprite = pyglet.sprite.Sprite(self.play_with_cart_img, batch=self.batch,
                                                                    group=self.group)
            self.play_with_cart_minor_sprite.position = (SCREEN_WIDTH * 0.0001, SCREEN_HEIGHT * 0.18, 0)
            self.sprite.append(self.play_with_cart_minor_sprite)

        if 5 in runner:
            self.runner_mini_sprite = pyglet.sprite.Sprite(self.runner_img, batch=self.batch, group=self.group)
            self.runner_mini_sprite.position = (SCREEN_WIDTH * 0.932, SCREEN_HEIGHT * 0.06, 0)
            self.sprite.append(self.runner_mini_sprite)
        if 5 in x2:
            self.x2_mini_sprite = pyglet.sprite.Sprite(self.x2_img, batch=self.batch, group=self.group)
            self.x2_mini_sprite.position = (SCREEN_WIDTH * 0.82, SCREEN_HEIGHT * 0.208, 0)
            self.sprite.append(self.x2_mini_sprite)
        if 5 in play_with_cart:
            self.play_with_cart_mini_sprite = pyglet.sprite.Sprite(self.play_with_cart_img, batch=self.batch,
                                                                    group=self.group)
            self.play_with_cart_mini_sprite.position = (SCREEN_WIDTH * 0.495, SCREEN_HEIGHT * 0.18, 0)
            self.sprite.append(self.play_with_cart_mini_sprite)


class Field():
    def __init__(self):
        global field
        global field_logo
        self.batch = resources.FIELD_BATCH
        self.field_count = 0
        self.group = resources.FIELD_GROUP
        self.micro = config.VISUAL_MICRO

        self.mega_activ = False
        self.mega = resources.FIELD['mega_anime']

        self.anime_mega = pyglet.image.Animation.from_image_sequence(self.mega, duration=0.05, loop=True)
        self.image_mega = resources.FIELD['mega']
        # for i in self.mega:
        #     i.width = int(SCREEN_WIDTH * 0.85)
        #     i.height = int(SCREEN_HEIGHT * 0.6)
        # self.image_mega.width = int(SCREEN_WIDTH * 0.85)
        # self.image_mega.height = int(SCREEN_HEIGHT * 0.6)

        self.grand = resources.FIELD['grand_anime']
        self.grand_activ = False
        self.anime_grand = pyglet.image.Animation.from_image_sequence(self.grand, duration=0.05, loop=True)
        self.image_grand = resources.FIELD['grand']
        # for i in self.grand:
        #     i.width = int(SCREEN_WIDTH * 0.85)
        #     i.height = int(SCREEN_HEIGHT * 0.6)
        # self.image_grand.width = int(SCREEN_WIDTH * 0.85)
        # self.image_grand.height = int(SCREEN_HEIGHT * 0.6)

        self.major_activ = False
        self.major = resources.FIELD['major_anime']
        self.anime_major = pyglet.image.Animation.from_image_sequence(self.major, duration=0.05, loop=True)
        self.image_major = resources.FIELD['major']
        # for i in self.major:
        #     i.width = int(SCREEN_WIDTH * 0.85)
        #     i.height = int(SCREEN_HEIGHT * 0.6)
        # self.image_major.width = int(SCREEN_WIDTH * 0.85)
        # self.image_major.height = int(SCREEN_HEIGHT * 0.6)

        self.minor_activ = False
        self.minor = resources.FIELD['minor_anime']
        self.anime_minor = pyglet.image.Animation.from_image_sequence(self.minor, duration=0.05, loop=True)
        self.image_minor = resources.FIELD['minor']
        # for i in self.minor:
        #     i.width = int(SCREEN_WIDTH * 0.85)
        #     i.height = int(SCREEN_HEIGHT * 0.6)
        # self.image_minor.width = int(SCREEN_WIDTH * 0.85)
        # self.image_minor.height = int(SCREEN_HEIGHT * 0.6)

        # self.minor_activ = False
        # self.minor_5 = resources.FIELD['minor_anime_5']
        # self.anime_minor_5 = pyglet.image.Animation.from_image_sequence(self.minor_5, duration=0.05, loop=True)
        # self.image_minor_5 = resources.FIELD['minor_5']
        # for i in self.minor_5:
        #     i.width = int(SCREEN_WIDTH * 0.85)
        #     i.height = int(SCREEN_HEIGHT * 0.6)
        # self.image_minor_5.width = int(SCREEN_WIDTH * 0.85)
        # self.image_minor_5.height = int(SCREEN_HEIGHT * 0.6)

        self.mini_activ = False
        self.mini = resources.FIELD['mini_anime']
        self.anime_mini = pyglet.image.Animation.from_image_sequence(self.mini, duration=0.05, loop=True)
        self.image_mini = resources.FIELD['mini']

    def reset(self):
        try:
            self.mega_sprite.delete()
            self.mega_sprite = None
        except AttributeError:
            pass
        try:
            self.grand_sprite.delete()
            self.grand_sprite = None
        except AttributeError:
            pass
        try:
            self.major_sprite.delete()
            self.major_sprite = None
        except AttributeError:
            pass
        try:
            self.minor_sprite.delete()
            self.minor_sprite = None
        except AttributeError:
            pass
        try:
            self.mini_sprite.delete()
            self.mini_sprite = None
        except AttributeError:
            pass

    def one_show(self):
        for i in self.mega:
            i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.11))
            i.height = int(SCREEN_HEIGHT * 0.66)
        self.image_mega.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
        self.image_mega.height = int(SCREEN_HEIGHT * 0.66)

        if self.mega_activ is True:
            self.mega_sprite = pyglet.sprite.Sprite(self.anime_mega, batch=self.batch, group=self.group)
            self.mega_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.355, 0)
        else:
            self.mega_sprite = pyglet.sprite.Sprite(self.image_mega, batch=self.batch, group=self.group)
            self.mega_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)

    def tow_show(self):
        for i in self.mega:
            i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.11))
            i.height = int(SCREEN_HEIGHT * 0.66)
        self.image_mega.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
        self.image_mega.height = int(SCREEN_HEIGHT * 0.66)
        for i in self.grand:
            i.width = int(SCREEN_WIDTH * 0.85)
            i.height = int(SCREEN_HEIGHT * 0.66)
        self.image_grand.width = int(SCREEN_WIDTH * 0.85)
        self.image_grand.height = int(SCREEN_HEIGHT * 0.66)

        if self.mega_activ is True:
            self.mega_sprite = pyglet.sprite.Sprite(self.anime_mega, batch=self.batch, group=self.group)
            self.mega_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.355, 0)
        else:
            self.mega_sprite = pyglet.sprite.Sprite(self.image_mega, batch=self.batch, group=self.group)
            self.mega_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)

        if self.grand_activ is True:
            self.grand_sprite = pyglet.sprite.Sprite(self.anime_grand, batch=self.batch, group=self.group)
            self.grand_sprite.position = (SCREEN_WIDTH * 0.075, SCREEN_HEIGHT * 0.1, 0)
        else:
            self.grand_sprite = pyglet.sprite.Sprite(self.image_grand, batch=self.batch, group=self.group)
            self.grand_sprite.position = (SCREEN_WIDTH * 0.075, SCREEN_HEIGHT * 0.1, 0)

    def free_show(self):
        for i in self.mega:
            i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
            i.height = int(SCREEN_HEIGHT * 0.66)
        self.image_mega.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
        self.image_mega.height = int(SCREEN_HEIGHT * 0.66)
        for i in self.grand:
            i.width = int(SCREEN_WIDTH * 0.85)
            i.height = int(SCREEN_HEIGHT * 0.66)
        self.image_grand.width = int(SCREEN_WIDTH * 0.85)
        self.image_grand.height = int(SCREEN_HEIGHT * 0.66)
        for i in self.major:
            i.width = int(SCREEN_WIDTH * 0.7)
            i.height = int(SCREEN_HEIGHT * 0.66)
        self.image_major.width = int(SCREEN_WIDTH * 0.7)
        self.image_major.height = int(SCREEN_HEIGHT * 0.66)

        if self.mega_activ is True:
            self.mega_sprite = pyglet.sprite.Sprite(self.anime_mega, batch=self.batch, group=self.group)
            self.mega_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.355, 0)
        else:
            self.mega_sprite = pyglet.sprite.Sprite(self.image_mega, batch=self.batch, group=self.group)
            self.mega_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)

        if self.grand_activ is True:
            self.grand_sprite = pyglet.sprite.Sprite(self.anime_grand, batch=self.batch, group=self.group)
            self.grand_sprite.position = (SCREEN_WIDTH * 0.075, SCREEN_HEIGHT * 0.1, 0)
        else:
            self.grand_sprite = pyglet.sprite.Sprite(self.image_grand, batch=self.batch, group=self.group)
            self.grand_sprite.position = (SCREEN_WIDTH * 0.075, SCREEN_HEIGHT * 0.1, 0)

        if self.major_activ is True:
            self.major_sprite = pyglet.sprite.Sprite(self.anime_major, batch=self.batch, group=self.group)
            self.major_sprite.position = (SCREEN_WIDTH * 0.14, SCREEN_HEIGHT - (SCREEN_HEIGHT * 1.17), 0)
        else:
            self.major_sprite = pyglet.sprite.Sprite(self.image_major, batch=self.batch, group=self.group)
            self.major_sprite.position = (SCREEN_WIDTH * 0.14, SCREEN_HEIGHT - (SCREEN_HEIGHT * 1.17), 0)

    def for_show(self):
        for i in self.mega:
            i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
            i.height = int(SCREEN_HEIGHT * 0.66)
        self.image_mega.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
        self.image_mega.height = int(SCREEN_HEIGHT * 0.66)
        for i in self.grand:
            i.width = int(SCREEN_WIDTH * 0.85)
            i.height = int(SCREEN_HEIGHT * 0.66)
        self.image_grand.width = int(SCREEN_WIDTH * 0.85)
        self.image_grand.height = int(SCREEN_HEIGHT * 0.66)
        for i in self.major:
            i.width = int(SCREEN_WIDTH * 0.57)
            i.height = int(SCREEN_HEIGHT * 0.66)
        self.image_major.width = int(SCREEN_WIDTH * 0.57)
        self.image_major.height = int(SCREEN_HEIGHT * 0.66)
        for i in self.minor:
            i.width = int(SCREEN_WIDTH * 0.57)
            i.height = int(SCREEN_HEIGHT * 0.66)
        self.image_minor.width = int(SCREEN_WIDTH * 0.57)
        self.image_minor.height = int(SCREEN_HEIGHT * 0.66)

        if self.mega_activ is True:
            self.mega_sprite = pyglet.sprite.Sprite(self.anime_mega, batch=self.batch, group=self.group)
            self.mega_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.355, 0)
        else:
            self.mega_sprite = pyglet.sprite.Sprite(self.image_mega, batch=self.batch, group=self.group)
            self.mega_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)

        if self.grand_activ is True:
            self.grand_sprite = pyglet.sprite.Sprite(self.anime_grand, batch=self.batch, group=self.group)
            self.grand_sprite.position = (SCREEN_WIDTH * 0.075, SCREEN_HEIGHT * 0.1, 0)
        else:
            self.grand_sprite = pyglet.sprite.Sprite(self.image_grand, batch=self.batch, group=self.group)
            self.grand_sprite.position = (SCREEN_WIDTH * 0.075, SCREEN_HEIGHT * 0.1, 0)

        if self.major_activ is True:
            self.major_sprite = pyglet.sprite.Sprite(self.anime_major, batch=self.batch, group=self.group)
            self.major_sprite.position = (SCREEN_WIDTH-(SCREEN_WIDTH * 1.035), SCREEN_HEIGHT - (SCREEN_HEIGHT * 1.17), 0)
        else:
            self.major_sprite = pyglet.sprite.Sprite(self.image_major, batch=self.batch, group=self.group)
            self.major_sprite.position = (SCREEN_WIDTH -(SCREEN_WIDTH * 1.035), SCREEN_HEIGHT - (SCREEN_HEIGHT * 1.17), 0)

        if self.minor_activ is True:
            self.minor_sprite = pyglet.sprite.Sprite(self.anime_minor, batch=self.batch, group=self.group)
            self.minor_sprite.position = (SCREEN_WIDTH * 0.465, SCREEN_HEIGHT - (SCREEN_HEIGHT * 1.17), 0)
        else:
            self.minor_sprite = pyglet.sprite.Sprite(self.image_minor, batch=self.batch, group=self.group)
            self.minor_sprite.position = (SCREEN_WIDTH * 0.465, SCREEN_HEIGHT - (SCREEN_HEIGHT * 1.17), 0)

    def five_show(self):
        for i in self.mega:
            i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
            i.height = int(SCREEN_HEIGHT * 0.66)
        self.image_mega.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
        self.image_mega.height = int(SCREEN_HEIGHT * 0.66)
        for i in self.grand:
            i.width = int(SCREEN_WIDTH * 0.57)
            i.height = int(SCREEN_HEIGHT * 0.66)
        self.image_grand.width = int(SCREEN_WIDTH * 0.57)
        self.image_grand.height = int(SCREEN_HEIGHT * 0.66)
        for i in self.major:
            i.width = int(SCREEN_WIDTH * 0.57)
            i.height = int(SCREEN_HEIGHT * 0.66)
        self.image_major.width = int(SCREEN_WIDTH * 0.57)
        self.image_major.height = int(SCREEN_HEIGHT * 0.66)
        for i in self.minor:
            i.width = int(SCREEN_WIDTH * 0.57)
            i.height = int(SCREEN_HEIGHT * 0.66)
        self.image_minor.width = int(SCREEN_WIDTH * 0.57)
        self.image_minor.height = int(SCREEN_HEIGHT * 0.66)

        for i in self.mini:
            i.width = int(SCREEN_WIDTH * 0.57)
            i.height = int(SCREEN_HEIGHT * 0.66)
        self.image_mini.width = int(SCREEN_WIDTH * 0.57)
        self.image_mini.height = int(SCREEN_HEIGHT * 0.66)

        if self.mega_activ is True:
            self.mega_sprite = pyglet.sprite.Sprite(self.anime_mega, batch=self.batch, group=self.group)
            self.mega_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.355, 0)
        else:
            self.mega_sprite = pyglet.sprite.Sprite(self.image_mega, batch=self.batch, group=self.group)
            self.mega_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)

        if self.grand_activ is True:
            self.grand_sprite = pyglet.sprite.Sprite(self.anime_grand, batch=self.batch, group=self.group)
            self.grand_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.035), SCREEN_HEIGHT * 0.1, 0)
        else:
            self.grand_sprite = pyglet.sprite.Sprite(self.image_grand, batch=self.batch, group=self.group)
            self.grand_sprite.position = (
                SCREEN_WIDTH - (SCREEN_WIDTH * 1.035), SCREEN_HEIGHT * 0.1, 0)

        if self.major_activ is True:
            self.major_sprite = pyglet.sprite.Sprite(self.anime_major, batch=self.batch, group=self.group)
            self.major_sprite.position = (SCREEN_WIDTH * 0.467, SCREEN_HEIGHT * 0.1, 0)
        else:
            self.major_sprite = pyglet.sprite.Sprite(self.image_major, batch=self.batch, group=self.group)
            self.major_sprite.position = (SCREEN_WIDTH * 0.467, SCREEN_HEIGHT * 0.1, 0)

        if self.minor_activ is True:
            self.minor_sprite = pyglet.sprite.Sprite(self.anime_minor, batch=self.batch, group=self.group)
            self.minor_sprite.position = (
            SCREEN_WIDTH-(SCREEN_WIDTH * 1.035), SCREEN_HEIGHT - (SCREEN_HEIGHT * 1.17), 0)
        else:
            self.minor_sprite = pyglet.sprite.Sprite(self.image_minor, batch=self.batch, group=self.group)
            self.minor_sprite.position = (
            SCREEN_WIDTH -(SCREEN_WIDTH * 1.035), SCREEN_HEIGHT - (SCREEN_HEIGHT * 1.17), 0)

        if self.mini_activ is True:
            self.mini_sprite = pyglet.sprite.Sprite(self.anime_mini, batch=self.batch, group=self.group)
            self.mini_sprite.position = (SCREEN_WIDTH * 0.465, SCREEN_HEIGHT - (SCREEN_HEIGHT * 1.17), 0)
        else:
            self.mini_sprite = pyglet.sprite.Sprite(self.image_mini, batch=self.batch, group=self.group)
            self.mini_sprite.position = (SCREEN_WIDTH * 0.465, SCREEN_HEIGHT - (SCREEN_HEIGHT * 1.17), 0)


# class Name():
#     def __init__(self):
#         self.group = resources.COUNT_GROUP
#         self.batch = resources.FIELD_BATCH
#
#         self.mega = resources.NAME['mega']
#         self.mega.width = int(SCREEN_WIDTH * 0.2)
#         self.mega.height = int(SCREEN_HEIGHT * 0.13)
#
#         self.grand = resources.NAME['grand']
#         self.grand.width = int(SCREEN_WIDTH * 0.2)
#         self.grand.height = int(SCREEN_HEIGHT * 0.10)
#
#         self.major = resources.NAME['major']
#         self.major.width = int(SCREEN_WIDTH * 0.2)
#         self.major.height = int(SCREEN_HEIGHT * 0.10)
#
#         self.minor = resources.NAME['minor']
#         self.minor.width = int(SCREEN_WIDTH * 0.2)
#         self.minor.height = int(SCREEN_HEIGHT * 0.10)
#
#         self.mini = resources.NAME['mini']
#         self.mini.width = int(SCREEN_WIDTH * 0.2)
#         self.mini.height = int(SCREEN_HEIGHT * 0.10)
#
#     def reset(self):
#         try:
#             self.mega_sprite.delete()
#         except AttributeError:
#             pass
#         try:
#             self.grand_sprite.delete()
#         except AttributeError:
#             pass
#         try:
#             self.major_sprite.delete()
#         except AttributeError:
#             pass
#         try:
#             self.minor_sprite.delete()
#         except AttributeError:
#             pass
#         try:
#             self.mini_sprite.delete()
#         except AttributeError:
#             pass
#
#     def one_show(self):
#         self.mega_sprite = pyglet.sprite.Sprite(self.mega, batch=self.batch, group=self.group)
#         self.mega_sprite.position = (SCREEN_WIDTH * 0.38, SCREEN_HEIGHT * 0.75, 0)
#
#     def tow_show(self):
#         self.mega_sprite = pyglet.sprite.Sprite(self.mega, batch=self.batch, group=self.group)
#         self.mega_sprite.position = (SCREEN_WIDTH * 0.39, SCREEN_HEIGHT * 0.75, 0)
#
#         self.grand_sprite = pyglet.sprite.Sprite(self.grand, batch=self.batch, group=self.group)
#         self.grand_sprite.position = (SCREEN_WIDTH * 0.39, SCREEN_HEIGHT * 0.5, 0)
#
#     def free_show(self):
#         self.mega_sprite = pyglet.sprite.Sprite(self.mega, batch=self.batch, group=self.group)
#         self.mega_sprite.position = (SCREEN_WIDTH * 0.39, SCREEN_HEIGHT * 0.75, 0)
#
#         self.grand_sprite = pyglet.sprite.Sprite(self.grand, batch=self.batch, group=self.group)
#         self.grand_sprite.position = (SCREEN_WIDTH * 0.39, SCREEN_HEIGHT * 0.53, 0)
#
#         self.major_sprite = pyglet.sprite.Sprite(self.major, batch=self.batch, group=self.group)
#         self.major_sprite.position = (SCREEN_WIDTH * 0.39, SCREEN_HEIGHT * 0.295, 0)
#
#     def for_show(self):
#         self.mega_sprite = pyglet.sprite.Sprite(self.mega, batch=self.batch, group=self.group)
#         self.mega_sprite.position = (SCREEN_WIDTH * 0.39, SCREEN_HEIGHT * 0.79, 0)
#
#         self.grand_sprite = pyglet.sprite.Sprite(self.grand, batch=self.batch, group=self.group)
#         self.grand_sprite.position = (SCREEN_WIDTH * 0.39, SCREEN_HEIGHT * 0.58, 0)
#
#         self.major_sprite = pyglet.sprite.Sprite(self.major, batch=self.batch, group=self.group)
#         self.major_sprite.position = (SCREEN_WIDTH * 0.39, SCREEN_HEIGHT * 0.35, 0)
#
#         self.minor_sprite = pyglet.sprite.Sprite(self.minor, batch=self.batch, group=self.group)
#         self.minor_sprite.position = (SCREEN_WIDTH * 0.4, SCREEN_HEIGHT * 0.165, 0)
#
#     def five_show(self):
#         self.mega_sprite = pyglet.sprite.Sprite(self.mega, batch=self.batch, group=self.group)
#         self.mega_sprite.position = (SCREEN_WIDTH * 0.39, SCREEN_HEIGHT * 0.79, 0)
#
#         self.grand_sprite = pyglet.sprite.Sprite(self.grand, batch=self.batch, group=self.group)
#         self.grand_sprite.position = (SCREEN_WIDTH * 0.39, SCREEN_HEIGHT * 0.58, 0)
#
#         self.major_sprite = pyglet.sprite.Sprite(self.major, batch=self.batch, group=self.group)
#         self.major_sprite.position = (SCREEN_WIDTH * 0.39, SCREEN_HEIGHT * 0.35, 0)
#
#         self.minor_sprite = pyglet.sprite.Sprite(self.minor, batch=self.batch, group=self.group)
#         self.minor_sprite.position = (SCREEN_WIDTH * 0.185, SCREEN_HEIGHT * 0.165, 0)
#
#         self.mini_sprite = pyglet.sprite.Sprite(self.mini, batch=self.batch, group=self.group)
#         self.mini_sprite.position = (SCREEN_WIDTH * 0.625, SCREEN_HEIGHT * 0.165, 0)

class RangeAndBetField():
    def __init__(self, mony='BGN'):
        self.count_group = resources.COUNT_GROUP
        self.batch = resources.FIELD_BATCH
        self.valuta = mony
        self.mega_activ = False
        self.grand_activ = False
        self.major_activ = False
        self.minor_activ = False
        self.mini_activ = False

        self.bet = resources.BET
        self.bet.width = int(SCREEN_WIDTH * 0.06)
        self.bet.height = int(SCREEN_HEIGHT * 0.1)

        self.range = resources.RANGE
        self.range.width = int(SCREEN_WIDTH * 0.05)
        self.range.height = int(SCREEN_HEIGHT * 0.14)

        self.count = resources.BET_AND_RANGE_COUNTERS['counters']
        for i in self.count:
            i.width = int(SCREEN_WIDTH * 0.05)
            i.height = int(SCREEN_HEIGHT * 0.08)
        self.tire = resources.BET_AND_RANGE_COUNTERS['tire']
        self.tire.width = int(SCREEN_WIDTH * 0.06)
        self.tire.height = int(SCREEN_HEIGHT * 0.06)

        # self.zapetaia = resources.BET_AND_RANGE_COUNTERS['zapetaia']
        # self.zapetaia.width = int(SCREEN_WIDTH * 0.06)
        # self.zapetaia.height = int(SCREEN_HEIGHT * 0.06)

        self.point = resources.BET_AND_RANGE_COUNTERS['point']
        self.point.width = int(SCREEN_WIDTH * 0.04)
        self.point.height = int(SCREEN_HEIGHT * 0.06)

        if self.valuta == 'BGN':
            self.mony = resources.BGN
            self.mony.width = int(SCREEN_WIDTH * 0.028)
            self.mony.height = int(SCREEN_HEIGHT * 0.04)
        else:
            self.mony = resources.EU
            self.mony.width = int(SCREEN_WIDTH * 0.02)
            self.mony.height = int(SCREEN_HEIGHT * 0.04)
        self.clock_img_red = resources.CLOCK_RED
        self.clock_img_red.width = int(SCREEN_WIDTH * 0.062)
        self.clock_img_red.height = int(SCREEN_HEIGHT * 0.08)
        self.clock_img_purple = resources.CLOCK_PURPLE
        self.clock_img_purple.width = int(SCREEN_WIDTH * 0.062)
        self.clock_img_purple.height = int(SCREEN_HEIGHT * 0.08)
        self.clock_img_yellow = resources.CLOCK_YELLOW
        self.clock_img_yellow.width = int(SCREEN_WIDTH * 0.062)
        self.clock_img_yellow.height = int(SCREEN_HEIGHT * 0.08)
        self.clock_img_blue = resources.CLOCK_BLUE
        self.clock_img_blue.width = int(SCREEN_WIDTH * 0.062)
        self.clock_img_blue.height = int(SCREEN_HEIGHT * 0.08)
        self.clock_img_green = resources.CLOCK_GREEN
        self.clock_img_green.width = int(SCREEN_WIDTH * 0.062)
        self.clock_img_green.height = int(SCREEN_HEIGHT * 0.08)
        self.use_times = False

    def reset(self):
        # FIXME: Зачистване на спритове
        try:
            if self.use_times is True:
                self.mega_clock_sprite.delete()
                self.mega_clock_sprite = None
            self.mega_range_sprite.delete()
            self.mega_range_sprite = None
            self.mega_bet_sprite.delete()
            self.mega_bet_sprite = None
            self.mega_mony_sprite.delete()
            self.mega_mony_sprite = None
            for i in self.mega_counters_sprite:
                i.delete()
            self.mega_counters_sprite = []
            for i in self.mega_bet_counters_sprite:
                i.delete()
            self.mega_bet_counters_sprite = []
        except AttributeError as e:
            pass
        try:
            if self.use_times is True:
                self.grand_clock_sprite.delete()
                self.grand_clock_sprite = None
            self.grand_range_sprite.delete()
            self.grand_range_sprite = None
            self.grand_bet_sprite.delete()
            self.grand_bet_sprite = None
            self.grand_mony_sprite.delete()
            self.grand_mony_sprite = None
            for i in self.grand_counters_sprite:
                i.delete()
            self.grand_counters_sprite = []
            for i in self.grand_bet_counters_sprite:
                i.delete()
            self.grand_bet_counters_sprite = []
        except AttributeError as e:
            pass
        try:
            if self.use_times is True:
                self.major_clock_sprite.delete()
                self.major_clock_sprite = None
            self.major_range_sprite.delete()
            self.major_range_sprite = None
            self.major_bet_sprite.delete()
            self.major_bet_sprite = None
            self.major_mony_sprite.delete()
            self.major_mony_sprite = None
            for i in self.major_counters_sprite:
                i.delete()
            self.major_counters_sprite = []
            for i in self.major_bet_counters_sprite:
                i.delete()
            self.major_bet_counters_sprite = []
        except AttributeError as e:
            pass
        try:
            if self.use_times is True:
                self.minor_clock_sprite.delete()
                self.minor_clock_sprite = None
            self.minor_range_sprite.delete()
            self.minor_range_sprite = None
            self.minor_bet_sprite.delete()
            self.minor_bet_sprite = None
            self.minor_mony_sprite.delete()
            self.minor_mony_sprite = None
            for i in self.minor_counters_sprite:
                i.delete()
            self.minor_counters_sprite = []
            for i in self.minor_bet_counters_sprite:
                i.delete()
            self.minor_bet_counters_sprite = []
        except AttributeError:
            pass
        try:
            if self.use_times is True:
                self.mini_clock_sprite.delete()
                self.mini_clock_sprite = None
            self.mini_range_sprite.delete()
            self.mini_range_sprite = None
            self.mini_bet_sprite.delete()
            self.mini_bet_sprite = None
            self.mini_mony_sprite.delete()
            self.mini_mony_sprite = None
            for i in self.mini_counters_sprite:
                i.delete()
            self.mini_counters_sprite = []
            for i in self.mini_bet_counters_sprite:
                i.delete()
            self.mini_bet_counters_sprite = []
        except AttributeError:
            pass

    def one_show(self, ranges=[], bet=[]):
        # ===============================================================================================================
        # MEGA
        # ===============================================================================================================
        self.mega_mony_sprite = pyglet.sprite.Sprite(self.mony, batch=self.batch, group=self.count_group)
        self.mega_bet_sprite = pyglet.sprite.Sprite(self.bet, batch=self.batch, group=self.count_group)
        self.mega_range_sprite = pyglet.sprite.Sprite(self.range, batch=self.batch, group=self.count_group)
        self.mega_counters_sprite = []
        self.mega_bet_counters_sprite = []
        for i in "{:.2f}".format(bet[0]):
            if i == '.':
                self.mega_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.point, batch=self.batch, group=self.count_group))
            else:
                self.mega_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[0]['from']):
            self.mega_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.mega_counters_sprite.append(pyglet.sprite.Sprite(self.tire, batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[0]['to']):
            self.mega_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.mega_mony_sprite.position = (SCREEN_WIDTH * 0.93, SCREEN_HEIGHT * 0.69, 0)
        self.mega_range_sprite.position = (SCREEN_WIDTH * 0.24, SCREEN_HEIGHT * 0.538, 0)
        gradient = 1.045
        width = SCREEN_WIDTH * 0.28
        for i in self.mega_counters_sprite:
            if i.image is self.tire:
                width = width * 0.99
                i.position = (width, SCREEN_HEIGHT * 0.578, 0)
                width = width * 1.02
                gradient = gradient - 0.008
            else:
                i.position = (width, SCREEN_HEIGHT * 0.566, 0)
            width = width * gradient
        lens = 0.66
        bet_lens = 0.829
        if len(self.mega_bet_counters_sprite) == 7:
            pass
        elif len(self.mega_bet_counters_sprite) == 6:
            lens += 0.012
            bet_lens = 0.845
        elif len(self.mega_bet_counters_sprite) == 5:
            lens += 0.024
            bet_lens = 0.862
        elif len(self.mega_bet_counters_sprite) == 4:
            lens += 0.035
            bet_lens = 0.875
        width = SCREEN_WIDTH * lens
        gradient = 1.02
        point = False
        for i in self.mega_bet_counters_sprite:
            if i.image is not self.point:
                i.position = (width, SCREEN_HEIGHT * 0.566, 0)
                if point == True:
                    point = False
                    gradient = 1.02
                width = width * gradient
            else:
                point = True
                i.position = (width * 1.004, SCREEN_HEIGHT * 0.565, 0)
                width = (width * 0.997) * 1.015
        self.mega_bet_sprite.position = (width * bet_lens, SCREEN_HEIGHT * 0.556, 0)
        if self.use_times is True:
            self.mega_clock_sprite = pyglet.sprite.Sprite(self.clock_img_red, batch=self.batch, group=self.count_group)
            self.mega_clock_sprite.position = (SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.64, 0)

    def tow_show(self, ranges=[], bet=[]):
        # ===============================================================================================================
        # MEGA
        # ===============================================================================================================
        self.mega_mony_sprite = pyglet.sprite.Sprite(self.mony, batch=self.batch, group=self.count_group)
        self.mega_bet_sprite = pyglet.sprite.Sprite(self.bet, batch=self.batch, group=self.count_group)
        self.mega_range_sprite = pyglet.sprite.Sprite(self.range, batch=self.batch, group=self.count_group)
        self.mega_counters_sprite = []
        self.mega_bet_counters_sprite = []
        for i in "{:.2f}".format(bet[0]):
            if i == '.':
                self.mega_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.point, batch=self.batch, group=self.count_group))
            else:
                self.mega_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[0]['from']):
            self.mega_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.mega_counters_sprite.append(pyglet.sprite.Sprite(self.tire, batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[0]['to']):
            self.mega_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.mega_mony_sprite.position = (SCREEN_WIDTH * 0.93, SCREEN_HEIGHT * 0.69, 0)
        self.mega_range_sprite.position = (SCREEN_WIDTH * 0.24, SCREEN_HEIGHT * 0.538, 0)
        gradient = 1.045
        width = SCREEN_WIDTH * 0.28
        for i in self.mega_counters_sprite:
            if i.image is self.tire:
                width = width * 0.99
                i.position = (width, SCREEN_HEIGHT * 0.578, 0)
                width = width * 1.02
                gradient = gradient - 0.008
            else:
                i.position = (width, SCREEN_HEIGHT * 0.566, 0)
            width = width * gradient
        lens = 0.66
        bet_lens = 0.829
        if len(self.mega_bet_counters_sprite) == 7:
            pass
        elif len(self.mega_bet_counters_sprite) == 6:
            lens += 0.012
            bet_lens = 0.845
        elif len(self.mega_bet_counters_sprite) == 5:
            lens += 0.024
            bet_lens = 0.862
        elif len(self.mega_bet_counters_sprite) == 4:
            lens += 0.035
            bet_lens = 0.875
        width = SCREEN_WIDTH * lens
        gradient = 1.02
        point = False
        for i in self.mega_bet_counters_sprite:
            if i.image is not self.point:
                i.position = (width, SCREEN_HEIGHT * 0.566, 0)
                if point == True:
                    point = False
                    gradient = 1.02
                width = width * gradient
            else:
                point = True
                i.position = (width * 1.004, SCREEN_HEIGHT * 0.565, 0)
                width = (width * 0.997) * 1.015
        self.mega_bet_sprite.position = (width * bet_lens, SCREEN_HEIGHT * 0.556, 0)
        if self.use_times is True:
            self.mega_clock_sprite = pyglet.sprite.Sprite(self.clock_img_red, batch=self.batch, group=self.count_group)
            self.mega_clock_sprite.position = (SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.64, 0)

        # ===============================================================================================================
        # GRAND
        # ===============================================================================================================
        self.grand_mony_sprite = pyglet.sprite.Sprite(self.mony, batch=self.batch, group=self.count_group)
        self.grand_bet_sprite = pyglet.sprite.Sprite(self.bet, batch=self.batch, group=self.count_group)
        self.grand_range_sprite = pyglet.sprite.Sprite(self.range, batch=self.batch, group=self.count_group)
        self.grand_counters_sprite = []
        self.grand_bet_counters_sprite = []
        for i in "{:.2f}".format(bet[1]):
            if i == '.':
                self.grand_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.point, batch=self.batch, group=self.count_group))
            else:
                self.grand_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[1]['from']):
            self.grand_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.grand_counters_sprite.append(pyglet.sprite.Sprite(self.tire, batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[1]['to']):
            self.grand_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.grand_mony_sprite.position = (SCREEN_WIDTH * 0.825, SCREEN_HEIGHT * 0.43, 0)
        self.grand_range_sprite.position = (SCREEN_WIDTH * 0.3, SCREEN_HEIGHT * 0.267, 0)
        gradient = 1.036
        width = SCREEN_WIDTH * 0.34
        for i in self.grand_counters_sprite:
            if i.image is self.tire:
                width = width * 0.99
                i.position = (width, SCREEN_HEIGHT * 0.305, 0)
                width = width * 1.02
                gradient = gradient - 0.0045
            else:
                i.position = (width, SCREEN_HEIGHT * 0.295, 0)
            width = width * gradient
        lens = 0.6
        bet_lens = 0.824
        if len(self.grand_bet_counters_sprite) == 7:
            pass
        elif len(self.grand_bet_counters_sprite) == 6:
            lens += 0.012
            bet_lens = 0.842
        elif len(self.grand_bet_counters_sprite) == 5:
            lens += 0.024
            bet_lens = 0.86
        elif len(self.grand_bet_counters_sprite) == 4:
            lens += 0.035
            bet_lens = 0.875
        width = SCREEN_WIDTH * lens
        gradient = 1.02
        point = False
        for i in self.grand_bet_counters_sprite:
            if i.image is not self.point:
                i.position = (width, SCREEN_HEIGHT * 0.295, 0)
                if point == True:
                    point = False
                    gradient = 1.02
                width = width * gradient
            else:
                point = True
                i.position = (width * 1.004, SCREEN_HEIGHT * 0.295, 0)
                width = (width * 0.997) * 1.015
        self.grand_bet_sprite.position = (width * bet_lens, SCREEN_HEIGHT * 0.285, 0)
        if self.use_times is True:
            self.grand_clock_sprite = pyglet.sprite.Sprite(self.clock_img_purple, batch=self.batch,
                                                           group=self.count_group)
            self.grand_clock_sprite.position = (SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.38, 0)

    def free_show(self, ranges=[], bet=[]):
        # ===============================================================================================================
        # MEGA
        # ===============================================================================================================
        self.mega_mony_sprite = pyglet.sprite.Sprite(self.mony, batch=self.batch, group=self.count_group)
        self.mega_bet_sprite = pyglet.sprite.Sprite(self.bet, batch=self.batch, group=self.count_group)
        self.mega_range_sprite = pyglet.sprite.Sprite(self.range, batch=self.batch, group=self.count_group)
        self.mega_counters_sprite = []
        self.mega_bet_counters_sprite = []
        for i in "{:.2f}".format(bet[0]):
            if i == '.':
                self.mega_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.point, batch=self.batch, group=self.count_group))
            else:
                self.mega_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[0]['from']):
            self.mega_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.mega_counters_sprite.append(pyglet.sprite.Sprite(self.tire, batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[0]['to']):
            self.mega_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.mega_mony_sprite.position = (SCREEN_WIDTH * 0.93, SCREEN_HEIGHT * 0.69, 0)
        self.mega_range_sprite.position = (SCREEN_WIDTH * 0.24, SCREEN_HEIGHT * 0.538, 0)
        gradient = 1.045
        width = SCREEN_WIDTH * 0.28
        for i in self.mega_counters_sprite:
            if i.image is self.tire:
                width = width * 0.99
                i.position = (width, SCREEN_HEIGHT * 0.578, 0)
                width = width * 1.02
                gradient = gradient - 0.008
            else:
                i.position = (width, SCREEN_HEIGHT * 0.566, 0)
            width = width * gradient
        lens = 0.66
        bet_lens = 0.829
        if len(self.mega_bet_counters_sprite) == 7:
            pass
        elif len(self.mega_bet_counters_sprite) == 6:
            lens += 0.012
            bet_lens = 0.845
        elif len(self.mega_bet_counters_sprite) == 5:
            lens += 0.024
            bet_lens = 0.862
        elif len(self.mega_bet_counters_sprite) == 4:
            lens += 0.035
            bet_lens = 0.875
        width = SCREEN_WIDTH * lens
        gradient = 1.02
        point = False
        for i in self.mega_bet_counters_sprite:
            if i.image is not self.point:
                i.position = (width, SCREEN_HEIGHT * 0.566, 0)
                if point == True:
                    point = False
                    gradient = 1.02
                width = width * gradient
            else:
                point = True
                i.position = (width * 1.004, SCREEN_HEIGHT * 0.565, 0)
                width = (width * 0.997) * 1.015
        self.mega_bet_sprite.position = (width * bet_lens, SCREEN_HEIGHT * 0.556, 0)
        if self.use_times is True:
            self.mega_clock_sprite = pyglet.sprite.Sprite(self.clock_img_red, batch=self.batch, group=self.count_group)
            self.mega_clock_sprite.position = (SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.64, 0)

        # ===============================================================================================================
        # GRAND
        # ===============================================================================================================
        self.grand_mony_sprite = pyglet.sprite.Sprite(self.mony, batch=self.batch, group=self.count_group)
        self.grand_bet_sprite = pyglet.sprite.Sprite(self.bet, batch=self.batch, group=self.count_group)
        self.grand_range_sprite = pyglet.sprite.Sprite(self.range, batch=self.batch, group=self.count_group)
        self.grand_counters_sprite = []
        self.grand_bet_counters_sprite = []
        for i in "{:.2f}".format(bet[1]):
            if i == '.':
                self.grand_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.point, batch=self.batch, group=self.count_group))
            else:
                self.grand_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[1]['from']):
            self.grand_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.grand_counters_sprite.append(pyglet.sprite.Sprite(self.tire, batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[1]['to']):
            self.grand_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.grand_mony_sprite.position = (SCREEN_WIDTH * 0.825, SCREEN_HEIGHT * 0.43, 0)
        self.grand_range_sprite.position = (SCREEN_WIDTH * 0.3, SCREEN_HEIGHT * 0.267, 0)
        gradient = 1.036
        width = SCREEN_WIDTH * 0.34
        for i in self.grand_counters_sprite:
            if i.image is self.tire:
                width = width * 0.99
                i.position = (width, SCREEN_HEIGHT * 0.305, 0)
                width = width * 1.02
                gradient = gradient - 0.0045
            else:
                i.position = (width, SCREEN_HEIGHT * 0.295, 0)
            width = width * gradient
        lens = 0.6
        bet_lens = 0.824
        if len(self.grand_bet_counters_sprite) == 7:
            pass
        elif len(self.grand_bet_counters_sprite) == 6:
            lens += 0.012
            bet_lens = 0.842
        elif len(self.grand_bet_counters_sprite) == 5:
            lens += 0.024
            bet_lens = 0.86
        elif len(self.grand_bet_counters_sprite) == 4:
            lens += 0.035
            bet_lens = 0.875
        width = SCREEN_WIDTH * lens
        gradient = 1.02
        point = False
        for i in self.grand_bet_counters_sprite:
            if i.image is not self.point:
                i.position = (width, SCREEN_HEIGHT * 0.295, 0)
                if point == True:
                    point = False
                    gradient = 1.02
                width = width * gradient
            else:
                point = True
                i.position = (width * 1.004, SCREEN_HEIGHT * 0.295, 0)
                width = (width * 0.997) * 1.015
        self.grand_bet_sprite.position = (width * bet_lens, SCREEN_HEIGHT * 0.285, 0)
        if self.use_times is True:
            self.grand_clock_sprite = pyglet.sprite.Sprite(self.clock_img_purple, batch=self.batch,
                                                           group=self.count_group)
            self.grand_clock_sprite.position = (SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.38, 0)
        # ===============================================================================================================
        # MAJOR
        # ===============================================================================================================
        self.major_mony_sprite = pyglet.sprite.Sprite(self.mony, batch=self.batch, group=self.count_group)
        self.major_bet_sprite = pyglet.sprite.Sprite(self.bet, batch=self.batch, group=self.count_group)
        self.major_range_sprite = pyglet.sprite.Sprite(self.range, batch=self.batch, group=self.count_group)
        self.major_counters_sprite = []
        self.major_bet_counters_sprite = []
        for i in "{:.2f}".format(bet[2]):
            if i == '.':
                self.major_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.point, batch=self.batch, group=self.count_group))
            else:
                self.major_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[2]['from']):
            self.major_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.major_counters_sprite.append(pyglet.sprite.Sprite(self.tire, batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[2]['to']):
            self.major_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.major_mony_sprite.position = (SCREEN_WIDTH * 0.75, SCREEN_HEIGHT * 0.163, 0)
        self.major_range_sprite.position = (SCREEN_WIDTH * 0.325, SCREEN_HEIGHT - (SCREEN_HEIGHT * 1.005), 0)
        gradient = 1.034
        width = SCREEN_WIDTH * 0.36
        for i in self.major_counters_sprite:
            if i.image is self.tire:
                width = width * 0.99
                i.position = (width, SCREEN_HEIGHT * 0.034, 0)
                width = width * 1.005
                # gradient = gradient - 0.0
            else:
                i.position = (width, SCREEN_HEIGHT * 0.024, 0)
            width = width * gradient
        lens = 0.555
        bet_lens = 0.822
        if len(self.major_bet_counters_sprite) == 7:
            pass
        elif len(self.major_bet_counters_sprite) == 6:
            lens += 0.012
            bet_lens = 0.84
        elif len(self.major_bet_counters_sprite) == 5:
            lens += 0.024
            bet_lens = 0.858
        elif len(self.major_bet_counters_sprite) == 4:
            lens += 0.035
            bet_lens = 0.87
        width = SCREEN_WIDTH * lens
        gradient = 1.025
        point = False
        for i in self.major_bet_counters_sprite:
            if i.image is not self.point:
                i.position = (width, SCREEN_HEIGHT * 0.024, 0)
                if point == True:
                    point = False
                    gradient = 1.023
                width = width * gradient
            else:
                point = True
                i.position = (width * 0.9999, SCREEN_HEIGHT * 0.024, 0)
                width = (width * 0.997) * 1.008
        self.major_bet_sprite.position = (width * bet_lens, SCREEN_HEIGHT * 0.015, 0)
        if self.use_times is True:
            self.major_clock_sprite = pyglet.sprite.Sprite(self.clock_img_yellow, batch=self.batch,
                                                           group=self.count_group)
            self.major_clock_sprite.position = (SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.14, 0)

    def for_show(self, ranges=[], bet=[]):
        # ===============================================================================================================
        # MEGA
        # ===============================================================================================================
        self.mega_mony_sprite = pyglet.sprite.Sprite(self.mony, batch=self.batch, group=self.count_group)
        self.mega_bet_sprite = pyglet.sprite.Sprite(self.bet, batch=self.batch, group=self.count_group)
        self.mega_range_sprite = pyglet.sprite.Sprite(self.range, batch=self.batch, group=self.count_group)
        self.mega_counters_sprite = []
        self.mega_bet_counters_sprite = []
        for i in "{:.2f}".format(bet[0]):
            if i == '.':
                self.mega_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.point, batch=self.batch, group=self.count_group))
            else:
                self.mega_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[0]['from']):
            self.mega_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.mega_counters_sprite.append(pyglet.sprite.Sprite(self.tire, batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[0]['to']):
            self.mega_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.mega_mony_sprite.position = (SCREEN_WIDTH * 0.93, SCREEN_HEIGHT * 0.69, 0)
        self.mega_range_sprite.position = (SCREEN_WIDTH * 0.24, SCREEN_HEIGHT * 0.538, 0)
        gradient = 1.045
        width = SCREEN_WIDTH * 0.28
        for i in self.mega_counters_sprite:
            if i.image is self.tire:
                width = width * 0.99
                i.position = (width, SCREEN_HEIGHT * 0.578, 0)
                width = width * 1.02
                gradient = gradient - 0.008
            else:
                i.position = (width, SCREEN_HEIGHT * 0.566, 0)
            width = width * gradient
        lens = 0.66
        bet_lens = 0.829
        if len(self.mega_bet_counters_sprite) == 7:
            pass
        elif len(self.mega_bet_counters_sprite) == 6:
            lens += 0.012
            bet_lens = 0.845
        elif len(self.mega_bet_counters_sprite) == 5:
            lens += 0.024
            bet_lens = 0.862
        elif len(self.mega_bet_counters_sprite) == 4:
            lens += 0.035
            bet_lens = 0.875
        width = SCREEN_WIDTH * lens
        gradient = 1.02
        point = False
        for i in self.mega_bet_counters_sprite:
            if i.image is not self.point:
                i.position = (width, SCREEN_HEIGHT * 0.566, 0)
                if point == True:
                    point = False
                    gradient = 1.02
                width = width * gradient
            else:
                point = True
                i.position = (width * 1.004, SCREEN_HEIGHT * 0.565, 0)
                width = (width * 0.997) * 1.015
        self.mega_bet_sprite.position = (width * bet_lens, SCREEN_HEIGHT * 0.556, 0)
        if self.use_times is True:
            self.mega_clock_sprite = pyglet.sprite.Sprite(self.clock_img_red, batch=self.batch, group=self.count_group)
            self.mega_clock_sprite.position = (SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.64, 0)

        # ===============================================================================================================
        # GRAND
        # ===============================================================================================================
        self.grand_mony_sprite = pyglet.sprite.Sprite(self.mony, batch=self.batch, group=self.count_group)
        self.grand_bet_sprite = pyglet.sprite.Sprite(self.bet, batch=self.batch, group=self.count_group)
        self.grand_range_sprite = pyglet.sprite.Sprite(self.range, batch=self.batch, group=self.count_group)
        self.grand_counters_sprite = []
        self.grand_bet_counters_sprite = []
        for i in "{:.2f}".format(bet[1]):
            if i == '.':
                self.grand_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.point, batch=self.batch, group=self.count_group))
            else:
                self.grand_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[1]['from']):
            self.grand_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.grand_counters_sprite.append(pyglet.sprite.Sprite(self.tire, batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[1]['to']):
            self.grand_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.grand_mony_sprite.position = (SCREEN_WIDTH * 0.825, SCREEN_HEIGHT * 0.43, 0)
        self.grand_range_sprite.position = (SCREEN_WIDTH * 0.3, SCREEN_HEIGHT * 0.267, 0)
        gradient = 1.036
        width = SCREEN_WIDTH * 0.34
        for i in self.grand_counters_sprite:
            if i.image is self.tire:
                width = width * 0.99
                i.position = (width, SCREEN_HEIGHT * 0.305, 0)
                width = width * 1.02
                gradient = gradient - 0.0045
            else:
                i.position = (width, SCREEN_HEIGHT * 0.295, 0)
            width = width * gradient
        lens = 0.6
        bet_lens = 0.824
        if len(self.grand_bet_counters_sprite) == 7:
            pass
        elif len(self.grand_bet_counters_sprite) == 6:
            lens += 0.012
            bet_lens = 0.842
        elif len(self.grand_bet_counters_sprite) == 5:
            lens += 0.024
            bet_lens = 0.86
        elif len(self.grand_bet_counters_sprite) == 4:
            lens += 0.035
            bet_lens = 0.875
        width = SCREEN_WIDTH * lens
        gradient = 1.02
        point = False
        for i in self.grand_bet_counters_sprite:
            if i.image is not self.point:
                i.position = (width, SCREEN_HEIGHT * 0.295, 0)
                if point == True:
                    point = False
                    gradient = 1.02
                width = width * gradient
            else:
                point = True
                i.position = (width * 1.004, SCREEN_HEIGHT * 0.295, 0)
                width = (width * 0.997) * 1.015
        self.grand_bet_sprite.position = (width * bet_lens, SCREEN_HEIGHT * 0.285, 0)
        if self.use_times is True:
            self.grand_clock_sprite = pyglet.sprite.Sprite(self.clock_img_purple, batch=self.batch,
                                                           group=self.count_group)
            self.grand_clock_sprite.position = (SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.38, 0)
        # ===============================================================================================================
        # MAJOR
        # ===============================================================================================================
        self.major_mony_sprite = pyglet.sprite.Sprite(self.mony, batch=self.batch, group=self.count_group)
        self.major_bet_sprite = pyglet.sprite.Sprite(self.bet, batch=self.batch, group=self.count_group)
        self.major_range_sprite = pyglet.sprite.Sprite(self.range, batch=self.batch, group=self.count_group)
        self.major_counters_sprite = []
        self.major_bet_counters_sprite = []
        for i in "{:.2f}".format(bet[2]):
            if i == '.':
                self.major_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.point, batch=self.batch, group=self.count_group))
            else:
                self.major_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[2]['from']):
            self.major_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.major_counters_sprite.append(pyglet.sprite.Sprite(self.tire, batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[2]['to']):
            self.major_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.major_mony_sprite.position = (SCREEN_WIDTH * 0.46, SCREEN_HEIGHT * 0.16, 0)
        self.major_range_sprite.position = (SCREEN_WIDTH * 0.11, SCREEN_HEIGHT - (SCREEN_HEIGHT * 1.005), 0)
        gradient = 1.08
        width = SCREEN_WIDTH * 0.145
        for i in self.major_counters_sprite:
            if i.image is self.tire:
                width = width * 0.97
                i.position = (width, SCREEN_HEIGHT * 0.034, 0)
                width = width * 1.03
                gradient = gradient - 0.018
            else:
                i.position = (width, SCREEN_HEIGHT * 0.024, 0)
            width = width * gradient
        lens = 0.294
        bet_lens = 0.69
        if len(self.major_bet_counters_sprite) == 7:
            pass
        elif len(self.major_bet_counters_sprite) == 6:
            lens += 0.012
            bet_lens = 0.72
        elif len(self.major_bet_counters_sprite) == 5:
            lens += 0.024
            bet_lens = 0.75
        elif len(self.major_bet_counters_sprite) == 4:
            lens += 0.035
            bet_lens = 0.775
        width = SCREEN_WIDTH * lens
        gradient = 1.04
        point = False
        for i in self.major_bet_counters_sprite:
            if i.image is not self.point:
                i.position = (width, SCREEN_HEIGHT * 0.024, 0)
                if point == True:
                    point = False
                    gradient = 1.038
                width = width * gradient
            else:
                point = True
                i.position = (width * 1.001, SCREEN_HEIGHT * 0.024, 0)
                width = (width * 0.997) * 1.015
        self.major_bet_sprite.position = (width * bet_lens, SCREEN_HEIGHT * 0.015, 0)
        if self.use_times is True:
            self.major_clock_sprite = pyglet.sprite.Sprite(self.clock_img_blue, batch=self.batch,
                                                           group=self.count_group)
            self.major_clock_sprite.position = (SCREEN_WIDTH * 0.015, SCREEN_HEIGHT * 0.1, 0)

        # ===============================================================================================================
        # MINOR
        # ===============================================================================================================
        self.minor_mony_sprite = pyglet.sprite.Sprite(self.mony, batch=self.batch, group=self.count_group)
        self.minor_bet_sprite = pyglet.sprite.Sprite(self.bet, batch=self.batch, group=self.count_group)
        self.minor_range_sprite = pyglet.sprite.Sprite(self.range, batch=self.batch, group=self.count_group)
        self.minor_counters_sprite = []
        self.minor_bet_counters_sprite = []
        for i in "{:.2f}".format(bet[3]):
            if i == '.':
                self.minor_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.point, batch=self.batch, group=self.count_group))
            else:
                self.minor_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[3]['from']):
            self.minor_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.minor_counters_sprite.append(pyglet.sprite.Sprite(self.tire, batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[3]['to']):
            self.minor_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.minor_mony_sprite.position = (SCREEN_WIDTH * 0.96, SCREEN_HEIGHT * 0.16, 0)
        self.minor_range_sprite.position = (SCREEN_WIDTH * 0.612, SCREEN_HEIGHT - (SCREEN_HEIGHT * 1.005), 0)
        gradient = 1.02
        width = SCREEN_WIDTH * 0.648
        for i in self.minor_counters_sprite:
            if i.image is self.tire:
                width = width * 0.99
                i.position = (width, SCREEN_HEIGHT * 0.034, 0)
                width = width * 1.005
                # gradient = gradient - 0.0
            else:
                i.position = (width, SCREEN_HEIGHT * 0.024, 0)
            width = width * gradient
        lens = 0.794
        bet_lens = 0.872
        if len(self.minor_bet_counters_sprite) == 7:
            pass
        elif len(self.minor_bet_counters_sprite) == 6:
            lens += 0.012
            bet_lens = 0.885
        elif len(self.minor_bet_counters_sprite) == 5:
            lens += 0.024
            bet_lens = 0.89
        elif len(self.minor_bet_counters_sprite) == 4:
            lens += 0.035
            bet_lens = 0.91
        width = SCREEN_WIDTH * lens
        gradient = 1.015
        point = False
        for i in self.minor_bet_counters_sprite:
            if i.image is not self.point:
                i.position = (width, SCREEN_HEIGHT * 0.024, 0)
                if point == True:
                    point = False
                    gradient = 1.015
                width = width * gradient
            else:
                point = True
                i.position = (width * 0.9999, SCREEN_HEIGHT * 0.024, 0)
                width = (width * 0.997) * 1.008
        self.minor_bet_sprite.position = (width * bet_lens, SCREEN_HEIGHT * 0.015, 0)
        if self.use_times is True:
            self.minor_clock_sprite = pyglet.sprite.Sprite(self.clock_img_green, batch=self.batch,
                                                          group=self.count_group)
            self.minor_clock_sprite.position = (SCREEN_WIDTH * 0.52, SCREEN_HEIGHT * 0.1, 0)

    def five_show(self, ranges=[], bet=[]):
        # ===============================================================================================================
        # MEGA
        # ===============================================================================================================
        self.mega_mony_sprite = pyglet.sprite.Sprite(self.mony, batch=self.batch, group=self.count_group)
        self.mega_bet_sprite = pyglet.sprite.Sprite(self.bet, batch=self.batch, group=self.count_group)
        self.mega_range_sprite = pyglet.sprite.Sprite(self.range, batch=self.batch, group=self.count_group)
        self.mega_counters_sprite = []
        self.mega_bet_counters_sprite = []
        for i in "{:.2f}".format(bet[0]):
            if i == '.':
                self.mega_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.point, batch=self.batch, group=self.count_group))
            else:
                self.mega_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[0]['from']):
            self.mega_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.mega_counters_sprite.append(pyglet.sprite.Sprite(self.tire, batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[0]['to']):
            self.mega_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.mega_mony_sprite.position = (SCREEN_WIDTH * 0.93, SCREEN_HEIGHT * 0.69, 0)
        self.mega_range_sprite.position = (SCREEN_WIDTH * 0.24, SCREEN_HEIGHT * 0.538, 0)
        gradient = 1.045
        width = SCREEN_WIDTH * 0.28
        for i in self.mega_counters_sprite:
            if i.image is self.tire:
                width = width * 0.99
                i.position = (width, SCREEN_HEIGHT * 0.578, 0)
                width = width * 1.02
                gradient = gradient - 0.008
            else:
                i.position = (width, SCREEN_HEIGHT * 0.566, 0)
            width = width * gradient
        lens = 0.66
        bet_lens = 0.829
        if len(self.mega_bet_counters_sprite) == 7:
            pass
        elif len(self.mega_bet_counters_sprite) == 6:
            lens += 0.012
            bet_lens = 0.845
        elif len(self.mega_bet_counters_sprite) == 5:
            lens += 0.024
            bet_lens = 0.862
        elif len(self.mega_bet_counters_sprite) == 4:
            lens += 0.035
            bet_lens = 0.875
        width = SCREEN_WIDTH * lens
        gradient = 1.02
        point = False
        for i in self.mega_bet_counters_sprite:
            if i.image is not self.point:
                i.position = (width, SCREEN_HEIGHT * 0.566, 0)
                if point == True:
                    point = False
                    gradient = 1.02
                width = width * gradient
            else:
                point = True
                i.position = (width * 1.004, SCREEN_HEIGHT * 0.565, 0)
                width = (width * 0.997) * 1.015
        self.mega_bet_sprite.position = (width * bet_lens, SCREEN_HEIGHT * 0.556, 0)
        if self.use_times is True:
            self.mega_clock_sprite = pyglet.sprite.Sprite(self.clock_img_red, batch=self.batch, group=self.count_group)
            self.mega_clock_sprite.position = (SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.64, 0)

        # ===============================================================================================================
        # GRAND
        # ===============================================================================================================
        self.grand_mony_sprite = pyglet.sprite.Sprite(self.mony, batch=self.batch, group=self.count_group)
        self.grand_bet_sprite = pyglet.sprite.Sprite(self.bet, batch=self.batch, group=self.count_group)
        self.grand_range_sprite = pyglet.sprite.Sprite(self.range, batch=self.batch, group=self.count_group)
        self.grand_counters_sprite = []
        self.grand_bet_counters_sprite = []
        for i in "{:.2f}".format(bet[1]):
            if i == '.':
                self.grand_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.point, batch=self.batch, group=self.count_group))
            else:
                self.grand_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[1]['from']):
            self.grand_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.grand_counters_sprite.append(pyglet.sprite.Sprite(self.tire, batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[1]['to']):
            self.grand_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.grand_mony_sprite.position = (SCREEN_WIDTH * 0.46, SCREEN_HEIGHT * 0.43, 0)
        self.grand_range_sprite.position = (SCREEN_WIDTH * 0.11, SCREEN_HEIGHT * 0.267, 0)
        gradient = 1.08
        width = SCREEN_WIDTH * 0.145
        for i in self.grand_counters_sprite:
            if i.image is self.tire:
                width = width * 0.97
                i.position = (width, SCREEN_HEIGHT * 0.307, 0)
                width = width * 1.02
                gradient = gradient - 0.018
            else:
                i.position = (width, SCREEN_HEIGHT * 0.295, 0)
            width = width * gradient
        lens = 0.295
        bet_lens = 0.69
        if len(self.grand_bet_counters_sprite) == 7:
            pass
        elif len(self.grand_bet_counters_sprite) == 6:
            lens += 0.012
            bet_lens = 0.72
        elif len(self.grand_bet_counters_sprite) == 5:
            lens += 0.024
            bet_lens = 0.75
        elif len(self.grand_bet_counters_sprite) == 4:
            lens += 0.035
            bet_lens = 0.775
        width = SCREEN_WIDTH * lens
        gradient = 1.04
        point = False
        for i in self.grand_bet_counters_sprite:
            if i.image is not self.point:
                i.position = (width, SCREEN_HEIGHT * 0.295, 0)
                if point == True:
                    point = False
                    gradient = 1.038
                width = width * gradient
            else:
                point = True
                i.position = (width * 1.001, SCREEN_HEIGHT * 0.295, 0)
                width = (width * 0.997) * 1.015
        self.grand_bet_sprite.position = (width * bet_lens, SCREEN_HEIGHT * 0.285, 0)
        if self.use_times is True:
            self.grand_clock_sprite = pyglet.sprite.Sprite(self.clock_img_purple, batch=self.batch,
                                                           group=self.count_group)
            self.grand_clock_sprite.position = (SCREEN_WIDTH * 0.015, SCREEN_HEIGHT * 0.37, 0)

        # ===============================================================================================================
        # MAJOR
        # ===============================================================================================================
        self.major_mony_sprite = pyglet.sprite.Sprite(self.mony, batch=self.batch, group=self.count_group)
        self.major_bet_sprite = pyglet.sprite.Sprite(self.bet, batch=self.batch, group=self.count_group)
        self.major_range_sprite = pyglet.sprite.Sprite(self.range, batch=self.batch, group=self.count_group)
        self.major_counters_sprite = []
        self.major_bet_counters_sprite = []
        for i in "{:.2f}".format(bet[2]):
            if i == '.':
                self.major_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.point, batch=self.batch, group=self.count_group))
            else:
                self.major_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[2]['from']):
            self.major_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.major_counters_sprite.append(pyglet.sprite.Sprite(self.tire, batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[2]['to']):
            self.major_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.major_mony_sprite.position = (SCREEN_WIDTH * 0.96, SCREEN_HEIGHT * 0.43, 0)
        self.major_range_sprite.position = (SCREEN_WIDTH * 0.612, SCREEN_HEIGHT * 0.267, 0)
        gradient = 1.02
        width = SCREEN_WIDTH * 0.648
        for i in self.major_counters_sprite:
            if i.image is self.tire:
                width = width * 0.99
                i.position = (width, SCREEN_HEIGHT * 0.307, 0)
                width = width * 1.005
                # gradient = gradient - 0.0
            else:
                i.position = (width, SCREEN_HEIGHT * 0.295, 0)
            width = width * gradient
        lens = 0.798
        bet_lens = 0.872
        if len(self.major_bet_counters_sprite) == 7:
            pass
        elif len(self.major_bet_counters_sprite) == 6:
            lens += 0.012
            bet_lens = 0.885
        elif len(self.major_bet_counters_sprite) == 5:
            lens += 0.024
            bet_lens = 0.89
        elif len(self.major_bet_counters_sprite) == 4:
            lens += 0.035
            bet_lens = 0.91
        width = SCREEN_WIDTH * lens
        gradient = 1.015
        point = False
        for i in self.major_bet_counters_sprite:
            if i.image is not self.point:
                i.position = (width, SCREEN_HEIGHT * 0.295, 0)
                if point == True:
                    point = False
                    gradient = 1.015
                width = width * gradient
            else:
                point = True
                i.position = (width * 0.9999, SCREEN_HEIGHT * 0.295, 0)
                width = (width * 0.997) * 1.008
        self.major_bet_sprite.position = (width * bet_lens, SCREEN_HEIGHT * 0.285, 0)
        if self.use_times is True:
            self.major_clock_sprite = pyglet.sprite.Sprite(self.clock_img_yellow, batch=self.batch,
                                                          group=self.count_group)
            self.major_clock_sprite.position = (SCREEN_WIDTH * 0.52, SCREEN_HEIGHT * 0.37, 0)

        # ===============================================================================================================
        # MINOR
        # ===============================================================================================================
        self.minor_mony_sprite = pyglet.sprite.Sprite(self.mony, batch=self.batch, group=self.count_group)
        self.minor_bet_sprite = pyglet.sprite.Sprite(self.bet, batch=self.batch, group=self.count_group)
        self.minor_range_sprite = pyglet.sprite.Sprite(self.range, batch=self.batch, group=self.count_group)
        self.minor_counters_sprite = []
        self.minor_bet_counters_sprite = []
        for i in "{:.2f}".format(bet[3]):
            if i == '.':
                self.minor_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.point, batch=self.batch, group=self.count_group))
            else:
                self.minor_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[3]['from']):
            self.minor_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.minor_counters_sprite.append(pyglet.sprite.Sprite(self.tire, batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[3]['to']):
            self.minor_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.minor_mony_sprite.position = (SCREEN_WIDTH * 0.46, SCREEN_HEIGHT * 0.16, 0)
        self.minor_range_sprite.position = (SCREEN_WIDTH * 0.11, SCREEN_HEIGHT - (SCREEN_HEIGHT * 1.005), 0)
        gradient = 1.08
        width = SCREEN_WIDTH * 0.145
        for i in self.minor_counters_sprite:
            if i.image is self.tire:
                width = width * 0.97
                i.position = (width, SCREEN_HEIGHT * 0.034, 0)
                width = width * 1.03
                gradient = gradient - 0.018
            else:
                i.position = (width, SCREEN_HEIGHT * 0.024, 0)
            width = width * gradient
        lens = 0.294
        bet_lens = 0.69
        if len(self.minor_bet_counters_sprite) == 7:
            pass
        elif len(self.minor_bet_counters_sprite) == 6:
            lens += 0.012
            bet_lens = 0.72
        elif len(self.minor_bet_counters_sprite) == 5:
            lens += 0.024
            bet_lens = 0.75
        elif len(self.minor_bet_counters_sprite) == 4:
            lens += 0.035
            bet_lens = 0.775
        width = SCREEN_WIDTH * lens
        gradient = 1.04
        point = False
        for i in self.minor_bet_counters_sprite:
            if i.image is not self.point:
                i.position = (width, SCREEN_HEIGHT * 0.024, 0)
                if point == True:
                    point = False
                    gradient = 1.038
                width = width * gradient
            else:
                point = True
                i.position = (width * 1.001, SCREEN_HEIGHT * 0.024, 0)
                width = (width * 0.997) * 1.015
        self.minor_bet_sprite.position = (width * bet_lens, SCREEN_HEIGHT * 0.015, 0)
        if self.use_times is True:
            self.minor_clock_sprite = pyglet.sprite.Sprite(self.clock_img_blue, batch=self.batch,
                                                           group=self.count_group)
            self.minor_clock_sprite.position = (SCREEN_WIDTH * 0.015, SCREEN_HEIGHT * 0.1, 0)

        # ===============================================================================================================
        # MINI
        # ===============================================================================================================
        self.mini_mony_sprite = pyglet.sprite.Sprite(self.mony, batch=self.batch, group=self.count_group)
        self.mini_bet_sprite = pyglet.sprite.Sprite(self.bet, batch=self.batch, group=self.count_group)
        self.mini_range_sprite = pyglet.sprite.Sprite(self.range, batch=self.batch, group=self.count_group)
        self.mini_counters_sprite = []
        self.mini_bet_counters_sprite = []
        for i in "{:.2f}".format(bet[4]):
            if i == '.':
                self.mini_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.point, batch=self.batch, group=self.count_group))
            else:
                self.mini_bet_counters_sprite.append(
                    pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[4]['from']):
            self.mini_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.mini_counters_sprite.append(pyglet.sprite.Sprite(self.tire, batch=self.batch, group=self.count_group))
        for i in "{:.0f}".format(ranges[4]['to']):
            self.mini_counters_sprite.append(
                pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
        self.mini_mony_sprite.position = (SCREEN_WIDTH * 0.96, SCREEN_HEIGHT * 0.16, 0)
        self.mini_range_sprite.position = (SCREEN_WIDTH * 0.612, SCREEN_HEIGHT - (SCREEN_HEIGHT * 1.005), 0)
        gradient = 1.02
        width = SCREEN_WIDTH * 0.648
        for i in self.mini_counters_sprite:
            if i.image is self.tire:
                width = width * 0.99
                i.position = (width, SCREEN_HEIGHT * 0.034, 0)
                width = width * 1.005
                # gradient = gradient - 0.0
            else:
                i.position = (width, SCREEN_HEIGHT * 0.024, 0)
            width = width * gradient
        lens = 0.794
        bet_lens = 0.872
        if len(self.mini_bet_counters_sprite) == 7:
            pass
        elif len(self.mini_bet_counters_sprite) == 6:
            lens += 0.012
            bet_lens = 0.885
        elif len(self.mini_bet_counters_sprite) == 5:
            lens += 0.024
            bet_lens = 0.89
        elif len(self.mini_bet_counters_sprite) == 4:
            lens += 0.035
            bet_lens = 0.91
        width = SCREEN_WIDTH * lens
        gradient = 1.015
        point = False
        for i in self.mini_bet_counters_sprite:
            if i.image is not self.point:
                i.position = (width, SCREEN_HEIGHT * 0.024, 0)
                if point == True:
                    point = False
                    gradient = 1.015
                width = width * gradient
            else:
                point = True
                i.position = (width * 0.9999, SCREEN_HEIGHT * 0.024, 0)
                width = (width * 0.997) * 1.008
        self.mini_bet_sprite.position = (width * bet_lens, SCREEN_HEIGHT * 0.015, 0)
        if self.use_times is True:
            self.mini_clock_sprite = pyglet.sprite.Sprite(self.clock_img_green, batch=self.batch,
                                                           group=self.count_group)
            self.mini_clock_sprite.position = (SCREEN_WIDTH * 0.52, SCREEN_HEIGHT * 0.1, 0)


class Main():
    def __init__(self):
        global BET_IN_FIELD
        self.count = 0
        self.field = Field()
        # self.BET_IN_FIELD = BET_IN_FIELD
        # if self.BET_IN_FIELD is True:
        self.ranges_field = RangeAndBetField()
        self.times = False
        self.stop_group = StopGroup()
        self.config = GroupConfig()
        # else:
        #     self.ranges_field = RangeAndBetOutField()
        # self.names = Name()
        self.last_activ = []
        self.ranges = []
        self.bet = []
        self.last_range_and_bet = []
        self.x2 = []
        self.runner = []
        self.play_with_cart = []
        self.my_time = time.time()

    def full_reset(self):
        self.field.reset()
        # self.ranges_field.reset()
        # self.names.reset()
        self.count = 0
        # self.field = Field()
        # self.BET_IN_FIELD = BET_IN_FIELD
        # if self.BET_IN_FIELD is True:
        self.ranges_field.reset()
        self.stop_group.reset()
        self.config.reset()
        self.times = False
        self.last_activ = []
        self.last_range_and_bet = []
        self.ranges = []
        self.bet = []
        self.my_time = time.time()

    def show(self, count=0, activ=[], times=False, ranges=[], bet=[], stop_group=False, x2=[], runner=[], play_with_cart=[]):
        if (self.last_activ != activ or self.count != count or self.times != times or ranges != self.ranges or
                bet != self.bet or self.x2 != x2 or self.runner != runner or self.play_with_cart != play_with_cart):
            self.last_activ = activ
            self.count = count
            self.times = times
            self.ranges = ranges
            self.bet = bet
            self.play_with_cart = play_with_cart
            self.runner = runner
            self.x2 = x2
            self.ranges_field.use_times = self.times
            self.ranges_field.reset()
            self.stop_group.reset()
            self.config.reset()
            self.field.reset()
            self.ranges_field.reset()
            if config.FIELF_ACTIVE is True:
                if 1 in activ:
                    self.field.mega_activ = True
                    self.ranges_field.mega_activ = True
                    self.config.mega_activ = True
                else:
                    self.field.mega_activ = True
                    self.ranges_field.mega_activ = False
                    self.config.mega_activ = False
                if 2 in activ:
                    self.field.grand_activ = True
                    self.ranges_field.grand_activ = True
                    self.config.grand_activ = True
                else:
                    self.field.grand_activ = True
                    self.ranges_field.grand_activ = False
                    self.config.grand_activ = False
                if 3 in activ:
                    self.field.major_activ = True
                    self.ranges_field.major_activ = True
                    self.config.major_activ = True
                else:
                    self.field.major_activ = True
                    self.ranges_field.major_activ = False
                    self.config.major_activ = False
                if 4 in activ:
                    self.field.minor_activ = True
                    self.ranges_field.minor_activ = True
                    self.config.minor_activ = True
                else:
                    self.field.minor_activ = True
                    self.ranges_field.minor_activ = False
                    self.config.minor_activ = False
                if 5 in activ:
                    self.field.mini_activ = True
                    self.ranges_field.mini_activ = True
                    self.config.mini_activ = True
                else:
                    self.field.mini_activ = True
                    self.ranges_field.mini_activ = False
                    self.config.mini_activ = False
            else:
                if 1 in activ:
                    self.field.mega_activ = False
                    self.ranges_field.mega_activ = True
                    self.config.mega_activ = True
                else:
                    self.field.mega_activ = False
                    self.ranges_field.mega_activ = False
                    self.config.mega_activ = False
                if 2 in activ:
                    self.field.grand_activ = False
                    self.ranges_field.grand_activ = True
                    self.config.grand_activ = True
                else:
                    self.field.grand_activ = False
                    self.ranges_field.grand_activ = False
                    self.config.grand_activ = False
                if 3 in activ:
                    self.field.major_activ = False
                    self.ranges_field.major_activ = True
                    self.config.major_activ = True
                else:
                    self.field.major_activ = False
                    self.ranges_field.major_activ = False
                    self.config.major_activ = False
                if 4 in activ:
                    self.field.minor_activ = False
                    self.ranges_field.minor_activ = True
                    self.config.minor_activ = True
                else:
                    self.field.minor_activ = False
                    self.ranges_field.minor_activ = False
                    self.config.minor_activ = False
                if 5 in activ:
                    self.field.mini_activ = False
                    self.ranges_field.mini_activ = True
                    self.config.mini_activ = True
                else:
                    self.field.mini_activ = False
                    self.ranges_field.mini_activ = False
                    self.config.mini_activ = False
            if count == 1:
                self.ranges_field.one_show(ranges, bet)
                self.field.one_show()
                self.config.one_show(x2, runner, play_with_cart)
            elif count == 2:
                self.field.tow_show()
                self.ranges_field.tow_show(ranges, bet)
                self.config.tow_show(x2, runner, play_with_cart)
            elif count == 3:
                self.ranges_field.free_show(ranges, bet)
                self.field.free_show()
                self.config.free_show(x2, runner, play_with_cart)
            elif count == 4:
                self.ranges_field.for_show(ranges, bet)
                self.field.for_show()
                self.config.for_show(x2, runner, play_with_cart)
            elif count == 5:
                self.ranges_field.five_show(ranges, bet)
                self.field.five_show()
                self.config.five_show(x2, runner, play_with_cart)
            else:
                pass
        if stop_group:
            self.stop_group.show()
        else:
            self.stop_group.reset()
        resources.FIELD_BATCH.draw()
        # print(self.field.anime_mega.frames[4].image == self.field.mega[4])
