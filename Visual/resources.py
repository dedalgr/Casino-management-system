# -*- coding:utf-8 -*-
import pyglet
import log
import config
if config.PYGAME is True:
    from pygame import mixer
    try:
        mixer.init()
        DOWN_WAV = mixer.Sound('wav/down.wav')
        RUNNER_WAV = mixer.Sound('wav/runner.wav')
        CHANGE_WAV = mixer.Sound('wav/change.wav')
        BEEP = mixer.Sound('wav/beep-07a.wav')
    except Exception as e:
        log.stdout_logger.error(e, exc_info=True)
        mixer = 'No Device'
        DOWN_WAV = None
        RUNNER_WAV = None
        CHANGE_WAV = None
        BEEP = None
else:
    try:
        DOWN_WAV = pyglet.resource.media('wav/down.wav', streaming=True)
        RUNNER_WAV = pyglet.resource.media('wav/runner.wav', streaming=True)
        CHANGE_WAV = pyglet.resource.media('wav/change.wav', streaming=True)
        BEEP = pyglet.resource.media('wav/beep-07a.wav', streaming=True)
    except Exception as e:
        log.stdout_logger.error(e, exc_info=True)
        mixer = 'No Device'
        DOWN_WAV = None
        RUNNER_WAV = None
        CHANGE_WAV = None
        BEEP = None

platform = pyglet.canvas.get_display()
display = platform.get_screens()
screen = platform.get_default_screen()
SCREEN_WIDTH = screen.width
SCREEN_HEIGHT = screen.height

FIELD_BATCH = pyglet.graphics.Batch()
BACKGROUND_BATCH = pyglet.graphics.Batch()
BET_AND_RANGES_BATCH = pyglet.graphics.Batch()
COUNTERS_BATCH = pyglet.graphics.Batch()
DOWN_BATCH = pyglet.graphics.Batch()
ERROR_BATCH = pyglet.graphics.Batch()
X2_BATCH = pyglet.graphics.Batch()
RUNNER_BATCH = pyglet.graphics.Batch()
BACKBROUND_GROUP = pyglet.graphics.Group(0)
BACKBROUND_LOGO_GROUP = pyglet.graphics.Group(1)
FIELD_GROUP = pyglet.graphics.Group(2)
FIELD_LOGO_GROUP = pyglet.graphics.Group(3)
COUNT_GROUP = pyglet.graphics.Group(4)
STOP_GROUP = pyglet.graphics.Group(5)
STOP_GROUP_BATCH = pyglet.graphics.Batch()

if config.BACKGROUND_ANIME == 0:
    BACKGROUND = {'anime': [pyglet.resource.image('img/background/startup.png')]}
elif config.BACKGROUND_ANIME == 1:
    if config.VISUAL_MICRO is False:
        BACKGROUND = {'anime': [pyglet.resource.image('img/background/1/image%s.png' % (i)) for i in range(10)]}
    else:
        BACKGROUND = {'anime': [pyglet.resource.image('img/background/1/image%s.png' % (9))]}
elif config.BACKGROUND_ANIME == 2:
    if config.VISUAL_MICRO is False:
        BACKGROUND = {'anime': [pyglet.resource.image('img/background/2/image%s.png' % (i)) for i in range(9)]}
    else:
        BACKGROUND = {'anime': [pyglet.resource.image('img/background/2/image%s.png' % (i)) for i in range(9)]}
elif config.BACKGROUND_ANIME == 3:
    if config.VISUAL_MICRO is False:
        BACKGROUND = {'anime': [pyglet.resource.image('img/background/3/image%s.png' % (i)) for i in range(17)]}
    else:
        BACKGROUND = {'anime': [pyglet.resource.image('img/background/3/image%s.png' % (8))]}
elif config.BACKGROUND_ANIME == 4:
    if config.VISUAL_MICRO is False:
        BACKGROUND = {'anime': [pyglet.resource.image('img/background/4/image%s.png' % (i)) for i in range(18)]}
    else:
        BACKGROUND = {'anime': [pyglet.resource.image('img/background/4/image%s.png' % (i)) for i in range(18)]}
