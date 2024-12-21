#-*- coding:utf-8 -*-
'''
Created on 8.09.2018 г.

@author: dedal
'''
import sqlite3
import MySQLdb
import psycopg2
import os
import datetime
from .exception import *  # @UnusedWildImport

class SQLdb():
    
    def __init__(self, dbname, user, passwd, host, port):
        '''
        Параметри на инстанцията:
        self.dbname
        self.user
        self.passwd
        self.conn
        self.db
        '''
        
        self.dbname = dbname
        self.user = user
        self.passwd = passwd
        if host == 'localhost': 
            host = '127.0.0.1'
        self.host = host
        self.port = port
        
    def get(self, query):
        '''  
        Използване:
            db = MySQL('testing', 'root', '102055', 'localhost')
            a = db.get('select * from user')
            print a['Name']
        
        Връща:
            Първия резултат от заявката като речник.
        '''
        self.db.execute(query)
        result = self.db.fetchone()
        return result
    
    def get_all(self, query):
        '''
        Използване:
            db = MySQL('testing', 'root', '102055', 'localhost')
            a = db.get_all('select * from user')
            print a[1]['Name']
            
        Връща:
            Резултата от заявката като наредена точка от речници.
        '''
        self.db.execute(query)
        result = self.db.fetchall()
        return result
    
    def set(self, query):
        '''
        Използване:
            db = MySQL('testing', 'root', '102055', 'localhost')
            a = db.set("INSERT INTO user(`Name`, `E-mail`, `sity`, `adres`) VALUES ('Гергана Дикиджиева','geci83@abv.bg','Тополи','ул.Овчага 71')")
            print a
            
        Връща:
            True
        '''
        self.db.execute(query)
        return True
    
    def set_many(self, query, value):
        '''
        Използване:
            db = MySQL('testing', 'root', '102055', 'localhost')
            a = db.set_many("""INSERT INTO user(`Name`, `E-mail`, `sity`, `adres`) 
                            VALUES (%s, %s, %s, %s)""",
                            [
                                ('1','1','1','1'),
                                ('2','2','2','2')
                            ]
                        )
        
        Връща:
            True
        '''
        self.db.executemany(query, value)
        return True

    def close(self):
        '''
        Използване:
            db = MySQL('testing', 'root', '102055', 'localhost')
            db.close()
            
        Връща:
            True
        '''
        self.conn.close()
        return True
    
    def commit(self):
        self.conn.commit()

class MySQL(SQLdb):
    '''
    Работи с MySQL база данни:
    
    Функции:
    __init__(dbname, user, passwd, host)
    get(query)
    get_all(query)
    set(query)
    set_many(query, value)
    close()
    _backup(path)
    _restory(scrypt)
    '''

    def connect(self):
        try:
            self.conn = MySQLdb.connect(db=self.dbname, user=self.user, host=self.host, passwd=self.passwd)
            self.conn.set_character_set('utf8')
            self.db = self.conn.cursor()
        except Exception as e:
            raise NoSQLDBConnection(e)
    
    
        
    def _backup(self, path, dump=None):
        '''
        Важно:
            Нуждае се от mysqldump.exe!
        
        Използване:
            db = MySQL('testing', 'root', '102055', 'localhost')
            a = db._backup('d:/Python/coffee-trade/bin/lib/')
            print a
            
        Връща:
            True
        '''
        path = path + '/' + self.dbname + '_' + 'bakup'
        now = datetime.datetime.now()
        now = now.strftime(path + '_' + "%d-%m-%Y_%H-%M-%S") + '.sql'
        if dump == None:
            command = '''mysqldump -u %s --password="%s" %s > %s''' % (self.user, self.passwd, self.dbname, now )
        else: 
            command = '''%s -u %s --password="%s" %s > %s''' % (dump, self.user, self.passwd, self.dbname, now )
        os.popen(command)
        self.close()
        return True
    
    def _restore(self, scrypt):
        '''
        Използване:
            db = MySQL('testing', 'root', '102055', 'localhost')
            a = db._restory('testing_bakup_21-12-2014_16-38-29.sql')
            print a
            
        Връща:
            True
        '''
        data = open(scrypt, 'r')
        query = " ".join(data.readlines())
        self.db.execute(query)
        return True
    
