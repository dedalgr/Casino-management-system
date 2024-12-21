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

# class RangeAndBetField():
#     def __init__(self, mony='BGN'):
#         self.count_group = resources.COUNT_GROUP
#         self.batch = resources.FIELD_BATCH
#         self.valuta = mony
#         self.mega_activ = False
#         self.grand_activ = False
#         self.major_activ = False
#         self.minor_activ = False
#         self.mini_activ = False
#
#         self.bet = resources.BET
#         self.bet.width = int(SCREEN_WIDTH * 0.06)
#         self.bet.height = int(SCREEN_HEIGHT * 0.1)
#
#         self.range = resources.RANGE
#         self.range.width = int(SCREEN_WIDTH * 0.05)
#         self.range.height = int(SCREEN_HEIGHT * 0.14)
#
#         self.count = resources.BET_AND_RANGE_COUNTERS['counters']
#         for i in self.count:
#             i.width = int(SCREEN_WIDTH * 0.05)
#             i.height = int(SCREEN_HEIGHT * 0.08)
#         self.tire = resources.BET_AND_RANGE_COUNTERS['tire']
#         self.tire.width = int(SCREEN_WIDTH * 0.06)
#         self.tire.height = int(SCREEN_HEIGHT * 0.06)
#
#         # self.zapetaia = resources.BET_AND_RANGE_COUNTERS['zapetaia']
#         # self.zapetaia.width = int(SCREEN_WIDTH * 0.06)
#         # self.zapetaia.height = int(SCREEN_HEIGHT * 0.06)
#
#         self.point = resources.BET_AND_RANGE_COUNTERS['point']
#         self.point.width = int(SCREEN_WIDTH * 0.04)
#         self.point.height = int(SCREEN_HEIGHT * 0.06)
#
#         if self.valuta == 'BGN':
#             self.mony = resources.BGN
#             self.mony.width = int(SCREEN_WIDTH * 0.028)
#             self.mony.height = int(SCREEN_HEIGHT * 0.04)
#         else:
#             self.mony = resources.EU
#             self.mony.width = int(SCREEN_WIDTH * 0.02)
#             self.mony.height = int(SCREEN_HEIGHT * 0.04)
#         self.clock_img_red = resources.CLOCK_RED
#         self.clock_img_red.width = int(SCREEN_WIDTH * 0.062)
#         self.clock_img_red.height = int(SCREEN_HEIGHT * 0.08)
#         self.clock_img_purple = resources.CLOCK_PURPLE
#         self.clock_img_purple.width = int(SCREEN_WIDTH * 0.062)
#         self.clock_img_purple.height = int(SCREEN_HEIGHT * 0.08)
#         self.clock_img_yellow = resources.CLOCK_YELLOW
#         self.clock_img_yellow.width = int(SCREEN_WIDTH * 0.062)
#         self.clock_img_yellow.height = int(SCREEN_HEIGHT * 0.08)
#         self.clock_img_blue = resources.CLOCK_BLUE
#         self.clock_img_blue.width = int(SCREEN_WIDTH * 0.062)
#         self.clock_img_blue.height = int(SCREEN_HEIGHT * 0.08)
#         self.clock_img_green = resources.CLOCK_GREEN
#         self.clock_img_green.width = int(SCREEN_WIDTH * 0.062)
#         self.clock_img_green.height = int(SCREEN_HEIGHT * 0.08)
#         self.use_times = False
#
#     def reset(self):
#         # FIXME: Зачистване на спритове
#         try:
#             if self.use_times is True:
#                 self.mega_clock_sprite.delete()
#                 self.mega_clock_sprite = None
#             self.mega_range_sprite.delete()
#             self.mega_range_sprite = None
#             self.mega_bet_sprite.delete()
#             self.mega_bet_sprite = None
#             self.mega_mony_sprite.delete()
#             self.mega_mony_sprite = None
#             for i in self.mega_counters_sprite:
#                 i.delete()
#             self.mega_counters_sprite = []
#             for i in self.mega_bet_counters_sprite:
#                 i.delete()
#             self.mega_bet_counters_sprite = []
#         except AttributeError as e:
#             pass
#         try:
#             if self.use_times is True:
#                 self.grand_clock_sprite.delete()
#                 self.grand_clock_sprite = None
#             self.grand_range_sprite.delete()
#             self.grand_range_sprite = None
#             self.grand_bet_sprite.delete()
#             self.grand_bet_sprite = None
#             self.grand_mony_sprite.delete()
#             self.grand_mony_sprite = None
#             for i in self.grand_counters_sprite:
#                 i.delete()
#             self.grand_counters_sprite = []
#             for i in self.grand_bet_counters_sprite:
#                 i.delete()
#             self.grand_bet_counters_sprite = []
#         except AttributeError as e:
#             pass
#         try:
#             if self.use_times is True:
#                 self.major_clock_sprite.delete()
#                 self.major_clock_sprite = None
#             self.major_range_sprite.delete()
#             self.major_range_sprite = None
#             self.major_bet_sprite.delete()
#             self.major_bet_sprite = None
#             self.major_mony_sprite.delete()
#             self.major_mony_sprite = None
#             for i in self.major_counters_sprite:
#                 i.delete()
#             self.major_counters_sprite = []
#             for i in self.major_bet_counters_sprite:
#                 i.delete()
#             self.major_bet_counters_sprite = []
#         except AttributeError as e:
#             pass
#         try:
#             if self.use_times is True:
#                 self.minor_clock_sprite.delete()
#                 self.minor_clock_sprite = None
#             self.minor_range_sprite.delete()
#             self.minor_range_sprite = None
#             self.minor_bet_sprite.delete()
#             self.minor_bet_sprite = None
#             self.minor_mony_sprite.delete()
#             self.minor_mony_sprite = None
#             for i in self.minor_counters_sprite:
#                 i.delete()
#             self.minor_counters_sprite = []
#             for i in self.minor_bet_counters_sprite:
#                 i.delete()
#             self.minor_bet_counters_sprite = []
#         except AttributeError:
#             pass
#         try:
#             if self.use_times is True:
#                 self.mini_clock_sprite.delete()
#                 self.mini_clock_sprite = None
#             self.mini_range_sprite.delete()
#             self.mini_range_sprite = None
#             self.mini_bet_sprite.delete()
#             self.mini_bet_sprite = None
#             self.mini_mony_sprite.delete()
#             self.mini_mony_sprite = None
#             for i in self.mini_counters_sprite:
#                 i.delete()
#             self.mini_counters_sprite = []
#             for i in self.mini_bet_counters_sprite:
#                 i.delete()
#             self.mini_bet_counters_sprite = []
#         except AttributeError:
#             pass
#
#     def one_show(self, ranges=[], bet=[]):
#         # ===============================================================================================================
#         # MEGA
#         # ===============================================================================================================
#         self.mega_mony_sprite = pyglet.sprite.Sprite(self.mony, batch=self.batch, group=self.count_group)
#         self.mega_bet_sprite = pyglet.sprite.Sprite(self.bet, batch=self.batch, group=self.count_group)
#         self.mega_range_sprite = pyglet.sprite.Sprite(self.range, batch=self.batch, group=self.count_group)
#         self.mega_counters_sprite = []
#         self.mega_bet_counters_sprite = []
#         for i in "{:.2f}".format(bet[0]):
#             if i == '.':
#                 self.mega_bet_counters_sprite.append(
#                     pyglet.sprite.Sprite(self.point, batch=self.batch, group=self.count_group))
#             else:
#                 self.mega_bet_counters_sprite.append(
#                     pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
#         for i in "{:.0f}".format(ranges[0]['from']):
#             self.mega_counters_sprite.append(
#                 pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
#         self.mega_counters_sprite.append(pyglet.sprite.Sprite(self.tire, batch=self.batch, group=self.count_group))
#         for i in "{:.0f}".format(ranges[0]['to']):
#             self.mega_counters_sprite.append(
#                 pyglet.sprite.Sprite(self.count[int(i)], batch=self.batch, group=self.count_group))
#         self.mega_mony_sprite.position = (SCREEN_WIDTH * 0.93, SCREEN_HEIGHT * 0.69, 0)
#         self.mega_range_sprite.position = (SCREEN_WIDTH * 0.24, SCREEN_HEIGHT * 0.538, 0)
#         gradient = 1.045
#         width = SCREEN_WIDTH * 0.28
#         for i in self.mega_counters_sprite:
#             if i.image is self.tire:
#                 width = width * 0.99
#                 i.position = (width, SCREEN_HEIGHT * 0.578, 0)
#                 width = width * 1.02
#                 gradient = gradient - 0.008
#             else:
#                 i.position = (width, SCREEN_HEIGHT * 0.566, 0)
#             width = width * gradient
#         lens = 0.66
#         bet_lens = 0.829
#         if len(self.mega_bet_counters_sprite) == 7:
#             pass
#         elif len(self.mega_bet_counters_sprite) == 6:
#             lens += 0.012
#             bet_lens = 0.845
#         elif len(self.mega_bet_counters_sprite) == 5:
#             lens += 0.024
#             bet_lens = 0.862
#         elif len(self.mega_bet_counters_sprite) == 4:
#             lens += 0.035
#             bet_lens = 0.875
#         width = SCREEN_WIDTH * lens
#         gradient = 1.02
#         point = False
#         for i in self.mega_bet_counters_sprite:
#             if i.image is not self.point:
#                 i.position = (width, SCREEN_HEIGHT * 0.566, 0)
#                 if point == True:
#                     point = False
#                     gradient = 1.02
#                 width = width * gradient
#             else:
#                 point = True
#                 i.position = (width * 1.004, SCREEN_HEIGHT * 0.565, 0)
#                 width = (width * 0.997) * 1.015
#         self.mega_bet_sprite.position = (width * bet_lens, SCREEN_HEIGHT * 0.556, 0)
#         if self.use_times is True:
#             self.mega_clock_sprite = pyglet.sprite.Sprite(self.clock_img_red, batch=self.batch, group=self.count_group)
#             self.mega_clock_sprite.position = (SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.64, 0)