elif config.BACKGROUND_ANIME == 5:
    BACKGROUND = {'anime': [pyglet.resource.image('img/background/Screen1_bg.png')]}
else:
    config.BACKGROUND_ANIME = 0
    BACKGROUND = {'anime': [pyglet.resource.image('img/background/startup.png')]}


LOGO = pyglet.resource.image('img/background/cashboxL.png')
ERROR = pyglet.resource.image('img/background/startup.png')
BGN = pyglet.resource.image('img/bet_and_range/BGN.png')
EU = pyglet.resource.image('img/bet_and_range/EU.png')
BET = pyglet.resource.image('img/bet_and_range/BET.png')
RANGE = pyglet.resource.image('img/bet_and_range/RANGE.png')
RUNER_FLAG = pyglet.resource.image('img/config/runner_blue.png')
X2 = pyglet.resource.image('img/config/x2.png')
PLAY_WITH_CART = pyglet.resource.image('img/config/in_out.png')
STOP = pyglet.resource.image('img/config/znak.png')
BET_AND_RANGE_COUNTERS = {
    'counters':[pyglet.resource.image('img/bet_and_range/%s.png' % (i)) for i in range(10)],
    'tire': pyglet.resource.image('img/bet_and_range/tire.png'),
    'point':pyglet.resource.image('img/bet_and_range/point.png'),
    # 'zapetaia':pyglet.resource.image('img/bet_and_range/zapetaia.png')
}
if config.VISUAL_MICRO is False:
    if config.FIELF_COLOR_NAME is False:
        inactiv = 'inactiv.png'
    else:
        inactiv = 'inactiv_color.png'
    FIELD = {
            'mega': pyglet.resource.image('img/field/red/%s' % (inactiv)),
            'mega_anime':[pyglet.resource.image('img/field/red/r%s.png' % (i)) for i in range(1,125)],
            'grand':pyglet.resource.image('img/field/purple/%s' % (inactiv)),
            'grand_anime':[pyglet.resource.image('img/field/purple/p%s.png' % (i)) for i in range(1, 125)],
            'major':pyglet.resource.image('img/field/yellow/%s' % (inactiv)),
            'major_anime':[pyglet.resource.image('img/field/yellow/y%s.png' % (i)) for i in range(1, 125)],
            'minor':pyglet.resource.image('img/field/blue/%s' % (inactiv)),
            'minor_anime':[pyglet.resource.image('img/field/blue/b%s.png' % (i)) for i in range(1, 125)],
            'mini':pyglet.resource.image('img/field/green/%s' % (inactiv)),
            'mini_anime':[pyglet.resource.image('img/field/green/g%s.png' % (i)) for i in range(1, 125)]
    }
else:
    if config.FIELF_COLOR_NAME is False:
        inactiv = 'inactiv.png'
    else:
        inactiv = 'inactiv_color.png'
    FIELD = {
        'mega': pyglet.resource.image('img/field/red/%s' % (inactiv)),
        'mega_anime': [pyglet.resource.image('img/field/red/r58.png')],
        'grand':pyglet.resource.image('img/field/purple/%s' % (inactiv)),
        'grand_anime': [pyglet.resource.image('img/field/purple/p58.png')],
        'major':pyglet.resource.image('img/field/yellow/%s' % (inactiv)),
        'major_anime': [pyglet.resource.image('img/field/yellow/y58.png')],
        'minor':pyglet.resource.image('img/field/blue/%s' % (inactiv)),
        'minor_anime': [pyglet.resource.image('img/field/blue/b58.png')],
        'mini':pyglet.resource.image('img/field/green/%s' % (inactiv)),
        'mini_anime': [pyglet.resource.image('img/field/green/g58.png')]
    }

