# -*- coding:utf-8 -*-
import queue
import sys
import os
import time
# import gc
import threading
import config
import log
import client
import server
import weckup
import pyglet
from pyglet.window import key
import background
import field
import counters
import down
import error
import runer
import datetime
from queue import Empty
import resources
# from pygame import mixer
import pytz
from pyglet.gl import *
import pyglet.gl

# try:
#     mixer.init()
# except Exception as e:
#     log.stdout_logger.error(e, exc_info=True)
#     mixer = 'No Device'
#
#
#


pyglet.options['debug_gl'] = False
pyglet.options['double_buffer'] = True
pyglet.options['xsync'] = True
pyglet.options['vsync'] = False

# platform = pyglet.canvas.get_display()
# display = platform.get_screens()
# screen = platform.get_default_screen()
SCREEN_WIDTH = resources.SCREEN_WIDTH
SCREEN_HEIGHT = resources.SCREEN_HEIGHT
# pyglet.clock.schedule_interval_soft()
if config.DEBUG == False:
    window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT, fullscreen=True)
    window.set_mouse_visible(False)
else:
    window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT)

fps_display = pyglet.window.FPSDisplay(window=window)

if config.PYGAME is True:
    def stop_player():
        if resources.RUNNER_WAV and resources.CHANGE_WAV and resources.DOWN_WAV and resources.BEEP:
            resources.RUNNER_WAV.stop()
            resources.CHANGE_WAV.stop()
            resources.DOWN_WAV.stop()
            resources.BEEP.stop()
    #     global mixer
    #     if mixer == 'No Device':
    #         return
    #     try:
    #         mixer.music.stop()
    #         mixer.quit()
    #     except Exception:
    #         pass

    def play_sound(music):
        stop_player()
        if music:
            music.play()
else:
    player = pyglet.media.Player()

    def play_sound(music):
        #     music.play()
        global player
        player.delete()
        player = pyglet.media.Player()
        player.queue(music)
        player.play()

#-----------------------------------------------------------------------------------------------------------------------
# GLOBAL
#-----------------------------------------------------------------------------------------------------------------------
MY_TIME2 = time.time()
COUNT = 0
REVERT = False
BACKGROUND = background.Main()
FIELD = field.Main()
COUNTERS = counters.Main()
DOWN = down.Down()
ERROR = error.ErrorDisplay()
RUNNER = runer.Main()
DB = None
MY_GROUP = None
MY_IP = config.IP
ERROR_LOG = None
ERROR_COUNT = 0
SERVER = None
DOWN_COUNT = 0
RUNNER_COUNT = 0
RUNNER_TIME = time.time()
ALIFE_START = False
DOWN_DATA = None
CHANGE_PLAY = None
Q = server.Q
# gc.enable()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ESCAPE and config.DEBUG is True:
        SERVER.shutdown()
        SERVER.socket.close()
        pyglet.app.exit()
        sys.exit()
    if symbol == key.ESCAPE and config.DEBUG is False:
        return True

def restart_program():
    global SERVER
    try:
        SERVER.terminate()
    except:
        pass
    SERVER.socket.close()
    pyglet.app.exit()
    python = sys.executable
    os.execl(python, python, * sys.argv)

def kill_visual():
    global SERVER
    SERVER.shutdown()
    SERVER.socket.close()
    pyglet.app.exit()
    return True
# VALUES = [10.89]

# ERROR.show_error('', text='')
    # window.clear()
    # if FIRST:
    #     DOWN.down_show(20.56, '1', 'red')
    #
    #     FIRST = False
    # my_time = time.time()+30
    # if my_time > time.time():
    #     my_time = time.time() + 30
    #     DOWN.reset()
    # DOWN.down_show(50000.93, 109, 'red')

    #

    #
    # BACKGROUND.show()
    # RUNNER.show(color='red', values=VALUES, device=[18, 20, 3, 69, 17, 6], procent=[4, 9, 1, 4,7], down_on=150000.25, max_len=5)
    # activ = [1,2,3,4]
    # FIELD.show(5, activ=activ)
    # # # #
    # #
    # COUNTERS.show(ranges=[
    #     {'from':2000.00, 'to':10000.00},
    #     {'from': 5000.00, 'to': 10000.00},
    #     {'from': 3000.00, 'to': 5000.00},
    #     {'from': 500.00, 'to': 800.00},
    #     {'from': 100.00, 'to': 200.00},
    # ],
    #     bet=[
    #         2,
    #         1,
    #         0.5,
    #         0.4,
    #         0
    #          ],
    #     activ=activ,
    # values=VALUES,
    # runner=[1, 2,3,4,5], x2=[1,2,3,4,5], play_with_cart=[1,2,3,4,5])

    # BATCH.draw()