class Field():
    def __init__(self):
        self.field_group = resources.FIELD_GROUP
        self.counter_group = resources.COUNT_GROUP
        self.batch = resources.RUNNER_BATCH
        self.old_color = None
        self.x2_img = resources.X2
        self.x2_img.width = int(SCREEN_WIDTH * 0.04)
        self.x2_img.height = int(SCREEN_HEIGHT * 0.08)
        self.x2 = False
        self.x2_sprite = None
        self.duel = resources.DUEL
        self.duel.width = int(SCREEN_WIDTH * 0.1)
        self.duel.height = int(SCREEN_HEIGHT * 0.06)
        self.duel_sprite = None

        if config.FIELF_ACTIVE is True:
            self.mega = resources.FIELD['mega_anime']
            self.anime_mega = pyglet.image.Animation.from_image_sequence(self.mega, duration=0.05, loop=True)

            self.grand = resources.FIELD['grand_anime']
            self.anime_grand = pyglet.image.Animation.from_image_sequence(self.grand, duration=0.05, loop=True)

            self.major = resources.FIELD['major_anime']
            self.anime_major = pyglet.image.Animation.from_image_sequence(self.major, duration=0.05, loop=True)

            self.minor = resources.FIELD['minor_anime']
            self.anime_minor = pyglet.image.Animation.from_image_sequence(self.minor, duration=0.05, loop=True)

            self.mini = resources.FIELD['mini_anime']
            self.anime_mini = pyglet.image.Animation.from_image_sequence(self.mini, duration=0.05, loop=True)
        else:
            self.anime_mega = resources.FIELD['mega']
            self.anime_grand = resources.FIELD['grand']
            self.anime_major = resources.FIELD['major']
            self.anime_minor = resources.FIELD['minor']
            self.anime_mini = resources.FIELD['mini']


    def set_field(self, x2=False):
        if x2 != self.x2:
            self.x2 = x2
            if self.x2:
                self.x2_sprite = pyglet.sprite.Sprite(self.x2_img, batch=self.batch, group=self.counter_group)
                self.x2_sprite.position = (SCREEN_WIDTH * 0.67, SCREEN_HEIGHT * 0.745, 0)
            else:
                if self.x2_sprite:
                    self.self.x2_sprite.delete()
        self.duel_sprite = pyglet.sprite.Sprite(self.duel, batch=self.batch, group=self.counter_group)

        if self.old_color == 'red':
            self.duel_sprite.position = (SCREEN_WIDTH * 0.45, SCREEN_HEIGHT * 0.576, 0)
            if config.FIELF_ACTIVE is True:
                for i in self.mega:
                    i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.11))
                    i.height = int(SCREEN_HEIGHT * 0.66)
                self.mega_sprite = pyglet.sprite.Sprite(self.anime_mega, batch=self.batch, group=self.field_group)
                self.mega_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.355, 0)
            else:
                self.anime_mega.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
                self.anime_mega.height = int(SCREEN_HEIGHT * 0.66)
                self.mega_sprite = pyglet.sprite.Sprite(self.anime_mega, batch=self.batch, group=self.field_group)
                self.mega_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)

        elif self.old_color == 'purple':
            self.duel_sprite.position = (SCREEN_WIDTH * 0.45, SCREEN_HEIGHT * 0.574, 0)
            if config.FIELF_ACTIVE is True:
                for i in self.grand:
                    i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.11))
                    i.height = int(SCREEN_HEIGHT * 0.66)
                self.grand_sprite = pyglet.sprite.Sprite(self.anime_grand, batch=self.batch, group=self.field_group)
                self.grand_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
            else:
                self.anime_grand.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
                self.anime_grand.height = int(SCREEN_HEIGHT * 0.66)
                self.grand_sprite = pyglet.sprite.Sprite(self.anime_grand, batch=self.batch, group=self.field_group)
                self.grand_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
        elif self.old_color == 'yellow':
            self.duel_sprite.position = (SCREEN_WIDTH * 0.452, SCREEN_HEIGHT * 0.574, 0)
            if config.FIELF_ACTIVE is True:
                for i in self.major:
                    i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.11))
                    i.height = int(SCREEN_HEIGHT * 0.66)
                self.major_sprite = pyglet.sprite.Sprite(self.anime_major, batch=self.batch, group=self.field_group)
                self.major_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
            else:
                self.anime_major.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
                self.anime_major.height = int(SCREEN_HEIGHT * 0.66)
                self.major_sprite = pyglet.sprite.Sprite(self.anime_major, batch=self.batch, group=self.field_group)
                self.major_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
        elif self.old_color == 'blue':
            self.duel_sprite.position = (SCREEN_WIDTH * 0.452, SCREEN_HEIGHT * 0.574, 0)
            if config.FIELF_ACTIVE is True:
                for i in self.minor:
                    i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.11))
                    i.height = int(SCREEN_HEIGHT * 0.66)
                self.minor_sprite = pyglet.sprite.Sprite(self.anime_minor, batch=self.batch, group=self.field_group)
                self.minor_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
            else:
                self.anime_minor.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
                self.anime_minor.height = int(SCREEN_HEIGHT * 0.66)
                self.minor_sprite = pyglet.sprite.Sprite(self.anime_minor, batch=self.batch, group=self.field_group)
                self.minor_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
        elif self.old_color == 'green':
            self.duel_sprite.position = (SCREEN_WIDTH * 0.45, SCREEN_HEIGHT * 0.576, 0)
            if config.FIELF_ACTIVE is True:
                for i in self.mini:
                    i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.11))
                    i.height = int(SCREEN_HEIGHT * 0.66)
                self.mini_sprite = pyglet.sprite.Sprite(self.anime_mini, batch=self.batch, group=self.field_group)
                self.mini_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
            else:
                self.anime_mini.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
                self.anime_mini.height = int(SCREEN_HEIGHT * 0.66)
                self.mini_sprite = pyglet.sprite.Sprite(self.anime_mini, batch=self.batch, group=self.field_group)
                self.mini_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
        else:
            self.duel_sprite.position = (SCREEN_WIDTH * 0.45, SCREEN_HEIGHT * 0.576, 0)
            if config.FIELF_ACTIVE is True:
                for i in self.mega:
                    i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.11))
                    i.height = int(SCREEN_HEIGHT * 0.66)
                self.mega_sprite = pyglet.sprite.Sprite(self.anime_mega, batch=self.batch, group=self.field_group)
                self.mega_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
            else:
                self.anime_mega.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
                self.anime_mega.height = int(SCREEN_HEIGHT * 0.66)
                self.mega_sprite = pyglet.sprite.Sprite(self.anime_mega, batch=self.batch, group=self.field_group)
                self.mega_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)

    def reset(self):
        if self.duel_sprite:
            self.duel_sprite.delete()
            self.duel_sprite = None
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
        self.old_color = None
        # self.x2 = False
        # self.x2_sprite = None

