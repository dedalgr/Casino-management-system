#-*- coding:utf-8 -*-
'''
Created on 16.05.2017 г.

@author: dedal
'''

LINUX_COMMAND = {}
IP = 'get_ip'
REBOOT = 'reboot'
WHO = 'who'

#===============================================================================
# # Date format = yyyy-mm-dd 
# # Time format = hh:mm
#===============================================================================
SET_DATE_TIME = 'SET_TIME'

#===============================================================================
# ip = 192.168.1.11 >> 11 или по-голямо
# gw = 192.168.1.1 >> Адреса на рутера
# db_id = 10 >> id на продаденото pc от база става мак адрес
#===============================================================================
GET_ERROR_LOG = 'GET_ERROR_LOG'
ALIFE = 'alive'


#===============================================================================
# SAS protocol
#===============================================================================

SAS_F_COEF = 'sas.coef'
SAS_F_EVENT = 'sas.get_event'
SAS_F_METER_SINGLE = 'sas.get_single_meter'
SAS_F_METER_MULTI = 'sas.get_multi_meter'

# delay_time=100 >> Приема време 100 мили секунди
SAS_F_DELAY_GAME = 'sas.delay_game'

SAS_F_VERSION = 'sas.sas_version'
SAS_F_TIME_GET = 'sas.get_date_time'

# date = 12.22.2017, time = 10:08
SAS_F_TIME_SET = 'sas.set_date_time'

# mony=100.20, tax='00' >> tax='01', tax='02'
SAS_F_LEGACY_BONUS = 'sas.set_legacy_bonus'
SAS_F_MULTI_CMD = 'sas.multi_cmd'
#===============================================================================
# SAS COMMAND
#===============================================================================
SAS_C_SINGLE_CURENT_CREDIT = 'curent credit'
SAS_C_SINGLE_OUT = 'out'
SAS_C_SINGLE_OUT_IN_CREDIT = 'out credit'
SAS_C_SINGLE_BILL = 'bill'
SAS_C_SINGLE_BET = 'bet'
SAS_C_SINGLE_WON = 'won'
SAS_C_SINGLE_IN = 'in'
SAS_C_SINGLE_IN_IN_CREDIT = 'in credit'
SAS_C_SINGLE_JP = 'jp'
SAS_C_SINGLE_GAME_PAYED = 'game won'
SAS_C_SINGLE_GAME_LOST = 'game lost'
SAS_C_SINGLE_GAME_WON = 'game won'
SAS_C_SINGLE_GAME_IN_MACHIN = 'game implement'
SAS_C_SINGLE_GAME_SELECTED = 'selected game'
SAS_C_SINGLE_DENOMINATION = 'denomination'
SAS_C_SINGLE_HALT = 'halt'
SAS_C_SINGLE_START = 'start'
SAS_C_SINGLE_BILL_STOP = 'halt bill'
SAS_C_SINGLE_BILL_START = 'start bill'

SAS_C_MULTI_19 = '19'
SAS_C_MULTI_0F = '0F'
SAS_C_MULTI_1C = '1C'
SAS_C_MULTI_19_IN_CREDIT = '19 credit'
SAS_C_MULTI_0F_IN_CREDIT = '0F credit'
SAS_C_MULTI_1C_IN_CREDIT = '1C credit'
SAS_C_MULTI_BILL = 'bill'

# Приемат номер на игра
# game_n = '0001'
SAS_C_MULTI_FOR_GAME = 'meter for game'
SAS_C_MULTI_GAME_CONF = 'game conf'

KS_CHANGE_KEY = 'keysystem_change'
KS_DEACTIV = 'keysystem_stop'
KS_ACTIVE = 'keysystem_start'
# KS_BLOCK = 'KS_USE_BLOCK'
KS_RELAY_PORT = 'KS_RELAY_PORT'

if __name__ == '__main__':
    pass