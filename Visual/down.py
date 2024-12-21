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

class Down():
    def __init__(self):
        self.group = resources.BACKBROUND_GROUP
        self.batch = resources.DOWN_BATCH
        self.field_group = resources.FIELD_GROUP
        self.counter_group = resources.COUNT_GROUP
        self.old_value = None
        self.old_mashine = None
        self.old_color = None
        self.background_img = resources.DOWN_ANIME
        for i in self.background_img:
            i.width = int(SCREEN_WIDTH)
            i.height = int(SCREEN_HEIGHT)
        if config.FONT == 1:
            self.point_sum = 0.0
        elif config.FONT == 2:
            self.point_sum = 0.014
        else:
            self.point_sum = 0.0
        self.won = resources.WON
        self.won.width = int(SCREEN_WIDTH * 0.1)
        self.won.height = int(SCREEN_HEIGHT * 0.06)
        self.won_sprite = None

        # def add_text(casino_name):
        #     #     text = u'%s' % (mashin_n)

        self.casino_name = pyglet.text.Label('',
                                        font_name='Times New Roman',
                                        font_size=95,
                                        x=SCREEN_WIDTH * 0.45, y=SCREEN_HEIGHT * 0.1)

        self.background_anime = pyglet.image.Animation.from_image_sequence(self.background_img, duration=0.05,
                                                                           loop=True)
        self.background_sprite = pyglet.sprite.Sprite(self.background_anime, batch=self.batch, group=self.group)

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

        self.position = resources.COUNTERS_INDEX
        self.counters_anime = resources.COUNTERS
        self.device_sprite = []
        self.value_sprite = []
        self.field_sprite = None

        self.device_img = resources.DOWN_DEVICE
        for i in self.device_img:
            i.width = int(SCREEN_WIDTH * 0.15)
            i.height = int(SCREEN_HEIGHT * 0.40)

    def reset(self):
        try:
            if self.won_sprite:
                self.won_sprite.delete()
                self.won_sprite = None
            for i in self.device_sprite:
                i.delete()
            self.device_sprite = []
            for i in self.value_sprite:
                i.delete()
            self.value_sprite = []
            self.field_sprite.delete()
            self.field_sprite = None
            self.old_value = None
            self.old_mashine = None
            self.old_color = None
        except AttributeError as e:
            pass


    def set_field(self):
        self.won_sprite = pyglet.sprite.Sprite(self.won, batch=self.batch, group=self.counter_group)
        self.won_sprite.position = (SCREEN_WIDTH * 0.45, SCREEN_HEIGHT * 0.576, 0)
        if self.old_color == 'red':
            if config.FIELF_ACTIVE is True:
                for i in self.mega:
                    i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.11))
                    i.height = int(SCREEN_HEIGHT * 0.66)
                self.field_sprite = pyglet.sprite.Sprite(self.anime_mega, batch=self.batch, group=self.field_group)
                self.field_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.355, 0)
            else:
                self.anime_mega.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
                self.anime_mega.height = int(SCREEN_HEIGHT * 0.66)
                self.field_sprite = pyglet.sprite.Sprite(self.anime_mega, batch=self.batch, group=self.field_group)
                self.field_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
        elif self.old_color == 'purple':
            if config.FIELF_ACTIVE is True:
                for i in self.grand:
                    i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.11))
                    i.height = int(SCREEN_HEIGHT * 0.66)
                self.field_sprite = pyglet.sprite.Sprite(self.anime_grand, batch=self.batch, group=self.field_group)
                self.field_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
            else:
                self.anime_grand.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
                self.anime_grand.height = int(SCREEN_HEIGHT * 0.66)
                self.field_sprite = pyglet.sprite.Sprite(self.anime_grand, batch=self.batch, group=self.field_group)
                self.field_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
        elif self.old_color == 'yellow':
            if config.FIELF_ACTIVE is True:
                for i in self.major:
                    i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.11))
                    i.height = int(SCREEN_HEIGHT * 0.66)
                self.field_sprite = pyglet.sprite.Sprite(self.anime_major, batch=self.batch, group=self.field_group)
                self.field_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
            else:
                self.anime_major.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
                self.anime_major.height = int(SCREEN_HEIGHT * 0.66)
                self.field_sprite = pyglet.sprite.Sprite(self.anime_major, batch=self.batch, group=self.field_group)
                self.field_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
        elif self.old_color == 'blue':
            if config.FIELF_ACTIVE is True:
                for i in self.minor:
                    i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.11))
                    i.height = int(SCREEN_HEIGHT * 0.66)
                self.field_sprite = pyglet.sprite.Sprite(self.anime_minor, batch=self.batch, group=self.field_group)
                self.field_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
            else:
                self.anime_minor.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
                self.anime_minor.height = int(SCREEN_HEIGHT * 0.66)
                self.field_sprite = pyglet.sprite.Sprite(self.anime_minor, batch=self.batch, group=self.field_group)
                self.field_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
        elif self.old_color == 'green':
            if config.FIELF_ACTIVE is True:
                for i in self.mini:
                    i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.11))
                    i.height = int(SCREEN_HEIGHT * 0.66)
                self.field_sprite = pyglet.sprite.Sprite(self.anime_mini, batch=self.batch, group=self.field_group)
                self.field_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
            else:
                self.anime_mini.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
                self.anime_mini.height = int(SCREEN_HEIGHT * 0.66)
                self.field_sprite = pyglet.sprite.Sprite(self.anime_mini, batch=self.batch, group=self.field_group)
                self.field_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)
        else:
            if config.FIELF_ACTIVE is True:
                for i in self.mega:
                    i.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.11))
                    i.height = int(SCREEN_HEIGHT * 0.66)
                self.field_sprite = pyglet.sprite.Sprite(self.anime_mega, batch=self.batch, group=self.field_group)
                self.field_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.355, 0)
            else:
                self.anime_mega.width = int(SCREEN_WIDTH + (SCREEN_WIDTH * 0.1))
                self.anime_mega.height = int(SCREEN_HEIGHT * 0.66)
                self.field_sprite = pyglet.sprite.Sprite(self.anime_mega, batch=self.batch, group=self.field_group)
                self.field_sprite.position = (SCREEN_WIDTH - (SCREEN_WIDTH * 1.05), SCREEN_HEIGHT * 0.37, 0)

    def set_device(self):
        if len(str(self.old_mashine)) == 1:
            self.device_sprite.append(
                pyglet.sprite.Sprite(resources.DOWN_DEVICE[self.old_mashine], batch=self.batch,
                                     group=self.counter_group))
            self.device_sprite[0].position = (SCREEN_WIDTH * 0.42, SCREEN_HEIGHT * 0.18, 0)
        elif len(str(self.old_mashine)) == 2:
            self.device_sprite.append(
                pyglet.sprite.Sprite(resources.DOWN_DEVICE[int(str(self.old_mashine)[0])], batch=self.batch,
                                     group=self.counter_group))
            self.device_sprite[0].position = (SCREEN_WIDTH * 0.35, SCREEN_HEIGHT * 0.18, 0)
            self.device_sprite.append(
                pyglet.sprite.Sprite(resources.DOWN_DEVICE[int(str(self.old_mashine)[1])], batch=self.batch,
                                     group=self.counter_group))
            self.device_sprite[1].position = (SCREEN_WIDTH * 0.47, SCREEN_HEIGHT * 0.18, 0)
        elif len(str(self.old_mashine)) == 3:
            self.device_sprite.append(
                pyglet.sprite.Sprite(resources.DOWN_DEVICE[int(str(self.old_mashine)[0])], batch=self.batch,
                                     group=self.counter_group))
            self.device_sprite[0].position = (SCREEN_WIDTH * 0.31, SCREEN_HEIGHT * 0.18, 0)
            self.device_sprite.append(
                pyglet.sprite.Sprite(resources.DOWN_DEVICE[int(str(self.old_mashine)[1])], batch=self.batch,
                                     group=self.counter_group))
            self.device_sprite[1].position = (SCREEN_WIDTH * 0.41, SCREEN_HEIGHT * 0.18, 0)
            self.device_sprite.append(
                pyglet.sprite.Sprite(resources.DOWN_DEVICE[int(str(self.old_mashine)[2])], batch=self.batch,
                                     group=self.counter_group))
            self.device_sprite[2].position = (SCREEN_WIDTH * 0.51, SCREEN_HEIGHT * 0.18, 0)

    def format(self, values):
        return "{:.2f}".format(values)

    def set_value(self):
        gradient = 0.40
        mega_height = 0.625
        values = "{:.2f}".format(self.old_value)
        if self.old_color == 'red':
            for i in range(len(values) - 3):
                gradient -= 0.02
            if len(values) == 10:
                gradient += 0.01
            if len(values) == 9:
                gradient += 0.02
            if len(values) == 8:
                gradient += 0.02
            if len(values) == 7:
                gradient += 0.03
            if len(values) == 6:
                gradient += 0.04
            if len(values) == 5:
                gradient += 0.05
            if len(values) == 4:
                gradient += 0.06

            for i in values:
                if i == '.':
                    mega_point_object = pyglet.sprite.Sprite(self.counters_anime['mega_point'],
                                                                 batch=self.batch,
                                                                 group=self.counter_group)
                    self.value_sprite.append(mega_point_object)
                else:
                    self.value_sprite.append(
                            pyglet.sprite.Sprite(self.counters_anime['mega'][self.position[i]], batch=self.batch,
                                                 group=self.counter_group))
            mega_point_show = False
            for i in range(len(values)):
                if i == 2 and len(values) > 10:
                    gradient += 0.03
                if i == 5 and len(values) > 10:
                    gradient += 0.03

                if i == 1 and len(values) == 10:
                    gradient += 0.03
                if i == 4 and len(values) == 10:
                    gradient += 0.03

                if i == 3 and len(values) == 9:
                    gradient += 0.03

                if i == 2 and len(values) == 8:
                    gradient += 0.03

                if i == 1 and len(values) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[0]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[0]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[0]) == 9:
                #     gradient += 0.03

                if self.value_sprite[i] == mega_point_object:
                    self.value_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * mega_height, 0)
                    mega_point_show = True
                else:
                    self.value_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mega_height, 0)
                if mega_point_show == False:
                    gradient += 0.044
                else:
                    gradient += 0.012
                    mega_point_show = False

        elif self.old_color == 'purple':
            mega_height = 0.625
            for i in range(len(values) - 3):
                gradient -= 0.02
            if len(values) == 10:
                gradient += 0.01
            if len(values) == 9:
                gradient += 0.02
            if len(values) == 8:
                gradient += 0.02
            if len(values) == 7:
                gradient += 0.03
            if len(values) == 6:
                gradient += 0.04
            if len(values) == 5:
                gradient += 0.05
            if len(values) == 4:
                gradient += 0.06

            for i in values:
                if i == '.':
                    grand_point_object = pyglet.sprite.Sprite(self.counters_anime['grand_point'],
                                                             batch=self.batch,
                                                             group=self.counter_group)
                    self.value_sprite.append(grand_point_object)
                else:
                    self.value_sprite.append(
                        pyglet.sprite.Sprite(self.counters_anime['grand'][self.position[i]], batch=self.batch,
                                             group=self.counter_group))
            grand_point_show = False

            for i in range(len(values)):
                if i == 2 and len(values) > 10:
                    gradient += 0.03
                if i == 5 and len(values) > 10:
                    gradient += 0.03

                if i == 1 and len(values) == 10:
                    gradient += 0.03
                if i == 4 and len(values) == 10:
                    gradient += 0.03

                if i == 3 and len(values) == 9:
                    gradient += 0.03

                if i == 2 and len(values) == 8:
                    gradient += 0.03

                if i == 1 and len(values) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[0]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[0]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[0]) == 9:
                #     gradient += 0.03

                if self.value_sprite[i] == grand_point_object:
                    self.value_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * mega_height, 0)
                    grand_point_show = True
                else:
                    self.value_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mega_height, 0)
                if grand_point_show == False:
                    gradient += 0.044
                else:
                    gradient += 0.012
                    grand_point_show = False
        elif self.old_color == 'yellow':
            mega_height = 0.625
            for i in range(len(values) - 3):
                gradient -= 0.02
            if len(values) == 10:
                gradient += 0.01
            if len(values) == 9:
                gradient += 0.02
            if len(values) == 8:
                gradient += 0.02
            if len(values) == 7:
                gradient += 0.03
            if len(values) == 6:
                gradient += 0.04
            if len(values) == 5:
                gradient += 0.05
            if len(values) == 4:
                gradient += 0.06

            for i in values:
                if i == '.':
                    major_point_object = pyglet.sprite.Sprite(self.counters_anime['major_point'],
                                                             batch=self.batch,
                                                             group=self.counter_group)
                    self.value_sprite.append(major_point_object)
                else:
                    self.value_sprite.append(
                        pyglet.sprite.Sprite(self.counters_anime['major'][self.position[i]], batch=self.batch,
                                             group=self.counter_group))
            major_point_show = False

            for i in range(len(values)):
                if i == 2 and len(values) > 10:
                    gradient += 0.03
                if i == 5 and len(values) > 10:
                    gradient += 0.03

                if i == 1 and len(values) == 10:
                    gradient += 0.03
                if i == 4 and len(values) == 10:
                    gradient += 0.03

                if i == 3 and len(values) == 9:
                    gradient += 0.03

                if i == 2 and len(values) == 8:
                    gradient += 0.03

                if i == 1 and len(values) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[0]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[0]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[0]) == 9:
                #     gradient += 0.03

                if self.value_sprite[i] == major_point_object:
                    self.value_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * mega_height, 0)
                    major_point_show = True
                else:
                    self.value_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mega_height, 0)
                if major_point_show == False:
                    gradient += 0.044
                else:
                    gradient += 0.012
                    major_point_show = False
        elif self.old_color == 'blue':
            mega_height = 0.625
            for i in range(len(values) - 3):
                gradient -= 0.02
            if len(values) == 10:
                gradient += 0.01
            if len(values) == 9:
                gradient += 0.02
            if len(values) == 8:
                gradient += 0.02
            if len(values) == 7:
                gradient += 0.03
            if len(values) == 6:
                gradient += 0.04
            if len(values) == 5:
                gradient += 0.05
            if len(values) == 4:
                gradient += 0.06

            for i in values:
                if i == '.':
                    minor_point_object = pyglet.sprite.Sprite(self.counters_anime['minor_point'],
                                                             batch=self.batch,
                                                             group=self.counter_group)
                    self.value_sprite.append(minor_point_object)
                else:
                    self.value_sprite.append(
                        pyglet.sprite.Sprite(self.counters_anime['minor'][self.position[i]], batch=self.batch,
                                             group=self.counter_group))
            minor_point_show = False

            for i in range(len(values)):
                if i == 2 and len(values) > 10:
                    gradient += 0.03
                if i == 5 and len(values) > 10:
                    gradient += 0.03

                if i == 1 and len(values) == 10:
                    gradient += 0.03
                if i == 4 and len(values) == 10:
                    gradient += 0.03

                if i == 3 and len(values) == 9:
                    gradient += 0.03

                if i == 2 and len(values) == 8:
                    gradient += 0.03

                if i == 1 and len(values) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[0]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[0]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[0]) == 9:


                if self.value_sprite[i] == minor_point_object:
                    self.value_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * mega_height, 0)
                    minor_point_show = True
                else:
                    self.value_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mega_height, 0)
                if minor_point_show == False:
                    gradient += 0.044
                else:
                    gradient += 0.012
                    minor_point_show = False
        elif self.old_color == 'green':
            mega_height = 0.625
            for i in range(len(values) - 3):
                gradient -= 0.02
            if len(values) == 10:
                gradient += 0.01
            if len(values) == 9:
                gradient += 0.02
            if len(values) == 8:
                gradient += 0.02
            if len(values) == 7:
                gradient += 0.03
            if len(values) == 6:
                gradient += 0.04
            if len(values) == 5:
                gradient += 0.05
            if len(values) == 4:
                gradient += 0.06

            for i in values:

                if i == '.':
                    mini_point_object = pyglet.sprite.Sprite(self.counters_anime['mini_point'],
                                                             batch=self.batch,
                                                             group=self.counter_group)
                    self.value_sprite.append(mini_point_object)
                else:
                    self.value_sprite.append(
                        pyglet.sprite.Sprite(self.counters_anime['mini'][self.position[i]], batch=self.batch,
                                             group=self.counter_group))
            mini_point_show = False

            for i in range(len(values)):
                if i == 2 and len(values) > 10:
                    gradient += 0.03
                if i == 5 and len(values) > 10:
                    gradient += 0.03

                if i == 1 and len(values) == 10:
                    gradient += 0.03
                if i == 4 and len(values) == 10:
                    gradient += 0.03

                if i == 3 and len(values) == 9:
                    gradient += 0.03

                if i == 2 and len(values) == 8:
                    gradient += 0.03

                if i == 1 and len(values) == 7:
                    gradient += 0.03

                if self.value_sprite[i] == mini_point_object:
                    self.value_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * mega_height, 0)
                    mini_point_show = True
                else:
                    self.value_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mega_height, 0)
                if mini_point_show == False:
                    gradient += 0.044
                else:
                    gradient += 0.012
                    mini_point_show = False
        else:
            mega_height = 0.625
            for i in range(len(values) - 3):
                gradient -= 0.02
            if len(values) == 10:
                gradient += 0.01
            if len(values) == 9:
                gradient += 0.02
            if len(values) == 8:
                gradient += 0.02
            if len(values) == 7:
                gradient += 0.03
            if len(values) == 6:
                gradient += 0.04
            if len(values) == 5:
                gradient += 0.05
            if len(values) == 4:
                gradient += 0.06

            for i in values:
                if i == '.':
                    mega_point_object = pyglet.sprite.Sprite(self.counters_anime['mega_point'],
                                                             batch=self.batch,
                                                             group=self.counter_group)
                    self.value_sprite.append(mega_point_object)
                else:
                    self.value_sprite.append(
                        pyglet.sprite.Sprite(self.counters_anime['mega'][self.position[i]], batch=self.batch,
                                             group=self.counter_group))
            mega_point_show = False

            for i in range(len(values)):
                if i == 2 and len(values) > 10:
                    gradient += 0.03
                if i == 5 and len(values) > 10:
                    gradient += 0.03

                if i == 1 and len(values) == 10:
                    gradient += 0.03
                if i == 4 and len(values) == 10:
                    gradient += 0.03

                if i == 3 and len(values) == 9:
                    gradient += 0.03

                if i == 2 and len(values) == 8:
                    gradient += 0.03

                if i == 1 and len(values) == 7:
                    gradient += 0.03
                # elif i == 1 and len(values[0]) == 7:
                #     gradient += 0.03
                # elif i == 2 and len(values[0]) == 8:
                #     gradient += 0.03
                # elif i == 3 and len(values[0]) == 9:
                #     gradient += 0.03


                if self.value_sprite[i] == mega_point_object:
                    self.value_sprite[i].position = (SCREEN_WIDTH * (gradient + self.point_sum), SCREEN_HEIGHT * mega_height, 0)
                    mega_point_show = True
                else:
                    self.value_sprite[i].position = (SCREEN_WIDTH * gradient, SCREEN_HEIGHT * mega_height, 0)
                if mega_point_show == False:
                    gradient += 0.044
                else:
                    gradient += 0.012
                    mega_point_show = False

    def down_show(self, value, mashine, color, casino_name=''):
        if value != self.old_value or int(mashine) != self.old_mashine or color != self.old_color:
            self.reset()
            self.old_value = value
            self.old_color = color
            self.old_mashine = int(mashine)
            self.set_field()
            self.set_value()
            self.set_device()
            self.casino_name.text = casino_name
        self.batch.draw()
        self.casino_name.draw()