class Counter():
    def __init__(self):
        self.batch = resources.RUNNER_BATCH
        self.group = resources.COUNT_GROUP
        self.micro = config.VISUAL_MICRO
        self.duration = 0.01
        self.point_sum = 0.0
        self.values = []
        self.mega_sprite = []
        self.mega_anime = []
        self.mega_activ = True
        self.grand_sprite = []
        self.grand_anime = []
        self.grand_activ = True
        self.major_sprite = []
        self.major_anime = []
        self.major_activ = True
        self.minor_sprite = []
        self.minor_anime = []
        self.minor_activ = True
        self.mini_sprite = []
        self.mini_anime = []
        self.mini_activ = True
        # self.position = {'0':0, '1':36, '2':72, '3':108, '4':143, '5':180, '6':216, '7':252, '8':288, '9':324, '10':359}
        self.position = resources.COUNTERS_INDEX
        # if self.micro is False:
        #     self.position = {'0':0, '1':36, '2':72, '3':108, '4':143, '5':180, '6':216, '7':252, '8':288, '9':324, '10':359}
        # else:
        #     self.position = {'0': 0, '1': 2, '2': 4, '3': 6, '4': 8, '5': 10, '6': 12, '7': 14, '8': 16, '9': 18,
        #                      '10': 20}
        self.counters_anime = resources.COUNTERS

        # self.counters_anime['mega_point'].width = int(SCREEN_WIDTH * 0.017)
        # self.counters_anime['mega_point'].height = int(SCREEN_HEIGHT * 0.048)
        # for i in self.counters_anime['mega']:
        #     i.width = int(SCREEN_WIDTH * 0.05)
        #     i.height = int(SCREEN_HEIGHT * 0.12)
        #
        # self.counters_anime['grand_point'].width = int(SCREEN_WIDTH * 0.017)
        # self.counters_anime['grand_point'].height = int(SCREEN_HEIGHT * 0.048)
        # for i in self.counters_anime['grand']:
        #     i.width = int(SCREEN_WIDTH * 0.05)
        #     i.height = int(SCREEN_HEIGHT * 0.12)
        #
        # self.counters_anime['major_point'].width = int(SCREEN_WIDTH * 0.017)
        # self.counters_anime['major_point'].height = int(SCREEN_HEIGHT * 0.048)
        # for i in self.counters_anime['major']:
        #     i.width = int(SCREEN_WIDTH * 0.06)
        #     i.height = int(SCREEN_HEIGHT * 0.13)
        #
        # self.counters_anime['minor_point'].width = int(SCREEN_WIDTH * 0.017)
        # self.counters_anime['minor_point'].height = int(SCREEN_HEIGHT * 0.048)
        # for i in self.counters_anime['minor']:
        #     i.width = int(SCREEN_WIDTH * 0.05)
        #     i.height = int(SCREEN_HEIGHT * 0.12)
        #
        # self.counters_anime['mini_point'].width = int(SCREEN_WIDTH * 0.017)
        # self.counters_anime['mini_point'].height = int(SCREEN_HEIGHT * 0.048)
        # for i in self.counters_anime['mini']:
        #     i.width = int(SCREEN_WIDTH * 0.05)
        #     i.height = int(SCREEN_HEIGHT * 0.12)
        #
        # self.counters_anime['gray_point'].width = int(SCREEN_WIDTH * 0.017)
        # self.counters_anime['gray_point'].height = int(SCREEN_HEIGHT * 0.048)
        # for i in self.counters_anime['gray']:
        #     i.width = int(SCREEN_WIDTH * 0.05)
        #     i.height = int(SCREEN_HEIGHT * 0.12)


    def reset(self, obj):
        try:
            if obj != 'ALL':
                for i in obj:
                    i.delete()
                obj = []
            else:
                for i in self.mega_sprite:
                    i.delete()
                self.mega_sprite = []
                for i in self.grand_sprite:
                    i.delete()
                self.grand_sprite = []
                for i in self.minor_sprite:
                    i.delete()
                self.minor_sprite = []
                for i in self.major_sprite:
                    i.delete()
                self.major_sprite = []
                for i in self.mini_sprite:
                    i.delete()
                self.mini_sprite = []
        except AttributeError:
            pass


    def anime_maker(self):
        pass


    def format(self, values=[]):
        tmp = []
        for i in values:
            tmp.append("{:.2f}".format(i))
        return tmp

    def red_show(self, values=[]):
        values = self.format(values)
        # --------------------------------------------------------------------------------------------------------------
        # MEGA
        # ---------------------------------------------------------------------------------------------------------------
        gradient = 0.39
        mega_height = 0.625

        if len(self.values) == 0:

            self.reset(self.mega_sprite)

            for i in range(len(values[0]) - 3):
                gradient -= 0.02
            if len(values[0]) == 10:
                gradient += 0.01
            if len(values[0]) == 9:
                gradient += 0.02
            if len(values[0]) == 8:
                gradient += 0.02
            if len(values[0]) == 7:
                gradient += 0.03
            if len(values[0]) == 6:
                gradient += 0.04
            if len(values[0]) == 5:
                gradient += 0.05
            if len(values[0]) == 4:
                gradient += 0.06

            for i in values[0]:
                if i == '.':
                    if self.mega_activ == True:
                        mega_point_object = pyglet.sprite.Sprite(self.counters_anime['mega_point'], batch=self.batch,
                                                                 group=self.group)
                    else:
                        mega_point_object = pyglet.sprite.Sprite(self.counters_anime['gray_point'], batch=self.batch,
                                                                 group=self.group)
                    self.mega_sprite.append(mega_point_object)
                else:
                    if self.mega_activ == True:
                        self.mega_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['mega'][self.position[i]], batch=self.batch,
                                                 group=self.group))
                    else:
                        self.mega_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['gray'][self.position[i]], batch=self.batch,
                                                 group=self.group))
            mega_point_show = False

            for i in range(len(values[0])):
                if i == 2 and len(values[0]) > 10:
                    gradient += 0.03
                if i == 5 and len(values[0]) > 10:
                    gradient += 0.03

                if i == 1 and len(values[0]) == 10:
                    gradient += 0.03
                if i == 4 and len(values[0]) == 10:
                    gradient += 0.03

                if i == 3 and len(values[0]) == 9:
                    gradient += 0.03

                if i == 2 and len(values[0]) == 8:
                    gradient += 0.03

                if i == 1 and len(values[0]) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[0]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[0]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[0]) == 9:
                #     gradient += 0.03

                if self.mega_sprite[i] == mega_point_object:
                    self.mega_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * mega_height, 0)
                    mega_point_show = True
                else:
                    self.mega_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mega_height, 0)
                if mega_point_show == False:
                    gradient += 0.044
                else:
                    gradient += 0.012
                    mega_point_show = False
            # self.values.append(values[0])
            # print(type(self.values[0]), type(values[0]))
            # return
        else:
            if self.values[0] != values[0]:

                # while True:
                #     if self.mega_anime:
                #         pass
                #     else:
                #         break
                self.reset(self.mega_sprite)
                self.mega_sprite = []
                for i in range(len(values[0]) - 3):
                    gradient -= 0.02
                if len(values[0]) == 10:
                    gradient += 0.01
                if len(values[0]) == 9:
                    gradient += 0.02
                if len(values[0]) == 8:
                    gradient += 0.02
                if len(values[0]) == 7:
                    gradient += 0.03
                if len(values[0]) == 6:
                    gradient += 0.04
                if len(values[0]) == 5:
                    gradient += 0.05
                if len(values[0]) == 4:
                    gradient += 0.06
                count = 0
                for i in values[0]:

                    if i == '.':
                        if self.mega_activ == True:
                            mega_point_object = pyglet.sprite.Sprite(self.counters_anime['mega_point'],
                                                                     batch=self.batch,
                                                                     group=self.group)
                        else:
                            mega_point_object = pyglet.sprite.Sprite(self.counters_anime['gray_point'],
                                                                     batch=self.batch,
                                                                     group=self.group)
                        self.mega_sprite.append(mega_point_object)
                    else:
                        img = []
                        if self.values[0][count] == '.':
                            count -= 1
                        if self.mega_activ == True:
                            if self.micro is False:
                                if self.position[self.values[0][count]] > self.position[i]:
                                    for b in range(self.position[self.values[0][count]], self.position['10']):
                                        img.append(self.counters_anime['mega'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['mega'][b])
                                else:
                                    for b in range(self.position[self.values[0][count]], self.position[i]):
                                        img.append(self.counters_anime['mega'][b])

                            if img != []:
                                img.append(self.counters_anime['mega'][self.position[i]])
                                self.mega_sprite.append(
                                    pyglet.sprite.Sprite(
                                        pyglet.image.Animation.from_image_sequence(img, duration=self.duration,
                                                                                   loop=False),
                                        batch=self.batch, group=self.group))
                                # img.append(self.counters_anime['mega'][self.position[i]])
                            else:
                                self.mega_sprite.append(
                                    pyglet.sprite.Sprite(self.counters_anime['mega'][self.position[i]],
                                                         batch=self.batch,
                                                         group=self.group))
                        else:
                            if self.values[0][count] == '.':
                                count -= 1
                            if self.micro is False:
                                if self.position[self.values[0][count]] > self.position[i]:
                                    for b in range(self.position[self.values[0][count]], self.position['10']):
                                        img.append(self.counters_anime['gray'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])
                                else:
                                    for b in range(self.position[self.values[0][count]], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])

                            if img != []:
                                img.append(self.counters_anime['gray'][self.position[i]])
                                self.mega_sprite.append(
                                    pyglet.sprite.Sprite(
                                        pyglet.image.Animation.from_image_sequence(img, duration=self.duration,
                                                                                   loop=False),
                                        batch=self.batch, group=self.group))
                                # img.append(self.counters_anime['mega'][self.position[i]])
                            else:
                                self.mega_sprite.append(
                                    pyglet.sprite.Sprite(self.counters_anime['gray'][self.position[i]],
                                                         batch=self.batch,
                                                         group=self.group))

                    count += 1
                mega_point_show = False
                for i in range(len(values[0])):
                    if i == 2 and len(values[0]) > 10:
                        gradient += 0.03
                    if i == 5 and len(values[0]) > 10:
                        gradient += 0.03

                    if i == 1 and len(values[0]) == 10:
                        gradient += 0.03
                    if i == 4 and len(values[0]) == 10:
                        gradient += 0.03

                    if i == 3 and len(values[0]) == 9:
                        gradient += 0.03

                    if i == 2 and len(values[0]) == 8:
                        gradient += 0.03

                    if i == 1 and len(values[0]) == 7:
                        gradient += 0.03
                    if self.mega_sprite[i] == mega_point_object:
                        self.mega_sprite[i].position = (
                        SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * mega_height, 0)
                        mega_point_show = True
                    else:
                        self.mega_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mega_height, 0)
                    if mega_point_show == False:
                        gradient += 0.044
                    else:
                        gradient += 0.012
                        mega_point_show = False

    def purple_show(self, values=[]):
        values = self.format(values)
        # --------------------------------------------------------------------------------------------------------------
        # GRAND
        # ---------------------------------------------------------------------------------------------------------------
        gradient = 0.39
        grand_height = 0.625

        if len(self.values) == 0:

            self.reset(self.grand_sprite)

            for i in range(len(values[0]) - 3):
                gradient -= 0.02
            if len(values[0]) == 10:
                gradient += 0.01
            if len(values[0]) == 9:
                gradient += 0.02
            if len(values[0]) == 8:
                gradient += 0.02
            if len(values[0]) == 7:
                gradient += 0.03
            if len(values[0]) == 6:
                gradient += 0.04
            if len(values[0]) == 5:
                gradient += 0.05
            if len(values[0]) == 4:
                gradient += 0.06

            for i in values[0]:
                if i == '.':
                    if self.grand_activ == True:
                        grand_point_object = pyglet.sprite.Sprite(self.counters_anime['grand_point'], batch=self.batch,
                                                                 group=self.group)
                    else:
                        grand_point_object = pyglet.sprite.Sprite(self.counters_anime['gray_point'], batch=self.batch,
                                                                 group=self.group)
                    self.grand_sprite.append(grand_point_object)
                else:
                    if self.grand_activ == True:
                        self.grand_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['grand'][self.position[i]], batch=self.batch,
                                                 group=self.group))
                    else:
                        self.grand_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['gray'][self.position[i]], batch=self.batch,
                                                 group=self.group))
            grand_point_show = False

            for i in range(len(values[0])):
                if i == 2 and len(values[0]) > 10:
                    gradient += 0.03
                if i == 5 and len(values[0]) > 10:
                    gradient += 0.03

                if i == 1 and len(values[0]) == 10:
                    gradient += 0.03
                if i == 4 and len(values[0]) == 10:
                    gradient += 0.03

                if i == 3 and len(values[0]) == 9:
                    gradient += 0.03

                if i == 2 and len(values[0]) == 8:
                    gradient += 0.03

                if i == 1 and len(values[0]) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[0]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[0]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[0]) == 9:
                #     gradient += 0.03

                if self.grand_sprite[i] == grand_point_object:
                    self.grand_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * grand_height, 0)
                    grand_point_show = True
                else:
                    self.grand_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * grand_height, 0)
                if grand_point_show == False:
                    gradient += 0.044
                else:
                    gradient += 0.012
                    grand_point_show = False
            # self.values.append(values[0])
            # print(type(self.values[0]), type(values[0]))
            # return
        else:
            if self.values[0] != values[0]:

                # while True:
                #     if self.grand_anime:
                #         pass
                #     else:
                #         break
                self.reset(self.grand_sprite)
                self.grand_sprite = []
                for i in range(len(values[0]) - 3):
                    gradient -= 0.02
                if len(values[0]) == 10:
                    gradient += 0.01
                if len(values[0]) == 9:
                    gradient += 0.02
                if len(values[0]) == 8:
                    gradient += 0.02
                if len(values[0]) == 7:
                    gradient += 0.03
                if len(values[0]) == 6:
                    gradient += 0.04
                if len(values[0]) == 5:
                    gradient += 0.05
                if len(values[0]) == 4:
                    gradient += 0.06
                count = 0
                for i in values[0]:

                    if i == '.':
                        if self.grand_activ == True:
                            grand_point_object = pyglet.sprite.Sprite(self.counters_anime['grand_point'],
                                                                     batch=self.batch,
                                                                     group=self.group)
                        else:
                            grand_point_object = pyglet.sprite.Sprite(self.counters_anime['gray_point'],
                                                                     batch=self.batch,
                                                                     group=self.group)
                        self.grand_sprite.append(grand_point_object)
                    else:
                        img = []
                        if self.values[0][count] == '.':
                            count -= 1
                        if self.grand_activ == True:
                            if self.micro is False:
                                if self.position[self.values[0][count]] > self.position[i]:
                                    for b in range(self.position[self.values[0][count]], self.position['10']):
                                        img.append(self.counters_anime['grand'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['grand'][b])
                                else:
                                    for b in range(self.position[self.values[0][count]], self.position[i]):
                                        img.append(self.counters_anime['grand'][b])

                            if img != []:
                                img.append(self.counters_anime['grand'][self.position[i]])
                                self.grand_sprite.append(
                                    pyglet.sprite.Sprite(
                                        pyglet.image.Animation.from_image_sequence(img, duration=self.duration,
                                                                                   loop=False),
                                        batch=self.batch, group=self.group))
                                # img.append(self.counters_anime['grand'][self.position[i]])
                            else:
                                self.grand_sprite.append(
                                    pyglet.sprite.Sprite(self.counters_anime['grand'][self.position[i]],
                                                         batch=self.batch,
                                                         group=self.group))
                        else:
                            if self.values[0][count] == '.':
                                count -= 1
                            if self.micro is False:
                                if self.position[self.values[0][count]] > self.position[i]:
                                    for b in range(self.position[self.values[0][count]], self.position['10']):
                                        img.append(self.counters_anime['gray'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])
                                else:
                                    for b in range(self.position[self.values[0][count]], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])

                            if img != []:
                                img.append(self.counters_anime['gray'][self.position[i]])
                                self.grand_sprite.append(
                                    pyglet.sprite.Sprite(
                                        pyglet.image.Animation.from_image_sequence(img, duration=self.duration,
                                                                                   loop=False),
                                        batch=self.batch, group=self.group))
                                # img.append(self.counters_anime['grand'][self.position[i]])
                            else:
                                self.grand_sprite.append(
                                    pyglet.sprite.Sprite(self.counters_anime['gray'][self.position[i]],
                                                         batch=self.batch,
                                                         group=self.group))

                    count += 1
                grand_point_show = False
                for i in range(len(values[0])):
                    if i == 2 and len(values[0]) > 10:
                        gradient += 0.03
                    if i == 5 and len(values[0]) > 10:
                        gradient += 0.03

                    if i == 1 and len(values[0]) == 10:
                        gradient += 0.03
                    if i == 4 and len(values[0]) == 10:
                        gradient += 0.03

                    if i == 3 and len(values[0]) == 9:
                        gradient += 0.03

                    if i == 2 and len(values[0]) == 8:
                        gradient += 0.03

                    if i == 1 and len(values[0]) == 7:
                        gradient += 0.03
                    if self.grand_sprite[i] == grand_point_object:
                        self.grand_sprite[i].position = (
                        SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * grand_height, 0)
                        grand_point_show = True
                    else:
                        self.grand_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * grand_height, 0)
                    if grand_point_show == False:
                        gradient += 0.044
                    else:
                        gradient += 0.012
                        grand_point_show = False

    def yellow_show(self, values=[]):
        values = self.format(values)
        # --------------------------------------------------------------------------------------------------------------
        # MAJOR
        # ---------------------------------------------------------------------------------------------------------------
        gradient = 0.39
        major_height = 0.625

        if len(self.values) == 0:

            self.reset(self.major_sprite)

            for i in range(len(values[0]) - 3):
                gradient -= 0.02
            if len(values[0]) == 10:
                gradient += 0.01
            if len(values[0]) == 9:
                gradient += 0.02
            if len(values[0]) == 8:
                gradient += 0.02
            if len(values[0]) == 7:
                gradient += 0.03
            if len(values[0]) == 6:
                gradient += 0.04
            if len(values[0]) == 5:
                gradient += 0.05
            if len(values[0]) == 4:
                gradient += 0.06

            for i in values[0]:
                if i == '.':
                    if self.major_activ == True:
                        major_point_object = pyglet.sprite.Sprite(self.counters_anime['major_point'], batch=self.batch,
                                                                 group=self.group)
                    else:
                        major_point_object = pyglet.sprite.Sprite(self.counters_anime['gray_point'], batch=self.batch,
                                                                 group=self.group)
                    self.major_sprite.append(major_point_object)
                else:
                    if self.major_activ == True:
                        self.major_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['major'][self.position[i]], batch=self.batch,
                                                 group=self.group))
                    else:
                        self.major_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['gray'][self.position[i]], batch=self.batch,
                                                 group=self.group))
            major_point_show = False

            for i in range(len(values[0])):
                if i == 2 and len(values[0]) > 10:
                    gradient += 0.03
                if i == 5 and len(values[0]) > 10:
                    gradient += 0.03

                if i == 1 and len(values[0]) == 10:
                    gradient += 0.03
                if i == 4 and len(values[0]) == 10:
                    gradient += 0.03

                if i == 3 and len(values[0]) == 9:
                    gradient += 0.03

                if i == 2 and len(values[0]) == 8:
                    gradient += 0.03

                if i == 1 and len(values[0]) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[0]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[0]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[0]) == 9:
                #     gradient += 0.03
                if self.major_sprite[i] == major_point_object:
                    self.major_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * major_height, 0)
                    major_point_show = True
                else:
                    self.major_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * major_height, 0)
                if major_point_show == False:
                    gradient += 0.044
                else:
                    gradient += 0.012
                    major_point_show = False
            # self.values.append(values[0])
            # print(type(self.values[0]), type(values[0]))
            # return
        else:
            if self.values[0] != values[0]:

                # while True:
                #     if self.major_anime:
                #         pass
                #     else:
                #         break
                self.reset(self.major_sprite)
                self.major_sprite = []
                for i in range(len(values[0]) - 3):
                    gradient -= 0.02
                if len(values[0]) == 10:
                    gradient += 0.01
                if len(values[0]) == 9:
                    gradient += 0.02
                if len(values[0]) == 8:
                    gradient += 0.02
                if len(values[0]) == 7:
                    gradient += 0.03
                if len(values[0]) == 6:
                    gradient += 0.04
                if len(values[0]) == 5:
                    gradient += 0.05
                if len(values[0]) == 4:
                    gradient += 0.06
                count = 0
                for i in values[0]:

                    if i == '.':
                        if self.major_activ == True:
                            major_point_object = pyglet.sprite.Sprite(self.counters_anime['major_point'],
                                                                     batch=self.batch,
                                                                     group=self.group)
                        else:
                            major_point_object = pyglet.sprite.Sprite(self.counters_anime['gray_point'],
                                                                     batch=self.batch,
                                                                     group=self.group)
                        self.major_sprite.append(major_point_object)
                    else:
                        img = []
                        if self.values[0][count] == '.':
                            count -= 1
                        if self.major_activ == True:
                            if self.micro is False:
                                if self.position[self.values[0][count]] > self.position[i]:
                                    for b in range(self.position[self.values[0][count]], self.position['10']):
                                        img.append(self.counters_anime['major'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['major'][b])
                                else:
                                    for b in range(self.position[self.values[0][count]], self.position[i]):
                                        img.append(self.counters_anime['major'][b])

                            if img != []:
                                img.append(self.counters_anime['major'][self.position[i]])
                                self.major_sprite.append(
                                    pyglet.sprite.Sprite(
                                        pyglet.image.Animation.from_image_sequence(img, duration=self.duration,
                                                                                   loop=False),
                                        batch=self.batch, group=self.group))
                                # img.append(self.counters_anime['major'][self.position[i]])
                            else:
                                self.major_sprite.append(
                                    pyglet.sprite.Sprite(self.counters_anime['major'][self.position[i]],
                                                         batch=self.batch,
                                                         group=self.group))
                        else:
                            if self.values[0][count] == '.':
                                count -= 1
                            if self.micro is False:
                                if self.position[self.values[0][count]] > self.position[i]:
                                    for b in range(self.position[self.values[0][count]], self.position['10']):
                                        img.append(self.counters_anime['gray'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])
                                else:
                                    for b in range(self.position[self.values[0][count]], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])

                            if img != []:
                                img.append(self.counters_anime['gray'][self.position[i]])
                                self.major_sprite.append(
                                    pyglet.sprite.Sprite(
                                        pyglet.image.Animation.from_image_sequence(img, duration=self.duration,
                                                                                   loop=False),
                                        batch=self.batch, group=self.group))
                                # img.append(self.counters_anime['major'][self.position[i]])
                            else:
                                self.major_sprite.append(
                                    pyglet.sprite.Sprite(self.counters_anime['gray'][self.position[i]],
                                                         batch=self.batch,
                                                         group=self.group))

                    count += 1
                major_point_show = False
                for i in range(len(values[0])):
                    if i == 2 and len(values[0]) > 10:
                        gradient += 0.03
                    if i == 5 and len(values[0]) > 10:
                        gradient += 0.03

                    if i == 1 and len(values[0]) == 10:
                        gradient += 0.03
                    if i == 4 and len(values[0]) == 10:
                        gradient += 0.03

                    if i == 3 and len(values[0]) == 9:
                        gradient += 0.03

                    if i == 2 and len(values[0]) == 8:
                        gradient += 0.03

                    if i == 1 and len(values[0]) == 7:
                        gradient += 0.03
                    if self.major_sprite[i] == major_point_object:
                        self.major_sprite[i].position = (
                        SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * major_height, 0)
                        major_point_show = True
                    else:
                        self.major_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * major_height, 0)
                    if major_point_show == False:
                        gradient += 0.044
                    else:
                        gradient += 0.012
                        major_point_show = False

    def blue_show(self, values=[]):
        values = self.format(values)
        # --------------------------------------------------------------------------------------------------------------
        # MINOR
        # ---------------------------------------------------------------------------------------------------------------
        gradient = 0.39
        minor_height = 0.625

        if len(self.values) == 0:

            self.reset(self.minor_sprite)

            for i in range(len(values[0]) - 3):
                gradient -= 0.02
            if len(values[0]) == 10:
                gradient += 0.01
            if len(values[0]) == 9:
                gradient += 0.02
            if len(values[0]) == 8:
                gradient += 0.02
            if len(values[0]) == 7:
                gradient += 0.03
            if len(values[0]) == 6:
                gradient += 0.04
            if len(values[0]) == 5:
                gradient += 0.05
            if len(values[0]) == 4:
                gradient += 0.06

            for i in values[0]:
                if i == '.':
                    if self.minor_activ == True:
                        minor_point_object = pyglet.sprite.Sprite(self.counters_anime['minor_point'], batch=self.batch,
                                                                 group=self.group)
                    else:
                        minor_point_object = pyglet.sprite.Sprite(self.counters_anime['gray_point'], batch=self.batch,
                                                                 group=self.group)
                    self.minor_sprite.append(minor_point_object)
                else:
                    if self.minor_activ == True:
                        self.minor_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['minor'][self.position[i]], batch=self.batch,
                                                 group=self.group))
                    else:
                        self.minor_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['gray'][self.position[i]], batch=self.batch,
                                                 group=self.group))
            minor_point_show = False

            for i in range(len(values[0])):
                if i == 2 and len(values[0]) > 10:
                    gradient += 0.03
                if i == 5 and len(values[0]) > 10:
                    gradient += 0.03

                if i == 1 and len(values[0]) == 10:
                    gradient += 0.03
                if i == 4 and len(values[0]) == 10:
                    gradient += 0.03

                if i == 3 and len(values[0]) == 9:
                    gradient += 0.03

                if i == 2 and len(values[0]) == 8:
                    gradient += 0.03

                if i == 1 and len(values[0]) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[0]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[0]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[0]) == 9:
                #     gradient += 0.03

                if self.minor_sprite[i] == minor_point_object:
                    self.minor_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * minor_height, 0)
                    minor_point_show = True
                else:
                    self.minor_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * minor_height, 0)
                if minor_point_show == False:
                    gradient += 0.044
                else:
                    gradient += 0.012
                    minor_point_show = False
            # self.values.append(values[0])
            # print(type(self.values[0]), type(values[0]))
            # return
        else:
            if self.values[0] != values[0]:

                # while True:
                #     if self.minor_anime:
                #         pass
                #     else:
                #         break
                self.reset(self.minor_sprite)
                self.minor_sprite = []
                for i in range(len(values[0]) - 3):
                    gradient -= 0.02
                if len(values[0]) == 10:
                    gradient += 0.01
                if len(values[0]) == 9:
                    gradient += 0.02
                if len(values[0]) == 8:
                    gradient += 0.02
                if len(values[0]) == 7:
                    gradient += 0.03
                if len(values[0]) == 6:
                    gradient += 0.04
                if len(values[0]) == 5:
                    gradient += 0.05
                if len(values[0]) == 4:
                    gradient += 0.06
                count = 0
                for i in values[0]:

                    if i == '.':
                        if self.minor_activ == True:
                            minor_point_object = pyglet.sprite.Sprite(self.counters_anime['minor_point'],
                                                                     batch=self.batch,
                                                                     group=self.group)
                        else:
                            minor_point_object = pyglet.sprite.Sprite(self.counters_anime['gray_point'],
                                                                     batch=self.batch,
                                                                     group=self.group)
                        self.minor_sprite.append(minor_point_object)
                    else:
                        img = []
                        if self.values[0][count] == '.':
                            count -= 1
                        if self.minor_activ == True:
                            if self.micro is False:
                                if self.position[self.values[0][count]] > self.position[i]:
                                    for b in range(self.position[self.values[0][count]], self.position['10']):
                                        img.append(self.counters_anime['minor'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['minor'][b])
                                else:
                                    for b in range(self.position[self.values[0][count]], self.position[i]):
                                        img.append(self.counters_anime['minor'][b])

                            if img != []:
                                img.append(self.counters_anime['minor'][self.position[i]])
                                self.minor_sprite.append(
                                    pyglet.sprite.Sprite(
                                        pyglet.image.Animation.from_image_sequence(img, duration=self.duration,
                                                                                   loop=False),
                                        batch=self.batch, group=self.group))
                                # img.append(self.counters_anime['minor'][self.position[i]])
                            else:
                                self.minor_sprite.append(
                                    pyglet.sprite.Sprite(self.counters_anime['minor'][self.position[i]],
                                                         batch=self.batch,
                                                         group=self.group))
                        else:
                            if self.values[0][count] == '.':
                                count -= 1
                            if self.micro is False:
                                if self.position[self.values[0][count]] > self.position[i]:
                                    for b in range(self.position[self.values[0][count]], self.position['10']):
                                        img.append(self.counters_anime['gray'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])
                                else:
                                    for b in range(self.position[self.values[0][count]], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])

                            if img != []:
                                img.append(self.counters_anime['gray'][self.position[i]])
                                self.minor_sprite.append(
                                    pyglet.sprite.Sprite(
                                        pyglet.image.Animation.from_image_sequence(img, duration=self.duration,
                                                                                   loop=False),
                                        batch=self.batch, group=self.group))
                                # img.append(self.counters_anime['minor'][self.position[i]])
                            else:
                                self.minor_sprite.append(
                                    pyglet.sprite.Sprite(self.counters_anime['gray'][self.position[i]],
                                                         batch=self.batch,
                                                         group=self.group))

                    count += 1
                minor_point_show = False
                for i in range(len(values[0])):
                    if i == 2 and len(values[0]) > 10:
                        gradient += 0.03
                    if i == 5 and len(values[0]) > 10:
                        gradient += 0.03

                    if i == 1 and len(values[0]) == 10:
                        gradient += 0.03
                    if i == 4 and len(values[0]) == 10:
                        gradient += 0.03

                    if i == 3 and len(values[0]) == 9:
                        gradient += 0.03

                    if i == 2 and len(values[0]) == 8:
                        gradient += 0.03

                    if i == 1 and len(values[0]) == 7:
                        gradient += 0.03
                    if self.minor_sprite[i] == minor_point_object:
                        self.minor_sprite[i].position = (
                        SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * minor_height, 0)
                        minor_point_show = True
                    else:
                        self.minor_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * minor_height, 0)
                    if minor_point_show == False:
                        gradient += 0.044
                    else:
                        gradient += 0.012
                        minor_point_show = False

    def green_show(self, values=[]):
        values = self.format(values)
        # --------------------------------------------------------------------------------------------------------------
        # MINI
        # ---------------------------------------------------------------------------------------------------------------
        gradient = 0.39
        mini_height = 0.625

        if len(self.values) == 0:

            self.reset(self.mini_sprite)

            for i in range(len(values[0]) - 3):
                gradient -= 0.02
            if len(values[0]) == 10:
                gradient += 0.01
            if len(values[0]) == 9:
                gradient += 0.02
            if len(values[0]) == 8:
                gradient += 0.02
            if len(values[0]) == 7:
                gradient += 0.03
            if len(values[0]) == 6:
                gradient += 0.04
            if len(values[0]) == 5:
                gradient += 0.05
            if len(values[0]) == 4:
                gradient += 0.06

            for i in values[0]:
                if i == '.':
                    if self.mini_activ == True:
                        mini_point_object = pyglet.sprite.Sprite(self.counters_anime['mini_point'], batch=self.batch,
                                                                 group=self.group)
                    else:
                        mini_point_object = pyglet.sprite.Sprite(self.counters_anime['gray_point'], batch=self.batch,
                                                                 group=self.group)
                    self.mini_sprite.append(mini_point_object)
                else:
                    if self.mini_activ == True:
                        self.mini_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['mini'][self.position[i]], batch=self.batch,
                                                 group=self.group))
                    else:
                        self.mini_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['gray'][self.position[i]], batch=self.batch,
                                                 group=self.group))
            mini_point_show = False

            for i in range(len(values[0])):
                if i == 2 and len(values[0]) > 10:
                    gradient += 0.03
                if i == 5 and len(values[0]) > 10:
                    gradient += 0.03

                if i == 1 and len(values[0]) == 10:
                    gradient += 0.03
                if i == 4 and len(values[0]) == 10:
                    gradient += 0.03

                if i == 3 and len(values[0]) == 9:
                    gradient += 0.03

                if i == 2 and len(values[0]) == 8:
                    gradient += 0.03

                if i == 1 and len(values[0]) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[0]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[0]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[0]) == 9:
                #     gradient += 0.03

                if self.mini_sprite[i] == mini_point_object:
                    self.mini_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * mini_height, 0)
                    mini_point_show = True
                else:
                    self.mini_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mini_height, 0)
                if mini_point_show == False:
                    gradient += 0.044
                else:
                    gradient += 0.012
                    mini_point_show = False
            # self.values.append(values[0])
            # print(type(self.values[0]), type(values[0]))
            # return
        else:
            if self.values[0] != values[0]:

                # while True:
                #     if self.mini_anime:
                #         pass
                #     else:
                #         break
                self.reset(self.mini_sprite)
                self.mini_sprite = []
                for i in range(len(values[0]) - 3):
                    gradient -= 0.02
                if len(values[0]) == 10:
                    gradient += 0.01
                if len(values[0]) == 9:
                    gradient += 0.02
                if len(values[0]) == 8:
                    gradient += 0.02
                if len(values[0]) == 7:
                    gradient += 0.03
                if len(values[0]) == 6:
                    gradient += 0.04
                if len(values[0]) == 5:
                    gradient += 0.05
                if len(values[0]) == 4:
                    gradient += 0.06
                count = 0
                for i in values[0]:

                    if i == '.':
                        if self.mini_activ == True:
                            mini_point_object = pyglet.sprite.Sprite(self.counters_anime['mini_point'],
                                                                     batch=self.batch,
                                                                     group=self.group)
                        else:
                            mini_point_object = pyglet.sprite.Sprite(self.counters_anime['gray_point'],
                                                                     batch=self.batch,
                                                                     group=self.group)
                        self.mini_sprite.append(mini_point_object)
                    else:
                        img = []
                        if self.values[0][count] == '.':
                            count -= 1
                        if self.mini_activ == True:
                            if self.micro is False:
                                if self.position[self.values[0][count]] > self.position[i]:
                                    for b in range(self.position[self.values[0][count]], self.position['10']):
                                        img.append(self.counters_anime['mini'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['mini'][b])
                                else:
                                    for b in range(self.position[self.values[0][count]], self.position[i]):
                                        img.append(self.counters_anime['mini'][b])

                            if img != []:
                                img.append(self.counters_anime['mini'][self.position[i]])
                                self.mini_sprite.append(
                                    pyglet.sprite.Sprite(
                                        pyglet.image.Animation.from_image_sequence(img, duration=self.duration,
                                                                                   loop=False),
                                        batch=self.batch, group=self.group))
                                # img.append(self.counters_anime['mini'][self.position[i]])
                            else:
                                self.mini_sprite.append(
                                    pyglet.sprite.Sprite(self.counters_anime['mini'][self.position[i]],
                                                         batch=self.batch,
                                                         group=self.group))
                        else:
                            if self.values[0][count] == '.':
                                count -= 1
                            if self.micro is False:
                                if self.position[self.values[0][count]] > self.position[i]:
                                    for b in range(self.position[self.values[0][count]], self.position['10']):
                                        img.append(self.counters_anime['gray'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])
                                else:
                                    for b in range(self.position[self.values[0][count]], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])

                            if img != []:
                                img.append(self.counters_anime['gray'][self.position[i]])
                                self.mini_sprite.append(
                                    pyglet.sprite.Sprite(
                                        pyglet.image.Animation.from_image_sequence(img, duration=self.duration,
                                                                                   loop=False),
                                        batch=self.batch, group=self.group))
                                # img.append(self.counters_anime['mini'][self.position[i]])
                            else:
                                self.mini_sprite.append(
                                    pyglet.sprite.Sprite(self.counters_anime['gray'][self.position[i]],
                                                         batch=self.batch,
                                                         group=self.group))

                    count += 1
                mini_point_show = False
                for i in range(len(values[0])):
                    if i == 2 and len(values[0]) > 10:
                        gradient += 0.03
                    if i == 5 and len(values[0]) > 10:
                        gradient += 0.03

                    if i == 1 and len(values[0]) == 10:
                        gradient += 0.03
                    if i == 4 and len(values[0]) == 10:
                        gradient += 0.03

                    if i == 3 and len(values[0]) == 9:
                        gradient += 0.03

                    if i == 2 and len(values[0]) == 8:
                        gradient += 0.03

                    if i == 1 and len(values[0]) == 7:
                        gradient += 0.03
                    if self.mini_sprite[i] == mini_point_object:
                        self.mini_sprite[i].position = (
                        SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * mini_height, 0)
                        mini_point_show = True
                    else:
                        self.mini_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mini_height, 0)
                    if mini_point_show == False:
                        gradient += 0.044
                    else:
                        gradient += 0.012
                        mini_point_show = False

    def show(self, values=[], color='red'):
        if color=='red':
            self.red_show(values)
        elif color=='purple':
            self.purple_show(values)
        elif color == 'yellow':
            self.yellow_show(values)
        elif color == 'blue':
            self.blue_show(values)
        elif color == 'green':
            self.green_show(values)
        else:
            self.red_show(values)

