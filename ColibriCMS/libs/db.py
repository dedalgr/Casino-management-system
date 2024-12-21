#-*- coding:utf-8 -*-
'''
Created on 6.10.2018 г.

@author: dedal
'''

import psycopg2
import os
import datetime

class NoSQLDBConnection(Exception):
    pass

class NoSQLiteDB(Exception):
    pass


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
                
if __name__ == '__main__':
    DB = PostgreSQL(host='127.0.0.1', user='mistralcms', passwd='use_system10', dbname='mistralcms', port=5432)
    DB.connect()
    # DB.db.execute('TRUNCATE system_log;')
    # DB.db.execute('TRUNCATE get_counter_error;')
    DB._restore('/home/dedal/ivan_asenovgrad_1.backup')
    # import datetimemistralcms_12-11-2020_12-46-53.backup
    # cmd = r'''INSERT INTO get_counter_error ("user_id", "info", "pub_time") VALUES (%s, '%s', '%s');''' % (2, str('DB RESTORY'), datetime.datetime.now() )
    # print cmd
    # cur = DB.conn.cursor()
    # cur.execute(cmd)
    # DB.close_all_session()
    # print 1
    # DB.drop_tables()
    # print 2
    # DB._restore('/home/dedal/mistralcms_02-01-2020_12-36-28.backup')
    # DB.create_db()
