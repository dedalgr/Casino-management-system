#-*- coding:utf-8 -*-
'''
Created on 8.09.2018 г.

@author: dedal
'''
if __name__ == '__main__':
    from exception import *
else:
    from .exception import *  # @UnusedWildImport
import time  # @UnusedImport
import datetime  # @UnusedImport
import threading
# import shelve

try:
    import cPickle as pickle  # @UnusedImport
except ImportError as e:
    import pickle  # @UnusedImport @Reimport

import json
# import bsddb3
# from bsddb3.db import DBNotFoundError
from . import sql_db

class SQLite():
    
    def __init__(self, name, crypt=None, use_json=True, new_db=False):
        self.table_name = 'keys'
        if use_json == True:
            self.pickle = json
        else:
            self.pickle = pickle
        self.crypt = crypt
        self.lock = threading.Lock()
        
        if new_db == False:
            try:
                self.db = sql_db.SQLite(name)
                self.open()
            except NoSQLiteDB as e:
                raise EmptyDB(e)
        else:
            open(name, 'a').close()
            self.db = sql_db.SQLite(name)
            self.open()
            self.new_table()
            
    def open(self):
        self.db.connect()
        return True
    
    def new_table(self):
        sql_create_tasks_table = "CREATE TABLE IF NOT EXISTS %s (id integer PRIMARY KEY, key text NOT NULL UNIQUE, value text NOT NULL);" % (self.table_name)
        self.db.set(sql_create_tasks_table)
        self.db.commit()
    
    def sync(self):
        self.db.commit()
        return True
    
    def close(self):
        self.db.close()
        return True
    
    def get(self, key):
        query = "select value from %s where key='%s'"% (self.table_name, key)
        try:
            data = self.db.get(query)[0]
            if self.crypt != None:
                data = self.pickle.loads(self.crypt.decrypt(data))
            else:
                data = self.pickle.loads(data)
            return data
        except ValueError as e:
            raise DBValueError(e)
        except TypeError as e:
            raise KeyError(e)
        except Exception as e:
            raise e

    def set(self, key, data={}):
        try:
            if self.crypt != None:
                data = self.crypt.encrypt(self.pickle.dumps(data))
            else:
                data = self.pickle.dumps(data)
            try:
                self.get(key)
            except KeyError:
                query = "INSERT INTO %s (`key`, `value`) VALUES ('%s', '%s')" % (self.table_name, key, data)
            else:
                query = "UPDATE %s SET value='%s' WHERE key='%s'" % (self.table_name, data, key)
            self.db.set(query)
            return True
        except ValueError as e:
            raise DBValueError(e)
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
        query = "delete from %s where key='%s'"% (self.table_name, key)
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
            
# class Berkeley():
#
#     def __init__(self, name='./berkely.db', crypt=None, use_json=True, new_db=False):
#         if use_json == True:
#             self.pickle = json
#         else:
#             self.pickle = pickle
#         if new_db == False:
#             try:
#                 open(name, 'r')
#             except IOError as e:
#                 raise EmptyDB(e)
#         self.new_db = new_db
#         self.name = name
#         self.crypt = crypt
#         self.lock = threading.Lock()
#         self.open()
#
#     def acquire(self, in_loop=True):
#         return self.lock.acquire(in_loop)
#
#     def release(self):
#         if self.isLock() == True:
#             return self.lock.release()
#         return True
#
#     def isLock(self):
#         return self.lock.locked()
#
#     def open(self):
#         self.db = bsddb3.db.DB()  # @UndefinedVariable
#         self.db.open(self.name, None, bsddb3.db.DB_HASH, bsddb3.db.DB_CREATE)  # @UndefinedVariable
#         return True
#
#     def close(self):
#         self.db.close()
#         return True
#
#     def sync(self):
#         self.db.sync()
#         return True
#
#     def set(self, key, data={}):
#         try:
#             if self.crypt != None:
#                 self.db[key] = self.crypt.encrypt(self.pickle.dumps(data))
#             else:
#                 self.db[key] = self.pickle.dumps(data)
#         except ValueError as e:
#             raise DBValueError(e)
#         return True
#
#     def get(self, key):
#         data = None
#         try:
#             key = self.db[key]
#             if self.crypt != None:
#                 data = self.pickle.loads(self.crypt.decrypt(key))
#             else:
#                 data = self.pickle.loads(key)
#             return data
#         except ValueError as e:
#             raise DBValueError(e)
#
#
#     def keys(self):
#         try:
#             data = self.db.keys()
#             var = []
#             for item in data:
#                 var.append(item)
#             return var
#         except ValueError as e:
#             raise DBValueError(e)
#
#     def dell(self, key):
#         try:
#             del self.db[key]
#             return True
#         except ValueError as e:
#             raise DBValueError(e)
#         except DBNotFoundError as e:
#             raise KeyError(key)
        
# class Shelve(Berkeley):
#
#     def open(self):
#         self.db = bsddb3.db.DB()  # @UndefinedVariable
#         if self.new_db == True:
#             self.db = shelve.open(self.name, 'n')
#         else:
#             self.db = shelve.open(self.name, 'w')
#         return True
    
if __name__ == '__main__':
    pg = SQLite('smib.dbsql', new_db=True)
    print(list(pg.keys()))
    def a():
        while True:
            pg = SQLite('smib.dbsql', new_db=True)
            pg.acquire()
            pg.set('test3', [])
            print(pg.get('test3'), 'a')
            pg.release()
    def b():
        while True:
            pg = SQLite('smib.dbsql', new_db=True)
            pg.acquire()
            pg.set('test3', {})
            print(pg.get('test3'), 'b')
            pg.release()
    t = threading.Thread(target=a)
    t.start()
    i = threading.Thread(target=b)
    i.start()
   