class Counter2(Counter):
    def __init__(self):
        Counter.__init__(self)
        self.point_sum = 0.014

class BagField():
    def __init__(self):
        self.batch = resources.RUNNER_BATCH
        self.field_group = resources.FIELD_GROUP
        self.counter_group = resources.COUNT_GROUP
        self.runner_field = resources.RUNNER_FIELD
        self.field_sprites_count = None
        self.field_sprites = None
        self.down_on_sprite = []
        self.color = None
        self.counters = resources.RUNNER_DOWNON
        self.micro = config.VISUAL_MICRO
        self.position = resources.RUNNER_INDEX
        if config.FONT == 1:
            self.point_sum = 0.0
        elif config.FONT == 2:
            self.point_sum = 0.014
        else:
            self.point_sum = 0.0

        # self.counters['gray_point'].width = int(SCREEN_WIDTH * 0.017)
        # self.counters['gray_point'].height = int(SCREEN_HEIGHT * 0.048)
        # for i in self.counters['gray']:
        #     i.width = int(SCREEN_WIDTH * 0.05)
        #     i.height = int(SCREEN_HEIGHT * 0.12)

        self.down_on = ''
        for i in self.runner_field:
            self.runner_field[i].width = int(SCREEN_WIDTH * 0.80)
            self.runner_field[i].height = int(SCREEN_HEIGHT * 0.785)
        # self.field_h = resources.EMPTY_FIELD_H
        # self.field_y = resources.EMPTY_FIELD_Y
        # self.field_y.width = int(SCREEN_WIDTH * 0.15)
        # self.field_y.height = int(SCREEN_HEIGHT * 0.518)
        #
        # self.field_h.width = int(SCREEN_WIDTH * 0.7)
        # self.field_h.height = int(SCREEN_HEIGHT * 0.55)
        #
        # self.field_h_sprite = pyglet.sprite.Sprite(self.field_h, batch=self.batch,
        #                                                      group=self.field_group)
        # self.field_h_sprite.position =  (SCREEN_WIDTH * 0.18, SCREEN_HEIGHT * 0.07, 0)
        #
        # self.field_y_sprite = pyglet.sprite.Sprite(self.field_y, batch=self.batch,
        #                                            group=self.field_group)
        # self.field_y_sprite.position = (SCREEN_WIDTH * 0.03, SCREEN_HEIGHT * 0.085, 0)

        self.device_img = resources.RUNNER_DEVICE
        for i in self.device_img:
            i.width = int(SCREEN_WIDTH * 0.03)
            i.height = int(SCREEN_HEIGHT * 0.06)

        self.device = []
        self.sprites = []
        self.color = None


    def format_device(self, device=[]):
        tmp = []
        for i in device:
            tmp.append(str(i))
        return tmp

    def show(self):
        # if config.FONT == 2:
        #     gradient = 0.385
        # else:
        gradient = 0.40
        # if self.mega_activ == False:
        #     mega_height = 0.650
        # else:
        mega_height = 0.472
        for i in range(len(self.down_on) - 3):
            gradient -= 0.02
        if len(self.down_on) == 10:
            gradient += 0.01
        if len(self.down_on) == 9:
            gradient += 0.02
        if len(self.down_on) == 8:
            gradient += 0.02
        if len(self.down_on) == 7:
            gradient += 0.03
        if len(self.down_on) == 6:
            gradient += 0.04
        if len(self.down_on) == 5:
            gradient += 0.05
        if len(self.down_on) == 4:
            gradient += 0.06
        for i in self.down_on:
            if i == '.':
                point_object = pyglet.sprite.Sprite(self.counters['gray_point'], batch=self.batch,
                                                         group=self.counter_group)
                self.down_on_sprite.append(point_object)
            else:
                self.down_on_sprite.append(
                    pyglet.sprite.Sprite(self.counters['gray'][self.position[i]], batch=self.batch,
                                         group=self.counter_group))
        point_show = False
        for i in range(len(self.down_on)):
            if i == 2 and len(self.down_on) > 10:
                gradient += 0.03
            if i == 5 and len(self.down_on) > 10:
                gradient += 0.03

            if i == 1 and len(self.down_on) == 10:
                gradient += 0.03
            if i == 4 and len(self.down_on) == 10:
                gradient += 0.03

            if i == 3 and len(self.down_on) == 9:
                gradient += 0.03

            if i == 2 and len(self.down_on) == 8:
                gradient += 0.03

            if i == 1 and len(self.down_on) == 7:
                gradient += 0.03

            if self.down_on_sprite[i] == point_object:
                self.down_on_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mega_height, 0)
                point_show = True
            else:
                self.down_on_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mega_height, 0)
            if point_show == False:
                gradient += 0.044
            else:
                gradient += 0.012
                point_show = False


    def show_3(self, color='mega'):
        gradient = 0.08
        if len(self.device[0]) == 1:
            left = 0.265
        else:
            left = 0.275
        try:
            for b in reversed(self.device[0]):
                sprites = pyglet.sprite.Sprite(self.device_img[int(b)], batch=self.batch,
                                               group=self.counter_group)
                sprites.position = (SCREEN_WIDTH * left, SCREEN_HEIGHT * gradient, 0)
                left = left - 0.022
                self.sprites.append(sprites)
        except IndexError:
            pass
        try:
            if len(self.device[1]) == 1:
                left = 0.485
            else:
                left = 0.495
            for b in reversed(self.device[1]):
                sprites = pyglet.sprite.Sprite(self.device_img[int(b)], batch=self.batch,
                                               group=self.counter_group)
                sprites.position = (SCREEN_WIDTH * left, SCREEN_HEIGHT * gradient, 0)
                left = left - 0.022
                self.sprites.append(sprites)
        except IndexError:
            pass
        try:
            if len(self.device[2]) == 1:
                left = 0.70
            else:
                left = 0.71
            for b in reversed(self.device[2]):
                sprites = pyglet.sprite.Sprite(self.device_img[int(b)], batch=self.batch,
                                               group=self.counter_group)
                sprites.position = (SCREEN_WIDTH * left, SCREEN_HEIGHT * gradient, 0)
                left = left - 0.022
                self.sprites.append(sprites)
        except IndexError:
            pass

    def show_2(self, color='mega'):
        gradient = 0.08
        if len(self.device[0]) == 1:
            left = 0.315
        else:
            left = 0.325
        try:
            for b in reversed(self.device[0]):
                sprites = pyglet.sprite.Sprite(self.device_img[int(b)], batch=self.batch,
                                               group=self.counter_group)
                sprites.position = (SCREEN_WIDTH * left, SCREEN_HEIGHT * gradient, 0)
                left = left - 0.022
                self.sprites.append(sprites)
        except IndexError:
            pass
        try:
            if len(self.device[1]) == 1:
                left = 0.65
            else:
                left = 0.66
            for b in reversed(self.device[1]):
                sprites = pyglet.sprite.Sprite(self.device_img[int(b)], batch=self.batch,
                                               group=self.counter_group)
                sprites.position = (SCREEN_WIDTH * left, SCREEN_HEIGHT * gradient, 0)
                left = left - 0.022
                self.sprites.append(sprites)
        except IndexError:
            pass

    def show_4(self, color='mega'):
        gradient = 0.08
        if len(self.device[0]) == 1:
            left = 0.245
        else:
            left = 0.255
        try:
            for b in reversed(self.device[0]):
                sprites = pyglet.sprite.Sprite(self.device_img[int(b)], batch=self.batch,
                                               group=self.counter_group)
                sprites.position = (SCREEN_WIDTH * left, SCREEN_HEIGHT * gradient, 0)
                left = left - 0.022
                self.sprites.append(sprites)
        except IndexError:
            pass
        try:
            if len(self.device[1]) == 1:
                left = 0.405
            else:
                left = 0.415
            for b in reversed(self.device[1]):
                sprites = pyglet.sprite.Sprite(self.device_img[int(b)], batch=self.batch,
                                               group=self.counter_group)
                sprites.position = (SCREEN_WIDTH * left, SCREEN_HEIGHT * gradient, 0)
                left = left - 0.022
                self.sprites.append(sprites)
        except IndexError:
            pass
        try:
            if len(self.device[2]) == 1:
                left = 0.565
            else:
                left = 0.575
            for b in reversed(self.device[2]):
                sprites = pyglet.sprite.Sprite(self.device_img[int(b)], batch=self.batch,
                                               group=self.counter_group)
                sprites.position = (SCREEN_WIDTH * left, SCREEN_HEIGHT * gradient, 0)
                left = left - 0.022
                self.sprites.append(sprites)
        except IndexError:
            pass

        try:
            if len(self.device[3]) == 1:
                left = 0.725
            else:
                left = 0.735
            for b in reversed(self.device[3]):
                sprites = pyglet.sprite.Sprite(self.device_img[int(b)], batch=self.batch,
                                               group=self.counter_group)
                sprites.position = (SCREEN_WIDTH * left, SCREEN_HEIGHT * gradient, 0)
                left = left - 0.022
                self.sprites.append(sprites)
        except IndexError:
            pass

    def show_5(self, color='mega'):
        gradient = 0.08
        if len(self.device[0]) == 1:
            left = 0.23
        else:
            left = 0.24
        try:
            for b in reversed(self.device[0]):
                sprites = pyglet.sprite.Sprite(self.device_img[int(b)], batch=self.batch,
                                               group=self.counter_group)
                sprites.position = (SCREEN_WIDTH * left, SCREEN_HEIGHT * gradient, 0)
                left = left - 0.022
                self.sprites.append(sprites)
        except IndexError:
            pass
        try:
            if len(self.device[1]) == 1:
                left = 0.358
            else:
                left = 0.365
            for b in reversed(self.device[1]):
                sprites = pyglet.sprite.Sprite(self.device_img[int(b)], batch=self.batch,
                                               group=self.counter_group)
                sprites.position = (SCREEN_WIDTH * left, SCREEN_HEIGHT * gradient, 0)
                left = left - 0.022
                self.sprites.append(sprites)
        except IndexError:
            pass
        try:
            if len(self.device[2]) == 1:
                left = 0.484
            else:
                left = 0.492
            for b in reversed(self.device[2]):
                sprites = pyglet.sprite.Sprite(self.device_img[int(b)], batch=self.batch,
                                               group=self.counter_group)
                sprites.position = (SCREEN_WIDTH * left, SCREEN_HEIGHT * gradient, 0)
                left = left - 0.022
                self.sprites.append(sprites)
        except IndexError:
            pass

        try:
            if len(self.device[3]) == 1:
                left = 0.61
            else:
                left = 0.62
            for b in reversed(self.device[3]):
                sprites = pyglet.sprite.Sprite(self.device_img[int(b)], batch=self.batch,
                                               group=self.counter_group)
                sprites.position = (SCREEN_WIDTH * left, SCREEN_HEIGHT * gradient, 0)
                left = left - 0.022
                self.sprites.append(sprites)
        except IndexError:
            pass

        try:
            if len(self.device[4]) == 1:
                left = 0.738
            else:
                left = 0.745
            for b in reversed(self.device[4]):
                sprites = pyglet.sprite.Sprite(self.device_img[int(b)], batch=self.batch,
                                               group=self.counter_group)
                sprites.position = (SCREEN_WIDTH * left, SCREEN_HEIGHT * gradient, 0)
                left = left - 0.022
                self.sprites.append(sprites)
        except IndexError:
            pass

    def show_mashine(self, color='red', device=[], max_len=3, down_on=''):
        if color != self.color:
            self.reset()
            self.color = color
            self.device = []
        device = self.format_device(device=device)


        if max_len != self.field_sprites_count or self.color != color:
            self.color = color

            self.field_sprites_count = max_len
            if self.field_sprites:
                self.field_sprites.delete()
            if self.field_sprites_count == 2:
                self.field_sprites = pyglet.sprite.Sprite(self.runner_field[2], batch=self.batch, group=self.field_group)
            elif self.field_sprites_count == 3:
                self.field_sprites = pyglet.sprite.Sprite(self.runner_field[3], batch=self.batch, group=self.field_group)
            elif self.field_sprites_count == 4:
                self.field_sprites = pyglet.sprite.Sprite(self.runner_field[4], batch=self.batch, group=self.field_group)
            elif self.field_sprites_count == 5:
                self.field_sprites = pyglet.sprite.Sprite(self.runner_field[5], batch=self.batch, group=self.field_group)
            self.field_sprites.position = (SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.00, 0)
        if self.down_on != "{:.2f}".format(down_on):
            for i in self.down_on_sprite:
                i.delete()
            self.down_on_sprite = []
            self.down_on = "{:.2f}".format(down_on)
            self.show()

        if device != self.device:
            self.reset()

            self.device = device
            if color == 'red':
                if self.field_sprites_count == 3:
                    self.show_3('mega')
                elif self.field_sprites_count == 2:
                    self.show_2('mega')
                elif self.field_sprites_count == 4:
                    self.show_4('mega')
                elif self.field_sprites_count == 5:
                    self.show_5('mega')
            elif color == 'purple':
                if self.field_sprites_count == 3:
                    self.show_3('grand')
                elif self.field_sprites_count == 2:
                    self.show_2('grand')
                elif self.field_sprites_count == 4:
                    self.show_4('grand')
                elif self.field_sprites_count == 5:
                    self.show_5('grand')
            elif color == 'yellow':
                if self.field_sprites_count == 3:
                    self.show_3('major')
                elif self.field_sprites_count == 2:
                    self.show_2('major')
                elif self.field_sprites_count == 4:
                    self.show_4('major')
                elif self.field_sprites_count == 5:
                    self.show_5('major')
            elif color == 'blue':
                if self.field_sprites_count == 3:
                    self.show_3('minor')
                elif self.field_sprites_count == 2:
                    self.show_2('minor')
                elif self.field_sprites_count == 4:
                    self.show_4('minor')
                elif self.field_sprites_count == 5:
                    self.show_5('minor')
            elif color == 'green':
                if self.field_sprites_count == 3:
                    self.show_3('mini')
                elif self.field_sprites_count == 2:
                    self.show_2('mini')
                elif self.field_sprites_count == 4:
                    self.show_4('mini')
                elif self.field_sprites_count == 5:
                    self.show_5('mini')
            else:
                if self.field_sprites_count == 3:
                    self.show_3('mega')
                elif self.field_sprites_count == 2:
                    self.show_2('mega')
                elif self.field_sprites_count == 4:
                    self.show_4('mega')
                elif self.field_sprites_count == 5:
                    self.show_5('mega')

    def reset(self):
        # try:
        for i in self.sprites:
            i.delete()
        self.sprites = []
        self.device = []
        self.sprites = []
        # self.color = None
            # self.field_sprites.delete()
        # except AttributeError:
        #     pass

