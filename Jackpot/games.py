# -*- coding:utf-8 -*-
'''
Created on 27.03.2017 г.

@author: dedal
'''
import calc  # @UnresolvedImport
import time  # @UnusedImport
import datetime
from time import mktime
import conf
import security.init
import exception
from threading import Thread
from multiprocessing import Process
from multiprocessing import Pipe
from multiprocessing import Queue
# import threading
# from functools import partial
import pytz
import db.db
import udp.client

# import socket.timeout

DB = db.db.MemDB()
SEND = udp.client.send
SEND_TO_VISUAL = udp.client.visual_send
VISUAL_Q = Queue()
# PIPE = {}
# ALL_PROC = {}


def down_rotation(curent, from_val, to_val, step, bet, down):
    dif_betwen = to_val - from_val
    my_val_now = curent - from_val
    stop_rotation_count = int((my_val_now / dif_betwen) * 100)
    for i in range(0, stop_rotation_count, step):
        if i == 0:
            pass
        else:
            bet = bet - (bet * down)
    return bet


def send_to_visual_direct(evt, ip, grup, level, value, mashin, bet=None, sas=True, go_down=0, port=conf.UDP_VISUAL_PORT, timeout=conf.UDP_TIMEOUT, casino_name=''):
    # data = DB.get_key('group')
    # data = data[grup]
    # for visual in data['visual']:

    try:
        if evt == 'ADD_BET':
            response = SEND_TO_VISUAL(ip=ip, port=port, evt=evt, grup=grup,
                                      level=level, mashin=mashin, timeout=timeout)
        elif evt == 'RUNER':
            response = SEND_TO_VISUAL(ip=ip, evt=evt, port=port, grup=grup,
                                      level=level, value=value, mashin=mashin, bet=bet,
                                      go_down=go_down, timeout=timeout)
        elif evt == 'DOWN':
            for i in range(3):
                response = SEND_TO_VISUAL(ip=ip, port=port, evt=evt, grup=grup,
                                          level=level, value=value, mashin=mashin,
                                          sas=sas, timeout=5, casino_name=casino_name)
                if response == True:
                    break
                # if response == True:
                #     break
        elif evt == 'START_RUNER':
            response = SEND_TO_VISUAL(ip=ip, port=port, evt=evt, grup=grup,
                                      level=level, value=value, mashin=mashin,
                                      go_down=go_down, timeout=timeout)
        else:
            response = SEND_TO_VISUAL(ip=ip, port=port, evt=evt, grup=grup,
                                      level=level, value=value, mashin=mashin, timeout=5)
    except exception as e:
        exception.log.stderr_logger.critical(e, exc_info=True)

