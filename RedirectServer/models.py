# -*- coding:utf-8 -*-
'''
Created on 27.09.2017 г.

@author: dedal
'''
import conf
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import declarative_base
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError, InvalidRequestError, OperationalError
import json
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean, Text, BigInteger
import datetime
import os
from sqlalchemy.pool import NullPool

#if __package__ == 'libs':

engine = create_engine('postgresql://%s:%s@%s:%s/%s' %
                           (conf.DB_USER, conf.DB_PASS, conf.DB_IP, conf.DB_PORT, conf.DB_NAME),
                           echo=conf.DB_DEBUG,
                           echo_pool=False,
                           pool_reset_on_return=True,
                           connect_args={'connect_timeout': 30},
                           # poolclass=NullPool,
                           # pool_recycle=60
                           )


session_factory = sessionmaker(bind=engine, autoflush=True)
Session = scoped_session(session_factory)
Base = declarative_base()


def sort_by_nom_in_l(data):
    row = {}
    for i in data:
        if i.mashin.nom_in_l in row:
            row[i.mashin.nom_in_l].old_enter = min([row[i.mashin.nom_in_l].old_enter, i.old_enter])
            row[i.mashin.nom_in_l].new_enter = max([row[i.mashin.nom_in_l].new_enter, i.new_enter])

            row[i.mashin.nom_in_l].old_exit = min([row[i.mashin.nom_in_l].old_exit, i.old_exit])
            row[i.mashin.nom_in_l].new_exit = max([row[i.mashin.nom_in_l].new_exit, i.new_exit])

            row[i.mashin.nom_in_l].bill_old = min([row[i.mashin.nom_in_l].bill_old, i.bill_old])
            row[i.mashin.nom_in_l].bill_new = max([row[i.mashin.nom_in_l].bill_new, i.bill_new])

        else:
            row[i.mashin.nom_in_l] = i
    data = []
    for i in sorted(list(row.keys())):
        data.append(row[i])
    data.reverse()
    return data


class Alembic(Base):
    __tablename__ = 'alembic_version'
    version_num = Column(String(32), nullable=False, primary_key=True)


class LN(Base):
    __tablename__ = 'lns'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    value = Column(Text, nullable=False)
    signature = Column(Text, nullable=False)

    # activ = Column(Boolean, nullable=False, unique=False, server_default='False')
    # activ_time = Column(DateTime, nullable=True)

    def __repr__(self):
        return self.name

    def to_json(self):
        self.value = json.dumps(self.value)
        return True

    def from_json(self):
        return json.loads(self.value)



class Config(Base):
    __tablename__ = 'config'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    value = Column(Text, nullable=True)

    def to_json(self):
        self.value = json.dumps(self.value)
        return True

    def from_json(self):
        return json.loads(self.value)



# class Right(Base):
#     __tablename__ = 'rights'
#     id = Column(Integer, primary_key=True)
#     mod_name = Column(String(100), nullable=False, unique=False)
#     option = Column(String(100), nullable=False, unique=True)
#
#     #     language = Column(String(100), nullable=False, unique=False)
#
#     def __unicode__(self):
#         return self.mod_name


class Model(Base):
    __tablename__ = 'mashin_model'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    def __unicode__(self):
        return self.name


class Flor(Base):
    __tablename__ = 'casino_flor'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    def __repr__(self):
        return self.name


class UserGrup(Base):
    __tablename__ = 'user_grup'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    right = Column(Text, nullable=True)
    default_use = Column(Boolean, nullable=False, unique=False, server_default='False')
    auto_mail = Column(Boolean, nullable=False, unique=False, server_default='False')
    rko_auto_mail = Column(Boolean, nullable=False, unique=False, server_default='False')
    bill_disable = Column(Boolean, nullable=False, unique=False, server_default='False')
    get_all_bill = Column(Boolean, nullable=False, unique=False, server_default='False')
    # add_bonus_hold = Column(Boolean, nullable=False, unique=False, server_default='False')
    boss_mail = Column(Text, nullable=False, unique=False, server_default='')
    service_mail = Column(Text, nullable=False, unique=False, server_default='')
    subject = Column(String(100), nullable=False, unique=False, server_default='')

    def __repr__(self):
        return self.name

    def to_json(self):
        self.right = json.dumps(self.right)
        return True

    def from_json(self):
        return json.loads(self.right)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    passwd = Column(String(100), nullable=False, unique=False)
    cart = Column(String(100), nullable=True, unique=True, index=True)
    cart_block_9 = Column(String(100), nullable=True, unique=False, index=True)
    grup_id = Column(Integer, ForeignKey(UserGrup.id), nullable=False)
    grup = relationship(UserGrup, backref="grups", lazy='joined')
    enable = Column(Boolean, nullable=False, unique=False, default=True)
    flor_id = Column(Integer, ForeignKey('casino_flor.id'), nullable=True, unique=False)
    flor = relationship('Flor', backref="my_flor")
    # kasa_id = Column(Integer, ForeignKey('kasa.id'), nullable=False, unique=True)
    kasa = Column(Float, server_default="0")
    login = Column(Boolean, nullable=True, unique=False, default=False)
    lipsi = Column(Float, server_default="0")

    #     kasa_id = Column(Integer, ForeignKey(Kasa.id), nullable=True)
    #     kasa = relationship(Kasa, foreign_keys=kasa_id, backref="users_kasa")

    def __unicode__(self):
        return self.name


class KasaTransfer(Base):
    __tablename__ = 'users_transfer_casa'
    id = Column(Integer, primary_key=True)

    from_user_id = Column(Integer, ForeignKey(User.id), nullable=False, unique=False)
    from_user = relationship(User, foreign_keys=[from_user_id], backref="from_user_id", lazy='joined')

    to_user_id = Column(Integer, ForeignKey(User.id), nullable=False, unique=False)
    to_user = relationship(User, foreign_keys=[to_user_id], backref="to_user_id", lazy='joined')

    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    mony = Column(Float, nullable=False, default=0)
    reson = Column(Integer, nullable=False, default=0)
    info = Column(Text, nullable=True)
    chk = Column(Boolean, nullable=False, unique=False, server_default="True")
    chk_to = Column(Boolean, nullable=False, unique=False, server_default="True")