def alife_chk(dt=None):
    global ERROR_LOG
    global ERROR_COUNT
    global DB
    # log.stderr_logger.error('alife run!')
    for i in range(5):
        response = client.send('ALIFE_VISUAL', my_name=MY_IP, timeout=5)
        if response == None:
            log.stderr_logger.error('CHECK SERVER NOT RESPONSE!')
            time.sleep(1)
            ERROR_COUNT = ERROR_COUNT + 1
        else:
            ERROR_COUNT = 0
            break
    if response == None:
        if ERROR_COUNT >= 5:
            ERROR_LOG = '00'
            ERROR_COUNT = 0
            DB = None
    elif response == False:
        ERROR_COUNT = 0
        ERROR_LOG = '16'
        ERROR_COUNT = 0
        DB = None
    elif type(response) == list:
        ERROR_COUNT = 0
        if 'ACTIV' == response[0]:
            err = response[1][19:21]
        # else:
            # err = '00'
        #         elif 'error' in response[1]:
        #             err = response['error']
        ERROR_LOG = err
        DB = None
    else:
        ERROR_COUNT = 0

def get_db():
    global DB
    global MY_GROUP
    global ERROR_LOG
    DB = {}
    MAIN_GRUP = None
    key = client.send('GET_DB_KEYS')

    for i in range(3):
        if key != None:
            break
        else:
            key = client.send('GET_DB_KEYS')
            time.sleep(3)

    if key == None:
        ERROR_LOG = '00'
        DB = None
        return
    for i in key:
        for b in range(5):
            a = client.send('GET_DB_KEY', key=i)
            if a != None:
                DB[i] = a
                break
            else:
                DB[i] = None
                time.sleep(5)
    if None in DB.values():
        DB = None
    if DB != None or DB != False:
        for i in DB:
            if DB[i] != False:
                if 'ACTIV' in DB[i]:
                    DB = DB[i]
                    break
                if DB[i] == None:
                    DB = None
                    break
        if type(DB) == list:
            time.sleep(10)
            err = DB[1]
            if 'error' not in err:
                err = err[19:21]
            elif DB[0] == 'ACTIV':
                err = DB[1][19:21]
            else:
                err = err['error']
            ERROR_LOG = err
            DB = None
            MAIN_GRUP = None
        else:
            try:
                MY_GROUP = DB['visual'][MY_IP]['group']
                ERROR_LOG = False
                if str(MY_GROUP) == u'Свободни':
                    MY_GROUP = None
                # elif MAIN_GRUP == 'Свободни':
                #     MAIN_GRUP = None
            except KeyError:
                ERROR_LOG = '16'
            else:
                if not MY_GROUP:
                    ERROR_LOG = '16'
            return
    elif DB == None or DB == False:
        ERROR_LOG = '00'
    return



def get_db_group(key='group'):
    global ERROR_LOG
    for i in range(10):
        a = client.send('GET_DB_KEY', key=key)

        if a != None:
            break
    if type(a) == list:
        err = a[1]
        if 'error' not in err:
            err = err[19:21]
        elif a[0] == 'ACTIV':
            err = a[1][19:21]
        else:
            err = err['error']
        ERROR_LOG = err
    else:
        log.stdout_logger.info('GET FROM SERVER: %s', str(a))
        return a