def log_write(level, grup, down_sum, down_on, min_bet=0, chk=True):
    # t = time.time() + conf.UDP_TIMEOUT

    tmp = DB.check_for_lock()
    if tmp != b'DOWN_ON':
        DB.set_lock(model='DOWN_ON')
    else:
        return False
    #
    #         break
    #     else:
    #         return False
    #     if time.time() >= t:
    #         return False
    DB.set_key('backup_log_stop', True)
    # tmp = DB.check_for_lock()
    # if tmp == b'DOWN_ON':
    #     DB.set_lock(model='DOWN_ON')
    # else:
    #     DB.set_lock(model=DB.check_for_lock())
    log_db = db.db.SQLite(name='log.db')

    date_now = datetime.datetime.utcnow()
    date_now = date_now.replace(tzinfo=pytz.UTC)
    date_now = date_now.astimezone(pytz.timezone(conf.RTC_TIME_ZONE))
    down_stop = DB.get_key('down_stop')
    mashin = DB.get_key('smib')
    sas = mashin[down_on]['sas']
    dates = date_now.strftime('%Y-%m-%d')
    times = date_now.strftime('%H:%M:%S')
    try:
        log = log_db.get_key(dates)
        if log == None:
            raise KeyError
    except KeyError:
        log_db.set_key(dates, {})
        log_db.sync()
        log = log_db.get_key(dates)
    # last_data = DB.get_key('group')
    # if last_data[grup]['level'][level]['value'] < last_data[grup]['level'][level]['down_value']:
    #     raise KeyError
    if sas == True:
        response = SEND(ip=down_on,
                        evt='sas.jp_down',
                        mony=round(down_sum, 2),
                        tax='00',
                        min_bet=min_bet,
                        port=conf.UDP_SMIB_PORT,
                        timeout=conf.UDP_TIMEOUT+2)
        print('ERROR, timeout %s', response)

        if response == None and chk == True:
            response = SEND(ip=down_on,
                            evt='send_chk_jp_down',
                            port=conf.UDP_SMIB_PORT,
                            timeout=conf.UDP_TIMEOUT)
            print('ERROR chk, timeout %s', response)
        if response == True or response == None:
            down_on = mashin[down_on]['licenz']
            send_to_visual(evt='DOWN', grup=grup, level=level, value=down_sum, mashin=down_on, sas=sas, timeout=5)
            try:
                log[grup]
                log[grup].append({'hour': times, 'mashin': down_on, 'down': level, 'sum': down_sum})
            except KeyError:
                log[grup] = [{'hour': times, 'mashin': down_on, 'down': level, 'sum': down_sum}]
            try:
                log_db.set_key(dates, log)
                log_db.sync()
                log_db.close()
                down_stop = DB.get_key('down_stop')
                down_stop[grup] = time.time()
                DB.set_key('down_stop', down_stop)
            except Exception as e:
                exception.log.stderr_logger.critical(e, exc_info=True)
            DB.set_key('backup_log_stop', False)
            DB.set_lock(model=tmp)
            return True

    elif sas == False:
        down_on = mashin[down_on]['licenz']
        try:
            log[grup]
        except KeyError:
            log[grup] = {}

        if dates not in log[grup]:
            log[grup] = [{'hour': times, 'mashin': down_on, 'down': level, 'sum': down_sum}]
        else:
            log[grup].append({'hour': times, 'mashin': down_on, 'down': level, 'sum': down_sum})
        log_db.set_key(dates, log)
        log_db.sync()
        log_db.close()

        send_to_visual(evt='DOWN', grup=grup, level=level, value=round(down_sum, 2), mashin=down_on, sas=sas, timeout=5)
        down_stop[grup] = time.time() + 3600
        DB.set_key('down_stop', down_stop)
        DB.set_key('backup_log_stop', False)
        DB.set_lock(model=tmp)
        return True
    DB.set_key('backup_log_stop', False)
    log_db.close()
    DB.set_lock(model=tmp)
    return False


# def send_data(ip, pipe):
#     #     data = DB.get_key('group')
#     #     data = data[grup]
#     #     for visual in data['visual']:
#     #     count = 0
#     while True:
#         data = pipe.recv()
#         # while pipe.poll():
#         #     if data['evt'] == 'ADD_BET':
#         #         print 'clean visual pipe'
#         #         data = pipe.recv()
#         #     elif data['evt'] == 'RUNER':
#         #         print 'clean visual pipe'
#         #         data = pipe.recv()
#         #     else:
#         #         break
#         # response = None
#         if 'timeout' in data:
#             timeout = data['timeout']
#         else:
#             timeout = conf.UDP_TIMEOUT
#         #         print count

        # if response == None:
        #     while pipe.poll():
        #         print 'clean visual pipe no response'
        #         pipe.recv()


# def create_proc():
#     global PIPE
#     global ALL_PROC
#     visual = DB.get_key('visual').keys()
#     for i in visual:
#         PIPE[i + '_send'], PIPE[i + '_recv'] = Pipe()
#         ALL_PROC[i] = Process(target=send_data, args=(i, PIPE[i + '_recv']))
#     for i in ALL_PROC:
#         ALL_PROC[i].start()


def send_to_visual(evt, grup, level, value, mashin, bet=None, sas=True, go_down=0, port=conf.UDP_VISUAL_PORT, timeout=conf.UDP_VISUAL_TIMEOUT, **kwargs):
    data = DB.get_key('group')
    try:
        data = data[grup]
    except KeyError as e:
        print(e)
        return
    visual = DB.get_key('visual')
    if data['hiden_visual'] is True:
        for i in data['visual']:
            visual[i]['group'] = grup
    casino_name = DB.get_key('casino_name')
    # global VISUAL_Q
    # global ALL_PROC
    # casino_name = DB.get_key('casino_name')
    # exception.log.stderr_logger.info('visual %s' % (str(visual)))
    # if global_gup is True:
    #     try:
    #         send_to_global = DB.mem_cach2.get('DOWN')
    #     except:
    #         send_to_global = DB.mem_cach.get('DOWN')
    #     casino_name = DB.get_key('casino_name')
    #     if send_to_global:
    #         if casino_name['name'] not in send_to_global['casino_name']:
    #             send_to_global['casino_name'].append(casino_name['name'])
    #             try:
    #                 DB.mem_cach2.set('DOWN', send_to_global)
    #             except:
    #                 DB.mem_cach.set('DOWN', send_to_global)
    #             kwargs = send_to_global
    # else:
    kwargs = {
            'evt': evt,
            'grup': grup,
            'level': level,
            'value': value,
            'mashin': mashin,
            'bet': bet,
            'sas': sas,
            'go_down': go_down,
            'port': port,
            'timeout': timeout,
            'casino_name':casino_name['name']
        }
    exception.log.stderr_logger.info('send to visual %s', kwargs)
    if 'global_mistery' in data:
        if data['global_mistery'] is True:
            # pass

            if evt == 'ADD_BET' or evt == 'RUNER' or evt == 'START_RUNER':
                if casino_name['ip']:
                    DB.mem_cach2.set('ADD_BET', kwargs)
                else:
                    DB.mem_cach.set('ADD_BET', kwargs)
            else:
                if casino_name['ip']:
                    DB.mem_cach2.set('DOWN', kwargs)
                else:
                    DB.mem_cach.set('DOWN', kwargs)
        else:
            for i in visual:
                if grup == visual[i]['group']:
                    send_to_visual_direct(ip=i, **kwargs)
    else:
        for i in visual:
            if grup == visual[i]['group']:
                send_to_visual_direct(ip=i, **kwargs)


