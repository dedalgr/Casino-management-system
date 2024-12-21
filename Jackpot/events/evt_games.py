# -*- coding:utf-8 -*-
'''
Created on 27.03.2017 г.

@author: dedal
'''

# import games  # @UnresolvedImport
import calc  # @UnresolvedImport
import games  # @UnresolvedImport
import db.db  # @UnresolvedImport
import conf  # @UnresolvedImport
import datetime
import time
import pytz
import exception
DB = db.db.MemDB()


def add_bet(**kwargs):
    t = time.time() + conf.UDP_TIMEOUT
    while True:
        if not DB.check_for_lock():
            DB.set_lock(conf.UDP_TIMEOUT, t)
            break
        if time.time() >= t:
            return False
    # if DB.get_key('stop_rotation'):
    #     return True
    data = DB.get_key('group')
    group = DB.get_key('group')
    try:
        db = DB.get_key('smib')[kwargs['smib_ip']]
    except KeyError:
        DB.delete_lock()
        return False
    revert = True
    go_down = DB.get_key('go_down')
    for i in group:
        if i in db['group']:
            for b in data[i]['level']:
                revert = True
                if 'player' in data[i]['level'][b]:
                    if data[i]['level'][b]['player'] == True:
                        if 'player' in kwargs:
                            if kwargs['player'] == False or kwargs['player'] == None:
                                revert = False

                if data[i]['game_type'] == 0 and data[i]['level'][b]['bet'] == False and revert == True:

                    data = games.clasic_level(ip=kwargs['smib_ip'], bet=kwargs['bet'],
                                              grup=i, level=b, db=data)
                elif data[i]['game_type'] == 1 and revert == True:
                    if 'day_down' in data[i]['level'][b]:
                        data = games.time_level(ip=kwargs['smib_ip'], bet=kwargs['bet'], grup=i, level=b, db=data)
                elif data[i]['game_type'] == 0 and data[i]['level'][b]['bet'] == True and revert == True:
                    data = games.runer(ip=kwargs['smib_ip'], bet=kwargs['bet'], grup=i, level=b, db=data)
            level = {}
            for item in data[i]['level']:
                level[item] = data[i]['level'][item]['value']
            try:
                go_down[i]
            except KeyError:
                if data[i]['hiden_visual'] == False:
                    games.send_to_visual('ADD_BET', grup=i, level=level, value=None, mashin=kwargs['smib_ip'])
            else:
                if go_down[i] == False and data[i]['hiden_visual'] == False:
                    games.send_to_visual('ADD_BET', grup=i, level=level, value=None, mashin=kwargs['smib_ip'])
                elif type(go_down[i]) == dict and data[i]['hiden_visual'] == False:
                    games.send_to_visual('ADD_BET', grup=i, level=level, value=None, mashin=kwargs['smib_ip'])
    if DB.check_for_lock() == b'DOWN_ON':
        pass
    elif DB.check_for_lock() != t:
        return False
    DB.set_key('group', data)
    # if lock is True:
    # if casino_name['ip']:
    #     DB.mem_cach2.delete('lock')
    # else:
    DB.delete_lock()
    # raise KeyError, DB.mem_cach.get('lock')
    return True


def DOWN_STOP(**kwargs):
    #     DB.set_key('down_stop', activ)
    down_stop = DB.get_key('down_stop')
    down_stop[kwargs['grup']] = False
    DB.set_key('down_stop', down_stop)
    DB.close()
    return True


def GET_BET(**kwargs):
    data = DB.get_key('group')
    DB.close()
    return data[kwargs['grup']]['level']


def DOWN_ON(**kwargs):
    t = time.time() + 5
    while True:
        if DB.check_for_lock() != b'DOWN_ON':
            DB.set_lock(model='DOWN_ON')
        else:
            break
        if time.time() >= t:
            DB.delete_lock()
            return False
    go_down = DB.get_key('go_down')
    down_stop = DB.get_key('down_stop')
    data = DB.get_key('group')
    my_time = time.time()
    if down_stop[kwargs['grup']] != False and down_stop[kwargs['grup']] + (conf.JP_BLOCK_TIME * 60) > my_time:
        DB.delete_lock()
        return False
    if go_down[kwargs['grup']] != False:
        DB.delete_lock()
        return False
    if data[kwargs['grup']]['level'][kwargs['level']]['value'] < data[kwargs['grup']]['level'][kwargs['level']]['down'][
        'from']:
        DB.delete_lock()
        return False
    # if data[kwargs['grup']]['global_mistery'] == True:
    # lock = True
    # if casino_name['ip']:
    # DB.mem_cach2.set('lock', True, expire=int(conf.UDP_TIMEOUT)+4)
    # else:
    # while True:
    #     if not DB.mem_cach.get('lock'):
    # DB.set_lock(model=2)
    #
    date_now = datetime.datetime.now()
    # date_now = date_now.replace(tzinfo=pytz.UTC)
    # date_now = date_now.astimezone(pytz.timezone(conf.RTC_TIME_ZONE))
    down_sum = round(data[kwargs['grup']]['level'][kwargs['level']]['value'], 2)
    if data[kwargs['grup']]['level'][kwargs['level']]['x2'] == True:
        if data[kwargs['grup']]['level'][kwargs['level']]['x2_time']['from'] <= date_now.hour and \
                data[kwargs['grup']]['level'][kwargs['level']]['x2_time']['to'] > date_now.hour:
            down_sum = round(down_sum * 2, 2)
    response = games.log_write(level=kwargs['level'],
                               grup=kwargs['grup'],
                               down_sum=down_sum,
                               down_on=kwargs['smib'],
                               min_bet=data[kwargs['grup']]['level'][kwargs['level']]['min bet'], chk=False)
    if response == True or response is None:
        data[kwargs['grup']]['level'][kwargs['level']]['value'] = data[kwargs['grup']]['level'][kwargs['level']][
                                                                      'start_value'] + \
                                                                  data[kwargs['grup']]['level'][kwargs['level']][
                                                                      'hiden_value']
        data[kwargs['grup']]['level'][kwargs['level']]['hiden_value'] = 0

        next_down = calc.mk_range(data[kwargs['grup']]['level'][kwargs['level']]['down']['from'],
                                  data[kwargs['grup']]['level'][kwargs['level']]['down']['to'] -
                                  (data[kwargs['grup']]['level'][kwargs['level']]['down']['to'] * 0.01),
                                  0.01)
        data[kwargs['grup']]['level'][kwargs['level']]['down_value'] = calc.mk_random(next_down)
        data[kwargs['grup']]['level'][kwargs['level']]['last_down'] = time.time()

        go_down = DB.get_key('go_down')
        try:
            go_down[kwargs['grup']] = False
            DB.set_key('go_down', go_down)
        except Exception as e:
            print(e)
        try:
            DB.set_key('group', data)
        except Exception as e:
            print(e)
            # DB.set_key('stop_rotation', True)
            # DB.set_lock()
            # if casino_name['ip']:
            #     while True:
            #         if not DB.mem_cach2.get('lock'):
            #             break
            #     DB.mem_cach2.set('lock', True)
            # else:
            #     while True:
            #         if not DB.mem_cach.get('lock'):
            #             break
            #     DB.mem_cach.set('lock', True)
            return False
        DB.close()
        # DB.set_key('stop_rotation', False)
        # if lock == True:
        # if casino_name['ip']:
        #     DB.mem_cach2.delete('lock')
        # else:

        if response is True:
            DB.delete_lock()
            return True
        else:
            DB.set_lock(model='DOWN_ON')
            return 'CHECK'
            # DB.set_lock()
    DB.delete_lock()
    return False