class Maker(Base):
    __tablename__ = 'mashin_maker'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    def __unicode__(self):
        return self.name


class Device(Base):
    __tablename__ = 'mashin'
    id = Column(Integer, primary_key=True)
    serial = Column(String(100), nullable=False, unique=True, index=True)
    nom_in_l = Column(Integer, nullable=False, index=True)
    by_hend_order = Column(Boolean, nullable=True, unique=False, default=False)

    model_id = Column(Integer, ForeignKey('mashin_model.id'), nullable=False)
    model = relationship("Model", backref="models", lazy='joined')

    el_in = Column(BigInteger, nullable=False)
    el_out = Column(BigInteger, nullable=False)
    mex_in = Column(Integer, nullable=False)
    mex_out = Column(Integer, nullable=False)

    won = Column(BigInteger, nullable=False, default=0)
    bet = Column(BigInteger, nullable=False, default=0)

    mex_coef = Column(Float, nullable=False)
    el_coef = Column(Float, nullable=False)

    bill = Column(Integer, nullable=False)

    enable = Column(Boolean, nullable=False, unique=False, default=True)
    # aft_enable = Column(Boolean, nullable=False, unique=False, default=False)

    flor_id = Column(Integer, ForeignKey('casino_flor.id'), nullable=False)
    flor = relationship("Flor", backref="flors", lazy='joined')

    maker_id = Column(Integer, ForeignKey('mashin_maker.id'), nullable=False)
    maker = relationship("Maker", backref="makers", lazy='joined')

    sas = Column(Boolean, nullable=False, unique=False, default=True)

    ip = Column(String(100), unique=False, nullable=True)
    smib_uuid = Column(String(100), unique=False, nullable=True)
    smib_version = Column(String(100), unique=False, nullable=True)
    bill_in_device = Column(Float, nullable=False, default=0)

    mk_revert = Column(Boolean, nullable=False, unique=False, default=False)

    def __unicode__(self):
        return self.serial


class PrihodType(Base):
    __tablename__ = 'prihod_type'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    hiden = Column(Boolean, nullable=False, server_default='False')

    def __unicode__(self):
        return self.name


class RazhodType(Base):
    __tablename__ = 'razhod_type'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    hiden = Column(Boolean, nullable=False, server_default='False')

    def __unicode__(self):
        return self.name


class Prihod(Base):
    __tablename__ = 'prihod'
    id = Column(Integer, primary_key=True)
    mony = Column(Float, nullable=False, default=0)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship(User, foreign_keys=user_id, backref="users_prihod")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    #     times = Column(Time, nullable=False, default=datetime.datetime.now)
    reson_id = Column(Integer, ForeignKey('prihod_type.id'), nullable=False)
    reson = relationship("PrihodType", backref="resons")
    info = Column(String(250), nullable=True)
    last_edit_time = Column(DateTime, nullable=True)
    #     last_edit_time = Column(Time, nullable=True)
    last_edit_by_id = Column(Integer, ForeignKey(User.id), nullable=True)
    last_edit_by = relationship(User, foreign_keys=last_edit_by_id, backref="prihod_edit_by")
    old_data = Column(Text, nullable=True, unique=False)
    chk = Column(Boolean, nullable=False, default=False)


class Razhod(Base):
    __tablename__ = 'razhod'
    id = Column(Integer, primary_key=True)
    mony = Column(Float, nullable=False, default=0)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship(User, foreign_keys=user_id, backref="users_razhod")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    #     times = Column(Time, nullable=False, default=datetime.datetime.now)
    reson_id = Column(Integer, ForeignKey('razhod_type.id'), nullable=False)
    reson = relationship("RazhodType", backref="resons")
    info = Column(String(250), nullable=True)
    last_edit_time = Column(DateTime, nullable=True)
    #     last_edit_time = Column(Time, nullable=True)
    last_edit_by_id = Column(Integer, ForeignKey(User.id), nullable=True)
    last_edit_by = relationship(User, foreign_keys=last_edit_by_id, backref="razhod_edit_by")
    old_data = Column(Text, nullable=True, unique=False)
    chk = Column(Boolean, nullable=False, default=False)

    def __unicode__(self):
        return self.info


class Lipsi(Base):
    __tablename__ = 'lipsi'
    id = Column(Integer, primary_key=True)
    mony = Column(Float, nullable=False, default=0)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship(User, foreign_keys=user_id, backref="users_lipsi")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    chk = Column(Boolean, nullable=False, default=False, server_default='True')
    if_lipsa = Column(Boolean, nullable=True, default=True)
    #     times = Column(Time, nullable=False, default=datetime.datetime.now)

    def __unicode__(self):
        return self.mony


class BosGetMony(Base):
    __tablename__ = 'boss_get_mony'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship(User, backref='boss_transfer_user')
    mony = Column(Float, nullable=False)
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    flor_id = Column(Integer, ForeignKey(Flor.id), nullable=True)


# flor =relationship(Flor, backref='boss_get_from_flor')
#     to_flor_id = Column(Integer, ForeignKey(Flor.id), nullable=True)
#     kasa_mpny = Column(Float, nullable=True)
#     user_to_id = Column(Integer, ForeignKey(User.id), nullable=True)
#     user_to = relationship(User, backref='boss_transfer_user')
#     get_pub_time = Column(DateTime, nullable=True)

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    mashin_id = Column(Integer, ForeignKey(Device.id), nullable=False)
    mashin = relationship(Device, foreign_keys=mashin_id, backref="mashin_order")
    #     mashin_nom_in_l = Column(Integer, nullable=False, default=0)

    flor_id = Column(Integer, ForeignKey(Flor.id), nullable=False)
    #     flor =  relationship(Flor, foreign_keys=flor_id, backref="work_onflors")
    old_bet = Column(BigInteger, nullable=False, default=0)
    new_bet = Column(BigInteger, nullable=False, default=0)

    old_won = Column(BigInteger, nullable=False, default=0)
    new_won = Column(BigInteger, nullable=False, default=0)

    old_enter = Column(BigInteger, nullable=False)
    old_exit = Column(BigInteger, nullable=False)

    new_enter = Column(BigInteger, nullable=False)
    new_exit = Column(BigInteger, nullable=False)

    mex_old_enter = Column(Integer, nullable=False)
    mex_old_exit = Column(Integer, nullable=False)

    mex_new_enter = Column(Integer, nullable=False)
    mex_new_exit = Column(Integer, nullable=False)

    bill_old = Column(Integer, nullable=False)
    bill_new = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship(User, foreign_keys=user_id, backref="order_users")

    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    #     pub_time = Column(Time, nullable=False, default=datetime.datetime.now)
    chk = Column(Boolean, nullable=False, default=False)

    #     in_doc_from_date = Column(String(100), nullable=True, unique=False)

    last_edit_by_id = Column(Integer, ForeignKey(User.id), nullable=True)
    last_edit_by = relationship(User, foreign_keys=last_edit_by_id, backref="edit_by")
    last_edit_time = Column(DateTime, nullable=True)
    #     last_edit_time = Column(Time, nullable=True)
    old_data = Column(Text, nullable=True, unique=False)


