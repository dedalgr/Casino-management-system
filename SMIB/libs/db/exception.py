#-*- coding:utf-8 -*-
'''
Created on 8.09.2018 г.

@author: dedal

'''
from pymemcache.exceptions import MemcacheUnexpectedCloseError
from threading import ThreadError
import socket

class MemDBCloseWarning(MemcacheUnexpectedCloseError):
    pass

class MemDBSocketError(socket.error):
    pass

class DBBadDump(Exception):
    pass

class BadSerializationFormat(Exception):
    pass

class DBNotLocked(Exception):
    pass

class DBValueError(Exception):
    pass

class NoSQLDBConnection(Exception):
    pass

class NoSQLiteDB(Exception):
    pass

class EmptyDB(Exception):
    pass