# -*- coding:utf-8 -*-
# from security.crypts import *
# from security._keys import db_key
# from conf import *
import datetime  # @UnusedImport
import bsddb3
import json
import socket
# from pymemcache.client.base import Client as mem_Client
import traceback
from pymemcache.client.base import PooledClient as mem_Client
import time
import conf  # @UnresolvedImport
import cr  # @UnresolvedImport
import pickle
from . import sql_db
# from sshtunnel import SSHTunnelForwarder
import sshtunnel
import threading
import logging
import multiprocessing

class Tunel(multiprocessing.Process):
    def __init__(self, server="192.168.1.11", port=55555, log=None, level=logging.WARNING):
        self.ip = server
        self.port = port
        multiprocessing.Process.__init__(self)
        sshtunnel.TUNNEL_TIMEOUT = conf.MEM_TIMEOUT
        self._abort = 0
        paramiko = logging.getLogger("paramiko")
        paramiko.setLevel(level)
        if log != None:
            paramiko.addHandler(log)
        self.server = None


    def close(self):
        try:
            self.server.stop()
        except:
            pass
        try:
            self.server.close()
        except:
            pass


    def restart(self):
        self.server.restart()

    def start_new(self):
        self.server = sshtunnel.SSHTunnelForwarder((self.ip, self.port),
                                                   ssh_username="colibri",
                                                   ssh_pkey='/home/colibri/.ssh/id_rsa',
                                                   remote_bind_address=('127.0.0.1', 11211),
                                                   local_bind_address=('127.0.0.1', 11222),
                                                   compression=False,
                                                   ssh_private_key_password='Vavilon10',
                                                   threaded=True
                                                   )
        self.server.start()

    def isAlive(self):
        return self.server.is_alive

    def abort(self):

        # self.server.stop()
        self._abort = 1
        # count = 0
        # while self.server.tunnel_is_up != {}:
        #     count += 1
        #     time.sleep(1)
        #     if count >= 3:
        #         break

    def run(self):
        error = 0
        while True:

            try:
                if not self.server:
                    self.start_new()
                time.sleep(10)
                if self._abort:
                    if self.isAlive():
                        self.close()
                        break
                else:
                    if self.isAlive():
                        self.mem_cach2 = mem_Client(('127.0.0.1', 11222), serializer=json_serializer,
                                                    deserializer=json_deserializer, connect_timeout=conf.MEM_TIMEOUT,
                                                    timeout=conf.MEM_TIMEOUT)
                        self.mem_cach2.get('casino_name')
                        error = 0
            except Exception as e:
                error += 1
                if error >= 6:
                    try:
                        self.close()
                        self.start_new()
                    except:
                        pass
                    else:
                        error = 0
                    traceback.print_exc()


class DBNotLocked(Exception):
    pass

class SQLite():

    def __init__(self, name='jp.db', path=None, use_json=True, new_db=False):
        if path != None:
            name = path + name
        self.table_name = 'keys'
        if use_json == True:
            self.pickle = json
        else:
            self.pickle = pickle
        self.crypt = None
        self.lock = threading.Lock()

        if new_db == False:
            try:
                self.db = sql_db.SQLite(name)
                self.open()
            except sql_db.NoSQLiteDB as e:
                open(name, 'a').close()
                self.db = sql_db.SQLite(name)
                self.open()
                self.new_table()
        else:
            open(name, 'a').close()
            self.db = sql_db.SQLite(name)
            self.open()
            self.new_table()

    def open(self):
        self.db.connect()
        return True

    def new_table(self):
        sql_create_tasks_table = "CREATE TABLE IF NOT EXISTS %s (id integer PRIMARY KEY, key text NOT NULL UNIQUE, value text NOT NULL);" % (
            self.table_name)
        self.db.set(sql_create_tasks_table)
        self.db.commit()

    def sync(self):
        self.db.commit()
        return True

    def close(self):
        self.db.close()
        return True

    def get_key(self, key):
        query = "select value from %s where key='%s'" % (self.table_name, key)
        try:
            data = self.db.get(query)[0]
            if self.crypt != None:
                data = self.pickle.loads(self.crypt.decrypt(data))
            else:
                data = self.pickle.loads(data)
            return data
        except ValueError as e:
            raise sql_db.DBValueError(e)
        except TypeError as e:
            raise KeyError(e)
        except Exception as e:
            raise e

    def set_key_to(self, to_key, key, data):
        from_db = self.get_key(to_key)
        # from_db = json.loads(self.crypt.decrypt(self.db[to_key]))
        from_db[key] = data
        self.set_key(to_key, from_db)
        return True

    def keys_from(self, key_from):
        key = self.get_key(key_from)
        # data = json.loads(self.crypt.decrypt(self.db[key],))
        return key.keys()

    def set_key(self, key, data=None):
        try:
            if data == None:
                data = {}
            # if key == 'group':
            #     raise KeyError, data
            if self.crypt != None:
                data = self.crypt.encrypt(self.pickle.dumps(data))
            else:
                data = self.pickle.dumps(data)
            try:
                if self.get_key(key) is None:
                    raise KeyError
            except KeyError:
                query = "INSERT INTO %s (`key`, `value`) VALUES ('%s', '%s')" % (self.table_name, key, data)
            else:
                query = "UPDATE %s SET value='%s' WHERE key='%s'" % (self.table_name, data, key)
            self.db.set(query)
            return True
        except ValueError as e:
            raise sql_db.DBValueError(e)
        except Exception as e:
            raise e

    def keys(self):
        query = 'SELECT key from %s' % (self.table_name)
        data = self.db.get_all(query)
        var = []
        for i in data:
            var.append(i[0])
        return var

    def dell(self, key):
        query = "delete from %s where key='%s'" % (self.table_name, key)
        self.db.set(query)
        return True

    def acquire(self, in_loop=True):
        return self.lock.acquire(in_loop)

    def release(self):
        if self.isLock() == True:
            return self.lock.release()
        return True

    def isLock(self):
        return self.lock.locked()


