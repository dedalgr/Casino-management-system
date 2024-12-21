# -*- coding:utf-8 -*-
import pyglet
import time
import resources

# platform = pyglet.canvas.get_display()
# display = platform.get_screens()
# screen = platform.get_default_screen()
SCREEN_WIDTH = resources.SCREEN_WIDTH
SCREEN_HEIGHT = resources.SCREEN_HEIGHT

class ErrorDisplay():
    def __init__(self):
        self.image = resources.ERROR
        self.group = resources.BACKBROUND_GROUP
        self.text_group = resources.BACKBROUND_LOGO_GROUP
        self.batch = resources.ERROR_BATCH
        self.image.width = int(SCREEN_WIDTH)
        self.image.height = int(SCREEN_HEIGHT)
        self.label = pyglet.text.Label( "",
                                  font_name='Times New Roman',
                                  font_size=65,
                                  x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2,
                                  anchor_x='center', anchor_y='center', batch=self.batch)
        self.background_sprite = pyglet.sprite.Sprite(self.image, batch=self.batch, group=self.group)

    def show_error(self, error='00', text='ERROR:'):
        self.label.delete()
        self.label = pyglet.text.Label(text + " " + error,
                                  font_name='Times New Roman',
                                  font_size=65,
                                  x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2,
                                  anchor_x='center', anchor_y='center', batch=self.batch, group=self.text_group)
        self.batch.draw()
        # label.draw()