def format_bet_data():
    global DB
    global MY_GROUP
    global ERROR_LOG
    var = []
    try:
        for item in DB['group'][MY_GROUP]['level']:
            var.append(DB['group'][MY_GROUP]['level'][item]['down']['to'])
    except KeyError as e:
        DB = None
        ERROR_LOG = None
        return
    var.sort(reverse=True)
    data = []
    for b in var:
        for level in DB['group'][MY_GROUP]['level']:
            if DB['group'][MY_GROUP]['level'][level]['down']['to'] == b:
                if DB['group'][MY_GROUP]['level'][level]['name'] not in data:
                    data.append(DB['group'][MY_GROUP]['level'][level]['name'])
    ranges = []
    bet = []
    activ = []
    values = []
    runner = []
    x2 = []
    play_with_cart = []
    times = False
    count = 1
    date_now = datetime.datetime.utcnow()
    date_now = date_now.replace(tzinfo=pytz.UTC)
    date_now = date_now.astimezone(pytz.timezone(config.TZ))

    sm_day = datetime.date.weekday(date_now)
    sm_day = str(sm_day)
    color = ['red', 'red', 'purple', 'yellow', 'blue', 'green']
    if DB['group'][MY_GROUP]['game_type'] == 0:
        for i in data:
            if config.SUM_RUNNER is True and DB['group'][MY_GROUP]['level'][i]['bet'] == True:
                ranges.append({'from': DB['group'][MY_GROUP]['level'][i]['down']['from'],
                               'to': DB['group'][MY_GROUP]['level'][i]['down']['to'] +
                                     DB['group'][MY_GROUP]['level'][i]['runner']['to']})

            else:
                ranges.append({'from': DB['group'][MY_GROUP]['level'][i]['down']['from'],
                               'to': DB['group'][MY_GROUP]['level'][i]['down']['to']})
            if DB['group'][MY_GROUP]['level'][i]['bet'] is False:
                bet.append(DB['group'][MY_GROUP]['level'][i]['min bet'])
            else:
                bet.append(0)
            if DB['group'][MY_GROUP]['level'][i]['value'] >= DB['group'][MY_GROUP]['level'][i]['down']['from']:
                activ.append(count)
            values.append(DB['group'][MY_GROUP]['level'][i]['value'])
            if DB['group'][MY_GROUP]['level'][i]['bet'] is True:
                runner.append(count)
            if DB['group'][MY_GROUP]['level'][i]['x2'] is True:
                if DB['group'][MY_GROUP]['level'][i]['x2_time']['from'] <= date_now.hour and DB['group'][MY_GROUP]['level'][i]['x2_time']['to'] > date_now.hour:
                    x2.append(count)
            if DB['group'][MY_GROUP]['level'][i]['player'] is True:
                play_with_cart.append(count)
            DB['group'][MY_GROUP]['level'][i]['color'] = color[count]
            count += 1
    else:
        for i in data:
            # TODO: Времева игра
            ranges.append({'from': DB['group'][MY_GROUP]['level'][i]['down']['from'],
                            'to': DB['group'][MY_GROUP]['level'][i]['down']['to']})
            if DB['group'][MY_GROUP]['level'][i]['bet'] is False:
                bet.append(DB['group'][MY_GROUP]['level'][i]['min bet'])
            else:
                bet.append(0)
            if DB['group'][MY_GROUP]['level'][i]['value'] >= DB['group'][MY_GROUP]['level'][i]['down']['from']:
                activ.append(count)
            values.append(DB['group'][MY_GROUP]['level'][i]['value'])
            if DB['group'][MY_GROUP]['level'][i]['bet'] is True:
                runner.append(count)
            DB['group'][MY_GROUP]['level'][i]['color'] = color[count]
            count += 1
            times = True
    stop_group = False
    if DB['group'][MY_GROUP]['activ'] != {}:
        if sm_day not in DB['group'][MY_GROUP]['activ']:
            stop_group = True
        else:
            if DB['group'][MY_GROUP]['activ'][sm_day]['from_hour'] <= date_now.hour and \
                    DB['group'][MY_GROUP]['activ'][sm_day]['to_hour'] > date_now.hour:
                stop_group = False
            else:
                stop_group = True
    data = {'ranges':ranges,
        'bet': bet,
        'activ':activ,
        'values':values,
        'runner':runner,
        'x2':x2,
        'play_with_cart':play_with_cart,
        'times':times,
        'stop_group':stop_group}
    return data

def add_bet_in_db(data):
    global DB
    global MY_GROUP
    for i in data['level']:
        DB['group'][MY_GROUP]['level'][i]['value'] = data['level'][i]