class BillTake(Base):
    __tablename__ = 'bill_take'
    id = Column(Integer, primary_key=True)
    mashin_id = Column(Integer, ForeignKey(Device.id), nullable=False)
    mashin = relationship(Device, foreign_keys=mashin_id, backref="mashin_bill_get")
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship(User, foreign_keys=user_id, backref="user_get_bill")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    #     pub_time = Column(Time, nullable=False, default=datetime.datetime.now)
    mony = Column(Integer, nullable=False)
    chk = Column(Boolean, nullable=False, default=False)


class Sity(Base):
    __tablename__ = 'sity'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)


class GetCounterError(Base):
    __tablename__ = 'get_counter_error'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=True)
    user = relationship(User, foreign_keys=user_id, backref="user_get_bill_error")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    #     pub_time = Column(Time, nullable=False, default=datetime.datetime.now)
    mashin_nom_in_l = Column(Integer, nullable=True)
    info = Column(Text, nullable=False, unique=False)


class MonyRKO(Base):
    __tablename__ = 'rko'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship(User, foreign_keys=user_id, backref="users_rko")
    total = Column(Float, nullable=False, unique=False)
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    #     times = Column(Time, nullable=False, default=datetime.datetime.now)
    rko_data = Column(Text, nullable=True, unique=False)

    def to_json(self):
        self.rko_data = json.dumps(self.rko_data)
        return True

    def from_json(self):
        return json.loads(self.rko_data)


class DayReport(Base):
    __tablename__ = 'day_report'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship(User, foreign_keys=user_id, backref="users_day_report")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    #     times = Column(Time, nullable=False, default=datetime.datetime.now)
    doc_data = Column(Text, nullable=True, unique=False)
    day_report = Column(Boolean, nullable=False, default=True)
    doc_nom = Column(Integer, index=True, nullable=False)

    def to_json(self):
        self.doc_data = json.dumps(self.doc_data)
        return True

    def from_json(self):
        return json.loads(self.doc_data)

class BonusCart(Base):
    __tablename__ = 'bonus_cart'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    pub_user_id = Column(Integer, ForeignKey(User.id), nullable=True)
    bub_user = relationship(User, foreign_keys=pub_user_id, backref="users_add_cart")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    mony = Column(Float, nullable=False, unique=False)
    cart = Column(String(100), nullable=False, unique=True, index=True)
    cart_type = Column(String(100), nullable=False, unique=False)
    active = Column(Boolean, nullable=False, default=True)
    no_bonus_out_befor = Column(Integer, nullable=False, unique=False, server_default='1')
    must_have_cust = Column(Boolean, nullable=True, default=False)





# class BonusInLog(Base):
#     __tablename__ = 'bonus_in_log'
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey(User.id), nullable=True)
#     user = relationship(User, foreign_keys=user_id, backref="users_dset_bonus_in")
#     mashin_id = Column(Integer, ForeignKey(Device.id), nullable=False)
#     mashin = relationship(Device, foreign_keys=mashin_id, backref="mashin_in_bonus_device")
#     pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
#     mony = Column(Float, nullable=False, unique=False)
#     # chk = Column(Boolean, nullable=False, unique=False, default=False)


class StartWork(Base):
    __tablename__ = 'user_start_work'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship(User, foreign_keys=user_id, backref="users_start_work")
    start = Column(Boolean, nullable=False, unique=False, server_default='False')
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    end_time = Column(DateTime, nullable=True)

class MonyOrder(Base):
    __tablename__ = 'mony_order'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship(User, foreign_keys=user_id, backref="users_mony_order")
    data = Column(Text, nullable=False)
    total = Column(Float, default=0)
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)

