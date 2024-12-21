#-*- coding:utf-8 -*-
'''
Created on 12.10.2018 г.

@author: dedal
'''

from sqlalchemy import desc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError, InvalidRequestError, OperationalError
import json
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String,  ForeignKey, DateTime, Float, Boolean, Text



class NoDBConnection(Exception):
    pass

class BadRequest(Exception):
    pass

class PostgresqlCtrl():
    
    def __init__(self, user, password, db_name, host='127.0.0.1', port=5432, timeout=30, debug=False, scoped=True):
        self.user = user
        self.port = port
        self.password = password
        self.host = host
        self.db_name = db_name
        self.debug = debug
        self.scoped = scoped
        self.timeout = timeout
        self.make_engine()
        self.make_session()
    
    def make_engine(self):
    
        self.engine = create_engine('postgresql://%s:%s@%s:%s/%s' %
                               (self.user, self.password, self.host, self.port, self.db_name),
                               echo=self.debug,
                               echo_pool=self.debug,
                               pool_reset_on_return=True,
                               connect_args = {'connect_timeout':self.timeout}
                               )
        return True
    
    def make_session(self):
        session_factory = sessionmaker(bind=self.engine) 
        if self.scoped == True: 
            self.session = scoped_session(session_factory)
        else:
            self.session = session_factory()
        return True

    def dispose(self):
        self.session.close()
        self.engine.dispose() 
    
    def expire(self):
        self.session.expire_all()
        
    def open(self):
        self.session = self.session()
        
    def close(self):
        self.session.remove() 
              
#     @staticmethod
    def make_obj(self, models_class):
        try:
            obj = models_class()
        except OperationalError as e:
            self.rollback()
            raise NoDBConnection(e)
        except InvalidRequestError as e:
            self.rollback()
            raise BadRequest(e)
        return obj
  
#     @staticmethod
    def commit(self):
        try:
            self.session.commit()
            self.expire()
            return True
        except IntegrityError as e:
            self.session.rollback()
            raise e
        except OperationalError as e:
            self.rollback()
            raise NoDBConnection(e)
        except InvalidRequestError as e:
            self.rollback()
            raise BadRequest(e)
            
        
    def rollback(self):
        try:
            self.session.rollback()
            return True
        except OperationalError as e:
            self.rollback()
            raise NoDBConnection(e)
        except InvalidRequestError as e:
            self.rollback()
            raise BadRequest(e)

    def add_object_to_session(self, obj):
        try:
            self.session.add(obj)
            return True
        except OperationalError as e:
            self.rollback()
            raise NoDBConnection(e)
        except InvalidRequestError as e:
            self.rollback()
            raise BadRequest(e)
#     
#     @staticmethod
    def get_all(self, models_class, order=None, descs=False):
        try:
            if order == None and descs == False:
                return self.session.query(models_class).all()
            elif order == None and descs == True:
                return self.session.query(models_class).order_by(desc('id')).all()
            elif order != None and descs == False:
                return self.session.query(models_class).order_by(order).all()
            elif order != None and descs == True:
                return self.session.query(models_class).order_by(desc(order)).all()
        except OperationalError as e:
            self.rollback()
            raise NoDBConnection(e)
        except InvalidRequestError as e:
            self.rollback()
            raise BadRequest(e)
        
    def get_one(self, models_class, order=None, descs=False):
        try:
            if order == None and descs == False:
                return self.session.query(models_class).first()
            elif order == None and descs == True:
                return self.session.query(models_class).order_by(desc('id')).first()
            elif order != None and descs == False:
                return self.session.query(models_class).order_by(order).first()
            elif order != None and descs == True:
                return self.session.query(models_class).order_by(desc(order)).first()
        except OperationalError as e:
            self.rollback()
            raise NoDBConnection(e)
        except InvalidRequestError as e:
            self.rollback()
            raise BadRequest(e)
        
    def get_one_where(self, models_class, order=None, descs=False, **kwargs):
        tmp_int = str(models_class.__name__) + '.%s==%d'
        tmp_str = str(models_class.__name__) + '.%s=="%s"'
        lte_int = str(models_class.__name__) + '.%s<=%d'
        gte_int = str(models_class.__name__) + '.%s>=%d'
        btw_int = str(models_class.__name__) + '.%s.between(%s, %s)'
        lte_str = str(models_class.__name__) + '.%s<="%s"'
        gte_str = str(models_class.__name__) + '.%s>="%s"'
        btw_str = str(models_class.__name__) + '.%s.between("%s", "%s")'
        bool_tmp= str(models_class.__name__) + '.%s.is_(%s)'
        
        select = ''
        for i in kwargs:
            if type(kwargs[i]) == str or type(kwargs[i]) == unicode:
                if i[-5:] == '__gte':
                    select = select + gte_str % (i[0:-5], kwargs[i]) + ','
                elif i[-5:] == '__lte':
                    select = select + lte_str % (i[0:-5], kwargs[i]) + ','
                else:
                    select = select + tmp_str % (i, kwargs[i]) + ','
                    
            elif type(kwargs[i]) == int:
                if i[-5:] == '__gte':
                    select = select + gte_int % (i[0:-5], kwargs[i]) + ','
                elif i[-5:] == '__lte':
                    select = select + lte_int % (i[0:-5], kwargs[i]) + ','
                else:
                    select = select + tmp_int % (i, kwargs[i]) + ','
            elif type(kwargs[i]) == bool  or kwargs[i] == None:
                select = select + bool_tmp % ( i, kwargs[i]) + ','
                
            else:
                if i[-5:] == '__btw':
                    if type(kwargs[i][0]) == str or type(kwargs[i][0]) == unicode:
                        select = select + btw_str % (i[0:-5], kwargs[i][0], kwargs[i][1]) + ','

                    else:
                        select = select + btw_int % (i[0:-5], kwargs[i][0], kwargs[i][1]) + ','
                else:
                    select = select + tmp_str % (i, kwargs[i]) + ','
        try:     
            if order == None and descs == False:
                return self.session.query(models_class).filter(*eval(select)).first()
            elif order == None and descs == True:
                return self.session.query(models_class).filter(*eval(select)).order_by(desc('id')).first()
            elif order != None and descs == False:
                return self.session.query(models_class).filter(*eval(select)).order_by(order).first()
            elif order != None and descs == True:
                return self.session.query(models_class).filter(*eval(select)).order_by(desc(order)).first()
        except OperationalError as e:
            self.rollback()
            raise NoDBConnection(e)
        except InvalidRequestError as e:
            self.rollback()
            raise BadRequest(e)
            
    def get_all_where_like(self, models_class, **kwargs):