class Procent():
    def __init__(self):
        self.batch = resources.RUNNER_BATCH
        self.group = resources.COUNT_GROUP
        self.line_img = resources.RUNNER_LINE
        self.old_procent = []
        self.old_len = None
        # for i in self.line_img:
        #     self.line_img[i].width = int(SCREEN_WIDTH * 0.80)
        #     self.line_img[i].height = int(SCREEN_HEIGHT * 0.895)

        self.sprites = []

    # def calc_procent(self, procent):
    #     return procent

    def reset(self):
        for i in self.sprites:
            i.delete()
        self.sprites = []
        self.old_procent = []

    def show_procent(self, procent=[], max_len=3):
        # procent = self.calc_procent(procent)
        if self.old_procent != procent or max_len != self.old_len:
            self.old_procent = procent
            self.old_len = max_len
            self.reset()
            if max_len == 2:
                for i in self.line_img:
                    self.line_img[i].width = int(SCREEN_WIDTH * 0.758)
                    if i != 'red':
                        self.line_img[i].height = int(SCREEN_HEIGHT * 0.33)
                    else:
                        self.line_img[i].height = int(SCREEN_HEIGHT * 0.44)
                gradient = -0.013
                red = False
                try:
                    for i in range(procent[0]):
                        if i <= 2:
                            tmp = pyglet.sprite.Sprite(self.line_img['green'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * -0.038, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 5:
                            tmp = pyglet.sprite.Sprite(self.line_img['yellow'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * -0.038, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 7:
                            tmp = pyglet.sprite.Sprite(self.line_img['orange'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * -0.038, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        else:
                            if red == False:
                                red = True
                                gradient -= 0.048
                            tmp = pyglet.sprite.Sprite(self.line_img['red'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * -0.038, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.04
                            self.sprites.append(tmp)
                except IndexError:
                    pass

                gradient = -0.009
                red = False
                try:
                    for i in range(procent[1]):
                        if i <= 2:
                            tmp = pyglet.sprite.Sprite(self.line_img['green'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.297, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 5:
                            tmp = pyglet.sprite.Sprite(self.line_img['yellow'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.297, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 7:
                            tmp = pyglet.sprite.Sprite(self.line_img['orange'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.297, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        else:
                            if red == False:
                                red = True
                                gradient -= 0.048
                            tmp = pyglet.sprite.Sprite(self.line_img['red'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.297, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.04
                            self.sprites.append(tmp)
                except IndexError:
                    pass
            elif max_len == 3:
                for i in self.line_img:
                    self.line_img[i].width = int(SCREEN_WIDTH * 0.485)
                    if i != 'red':
                        self.line_img[i].height = int(SCREEN_HEIGHT * 0.33)
                    else:
                        self.line_img[i].height = int(SCREEN_HEIGHT * 0.44)
                gradient = -0.013
                red = False
                try:
                    for i in range(procent[0]):
                        if i <= 2:
                            tmp = pyglet.sprite.Sprite(self.line_img['green'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH - ( SCREEN_WIDTH * 0.955 ), SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 5:
                            tmp = pyglet.sprite.Sprite(self.line_img['yellow'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH - ( SCREEN_WIDTH * 0.955 ), SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 7:
                            tmp = pyglet.sprite.Sprite(self.line_img['orange'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH - ( SCREEN_WIDTH * 0.955 ), SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        else:
                            if red == False:
                                red = True
                                gradient -= 0.048
                            tmp = pyglet.sprite.Sprite(self.line_img['red'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH - ( SCREEN_WIDTH * 0.955 ), SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.04
                            self.sprites.append(tmp)
                except IndexError:
                    pass
                gradient = -0.009
                red = False
                try:

                    for i in range(procent[1]):
                        if i <= 2:
                            tmp = pyglet.sprite.Sprite(self.line_img['green'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.261, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 5:
                            tmp = pyglet.sprite.Sprite(self.line_img['yellow'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.261, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 7:
                            tmp = pyglet.sprite.Sprite(self.line_img['orange'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.261, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        else:
                            if red == False:
                                red = True
                                gradient -= 0.048
                            tmp = pyglet.sprite.Sprite(self.line_img['red'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.261, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.04
                            self.sprites.append(tmp)
                except IndexError:
                    pass
                gradient = -0.007
                red = False
                try:
                    for i in range(procent[2]):
                        if i <= 2:
                            tmp = pyglet.sprite.Sprite(self.line_img['green'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.478, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 5:
                            tmp = pyglet.sprite.Sprite(self.line_img['yellow'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.478, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 7:
                            tmp = pyglet.sprite.Sprite(self.line_img['orange'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.478, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        else:
                            if red == False:
                                red = True
                                gradient -= 0.048
                            tmp = pyglet.sprite.Sprite(self.line_img['red'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.478, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.04
                            self.sprites.append(tmp)
                except IndexError:
                    pass
            elif max_len == 4:
                for i in self.line_img:
                    self.line_img[i].width = int(SCREEN_WIDTH * 0.36)
                    if i != 'red':
                        self.line_img[i].height = int(SCREEN_HEIGHT * 0.33)
                    else:
                        self.line_img[i].height = int(SCREEN_HEIGHT * 0.44)
                gradient = -0.013
                red = False
                try:
                    for i in range(procent[0]):
                        if i <= 2:
                            tmp = pyglet.sprite.Sprite(self.line_img['green'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 0.917), SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 5:
                            tmp = pyglet.sprite.Sprite(self.line_img['yellow'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 0.917), SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 7:
                            tmp = pyglet.sprite.Sprite(self.line_img['orange'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 0.917), SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        else:
                            if red == False:
                                red = True
                                gradient -= 0.048
                            tmp = pyglet.sprite.Sprite(self.line_img['red'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 0.917), SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.04
                            self.sprites.append(tmp)
                except IndexError:
                    pass
                gradient = -0.009
                red = False
                try:

                    for i in range(procent[1]):
                        if i <= 2:
                            tmp = pyglet.sprite.Sprite(self.line_img['green'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.243, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 5:
                            tmp = pyglet.sprite.Sprite(self.line_img['yellow'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.243, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 7:
                            tmp = pyglet.sprite.Sprite(self.line_img['orange'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.243, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        else:
                            if red == False:
                                red = True
                                gradient -= 0.048
                            tmp = pyglet.sprite.Sprite(self.line_img['red'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.243, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.04
                            self.sprites.append(tmp)
                except IndexError:
                    pass
                gradient = -0.007
                red = False
                try:
                    for i in range(procent[2]):
                        if i <= 2:
                            tmp = pyglet.sprite.Sprite(self.line_img['green'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.402, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 5:
                            tmp = pyglet.sprite.Sprite(self.line_img['yellow'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.402, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 7:
                            tmp = pyglet.sprite.Sprite(self.line_img['orange'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.402, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        else:
                            if red == False:
                                red = True
                                gradient -= 0.048
                            tmp = pyglet.sprite.Sprite(self.line_img['red'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.402, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.04
                            self.sprites.append(tmp)
                except IndexError:
                    pass
                gradient = -0.007
                red = False
                try:
                    for i in range(procent[3]):
                        if i <= 2:
                            tmp = pyglet.sprite.Sprite(self.line_img['green'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.564, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 5:
                            tmp = pyglet.sprite.Sprite(self.line_img['yellow'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.564, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 7:
                            tmp = pyglet.sprite.Sprite(self.line_img['orange'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.564, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        else:
                            if red == False:
                                red = True
                                gradient -= 0.048
                            tmp = pyglet.sprite.Sprite(self.line_img['red'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.564, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.04
                            self.sprites.append(tmp)
                except IndexError:
                    pass
            elif max_len == 5:
                for i in self.line_img:
                    self.line_img[i].width = int(SCREEN_WIDTH * 0.285)
                    if i != 'red':
                        self.line_img[i].height = int(SCREEN_HEIGHT * 0.33)
                    else:
                        self.line_img[i].height = int(SCREEN_HEIGHT * 0.44)
                gradient = -0.013
                red = False
                try:
                    for i in range(procent[0]):
                        if i <= 2:
                            tmp = pyglet.sprite.Sprite(self.line_img['green'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 0.895), SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 5:
                            tmp = pyglet.sprite.Sprite(self.line_img['yellow'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 0.895), SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 7:
                            tmp = pyglet.sprite.Sprite(self.line_img['orange'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 0.895), SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        else:
                            if red == False:
                                red = True
                                gradient -= 0.048
                            tmp = pyglet.sprite.Sprite(self.line_img['red'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 0.895), SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.04
                            self.sprites.append(tmp)
                except IndexError:
                    pass
                gradient = -0.009
                red = False
                try:

                    for i in range(procent[1]):
                        if i <= 2:
                            tmp = pyglet.sprite.Sprite(self.line_img['green'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.232, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 5:
                            tmp = pyglet.sprite.Sprite(self.line_img['yellow'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.232, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 7:
                            tmp = pyglet.sprite.Sprite(self.line_img['orange'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.232, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        else:
                            if red == False:
                                red = True
                                gradient -= 0.048
                            tmp = pyglet.sprite.Sprite(self.line_img['red'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.232, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.04
                            self.sprites.append(tmp)
                except IndexError:
                    pass
                gradient = -0.007
                red = False
                try:
                    for i in range(procent[2]):
                        if i <= 2:
                            tmp = pyglet.sprite.Sprite(self.line_img['green'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.359, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 5:
                            tmp = pyglet.sprite.Sprite(self.line_img['yellow'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.359, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 7:
                            tmp = pyglet.sprite.Sprite(self.line_img['orange'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.359, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        else:
                            if red == False:
                                red = True
                                gradient -= 0.048
                            tmp = pyglet.sprite.Sprite(self.line_img['red'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.359, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.04
                            self.sprites.append(tmp)
                except IndexError:
                    pass
                gradient = -0.007
                red = False
                try:
                    for i in range(procent[3]):
                        if i <= 2:
                            tmp = pyglet.sprite.Sprite(self.line_img['green'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.486, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 5:
                            tmp = pyglet.sprite.Sprite(self.line_img['yellow'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.486, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 7:
                            tmp = pyglet.sprite.Sprite(self.line_img['orange'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.486, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        else:
                            if red == False:
                                red = True
                                gradient -= 0.048
                            tmp = pyglet.sprite.Sprite(self.line_img['red'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.486, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.04
                            self.sprites.append(tmp)
                except IndexError:
                    pass
                gradient = -0.006
                red = False
                try:
                    for i in range(procent[4]):
                        if i <= 2:
                            tmp = pyglet.sprite.Sprite(self.line_img['green'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.612, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 5:
                            tmp = pyglet.sprite.Sprite(self.line_img['yellow'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.612, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        elif i <= 7:
                            tmp = pyglet.sprite.Sprite(self.line_img['orange'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.612, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.023
                            self.sprites.append(tmp)
                        else:
                            if red == False:
                                red = True
                                gradient -= 0.048
                            tmp = pyglet.sprite.Sprite(self.line_img['red'], batch=self.batch, group=self.group)
                            tmp.position = (SCREEN_WIDTH * 0.612, SCREEN_HEIGHT * gradient, 0)
                            gradient += 0.04
                            self.sprites.append(tmp)
                except IndexError:
                    pass

class Main():
    def __init__(self):
        self.color = None
        self.field = Field()
        self.batch = resources.RUNNER_BATCH
        if config.FONT == 1:
            self.value_show = Counter()
        elif config.FONT == 2:
            self.value_show = Counter2()
        else:
            self.value_show = Counter()
        self.bag_field = BagField()
        self.procent = Procent()
        self.x2 = False
        self.device = []
        self.max_len = None
        self.down_on = None
        self.procent_data = None
        self.value = None

    def full_reset(self):
        self.color = None
        self.x2 = False
        self.device = []
        self.max_len = None
        self.down_on = None
        self.field.old_color = None
        self.field.reset()
        self.bag_field.reset()
        self.procent.reset()
        self.procent_data = None
        self.value_show.reset('ALL')
        self.value = None
        self.value_show.values = []

    def show(self, color='red', values=[], device=[], x2=False, procent=[], max_len=3, down_on=''):
        if self.color != color or x2 != self.x2 or device != self.device or max_len != self.max_len or down_on != self.down_on:
            self.full_reset()

            self.x2 = x2
            self.device = device
            self.max_len = max_len
            self.down_on = down_on
            self.field.old_color = color
            self.field.set_field(x2)
            self.color = color
            self.bag_field.show_mashine(color=color, device=device, max_len=max_len, down_on=down_on)
        tmp = []
        for i in values:
            tmp.append("{:.2f}".format(i))

        if self.procent_data != procent:
            self.procent_data = procent
            self.procent.show_procent(procent=procent, max_len=max_len)
        if self.value != tmp:
            self.value = tmp
            self.value_show.show(color=self.color, values=values)
            self.value_show.values = tmp
        self.batch.draw()