CLOCK_RED = pyglet.resource.image('img/bet_and_range/clock_red.png')
CLOCK_BLUE = pyglet.resource.image('img/bet_and_range/clock_blue.png')
CLOCK_GREEN = pyglet.resource.image('img/bet_and_range/clock_green.png')
CLOCK_PURPLE = pyglet.resource.image('img/bet_and_range/clock_purple.png')
CLOCK_YELLOW = pyglet.resource.image('img/bet_and_range/clock_yellow.png')
if config.FONT == 1:
    if config.VISUAL_MICRO is False:
        COUNTERS_INDEX = {'0':0, '1':36, '2':72, '3':108, '4':143, '5':180, '6':216, '7':252, '8':288, '9':324, '10':359}
        COUNTERS = {
            'mega':[pyglet.resource.image('img/counters/1/red/image%s.png' % (i)) for i in range(360)],
            'grand':[pyglet.resource.image('img/counters/1/purple/image%s.png' % (i)) for i in range(360)],
            'major':[pyglet.resource.image('img/counters/1/yellow/image%s.png' % (i)) for i in range(360)],
            'minor':[pyglet.resource.image('img/counters/1/blue/image%s.png' % (i)) for i in range(360)],
            'mini':[pyglet.resource.image('img/counters/1/green/image%s.png' % (i)) for i in range(360)],
            'gray':[pyglet.resource.image('img/counters/1/grey/image%s.png' % (i)) for i in range(360)],
            'gray_point':pyglet.resource.image('img/counters/1/grey/point.png'),
            'mega_point':pyglet.resource.image('img/counters/1/red/point.png'),
            'grand_point':pyglet.resource.image('img/counters/1/purple/point.png'),
            'major_point':pyglet.resource.image('img/counters/1/yellow/point.png'),
            'minor_point':pyglet.resource.image('img/counters/1/blue/point.png'),
            'mini_point':pyglet.resource.image('img/counters/1/green/point.png'),
        }
    else:
        COUNTERS_INDEX = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10}
        var = [0, 36, 72, 108, 143, 180, 216, 252, 288, 324, 359]
        COUNTERS = {
            'mega':[pyglet.resource.image('img/counters/1/red/image%s.png' % (i)) for i in var],
            'grand':[pyglet.resource.image('img/counters/1/purple/image%s.png' % (i)) for i in var],
            'major':[pyglet.resource.image('img/counters/1/yellow/image%s.png' % (i)) for i in var],
            'minor':[pyglet.resource.image('img/counters/1/blue/image%s.png' % (i)) for i in var],
            'mini':[pyglet.resource.image('img/counters/1/green/image%s.png' % (i)) for i in var],
            'gray':[pyglet.resource.image('img/counters/1/grey/image%s.png' % (i)) for i in var],
            'gray_point':pyglet.resource.image('img/counters/1/grey/point.png'),
            'mega_point':pyglet.resource.image('img/counters/1/red/point.png'),
            'grand_point':pyglet.resource.image('img/counters/1/purple/point.png'),
            'major_point':pyglet.resource.image('img/counters/1/yellow/point.png'),
            'minor_point':pyglet.resource.image('img/counters/1/blue/point.png'),
            'mini_point':pyglet.resource.image('img/counters/1/green/point.png'),
        }

    COUNTERS['mega_point'].width = int(SCREEN_WIDTH * 0.017)
    COUNTERS['mega_point'].height = int(SCREEN_HEIGHT * 0.048)
    for i in COUNTERS['mega']:
        i.width = int(SCREEN_WIDTH * 0.05)
        i.height = int(SCREEN_HEIGHT * 0.12)

    COUNTERS['grand_point'].width = int(SCREEN_WIDTH * 0.017)
    COUNTERS['grand_point'].height = int(SCREEN_HEIGHT * 0.048)
    for i in COUNTERS['grand']:
        i.width = int(SCREEN_WIDTH * 0.05)
        i.height = int(SCREEN_HEIGHT * 0.12)

    COUNTERS['major_point'].width = int(SCREEN_WIDTH * 0.017)
    COUNTERS['major_point'].height = int(SCREEN_HEIGHT * 0.048)
    for i in COUNTERS['major']:
        i.width = int(SCREEN_WIDTH * 0.06)
        i.height = int(SCREEN_HEIGHT * 0.13)

    COUNTERS['minor_point'].width = int(SCREEN_WIDTH * 0.017)
    COUNTERS['minor_point'].height = int(SCREEN_HEIGHT * 0.048)
    for i in COUNTERS['minor']:
        i.width = int(SCREEN_WIDTH * 0.05)
        i.height = int(SCREEN_HEIGHT * 0.12)

    COUNTERS['mini_point'].width = int(SCREEN_WIDTH * 0.017)
    COUNTERS['mini_point'].height = int(SCREEN_HEIGHT * 0.048)
    for i in COUNTERS['mini']:
        i.width = int(SCREEN_WIDTH * 0.05)
        i.height = int(SCREEN_HEIGHT * 0.12)

    COUNTERS['gray_point'].width = int(SCREEN_WIDTH * 0.017)
    COUNTERS['gray_point'].height = int(SCREEN_HEIGHT * 0.048)
    for i in COUNTERS['gray']:
        i.width = int(SCREEN_WIDTH * 0.05)
        i.height = int(SCREEN_HEIGHT * 0.12)