class CustGrup(Base):
    __tablename__ = 'Cust_grup'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    enable = Column(Boolean, nullable=False, unique=False, default=True)
    selected = Column(Boolean, nullable=False, unique=False, server_default='False')

    mony_back_use = Column(Boolean, nullable=False, unique=False, default=False)
    mony_back_pr = Column(Float, nullable=True, unique=False)
    mony_back_pay = Column(Integer, nullable=True, unique=False, default=0)
    mony_back_min_pay = Column(Integer, nullable=True, unique=False, server_default='0')

    tombola_use = Column(Boolean, nullable=False, unique=False, default=False)
    tombola_on_in = Column(Boolean, nullable=False, unique=False, default=False)
    tombola_coef = Column(Float, nullable=True, unique=False)

    bonus_hold = Column(Boolean, nullable=False, unique=False, server_default='False')
    bonus_use = Column(Boolean, nullable=False, unique=False, default=False)
    bonus_direct = Column(Boolean, nullable=True, unique=False, default=False)
    bonus_by_in = Column(Boolean, nullable=False, unique=False, default=False)
    bonus_one_per_day = Column(Boolean, nullable=False, unique=False, default=False)
    bonus_on_mony = Column(Float, nullable=False, unique=False, default=False)
    # bonus_if_lost = Column(Boolean, nullable=False, unique=False, default=False)
    bonus_waith_for_in = Column(Boolean, nullable=False, unique=False, default=False)
    no_out_befor = Column(Integer, nullable=False, server_default='1')
    #     bonus_row = Column(Integer, index=False, nullable=False, default=3, unique=False)
    bonus_row = Column(Text, nullable=False, server_default='')
    # x2 = Column(Boolean, nullable=False, server_default='False')
    # bonus_row_1_mony = Column(Float, nullable=False, unique=False, default=5)
    # bonus_row_1_count = Column(Float, nullable=False, unique=False, default=3)
    # bonus_row_2_mony = Column(Float, nullable=False, unique=False, default=10)
    # bonus_row_2_count = Column(Float, nullable=False, unique=False, default=3)
    # bonus_row_3_mony = Column(Float, nullable=False, unique=False, default=20)
    # bonus_row_3_count = Column(Float, nullable=False, unique=False, default=2)
    # bonus_row_4_mony = Column(Float, nullable=False, unique=False, default=50)
    # bonus_row_4_count = Column(Float, nullable=False, unique=False, default=1)
    pub_user_id = Column(Integer, ForeignKey(User.id), nullable=True)
    bonus_on_day = Column(Text, nullable=False, server_default='')
    bub_user = relationship(User, foreign_keys=pub_user_id, backref="users_add_cust_group")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    bonus_warning_use = Column(Boolean, nullable=False, server_default='False')
    bonus_warning_mony = Column(Float, nullable=False, unique=False, server_default='100')
    bonus_revert_by_bet = Column(Boolean, nullable=False, server_default='False')
    one_day_back_total = Column(Boolean, nullable=False, server_default='False')
    month_back = Column(Boolean, nullable=False, server_default='False')
    restricted_bonus = Column(Boolean, nullable=False, server_default='False')

    use_total_procent = Column(Boolean, nullable=False, server_default='False')
    total_procent = Column(Integer, nullable=False, unique=False, server_default='1')
    more_than_one_from_redirect = Column(Boolean, nullable=False, server_default='False')
    bonus_in_mony = Column(Boolean, nullable=False, server_default='False')
    bonus_in_mony_sum = Column(Integer, nullable=False, unique=False, server_default='1')
    region_id = Column(Integer, nullable=True, unique=False)
    bonus_waith_for_in_mony = Column(Integer, nullable=False, server_default='0')
    bonus_if_man = Column(Boolean, nullable=True)
    # bonus_count = Column(Integer, nullable=False, unique=False, server_default='1')
    # up_bonus_with = Column(Integer, nullable=False, unique=False, server_default='5')
    # up_on_mony_with = Column(Integer, nullable=False, unique=False, server_default='5')


class CustUser(Base):
    __tablename__ = 'Cust_user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    pin = Column(String(100), nullable=True, unique=False)
    curent_mony = Column(Float, nullable=False, unique=False, default=0)
    e_mail = Column(String(200), nullable=True, unique=False)
    tel = Column(String(100), nullable=True, unique=False)
    personal_cart_id = Column(String(100), nullable=False, unique=True)
    country_code = Column(String(6), nullable=False, unique=False, server_default='BGR')
    personal_cart_valid = Column(DateTime, nullable=True)
    personal_egn = Column(String(100), nullable=False, unique=True)
    personal_addres = Column(Text, nullable=True, unique=False)
    persona_sity_id = Column(Integer, ForeignKey(Sity.id), nullable=True)
    persona_sity = relationship(Sity, backref="cust_personal_sity", lazy='joined')
    forbiden = Column(Boolean, nullable=False, unique=False, default=True)
    use_group_conf = Column(Boolean, nullable=False, unique=False, default=True)

    mony_back_use = Column(Boolean, nullable=False, unique=False, default=False)
    mony_back_pr = Column(Float, nullable=True, unique=False)
    mony_back_pay = Column(Integer, nullable=True, unique=False, default=0)
    mony_back_min_pay = Column(Integer, nullable=True, unique=False, server_default='0')

    tombola_use = Column(Boolean, nullable=False, unique=False, default=False)
    tombola_coef = Column(Float, nullable=True, unique=False)
    tombola_on_in = Column(Boolean, nullable=False, unique=False, default=False)

    bonus_use = Column(Boolean, nullable=False, unique=False, default=False)
    bonus_direct = Column(Boolean, nullable=True, unique=False, default=False)
    bonus_waith_for_in = Column(Boolean, nullable=False, unique=False, default=False)
    bonus_by_in = Column(Boolean, nullable=False, unique=False, default=False)
    bonus_one_per_day = Column(Boolean, nullable=False, unique=False, default=False)
    bonus_on_mony = Column(Float, nullable=False, unique=False, default=False)
    # bonus_if_lost = Column(Boolean, nullable=False, unique=False, default=False)

    #     bonus_row = Column(Integer, index=False, nullable=False, default=3, unique=False)
    bonus_hold = Column(Boolean, nullable=False, unique=False, server_default='False')
    no_out_befor = Column(Integer, nullable=False, server_default='1')
    bonus_row = Column(Text, nullable=False, server_default='')
    in_nra = Column(Boolean, nullable=False, server_default='False')
    # bonus_row_1_mony = Column(Float, nullable=False, unique=False, default=5)
    # bonus_row_1_count = Column(Float, nullable=False, unique=False, default=4)
    # bonus_row_2_mony = Column(Float, nullable=False, unique=False, default=10)
    # bonus_row_2_count = Column(Float, nullable=False, unique=False, default=3)
    # bonus_row_3_mony = Column(Float, nullable=False, unique=False, default=20)
    # bonus_row_3_count = Column(Float, nullable=False, unique=False, default=2)
    # bonus_row_4_mony = Column(Float, nullable=False, unique=False, default=50)
    # bonus_row_4_count = Column(Float, nullable=False, unique=False, default=1)
    grup_id = Column(Integer, ForeignKey(CustGrup.id), nullable=False)
    bonus_on_day = Column(Text, nullable=False, server_default='')
    grup = relationship(CustGrup, backref="cust_grups", lazy='joined')
    #     total_in = Column(Float, nullable=False, unique=False, default=0)
    #     total_won = Column(Float, nullable=False, unique=False, default=0)
    #     total_out = Column(Float, nullable=False, unique=False, default=0)
    #     total_bill = Column(Float, nullable=False, unique=False, default=0)
    #     total_game = Column(Float, nullable=False, unique=False, default=0)
    total_bonus = Column(Float, nullable=False, unique=False, default=0)
    total_mony_back = Column(Float, nullable=False, unique=False, default=0)
    total_tombula = Column(Float, nullable=False, unique=False, default=0)
    pub_user_id = Column(Integer, ForeignKey(User.id), nullable=True)
    pub_user = relationship(User, foreign_keys=pub_user_id, backref="users_add_cust")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    bonus_warning_use = Column(Boolean, nullable=False, server_default='False')
    bonus_warning_mony = Column(Float, nullable=False, unique=False, server_default='100')
    bonus_revert_by_bet = Column(Boolean, nullable=False, server_default='False')
    one_day_back_total = Column(Boolean, nullable=False, server_default='False')
    month_back = Column(Boolean, nullable=False, server_default='False')
    restricted_bonus = Column(Boolean, nullable=False, server_default='False')

    use_total_procent = Column(Boolean, nullable=False, server_default='False')
    total_procent = Column(Integer, nullable=False, unique=False, server_default='1')
    more_than_one_from_redirect = Column(Boolean, nullable=False, server_default='False')
    bonus_in_mony = Column(Boolean, nullable=False, server_default='False')
    bonus_in_mony_sum = Column(Integer, nullable=False, unique=False, server_default='1')
    region_id = Column(Integer, nullable=True, unique=False)
    bonus_waith_for_in_mony = Column(Integer, nullable=False, server_default='0')
    man = Column(Boolean, nullable=True)
    bonus_if_man = Column(Boolean, nullable=True)
    # bonus_count = Column(Integer, nullable=False, unique=False, server_default='1')
    # up_bonus_with = Column(Integer, nullable=False, unique=False, server_default='5')
    # up_on_mony_with = Column(Integer, nullable=False, unique=False, server_default='5')