class Berkeley():

    def __init__(self, name='jp.db', path=None):
        self.crypt = cr.Crypt(cr.Q2, cr.IV, compress=False)
        self.db = bsddb3.db.DB()
        if path == None:
            self.db.open(name, None, bsddb3.db.DB_HASH, bsddb3.db.DB_CREATE)
        else:
            self.db.open(path + name, None, bsddb3.db.DB_HASH, bsddb3.db.DB_CREATE)

    def isLock(self):
        return self.lock.locked()

    def acquire(self):
        self.lock.acquire()

    def release(self):
        try:
            self.lock.release()
        except Exception as e:
            raise DBNotLocked(e)

    def close(self):
        self.db.close()
        return True

    def sync(self):
        self.db.sync()
        return True

    def set_key(self, key, data=None):
        if data == None:
            self.db[key] = self.crypt.encrypt(json.dumps({}))
        else:
            self.db[key] = self.crypt.encrypt(json.dumps(data))
        return True

    def get_key(self, key):
        key = self.db[key]
        return json.loads(self.crypt.decrypt(key))

    def set_key_to(self, to_key, key, data):
        from_db = json.loads(self.crypt.decrypt(self.db[to_key]))
        from_db[key] = data
        self.db[to_key] = self.crypt.encrypt(json.dumps(from_db))
        return True

    def keys(self):
        data = self.db.keys()
        var = []
        for item in data:
            var.append(item)
        return var

    def keys_from(self, key_from):
        key = self.crypt.encrypt(key_from)
        data = json.loads(self.crypt.decrypt(self.db[key], ))
        return data.keys()

    def dell(self, key, del_key):
        db_key = self.get_key(key)
        del db_key[del_key]
        self.set_key(key, db_key)
        return True


def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2


def json_deserializer(key, value, flags):
    if flags == 1:
        return value
    if flags == 2:
        return json.loads(value)
    print("Unknown serialization format")




