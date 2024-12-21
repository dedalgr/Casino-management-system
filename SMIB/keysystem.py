#-*- coding:utf-8 -*-
'''
Created on 21.02.2019

@author: dedal
'''
from multiprocessing import Process
import log
import time
import os

class KeySystem(Process):
    def __init__(self, **kwargs):
        Process.__init__(self, name='KeySystem')
        # self.daemon = True
        self.db = kwargs['db']
        self.conf = kwargs['conf']
        self.pipe = kwargs['pipe']
        self.log = log.get_log(log.LOG_CHANEL_LEVEL['keysystem'])
        
        self.multikey = self.conf.get('KEYSYSTEM', 'multi_key', 'bool')
        self.timeout = self.conf.get('KEYSYSTEM', 'relay_timeout', 'float')
        self.credit_relay = self.conf.get('KEYSYSTEM', 'credit', 'int')
        self.report_relay = self.conf.get('KEYSYSTEM', 'report', 'int')
        
        # if self.timeout < 0.6:
        #     self.timeout = 0.6
        self.aft = self.conf.get('KEYSYSTEM', 'aft', 'bool')
        self.get_all_keys()
        self.credit_open = self.credit_status()
        self.report_open = self.report_status()
        
        if self.credit_open is True:
            self.close_credit()
        if self.report_open is True:
            self.close_report()
    
    def old_poll_clean(self):
        for i in self.pipe:
            if self.pipe[i].poll():
                self.pipe[i].recv()
                
    def get_all_keys(self):
        if self.multikey is False:
            self.all_keys = self.db.get('KEYSYSTEM')
        else:
            self.all_keys = self.db.get('MULTI_KEYSYSTEM')
        self.log.debug('all keys: %s', self.all_keys)
        return self.all_keys
    
    def open_credit(self):
        cmd = 'sudo modio2tool -B 1 -s %s' % (self.credit_relay)
        self.log.debug('open relay credit: %s', self.credit_relay)
        tmp = os.popen(cmd).read()
        if 'error' in tmp:
            self.log.error('bad relay option %s', cmd)
            if self.relay_status() is False:
                self.log.error('no relay connected')
            return False
        return True
    
    def close_credit(self):
        cmd = 'sudo modio2tool -B 1 -c %s' % (self.credit_relay)
        self.log.debug('close relay credit: %s', self.credit_relay)
        tmp = os.popen(cmd).read()
        if 'error' in tmp:
            self.log.error('bad relay option %s', cmd)
            if self.relay_status() is False:
                self.log.error('no relay connected')
            return False
        return True
    
    def credit_status(self):
        cmd = 'sudo modio2tool -B 1 -r %s' % (self.credit_relay)
        tmp = os.popen(cmd).read()
        # self.log.error('%s', tmp)
        if tmp == 'Relays: 0x02\n':
            return True
        if self.relay_status() is False:
            self.log.error('no relay connected')
        return False
    
    def open_report(self):
        cmd = 'sudo modio2tool -B 1 -s %s' % (self.report_relay)
        self.log.debug('open relay report: %s', self.report_relay)
        tmp = os.popen(cmd).read()
        if 'error' in tmp:
            self.log.error('bad relay option %s', cmd)
            if self.relay_status() is False:
                self.log.error('no relay connected')
            return False
        return True
    
    def close_report(self):
        cmd = 'sudo modio2tool -B 1 -c %s' % (self.report_relay)
        self.log.debug('close relay report: %s', self.report_relay)
        tmp = os.popen(cmd).read()
        if 'error' in tmp:
            self.log.error('bad relay option %s', cmd)
            if self.relay_status() is False:
                self.log.error('no relay connected')
            return False
        return True
    
    def report_status(self):
        cmd = 'sudo modio2tool -B 1 -r %s' % (self.report_relay)
        tmp = os.popen(cmd).read()
        if tmp == 'Relays: 0x02\n':
            return True
        if self.relay_status() is False:
            self.log.error('no relay connected')
        return False
    
    def relay_status(self):
        cmd = 'sudo modio2tool -B 1 -H'
        tmp = os.popen(cmd).read()
        if 'ID: 0x0\n' == tmp:
            return False
        return True
    
    def relay_test(self):
        self.open_credit()
        self.close_credit()
        self.open_report()
        self.close_report()
        return True
    
    def run(self):
        while 1:
            try:
                data = self.pipe['rfid'].recv()
                self.log.debug('read from rfid: %s', data)
                if data == 1:
                    self.credit_open = self.open_credit()
                elif data == 2:
                    self.report_open = self.open_report()
                while self.pipe['rfid'].poll(self.timeout):
                    self.pipe['rfid'].recv()
                # else:
                #     self.pipe['rfid'].send(True)
                if self.credit_open is True:
                    self.close_credit()
                if self.report_open is True:
                    self.close_report()
                self.report_open = False
                self.credit_open = False
            except Exception as e:
                self.credit_open = False
                self.report_open = False
                self.log.critical(e, exc_info=True)
                time.sleep(0.5)
                try:
                    self.close_credit()
                    self.close_report()
                except Exception as e:
                    self.log.critical(e, exc_info=True)