class CustCart(Base):
    __tablename__ = 'Cust_cart'
    id = Column(Integer, primary_key=True)
    catr_id = Column(String(100), nullable=False, unique=True, index=True)
    user_id = Column(Integer, ForeignKey(CustUser.id), nullable=True, unique=False)
    user = relationship(CustUser, foreign_keys=[user_id], backref="user_cart", lazy='joined')
    pub_user_id = Column(Integer, ForeignKey(User.id), nullable=True, unique=False)
    pub_user = relationship(User, foreign_keys=[pub_user_id], backref="users_add_cust_cart", lazy='joined')
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)


class CustStatistic(Base):
    __tablename__ = 'Cust_statistic'
    id = Column(Integer, primary_key=True)
    out = Column(Float, nullable=False, unique=False, default=False)
    bill = Column(Float, nullable=False, unique=False, default=False)
    ins = Column(Float, nullable=False, unique=False, default=0)
    won = Column(Float, nullable=False, unique=False, default=0)
    bet = Column(Float, nullable=False, unique=False, default=0)
    total_mony_back = Column(Float, nullable=False, unique=False, default=0)
    curent_credit = Column(Float, nullable=False, unique=False, default=0)
    curent_credit_on_in = Column(Float, nullable=False, unique=False, server_default='0')
    total_tombula = Column(Float, nullable=False, unique=False, default=0)
    bonus_mony = Column(Float, nullable=False, unique=False, default=0)
    game_played = Column(Integer, nullable=False, unique=False, default=0)
    cust_id = Column(Integer, ForeignKey(CustUser.id), nullable=True, unique=False)
    cust = relationship(CustUser, foreign_keys=[cust_id], backref="cust")
    device_id = Column(Integer, ForeignKey(Device.id), nullable=True, unique=False)
    device = relationship(Device, foreign_keys=device_id, backref="device")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    come_on_emg_time = Column(DateTime, nullable=True)

class BonusCartLog(Base):
    __tablename__ = 'bonus_cart_log'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=True)
    user = relationship(User, foreign_keys=user_id, backref="users_dset_bonus_cart")
    mashin_id = Column(Integer, ForeignKey(Device.id), nullable=False)
    mashin = relationship(Device, foreign_keys=mashin_id, backref="mashin_init_bonus_cart")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    cart_id = Column(Integer, ForeignKey(BonusCart.id), nullable=False)
    cart = relationship(BonusCart, foreign_keys=cart_id, backref="cart_info")
    mony = Column(Float, nullable=False, unique=False)
    credit = Column(Float, nullable=True, unique=False, server_default='0')
    bonus = Column(Float, nullable=False, unique=False)
    bonus_hold = Column(Boolean, nullable=False, unique=False, default=False)
    cust_id = Column(Integer, ForeignKey(CustUser.id), nullable=True)
    cust = relationship(CustUser, foreign_keys=cust_id, backref="cust_get_dset_bonus_cart")
    chk = Column(Boolean, nullable=False, unique=False, default=False)

class MonuBackPay(Base):
    __tablename__ = 'Cust_monyback_pay'
    id = Column(Integer, primary_key=True)
    mony = Column(Float, nullable=False, unique=False, default=0)
    cust_id = Column(Integer, ForeignKey(CustUser.id), nullable=False, unique=False)
    cust = relationship(CustUser, foreign_keys=[cust_id], backref="cust_get_monyback")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    pub_user_id = Column(Integer, ForeignKey(User.id), nullable=True, unique=False)
    pub_user = relationship(User, foreign_keys=[pub_user_id], backref="users_pay_monyback_to_cust")
    chk = Column(Boolean, nullable=True, unique=False, default=False)


