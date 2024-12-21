#-*- coding:utf-8 -*-
'''
Created on 28.10.2017 г.

@author: dedal
'''
from . import jpconf
import libs

class JPMain(jpconf.user.Login):
    def __init__(self, parent):
        err = libs.DB.make_obj(libs.models.GetCounterError)
        err.user_id = parent.USER.id  # @UndefinedVariable
#             err.mashin_nom_in_l = 1
        err.info = 'JPSERVER' + ': ' + _(u'Отворена програма за настройки на сървър %s.') % (parent.USER.name )
        libs.DB.add_object_to_session(err)
        # try:
        libs.DB.commit()
        # except:
        #     libs.DB.rollback()
        jpconf.user.Login.__init__(self, parent)