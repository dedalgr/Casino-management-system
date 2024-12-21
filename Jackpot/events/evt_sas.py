#-*- coding:utf-8 -*-
import db.db  # @UnresolvedImport
import udp.client  # @UnresolvedImport
# DB = db.db.MemDB()
SEND = udp.client.send
import conf 

def SMIB_WHO(**kwargs):
    return SEND('who', ip=kwargs['new_ip'], port=conf.UDP_SMIB_PORT)  # @UndefinedVariable

def DISABLE_GAME(**kwargs):
    return SEND('disable_game_from_jackpot', ip=kwargs['new_ip'], port=conf.UDP_SMIB_PORT)  # @UndefinedVariable

def EBABLE_JP_MOD(**kwargs):
    return SEND('jackpot_start', ip=kwargs['new_ip'], port=conf.UDP_SMIB_PORT)  # @UndefinedVariable

def DISABLE_JP_MOD(**kwargs):
    return SEND('jackpot_stop', ip=kwargs['new_ip'], port=conf.UDP_SMIB_PORT)  # @UndefinedVariable
   
def CHANGE_PR(**kwargs):
    return SEND('set_jacpot_procent', ip=kwargs['new_ip'], pr=kwargs['pr'], port=conf.UDP_SMIB_PORT)  # @UndefinedVariable
    
def GET_MULTI_METER(**kwargs):
    data = SEND('sas.meter', ip=kwargs['new_ip'], port=conf.UDP_SMIB_PORT)  # @UndefinedVariable
    return data

def GET_SINGLE_METER(**kwargs):
    data = SEND('sas.meter', ip=kwargs['new_ip'], port=conf.UDP_SMIB_PORT)  # @UndefinedVariable
    return data[kwargs['command']]
