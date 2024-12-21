#-*- coding:utf-8 -*-
'''
Created on 31.10.2019 г.

@author: dedal
'''
import json
if __name__ == '__main__':
    import sys
    import os
    import gui
    import msg
    sys.path.append('/home/dedal/Colibri/ColibriCMS/2_1/libs')
    sys.path.append('/home/dedal/Colibri/ColibriCMS/2_1/')
    # os.chdir('/home/dedal/Colibri/ColibriCMS/2_1')
    from libs import models as models
else:
    from . import gui
    from . import msg
    from libs import models as models
    # import models


# MODULE = {
#         'order': 2,
#         'keysystem': 3,
#         'taloni': 4,
#         'klienti': 5,
#         'kartov modul': 6,
#         }

RIGHT = { 'main':{
    1:msg.main_m_tool3,
    2:msg.main_m_tool9,
    3:msg.main_m_tool5,
    4:msg.main_m_tool8,
    5:msg.main_m_tool10,
    6:msg.main_m_tool102,
    7:msg.main_m_tool101,
    8:msg.main_m_button9,
    9:msg.main_m_button25,
    10:msg.main_m_button26,
    11:msg.main_m_button7,
    12:msg.main_m_button6,
    13:msg.main_m_button30,
    14:msg.main_m_button12,
    15:msg.main_m_button13,
    16:msg.main_m_button15,
    17:msg.main_m_button21,
    18:msg.main_m_button22,
    19:msg.main_m_button251,
    20:msg.main_m_tool91,
    21:msg.main_m_order_print,
    22:msg.main_m_button301,
    23:msg.main_d_click,
    24:msg.main_set_service_info,
    25:msg.server_and_smib_player_reset,
    26:msg.set_emg_date_time,
    27:msg.clean_goged_in,
    28:msg.main_m_tool103,
}
,
          'cust':{
    1:msg.cust_m_tool2,
    2:msg.cust_m_tool9,
    3:msg.cust_m_tool3,
    4:msg.cust_m_tool4,
    5:msg.cust_m_tool5,
    6:msg.cust_m_tool7,
    7:msg.cust_m_tool8,
    8:msg.cust_m_tool91,
    9:msg.curt_m_listCtrl2_monyback,
    10:msg.curt_m_listCtrl2_talon,
    11:msg.curt_del_all_talon,
    12:msg.cust_group_replace_row,
    13:msg.cust_atm,
    14:msg.root_show_cust,
    15:msg.user_show_cust,
    16:msg.cust_cart_lost,
    17:msg.cust_reserve,
    18:msg.cust_print_rko,
    19:msg.cust_del_group,
    20:msg.catd_copy,
    21:msg.group_copy,
    22:msg.cart_price,
    23:msg.check_egn_by_hand
          },
          'config':{
    1:msg.conf_m_tool1,
    2:msg.conf_m_tool2,
    3:msg.conf_m_tool4,
    4:msg.conf_m_tool7,
    5:msg.conf_m_tool16,
    6:msg.conf_m_tool22,
    7:msg.conf_m_tool10,
    8:'SAS Tester',
          },
          'order':{
    1:msg.order_m_tool6,
    2:msg.order_m_tool2,
    3:msg.order_m_tool102,
    4:msg.order_m_tool3,
    5:msg.order_m_tool4,
    6:msg.order_m_tool8,
    7:msg.order_m_tool101,
    8:msg.order_m_tool111,
    9:msg.order_m_tool10,
    10:msg.order_elcount_edit,

    11:msg.order_prihod_tupe_add,
    12:msg.order_razhod_tupe_add,
    13:msg.order_prihod_edit,
    14:msg.order_razhod_edit,
    15:msg.order_load_user_order,
    16:msg.order_handcount_edit,
          },
          'user':{
    1:msg.user_m_tool2,
    2:msg.user_m_tool3,
    3:msg.user_m_tool4,
    4:msg.user_hold_missing_mony,
          },
          'mashin':{
    1:msg.mashin_m_tool2,
    2:msg.mashin_m_tool3,
    3:msg.mashin_m_tool5,
    4:msg.mashin_m_tool4,
    5:msg.mashin_elcount_edit,
    6:msg.mashin_edit,
    7:msg.mashin_add_to_jp,
          },
          'diff': {
    # 1:msg.diff_order_edit,
    1:msg.diff_month_report_from_to,
    2:msg.lock_procent_in_realtime,
          },
    'report': {
        1:msg.report_order_edit,
        2:msg.report_m_tool2,
        3:msg.report_m_tool3,
        4:msg.report_m_tool4,
        5:msg.report_m_tool6,
        6:msg.report_m_tool9,
        7:msg.report_m_tool7,
        8:msg.report_m_tool8,
    }

}


def right_install(name='OWNER'):
    db = models.DBCtrl()
    group = db.get_one_where(models.UserGrup, name=name)
    #group.name = 'OWNER'
    right = {}
    for i in list(RIGHT.keys()):
        right[i] = (list(RIGHT[i].keys()))
    # right = group.to_json()
    # print right
    group.right = right
    group.to_json()
    db.add_object_to_session(group)
    db.commit()

def db_init_new():
    DB = models.DBCtrl()

    group = DB.make_obj(models.UserGrup)
    group.name = 'OWNER'
    right = {}
    for i in list(RIGHT.keys()):
        right[i] = (list(RIGHT[i].keys()))
    group.right = right
    group.to_json()
    DB.add_object_to_session(group)
    DB.commit()

    pr_type = DB.make_obj(models.PrihodType)
    pr_type.name = u'Cust Cart'
    pr_type.hiden = True
    DB.add_object_to_session(pr_type)
    DB.commit()
    # rh_type = DB.make_obj(models.RazhodType)
    # rh_type.name = u'AFT Bonus'
    # DB.add_object_to_session(rh_type)
    # DB.commit()
    # monyback = DB.make_obj(models.RazhodType)
    # monyback.name = u'MonyBack'
    # DB.add_object_to_session(monyback)
    # DB.commit()

    user = DB.make_obj(models.User)
    user.name = 'root'
    user.passwd = '123456'
    user.grup_id = group.id
    DB.add_object_to_session(user)
    DB.commit()



if __name__ == '__main__':
    # import os
    # os.chdir('/home/dedal/Coliblri/ColibriCMS/2_1/')
    db_init_new()
    # right_install()
