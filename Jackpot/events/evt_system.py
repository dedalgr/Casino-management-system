#-*- coding:utf-8 -*-
'''
Created on 31.03.2017 г.

@author: dedal
'''
# from conf import * 
import os
import conf  # @UnresolvedImport
import db.db  # @UnresolvedImport
import udp.client  # @UnresolvedImport
DB = db.db.MemDB()
SEND = udp.client.send

def VISUAL_ONLY(**kwargs):
    os.system('disable')
    os.system('sudo mount -o remount rw /')
    cmd = "sudo sed -i 's/%s/%s/g' /etc/network/interfaces" % ('192.168.1.5', kwargs['new_ip'])
    os.system(cmd)
    os.system('reboot')

def WHO(**kwargs):
    who = DB.get_key('INIT')  
    DB.close()
    return who


def REBOOT_SMIB(**kwargs):
    smib = DB.get_key('smib')  
    for i in smib:
        SEND(i, 'reboot')  

def GET_ERROR_LOG(**kwargs):
    try:
        data = os.popen('journalctl --unit=colibri').read()
    except:
        data = u''
    return data

def DEL_ERROR_LOG(**kwargs):
    return True
    # cmd = 'sudo cat /dev/null > %s' % ('/var/log/syslog')
    # os.system(cmd)
    # return True


if __name__ == '__main__':
    pass