class BonusPay(Base):
    __tablename__ = 'Cust_bonus'
    id = Column(Integer, primary_key=True)
    mony = Column(Float, nullable=False, unique=False, default=0)
    cust_id = Column(Integer, ForeignKey(CustUser.id), nullable=False, unique=False)
    cust = relationship(CustUser, foreign_keys=[cust_id], backref="cust_get_bonus")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    device_id = Column(Integer, ForeignKey(Device.id), nullable=True, unique=False)
    device = relationship(Device, foreign_keys=device_id, backref="device_bonus")
    activ = Column(Boolean, nullable=False, unique=False, default=True)
    last = Column(Boolean, nullable=False, unique=False, default=True)
    use_it = Column(Boolean, nullable=False, unique=False, server_default='True')
    initial_on_device_id = Column(Integer, ForeignKey(Device.id), nullable=True, unique=False)
    initial_on_device = relationship(Device, foreign_keys=initial_on_device_id, backref="initial_on_device_bonus")
    initial_pub_time = Column(DateTime, nullable=True)
    from_in = Column(Boolean, nullable=False, unique=False, server_default='False')
    user_id = Column(Integer, ForeignKey(User.id), nullable=True, unique=False)
    chk = Column(Boolean, nullable=True, unique=False, default=False)
    from_redirect = Column(Boolean, nullable=False, unique=False, server_default='False')
    from_redirect_name = Column(String(100), nullable=True, unique=False)


class TombulaPrinted(Base):
    __tablename__ = 'Cust_tpombula_printed'
    id = Column(Integer, primary_key=True)
    tombula_count = Column(Integer, nullable=False, unique=False, default=0)
    cust_id = Column(Integer, ForeignKey(CustUser.id), nullable=False, unique=False)
    cust = relationship(CustUser, foreign_keys=[cust_id], backref="cust_print_tombula")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    pub_user_id = Column(Integer, ForeignKey(User.id), nullable=False, unique=False)
    pub_user = relationship(User, foreign_keys=[pub_user_id], backref="users_print_tombula_to_cust")

class PointInMonyPrinted(Base):
    __tablename__ = 'Cust_point_printed'
    id = Column(Integer, primary_key=True)
    point_sum = Column(Float, nullable=False, unique=False, default=0)
    cust_id = Column(Integer, ForeignKey(CustUser.id), nullable=False, unique=False)
    cust = relationship(CustUser, foreign_keys=[cust_id], backref="cust_print_point")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    pub_user_id = Column(Integer, ForeignKey(User.id), nullable=False, unique=False)
    pub_user = relationship(User, foreign_keys=[pub_user_id], backref="users_print_point_to_cust")

class CashOutPrinted(Base):
    __tablename__ = 'Cust_rko_printed'
    id = Column(Integer, primary_key=True)
    mony = Column(Float, nullable=False, unique=False, default=0)
    cust_id = Column(Integer, ForeignKey(CustUser.id), nullable=True, unique=False)
    cust = relationship(CustUser, foreign_keys=[cust_id], backref="cust_print_rko")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    pub_user_id = Column(Integer, ForeignKey(User.id), nullable=False, unique=False)
    pub_user = relationship(User, foreign_keys=[pub_user_id], backref="users_print_rko_to_cust")

class MonyOnCart(Base):
    __tablename__ = 'Cust_mony_on_cart'
    id = Column(Integer, primary_key=True)
    cust_id = Column(Integer, ForeignKey(CustUser.id), nullable=False, unique=False)
    cust = relationship(CustUser, foreign_keys=[cust_id], backref="cust_change_mony_on_cart")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    pub_user_id = Column(Integer, ForeignKey(User.id), nullable=False, unique=False)
    pub_user = relationship(User, foreign_keys=[pub_user_id], backref="users_change_mony_on_cart")
    mony = Column(Float, nullable=False, unique=False, default=0)
    out = Column(Boolean, nullable=False, unique=False)
    chk = Column(Boolean, nullable=True, unique=False, default=False)


class CustInOutAFT(Base):
    __tablename__ = 'Cust_in_out_aft'
    id = Column(Integer, primary_key=True)
    cust_id = Column(Integer, ForeignKey(CustUser.id), nullable=False, unique=False)
    cust = relationship(CustUser, foreign_keys=[cust_id], backref="cust_in_out_aft")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    mony = Column(Float, nullable=False, unique=False, default=0)
    out = Column(Boolean, nullable=False, unique=False)
    chk = Column(Boolean, nullable=False, unique=False, default=False)
    device_id = Column(Integer, ForeignKey(Device.id), nullable=False, unique=False)
    device = relationship(Device, foreign_keys=device_id, backref="device_in_out_aft")
    user_id = Column(Integer, ForeignKey(User.id), nullable=True, unique=False)
    user = relationship(User, foreign_keys=user_id, backref="device_in_out_aft_user")


class Log(Base):
    __tablename__ = 'system_log'
    id = Column(Integer, primary_key=True)
    asctime = Column(DateTime, nullable=False)
    level = Column(String(100), nullable=False, unique=False)
    name = Column(String(200), nullable=False, unique=False)
    proces_name = Column(String(200), nullable=False, unique=False)
    func_name = Column(String(200), nullable=False, unique=False)
    lineno = Column(String(200), nullable=False, unique=False)
    # msg = Column(String(200), nullable=False, unique=False)
    msg_text = Column(Text, nullable=False, unique=False, server_default='')
    device_id = Column(Integer, ForeignKey(Device.id), nullable=True, unique=False)
    device = relationship(Device, foreign_keys=device_id, backref="device_log")
    text = Column(Text, nullable=True, unique=False)
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)

class ClienBonusHold(Base):
    __tablename__ = 'client_bonus_hold'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=True)
    user = relationship(User, foreign_keys=user_id, backref="users_dset_cust_bonus_cart")
    mashin_id = Column(Integer, ForeignKey(Device.id), nullable=False)
    mashin = relationship(Device, foreign_keys=mashin_id, backref="mashin_init_cust_bonus_cart")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    cart_id = Column(Integer, ForeignKey(CustUser.id), nullable=False)
    cart = relationship(CustUser, foreign_keys=cart_id, backref="bonus_info")
    mony = Column(Float, nullable=False, unique=False)
    credit = Column(Float, nullable=True, unique=False, server_default='0')
    bonus = Column(Float, nullable=False, unique=False)
    bonus_hold = Column(Boolean, nullable=False, unique=False, default=True)
    chk = Column(Boolean, nullable=False, unique=False, default=False)