class MemDB():
    def __init__(self, re_read=False):

        db = SQLite()
        try:
            self.casino_name = db.get_key('casino_name')
            try:
                self.casino_name['ip']
            except KeyError:
                db.set_key('casino_name', {'name': '', 'ip': ''})
                db.sync()
                self.casino_name = db.get_key('casino_name')
        except:
            db.set_key('casino_name', {'name': '', 'ip': ''})
            db.sync()
            self.casino_name = db.get_key('casino_name')
        self.all_keys = db.keys()
        self.mem_cach2 = None
        # self.tunel_server = None
        if self.casino_name['ip']:
            self.tunel_server = True
            try:
                # self.tunel_server = Tunel(server=self.casino_name['ip'], port=55555)
                # self.tunel_server.start()
                self.mem_cach2 = mem_Client(('127.0.0.1', 11222), serializer=json_serializer,
                                                deserializer=json_deserializer, connect_timeout=conf.MEM_TIMEOUT, timeout=conf.MEM_TIMEOUT)
            except Exception as e:
                self.mem_cach2 = None
                traceback.print_exc()
        else:
            self.mem_cach2 = None
        self.mem_cach = mem_Client(('127.0.0.1', 11211), serializer=json_serializer, deserializer=json_deserializer)
        if re_read == True:
            for i in self.all_keys:
                self.mem_cach.set(i, db.get_key(i))
        self.set_key('REBOOT', False)

    def set_lock(self, timeout=0, model=True):
        if self.casino_name['ip'] and not self.mem_cach2:
            if not self.mem_cach2:
                try:
                    self.mem_cach2 = mem_Client(('127.0.0.1', 11222), serializer=json_serializer,
                                                deserializer=json_deserializer, connect_timeout=conf.MEM_TIMEOUT,
                                                timeout=conf.MEM_TIMEOUT)
                except Exception as e:
                    self.mem_cach2 = None
                    traceback.print_exc()
        if self.casino_name['ip'] and self.mem_cach2:
            try:
                if timeout > 0:
                    self.mem_cach2.set('lock', model, expire=timeout)
                else:
                    self.mem_cach2.set('lock', model)
            except Exception as e:
                traceback.print_exc()
        if timeout > 0:
            self.mem_cach.set('lock', model, expire=timeout)
        else:
            self.mem_cach.set('lock', model)

    def delete_lock(self, model=1):
        if self.casino_name['ip'] and not self.mem_cach2:
            if not self.mem_cach2:
                try:
                    self.mem_cach2 = mem_Client(('127.0.0.1', 11222), serializer=json_serializer,
                                                deserializer=json_deserializer, connect_timeout=conf.MEM_TIMEOUT,
                                                timeout=conf.MEM_TIMEOUT)
                except Exception as e:
                    self.mem_cach2 = None
                    traceback.print_exc()
        if self.casino_name['ip'] and self.mem_cach2:
            try:
                self.mem_cach2.delete('lock')
            except Exception as e:
                traceback.print_exc()
        return self.mem_cach.delete('lock')

    def check_for_lock(self):
        if self.casino_name['ip'] and not self.mem_cach2:
            if not self.mem_cach2:
                try:
                    self.mem_cach2 = mem_Client(('127.0.0.1', 11222), serializer=json_serializer,
                                                deserializer=json_deserializer, connect_timeout=conf.MEM_TIMEOUT,
                                                timeout=conf.MEM_TIMEOUT)
                except Exception as e:
                    self.mem_cach2 = None
                    traceback.print_exc()
        if self.casino_name['ip'] and self.mem_cach2:
            try:
                if self.mem_cach2.get('lock'):
                    return self.mem_cach2.get('lock')
            except Exception as e:
                traceback.print_exc()
        # if self.mem_cach.get('lock'):
        return self.mem_cach.get('lock')

    def close(self):
        # self.mem_cach.close()
        # if self.mem_cach2:
        #     try:
        #         self.mem_cach2.close()
        #     except:
        #         pass
        return True


    def isLock(self):
        return self.lock.locked()

    def acquire(self):
        self.lock.acquire()

    def release(self):
        try:
            self.lock.release()
        except Exception as e:
            raise DBNotLocked(e)

    # def delete(self, key):

    def get_key(self, key):
        data = self.mem_cach.get(key)
        if key == 'group' and self.casino_name['ip']:
            if not self.mem_cach2:
                try:
                    self.mem_cach2 = mem_Client(('127.0.0.1', 11222), serializer=json_serializer,
                                            deserializer=json_deserializer, connect_timeout=conf.MEM_TIMEOUT, timeout=conf.MEM_TIMEOUT)
                except Exception as e:
                    self.mem_cach2 = None
                    traceback.print_exc()
            try:
                data2 = self.mem_cach2.get(key)
                if data2:
                    for i in data2.keys():
                        if 'global_mistery' in data2[i]:
                            if data2[i]['global_mistery'] is True:
                                data[i] = data2[i]
            except Exception as e:
                traceback.print_exc()
        return data

    def set_key(self, key, data=None):
        if key == 'casino_name':
            if not self.casino_name['ip'] and data['ip'] and not self.tunel_server:
                self.tunel_server = Tunel(server=data['ip'], port=55555)
                self.tunel_server.start()
            self.casino_name = data
            if self.casino_name['ip']:
                if not self.mem_cach2:
                    try:
                        self.mem_cach2 = mem_Client(('127.0.0.1', 11222), serializer=json_serializer,
                                                    deserializer=json_deserializer, connect_timeout=conf.MEM_TIMEOUT,
                                                    timeout=conf.MEM_TIMEOUT)
                    except Exception as e:
                        self.mem_cach2 = None
                        traceback.print_exc()
        if key == 'group' and self.casino_name['ip']:
            if not self.mem_cach2:
                try:
                    self.mem_cach2 = mem_Client(('127.0.0.1', 11222), serializer=json_serializer,
                                            deserializer=json_deserializer, connect_timeout=conf.MEM_TIMEOUT, timeout=conf.MEM_TIMEOUT)
                except Exception as e:
                    self.mem_cach2 = None
                    traceback.print_exc()
            try:
                to_del = []
                for i in data:
                    if data[i]['global_mistery'] is True:
                        tmp = self.mem_cach2.get('group')
                        if tmp:
                            tmp[i] = data[i]
                            self.mem_cach2.set('group', tmp)
                        to_del.append(i)
                for i in to_del:
                    del data[i]
            except Exception as e:
                traceback.print_exc()
        self.mem_cach.set(key, data)
        return True

    def set_key_to(self, to_key, key, data):
        db_data = self.get_key(to_key)
        db_data[key] = data
        self.set_key(to_key, db_data)
        return True

    def keys(self):
        return self.all_keys

    def keys_from(self, key_from):
        data = self.mem_cach.get(key_from).keys()
        self.close()
        return data

    def dell(self, key, del_key):
        db_data = self.get_key(key)
        del db_data[del_key]
        self.set_key(key, db_data)
        return True