def get_first_3(data, count=3):
    all_bet = data.copy()
    ips = []
    bets = []
    for i in all_bet:
        ips.append(i)
        bets.append(all_bet[i])
    for i in range(len(all_bet) - count):
        my_bet = min(bets)
        ind = bets.index(my_bet)
        del bets[ind]
        my_ip = ips[ind]
        del ips[ind]
        del all_bet[my_ip]
    return all_bet


def time_level(ip, bet, grup, level, db):
    data = db
    go_down = DB.get_key('go_down')
    # raise KeyError, go_down

    #     log = DB.get_key('log')
    # if DB.get_key('stop_rotation') == True:
    #     return data

    down_stop = DB.get_key('down_stop')
    my_time = time.time()
    real_bet = bet
    date_now = datetime.datetime.utcnow()
    date_now = date_now.replace(tzinfo=pytz.UTC)
    date_now = date_now.astimezone(pytz.timezone(conf.RTC_TIME_ZONE))

    sm = datetime.date.weekday(date_now)
    last_down = time.gmtime(data[grup]['level'][level]['last_down'])
    last_down = datetime.datetime.fromtimestamp(mktime(last_down))
    last_down = last_down.replace(tzinfo=pytz.UTC)
    last_down = last_down.astimezone(pytz.timezone(conf.RTC_TIME_ZONE))
    # try:
    #     data[grup]['min_mashin']
    # except KeyError:
    #     data[grup]['min_mashin'] = 0
    # try:
    #     data[grup]['min_mashin_play_time']
    # except KeyError:
    #     data[grup]['min_mashin_play_time'] = 1

    try:
        go_down[grup]
    except KeyError:
        go_down[grup] = {}

    if len(str(date_now.minute)) == 1:
        hour_now = '%s.0%s' % (date_now.hour, date_now.minute)
    else:
        hour_now = '%s.%s' % (date_now.hour, date_now.minute)
    hour_now = float(hour_now)

    if data[grup]['min_mashin'] > 1:
        if (sm in data[grup]['level'][level]['day_down'] and
                hour_now >= data[grup]['level'][level]['down']['from'] and
                hour_now < data[grup]['level'][level]['down']['to']):
            if ip not in go_down[grup]:
                go_down[grup][ip] = [time.time(), time.time()]
            else:
                go_down[grup][ip][0] = time.time()
        elif (data[grup]['level'][level]['day_down'][0] == -1 and
              hour_now >= data[grup]['level'][level]['down']['from'] and
              hour_now < data[grup]['level'][level]['down']['to'] and
              hour_now >= data[grup]['level'][level]['down_value']):
            if ip not in go_down[grup]:
                go_down[grup][ip] = [time.time(), time.time()]
            else:
                go_down[grup][ip][0] = time.time()
    else:
        go_down[grup] = {}
    # print  time.time() - go_down[grup][ip][1] < (data[grup]['min_mashin_play_time'] * 60)
    tmp = {}
    if data[grup]['min_mashin'] > 1:
        try:
            for i in go_down[grup].keys():
                if go_down[grup][i][0] + 60 <= time.time():  # (data[grup]['min_mashin_play_time'] * 60) <= time.time():
                    del go_down[grup][i]
        except:
            go_down[grup] = {}
    for i in go_down[grup].keys():
        tmp[i] = go_down[grup][i]
    try:
        down_stop[grup]
    except KeyError:
        down_stop[grup] = False
        DB.set_key('down_stop', down_stop)

    if down_stop[grup] != False and down_stop[grup] + (conf.JP_BLOCK_TIME * 60) <= my_time:
        down_stop[grup] = False
        DB.set_key('down_stop', down_stop)
    try:
        data[grup]['real_down_procent']
    except KeyError:
        data[grup]['real_down_procent'] = 0

    #     if data[grup]['hold_rotation']['use'] == True:
    #         bet = down_rotation(data[grup]['level'][level]['value'], data[grup]['level'][level]['down']['from'], data[grup]['level'][level]['down']['to'],
    #                             data[grup]['hold_rotation']['step'], bet, data[grup]['hold_rotation']['hold'])
    #         if bet <= real_bet/2:
    #             bet = real_bet/2
    if (sm in data[grup]['level'][level]['day_down'] and
            hour_now >= data[grup]['level'][level]['down']['from'] and
            hour_now < data[grup]['level'][level]['down']['to']):
        if data[grup]['level'][level]['bet'] == True and down_stop[grup] == False and bet > 0:
            data[grup]['level'][level]['value'] = data[grup]['level'][level]['value'] + (
                    bet * data[grup]['level'][level]['procent'])
    elif (data[grup]['level'][level]['day_down'][0] == -1 and
          hour_now >= data[grup]['level'][level]['down']['from'] and
          hour_now < data[grup]['level'][level]['down']['to']):
        if data[grup]['level'][level]['bet'] == True and down_stop[grup] == False and bet > 0:
            data[grup]['level'][level]['value'] = data[grup]['level'][level]['value'] + (
                    bet * data[grup]['level'][level]['procent'])
    # raise KeyError,  hour_now <= data[grup]['level'][level]['down_value']
    if (sm in data[grup]['level'][level]['day_down'] and
            hour_now >= data[grup]['level'][level]['down']['from'] and
            hour_now < data[grup]['level'][level]['down']['to'] and
            hour_now >= data[grup]['level'][level]['down_value'] and
            down_stop[grup] == False and real_bet >= data[grup]['level'][level]['min bet']):

        down_sum = data[grup]['level'][level]['value']
        log = None
        if date_now.year != last_down.year or date_now.month != last_down.month:
            if data[grup]['min_mashin'] > 1:
                for i in go_down[grup].keys():
                    if time.time() - go_down[grup][i][1] < (data[grup]['min_mashin_play_time'] * 60):
                        del go_down[grup][i]
                if len(go_down[grup].keys()) >= data[grup]['min_mashin']:
                    log = log_write(level, grup, down_sum, ip, data[grup]['level'][level]['min bet'])
                else:
                    log = False
            else:
                log = log_write(level, grup, down_sum, ip, data[grup]['level'][level]['min bet'])
            #                 if log == True:
            #                     break
            if log == True:
                go_down[grup] = {}
                tmp = {}
                data[grup]['level'][level]['value'] = data[grup]['level'][level]['start_value']
                if data[grup]['real_down_procent'] <= 1 and data[grup]['real_down_procent'] > 0:
                    next_down = calc.mk_time_range(
                        data[grup]['level'][level]['down']['from'] + data[grup]['real_down_procent'],
                        data[grup]['level'][level]['down']['to'],
                        0.01)
                else:
                    next_down = calc.mk_time_range(data[grup]['level'][level]['down']['from'],
                                                   data[grup]['level'][level]['down']['to'],
                                                   0.01)
                data[grup]['level'][level]['down_value'] = calc.mk_random(next_down)
                data[grup]['level'][level]['last_down'] = time.time()
        elif date_now.day != last_down.day:
            log = None
            if data[grup]['min_mashin'] > 1:
                for i in go_down[grup].keys():
                    if time.time() - go_down[grup][i][1] < (data[grup]['min_mashin_play_time'] * 60):
                        del go_down[grup][i]
                if len(go_down[grup].keys()) >= data[grup]['min_mashin']:
                    log = log_write(level, grup, down_sum, ip, data[grup]['level'][level]['min bet'])
                else:
                    log = False
            else:
                log = log_write(level, grup, down_sum, ip, data[grup]['level'][level]['min bet'])
            # log = log_write(level, grup, down_sum, ip, data[grup]['level'][level]['min bet'])
            #                 if log == True:
            #                     break
            if log == True:
                data[grup]['level'][level]['value'] = data[grup]['level'][level]['start_value']
                go_down[grup] = {}
                tmp = {}
                if data[grup]['real_down_procent'] <= 1 and data[grup]['real_down_procent'] > 0:
                    next_down = calc.mk_time_range(
                        data[grup]['level'][level]['down']['from'] + data[grup]['real_down_procent'],
                        data[grup]['level'][level]['down']['to'],
                        0.01)
                else:
                    next_down = calc.mk_time_range(data[grup]['level'][level]['down']['from'],
                                                   data[grup]['level'][level]['down']['to'],
                                                   0.01)
                data[grup]['level'][level]['down_value'] = calc.mk_random(next_down)
                data[grup]['level'][level]['last_down'] = time.time()


    elif (data[grup]['level'][level]['day_down'][0] == -1 and
          hour_now >= data[grup]['level'][level]['down']['from'] and
          hour_now < data[grup]['level'][level]['down']['to'] and
          hour_now >= data[grup]['level'][level]['down_value'] and
          down_stop[grup] == False and real_bet >= data[grup]['level'][level]['min bet']):

        # raise KeyError, data[grup]['level'][level]['down']['from']
        # if data[grup]['level'][level]['bet'] == True and down_stop[grup] == False and bet > 0:
        #     data[grup]['level'][level]['value'] = data[grup]['level'][level]['value'] + (
        #             bet * data[grup]['level'][level]['procent'])
        down_sum = data[grup]['level'][level]['value']
        if date_now.year != last_down.year or date_now.month != last_down.month:
            # raise KeyError, (time.time() - go_down[grup][i][1] < (data[grup]['min_mashin_play_time'] * 60))
            if data[grup]['min_mashin'] > 1:
                for i in go_down[grup].keys():
                    if time.time() - go_down[grup][i][1] < (data[grup]['min_mashin_play_time'] * 60):
                        del go_down[grup][i]
                if len(go_down[grup].keys()) >= data[grup]['min_mashin']:
                    log = log_write(level, grup, down_sum, ip, data[grup]['level'][level]['min bet'])
                else:
                    log = False
            else:
                log = log_write(level, grup, down_sum, ip, data[grup]['level'][level]['min bet'])
            # log = log_write(level, grup, down_sum, ip, data[grup]['level'][level]['min bet'])
            #                 if log == True:
            #                     break
            if log == True:
                data[grup]['level'][level]['value'] = data[grup]['level'][level]['start_value']
                go_down[grup] = {}
                tmp = {}
                if data[grup]['real_down_procent'] <= 1 and data[grup]['real_down_procent'] > 0:
                    next_down = calc.mk_time_range(
                        data[grup]['level'][level]['down']['from'] + data[grup]['real_down_procent'],
                        data[grup]['level'][level]['down']['to'],
                        0.01)
                else:
                    next_down = calc.mk_time_range(data[grup]['level'][level]['down']['from'],
                                                   data[grup]['level'][level]['down']['to'],
                                                   0.01)
                data[grup]['level'][level]['down_value'] = calc.mk_random(next_down)
                data[grup]['level'][level]['last_down'] = time.time()
        elif date_now.day != last_down.day:
            if data[grup]['min_mashin'] > 1:

                for i in go_down[grup].keys():
                    if time.time() - go_down[grup][i][1] < (data[grup]['min_mashin_play_time'] * 60):
                        del go_down[grup][i]
                if len(go_down[grup].keys()) >= data[grup]['min_mashin']:
                    log = log_write(level, grup, down_sum, ip, data[grup]['level'][level]['min bet'])
                else:
                    log = False
            else:
                log = log_write(level, grup, down_sum, ip, data[grup]['level'][level]['min bet'])
            if log == True:
                data[grup]['level'][level]['value'] = data[grup]['level'][level]['start_value']
                go_down[grup] = {}
                tmp = {}
                if data[grup]['real_down_procent'] <= 1 and data[grup]['real_down_procent'] > 0:
                    next_down = calc.mk_time_range(
                        data[grup]['level'][level]['down']['from'] + data[grup]['real_down_procent'],
                        data[grup]['level'][level]['down']['to'],
                        0.01)
                else:
                    next_down = calc.mk_time_range(data[grup]['level'][level]['down']['from'],
                                                   data[grup]['level'][level]['down']['to'],
                                                   0.01)
                data[grup]['level'][level]['down_value'] = calc.mk_random(next_down)
                data[grup]['level'][level]['last_down'] = time.time()
    DB.close()
    go_down[grup] = tmp
    DB.set_key('go_down', go_down)
    # raise KeyError, 'test'
    return data