class RamClear(Base):
    __tablename__ = 'emg_ram_clear'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship(User, foreign_keys=user_id, backref="user_emg_ram_clear")
    mashin_id = Column(Integer, ForeignKey(Device.id), nullable=False)
    mashin = relationship(Device, foreign_keys=mashin_id, backref="mashin_emg_ram_clear")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    el_in = Column(Integer, nullable=False)
    el_out = Column(Integer, nullable=False)
    mex_in = Column(Integer, nullable=False)
    mex_out = Column(Integer, nullable=False)
    bill = Column(Integer, nullable=False)
    chk = Column(Boolean, nullable=False, unique=False, default=False)

class EMGService(Base):
    __tablename__ = 'emg_service'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship(User, foreign_keys=user_id, backref="user_emg_service")
    mashin_id = Column(Integer, ForeignKey(Device.id), nullable=True)
    mashin = relationship(Device, foreign_keys=mashin_id, backref="mashin_emg_service")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    info = Column(Text, nullable=False, server_default='')
    fix_info = Column(Text, nullable=False, server_default='')
    part_mony = Column(Float, nullable=True, unique=False, server_default='0')
    is_ram_clear = Column(Boolean, nullable=False, unique=False, server_default='False')
    is_fix = Column(Boolean, nullable=False, unique=False, server_default='False')
    user_fix_id = Column(Integer, ForeignKey(User.id), nullable=True)
    user_fix = relationship(User, foreign_keys=user_fix_id, backref="user_fix_emg_service")
    fix_time = Column(DateTime, nullable=True)
    ramclear_id = Column(Integer, ForeignKey(RamClear.id), nullable=True)
    ram_clear = relationship(RamClear, foreign_keys=ramclear_id, backref="ramclear_fix_emg_service")

class BankTransfer(Base):
    __tablename__ = 'bank_transfer'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=True)
    user = relationship(User, foreign_keys=user_id, backref="user_make_bank_transfer")
    cust_id = Column(Integer, ForeignKey(CustUser.id), nullable=True)
    cust = relationship(CustUser, foreign_keys=cust_id, backref="cust_make_bank_transfer")
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    mony = Column(Float, nullable=False, unique=False)
    chk = Column(Boolean, nullable=False, unique=False, default=False)

class InOut(Base):
    __tablename__ = 'in_out'
    id = Column(Integer, primary_key=True)
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    mony = Column(Float, nullable=False, unique=False, default=0)
    out = Column(Boolean, nullable=False, unique=False)
    bill = Column(Boolean, nullable=False, unique=False)
    device_id = Column(Integer, ForeignKey(Device.id), nullable=False, unique=False)
    device = relationship(Device, foreign_keys=device_id, backref="device_in_out")
    player_id = Column(Integer, ForeignKey(CustUser.id), nullable=True)
    player = relationship(CustUser, foreign_keys=player_id, backref="player_make_in_out")
    user_id = Column(Integer, ForeignKey(User.id), nullable=True, unique=False)
    user = relationship(User, foreign_keys=user_id, backref="device_in_out_user")

class UserHaveMony(Base):
    __tablename__ = 'usert_have_mony'
    id = Column(Integer, primary_key=True)
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    mony = Column(Float, nullable=False, unique=False, default=0)
    user_id = Column(Integer, ForeignKey(User.id), nullable=True)
    user = relationship(User, foreign_keys=user_id, backref="user_have_mony_befor_order")

class CartPrise(Base):
    __tablename__ = 'cart_price'
    id = Column(Integer, primary_key=True, index=True)
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship(User, foreign_keys=user_id, backref="user_cust_cart_price")
    mony = Column(Float, nullable=False, unique=False)
    chk = Column(Boolean, nullable=False, unique=False, default=False)

class EGNCheck(Base):
    __tablename__ = 'chk_egn'
    id = Column(Integer, primary_key=True, index=True)
    pub_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    user_id = Column(Integer, ForeignKey(User.id), nullable=True)
    user = relationship(User, foreign_keys=user_id, backref="user_chk_egn")
    by_hand = Column(Boolean, nullable=False, unique=False, default=False)
    player_id = Column(Integer, ForeignKey(CustUser.id), nullable=True)
    player = relationship(CustUser, foreign_keys=player_id, backref="player_egn_chek")
    egn = Column(Text, nullable=False, default='')