class DictDB():
    def __init__(self, re_read=False):

        db = SQLite()
        try:
            self.casino_name = db.get_key('casino_name')
            try:
                self.casino_name['ip']
            except KeyError:
                db.set_key('casino_name', {'name': '', 'ip': ''})
                db.sync()
                self.casino_name = db.get_key('casino_name')
        except:
            db.set_key('casino_name', {'name': '', 'ip': ''})
            db.sync()
            self.casino_name = db.get_key('casino_name')
        self.all_keys = db.keys()
        if self.casino_name['ip']:
            try:
                self.tunel_server = Tunel(server=self.casino_name['ip'], port=55555)
                self.tunel_server.start()
                self.mem_cach2 = mem_Client(('127.0.0.1', 11222), serializer=json_serializer,
                                            deserializer=json_deserializer, connect_timeout=conf.MEM_TIMEOUT,
                                            timeout=conf.MEM_TIMEOUT)
            except Exception as e:
                traceback.print_exc()
        self.mem_cach = mem_Client(('127.0.0.1', 11211), serializer=json_serializer, deserializer=json_deserializer)
        self.db = {}
        if re_read == True:
            for i in self.all_keys:
                self.db[i] = db.get_key(i)
        self.set_key('REBOOT', False)

    def acquire(self, in_loop=False):
        return self.lock.acquire(in_loop)

    def release(self):
        if self.isLock() == True:
            return self.lock.release()
        return True

    def isLock(self):
        return self.lock.locked()

    def get_key(self, key):
        try:
            return self.db[key]
        except KeyError:
            return

    def set_key(self, key, data={}):
        #         if data == None:
        #             data = {}
        self.db[key] = data
        return True

    def set_key_to(self, to_key, key, data):
        db_data = self.get_key(to_key)
        db_data[key] = data
        self.set_key(to_key, db_data)
        return True

    def keys(self):
        return self.db.keys()

    def keys_from(self, key_from):
        data = self.db[key_from].keys()
        self.close()
        return data

    def dell(self, key, del_key):
        del self.db[key][del_key]
        return True

    def mk_dump(self):
        if self.dump != None:
            keys = self.dump.keys()
            for i in keys:
                data = self.db[i]
                self.dump.set(i, data)
            self.dump.sync()
            return True
        return None

    def load_dump(self):
        self.db = {}
        if self.dump != None:
            for i in self.dump.keys():
                self.db.set(i, self.dump.get(i))
            return True
        return False

    def close(self):
        if self.dump != None:
            self.dump.close()
        return True

    def sync(self, key):
        if self.dump != None:
            data = self.get(key)
            self.dump.set(key, data)
            self.dump.sync()
            return True
        return False