def clasic_level(ip, bet, grup, level, db):
    data = db
    # if DB.get_key('stop_rotation') == True:
    #     return data
    if bet < 0:
        return data
    # if bet < 0:
    #     return data
    go_down = DB.get_key('go_down')
    down_stop = DB.get_key('down_stop')
    real_bet = bet
    try:
        go_down[grup]
    except KeyError:
        go_down[grup] = False
        DB.set_key('go_down', go_down)
    my_time = time.time()

    try:
        down_stop[grup]
    except KeyError:
        down_stop[grup] = False
        DB.set_key('down_stop', down_stop)

    if down_stop[grup] != False and down_stop[grup] + (conf.JP_BLOCK_TIME * 60) <= my_time:
        down_stop[grup] = False
        DB.set_key('down_stop', down_stop)

    date_now = datetime.datetime.utcnow()
    date_now = date_now.replace(tzinfo=pytz.UTC)
    date_now = date_now.astimezone(pytz.timezone(conf.RTC_TIME_ZONE))

    sm_day = datetime.date.weekday(date_now)
    sm_day = str(sm_day)
    # try:
    #     data[grup]['level'][level]['x2']
    # except KeyError:
    #     data[grup]['level'][level]['x2'] = False
    #     data[grup]['level'][level]['x2_time'] = {'from':'', 'to':''}
    # try:
    #     data[grup]['level'][level]['hold_procent']
    # except KeyError:
    #     data[grup]['level'][level]['hold_procent'] = 0
    # try:
    #     data[grup]['real_down_procent']
    # except KeyError:
    #     data[grup]['real_down_procent'] = 0
    #
    # try:
    #     data[grup]['rotate_if_min_bet']
    # except KeyError:
    #     data[grup]['rotate_if_min_bet'] = False
    #     data[grup]['hold_rotation']['step'] = 0
    #     data[grup]['hold_rotation']['hold'] = 1
    #     dif_betwen = (data[grup]['level'][level]['down']['to']-data[grup]['level'][level]['down']['from'])
    #     my_val_now = (data[grup]['level'][level]['value']-data[grup]['level'][level]['down']['from'])
    #     stop_rotation_count = int((my_val_now / dif_betwen)*100)

    if data[grup]['activ'] != {}:
        if sm_day not in data[grup]['activ']:
            return data
        else:
            if data[grup]['activ'][sm_day]['from_hour'] <= date_now.hour and data[grup]['activ'][sm_day][
                'to_hour'] > date_now.hour:
                pass
            else:
                return data
    if real_bet < data[grup]['level'][level]['min bet'] and data[grup]['rotate_if_min_bet'] == True:
        return data

    if data[grup]['hold_rotation']['use'] == True:
        bet = down_rotation(data[grup]['level'][level]['value'], data[grup]['level'][level]['down']['from'],
                            data[grup]['level'][level]['down']['to'],
                            data[grup]['hold_rotation']['step'], bet, data[grup]['hold_rotation']['hold'])
        if bet <= real_bet / 2:
            bet = real_bet / 2
    if go_down[grup] == False and bet > 0:
        data[grup]['level'][level]['value'] = data[grup]['level'][level]['value'] + (
                    bet * data[grup]['level'][level]['procent'])
        if data[grup]['level'][level]['value'] > data[grup]['level'][level]['down_value']:
            data[grup]['level'][level]['value'] = data[grup]['level'][level]['down_value']
        else:
            data[grup]['level'][level]['hiden_value'] = data[grup]['level'][level]['hiden_value'] + (
                        bet * data[grup]['level'][level]['hiden'])

    if (data[grup]['level'][level]['value'] >= data[grup]['level'][level]['down_value'] and
            real_bet >= data[grup]['level'][level]['min bet'] and down_stop[grup] == False and go_down[grup] == False):
        down_sum = data[grup]['level'][level]['value']
        log = None
        #         for i in range(conf.DOWN_COUNT):  # @UnusedVariable
        if data[grup]['level'][level]['x2'] == True:
            if data[grup]['level'][level]['x2_time']['from'] <= date_now.hour and data[grup]['level'][level]['x2_time'][
                'to'] > date_now.hour:
                down_sum = down_sum * 2
        log = log_write(level, grup, down_sum, ip, data[grup]['level'][level]['min bet'])
        #             if log == True:
        #                 break
        if log == True:
            data[grup]['level'][level]['value'] = data[grup]['level'][level]['start_value'] + \
                                                  data[grup]['level'][level]['hiden_value']
            data[grup]['level'][level]['hiden_value'] = 0.0

            down_to = data[grup]['level'][level]['down']['to'] - (data[grup]['level'][level]['down']['to'] * 0.01)
            if data[grup]['level'][level]['hold_procent'] <= 1 and data[grup]['level'][level]['hold_procent'] > 0:
                down_from = (down_to - data[grup]['level'][level]['down']['from']) * data[grup]['level'][level][
                    'hold_procent']
                down_from = data[grup]['level'][level]['down']['from'] + down_from
            elif data[grup]['real_down_procent'] <= 1 and data[grup]['real_down_procent'] > 0:
                down_from = (down_to - data[grup]['level'][level]['down']['from']) * data[grup]['real_down_procent']
                down_from = data[grup]['level'][level]['down']['from'] + down_from

            else:
                down_from = data[grup]['level'][level]['down']['from']

            next_down = calc.mk_range(down_from, down_to, 0.01)
            data[grup]['level'][level]['down_value'] = calc.mk_random(next_down)
            data[grup]['level'][level]['last_down'] = time.time()
    DB.close()
    return data


