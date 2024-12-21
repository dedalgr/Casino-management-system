#-*- coding:utf-8 -*-
'''
Created on 04.01.2020

@author: dedal
'''

import os
import multiprocessing
import time
import conf
import logging.handlers

def ssh_port():
    cmd = 'sudo grep Port /etc/ssh/sshd_config'
    data = os.popen(cmd).read()
    data = data.replace('Port ', '')
    try:
        data = int(data)
    except ValueError:
        try:
            cmd = 'sudo grep "\<Port\>" /etc/ssh/sshd_config'
            data = os.popen(cmd).read()[:-1]
            data = data.replace('Port ', '')
            data = int(data)
        except ValueError:
            return  None
    return data

my_ssh_port = ssh_port()

IP_TABLESS = [
    'sudo iptables -F',
    'sudo iptables -A INPUT -p icmp -j ACCEPT', # Позволява пинг използва се за проверка от SMIB
    'sudo iptables -A INPUT -s 127.0.0.0/24 --j ACCEPT', # Отваря всички локални портове
    'sudo iptables -I INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT', # Позволява използването на интерне
    'sudo iptables -A INPUT -p tcp --dport %s -j ACCEPT'  % (my_ssh_port), # Позволява връзка към SSH, Иска ключ
    'sudo iptables -A INPUT -s NEW_SVN_IP -j ACCEPT', # Отваря всички портове за мен
    'sudo iptables -A INPUT -p tcp -s 192.168.1.0/24  --dport 631 -j ACCEPT',
    'sudo iptables -A INPUT -p tcp -s 192.168.1.0/24  --dport 53 -j ACCEPT',
    'sudo iptables -A INPUT -p tcp -s 192.168.1.0/24  --dport 5353 -j ACCEPT',
    # 'sudo iptables -A INPUT -s 192.168.1.0/24 -j ACCEPT', # Отваря всичло за локална мрежа
    'sudo iptables -A INPUT -p udp --dport %s -j ACCEPT' % (conf.PORT), # Отваря всичло за 30593
    'sudo iptables -A INPUT -p tcp --dport %s -j ACCEPT' % (conf.PORT), # Отваря всичло за 30593
    'sudo iptables -A INPUT -p udp --dport %s -j ACCEPT' % (conf.PORT_2), # Отваря всичло за 40593
    'sudo iptables -A INPUT -p udp --dport %s -j ACCEPT' % (logging.handlers.DEFAULT_TCP_LOGGING_PORT + 1), # Отваря всичло за 40593
    'sudo iptables -A INPUT -p udp --dport %s -j ACCEPT' % (logging.handlers.DEFAULT_TCP_LOGGING_PORT),
    'sudo iptables -A INPUT -p tcp --dport %s -j ACCEPT' % (logging.handlers.DEFAULT_TCP_LOGGING_PORT + 1), # Отваря всичло за 40593
    'sudo iptables -A INPUT -p tcp --dport %s -j ACCEPT' % (logging.handlers.DEFAULT_TCP_LOGGING_PORT),
    'sudo iptables -A INPUT -i lo -p all -j ACCEPT',
    'sudo iptables -A INPUT -j DROP'
]

class BanProc(multiprocessing.Process):
    def __init__(self, log):
        self.log = log
        self.ban = {}
        self.file_name = conf.BAN_DB_LOG
        self.originalTime = os.path.getmtime(self.file_name)
        self.check_time = conf.BAN_CHK
        self.cmd = 'sudo iptables -A INPUT -s %s -j DROP'
        self.max_wrong_login = conf.BAN_MAX_DB_WRONG_LOGIN
        self.my_file = open(self.file_name).readlines()
        multiprocessing.Process.__init__(self, name='BAN_SYSTEM')
        self.log.info('BAN RUN')

    def brute_force_ban(self):
        if (os.path.getmtime(self.file_name) > self.originalTime):
            if (os.path.getmtime(self.file_name) > self.originalTime):
                with open(self.file_name, 'r') as f:
                    a = f.readlines()
                    for i in a:
                        if i not in self.my_file:
                            self.my_file.append(i)
                            b = i.split()
                            if b[5] == 'FATAL:' and b[6] == 'no' and b[7] == 'pg_hba.conf':
                                ip = b[11]
                                ip = ip.replace('"', '')
                                ip = ip.replace(',', '')
                                if ip not in self.ban:
                                    self.log.warning('add ip to ban %s', ip)
                                    self.ban[ip] = 0
                                else:
                                    if self.ban[ip] != self.max_wrong_login and self.ban[ip] < self.max_wrong_login + 1:
                                        self.ban[ip] += 1
                                        self.log.warning('ip in ban loop %s max loop %s' % (ip, self.max_wrong_login))
                                        # print self.ban[ip]
                self.originalTime = os.path.getmtime(self.file_name)
        for i in list(self.ban.keys()):
            if self.ban[i] == self.max_wrong_login:
                self.log.info(self.cmd % (i))
                self.ban[i] += 1
                os.system(self.cmd % (i))


    def ban_ssh(self):
        pass

    def run(self):
        while True:
            try:
                self.brute_force_ban()
                self.ban_ssh()
                time.sleep(self.check_time)
            except Exception as e:
                self.log.critical(e, exc_info=True)