elif config.FONT == 2:
    if config.VISUAL_MICRO is False:
        COUNTERS_INDEX = {'0':0, '1':12, '2':25, '3':38, '4':50, '5':62, '6':75, '7':87, '8':100, '9':112, '10':124}
        COUNTERS = {
            'mega':[pyglet.resource.image('img/counters/2/red/image%s.png' % (i)) for i in range(125)],
            'grand':[pyglet.resource.image('img/counters/2/purple/image%s.png' % (i)) for i in range(125)],
            'major':[pyglet.resource.image('img/counters/2/yellow/image%s.png' % (i)) for i in range(125)],
            'minor':[pyglet.resource.image('img/counters/2/blue/image%s.png' % (i)) for i in range(125)],
            'mini':[pyglet.resource.image('img/counters/2/green/image%s.png' % (i)) for i in range(125)],
            'gray':[pyglet.resource.image('img/counters/2/grey/image%s.png' % (i)) for i in range(125)],
            'gray_point':pyglet.resource.image('img/counters/2/grey/point.png'),
            'mega_point':pyglet.resource.image('img/counters/2/red/point.png'),
            'grand_point':pyglet.resource.image('img/counters/2/purple/point.png'),
            'major_point':pyglet.resource.image('img/counters/2/yellow/point.png'),
            'minor_point':pyglet.resource.image('img/counters/2/blue/point.png'),
            'mini_point':pyglet.resource.image('img/counters/2/green/point.png'),
        }
    else:
        COUNTERS_INDEX = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10}
        var = [0, 12, 25, 38, 50, 62, 75, 87, 100, 112, 124]
        COUNTERS = {
            'mega':[pyglet.resource.image('img/counters/2/red/image%s.png' % (i)) for i in var],
            'grand':[pyglet.resource.image('img/counters/2/purple/image%s.png' % (i)) for i in var],
            'major':[pyglet.resource.image('img/counters/2/yellow/image%s.png' % (i)) for i in var],
            'minor':[pyglet.resource.image('img/counters/2/blue/image%s.png' % (i)) for i in var],
            'mini':[pyglet.resource.image('img/counters/2/green/image%s.png' % (i)) for i in var],
            'gray':[pyglet.resource.image('img/counters/2/grey/image%s.png' % (i)) for i in var],
            'gray_point':pyglet.resource.image('img/counters/2/grey/point.png'),
            'mega_point':pyglet.resource.image('img/counters/2/red/point.png'),
            'grand_point':pyglet.resource.image('img/counters/2/purple/point.png'),
            'major_point':pyglet.resource.image('img/counters/2/yellow/point.png'),
            'minor_point':pyglet.resource.image('img/counters/2/blue/point.png'),
            'mini_point':pyglet.resource.image('img/counters/2/green/point.png'),
        }

    COUNTERS['mega_point'].width = int(SCREEN_WIDTH * 0.015)
    COUNTERS['mega_point'].height = int(SCREEN_HEIGHT * 0.042)
    for i in COUNTERS['mega']:
        i.width = int(SCREEN_WIDTH * 0.068)
        i.height = int(SCREEN_HEIGHT * 0.142)

    COUNTERS['grand_point'].width = int(SCREEN_WIDTH * 0.015)
    COUNTERS['grand_point'].height = int(SCREEN_HEIGHT * 0.042)
    for i in COUNTERS['grand']:
        i.width = int(SCREEN_WIDTH * 0.074)
        i.height = int(SCREEN_HEIGHT * 0.143)

    COUNTERS['major_point'].width = int(SCREEN_WIDTH * 0.015)
    COUNTERS['major_point'].height = int(SCREEN_HEIGHT * 0.042)
    for i in COUNTERS['major']:
        i.width = int(SCREEN_WIDTH * 0.074)
        i.height = int(SCREEN_HEIGHT * 0.143)

    COUNTERS['minor_point'].width = int(SCREEN_WIDTH * 0.015)
    COUNTERS['minor_point'].height = int(SCREEN_HEIGHT * 0.042)
    for i in COUNTERS['minor']:
        i.width = int(SCREEN_WIDTH * 0.074)
        i.height = int(SCREEN_HEIGHT * 0.143)

    COUNTERS['mini_point'].width = int(SCREEN_WIDTH * 0.015)
    COUNTERS['mini_point'].height = int(SCREEN_HEIGHT * 0.042)
    for i in COUNTERS['mini']:
        i.width = int(SCREEN_WIDTH * 0.074)
        i.height = int(SCREEN_HEIGHT * 0.143)

    COUNTERS['gray_point'].width = int(SCREEN_WIDTH * 0.015)
    COUNTERS['gray_point'].height = int(SCREEN_HEIGHT * 0.042)
    for i in COUNTERS['gray']:
        i.width = int(SCREEN_WIDTH * 0.074)
        i.height = int(SCREEN_HEIGHT * 0.143)