def runer(ip, bet, grup, level, db):
    # raise KeyError
    data = db
    down_stop = DB.get_key('down_stop')
    go_down = DB.get_key('go_down')
    my_time = time.time()
    try:
        down_stop[grup]
    except KeyError:
        down_stop[grup] = False
        DB.set_key('down_stop', down_stop)
    if down_stop[grup] != False and down_stop[grup] + (conf.JP_BLOCK_TIME * 60) <= my_time:
        down_stop[grup] = False
        DB.set_key('down_stop', down_stop)
    try:
        go_down[grup]
    except KeyError:
        go_down[grup] = False
        DB.set_key('go_down', go_down)
    if bet < 0:
        return data
    real_bet = bet
    # try:
    #     data[grup]['level'][level]['x2']
    # except KeyError:
    #     data[grup]['level'][level]['x2'] = False
    #     data[grup]['level'][level]['x2_time'] = {{'from':'', 'to':''}}
    # try:
    #     data[grup]['real_down_procent']
    # except KeyError:
    #     data[grup]['real_down_procent'] = 0
    # try:
    #     data[grup]['level'][level]['hold_procent']
    # except KeyError:
    #     data[grup]['level'][level]['hold_procent'] = 0
    # try:
    #     data[grup]['rotate_if_min_bet']
    # except KeyError:
    #     data[grup]['rotate_if_min_bet'] = False
    #     data[grup]['hold_rotation']['step'] = 0
    #     data[grup]['hold_rotation']['hold'] = 1

    date_now = datetime.datetime.utcnow()
    date_now = date_now.replace(tzinfo=pytz.UTC)
    date_now = date_now.astimezone(pytz.timezone(conf.RTC_TIME_ZONE))

    sm_day = datetime.date.weekday(date_now)
    sm_day = str(sm_day)

    if data[grup]['activ'] != {}:
        if sm_day not in data[grup]['activ']:
            return data
        else:
            if data[grup]['activ'][sm_day]['from_hour'] <= date_now.hour and data[grup]['activ'][sm_day]['to_hour'] > date_now.hour:
                pass
            else:
                return data
    #     if bet < data[grup]['rotate_if_min_bet']:
    #         return data
    if data[grup]['hold_rotation']['use'] == True:
        bet = down_rotation(data[grup]['level'][level]['value'], data[grup]['level'][level]['down']['from'],
                            data[grup]['level'][level]['down']['to'],
                            data[grup]['hold_rotation']['step'], bet, data[grup]['hold_rotation']['hold'])
        if bet <= real_bet / 2:
            bet = real_bet / 2

    if go_down[grup] == False and bet > 0:
        data[grup]['level'][level]['value'] = data[grup]['level'][level]['value'] + (
                    bet * data[grup]['level'][level]['procent'])
        if data[grup]['level'][level]['value'] > data[grup]['level'][level]['down_value']:
            data[grup]['level'][level]['value'] = data[grup]['level'][level]['down_value']
        else:
            data[grup]['level'][level]['hiden_value'] = data[grup]['level'][level]['hiden_value'] + (
                        bet * data[grup]['level'][level]['hiden'])
    else:
        if go_down[grup][0] == level and data[grup]['level'][level]['value'] < go_down[grup][1]:
            data[grup]['level'][level]['value'] = data[grup]['level'][level]['value'] + (
                        bet * data[grup]['level'][level]['procent'])

            data[grup]['level'][level]['hiden_value'] = data[grup]['level'][level]['hiden_value'] + (
                        bet * data[grup]['level'][level]['hiden'])
        elif go_down[grup][0] == level and data[grup]['level'][level]['value'] > go_down[grup][1]:
            data[grup]['level'][level]['value'] = go_down[grup][1]

    if (data[grup]['level'][level]['value'] >= data[grup]['level'][level]['down_value'] and
            go_down[grup] == False and
            down_stop[grup] == False):

        down_on = calc.mk_range(data[grup]['level'][level]['runner']['from'],
                                data[grup]['level'][level]['runner']['to'],
                                0.01)
        down_on = calc.mk_random(down_on)
        go_down[grup] = [level, round(down_on + data[grup]['level'][level]['value'], 2), {}, {}]

        send_to_visual(evt='START_RUNER', grup=grup, level=level,
                       value=data[grup]['level'][level]['value'], mashin=ip, go_down=go_down[grup][1])
        if ip in go_down[grup][2]:
            go_down[grup][2][ip] = go_down[grup][2][ip] + bet
            go_down[grup][3][ip] = time.time()
        else:
            go_down[grup][2][ip] = bet
            go_down[grup][3][ip] = time.time()
        DB.set_key('go_down', go_down)
    #
    elif (down_stop[grup] == False and
          data[grup]['level'][level]['value'] >= data[grup]['level'][level]['down_value'] and
          go_down[grup][0] == level):

        in_runner = go_down[grup][3].copy()
        for item in in_runner:
            try:
                if go_down[grup][3][item] + 170 < time.time():
                    del go_down[grup][2][item]
                    del go_down[grup][3][item]
            except KeyError:
                pass
        #         print go_down[grup], data[grup]['level'][level]['value']
        if round(data[grup]['level'][level]['value'], 2) <= go_down[grup][1]:
            if ip in go_down[grup][2]:
                go_down[grup][2][ip] = go_down[grup][2][ip] + bet
                go_down[grup][3][ip] = time.time()
            else:
                go_down[grup][2][ip] = bet
                go_down[grup][3][ip] = time.time()
        DB.set_key('go_down', go_down)
        try:
            var = get_first_3(go_down[grup][2], count=data[grup]['level'][level]['runner_count'])
        except KeyError:
            var = get_first_3(go_down[grup][2])
            data[grup]['level'][level]['runner_count'] = 3
        # var = get_first_3(go_down[grup][2], count=get_first_3(go_down[grup][2], count=data[grup]['level'][level]['runner_count']))
        if data[grup]['level'][level]['value'] >= go_down[grup][1]:
            var3 = []
            all_bet = 0
            for i in go_down[grup][2]:
                all_bet = all_bet + go_down[grup][2][i]
            for i in var:
                try:
                    for b in range(int((float(var[i]) / all_bet) * 100)):  # @UnusedVariable
                        var3.append(i)
                except ZeroDivisionError:
                    pass
            down_on = False
            log = None
            down_sum = go_down[grup][1]
            if data[grup]['level'][level]['x2'] == True:
                if data[grup]['level'][level]['x2_time']['from'] <= date_now.hour and data[grup]['level'][level]['x2_time']['to'] > date_now.hour:
                    down_sum = down_sum * 2
            while len(var3) > 0:

                down_on = calc.mk_random(var3, mony=False)
                # for i in range(conf.DOWN_COUNT):
                if down_on != False:

                    log = log_write(level, grup, down_sum, down_on, 0)
                    if log == True:
                        data[grup]['level'][level]['value'] = data[grup]['level'][level]['start_value'] + \
                                                              data[grup]['level'][level]['hiden_value']
                        data[grup]['level'][level]['hiden_value'] = 0.0

                        down_to = data[grup]['level'][level]['down']['to'] - (
                                    data[grup]['level'][level]['down']['to'] * 0.01)

                        if data[grup]['level'][level]['hold_procent'] <= 1 and data[grup]['level'][level][
                            'hold_procent'] > 0:
                            down_from = (down_to - data[grup]['level'][level]['down']['from']) * data[grup][
                                'real_down_procent']
                            down_from = data[grup]['level'][level]['down']['from'] + down_from
                        elif data[grup]['real_down_procent'] <= 1 and data[grup]['real_down_procent'] > 0:
                            down_from = (down_to - data[grup]['level'][level]['down']['from']) * \
                                        data[grup]['level'][level]['hold_procent']
                            down_from = data[grup]['level'][level]['down']['from'] + down_from
                        else:
                            down_from = data[grup]['level'][level]['down']['from']
                        next_down = calc.mk_range(down_from, down_to, 0.01)
                        data[grup]['level'][level]['down_value'] = calc.mk_random(next_down)
                        data[grup]['level'][level]['last_down'] = time.time()
                        go_down[grup] = False
                        DB.set_key('go_down', go_down)
                        return data
                while True:
                    try:
                        del var3[var3.index(down_on)]
                    except ValueError:
                        down_on = False
                        break
        if data[grup]['hiden_visual'] == False:
            send_to_visual(evt='RUNER', grup=grup, level=level, value=data[grup]['level'][level]['value'],
                           mashin=ip, bet=var, go_down=go_down[grup][1])
    DB.close()
    return data


def rain(ip, bet, grup, level, db):
    pass
