# -*- coding:utf-8 -*-
from .evt_user import *
# from evt_mashin import *
# from evt_visual import *
from .evt_sas import *
# from evt_jp_group import *
from .evt_security import *
# from conf import *
from .evt_games import *
from .evt_system import *
import calc  # @UnresolvedImport
import os
import subversion
from conf import *
import db.db  # @UnresolvedImport
import udp.client  # @UnresolvedImport
import datetime
import rtc  # @UnresolvedImport
import time
import datetime
import games

DB = db.db.MemDB()
SEND = udp.client.send
SEND_TO_VISUAL = udp.client.visual_send


def ee(func, *args, **kwargs):
    '''
    Създава емитер
    :param func:
    :param args:
    :param kwargs:
    :return: повиканата функция

    '''

    if not args and not kwargs:
        func = func + '()'
        return eval(func)

    elif args and not kwargs:

        func = func + '(%s)' % ('%s,' * len(args))
        func = func % (args)
        return eval(func)

    elif kwargs and not args:
        func = func + '(**%s)' % (kwargs)
        return eval(func)


def get_date_time(**kwargs):
    now = datetime.datetime.now()
    dates = '%s-%s-%s' % (now.year, now.month, now.day)
    times = '%s:%s:%s' % (now.hour, now.minute, now.second)
    return {'dates': dates, 'times': times}


def STOP_ROTATION(**option):
    a = option['command']
    t = time.time() + conf.UDP_TIMEOUT
    if a:
        while True:
            if DB.check_for_lock() != 'STOP_ROTATION':
                DB.set_lock(model='STOP_ROTATION')
                time.sleep(0.02)
            else:
                break
            if time.time() >= t:
                return False
    else:
        DB.delete_lock()
    # DB.set_key('stop_rotation', a)
    return True

def CHK_STOP_ROTATION_STATUS(**kwargs):
    return DB.check_for_lock()

def reboot(**kwargs):
    reboot = DB.get_key('REBOOT')
    reboot = True
    DB.set_key('REBOOT', reboot)
    time.sleep(10)
    os.system('sudo reboot')
    return True


def ALIFE(**kwargs):
    return True

def ALIFE_VISUAL(**kwargs):
    try:
        visual = DB.get_key('visual')[kwargs['my_name']]
    except KeyError:
        return True
    grup = DB.get_key('group')
    if visual['group'] in grup:
        return True
    else:
        return False

def CHANGE_CONF(**option):
    section = option['section']
    del option['section']
    conf_file.update_option(section, **option)
    reboot()


def svn_update(**kwargs):
    if 'url' not in kwargs:
        url = 'svn://NEW_SVN_IP/home/dedal/svn/Jackpot_BIN/%s/' % (VERSION)
    else:
        url = kwargs['url']

    if 'my_dir' not in kwargs:
        my_dir = os.getcwd()
    else:
        my_dir = kwargs['my_dir']
    if 'user' in kwargs:
        user = kwargs['user']
    else:
        user = 'smib'
    if 'passwd' in kwargs:
        passwd = kwargs['passwd']
    else:
        passwd = 'smib_update'
    connect = subversion.SubVersion(folder=my_dir, user=user, passwd=passwd, url=url)
    connect.checkout()
    return connect.update()


def SET_DATE_TIME(**kwargs):
    '''
    Сверява датата и часовника на системата.
    :param date: Дата във формат: yyyy-mm-dd
    :param time: Час във формат: hh:mm
    :return: True
    '''
    cmd = 'sudo date --set %s' % (kwargs['dates'])
    os.system(cmd)
    cmd = 'sudo date --set %s' % (kwargs['times'])
    os.system(cmd)
    try:
        rtc.Write_RTC()
    except:
        pass
    return True


def GET_DATE_TIME(**kwargs):
    var = datetime.datetime.now()
    dates = '%s-%s-%s' % (var.year, var.month, var.day)
    times = '%s:%s:%s' % (var.hour, var.minute, var.second)
    var = {'dates': dates, 'times': times}
    return var


def GET_DB_KEYS(**kwargs):
    a = DB.keys()
    try:
        del a[a.index('log')]
    except ValueError:
        pass
    DB.close()
    return a


def GET_DB_KEY(**kwargs):
    data = DB.get_key(kwargs['key'])
    DB.close()
    return data


