# -*- coding:utf-8 -*-
import pyglet
import time
import resources
import config

SCREEN_WIDTH = resources.SCREEN_WIDTH
SCREEN_HEIGHT = resources.SCREEN_HEIGHT

class Values():
    def __init__(self):
        self.batch = resources.COUNTERS_BATCH
        self.group = resources.COUNT_GROUP
        self.duration=0.01
        self.micro = config.VISUAL_MICRO
        self.values = []
        self.mega_sprite = []
        self.mega_anime = []
        self.mega_activ = False
        self.grand_sprite = []
        self.grand_anime = []
        self.grand_activ = False
        self.major_sprite = []
        self.major_anime = []
        self.major_activ = False
        self.minor_sprite = []
        self.minor_anime = []
        self.minor_activ = False
        self.mini_sprite = []
        self.mini_anime = []
        self.mini_activ = False
        self.position = resources.COUNTERS_INDEX
        self.counters_anime = resources.COUNTERS
        self.point_sum = 0

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
        #     i.width = int(SCREEN_WIDTH * 0.5)
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
        except AttributeError as e:
            pass

    def format(self, values=[]):
        tmp = []
        for i in values:
            tmp.append("{:.2f}".format(i))
        return tmp

    def one_show(self, values=[]):
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
                    mega_point_show = True
                    self.mega_sprite[i].position = (SCREEN_WIDTH * (gradient+self.point_sum), SCREEN_HEIGHT * mega_height, 0)
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
                        mega_point_show = True
                        self.mega_sprite[i].position = (
                        SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * mega_height, 0)
                    else:
                        self.mega_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mega_height, 0)
                    if mega_point_show == False:
                        gradient += 0.044
                    else:
                        gradient += 0.012
                        mega_point_show = False

    def tow_show(self, values=[]):
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
                    gradient += 0.047
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
                        gradient += 0.047
                    else:
                        gradient += 0.012
                        mega_point_show = False

        #===============================================================================================================
        # GRAND
        # ==============================================================================================================
        gradient = 0.39
        grand_height = 0.355

        if len(self.values) == 0:

            self.reset(self.grand_sprite)

            for i in range(len(values[1]) - 3):
                gradient -= 0.02
            if len(values[1]) == 10:
                gradient += 0.01
            if len(values[1]) == 9:
                gradient += 0.02
            if len(values[1]) == 8:
                gradient += 0.02
            if len(values[1]) == 7:
                gradient += 0.03
            if len(values[1]) == 6:
                gradient += 0.04
            if len(values[1]) == 5:
                gradient += 0.05
            if len(values[1]) == 4:
                gradient += 0.06

            for i in values[1]:
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

            for i in range(len(values[1])):
                if i == 2 and len(values[1]) > 10:
                    gradient += 0.03
                if i == 5 and len(values[1]) > 10:
                    gradient += 0.03

                if i == 1 and len(values[1]) == 10:
                    gradient += 0.03
                if i == 4 and len(values[1]) == 10:
                    gradient += 0.03

                if i == 3 and len(values[1]) == 9:
                    gradient += 0.03

                if i == 2 and len(values[1]) == 8:
                    gradient += 0.03

                if i == 1 and len(values[1]) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[1]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[1]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[1]) == 9:
                #     gradient += 0.03

                if self.grand_sprite[i] == grand_point_object:
                    self.grand_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * grand_height, 0)
                    grand_point_show = True
                else:
                    self.grand_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * grand_height, 0)
                if grand_point_show == False:
                    gradient += 0.047
                else:
                    gradient += 0.012
                    grand_point_show = False
            # self.values.append(values[1])
            # print(type(self.values[1]), type(values[1]))
            # return
        else:
            # gradient = 0.39
            # grand_height = 0.355
            if self.values[1] != values[1]:

                # while True:
                #     if self.grand_anime:
                #         pass
                #     else:
                #         break
                self.reset(self.grand_sprite)
                self.grand_sprite = []
                for i in range(len(values[1]) - 3):
                    gradient -= 0.02
                if len(values[1]) == 10:
                    gradient += 0.01
                if len(values[1]) == 9:
                    gradient += 0.02
                if len(values[1]) == 8:
                    gradient += 0.02
                if len(values[1]) == 7:
                    gradient += 0.03
                if len(values[1]) == 6:
                    gradient += 0.04
                if len(values[1]) == 5:
                    gradient += 0.05
                if len(values[1]) == 4:
                    gradient += 0.06
                count = 0
                for i in values[1]:

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
                        if self.values[1][count] == '.':
                            count -= 1
                        if self.grand_activ == True:
                            if self.micro is False:
                                if self.position[self.values[1][count]] > self.position[i]:
                                    for b in range(self.position[self.values[1][count]], self.position['10']):
                                        img.append(self.counters_anime['grand'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['grand'][b])
                                else:
                                    for b in range(self.position[self.values[1][count]], self.position[i]):
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
                            if self.values[1][count] == '.':
                                count -= 1
                            if self.micro is False:
                                if self.position[self.values[1][count]] > self.position[i]:
                                    for b in range(self.position[self.values[1][count]], self.position['10']):
                                        img.append(self.counters_anime['gray'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])
                                else:
                                    for b in range(self.position[self.values[1][count]], self.position[i]):
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
                for i in range(len(values[1])):
                    if i == 2 and len(values[1]) > 10:
                        gradient += 0.03
                    if i == 5 and len(values[1]) > 10:
                        gradient += 0.03

                    if i == 1 and len(values[1]) == 10:
                        gradient += 0.03
                    if i == 4 and len(values[1]) == 10:
                        gradient += 0.03

                    if i == 3 and len(values[1]) == 9:
                        gradient += 0.03

                    if i == 2 and len(values[1]) == 8:
                        gradient += 0.03

                    if i == 1 and len(values[1]) == 7:
                        gradient += 0.03
                    if self.grand_sprite[i] == grand_point_object:
                        self.grand_sprite[i].position = (
                        SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * grand_height, 0)
                        grand_point_show = True
                    else:
                        self.grand_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * grand_height, 0)
                    if grand_point_show == False:
                        gradient += 0.047
                    else:
                        gradient += 0.012
                        grand_point_show = False


    def free_show(self, values=[]):
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
                self.mega_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mega_height, 0)
                if self.mega_sprite[i] == mega_point_object:
                    self.mega_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * mega_height, 0)
                    mega_point_show = True
                else:
                    self.mega_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mega_height, 0)
                if mega_point_show == False:
                    gradient += 0.047
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
                        gradient += 0.047
                    else:
                        gradient += 0.012
                        mega_point_show = False

        # ===============================================================================================================
        # GRAND
        # ==============================================================================================================
        gradient = 0.39
        grand_height = 0.355

        if len(self.values) == 0:

            self.reset(self.grand_sprite)

            for i in range(len(values[1]) - 3):
                gradient -= 0.02
            if len(values[1]) == 10:
                gradient += 0.01
            if len(values[1]) == 9:
                gradient += 0.02
            if len(values[1]) == 8:
                gradient += 0.02
            if len(values[1]) == 7:
                gradient += 0.03
            if len(values[1]) == 6:
                gradient += 0.04
            if len(values[1]) == 5:
                gradient += 0.05
            if len(values[1]) == 4:
                gradient += 0.06

            for i in values[1]:
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

            for i in range(len(values[1])):
                if i == 2 and len(values[1]) > 10:
                    gradient += 0.03
                if i == 5 and len(values[1]) > 10:
                    gradient += 0.03

                if i == 1 and len(values[1]) == 10:
                    gradient += 0.03
                if i == 4 and len(values[1]) == 10:
                    gradient += 0.03

                if i == 3 and len(values[1]) == 9:
                    gradient += 0.03

                if i == 2 and len(values[1]) == 8:
                    gradient += 0.03

                if i == 1 and len(values[1]) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[1]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[1]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[1]) == 9:
                #     gradient += 0.03

                if self.grand_sprite[i] == grand_point_object:
                    self.grand_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * grand_height, 0)
                    grand_point_show = True
                else:
                    self.grand_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * grand_height, 0)
                if grand_point_show == False:
                    gradient += 0.047
                else:
                    gradient += 0.012
                    grand_point_show = False
            # self.values.append(values[1])
            # print(type(self.values[1]), type(values[1]))
            # return
        else:
            if self.values[1] != values[1]:

                # while True:
                #     if self.grand_anime:
                #         pass
                #     else:
                #         break
                self.reset(self.grand_sprite)
                self.grand_sprite = []
                for i in range(len(values[1]) - 3):
                    gradient -= 0.02
                if len(values[1]) == 10:
                    gradient += 0.01
                if len(values[1]) == 9:
                    gradient += 0.02
                if len(values[1]) == 8:
                    gradient += 0.02
                if len(values[1]) == 7:
                    gradient += 0.03
                if len(values[1]) == 6:
                    gradient += 0.04
                if len(values[1]) == 5:
                    gradient += 0.05
                if len(values[1]) == 4:
                    gradient += 0.06
                count = 0
                for i in values[1]:

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
                        if self.values[1][count] == '.':
                            count -= 1
                        if self.grand_activ == True:
                            if self.micro is False:
                                if self.position[self.values[1][count]] > self.position[i]:
                                    for b in range(self.position[self.values[1][count]], self.position['10']):
                                        img.append(self.counters_anime['grand'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['grand'][b])
                                else:
                                    for b in range(self.position[self.values[1][count]], self.position[i]):
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
                            if self.values[1][count] == '.':
                                count -= 1
                            if self.micro is False:
                                if self.position[self.values[1][count]] > self.position[i]:
                                    for b in range(self.position[self.values[1][count]], self.position['10']):
                                        img.append(self.counters_anime['gray'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])
                                else:
                                    for b in range(self.position[self.values[1][count]], self.position[i]):
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
                for i in range(len(values[1])):
                    if i == 2 and len(values[1]) > 10:
                        gradient += 0.03
                    if i == 5 and len(values[1]) > 10:
                        gradient += 0.03

                    if i == 1 and len(values[1]) == 10:
                        gradient += 0.03
                    if i == 4 and len(values[1]) == 10:
                        gradient += 0.03

                    if i == 3 and len(values[1]) == 9:
                        gradient += 0.03

                    if i == 2 and len(values[1]) == 8:
                        gradient += 0.03

                    if i == 1 and len(values[1]) == 7:
                        gradient += 0.03
                    if self.grand_sprite[i] == grand_point_object:
                        self.grand_sprite[i].position = (
                        SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * grand_height, 0)
                        grand_point_show = True
                    else:
                        self.grand_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * grand_height, 0)
                    if grand_point_show == False:
                        gradient += 0.047
                    else:
                        gradient += 0.012
                        grand_point_show = False
        #===============================================================================================================
        # Major
        #===============================================================================================================
        gradient = 0.385
        major_height = 0.085

        if len(self.values) == 0:

            self.reset(self.major_sprite)

            for i in range(len(values[2]) - 3):
                gradient -= 0.02
            if len(values[2]) == 10:
                gradient += 0.01
            if len(values[2]) == 9:
                gradient += 0.02
            if len(values[2]) == 8:
                gradient += 0.02
            if len(values[2]) == 7:
                gradient += 0.03
            if len(values[2]) == 6:
                gradient += 0.04
            if len(values[2]) == 5:
                gradient += 0.05
            if len(values[2]) == 4:
                gradient += 0.06

            for i in values[2]:
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

            for i in range(len(values[2])):
                if i == 2 and len(values[2]) > 10:
                    gradient += 0.03
                if i == 5 and len(values[2]) > 10:
                    gradient += 0.03

                if i == 1 and len(values[2]) == 10:
                    gradient += 0.03
                if i == 4 and len(values[2]) == 10:
                    gradient += 0.03

                if i == 3 and len(values[2]) == 9:
                    gradient += 0.03

                if i == 2 and len(values[2]) == 8:
                    gradient += 0.03

                if i == 1 and len(values[2]) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[2]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[2]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[2]) == 9:
                #     gradient += 0.03
                self.major_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * major_height, 0)
                if self.major_sprite[i] == major_point_object:
                    self.major_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * major_height, 0)
                    major_point_show = True
                else:
                    self.major_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * major_height, 0)
                if major_point_show == False:
                    gradient += 0.047
                else:
                    gradient += 0.012
                    major_point_show = False     
            # self.values.append(values[2])
            # print(type(self.values[2]), type(values[2]))
            # return
        else:
            if self.values[2] != values[2]:

                # while True:
                #     if self.major_anime:
                #         pass
                #     else:
                #         break
                self.reset(self.major_sprite)
                self.major_sprite = []
                for i in range(len(values[2]) - 3):
                    gradient -= 0.02
                if len(values[2]) == 10:
                    gradient += 0.01
                if len(values[2]) == 9:
                    gradient += 0.02
                if len(values[2]) == 8:
                    gradient += 0.02
                if len(values[2]) == 7:
                    gradient += 0.03
                if len(values[2]) == 6:
                    gradient += 0.04
                if len(values[2]) == 5:
                    gradient += 0.05
                if len(values[2]) == 4:
                    gradient += 0.06
                count = 0
                for i in values[2]:

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
                        if self.values[2][count] == '.':
                            count -= 1
                        if self.major_activ == True:
                            if self.micro is False:
                                if self.position[self.values[2][count]] > self.position[i]:
                                    for b in range(self.position[self.values[2][count]], self.position['10']):
                                        img.append(self.counters_anime['major'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['major'][b])
                                else:
                                    for b in range(self.position[self.values[2][count]], self.position[i]):
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
                            if self.values[2][count] == '.':
                                count -= 1
                            if self.micro is False:
                                if self.position[self.values[2][count]] > self.position[i]:
                                    for b in range(self.position[self.values[2][count]], self.position['10']):
                                        img.append(self.counters_anime['gray'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])
                                else:
                                    for b in range(self.position[self.values[2][count]], self.position[i]):
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
                for i in range(len(values[2])):
                    if i == 2 and len(values[2]) > 10:
                        gradient += 0.03
                    if i == 5 and len(values[2]) > 10:
                        gradient += 0.03

                    if i == 1 and len(values[2]) == 10:
                        gradient += 0.03
                    if i == 4 and len(values[2]) == 10:
                        gradient += 0.03

                    if i == 3 and len(values[2]) == 9:
                        gradient += 0.03

                    if i == 2 and len(values[2]) == 8:
                        gradient += 0.03

                    if i == 1 and len(values[2]) == 7:
                        gradient += 0.03
                    if self.major_sprite[i] == major_point_object:
                        self.major_sprite[i].position = (
                        SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * major_height, 0)
                        major_point_show = True
                    else:
                        self.major_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * major_height, 0)
                    if major_point_show == False:
                        gradient += 0.047
                    else:
                        gradient += 0.012
                        major_point_show = False

    def for_show(self, values=[]):
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
                    gradient += 0.047
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
                # values[4]
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
                        gradient += 0.047
                    else:
                        gradient += 0.012
                        mega_point_show = False

        # ===============================================================================================================
        # GRAND
        # ==============================================================================================================
        gradient = 0.39
        grand_height = 0.355

        if len(self.values) == 0:

            self.reset(self.grand_sprite)

            for i in range(len(values[1]) - 3):
                gradient -= 0.02
            if len(values[1]) == 10:
                gradient += 0.01
            if len(values[1]) == 9:
                gradient += 0.02
            if len(values[1]) == 8:
                gradient += 0.02
            if len(values[1]) == 7:
                gradient += 0.03
            if len(values[1]) == 6:
                gradient += 0.04
            if len(values[1]) == 5:
                gradient += 0.05
            if len(values[1]) == 4:
                gradient += 0.06

            for i in values[1]:
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

            for i in range(len(values[1])):
                if i == 2 and len(values[1]) > 10:
                    gradient += 0.03
                if i == 5 and len(values[1]) > 10:
                    gradient += 0.03

                if i == 1 and len(values[1]) == 10:
                    gradient += 0.03
                if i == 4 and len(values[1]) == 10:
                    gradient += 0.03

                if i == 3 and len(values[1]) == 9:
                    gradient += 0.03

                if i == 2 and len(values[1]) == 8:
                    gradient += 0.03

                if i == 1 and len(values[1]) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[1]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[1]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[1]) == 9:
                #     gradient += 0.03

                if self.grand_sprite[i] == grand_point_object:
                    self.grand_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * grand_height, 0)
                    grand_point_show = True
                else:
                    self.grand_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * grand_height, 0)
                if grand_point_show == False:
                    gradient += 0.047
                else:
                    gradient += 0.012
                    grand_point_show = False
            # self.values.append(values[1])
            # print(type(self.values[1]), type(values[1]))
            # return
        else:
            if self.values[1] != values[1]:

                # while True:
                #     if self.grand_anime:
                #         pass
                #     else:
                #         break
                self.reset(self.grand_sprite)
                self.grand_sprite = []
                for i in range(len(values[1]) - 3):
                    gradient -= 0.02
                if len(values[1]) == 10:
                    gradient += 0.01
                if len(values[1]) == 9:
                    gradient += 0.02
                if len(values[1]) == 8:
                    gradient += 0.02
                if len(values[1]) == 7:
                    gradient += 0.03
                if len(values[1]) == 6:
                    gradient += 0.04
                if len(values[1]) == 5:
                    gradient += 0.05
                if len(values[1]) == 4:
                    gradient += 0.06
                count = 0
                for i in values[1]:

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
                        if self.values[1][count] == '.':
                            count -= 1
                        if self.grand_activ == True:
                            if self.micro is False:
                                if self.position[self.values[1][count]] > self.position[i]:
                                    for b in range(self.position[self.values[1][count]], self.position['10']):
                                        img.append(self.counters_anime['grand'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['grand'][b])
                                else:
                                    for b in range(self.position[self.values[1][count]], self.position[i]):
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
                            if self.values[1][count] == '.':
                                count -= 1
                            if self.micro is False:
                                if self.position[self.values[1][count]] > self.position[i]:
                                    for b in range(self.position[self.values[1][count]], self.position['10']):
                                        img.append(self.counters_anime['gray'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])
                                else:
                                    for b in range(self.position[self.values[1][count]], self.position[i]):
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
                for i in range(len(values[1])):
                    if i == 2 and len(values[1]) > 10:
                        gradient += 0.03
                    if i == 5 and len(values[1]) > 10:
                        gradient += 0.03

                    if i == 1 and len(values[1]) == 10:
                        gradient += 0.03
                    if i == 4 and len(values[1]) == 10:
                        gradient += 0.03

                    if i == 3 and len(values[1]) == 9:
                        gradient += 0.03

                    if i == 2 and len(values[1]) == 8:
                        gradient += 0.03

                    if i == 1 and len(values[1]) == 7:
                        gradient += 0.03
                    if self.grand_sprite[i] == grand_point_object:
                        self.grand_sprite[i].position = (
                        SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * grand_height, 0)
                        grand_point_show = True
                    else:
                        self.grand_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * grand_height, 0)
                    if grand_point_show == False:
                        gradient += 0.047
                    else:
                        gradient += 0.012
                        grand_point_show = False
        # ===============================================================================================================
        # Major
        # ===============================================================================================================
        gradient = 0.145
        major_height = 0.085

        if len(self.values) == 0:

            self.reset(self.major_sprite)

            for i in range(len(values[2]) - 3):
                gradient -= 0.02
            if len(values[2]) == 10:
                gradient += 0.01
            if len(values[2]) == 9:
                gradient += 0.02
            if len(values[2]) == 8:
                gradient += 0.02
            if len(values[2]) == 7:
                gradient += 0.03
            if len(values[2]) == 6:
                gradient += 0.04
            if len(values[2]) == 5:
                gradient += 0.05
            if len(values[2]) == 4:
                gradient += 0.06

            for i in values[2]:
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

            for i in range(len(values[2])):
                if i == 2 and len(values[2]) > 10:
                    gradient += 0.03
                if i == 5 and len(values[2]) > 10:
                    gradient += 0.03

                if i == 1 and len(values[2]) == 10:
                    gradient += 0.03
                if i == 4 and len(values[2]) == 10:
                    gradient += 0.03

                if i == 3 and len(values[2]) == 9:
                    gradient += 0.03

                if i == 2 and len(values[2]) == 8:
                    gradient += 0.03

                if i == 1 and len(values[2]) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[2]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[2]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[2]) == 9:
                #     gradient += 0.03
                if self.major_sprite[i] == major_point_object:
                    self.major_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * major_height, 0)
                    major_point_show = True
                else:
                    self.major_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * major_height, 0)
                if major_point_show == False:
                    gradient += 0.047
                else:
                    gradient += 0.012
                    major_point_show = False
                    # self.values.append(values[2])
            # print(type(self.values[2]), type(values[2]))
            # return
        else:
            if self.values[2] != values[2]:

                # while True:
                #     if self.major_anime:
                #         pass
                #     else:
                #         break
                self.reset(self.major_sprite)
                self.major_sprite = []
                for i in range(len(values[2]) - 3):
                    gradient -= 0.02
                if len(values[2]) == 10:
                    gradient += 0.01
                if len(values[2]) == 9:
                    gradient += 0.02
                if len(values[2]) == 8:
                    gradient += 0.02
                if len(values[2]) == 7:
                    gradient += 0.03
                if len(values[2]) == 6:
                    gradient += 0.04
                if len(values[2]) == 5:
                    gradient += 0.05
                if len(values[2]) == 4:
                    gradient += 0.06
                count = 0
                for i in values[2]:

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
                        if self.values[2][count] == '.':
                            count -= 1
                        if self.major_activ == True:
                            if self.micro is False:
                                if self.position[self.values[2][count]] > self.position[i]:
                                    for b in range(self.position[self.values[2][count]], self.position['10']):
                                        img.append(self.counters_anime['major'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['major'][b])
                                else:
                                    for b in range(self.position[self.values[2][count]], self.position[i]):
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
                            if self.values[2][count] == '.':
                                count -= 1
                            if self.micro is False:
                                if self.position[self.values[2][count]] > self.position[i]:
                                    for b in range(self.position[self.values[2][count]], self.position['10']):
                                        img.append(self.counters_anime['gray'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])
                                else:
                                    for b in range(self.position[self.values[2][count]], self.position[i]):
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
                for i in range(len(values[2])):
                    if i == 2 and len(values[2]) > 10:
                        gradient += 0.03
                    if i == 5 and len(values[2]) > 10:
                        gradient += 0.03

                    if i == 1 and len(values[2]) == 10:
                        gradient += 0.03
                    if i == 4 and len(values[2]) == 10:
                        gradient += 0.03

                    if i == 3 and len(values[2]) == 9:
                        gradient += 0.03

                    if i == 2 and len(values[2]) == 8:
                        gradient += 0.03

                    if i == 1 and len(values[2]) == 7:
                        gradient += 0.03
                    if self.major_sprite[i] == major_point_object:
                        self.major_sprite[i].position = (
                        SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * major_height, 0)
                        major_point_show = True
                    else:
                        self.major_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * major_height, 0)
                    if major_point_show == False:
                        gradient += 0.047
                    else:
                        gradient += 0.012
                        major_point_show = False

        # ===============================================================================================================
        # MINOR
        # ===============================================================================================================
        gradient = 0.65
        minor_height = 0.085

        if len(self.values) == 0:

            self.reset(self.minor_sprite)

            for i in range(len(values[3]) - 3):
                gradient -= 0.02
            if len(values[3]) == 10:
                gradient += 0.01
            if len(values[3]) == 9:
                gradient += 0.02
            if len(values[3]) == 8:
                gradient += 0.02
            if len(values[3]) == 7:
                gradient += 0.03
            if len(values[3]) == 6:
                gradient += 0.04
            if len(values[3]) == 5:
                gradient += 0.05
            if len(values[3]) == 4:
                gradient += 0.06

            for i in values[3]:
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
                    if self.minor_activ == True:
                        self.minor_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['minor'][self.position[i]],
                                                 batch=self.batch,
                                                 group=self.group))
                    else:
                        self.minor_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['gray'][self.position[i]],
                                                 batch=self.batch,
                                                 group=self.group))
            minor_point_show = False

            for i in range(len(values[3])):
                if i == 2 and len(values[3]) > 10:
                    gradient += 0.03
                if i == 5 and len(values[3]) > 10:
                    gradient += 0.03

                if i == 1 and len(values[3]) == 10:
                    gradient += 0.03
                if i == 4 and len(values[3]) == 10:
                    gradient += 0.03

                if i == 3 and len(values[3]) == 9:
                    gradient += 0.03

                if i == 2 and len(values[3]) == 8:
                    gradient += 0.03

                if i == 1 and len(values[3]) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[3]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[3]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[3]) == 9:
                #     gradient += 0.03

                if self.minor_sprite[i] == minor_point_object:
                    self.minor_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * minor_height, 0)
                    minor_point_show = True
                else:
                    self.minor_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * minor_height, 0)
                if minor_point_show == False:
                    gradient += 0.047
                else:
                    gradient += 0.012
                    minor_point_show = False
                    # self.values.append(values[3])
            # print(type(self.values[3]), type(values[3]))
            # return
        else:
            if self.values[3] != values[3]:

                # while True:
                #     if self.minor_anime:
                #         pass
                #     else:
                #         break
                self.reset(self.minor_sprite)
                self.minor_sprite = []
                for i in range(len(values[3]) - 3):
                    gradient -= 0.02
                if len(values[3]) == 10:
                    gradient += 0.01
                if len(values[3]) == 9:
                    gradient += 0.02
                if len(values[3]) == 8:
                    gradient += 0.02
                if len(values[3]) == 7:
                    gradient += 0.03
                if len(values[3]) == 6:
                    gradient += 0.04
                if len(values[3]) == 5:
                    gradient += 0.05
                if len(values[3]) == 4:
                    gradient += 0.06
                count = 0
                for i in values[3]:

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
                        if self.values[3][count] == '.':
                            count -= 1
                        if self.minor_activ == True:
                            if self.micro is False:
                                if self.position[self.values[3][count]] > self.position[i]:
                                    for b in range(self.position[self.values[3][count]], self.position['10']):
                                        img.append(self.counters_anime['minor'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['minor'][b])
                                else:
                                    for b in range(self.position[self.values[3][count]], self.position[i]):
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
                            if self.values[3][count] == '.':
                                count -= 1
                            if self.micro is False:
                                if self.position[self.values[3][count]] > self.position[i]:
                                    for b in range(self.position[self.values[3][count]], self.position['10']):
                                        img.append(self.counters_anime['gray'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])
                                else:
                                    for b in range(self.position[self.values[3][count]], self.position[i]):
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
                for i in range(len(values[3])):
                    if i == 2 and len(values[3]) > 10:
                        gradient += 0.03
                    if i == 5 and len(values[3]) > 10:
                        gradient += 0.03

                    if i == 1 and len(values[3]) == 10:
                        gradient += 0.03
                    if i == 4 and len(values[3]) == 10:
                        gradient += 0.03

                    if i == 3 and len(values[3]) == 9:
                        gradient += 0.03

                    if i == 2 and len(values[3]) == 8:
                        gradient += 0.03

                    if i == 1 and len(values[3]) == 7:
                        gradient += 0.03
                    if self.minor_sprite[i] == minor_point_object:
                        self.minor_sprite[i].position = (
                        SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * minor_height, 0)
                        minor_point_show = True
                    else:
                        self.minor_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * minor_height, 0)
                    if minor_point_show == False:
                        gradient += 0.047
                    else:
                        gradient += 0.012
                        minor_point_show = False

    def five_show(self, values=[]):
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
                    gradient += 0.047
                else:
                    gradient += 0.012
                    mega_point_show = False
            # self.values.append(values[0])
            # print(type(self.values[0]), type(values[0]))
            # return
        else:
            gradient = 0.40
            # if self.mega_activ == False or config.VISUAL_MICRO is True:
            #     mega_height = 0.705
            # else:
            # raise KeyError
            mega_height = 0.625
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
                        gradient += 0.047
                    else:
                        gradient += 0.012
                        mega_point_show = False

        # ===============================================================================================================
        # GRAND
        # ==============================================================================================================
        gradient = 0.143
        grand_height = 0.355

        if len(self.values) == 0:

            self.reset(self.grand_sprite)

            for i in range(len(values[1]) - 3):
                gradient -= 0.02
            if len(values[1]) == 10:
                gradient += 0.01
            if len(values[1]) == 9:
                gradient += 0.02
            if len(values[1]) == 8:
                gradient += 0.02
            if len(values[1]) == 7:
                gradient += 0.03
            if len(values[1]) == 6:
                gradient += 0.04
            if len(values[1]) == 5:
                gradient += 0.05
            if len(values[1]) == 4:
                gradient += 0.06

            for i in values[1]:
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

            for i in range(len(values[1])):
                if i == 2 and len(values[1]) > 10:
                    gradient += 0.03
                if i == 5 and len(values[1]) > 10:
                    gradient += 0.03

                if i == 1 and len(values[1]) == 10:
                    gradient += 0.03
                if i == 4 and len(values[1]) == 10:
                    gradient += 0.03

                if i == 3 and len(values[1]) == 9:
                    gradient += 0.03

                if i == 2 and len(values[1]) == 8:
                    gradient += 0.03

                if i == 1 and len(values[1]) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[1]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[1]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[1]) == 9:
                #     gradient += 0.03

                if self.grand_sprite[i] == grand_point_object:
                    self.grand_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * grand_height, 0)
                    grand_point_show = True
                else:
                    self.grand_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * grand_height, 0)
                if grand_point_show == False:
                    gradient += 0.047
                else:
                    gradient += 0.012
                    grand_point_show = False
                    # self.values.append(values[1])
            # print(type(self.values[1]), type(values[1]))
            # return
        else:
            if self.values[1] != values[1]:

                # while True:
                #     if self.grand_anime:
                #         pass
                #     else:
                #         break
                self.reset(self.grand_sprite)
                self.grand_sprite = []
                for i in range(len(values[1]) - 3):
                    gradient -= 0.02
                if len(values[1]) == 10:
                    gradient += 0.01
                if len(values[1]) == 9:
                    gradient += 0.02
                if len(values[1]) == 8:
                    gradient += 0.02
                if len(values[1]) == 7:
                    gradient += 0.03
                if len(values[1]) == 6:
                    gradient += 0.04
                if len(values[1]) == 5:
                    gradient += 0.05
                if len(values[1]) == 4:
                    gradient += 0.06
                count = 0
                for i in values[1]:

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
                        if self.values[1][count] == '.':
                            count -= 1
                        if self.grand_activ == True:
                            if self.micro is False:
                                if self.position[self.values[1][count]] > self.position[i]:
                                    for b in range(self.position[self.values[1][count]], self.position['10']):
                                        img.append(self.counters_anime['grand'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['grand'][b])
                                else:
                                    for b in range(self.position[self.values[1][count]], self.position[i]):
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
                            if self.values[1][count] == '.':
                                count -= 1
                            if self.micro is False:
                                if self.position[self.values[1][count]] > self.position[i]:
                                    for b in range(self.position[self.values[1][count]], self.position['10']):
                                        img.append(self.counters_anime['gray'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])
                                else:
                                    for b in range(self.position[self.values[1][count]], self.position[i]):
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
                for i in range(len(values[1])):
                    if i == 2 and len(values[1]) > 10:
                        gradient += 0.03
                    if i == 5 and len(values[1]) > 10:
                        gradient += 0.03

                    if i == 1 and len(values[1]) == 10:
                        gradient += 0.03
                    if i == 4 and len(values[1]) == 10:
                        gradient += 0.03

                    if i == 3 and len(values[1]) == 9:
                        gradient += 0.03

                    if i == 2 and len(values[1]) == 8:
                        gradient += 0.03

                    if i == 1 and len(values[1]) == 7:
                        gradient += 0.03
                    if self.grand_sprite[i] == grand_point_object:
                        self.grand_sprite[i].position = (
                        SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * grand_height, 0)
                        grand_point_show = True
                    else:
                        self.grand_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * grand_height, 0)
                    if grand_point_show == False:
                        gradient += 0.047
                    else:
                        gradient += 0.012
                        grand_point_show = False
        # ===============================================================================================================
        # MAJOR
        # ===============================================================================================================
        gradient = 0.65
        major_height = 0.355

        if len(self.values) == 0:

            self.reset(self.major_sprite)

            for i in range(len(values[2]) - 3):
                gradient -= 0.02
            if len(values[2]) == 10:
                gradient += 0.01
            if len(values[2]) == 9:
                gradient += 0.02
            if len(values[2]) == 8:
                gradient += 0.02
            if len(values[2]) == 7:
                gradient += 0.03
            if len(values[2]) == 6:
                gradient += 0.04
            if len(values[2]) == 5:
                gradient += 0.05
            if len(values[2]) == 4:
                gradient += 0.06

            for i in values[2]:
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
                    if self.major_activ == True:
                        self.major_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['major'][self.position[i]],
                                                 batch=self.batch,
                                                 group=self.group))
                    else:
                        self.major_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['gray'][self.position[i]],
                                                 batch=self.batch,
                                                 group=self.group))
            major_point_show = False

            for i in range(len(values[2])):
                if i == 2 and len(values[2]) > 10:
                    gradient += 0.03
                if i == 5 and len(values[2]) > 10:
                    gradient += 0.03

                if i == 1 and len(values[2]) == 10:
                    gradient += 0.03
                if i == 4 and len(values[2]) == 10:
                    gradient += 0.03

                if i == 3 and len(values[2]) == 9:
                    gradient += 0.03

                if i == 2 and len(values[2]) == 8:
                    gradient += 0.03

                if i == 1 and len(values[2]) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[2]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[2]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[2]) == 9:
                #     gradient += 0.03

                if self.major_sprite[i] == major_point_object:
                    self.major_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * major_height, 0)
                    major_point_show = True
                else:
                    self.major_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * major_height, 0)
                if major_point_show == False:
                    gradient += 0.047
                else:
                    gradient += 0.012
                    major_point_show = False
                    # self.values.append(values[2])
            # print(type(self.values[2]), type(values[2]))
            # return
        else:
            # if self.major_activ == False or config.VISUAL_MICRO is True:
            #     major_height = 0.705
            # else:
            # raise KeyError
            # major_height = 0.355
            if self.values[2] != values[2]:

                # while True:
                #     if self.major_anime:
                #         pass
                #     else:
                #         break
                self.reset(self.major_sprite)
                self.major_sprite = []
                for i in range(len(values[2]) - 3):
                    gradient -= 0.02
                if len(values[2]) == 10:
                    gradient += 0.01
                if len(values[2]) == 9:
                    gradient += 0.02
                if len(values[2]) == 8:
                    gradient += 0.02
                if len(values[2]) == 7:
                    gradient += 0.03
                if len(values[2]) == 6:
                    gradient += 0.04
                if len(values[2]) == 5:
                    gradient += 0.05
                if len(values[2]) == 4:
                    gradient += 0.06
                count = 0
                for i in values[2]:

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
                        if self.values[2][count] == '.':
                            count -= 1
                        if self.major_activ == True:
                            if self.micro is False:
                                if self.position[self.values[2][count]] > self.position[i]:
                                    for b in range(self.position[self.values[2][count]], self.position['10']):
                                        img.append(self.counters_anime['major'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['major'][b])
                                else:
                                    for b in range(self.position[self.values[2][count]], self.position[i]):
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
                            if self.values[2][count] == '.':
                                count -= 1
                            if self.micro is False:
                                if self.position[self.values[2][count]] > self.position[i]:
                                    for b in range(self.position[self.values[2][count]], self.position['10']):
                                        img.append(self.counters_anime['gray'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])
                                else:
                                    for b in range(self.position[self.values[2][count]], self.position[i]):
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
                for i in range(len(values[2])):
                    if i == 2 and len(values[2]) > 10:
                        gradient += 0.03
                    if i == 5 and len(values[2]) > 10:
                        gradient += 0.03

                    if i == 1 and len(values[2]) == 10:
                        gradient += 0.03
                    if i == 4 and len(values[2]) == 10:
                        gradient += 0.03

                    if i == 3 and len(values[2]) == 9:
                        gradient += 0.03

                    if i == 2 and len(values[2]) == 8:
                        gradient += 0.03

                    if i == 1 and len(values[2]) == 7:
                        gradient += 0.03
                    if self.major_sprite[i] == major_point_object:
                        self.major_sprite[i].position = (
                        SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * major_height, 0)
                        major_point_show = True
                    else:
                        self.major_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * major_height, 0)
                    if major_point_show == False:
                        gradient += 0.047
                    else:
                        gradient += 0.012
                        major_point_show = False
        # ===============================================================================================================
        # MINOR
        # ===============================================================================================================
        gradient = 0.15
        minor_height = 0.085

        if len(self.values) == 0:

            self.reset(self.minor_sprite)

            for i in range(len(values[3]) - 3):
                gradient -= 0.02
            if len(values[3]) == 10:
                gradient += 0.01
            if len(values[3]) == 9:
                gradient += 0.02
            if len(values[3]) == 8:
                gradient += 0.02
            if len(values[3]) == 7:
                gradient += 0.03
            if len(values[3]) == 6:
                gradient += 0.04
            if len(values[3]) == 5:
                gradient += 0.05
            if len(values[3]) == 4:
                gradient += 0.06

            for i in values[3]:
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

            for i in range(len(values[3])):
                if i == 2 and len(values[3]) > 10:
                    gradient += 0.03
                if i == 5 and len(values[3]) > 10:
                    gradient += 0.03

                if i == 1 and len(values[3]) == 10:
                    gradient += 0.03
                if i == 4 and len(values[3]) == 10:
                    gradient += 0.03

                if i == 3 and len(values[3]) == 9:
                    gradient += 0.03

                if i == 2 and len(values[3]) == 8:
                    gradient += 0.03

                if i == 1 and len(values[3]) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[3]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[3]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[3]) == 9:
                #     gradient += 0.03

                if self.minor_sprite[i] == minor_point_object:
                    self.minor_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * minor_height, 0)
                    minor_point_show = True
                else:
                    self.minor_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * minor_height, 0)
                if minor_point_show == False:
                    gradient += 0.047
                else:
                    gradient += 0.012
                    minor_point_show = False
                    # self.values.append(values[3])
            # print(type(self.values[3]), type(values[3]))
            # return
        else:
            if self.values[3] != values[3]:

                # while True:
                #     if self.minor_anime:
                #         pass
                #     else:
                #         break
                self.reset(self.minor_sprite)
                self.minor_sprite = []
                for i in range(len(values[3]) - 3):
                    gradient -= 0.02
                if len(values[3]) == 10:
                    gradient += 0.01
                if len(values[3]) == 9:
                    gradient += 0.02
                if len(values[3]) == 8:
                    gradient += 0.02
                if len(values[3]) == 7:
                    gradient += 0.03
                if len(values[3]) == 6:
                    gradient += 0.04
                if len(values[3]) == 5:
                    gradient += 0.05
                if len(values[3]) == 4:
                    gradient += 0.06
                count = 0
                for i in values[3]:

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
                        if self.values[3][count] == '.':
                            count -= 1
                        if self.minor_activ == True:
                            if self.micro is False:
                                if self.position[self.values[3][count]] > self.position[i]:
                                    for b in range(self.position[self.values[3][count]], self.position['10']):
                                        img.append(self.counters_anime['minor'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['minor'][b])
                                else:
                                    for b in range(self.position[self.values[3][count]], self.position[i]):
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
                            if self.values[3][count] == '.':
                                count -= 1
                            if self.micro is False:
                                if self.position[self.values[3][count]] > self.position[i]:
                                    for b in range(self.position[self.values[3][count]], self.position['10']):
                                        img.append(self.counters_anime['gray'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])
                                else:
                                    for b in range(self.position[self.values[3][count]], self.position[i]):
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
                for i in range(len(values[3])):
                    if i == 2 and len(values[3]) > 10:
                        gradient += 0.03
                    if i == 5 and len(values[3]) > 10:
                        gradient += 0.03

                    if i == 1 and len(values[3]) == 10:
                        gradient += 0.03
                    if i == 4 and len(values[3]) == 10:
                        gradient += 0.03

                    if i == 3 and len(values[3]) == 9:
                        gradient += 0.03

                    if i == 2 and len(values[3]) == 8:
                        gradient += 0.03

                    if i == 1 and len(values[3]) == 7:
                        gradient += 0.03
                    if self.minor_sprite[i] == minor_point_object:
                        self.minor_sprite[i].position = (
                        SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * minor_height, 0)
                        minor_point_show = True
                    else:
                        self.minor_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * minor_height, 0)
                    if minor_point_show == False:
                        gradient += 0.047
                    else:
                        gradient += 0.012
                        minor_point_show = False

        # ===============================================================================================================
        # MINI
        # ===============================================================================================================
        gradient = 0.645
        mini_height = 0.085

        if len(self.values) == 0:

            self.reset(self.mini_sprite)

            for i in range(len(values[4]) - 3):
                gradient -= 0.02
            if len(values[4]) == 10:
                gradient += 0.01
            if len(values[4]) == 9:
                gradient += 0.02
            if len(values[4]) == 8:
                gradient += 0.02
            if len(values[4]) == 7:
                gradient += 0.03
            if len(values[4]) == 6:
                gradient += 0.04
            if len(values[4]) == 5:
                gradient += 0.05
            if len(values[4]) == 4:
                gradient += 0.06

            for i in values[4]:
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
                    if self.mini_activ == True:
                        self.mini_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['mini'][self.position[i]],
                                                 batch=self.batch,
                                                 group=self.group))
                    else:
                        self.mini_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['gray'][self.position[i]],
                                                 batch=self.batch,
                                                 group=self.group))
            mini_point_show = False

            for i in range(len(values[4])):
                if i == 2 and len(values[4]) > 10:
                    gradient += 0.03
                if i == 5 and len(values[4]) > 10:
                    gradient += 0.03

                if i == 1 and len(values[4]) == 10:
                    gradient += 0.03
                if i == 4 and len(values[4]) == 10:
                    gradient += 0.03

                if i == 3 and len(values[4]) == 9:
                    gradient += 0.03

                if i == 2 and len(values[4]) == 8:
                    gradient += 0.03

                if i == 1 and len(values[4]) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[4]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[4]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[4]) == 9:


                if self.mini_sprite[i] == mini_point_object:
                    self.mini_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * mini_height, 0)
                    mini_point_show = True
                else:
                    self.mini_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mini_height, 0)
                if mini_point_show == False:
                    gradient += 0.047
                else:
                    gradient += 0.012
                    mini_point_show = False
                    # self.values.append(values[4])
            # print(type(self.values[4]), type(values[4]))
            # return
        else:
            if self.values[4] != values[4]:

                # while True:
                #     if self.mini_anime:
                #         pass
                #     else:
                #         break
                self.reset(self.mini_sprite)
                self.mini_sprite = []
                for i in range(len(values[4]) - 3):
                    gradient -= 0.02
                if len(values[4]) == 10:
                    gradient += 0.01
                if len(values[4]) == 9:
                    gradient += 0.02
                if len(values[4]) == 8:
                    gradient += 0.02
                if len(values[4]) == 7:
                    gradient += 0.03
                if len(values[4]) == 6:
                    gradient += 0.04
                if len(values[4]) == 5:
                    gradient += 0.05
                if len(values[4]) == 4:
                    gradient += 0.06
                count = 0
                for i in values[4]:

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
                        if self.values[4][count] == '.':
                            count -= 1
                        if self.mini_activ == True:
                            if self.micro is False:
                                if self.position[self.values[4][count]] > self.position[i]:
                                    for b in range(self.position[self.values[4][count]], self.position['10']):
                                        img.append(self.counters_anime['mini'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['mini'][b])
                                else:
                                    for b in range(self.position[self.values[4][count]], self.position[i]):
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
                            if self.values[4][count] == '.':
                                count -= 1
                            if self.micro is False:
                                if self.position[self.values[4][count]] > self.position[i]:
                                    for b in range(self.position[self.values[4][count]], self.position['10']):
                                        img.append(self.counters_anime['gray'][b])
                                    for b in range(self.position['0'], self.position[i]):
                                        img.append(self.counters_anime['gray'][b])
                                else:
                                    for b in range(self.position[self.values[4][count]], self.position[i]):
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
                for i in range(len(values[4])):
                    if i == 2 and len(values[4]) > 10:
                        gradient += 0.03
                    if i == 5 and len(values[4]) > 10:
                        gradient += 0.03

                    if i == 1 and len(values[4]) == 10:
                        gradient += 0.03
                    if i == 4 and len(values[4]) == 10:
                        gradient += 0.03

                    if i == 3 and len(values[4]) == 9:
                        gradient += 0.03

                    if i == 2 and len(values[4]) == 8:
                        gradient += 0.03

                    if i == 1 and len(values[4]) == 7:
                        gradient += 0.03
                    if self.mini_sprite[i] == mini_point_object:
                        self.mini_sprite[i].position = (
                        SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * mini_height, 0)
                        mini_point_show = True
                    else:
                        self.mini_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mini_height, 0)
                    if mini_point_show == False:
                        gradient += 0.047
                    else:
                        gradient += 0.012
                        mini_point_show = False