class DBCtrl():

    def __init__(self, my_session=False):
        if my_session == False:
            global Session
            self.session = Session()
        else:
            global session_factory
            my_session = scoped_session(session_factory)
            self.session = my_session()

    def dispose(self):
        self.session.close()
        engine.dispose()

    def expire(self, obj=None):
        if obj == None:
            self.session.expire_all()
        else:
            self.session.expire(obj)

    def del_all_table(self, name):
        return self.session.execute('''TRUNCATE TABLE %s''' % (name))

    def open(self):
        self.session = Session()

    def close(self):
        Session.remove()

    def make_obj(self, models_class):
        obj = models_class()
        return obj

    def commit(self):
        try:
            self.session.commit()
            return True
        except Exception as e:
            raise e
        return False

    def rollback(self):
        try:
            self.session.rollback()
            return True
        except Exception as e:
            raise e
        return False

    def add_object_to_session(self, obj):
        self.session.add(obj)
        return True

    def get_all(self, models_class, order=None, descs=False):
        if order == None and descs == False:
            return self.session.query(models_class).all()
        elif order == None and descs == True:
            return self.session.query(models_class).order_by(desc('id')).all()
        elif order != None and descs == False:
            return self.session.query(models_class).order_by(order).all()
        elif order != None and descs == True:
            return self.session.query(models_class).order_by(desc(order)).all()

    def get_pos(self):
        return self.session.query(Config).filter(Config.name == 'pos').first()

    def get_one(self, models_class, order=None, descs=False):
        if order == None and descs == False:
            return self.session.query(models_class).first()
        elif order == None and descs == True:
            return self.session.query(models_class).order_by(desc('id')).first()
        elif order != None and descs == False:
            return self.session.query(models_class).order_by(order).first()
        elif order != None and descs == True:
            return self.session.query(models_class).order_by(desc(order)).first()

    def get_one_where(self, models_class, order=None, descs=False, **kwargs):
        tmp_int = str(models_class.__name__) + '.%s==%d'
        tmp_str = str(models_class.__name__) + '.%s=="%s"'
        lte_int = str(models_class.__name__) + '.%s<=%d'
        gte_int = str(models_class.__name__) + '.%s>=%d'
        btw_int = str(models_class.__name__) + '.%s.between(%s, %s)'
        lte_str = str(models_class.__name__) + '.%s<="%s"'
        gte_str = str(models_class.__name__) + '.%s>="%s"'
        btw_str = str(models_class.__name__) + '.%s.between("%s", "%s")'
        bool_tmp = str(models_class.__name__) + '.%s.is_(%s)'

        select = ''
        for i in kwargs:
            if type(kwargs[i]) == str or type(kwargs[i]) == str:
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
            elif type(kwargs[i]) == bool or kwargs[i] == None:
                select = select + bool_tmp % (i, kwargs[i]) + ','

            else:
                if i[-5:] == '__btw':
                    if type(kwargs[i][0]) == str or type(kwargs[i][0]) == str:
                        select = select + btw_str % (i[0:-5], kwargs[i][0], kwargs[i][1]) + ','

                    else:
                        select = select + btw_int % (i[0:-5], kwargs[i][0], kwargs[i][1]) + ','
                else:
                    select = select + tmp_str % (i, kwargs[i]) + ','
        if order == None and descs == False:
            return self.session.query(models_class).filter(*eval(select)).first()
        elif order == None and descs == True:
            return self.session.query(models_class).filter(*eval(select)).order_by(desc('id')).first()
        elif order != None and descs == False:
            return self.session.query(models_class).filter(*eval(select)).order_by(order).first()
        elif order != None and descs == True:
            return self.session.query(models_class).filter(*eval(select)).order_by(desc(order)).first()

    def get_all_where_sort_bylike(self, models_class, **kwargs):
        tmp_str = str(models_class.__name__) + '.%s.like("%s")'
        select = ''
        for i in kwargs:
            select = tmp_str % (i, '%' + kwargs[i] + '%')

        return self.session.query(models_class).filter(eval(select)).all()

    def get_all_where(self, models_class, order=None, descs=False, **kwargs):
        tmp_int = str(models_class.__name__) + '.%s==%d'
        tmp_str = str(models_class.__name__) + '.%s=="%s"'
        lte_int = str(models_class.__name__) + '.%s<=%d'
        gte_int = str(models_class.__name__) + '.%s>=%d'
        btw_int = str(models_class.__name__) + '.%s.between(%s, %s)'
        lte_str = str(models_class.__name__) + '.%s<="%s"'
        gte_str = str(models_class.__name__) + '.%s>="%s"'
        btw_str = str(models_class.__name__) + '.%s.between("%s", "%s")'
        bool_tmp = str(models_class.__name__) + '.%s.is_(%s)'

        select = ''
        for i in kwargs:
            if type(kwargs[i]) == str or type(kwargs[i]) == str:
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
            elif type(kwargs[i]) == bool or kwargs[i] == None:
                select = select + bool_tmp % (i, kwargs[i]) + ','
            else:
                if i[-5:] == '__btw':
                    if type(kwargs[i][0]) == str or type(kwargs[i][0]) == str:
                        select = select + btw_str % (i[0:-5], kwargs[i][0], kwargs[i][1]) + ','

                    else:
                        select = select + btw_int % (i[0:-5], kwargs[i][0], kwargs[i][1]) + ','
                else:
                    select = select + tmp_str % (i, kwargs[i]) + ','
        if order == None and descs == False:
            return self.session.query(models_class).filter(*eval(select)).all()
        elif order == None and descs == True:
            return self.session.query(models_class).filter(*eval(select)).order_by(desc('id')).all()
        elif order != None and descs == False:
            return self.session.query(models_class).filter(*eval(select)).order_by(order).all()
        elif order != None and descs == True:
            return self.session.query(models_class).filter(*eval(select)).order_by(desc(order)).all()
    def delete_object(self, obj):
        self.session.delete(obj)
        return True

    def flush(self):
        try:
            self.session.flush()
            return True
        except Exception as e:
            raise e
        return False

    def empty_table(self, models_class):
        self.session.query(models_class).delete()
        return True

    def get_next_doc_num(self, models_class, field):
        tmp = str(models_class.__name__) + '.%s.desc()' % (field)
        try:
            doc_n = self.session.query(models_class).order_by(eval(tmp)).first()
        except Exception as e:
            print(e)
        if doc_n == None:
            return 0
        else:
            return doc_n.id + 1

def change_alembic_conf():
    cmd = 'rm alembic.ini alembic/env.py'
    os.system(cmd)
    cmd = 'cp models/alembic.ini alembic.ini'
    os.system(cmd)
    cmd = 'cp models/alembic/env.py alembic/env.py'
    os.system(cmd)

def alembic_migrate(comment):
    cmd = 'alembic revision --autogenerate -m "%s"' % (comment)
    os.system(cmd)


def alembic_upgrade(heads=False):
    if heads == False:
        os.system('alembic upgrade head')
    else:
        os.system('alembic upgrade heads')
    return True


def alembic_revision_change(rev):
    db = DBCtrl()
    data = db.get_one(Alembic, )
    data.version_num = rev
    db.add_object_to_session(data)
    db.commit()

def EGN_Unikal():
    db = DBCtrl(True)
    user = db.get_all(CustUser, )
    count = 200
    for i in user:
        if not i.personal_cart_id:
            i.personal_cart_id = str(count)
            # i.forbiden = True
            count += 1
            db.add_object_to_session(i)
        else:
            tmp = db.get_all_where(CustUser, personal_cart_id=i.personal_cart_id)
            if len(tmp) > 1:
                for b in tmp[:-1]:
                    b.personal_cart_id = str(count)
                    count += 1
                    b.forbiden = True
                    db.add_object_to_session(b)
        if not i.personal_egn:
            i.personal_egn = str(count)
            # i.forbiden = True
            count += 1
            db.add_object_to_session(i)
        else:
            tmp = db.get_all_where(CustUser, personal_egn=i.personal_egn)
            if len(tmp) > 1:
                for b in tmp[:-1]:
                    b.personal_egn = str(count)
                    count += 1
                    b.forbiden = True
                    db.add_object_to_session(b)
    db.commit()
if __name__ == '__main__':
    pass