def SET_DB_KEY(**kwargs):
    t = time.time() + int(conf.UDP_TIMEOUT)
    while True:
        if DB.check_for_lock() != b'SET_DB_KEY':
            DB.set_lock(int(conf.UDP_TIMEOUT), 'SET_DB_KEY')
        else:
            break
        if time.time() >= t:
            if DB.check_for_lock() == 'SET_DB_KEY':
                DB.delete_lock()
            return False
        time.sleep(0.02)
    casino_name = DB.get_key('casino_name')

    if kwargs['key'] == 'group':


        real_db = DB.get_key('group')

        for i in kwargs['data']:
            if i not in real_db:
                real_db[i] = kwargs['data'][i]
            for b in kwargs['data'][i]['level']:
                if kwargs['data'][i]['game_type'] == 0:
                    if 'value' not in kwargs['data'][i]['level'][b]:
                        kwargs['data'][i]['level'][b]['value'] = kwargs['data'][i]['level'][b]['start_value']
                        kwargs['data'][i]['level'][b]['hiden_value'] = 0.0
                    else:
                        if 'val_edit' not in kwargs['data'][i]['level'][b]:
                            kwargs['data'][i]['level'][b]['value'] = real_db[i]['level'][b]['value']
                        elif kwargs['data'][i]['level'][b]['val_edit'] == False:
                            kwargs['data'][i]['level'][b]['value'] = real_db[i]['level'][b]['value']
                        else:
                            del kwargs['data'][i]['level'][b]['val_edit']
                            if real_db[i]['level'][b]['value'] > real_db[i]['level'][b]['down_value']:
                                del_go_down = DB.get_key('go_down')
                                del_go_down[i] = False
                                DB.set_key('go_down', del_go_down)
                elif kwargs['data'][i]['game_type'] == 1:
                    if b in real_db[i]['level']:
                        kwargs['data'][i]['level'][b]['last_down'] = real_db[i]['level'][b]['last_down']
                    if 'value' not in kwargs['data'][i]['level'][b]:
                        kwargs['data'][i]['level'][b]['value'] = kwargs['data'][i]['level'][b]['start_value']
                        kwargs['data'][i]['level'][b]['hiden_value'] = 0.0
                    else:
                        kwargs['data'][i]['level'][b]['value'] = real_db[i]['level'][b]['value']

                if 'down_value' not in kwargs['data'][i]['level'][b]:
                    if kwargs['data'][i]['game_type'] == 0:
                        down_to = kwargs['data'][i]['level'][b]['down']['to'] - (
                                    kwargs['data'][i]['level'][b]['down']['to'] * 0.01)
                        try:
                            if kwargs['data'][i]['real_down_procent'] <= 1 and kwargs['data'][i][
                                'real_down_procent'] > 0:
                                down_from = (down_to - kwargs['data'][i]['level'][b]['down']['from']) * \
                                            kwargs['data'][i]['real_down_procent']
                                down_from = kwargs['data'][i]['level'][b]['down']['from'] + down_from
                            elif kwargs['data'][i]['level'][b]['hold_procent'] <= 1 and kwargs['data'][i]['level'][b][
                                'hold_procent'] > 0:
                                down_from = (down_to - kwargs['data'][i]['level'][b]['down']['from']) * \
                                            kwargs['data'][i]['level'][b]['hold_procent']
                                down_from = kwargs['data'][i]['level'][b]['down']['from'] + down_from
                            else:
                                down_from = kwargs['data'][i]['level'][b]['down']['from']
                        except KeyError:
                            kwargs['data'][i]['level'][b]['hold_procent'] = 0
                            # kwargs['data'][i]['level'][b]['hold_procent'] = 0
                            try:
                                if kwargs['data'][i]['real_down_procent'] <= 1 and kwargs['data'][i][
                                    'real_down_procent'] > 0:
                                    down_from = (down_to - kwargs['data'][i]['level'][b]['down']['from']) * \
                                                kwargs['data'][i]['real_down_procent']
                                    down_from = kwargs['data'][i]['level'][b]['down']['from'] + down_from
                                else:
                                    down_from = kwargs['data'][i]['level'][b]['down']['from']
                            except KeyError:
                                down_from = kwargs['data'][i]['level'][b]['down']['from']
                                kwargs['data'][i]['real_down_procent'] = 0

                        array = calc.mk_range(down_from,
                                              kwargs['data'][i]['level'][b]['down']['to'] -
                                              (kwargs['data'][i]['level'][b]['down']['to'] * 0.01),
                                              0.01)

                    elif kwargs['data'][i]['game_type'] == 1:

                        try:
                            if kwargs['data'][i]['real_down_procent'] <= 1 and kwargs['data'][i][
                                'real_down_procent'] > 0:
                                array = calc.mk_time_range(
                                    kwargs['data'][i]['level'][b]['down']['from'] + kwargs['data'][i][
                                        'real_down_procent'],
                                    kwargs['data'][i]['level'][b]['down']['to'],
                                    0.01)
                            else:
                                array = calc.mk_time_range(kwargs['data'][i]['level'][b]['down']['from'],
                                                           kwargs['data'][i]['level'][b]['down']['to'],
                                                           0.01)
                        except KeyError:
                            kwargs['data'][i]['real_down_procent'] = 0
                            array = calc.mk_time_range(kwargs['data'][i]['level'][b]['down']['from'],
                                                       kwargs['data'][i]['level'][b]['down']['to'],
                                                       0.01)

                    kwargs['data'][i]['level'][b]['down_value'] = calc.mk_random(array)
                else:
                    if real_db[i]['level'][b]['value'] > kwargs['data'][i]['level'][b]['down_value']:
                        kwargs['data'][i]['level'][b]['down_value'] = real_db[i]['level'][b]['down_value']

    elif kwargs['key'] == 'go_down':
        go_down = DB.get_key('go_down')
        kwargs['data'] = go_down
    elif kwargs['key'] == 'down_stop':
        down_stop = DB.get_key('down_stop')
        kwargs['data'] = down_stop
    elif kwargs['key'] == 'END':
        visual = DB.get_key('visual')
        for item in visual:
            for i in range(3):
                SEND_TO_VISUAL(ip=item, evt='SET_DB', port=conf.UDP_VISUAL_PORT, timeout=conf.UDP_VISUAL_TIMEOUT)

        if casino_name['ip']:
            DB.mem_cach2.set('DOWN', {'evt': 'SET_DB', 'time': time.time()})
        else:
            DB.mem_cach.set('DOWN', {'evt': 'SET_DB', 'time': time.time()})
        DB.delete_lock()
        return True
    # if kwargs['key'] != 'END':
    DB.set_key(kwargs['key'], kwargs['data'])
    DB.close()
    DB.delete_lock()
    # if stop_rotation == True:
    #     STOP_ROTATION(command=False)
    return True


