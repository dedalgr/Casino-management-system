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

class Main():
    def __init__(self):
        # global background
        # global background_logo
        self.my_time = time.time()
        self.logo_grup = resources.BACKBROUND_LOGO_GROUP
        self.group = resources.BACKBROUND_GROUP
        self.batch = resources.BACKGROUND_BATCH
        self.logo = resources.LOGO
        self.logo.width = int(SCREEN_WIDTH*0.6)
        self.logo.height = int(SCREEN_HEIGHT*0.25)

        self.img = resources.BACKGROUND['anime']
        self.img.reverse()
        for i in self.img:
            i.width = int(SCREEN_WIDTH)
            i.height = int(SCREEN_HEIGHT)
        self.bkg = self.img[0]

        if config.BACKGROUND_ANIME == 1:
            self.img.append(self.img[0])
            self.anime = pyglet.image.Animation.from_image_sequence(self.img, duration=0.1, loop=False)
        elif config.BACKGROUND_ANIME == 0:
            self.logo_sprite = pyglet.sprite.Sprite(self.logo, batch=self.batch, group=self.logo_grup)
            self.logo_sprite.position = (SCREEN_WIDTH * 0.19, SCREEN_HEIGHT * 0.79, 0)
            self.anime = pyglet.image.Animation.from_image_sequence(self.img, duration=0.1, loop=False)
        elif config.BACKGROUND_ANIME == 5:
            # self.logo_sprite = pyglet.sprite.Sprite(self.logo, batch=self.batch, group=self.logo_grup)
            # self.logo_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.79, 0)
            self.anime = pyglet.image.Animation.from_image_sequence(self.img, duration=0.1, loop=True)
        else:
            self.logo_sprite = pyglet.sprite.Sprite(self.logo, batch=self.batch, group=self.logo_grup)
            self.logo_sprite.position = (SCREEN_WIDTH * 0.19, SCREEN_HEIGHT * 0.79, 0)
            self.anime = pyglet.image.Animation.from_image_sequence(self.img, duration=0.1, loop=True)
        self.play_anime()
        # self.board_img = []
        # for i in range(1, 19):
        #     self.board_img.append(pyglet.resource.image('img/background/board/image%s.png' % (i)))
        # for i in self.board_img:
        #     i.width = int(SCREEN_WIDTH)
        #     i.height = int(SCREEN_HEIGHT)
        # self.anime_board = pyglet.image.Animation.from_image_sequence(self.board_img, duration=0.3, loop=True)
        # self.sprite_board = pyglet.sprite.Sprite(self.anime_board, batch=self.batch, group=self.logo_grup)

    # def reset(self):
    #     try:
    #         self.sprite.delete()
    #     except AttributeError:
    #         pass

    # def pick_show(self):
    #     self.sprite = pyglet.sprite.Sprite(self.bkg, batch=self.batch, group=self.group)

    def play_anime(self):
        self.sprite = pyglet.sprite.Sprite(self.anime, batch=self.batch, group=self.group)

    def show(self):
        if self.my_time + 10 < time.time() and config.VISUAL_MICRO is False and config.BACKGROUND_ANIME == 1:
            # self.reset()
            self.play_anime()
            self.my_time = time.time()
        self.batch.draw()