def play_runner(dt):
    global CHANGE_PLAY
    CHANGE_PLAY = time.time() + 40
    play_sound(resources.RUNNER_WAV)

def play_won(dt):
    play_sound(resources.DOWN_WAV)

def add_runner_in_db(data):
    global DB
    global MY_GROUP
    data['from'] = DB['group'][MY_GROUP]['level'][data['level']]['runner']['from']
    data['to'] = DB['group'][MY_GROUP]['level'][data['level']]['runner']['to']
    DB['group'][MY_GROUP]['level'][data['level']]['runner'] = data
    DB['group'][MY_GROUP]['level'][data['level']]['value'] = data['value']


def format_procent():
    global DB
    global MY_GROUP
    global RUNNER_COUNT
    proc = []
    all_pr = 0
    for i in DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['runner']['bet']:
        all_pr = all_pr + DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['runner']['bet'][i]
    for i in sorted(DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['runner']['bet'].keys(), reverse=True):
        tmp = 1
        try:
            tmp = int((((float(DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['runner']['bet'][i]) / all_pr) * 100) / 10))
        except ZeroDivisionError:
            pass
        proc.append(tmp)
    tmp = []
    for i in proc:
        if i <= 0:
            i=1
        tmp.append(i)
    proc = tmp
    return proc

def add_runer():
    global DB
    global MY_GROUP
    global RUNNER_COUNT
    date_now = datetime.datetime.utcnow()
    date_now = date_now.replace(tzinfo=pytz.UTC)
    date_now = date_now.astimezone(pytz.timezone(config.TZ))

    sm_day = datetime.date.weekday(date_now)
    sm_day = str(sm_day)
    x2 = False
    # print (RUNNER_COUNT, DB['group'][MY_GROUP]['level'])
    if DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['x2'] is True:
        if DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['x2_time']['from'] <= date_now.hour and DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['x2_time']['to'] > date_now.hour:
            x2 = True
    max_len = DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['runner_count']
    try:
        color = DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['color']
    except KeyError:
        format_bet_data()
        try:
            color = DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['color']
        except KeyError:
            color = 'red'
    # if 'go_down' not in DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['runner']:
    #     get_db()
    #     add_runner_in_db(data)
    go_down = DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['runner']['go_down']
    value = DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['runner']['value']
    device = []
    if 'bet' in DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['runner']:
        for i in sorted(DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['runner']['bet'].keys(), reverse=True):
            device.append(DB['smib'][i]['licenz'])
    else:
        DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['runner']['bet'] = {}
    procent = format_procent()
    # ranges = []
    # ranges.append({'from': DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['runner']['from'],
    #                'to': DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['runner']['to']})
    data = {'color':color, 'values':[value], 'device':device, 'procent':procent, 'down_on':go_down, 'max_len':max_len, 'x2':x2}
    return data

def down(data):
    global MY_GROUP
    global DB
    try:
        color = DB['group'][MY_GROUP]['level'][data['level']]['color']
    except KeyError:
        color = 'red'
    DOWN.down_show(data['value'], data['mashin'], color, data['casino_name'])

EMPTY_ERROR = time.time() + 10

Q_TIME = time.time() + config.Q_TIMEOUT
MY_TIME = time.time()

def query_clear(q=Q.queue, numbs=100, alls=False):
    if alls == True:
        return []
    tmp = []
    for i in q:
        if i.priority != numbs:
            tmp.append(i)
    return tmp

OLD_RUNNER_DATA = None

def beep(dt):
    play_sound(resources.BEEP)

