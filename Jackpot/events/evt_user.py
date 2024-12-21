#-*- coding:utf-8 -*-
import db.db  # @UnresolvedImport
DB = db.db.MemDB()

def LOGIN(**kwargs):
    users = DB.get_key('users')  #
    DB.close()
    try:
        user = users[kwargs['user']]
    except KeyError:
        return False
    if user['passwd'] != kwargs['passwd']:
        return False
    else:
        return True

def ADD_USER(**kwargs):
    DB.set_key_to('users', kwargs['user'], kwargs)
    DB.close()
    return True


def DEL_USER(**kwargs):
    DB.dell('users', kwargs['user'])
    DB.close()
    return True

def ALL_USER(**kwargs):
    user = DB.keys_from('users')
    DB.close()
    return user  #