else:
    if config.VISUAL_MICRO is False:
        COUNTERS_INDEX = {'0':0, '1':36, '2':72, '3':108, '4':143, '5':180, '6':216, '7':252, '8':288, '9':324, '10':359}
        COUNTERS = {
            'mega':[pyglet.resource.image('img/counters/1/red/image%s.png' % (i)) for i in range(360)],
            'grand':[pyglet.resource.image('img/counters/1/purple/image%s.png' % (i)) for i in range(360)],
            'major':[pyglet.resource.image('img/counters/1/yellow/image%s.png' % (i)) for i in range(360)],
            'minor':[pyglet.resource.image('img/counters/1/blue/image%s.png' % (i)) for i in range(360)],
            'mini':[pyglet.resource.image('img/counters/1/green/image%s.png' % (i)) for i in range(360)],
            'gray':[pyglet.resource.image('img/counters/1/grey/image%s.png' % (i)) for i in range(360)],
            'gray_point':pyglet.resource.image('img/counters/1/grey/point.png'),
            'mega_point':pyglet.resource.image('img/counters/1/red/point.png'),
            'grand_point':pyglet.resource.image('img/counters/1/purple/point.png'),
            'major_point':pyglet.resource.image('img/counters/1/yellow/point.png'),
            'minor_point':pyglet.resource.image('img/counters/1/blue/point.png'),
            'mini_point':pyglet.resource.image('img/counters/1/green/point.png'),
        }
    else:
        COUNTERS_INDEX = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10}
        var = [0, 36, 72, 108, 143, 180, 216, 252, 288, 324, 359]
        COUNTERS = {
            'mega':[pyglet.resource.image('img/counters/1/red/image%s.png' % (i)) for i in var],
            'grand':[pyglet.resource.image('img/counters/1/purple/image%s.png' % (i)) for i in var],
            'major':[pyglet.resource.image('img/counters/1/yellow/image%s.png' % (i)) for i in var],
            'minor':[pyglet.resource.image('img/counters/1/blue/image%s.png' % (i)) for i in var],
            'mini':[pyglet.resource.image('img/counters/1/green/image%s.png' % (i)) for i in var],
            'gray':[pyglet.resource.image('img/counters/1/grey/image%s.png' % (i)) for i in var],
            'gray_point':pyglet.resource.image('img/counters/1/grey/point.png'),
            'mega_point':pyglet.resource.image('img/counters/1/red/point.png'),
            'grand_point':pyglet.resource.image('img/counters/1/purple/point.png'),
            'major_point':pyglet.resource.image('img/counters/1/yellow/point.png'),
            'minor_point':pyglet.resource.image('img/counters/1/blue/point.png'),
            'mini_point':pyglet.resource.image('img/counters/1/green/point.png'),
        }

    COUNTERS['mega_point'].width = int(SCREEN_WIDTH * 0.017)
    COUNTERS['mega_point'].height = int(SCREEN_HEIGHT * 0.048)
    for i in COUNTERS['mega']:
        i.width = int(SCREEN_WIDTH * 0.05)
        i.height = int(SCREEN_HEIGHT * 0.12)

    COUNTERS['grand_point'].width = int(SCREEN_WIDTH * 0.017)
    COUNTERS['grand_point'].height = int(SCREEN_HEIGHT * 0.048)
    for i in COUNTERS['grand']:
        i.width = int(SCREEN_WIDTH * 0.05)
        i.height = int(SCREEN_HEIGHT * 0.12)

    COUNTERS['major_point'].width = int(SCREEN_WIDTH * 0.017)
    COUNTERS['major_point'].height = int(SCREEN_HEIGHT * 0.048)
    for i in COUNTERS['major']:
        i.width = int(SCREEN_WIDTH * 0.06)
        i.height = int(SCREEN_HEIGHT * 0.13)

    COUNTERS['minor_point'].width = int(SCREEN_WIDTH * 0.017)
    COUNTERS['minor_point'].height = int(SCREEN_HEIGHT * 0.048)
    for i in COUNTERS['minor']:
        i.width = int(SCREEN_WIDTH * 0.05)
        i.height = int(SCREEN_HEIGHT * 0.12)

    COUNTERS['mini_point'].width = int(SCREEN_WIDTH * 0.017)
    COUNTERS['mini_point'].height = int(SCREEN_HEIGHT * 0.048)
    for i in COUNTERS['mini']:
        i.width = int(SCREEN_WIDTH * 0.05)
        i.height = int(SCREEN_HEIGHT * 0.12)

    COUNTERS['gray_point'].width = int(SCREEN_WIDTH * 0.017)
    COUNTERS['gray_point'].height = int(SCREEN_HEIGHT * 0.048)
    for i in COUNTERS['gray']:
        i.width = int(SCREEN_WIDTH * 0.05)
        i.height = int(SCREEN_HEIGHT * 0.12)
            