# def GET_LOG_GRUP(**kwargs):
#     log = db.db.SQLite(name='log.db')
#     log_keys = log.get_key('log').keys()
#     log.close()
#     return log_keys


def GET_LOG(**kwargs):
    #     grup = kwargs['grup']
    from_date = kwargs['from_date']
    to_date = kwargs['to_date']
    log = db.db.SQLite(name='log.db')
    log_db = log.keys()
    #     log = log_db[grup]
    data = {}
    for i in log_db:
        if i >= from_date and i <= to_date:
            data[i] = log.get_key(i)
        # for b in log_db[i]:
        #     if b >= from_date and b <= to_date:
        #         if i not in data:
        #             data[i] = {}
        #         data[i][b] = log_db[i][b]
    log.close()
    return data


def GET_DB(**kwargs):
    # while True:
    #     if not DB.check_for_lock():
    #         break
    # DB.set_lock()
    keys = DB.keys()
    var = {}
    for i in keys:
        if i == 'log':
            pass
        else:
            var[i] = DB.get_key(i)
    DB.close()
    # DB.delete_lock()
    return var


def VISUAL_AUDIO_TEST(**kwargs):
    data = SEND_TO_VISUAL('AUDIO_TEST', ip=kwargs['visual_ip'], port=UDP_VISUAL_PORT)
    return data

def KILL_VISUAL(**kwargs):
    data = SEND_TO_VISUAL('KILL', ip=kwargs['visual_ip'], port=UDP_VISUAL_PORT, timeout=5)
    return True

def REBOOT_VISUAL(**kwargs):
    data = SEND_TO_VISUAL('REBOOT_VISUAL', ip=kwargs['visual_ip'], port=UDP_VISUAL_PORT, timeout=5)
    return True