class SQLite(SQLdb):
    '''
    Работи с SQLite база данни:
    
    Функции:
        __init__(dbname)
        get(query)
        get_all(query)
        set(query)
        set_many(query, value)
        close()
        _backup(path)
        _restory(scrypt)
    '''
    
    def __init__(self, dbname):
        '''
        Параметри на инстанцията:
        self.dbname
        self.conn
        self.db
        '''
        
        self.dbname = dbname
        try:
            open(self.dbname, 'r').close()
        except Exception as e:
            raise NoSQLiteDB(e)

        self.conn = sqlite3.connect(self.dbname, check_same_thread=False)  # @UndefinedVariable
        self.conn.row_factory = sqlite3.Row  # @UndefinedVariable
        self.conn.text_factory = str
        
    def connect(self):
        try:
            self.db = self.conn.cursor()
            self.db.execute('PRAGMA encoding="UTF-8";')
        except Exception as e:
            raise NoSQLDBConnection(e)
    
    def _backup(self, path):
        '''
        Използване:
            db = MySQL('testing', 'root', '102055', 'localhost')
            a = db._backup('d:/Python/coffee-trade/bin/lib/')
            print a
            
        Връща:
            True
        '''
        path = path + '/' + self.dbname + '_' + 'bakup'
        now = datetime.datetime.now()
        now = now.strftime(path + '_' + "%d-%m-%Y_%H-%M-%S") + '.sql'
        with open( now, 'w') as f:
            for line in self.conn.iterdump():
                f.write('%s\n' % line)
        f.close()
        self.commit()
        return True

    def _restore(self, scrypt):
        '''
        Използване:
            db = MySQL('testing', 'root', '102055', 'localhost')
            a = db._restory('testing_bakup_21-12-2014_16-38-29.sql')
            print a
            
        Връща:
            True
        '''
        alltable = self.get_all('select * from sqlite_sequence')
        for i in alltable:
            query = 'drop table %s' % ( i['name'] )
            self.set(query)
        scrypt = open(scrypt, 'r').read()
        self.db.executescript(scrypt)
        self.commit()
        return True

class PostgreSQL(SQLdb):

    def connect(self):
        try:
            self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, host=self.host, password=self.passwd, port=self.port)
        except Exception as e:
            raise NoSQLDBConnection(e)
        self.db = self.conn.cursor()

    def _backup(self, backup_path, table_names=None, name=None):

        now = datetime.datetime.now()
        passwd = 'PGPASSWORD="%s" ' % (self.passwd)
        if name == None:
            filename = self.dbname + '_' + now.strftime("%Y_%m_%d_%H_%M_%S") + '.backup'
        else:
            filename = name + '_' + now.strftime("%Y_%m_%d_%H_%M_%S") + '.backup'
        command_str = str(self.host)+" -p "+str(self.port)+" -d "+self.dbname+" -U "+self.user
        if os.name == 'posix':
            command_str = passwd+ "pg_dump -h "+command_str
        else:
            command_str = r"bin\\pg_dump.exe -h -b -f %s --format=custom -v postgresql://%s:%s@%s:%s/%s" % (backup_path+"/"+filename, self.user,self.passwd,self.host,self.port, self.dbname)
        if os.name == 'posix':
            if table_names is not None:
                for x in table_names:
                    command_str = command_str +" -t "+x

            command_str = command_str + " -F c -b -v -f '"+backup_path+"/"+filename+"'"
        try:
            os.system(command_str)
            print("Backup completed")
            return True

        except Exception as e:
            print("!!Problem occured!!")
            print(e)
            return False

    def _restore(self, backup_path, table_names=None):
        command_str = str(self.host) + " -p " + str(self.port) + " -d " + self.dbname + " -U " + self.user
        if os.name == 'posix':
            command_str = 'PGPASSWORD="%s" pg_restore -h %s ' % (self.passwd, command_str)
        else:
            # os.system('SET "PGPASSWORD=%s"' % ())
            command_str = r'SET "PGPASSWORD=%s" & bin\\pg_restore.exe --host "%s" --port "%s" --username "%s" -n public --dbname "%s" "%s"' % (self.passwd, self.host, self.port, self.user, self.dbname, backup_path)
        if os.name == 'posix':
            if table_names is not None:
                for x in table_names:
                    command_str = command_str + " -t " + x

            command_str = command_str + " -v '" + backup_path + "'"
        try:
            os.system(command_str)
            print("Restore completed")
            return True
        except Exception as e:
            print("!!Problem occured!!")
            print(e)
            return False

    def drop_tables(self):
        self.conn.set_isolation_level(0)
        cur = self.conn.cursor()
        cur.execute("drop schema public cascade")
        cur.execute("create schema public")
        return True

    def close_all_session(self):
        self.conn.set_isolation_level(0)
        cur = self.conn.cursor()
        cmd = '''SELECT pg_terminate_backend(pg_stat_activity.pid)
                    FROM pg_stat_activity
                    WHERE pg_stat_activity.datname = '%s'
                    AND pid <> pg_backend_pid();''' % (self.dbname)
        cur.execute(cmd)
        return True


    def drop_tables(self):
        self.conn.set_isolation_level(0)
        cur = self.conn.cursor()
            #         cur.execute("SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema ='public'")
            #         row = cur.fetchall()
            #         for i in row:
        cur.execute("drop schema public cascade")
        cur.execute("create schema public")
        return True

    def close_all_session(self):
        self.conn.set_isolation_level(0)
        cur = self.conn.cursor()
        cmd = '''SELECT pg_terminate_backend(pg_stat_activity.pid)
                    FROM pg_stat_activity
                    WHERE pg_stat_activity.datname = '%s'
                    AND pid <> pg_backend_pid();''' % (self.dbname)
        cur.execute(cmd)
        return True
            
if __name__ == '__main__':
    a = SQLite('smib.dbsql')
    a.connect()
    a.get('select * from user')