RUNNER_FIELD = {
    2:pyglet.resource.image('img/runner_display/2emg.png'),
    3:pyglet.resource.image('img/runner_display/3emg.png'),
    4:pyglet.resource.image('img/runner_display/4emg.png'),
    5:pyglet.resource.image('img/runner_display/5emg.png'),
                }

RUNNER_LINE = {
    'red':pyglet.resource.image('img/runner_display/2r.png'),
       'yellow':pyglet.resource.image('img/runner_display/2j.png'),
       'orange':pyglet.resource.image('img/runner_display/2o.png'),
       'green':pyglet.resource.image('img/runner_display/2g.png')
}


RUNNER_DEVICE = [pyglet.resource.image('img/runner_device/image%s.png' % (i)) for i in range(10)]
RUNNER_INDEX = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10}
var = [0, 36, 72, 108, 143, 180, 216, 252, 288, 324, 359]
RUNNER_DOWNON = {'gray': [pyglet.resource.image('img/counters/1/grey/image%s.png' % (i)) for i in var],
    'gray_point': pyglet.resource.image('img/counters/1/grey/point.png')}
RUNNER_DOWNON['gray_point'].width = int(SCREEN_WIDTH * 0.017)
RUNNER_DOWNON['gray_point'].height = int(SCREEN_HEIGHT * 0.048)
for i in RUNNER_DOWNON['gray']:
    i.width = int(SCREEN_WIDTH * 0.05)
    i.height = int(SCREEN_HEIGHT * 0.12)

if config.VISUAL_MICRO is False:
    DOWN_ANIME = [pyglet.resource.image('img/down/image%s.png' % (i)) for i in range(5, 27)]
else:
    DOWN_ANIME = [pyglet.resource.image('img/down/image5.png')]

DOWN_DEVICE = [pyglet.resource.image('img/down_device/image%s.png' % (i)) for i in range(10)]
DUEL = pyglet.resource.image('img/runner_display/duel.png')
WON = pyglet.resource.image('img/down/won.png')
