#-*- coding:utf-8 -*-
'''
Created on 8.09.2018 г.

@author: dedal
'''
from .exception import *
import time
import datetime
import threading

from pymemcache.client.base import PooledClient as mem_Client
# from memcached_stats import MemcachedStats
try:
    import _pickle as pickle  # @UnusedImport
except ImportError as e:
    import pickle  # @UnusedImport @Reimport

import json

class DictDB():
    def __init__(self, dump_db=None):
        
        self.dump = dump_db
        self.lock = threading.Lock()
        self.db = {}
        if self.dump  != None:
            for i in self.dump.keys():
                self.db[i] = self.dump.get(i)
    
    def acquire(self, in_loop=False):
        return self.lock.acquire(in_loop)
         
    def release(self):
        if self.isLock() == True:
            return self.lock.release()
        return True
    
    def isLock(self):
        return self.lock.locked()
    
    def get(self, key):
        try:
            return self.db[key]
        except KeyError:
            return 
        
    def set(self, key, data={}):
        self.db[key] = data
        return True

    
    def keys(self):
        return list(self.db.keys())
    
    def dell(self, key, del_key):
        del self.db[key][del_key]
        return True
    
    def mk_dump(self):
        if self.dump != None:
            keys = list(self.dump.keys())
            for i in keys:
                data = self.db[i]
                self.dump.set(i, data)
            self.dump.sync()
            return True
        return None
    
    def load_dump(self):
        self.db = {}
        if self.dump  != None:
            for i in list(self.dump.keys()):
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
    
    
class MemDB():
    def __init__(self, host=('127.0.0.1', 11211), dump_db=None, crypt=None, use_json=True):
        self.lock = self.lock = threading.Lock()
        self.dump = dump_db
        self.crypt = crypt
        # self.status = MemcachedStats(host=host[0], port=host[1])
        if use_json == True:
            self.pickle = json
        else:
            self.pickle = pickle
        self.mem_cach = mem_Client(host, serializer=self.serializer, deserializer=self.deserializer)
        self.load_dump()
        
    
    def serializer(self, key, value):
        try:
            if type(value) == str:
                if self.crypt != None:
                    return self.crypt.encrypt(value), 1
                else:
                    return value, 1
            else:
                if self.crypt != None:
                    return self.crypt.encrypt(self.pickle.dumps(value)), 2
                else:
                    return self.pickle.dumps(value), 2
        except Exception as e:
            raise BadSerializationFormat("Unknown serialization format")
        # return None

    def deserializer(self, key, value, flags):
        try:
            if self.crypt != None:
                if flags == 1:
                    return self.crypt.decrypt(value)
                if flags == 2:
                    return self.crypt.decrypt(self.pickle.loads(value))
            else:
                if flags == 1:
                    return value
                if flags == 2:
                    return self.pickle.loads(value)
        except Exception as e:
            raise BadSerializationFormat(e)

    def make_dump(self):
#         sync = False
        try:
            if self.dump != None:
                keys = list(self.dump.keys())
                for i in keys:
                    data = self.db[i]
                    self.dump.set(i, data)
                self.dump.sync()
                return True
            else:
                return False
        except socket.error:
            raise MemDBSocketError
        except MemcacheUnexpectedCloseError:
            raise MemDBCloseWarning
        except Exception as e:
            raise e

    
    def load_dump(self):
        try:
            if self.dump  != None:
                for i in list(self.dump.keys()):
                    self.mem_cach.set(i, self.dump.get(i))
                return True
        except socket.error:
            raise MemDBSocketError
        except MemcacheUnexpectedCloseError:
            raise MemDBCloseWarning
        except Exception as e:
            raise e

    
    def sync(self):
        try:
            if self.dump != None:
                for i in list(self.keys()):
                    data = self.mem_cach.get(i)
                    self.dump.set(i, data)
                self.dump.sync()
                return True
            else:
                return False
        except socket.error:
            raise MemDBSocketError
        except MemcacheUnexpectedCloseError:
            raise MemDBCloseWarning
        except Exception as e:
            raise e


    
    def close(self):
        if self.dump != None:
            self.dump.close()
        return True
    
    def keys(self):
        try:
            all_keys = list(self.status.keys())
            return all_keys
        except socket.error:
            raise MemDBSocketError
        except MemcacheUnexpectedCloseError:
            raise MemDBCloseWarning
        except Exception as e:
            raise e


    def acquire(self, in_loop=False):
        return self.lock.acquire(in_loop)

    def release(self):
        if self.isLock() == True:
            return self.lock.release()
        return True
     
    def isLock(self):
        return self.lock.locked()
    
    def get(self, key):
        try:
            return self.mem_cach.get(key)
        except socket.error:
            raise MemDBSocketError
        except MemcacheUnexpectedCloseError:
            raise MemDBCloseWarning
        except Exception as e:
            raise e

    
    def set(self, key, data={}):
        try:
            return self.mem_cach.set(key, data)
        except socket.error:
            raise MemDBSocketError
        except MemcacheUnexpectedCloseError:
            raise MemDBCloseWarning
        except Exception as e:
            raise e

    
    def dell(self, key):
        try:
            return self.mem_cach.delete(key)
        except socket.error:
            raise MemDBSocketError
        except MemcacheUnexpectedCloseError:
            raise MemDBCloseWarning
        except Exception as e:
            raise e
