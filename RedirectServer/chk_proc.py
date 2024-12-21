'''
Created on 12.03.2019

@author: dedal
'''

from multiprocessing import Process
import models
import time
import random
import libs
import datetime
import json
import client
import conf
import libs.db.sql_db
import os
import shutil

class Chk(Process):
    def __init__(self, log):
        self.db = libs.db.sql_db.PostgreSQL(dbname=conf.DB_NAME, user=conf.DB_USER, host=conf.DB_IP, passwd=conf.DB_PASS, port=conf.DB_PORT)
        Process.__init__(self, name='CHK')
        self.log = log
        self.sleep_time = random.randint(36000, 86400)
        self.rsa = libs.rsa.RSAKey()
        self.rsa.load_key(conf.PUB)
        self.port = conf.PORT
        self.buffer = conf.BUFFER
        self.timeout = conf.TIMEOUT
        self.log.info('CHK START')
        self.db_backup = conf.DB_BACKUP_PART

    def ls_chk(self, data, signature):
        values = json.loads(data)
        # signature = data.signature
        if values['uuid'] != libs.uuid_maker.mk_soft_id():
            self.log.error('wrong activ uuid')
            return False
        # elif values['init_time']+2700 < time.time():
        #     print 'wrong activ init_time'
        #     return False
        elif datetime.datetime.strptime(values['end_time'], '%d.%m.%Y') < datetime.datetime.now() and values['end_time'] != '01.01.2009':
            self.log.error('wrong activ end_time')
            return False
        # elif values['work'] == False:
        #     print 'wrong activ work'
        #     return False
        elif self.rsa.verify(data, signature) == False:
            self.log.error('wrong activ sig')
            return False
        return True

    def stop(self, evt, data):
        # return True
        all_dev = self.db.get_all('select (ip) from mashin where sas=True and enable=True')
        for i in all_dev:
            # print i
            self.log.warning( '%s %s' % (evt, i[0]))
            client.send(evt, ip=i[0], port=self.port, timeout=0, log=self.log)
        return True

    def mising_mod(self, evt):
        # return True
        all_dev = self.db.get_all('select (ip) from mashin where sas=True and enable=True')
        for i in all_dev:
            self.log.warning( '%s %s' % (evt, i[0]))
            client.send(evt, ip=i[0], port=self.port, log=self.log, timeout=0)

    def backup(self):
        try:
            if conf.DEBUG == False:
                try:
                    os.system('mkdir %s' % (self.db_backup))
                except Exception as e:
                    self.log.error(e, exc_info=True)
                files = self.get_files(self.db_backup)
                for i in files:
                    os.system('rm %s' % (i))
                self.db._backup(self.db_backup, name='auto_backup')
        except Exception as e:
            self.log.error(e, exc_info=True)

    def get_files(self, directory):
        file_paths = []
        for root, directories, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        return file_paths

    def run(self):
        while True:
            try:
                time.sleep(self.sleep_time)
                self.db.connect()
                self.backup()
                all_ln = self.db.get_all('select * from lns')
                # print all_ln
                # self.db.add_object_to_session(all_ln[0])
                all_mod = []
                for i in all_ln:

                    data = self.ls_chk(i[2], i[3])
                    val = json.loads(i[2])
                    all_mod.append(val['name'])
                    if data == False:
                        if val['name'] == 'base':
                            self.stop('sas_stop', val)
                            self.stop('rfid_stop', val)
                        elif val['name'] == 'keysystem':
                            self.stop('keysystem_stop', val)
                        elif val['name'] == 'bonus_cart':
                            self.stop('bonus_stop', val)
                        elif val['name'] == 'client':
                            self.stop('client_cart_stop', val)
                        elif val['name'] == 'jackpot':
                            self.stop('jackpot_stop', val)
                        val['end_time'] = '01.01.2009'
                        val['init_time'] = 0
                        val=json.dumps(val)
                        cmd = "UPDATE lns SET value='%s' WHERE id=%s;" % (val, i[0])
                        self.db.set(cmd)
                        self.db.commit()
                if 'base' not in all_mod:
                    self.mising_mod('sas_stop')
                    self.mising_mod('rfid_stop')
                if 'keysystem' not in all_mod:
                    self.mising_mod('keysystem_stop')
                if 'bonus_cart' not in all_mod:
                    self.mising_mod('bonus_stop')
                if 'client' not in all_mod:
                    self.mising_mod('client_cart_stop')
                if 'jackpot' not in all_mod:
                    self.mising_mod('jackpot_stop')

                self.db.close()
                self.sleep_time = random.randint(36000, 86400)

            except Exception as e:
                self.sleep_time = random.randint(36000, 86400)
                self.log.critical( e, exc_info=True)
                self.db.close()