def VISUAL_ALIFE(**kwargs):
    data = SEND_TO_VISUAL('set_ip', ip=kwargs['visual_ip'], visual_ip=kwargs['visual_ip'], port=UDP_VISUAL_PORT)
    return data

def VISUAL_GET_CONF(**kwargs):
    data = SEND_TO_VISUAL('get_conf', ip=kwargs['visual_ip'], port=UDP_VISUAL_PORT)
    return data

def VISUAL_SET_CONF(**kwargs):
    data = SEND_TO_VISUAL('set_conf', ip=kwargs['visual_ip'], port=UDP_VISUAL_PORT, **kwargs)
    return data

def VISUAL_UPDATE(**kwargs):
    data = SEND_TO_VISUAL('svn_update', ip=kwargs['visual_ip'], port=UDP_VISUAL_PORT)
    return data

def SET_DB(**kwargs):
    t = time.time() + conf.UDP_TIMEOUT
    while True:
        if DB.check_for_lock() != 'SET_DB':
            DB.set_lock(model='SET_DB')
            time.sleep(0.02)
        else:
            break
        if time.time() >= t:
            return False
    for i in kwargs['db']:
        DB.set_key(i, kwargs['db'][i])
    DB.close()
    DB.delete_lock()
    return True

def GET_WORK(**kwargs):
    data = DB.get_key('work')
    DB.close()
    return data

def chk_alife(**kwargs):
    return True

GLOBAL_EVENT = {
    'get_date_time': get_date_time,
    'STOP_ROTATION':STOP_ROTATION,
    'reboot':reboot,
    'chk_alife':chk_alife,
    'ALIFE':ALIFE,
    'CHANGE_CONF':CHANGE_CONF,
    'svn_update':svn_update,
    'SET_DATE_TIME':SET_DATE_TIME,
    'GET_DATE_TIME':GET_DATE_TIME,
    'GET_DB_KEYS':GET_DB_KEYS,
    'GET_DB_KEY':GET_DB_KEY,
    # 'GET_LOG_GRUP':GET_LOG_GRUP,
    'GET_LOG':GET_LOG,
    'GET_DB':GET_DB,
    'VISUAL_AUDIO_TEST':VISUAL_AUDIO_TEST,
    'REBOOT_VISUAL':REBOOT_VISUAL,
    'VISUAL_ALIFE':VISUAL_ALIFE,
    'SET_DB':SET_DB,
    'GET_WORK':GET_WORK,
    'add_bet':add_bet,
    'GET_BET':GET_BET,
    'DOWN_STOP':DOWN_STOP,
    'DOWN_ON':DOWN_ON,
    'run_linux_cmd':run_linux_cmd,
    'CHANGE_INIT_DATA':CHANGE_INIT_DATA,
    'BASE_KEY':BASE_KEY,
    'ACTIV':ACTIV,
    'GET_REAL_CRC':GET_REAL_CRC,
    'GET_CRC':GET_CRC,
    'CHK_CRC':CHK_CRC,
    'SET_NAME':SET_NAME,
    'SMIB_WHO':SMIB_WHO,
    'DISABLE_GAME':DISABLE_GAME,
    'EBABLE_JP_MOD':EBABLE_JP_MOD,
    'DISABLE_JP_MOD':DISABLE_JP_MOD,
    'CHANGE_PR':CHANGE_PR,
    'GET_MULTI_METER':GET_MULTI_METER,
    'GET_SINGLE_METER':GET_SINGLE_METER,
    'VISUAL_ONLY':VISUAL_ONLY,
    'WHO':WHO,
    'REBOOT_SMIB':REBOOT_SMIB,
    'GET_ERROR_LOG':GET_ERROR_LOG,
    'DEL_ERROR_LOG':DEL_ERROR_LOG,
    'LOGIN':LOGIN,
    'ADD_USER':ADD_USER,
    'DEL_USER':DEL_USER,
    'ALL_USER':ALL_USER,
    'ALIFE_VISUAL':ALIFE_VISUAL,
    'VISUAL_GET_CONF':VISUAL_GET_CONF,
    'VISUAL_SET_CONF':VISUAL_SET_CONF,
    'VISUAL_UPDATE':VISUAL_UPDATE,
}