#         Note.query.filter(Note.message.like("%somestr%")).all()
        tmp_str = str(models_class.__name__) + '.%s.like("%s")'
        select = ''
        for i in kwargs:
            select = tmp_str % (i, '%' + kwargs[i] + '%')
        try:
            return self.session.query(models_class).filter(eval(select)).all()
        except OperationalError as e:
            self.rollback()
            raise NoDBConnection(e)
        except InvalidRequestError as e:
            self.rollback()
            raise BadRequest(e)
            
    def get_all_where(self, models_class, order=None, descs=False, **kwargs):
        tmp_int =  str(models_class.__name__) + '.%s==%d'
        tmp_str = str(models_class.__name__) + '.%s=="%s"'
        lte_int = str(models_class.__name__) + '.%s<=%d'
        gte_int = str(models_class.__name__) + '.%s>=%d'
        btw_int = str(models_class.__name__) + '.%s.between(%s, %s)'
        lte_str = str(models_class.__name__) + '.%s<="%s"'
        gte_str = str(models_class.__name__) + '.%s>="%s"'
        btw_str = str(models_class.__name__) + '.%s.between("%s", "%s")'
        bool_tmp= str(models_class.__name__) + '.%s.is_(%s)'

        select = ''
        for i in kwargs:
            if type(kwargs[i]) == str  or type(kwargs[i]) == unicode:
                if i[-5:] == '__gte':
                    select = select + gte_str % (i[0:-5], kwargs[i]) + ','
                elif i[-5:] == '__lte':
                    select = select + lte_str % (i[0:-5], kwargs[i]) + ','
                else:
                    select = select + tmp_str % (i, kwargs[i]) + ','
                    
            elif type(kwargs[i]) == int:
                if i[-5:] == '__gte':
                    select = select + gte_int % (i[0:-5], kwargs[i]) + ','
                elif i[-5:] == '__lte':
                    select = select + lte_int % (i[0:-5], kwargs[i]) + ','
                else:
                    select = select + tmp_int % ( i, kwargs[i]) + ','
            elif type(kwargs[i]) == bool or kwargs[i] == None:
                select = select + bool_tmp % ( i, kwargs[i]) + ','
            else:
                if i[-5:] == '__btw':
                    if type(kwargs[i][0]) == str or type(kwargs[i][0]) == unicode:
                        select = select + btw_str % (i[0:-5], kwargs[i][0], kwargs[i][1]) + ','

                    else:
                        select = select + btw_int % (i[0:-5], kwargs[i][0], kwargs[i][1]) + ','
                else:
                    select = select + tmp_str % (i, kwargs[i]) + ','
        try:  
            if order == None and descs == False:
                return self.session.query(models_class).filter(*eval(select)).all()
            elif order == None and descs == True:
                return self.session.query(models_class).filter(*eval(select)).order_by(desc('id')).all()
            elif order != None and descs == False:
                return self.session.query(models_class).filter(*eval(select)).order_by(order).all()
            elif order != None and descs == True:
                return self.session.query(models_class).filter(*eval(select)).order_by(desc(order)).all()
        except OperationalError as e:
            self.rollback()
            raise NoDBConnection(e)
        except InvalidRequestError as e:
            self.rollback()
            raise BadRequest(e)
            
#     @staticmethod
    def delete_object(self, obj):
#         try:
        try:
            self.session.delete(obj)
            return True
        except OperationalError as e:
            self.rollback()
            raise NoDBConnection(e)
        except InvalidRequestError as e:
            self.rollback()
            raise BadRequest(e)
        
    def empty_table(self, models_class):
        try:
            self.session.query(models_class).delete()
            return True
        except OperationalError as e:
            self.rollback()
            raise NoDBConnection(e)
        except InvalidRequestError as e:
            self.rollback()
            raise BadRequest(e)
        

    