class Values2(Values):
    def __init__(self):
        Values.__init__(self)
        self.point_sum = 0.014

class Main():
    def __init__(self):
        self.activ = []
        self.value_len = 0
        self.value_data = []
        if config.FONT == 1:
            self.value = Values()
        elif config.FONT == 2:
            self.value = Values2()
        else:
            self.value = Values()

    def full_reset(self):
        self.activ = []
        self.value_len = 0
        self.value.reset('ALL')

    def show(self, values=[], activ=[], **kwargs):
        if 1 in activ:
            self.value.mega_activ = True
        else:
            self.value.mega_activ = False
        if 2 in activ:
            self.value.grand_activ = True
        else:
            self.value.grand_activ = False
        if 3 in activ:
            self.value.major_activ = True
        else:
            self.value.major_activ = False
        if 4 in activ:
            self.value.minor_activ = True
        else:
            self.value.minor_activ = False
        if 5 in activ:
            self.value.mini_activ = True
        else:
            self.value.mini_activ = False

        if activ != self.activ or len(values) != self.value_len:
            self.full_reset()
            self.activ = activ
            self.value_len = len(values)
            self.value_data = []
            self.value.values = []

        tmp = []
        for i in values:
            tmp.append("{:.2f}".format(i))

        if tmp != self.value_data:
            self.value_data = tmp
            if len(values) == 1:
                self.value.one_show(values=values)
            elif len(values) == 2:
                self.value.tow_show(values)
            elif len(values) == 3:
                self.value.free_show(values)
            elif len(values) == 4:
                self.value.for_show(values)
            elif len(values) == 5:
                self.value.five_show(values)
            else:
                self.full_reset()
            self.value.values = tmp

        self.value.batch.draw()