@window.event
def on_draw():
    global MY_TIME2
    global FIELD
    global COUNT
    global REVERT
    global BACKGROUND
    global FIRST
    global COUNTERS
    global DOWN
    global ERROR
    global RUNNER
    global ERROR_LOG
    global DB
    global MY_IP
    global MY_GROUP
    global DOWN_COUNT
    global RUNNER_COUNT
    global RUNNER_TIME
    global Q
    global ALIFE_START
    global DOWN_DATA
    global EMPTY_ERROR
    global MY_TIME
    global OLD_RUNNER_DATA
    global CHANGE_PLAY
    try:
        if len(Q.queue) > config.Q_MAX_COUNT:
            log.stdout_logger.warning('MAX Q COUNT: %s', config.Q_MAX_COUNT)
            Q.queue = query_clear(Q.queue, 100)
            Q.queue = query_clear(Q.queue, 101)
            Q.queue = query_clear(Q.queue, 102)
        if ERROR_LOG is None:
            ERROR.show_error('', text='SYSTEM LOADING')
            ERROR_LOG = 'GET_DB'
        elif ERROR_LOG == 'GET_DB' and not DB:
            ERROR.show_error('', text='SYSTEM LOADING')
            get_db()
        elif ERROR_LOG == '00':
            ERROR.show_error(ERROR_LOG)
            try:
                pyglet.clock.unschedule(play_won)
            except:
                pass
            try:
                pyglet.clock.unschedule(play_runner)
            except:
                pass
            get_db()
        elif MY_IP == 'None' or not MY_IP:
            ERROR_LOG = '16'
            Q.queue = query_clear(Q.queue, 100)
            Q.queue = query_clear(Q.queue, 101)
            Q.queue = query_clear(Q.queue, 102)
            ERROR.show_error(ERROR_LOG)
            try:
                data = Q.get(timeout=config.Q_TIMEOUT)
            except Empty:
                alife_chk()
            else:
                if data.priority == 2:
                    # Q.queue = []
                    config.CONF.update_option('SYSTEM', ip=data.item[1]['visual_ip'])
                    MY_IP = data.item[1]['visual_ip']
                    config.IP = data.item[1]['visual_ip']
                    DB = None

        elif MY_GROUP == None:
            ERROR_LOG = '16'
            try:
                pyglet.clock.unschedule(play_won)
            except:
                pass
            try:
                pyglet.clock.unschedule(play_runner)
            except:
                pass
            ERROR.show_error(ERROR_LOG)
            Q.queue = query_clear(Q.queue, 100)
            Q.queue = query_clear(Q.queue, 101)
            Q.queue = query_clear(Q.queue, 102)
            try:
                data = Q.get(timeout=config.Q_TIMEOUT)
            except Empty:
                alife_chk()
            else:
                if data.priority == 1:
                    FIELD.full_reset()
                    COUNTERS.full_reset()
                    DOWN.reset()
                    RUNNER.full_reset()
                    # Q.queue = []
                    DB = None
                    get_db()
                if data.priority == 2:
                    # Q.queue = []
                    config.CONF.update_option('SYSTEM', ip=data.item[1]['visual_ip'])
                    MY_IP = data.item[1]['visual_ip']
                    config.IP = data.item[1]['visual_ip']
                    FIELD.full_reset()
                    COUNTERS.full_reset()
                    DOWN.reset()
                    RUNNER.full_reset()
                    # Q.queue = []
                    DB = None
                    # get_db()
        elif DB is None:
            FIELD.full_reset()
            COUNTERS.full_reset()
            DOWN.reset()
            RUNNER.full_reset()

            get_db()
            Q.queue = query_clear(Q.queue, 100)
            Q.queue = query_clear(Q.queue, 101)
            Q.queue = query_clear(Q.queue, 102)
            if DB is None:
                ERROR_LOG = '00'
                ERROR.show_error(ERROR_LOG)
            try:
                pyglet.clock.unschedule(play_won)
            except:
                pass
            try:
                pyglet.clock.unschedule(play_runner)
            except:
                pass
            RUNNER_COUNT = 0
            OLD_RUNNER_DATA = None
            DOWN_COUNT = 0
            DOWN_DATA = None
        elif ERROR_LOG != None and ERROR_LOG != False:
            ERROR.show_error(ERROR_LOG)
            if ERROR_LOG == '20':
                if datetime.datetime.now().year >= 2023:
                    ERROR_LOG = False
            Q.queue = query_clear(Q.queue, 100)
            Q.queue = query_clear(Q.queue, 101)
            Q.queue = query_clear(Q.queue, 102)
            try:
                data = Q.get(timeout=config.Q_TIMEOUT)
            except Empty:
                alife_chk()
            else:
                if data.priority == 1:
                    FIELD.full_reset()
                    COUNTERS.full_reset()
                    DOWN.reset()
                    RUNNER.full_reset()
                    # Q.queue = []
                    DB = None
                    # get_db()
                if data.priority == 2:
                    # Q.queue = []
                    config.CONF.update_option('SYSTEM', ip=data.item[1]['visual_ip'])
                    MY_IP = data.item[1]['visual_ip']
                    config.IP = data.item[1]['visual_ip']
                    FIELD.full_reset()
                    COUNTERS.full_reset()
                    DOWN.reset()
                    RUNNER.full_reset()
                    # Q.queue = []
                    DB = None
                    # get_db()
            # Q.queue = query_clear(alls=True)
        elif DB['group'] is None:
            DB['group'] = get_db_group('group')
            Q.queue = query_clear(Q.queue, 100)
            Q.queue = query_clear(Q.queue, 101)
            Q.queue = query_clear(Q.queue, 102)
        elif datetime.datetime.now().year < 2023:
            ERROR_LOG = '20'
            ERROR.show_error(ERROR_LOG)
            Q.queue = query_clear(Q.queue, 100)
            Q.queue = query_clear(Q.queue, 101)
            Q.queue = query_clear(Q.queue, 102)
        else:
            ERROR_LOG = False
            try:
                data = Q.get_nowait()
                EMPTY_ERROR = time.time() + 10
                log.stdout_logger.info('q data: priority-%s, item %s' % (data.priority, data.item))
                if data.priority == 1:
                    FIELD.full_reset()
                    COUNTERS.full_reset()
                    DOWN.reset()
                    RUNNER.full_reset()
                    DB = None
                    get_db()
                    if RUNNER_COUNT:
                        RUNNER_COUNT = OLD_RUNNER_DATA.item[1]['level']
                        RUNNER_TIME = time.time()
                        add_runner_in_db(OLD_RUNNER_DATA.item[1])
                    Q.queue = query_clear(Q.queue, 100)
                    Q.queue = query_clear(Q.queue, 101)
                    Q.queue = query_clear(Q.queue, 102)
                    Q.queue = query_clear(Q.queue, 1)
                    # Q.queue = query_clear(Q.queue, 1)
                elif data.priority == 98:
                    restart_program()
                elif data.priority == 97:
                    kill_visual()
                elif data.priority == 3:
                    ERROR_LOG = str(data.item)
                elif data.priority == 9:
                    play_sound(resources.CHANGE_WAV)
                elif data.priority == 102:
                    try:
                        tmp = Q.queue[-1]
                        Q.queue = query_clear(Q.queue, numbs=102)
                        if tmp.priority == 102:
                            data = tmp
                    except IndexError:
                        pass
                    add_bet_in_db(data.item[1])
                    OLD_RUNNER_DATA = None
                elif data.priority == 100:
                    CHANGE_PLAY = time.time()
                    play_sound(resources.CHANGE_WAV)
                    RUNNER_COUNT = data.item[1]['level']
                    RUNNER_TIME = time.time()
                    pyglet.clock.schedule_interval(play_runner, 120)
                    add_runner_in_db(data.item[1])
                    Q.queue = query_clear(Q.queue, numbs=100)
                    Q.queue = query_clear(Q.queue, numbs=101)
                    Q.queue = query_clear(Q.queue, numbs=102)
                    OLD_RUNNER_DATA = None
                elif data.priority == 101:
                    try:
                        tmp = Q.queue[-1]
                        Q.queue = query_clear(Q.queue, numbs=101)
                        Q.queue = query_clear(Q.queue, numbs=102)
                        Q.queue = query_clear(Q.queue, numbs=100)
                        if tmp.priority == 101:
                            data = tmp
                    except IndexError:
                        pass

                    # Q.queue = query_clear(Q.queue, numbs=102)
                    # Q.queue = query_clear(Q.queue, numbs=101)
                    RUNNER_TIME = time.time()
                    if RUNNER_COUNT == 0:
                        CHANGE_PLAY = time.time()
                        play_sound(resources.CHANGE_WAV)
                        pyglet.clock.schedule_interval(play_runner, 120)
                    OLD_RUNNER_DATA = data
                    RUNNER_COUNT = data.item[1]['level']
                    add_runner_in_db(data.item[1])
                elif data.priority == 4:
                    RUNNER_COUNT = 0
                    DOWN_COUNT = time.time() + 60
                    DOWN_DATA = data.item[1]
                    play_won(None)
                    pyglet.clock.schedule_interval(play_won, 30)
                    try:
                        del DB['group'][MY_GROUP]['level'][RUNNER_COUNT]['runner']
                    except KeyError:
                        pass
                    Q.queue = query_clear(Q.queue, numbs=4)

                pyglet.clock.unschedule(alife_chk)
                ALIFE_START = False

            except Empty:
                if ALIFE_START is False and EMPTY_ERROR < time.time():
                    pyglet.clock.schedule_interval(alife_chk, config.ALIFE_INTERVAL)
                    ALIFE_START = True
            # if not DB:
            #     window.clear()
            if DB == None:
                get_db()
            elif MY_GROUP not in DB['group']:
                DB = None
                get_db()
                ERROR_LOG = '16'
                ERROR.show_error(ERROR_LOG)
                # DB['group'] = get_db_group('group')
            else:
                # if data.priority == 102 or data.priority == 101 or data.priority == 100:
                if not DOWN_COUNT:
                    BACKGROUND.show()
                    if not RUNNER_COUNT:
                        data = format_bet_data()
                        log.stdout_logger.debug('data format: %s', data)
                        FIELD.show(len(data['ranges']),
                                       activ=data['activ'],
                                       times=data['times'],
                                       bet=data['bet'],
                                       ranges=data['ranges'],
                                       stop_group=data['stop_group'],
                                       x2=data['x2'],
                                       runner=data['runner'],
                                       play_with_cart=data['play_with_cart'])
                        COUNTERS.show(**data)
                    elif RUNNER_COUNT:
                        if RUNNER_TIME + 300 < time.time():
                            pyglet.clock.unschedule(play_runner)
                            get_db()
                            RUNNER_COUNT = 0
                        else:
                            data = add_runer()
                            if data['device'] != RUNNER.device and CHANGE_PLAY == None:
                                pyglet.clock.schedule_once(beep, 0)
                            elif data['device'] != RUNNER.device and CHANGE_PLAY + 10 < time.time():
                                pyglet.clock.schedule_once(beep, 0)
                            RUNNER.show(**data)
                else:
                        # log.stderr_logger.error('down %s', DOWN_DATA)
                    down(DOWN_DATA)
                    # kill_visual()
                    # Q.queue = []
                    pyglet.clock.unschedule(play_runner)
                    if DOWN_COUNT <= time.time():
                        pyglet.clock.unschedule(play_won)
                        DOWN_COUNT = 0
                        DOWN_DATA = None
                        DB['group'] = None
                        DB['group'] = get_db_group('group')
                        CHANGE_PLAY = None
                    elif DOWN_COUNT + 120 <= time.time():
                        DOWN_COUNT = 0
                        DOWN_DATA = None
                        DB['group'] = None
                        DB['group'] = get_db_group('group')
                        CHANGE_PLAY = None
    # except Empty:
    #     if time.time() >= MY_TIME:
    #         MY_TIME = time.time() + config.ALIFE_INTERVAL
    #         alife_chk()

    except Exception as e:
        DB = None
        log.stdout_logger.critical(e, exc_info=True)

    if config.DEBUG is True:
        fps_display.draw()


# COUNT = 0
# def change_count(dt):
#     global VALUES
#     global COUNT
#     # window.flip()
#     if COUNT <20:
#         VALUES[0] += 0.08
#         COUNT += 1
#     else:
#         COUNT += 1
#     if COUNT > 40:
#         COUNT = 0
#     # VALUES[1] += 0.03
#     # VALUES[2] += 0.04
#     # VALUES[3] += 0.05
#     # VALUES[4] += 0.02
#
# pyglet.clock.schedule_interval_soft(change_count, 1)
def server_start():
    global SERVER
    SERVER = server.run_server(server.Handler, crypt=config.CRYPT, timeout=config.UDP_TIMEOUT,
                      buffer=config.UDP_BUFFER, in_thread=False, port=config.SELF_PORT,
                      ip='0.0.0.0', logging=log.stdout_logger)

server_start()

b = threading.Thread(target=weckup.wekup)
b.start()
# pyglet.clock.schedule_interval(on_draw, 1 / 60.0)
pyglet.app.run()
SERVER.shutdown()
SERVER.socket.close()