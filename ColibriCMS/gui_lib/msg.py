#-*- coding:utf-8 -*-
'''
Created on 25.05.2017 г.

@author: dedal
'''
import wx
import gettext
import os
if __package__:
    import libs
else:
    import sys
    import os
    # sys.path.append('/home/dedal/Colibri/ColibriCMS/2_1/libs')
    sys.path.append('/home/dedal/Colibri/ColibriCMS/2_1/')
    # os.chdir('/home/dedal/Colibri/ColibriCMS/2_1')
    import libs

locale_folder = os.path.abspath(os.path.join(os.path.abspath('locale')))
gettext.install('messages', locale_folder, names=['ugettext'], codeset='utf-8')
gettext.install('messages', locale_folder, names=['ugettext'], codeset='utf-8')
lang = gettext.translation('messages', 'locale', fallback=True, languages=[libs.conf.USE_LANGUAGE])
lang.install()

def show(parent, msg):
    dial = wx.MessageDialog(parent, *msg)
    dial.ShowModal()

########################################################################################################################
#  Mesage
########################################################################################################################
INFO = _(u'Информация!')
ERROR = _(u'Грешка!')
DB_WRONG_REQUEST = ( _(u'Грешна заявка към базата данни!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
SYSTEM_UPDATE = ( _(u'Системата не отговаря на минималната ревизия!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
DB_COPY_OK = ( _(u'Успешно архивиране!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
DB_COPY_NOT_OK = ( _(u'Неуспешно архивиране!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
DB_RESTORY_OK = ( _(u'Успешно връщане от архив!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
DB_RESTORY_NOT_OK = ( _(u'Неуспешно връщане от архив!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
NO_MONY = ( _(u'Недостатъчна наличност'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
MSG_JP_SERVER_ACTIVE_TRUE = ( _(u'Успешна активация!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
MSG_JP_SERVER_ACTIVE_FALSE = ( _(u'Грешен код за активация!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
MSG_NOT_SELECT_ITEM = ( _(u'Моля изберете от списъка!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
PROCES_FINISH = ( _(u'Процесът приключи!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
USER_NOT_HAVE_CART = ( _(u'Потребителя няма добавена карта!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
PROCES_FINISH_NOT_OK = ( _(u'Процесът приключи с грешка!'), INFO, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
MAKE_ORDER_ERROR = ( _(u'Моля направете отчет!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
WRITE_ORDER_IN_DB_ERROR = ( _(u'Грешка при генериране на ордер!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
PRINT_OK = ( _(u'Успешно отпечатване!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
PRINT_NOT_OK = ( _(u'Неуспешен печат!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
MSG_CONNECTION_ERROR = ( _(u'Няма връзка със сървъра!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
DB_HAVE_THIS_NAME = ( _(u'Името съществува!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
DB_BONUS_HAVE = ( _(u'Сумата съществува!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
EMPTY_FIELD = ( _(u'Полето е задължително!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
PASSWD_WRONG = ( _(u'Грешна парола'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
USER_IS_LOGIN = ( _(u'Потребителя е влязъл в системата'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
NO_HAVE_RIGHT = ( _(u'Нямате права за достъп'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
INVALID_DATA = ( _(u'Невалидни данни'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
INVALID_DATA_OR_EXIST = ( _(u'Невалидни данни или клиента съществува'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
NOT_EDITABLE = ( _(u'Не може да бъде редактирано'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
CANT_USE_IP = ( _(u'Резервиран IP адрес!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
NO_SMIB_CONNECTION = ( _(u'Няма връзка с SMIB модула!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
INVALID_IP = ( _(u'Невалиден IP адрес!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
NO_SAS_IN_DEVICE = ( _(u'SAS липсва!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
NO_MASHIN_CONNECTION = ( _(u'Няма връзка с машината!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
WORK_OFF = ( _(u'Успешно приключване на смяна!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
GET_DATA_OK = ( _(u'Успешно изтеглена информация!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
DB_WRITE_ERROR = ( _(u'Грешка при запис в базата данни!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
DB_WRITE_OK = ( _(u'Успешен запис!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
SET_CASINO_DATA = ( _(u'Липсва информация за казиното!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
NOT_ALL_ORDER_IS_FININSH = ( _(u'Не всички отчети са приключени!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
WHIGHT = ( _(u'Моля изчакайте!'), INFO,  wx.ICON_INFORMATION | wx.STAY_ON_TOP)
NOT_ALL_MASHIN_IS_IN_ORDER = ( _(u'Не всички машини са отчетени!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
NOT_ALL_ORDER_IS_FINISH = ( _(u'Не всички отчети са приключени!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
WORK_START_OK = ( _(u'Успешно стартиране на работа!'), INFO,  wx.ICON_INFORMATION | wx.STAY_ON_TOP)
COL_SELECT_IN_REPORT_CURENTSTATE = ( _(u'Няма избрани полета за показване!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
HAVE_DAY_REPORT = ( _(u'Вече има направен отчет!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
NO_DB_CONNECTION = ( _(u'Няма връзка със сървъра!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
BAD_COUNTER = ( _(u'Невалиден брояч!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
BAD_VALUE = ( _(u'Невалидна стойност!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
ALL_CART_DEL = ( _(u'Всички карти са изтрити!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
SELECT_GROUP = ( _(u'Избери група!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
SELECT_SITY = ( _(u'Избери град!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
CART_IN_USE = ( _(u'Картата се използва от друг клиент!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
NO_MONY_BACK_TO_PAY = ( _(u'Недостатъчна наличност!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
NO_RFID = ( _(u'Липсва четец!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
IN_TEST = ( _(u'В тестови режим!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
NO_POS_PRINTER = ( _(u'Липсва принтер по подразбиране!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
NO_MONY_TO_PRINT = ( _(u'Клиента не е на печалба!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
NO_LICENSE = ( _(u'Липсва лиценз!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
LICENSE_END_TIME = ( _(u'Лицензът е невалиден!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
LICENSE_CANT_WORK =  ( _(u'Лицензът е деактивиран!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
BAD_LICENSE_NAME =  (_(u'Грешно име на лиценз!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
ACTIVE_OK =  (_(u'Успешно активиран!'), INFO, wx.OK | wx.ICON_INFORMATION| wx.STAY_ON_TOP)
END_LICENSE_TIME =  (_(u'Наближава край на лиценз'), ERROR, wx.OK | wx.ICON_INFORMATION| wx.STAY_ON_TOP)
UPDATE_SMIB_AFTER_REBOOT = (_(u'Влиза в сила след рестарт!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
NO_DAY_REPORT = (_(u'Няма дневен отчет!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
MAIL_NOT_SEND = (_(u'Неуспешно изпратен E-MAIL!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
GET_BILL_NOW = (_(u'Извадете била на редактираната машина\nСумата ще бъде зачислена'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
MAIL_SEND = (_(u'Успешно изпратен E-MAIL!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
on_run_error = _(u'Грешка')
bad_rtc_server = _(u'Грешна дата и час?\nМоля проверете\n')
REBOOT_YES_NO = _(u'Влиза в сила след рестарт! Да се рестартира ли системата?')
POS_SYSTEM_UPDATE = _(u'Препоръчваме затваряне на програмата и използване на инсталатор или Update.exe.\nИскате ли да продължите?')
CHANGE_ALL_SMIB_CONF = _(u'Това ще копира избраните настройки на всички машини.\nМашини с различна конфигурация може да спрат да работят.\nИскате ли да продължите?')
NO_MONY_SET = (_(u'Моля въведете сума'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
WORK_NOT_START = (_(u'Няма започната смяна'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
WORK_IS_START = (_(u'Смяната е вече отворена'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
RFID_NOT_ENABLE = (_(u'RFID четеца не е активиран. Проверете Системни настройки.'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
RUN_PROGRAM = (_(u'След приключване на процеса, стартирате програмата отново!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
IP_IS_IN_USE = (_(u'IP е в мрежата!\nПРОВЕРЕТЕ!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
ADD_EIK = (_(u'Добавете ЕИК!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
GRUP_HAVE_USER = (_(u'В групата има клиенти!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)

EGN_IS_NOT_VALID = (_(u'Невалидно ЕГН!'), ERROR, wx.OK | wx.ICON_WARNING | wx.STAY_ON_TOP)
EGN_IS_VALID = [_(u'Валидно ЕГН!\nПол: %(man)s\nДата на раждане: %(burt_date)s\nОбласт на раждане: %(sity)s'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP]
EGN_NO_YEARS= (_(u'Малолетен!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
CART_EXPIRED = (_(u'Изтекла лична карта!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
OCR_READ_ERROR = (_(u'Неуспешно прочетена'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
GET_MONY = [_(u'Вземете пари: %(mony)s лв.'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP]
IN_DEBUG_MOD= (_(u'Само в DEBUG режим\nНе носим отговорност за правилна работа!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
INVALID_COUNTRY_CODE = (_(u'Невалиден код на държава!'), ERROR, wx.OK | wx.ICON_WARNING | wx.STAY_ON_TOP)
IN_NRA = (_(u'Посоченото ЕГН е вписано в регистъра!'), ERROR, wx.OK | wx.ICON_ERROR| wx.STAY_ON_TOP)
CANT_PLAY = (_(u'Има наложена забрана!'), ERROR, wx.OK | wx.ICON_ERROR| wx.STAY_ON_TOP)
NO_CONFIG = (_(u'Неуспешна конфигурация!'), ERROR, wx.OK | wx.ICON_ERROR| wx.STAY_ON_TOP)
IN_NRA_ERROR = (_(u'Неуспешна проверка в НАП'), ERROR, wx.OK | wx.ICON_WARNING| wx.STAY_ON_TOP)
NOT_IN_NRA = (_(u'Не е вписан в регистъра!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
TOKEN_END =  (_(u'Изтича токен за НАП!'), ERROR, wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
START_OCT = _(u'Да стартирам ли четеца за лични карти?\nМоля стартирайте само веднъж четец за лични карти!')
OCR_START = (_(u'Четец за лични карти е включен!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
NEED_HARD_REBOOT = (_(u'Препоръчваме хардуерен рестарт на контролера след промяна на IP!'), INFO, wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
COUNTRY_CODE = [
'ALA',
'ALB',
'DZA',
'ASM',
'AND',
'AGO',
'AIA',
'ATG',
'ARG',
'ARM',
'ABW',
'ASC',
'AUS',
'ATA',
'AUT',
'AZE',
'BHS',
'BHR',
'BGD',
'BRB',
'BLR',
'BEL',
'BLZ',
'BEN',
'BMU',
'BTN',
'BOL',
'BES',
'BIH',
'BWA',
'BVT',
'BRA',
'IOT',
'VGB',
'BRN',
'BGR',
'BFA',
'BDI',
'KHM',
'CMR',
'CAN',
'CPV',
'CYM',
'CAF',
'TCD',
'CHL',
'CHN',
'TWN',
'CXR',
'PYF',
'CCK',
'COL',
'COM',
'COG',
'COD',
'COK',
'CRI',
'CIV',
'HRV',
'CUB',
'ANG',
'CYP',
'CZE',
'DNK',
'DJI',
'DMA',
'DOM',
'ECU',
'EGY',
'SLV',
'GNQ',
'ERI',
'EST',
'SWZ',
'ETH',
'FLK',
'FRO',
'FJI',
'FIN',
'FRA',
'GUF',
'ATF',
'GAB',
'GMB',
'GEO',
'DEU',
'GHA',
'GIB',
'GRC',
'GRL',
'GRD',
'GLP',
'GUM',
'GTM',
'GGY',
'GIN',
'GNB',
'GUY',
'HTI',
'HMD',
'HND',
'HKG',
'HUN',
'ISL',
'IND',
'IDN',
'IRN',
'IRQ',
'IRL',
'IMN',
'ISR',
'ITA',
'JAM',
'JPN',
'JEY',
'JOR',
'KAZ',
'KEN',
'KIR',
'PRK',
'KOR',
'KWT',
'KGZ',
'LAO',
'LVA',
'LBN',
'LSO',
'LBR',
'LBY',
'LIE',
'LTU',
'LUX',
'MAC',
'MKD',
'MDG',
'MWI',
'MYS',
'MDV',
'MLI',
'MLT',
'MHL',
'MTQ',
'MRT',
'MUS',
'MYT',
'MEX',
'FSM',
'MDA',
'MCO',
'MNG',
'MNE',
'MSR',
'MAR',
'MOZ',
'MMR',
'NAM',
'NRU',
'NPL',
'NLD',
'ANT',
'NCL',
'NZL',
'NIC',
'NER',
'NGA',
'NIU',
'NFK',
'MNP',
'NOR',
'OMN',
'PAK',
'PLW',
'PAN',
'PNG',
'PRY',
'PER',
'PHL',
'PCN',
'POL',
'PRT',
'PRI',
'QAT',
'REU',
'ROU',
'RUS',
'RWA',
'BLM',
'SHN',
'KNA',
'LCA',
'MAF',
'SPM',
'VCT',
'WSM',
'SMR',
'STP',
'SAU',
'SEN',
'SRB',
'SYC',
'SLE',
'SGP',
'SXM',
'SVK',
'SVN',
'SLB',
'SOM',
'ZAF',
'SGS',
'SSD',
'ESP',
'LKA',
'SDN',
'SUR',
'SJM',
'SWE',
'CHE',
'SYR',
'TJK',
'TZA',
'THA',
'TLS',
'TGO',
'TKL',
'TON',
'TTO',
'TAA',
'TUN',
'TUR',
'TKM',
'TCA',
'TUV',
'VIR',
'UGA',
'UKR',
'ARE',
'GBR',
'USA',
'URY',
'UZB',
'VUT',
'VAT',
'VEN',
'VNM',
'UMI',
'WLF',
'ESH',
'YEM',
'ZMB',
'ZWE',
]
SITY = {
        43:_(u'Благоевград'),
        93:_(u'Бургас'),
        139: _(u'Варна'),
        169:_(u'Велико Търново'),
        183:_(u'Видин'),
        217:_(u'Враца'),
        233:_(u'Габрово'),
        281:_(u'Кърджали'),
        301:_(u'Кюстендил'),
        319:_(u'Ловеч'),
        341:_(u'Монтана'),
        377:_(u'Пазарджик'),
        395:_(u'Перник'),
        435:_(u'Плевен'),
        501:_(u'Пловдив'),
        527:_(u'Разград'),
        555:_(u'Русе'),
        575:_(u'Силистра'),
        601:_(u'Сливен'),
        623:_(u'Смолян'),
        721:_(u'София – град'),
        751:_(u'София – окръг'),
        789:_(u'Стара Загора'),
        821:_(u'Добрич'),
        843:_(u'Търговище'),
        871:_(u'Хасково'),
        903:_(u'Шумен'),
        925:_(u'Ямбол'),
        999:_(u'Неизвестен')
        }
########################################################################################################################
#  RIGHT
########################################################################################################################
right_group_name = {
    'main':_(u'Начало'),
    'order':_(u'Отчети'),
    'cust':_(u'Клиенти'),
    'config':_(u'Настройки'),
    'mashin':_(u'Машини'),
    'diff':_(u'Други'),
    'user':_(u'Потребители'),
    'report': _(u'Справки')
}
# REPORT
report_order_edit = _(u'Редактирай Отчет')
report_m_tool2 = _(u'Клиенти')
report_m_tool3 = _(u'Машини')
report_m_tool4 = _(u'Крупиета')
report_m_tool6 = _(u'Джакпот')
report_m_tool9 = _(u'Печат')
report_m_tool7 = _(u'E-mail')
report_m_tool8 = _(u'Експорт')
report_m_tool1 = _(u'Затвори')

# MAIN
main_m_tool3 = _(u'Регион')
main_m_tool9 = _(u'Отчети')
main_m_tool5 = _(u'Настройки')
main_m_tool8 = _(u'М. Броячи')
main_m_tool10 = _(u'Справки')
main_m_tool102 = _(u'Клиенти')
main_m_tool101 = _(u'Начало на смяна')
main_m_tool91 = _(u'Печат на отчети')
main_m_order_print = _(u'Печат на месечни отчети')
main_m_tool21 = _(u'Излез')
main_m_button9 = _(u'Проверка/SMIB')
main_m_button25 = _(u'Бонус Карти')
main_m_button26 = _(u'Намерих грешка')
main_m_button7 = _(u'Извади Бил')
main_m_button8 = _(u'Добави ключ')
main_m_button6 = _(u'Пусни бил')
main_m_button30 = _(u'Спри Бил')
main_m_button12 = _(u'Заключи')
main_m_button13 = _(u'Наблюдавай')
main_m_button15 = _(u'Рестарт SMIB')
main_m_button21 = _(u'Забави рилове')
main_m_button22 = _(u'Отключи/SMIB')
main_m_button251 = _(u'Извади пари')
main_m_button301 = _(u'Съобщение')
main_d_click = _(u'Добави повреда за сервиз')
main_m_tool103 = _(u'РКО')
main_set_service_info = _(u'Сервиз')
server_and_smib_player_reset = _(u'Изтрий играч')
set_emg_date_time = _(u'Свери час')
clean_goged_in = _(u'Освободи логнатите потребители')

# main_m_staticText15 = _(u'Съобщение')

# CUST
cust_m_tool2 = _(u'Нов клиент')
cust_m_tool9 = _(u'Редактирай Клиент')
cust_m_tool3 = _(u'Нова група')
cust_m_tool4 = _(u'Мънибек')
cust_m_tool5 = _(u'Печат на талони')
cust_m_tool7 = _(u'Добави пари')
cust_m_tool8 = _(u'Изплати')
cust_m_tool91 = _(u'С. Талон')
cust_m_tool1 = _(u'Затвори')
curt_m_listCtrl2_monyback = _(u'Изплати мънибек без карта')
curt_m_listCtrl2_talon = _(u'Печат талон без карта')
curt_del_all_talon = _(u'Занули всички талони')
cust_group_replace_row = _(u'Правила за промяна на група')
cust_atm = _(u'АТМ Терминал')
root_show_cust = _(u'Месечна статистика')
user_show_cust = _(u'Дневна статистика')
cust_cart_lost = _(u'Премахни статистика')
cust_reserve = _(u'Резервирай')
restricted_bonus = _(u'Не усвояеми')
cust_print_rko = _(u'Отпечатай ордер')
cust_del_group = _(u'Изтрий група')
catd_copy = _(u'Дубликат на карта')
group_copy = _(u'Дублирай Група')
cart_price = _(u'Цена на карта')
check_egn_by_hand = _(u'Ръчна проверка на ЕГН')
# cust_m_tool1 = _(u'Назад')


# CONFIG
conf_m_tool1 = _(u'Потребители')
conf_m_tool2 = _(u'Машини')
conf_m_tool4 = _(u'Лицензи')
conf_m_tool7 = _(u'Рестарт')
conf_m_tool16 = _(u'Джакпот')
conf_m_tool22 = _(u'Системни')
conf_m_tool10 = _(u'Бонус Карти')
conf_m_tool5 = _(u'Помощ')
conf_m_tool6 = _(u'Относно')
conf_m_tool3 = _(u'Затвори')

# ORDER
order_m_tool6 = _(u'Печат')
order_m_tool2 = _(u'Приходи')
order_m_tool102 = _(u'Трансфер')
order_m_tool3 = _(u'Разходи')
order_m_tool4 = _(u'Липси')
order_m_tool8 = _(u'Отчет')
order_m_tool101 = _(u'Ръчен отчет')
order_m_tool111 = _(u'Бил')
order_m_tool10 = _(u'Край на смяна')
order_elcount_edit = _(u'Редактирай електронно отчетени')
order_handcount_edit = _(u'Редактирай ръчно отчетени')
order_load_user_order = _(u'Зареди потребител')
order_prihod_tupe_add = _(u'Добави Основание Приход')
order_razhod_tupe_add = _(u'Добави Основание Разход')
order_prihod_edit = _(u'Редактирай Приход')
order_razhod_edit = _(u'Редактирай Разход')

# USER
user_m_tool2 = _(u'Добави група')
user_m_tool3 = _(u'Добави потребител')
user_m_tool4 = _(u'Активни')
user_hold_missing_mony = _(u'Удържане на липса')
user_m_tool1 = _(u'Затвори')

# MASHIN
mashin_m_tool2 = _(u'Добави машина')
mashin_m_tool3 = _(u'Добави регион')
mashin_m_tool5 = _(u'Добави модел')
mashin_m_tool4 = _(u'Добави производител')
mashin_elcount_edit = _(u'Редактирай Електронни броячи')
mashin_m_tool1 = _(u'Затвори')
mashin_edit = _(u'Редактиране на машини')
mashin_add_to_jp = _(u'Запис в джакпот')

# DIFF
diff_month_report_from_to = _(u'Месечен От/До')
lock_procent_in_realtime = _(u'Процент в реално време')


########################################################################################################################
#  LOCALIZE
########################################################################################################################

# ----------------------------------------------------------
# main.py
# ----------------------------------------------------------

# MainPanel
main_MainPanel_name = _(u'Начало')
main_MainPanel_tool = {
    'tool3':main_m_tool3,
    'tool9':main_m_tool9,
    'tool5':main_m_tool5,
    'tool8':main_m_tool8,
    'tool10':main_m_tool10,
    'tool102':main_m_tool102,
    'tool101':main_m_tool101,
    'tool91':main_m_tool91,
    'tool21':main_m_tool21,
    'tool103':main_set_service_info,
}
main_MainPanel_text = {
    1: _(u'Потребител'),
    2: _(u'Регион'),
    3: _(u'Каса'),
    4: _(u'Всички'),
    5: _(u'Номер'),
    6: _(u'IP'),
    7: _(u'Модел'),
    8: _(u'Статус'),
    9: _(u'Ревизия'),
    10: _(u'Играч'),
    11: _(u'Няма информация'),
    12: _(u'Няма'),
    13: _(u'OK'),
    15:_(u'Съобщение'),
    16: _(u'Отключена машина. Заключена от съображение за сигурност: '),
    17: _(u'Ключът за кредит беше сменен от: '),
    18:_(u'Билът беше спрян от: '),
    19:_(u'Билът беше стартиран от: '),
    20:_(u'Машината беше заключена / отключена: '),
    21:_(u"Смяна на кей системата"),
    'yes':_(u'Има съобщение'),
}
main_MainPanel_button = {
    'floar_button':_(u'Затвори'),
    'button9_1':main_m_button9,
    'button9_2':_(u'Стоп проверка/SMIB'),
    'button25':main_m_button25,
    'button26':main_m_button26,
    'button7':main_m_button7,
    'button8':main_m_button8,
    'button6':main_m_button6,
    'button30':main_m_button30,
    'button12':main_m_button12,
    'button13':main_m_button13,
    'button15':main_m_button15,
    'button21':main_m_button21,
    'button22':main_m_button22,
    'button251':main_m_button251,
    'button301':main_m_button301,
    'm_button32':server_and_smib_player_reset,
    'm_button35':set_emg_date_time,
}
main_MainPanel_tolltip = {
    'region_bpButton1':_(u'Добави нов регион'),
    'tool3':_(u'Избира регион за работа'),
    'tool9':_(u'Отчитане на машини'),
    'tool5':_(u'Настройки на системата'),
    'tool8':_(u'Проверка на механични броячи'),
    'tool10':_(u'Справки'),
    'tool102':_(u'Клиентски модул'),
    'tool101':_(u'Записва час на започване и приканва за избор на регион'),
    'tool91':_(u'Печат на отчети за комисия'),
    'tool21':_(u'Изход от системата'),
    'tool103':_(u'Сервиз на машини'),
    'button9': _(u'Проверява всички SMIB контролери'),
    'button25': _(u'Справка за поставени бонуси в реално време'),
    'button26': _(u'Докладва грешка към програмист'),
    'button7': _(u'Изваждане на бил по време на работа'),
    'button8': _(u'Променя ключ за кредит при авария със скачаща кейсистема'),
    'button6': _(u'Пуска всички бил аксептори в избрания регион'),
    'button30': _(u'Спира всички бил аксептори в избрания регион'),
    'button12': _(u'Заключва/отключва машина по SAS'),
    'button13': _(u'Наблюдение в реално време на машини'),
    'button15': _(u'Рестартира SMIB контролерите'),
    'button21': _(u'Забавя играта с Х милисекунди'),
    'button22': _(u'Отключва машина, заключена от съображения за сигурност'),
    'button251': _(u'Прави аут по AFT при грешно поставен бонус'),
    'button301': _(u'Съобщение видимо от всички потребители'),
    'text10':_(u'Промяна на парола: ctrl+p'),
    'm_listCtrl4': _(u'shift + клик / ctrl + клик'),
    'm_button32':_(u'Ръчно премахва играча'),
    'm_button35':_(u'Сверява часовника на машината'),
}

#  LoginPanel
main_LoginPanel_name = _(u'Вход в системата')
main_LoginPanel_text = {
    'Text5':_(u'Потребител'),
    'Text6':_(u'Парола'),
    'Text6_1':_(u'Моля поставете карта')
}
main_LoginPanel_button = {
    'button7':_(u'Вход с карта'),
    'button7_1':_(u'Вход с парола'),
    'button6':_(u'Влез'),
    'checkBox1':_(u'Промени казино'),
}
main_LoginPanel_tolltip = {
    'checkBox1':_(u'Избиране на друг сървър'),
    'm_button7':_(u'Влизане в системата с карта'),
    'm_button7_1':_(u'Влизане в системата с парола'),
}

# ServerSelect
main_ServerSelect_name = _(u'Избери сървър')
main_ServerSelect_text = {
    'Text5': _(u'Сървър'),
}
main_ServerSelect_button = {
    'button6': _(u'Промени'),
    'checkBox3': _(u'Отвори порт'),
    'm_checkBox5': _(u'Променливо криптиране'),
}
main_ServerSelect_tolltip = {
    'button3': _(u'Добавя нов сървър в системата'),
    'checkBox3':_(u'Прави възможна влизане извън локалната мрежа')
}

# BugReport
main_BugReport_name = _(u'Доклад за грешка')
main_BugReport_text = {
'text17': _(u'Описание'),
}
main_BugReport_button = {
    'button29': _(u'Затвори'),
    'button30': _(u'Изпрати')
}

# NewServer
main_NewServer_name = _(u'Добави Сървър')
main_NewServer_text = {
    'text9':_(u'Име'),
    'text10': _(u'IP адрес'),
}
main_NewServer_button = {
    'button16':_(u'Затвори'),
    'button17':_(u'Запис'),
}
main_NewServer_tolltip = {
    'Ctrl5': _(u'Свободен текст на латиница без интервали (my_new_server1)')
}

# KSChangeGuage
main_KSChangeGuage_name = _(u'Промяна на ключ за кредит')
main_KSChangeGuage_text = {
    'Text16': _(u'Машина'),
    'msg_ok': _(u'Завършено'),
    'no_ok': _(u'Грешка')
}
main_KSChangeGuage_button = {
    'button21':_(u'Отказ')
}

# PasswdChange
main_PasswdChange_name = _(u'Промяна на парола')
main_PasswdChange_text = {
    'Text14': _(u'Потребител'),
    'Text9':_(u'Парола'),
    'Text10':_(u'Повтори парола'),
}
main_PasswdChange_button = {
    'button5':_(u'Отказ'),
    'button6':_(u'Промени'),
}

# Mony Opis
order_mony_opis = {
    'title': _(u'Опис на пари'),
    'm_button16':_(u'Затвори'),
    'm_button17':_(u'Запис'),
    'm_staticText51':_(u'Общо'),
}
# MSGAdd
main_MSGAdd_name = _(u'Съобщения')
main_MSGAdd_text = {
    'Text17':_(u'Съобщение')

}
main_MSGAdd_button = {
    'button29':_(u'Отказ'),
    'button30':_(u'Запис'),
}
main_MSGAdd_tolltip = {
    'Ctrl7':_(u'Видимо от всички потребители')
}

# Reboot
main_Reboot_name = _(u'Рестарт на SMIB')
main_Reboot_text = {
    'Text12': _(u'След X минути'),
    'Text11': _(u'Планиран рестарт')
}
main_Reboot_button = {
    'button19':_(u'Отказ'),
    'button20':_(u'Рестарт'),
    'radioBtn3':_(u'Софтуерно'),
    'radioBtn4':_(u'Хардуерно'),
}
main_Reboot_tolltip = {
    'spinCtrl2':_(u'Използва се за хардуерен рестарт'),
    'radioBtn3':_(u'Бързо зареждане'),
    'radioBtn4':_(u'Бавно зареждане')
}

# HoldRill
main_HoldRill_name = _(u'Забави рил')
main_HoldRill_text = {
    'Text11':_(u'Време за забавяне'),
    'Text12':_(u'(кратно на 100)')
}
main_HoldRill_button = {
    'button19':_(u'Отказ'),
    'button20':_(u'Забави')
}
main_HoldRill_tolltip = {
    'spinCtrl2':_(u'Блокира аутоплей на EGT'),
}

# RegisterKey
main_RegisterKey_name = _(u'Регистриране на POS терминал')
main_RegisterKey_text = {
    'Text10': _(u'Нямате права за достъп!\nМоля свържете се със администратор!')
}
main_RegisterKey_button = {
    'button30':_(u'Промени Сървър'),
    'button18':_(u'Регистрирай')
}

main_SetPosID = {
    'name':_(u'Регистрирай'),
    'm_staticText16':_(u'Администратор'),
    'm_staticText17':_(u'Парола'),
    'm_staticText18':_(u'Pos Име'),
    'm_button30':_(u'Затвори'),
    'm_button31':_(u'Запис'),
}
main_RegisterKey_tolltip = {
    'textCtrl5':_(u'Изпратете кода на човек с права за достъп'),
}

# ----------------------------------------------------------
# users.main.py
# ----------------------------------------------------------

# AddCart
users_main_AddCart_name = _(u'Добави карта за вход')
users_main_AddCart_text = {
    'Text13':_(u'Моля поставете карта в четеца!'),
    'remove_cart':_(u'Моля извадете карта!'),
    'cart_in_use':_(u'Картата се използва от друг потребител!'),

}
users_main_AddCart_button = {
    'button7': _(u'Премахни'),
    'button8': _(u'Запис'),
    'button8_1': _(u'Затвори')
}

# AddUser
users_main_AddUser_name = _(u'Добави потребител')
users_main_AddUser_text = {
    'Text14':_(u'Име на потребител'),
    'Text9':_(u'Парола'),
    'Text10':_(u'Повтори парола'),
    'Text11':_(u'Избери група'),
    'have_cart':_(u'Карта налична'),
    'no_have_cart':_(u'Липсва карта'),

}
users_main_AddUser_button = {
    'radioBtn2':_(u'Активен'),
    'radioBtn3':_(u'Неактивен'),
    'button7':_(u'Добави Карта'),
    'button5':_(u'Затвори'),
    'button6':_(u'Запис'),
}
users_main_AddUser_tolltip = {
    'radioBtn2':_(u'Активира потребител'),
    'radioBtn3':_(u'Деактивира потребител'),
    'button7':_(u'Картата се използва за вход и кредит'),
}

# AddGrup
users_main_AddGrup_name = _(u'Добави група потребители')
users_main_AddGrup_text = {
    'Text1': _(u'Име на група потребители'),
    'Text3':_(u'Всички права'),
    'Text2':_(u'Права на група')
}

config_IvJump = {
    'name':_(u'Променливо криптиране'),
    'm_button23':_(u'Затвори')
}

users_main_AddGrup_button = {
    'button1':_(u'Затвори'),
    'checkBox71':_(u'Разреши за избор'),
    'button2':_(u'Запис'),
    'm_checkBox2':_(u'Изключи бил'),
    'm_checkBox3':_(u'Извади целия билл'),
    'm_checkBox4':_(u'Зачисли удържане'),
    'm_checkBox5':_(u'Авто E-mail'),
    'm_textCtrl9t':_(u'За повече от един имейл раздели със запетая'),
    'm_textCtrl10t':_(u'Приема само един имейл'),
    'm_checkBox51':_(u'РКО E-mail'),
}
users_main_AddGrup_tolltip = {
    'checkBox71':_(u'При редакция на потребител може да се избере'),
    'bpButton2':_(u'Добавя право към група'),
    'bpButton3':_(u'Премахва право от група'),
}

# UserConf
users_main_UserConf_name = {1:_(u'Настройки/Потребители'), 2:_(u'Настройки')}
users_main_UserConf_text = {
    1:_(u"Номер"),
    2:_(u'Име на група'),
    3:_(u"Номер"),
    4:_(u'Име на потребител'),
    5:_(u'Всички Потребители'),
    6:_(u'Активни Потребители'),
    7:_(u'Неактивни Потребители'),

}
users_main_UserConf_button = {
    'tool2':user_m_tool2,
    'tool3':user_m_tool3,
    'tool4':user_m_tool4,
    'tool1':user_m_tool1,
    'tool5':user_hold_missing_mony,
}
users_main_UserConf_tolltip = {
    'listCtrl1':_(u'Филтър! Два клика редактира'),
    'listCtrl2':_(u'Два клика редактира'),
    'tool2':_(u'Добавя нова група потребители'),
    'tool3':_(u'Добавя нов потребител'),
    'tool4':_(u'Показва всички влезли в системата'),
    'tool1':_(u'Връща в предходното меню'),
}

# LogedInUser
users_main_LogedInUser_name = _(u'Потребители в системата')
users_main_LogedInUser_text = {
    'list_column':_(u'Име на потребител')
}
users_main_LogedInUser_button = {
    'button9':_(u'Затвори')
}
users_main_LogedInUser_tolltip = {
    'Ctrl3':_(u'Двоен клик изхвърля от системата')
}

# ----------------------------------------------------------
# make_order.py
# ----------------------------------------------------------
make_order_Name = _(u'Отчет за ДКХ')
make_order_text = {
    'Text15':_(u'Номер на отчет'),
    1:_(u'ДНЕВЕН ОТЧЕТ'),
    2:_(u'МЕСЕЧЕН ОТЧЕТ')
    # 'sbSizer1':_(u'Тип на отчет!'),
}
make_order_button = {
    'radioBtn1':_(u'Дневен отчет'),
    'radioBtn2':_(u'Месечен отчет'),
    'checkBox2':_(u'От/До Дата'),
    'button5':_(u'Затвори'),
    'button6':_(u'Генерирай'),
}
make_order_tooltip = {
    'checkBox2':_(u'Позволява отчета да се генерира от дата до дата'),
}


# ----------------------------------------------------------
# mony.main.py
# ----------------------------------------------------------

# TransverPassword
mony_main_TransverPassword_name = _(u'Потвърди паричен трансфер')
mony_main_TransverPassword_text = {
    'Text7': _(u'Сума'),
    'Text11': _(u'Потвърди'),
}
mony_main_TransverPassword_button = {
    'button7': _(u'Отказ'),
    'button8': _(u'Потвърди'),
}
mony_main_TransverPassword_tolltip = {
    'Ctrl6':_(u'Въведете паролата на потребителя')
}

# MonyTransfer
mony_main_MonyTransfer_name = _(u'Паричен трансфер')
mony_main_MonyTransfer_text = {
    'm_staticText14': _(u'Сума'),
    'm_staticText15': _(u'Към Потребител'),
    'm_staticText16': _(u'Основание'),
    'm_textCtrl6':_(u'Описание на трансфер')
}
mony_main_MonyTransfer_button = {
    'm_button27': _(u'Отказ'),
    'm_button26': _(u'Запис'),
    'm_radioBtn3': _(u'Каса'),
    'm_radioBtn4': _(u'Допълване'),
    'm_radioBtn5': _(u'Налични'),
    'm_radioBtn6': _(u'Друго'),
}

# MonyInOut
mony_main_MonyInOut_name = {
    'prihod': _(u'Приходи'),
    'razhod':_(u'Разходи'),
}
mony_main_MonyInOut_text = {
    'm_staticText1':_(u'Сума'),
    'm_staticText2':_(u'Допълнителна информация'),
    'm_listCtrl1':_(u'Основание за приход'),
    'm_listCtrl1_1':_(u'Основание за разход'),
}
mony_main_MonyInOut_button = {
    'm_button1':_(u'Затвори'),
    'm_button4':_(u'Запис'),
}
mony_main_MonyInOut_tooltip = {
    # 'm_textCtrl3':_(u'Допълнителна информация'),
    'm_listCtrl1':_(u'Задължително трябва да се избере основание'),
    'm_bpButton1':_(u'Добави ново основание'),
    'm_bpButton2':_(u'Премахни основание'),
    'm_button1':_(u'Затвори'),
    'm_button4':_(u'Запис'),
}

# InOutReson
mony_main_InOutReson_name = {
    'prihod': _(u'Приходи'),
    'razhod':_(u'Разходи'),
    'lipsi':_(u'Липси')
}
mony_main_InOutReson_text = {
    'm_staticText3': _(u'Сума'),
    'm_staticText3_1': _(u'Основание за Приходи'),
    'm_staticText3_2': _(u'Основание за Разходи')

}
mony_main_InOutReson_button = {
    'm_radioBtn1': _(u'Липса'),
    'm_radioBtn2': _(u'Изплащане'),
    'm_button2': _(u'Затвори'),
    'm_button3': _(u'Запис'),
}


# ----------------------------------------------------------
# mashin.main.py
# ----------------------------------------------------------
# Mashin
mashin_main_Mashin_name = _(u'Настройки/Машини')
mashin_main_Mashin_button = {
'm_tool2':mashin_m_tool2,
'm_tool3':mashin_m_tool3,
'm_tool5':mashin_m_tool5,
'm_tool4':mashin_m_tool4,
'm_tool1':mashin_m_tool1,
'm_tool6':mashin_add_to_jp,
}
mashin_main_Mashin_text = {
1:_(u"Производител"),
    2:_(u"Активни"),
    3:_(u"Всички"),
    4:_(u"Неактивни"),
    5:_(u"Номер"),
    6:_(u"Модел"),
    7:_(u"Сериен номер"),
    8:_(u"IP Адрес"),
    9:_(u"SMIB версия"),
    10:_(u'Липсва'),
    11:_(u'Настройки')
}
mashin_main_Mashin_tolltip = {
    'm_tool2':_(u'Добавя нова машина'),
    'm_tool3':_(u'Добавя нов регион'),
    'm_tool5':_(u'Добавя нов модел'),
    'm_tool4':_(u'Добавя нов производител'),
    'm_tool1':_(u'Връща в предходното меню'),
    'm_tool6':_(u'Записва промените в джакпот сървъра'),
    'm_listCtrl2':_(u'Двоен клик редактира'),
}

# FlorSelect
mashin_main_FlorSelect_name = _(u'Регион')
mashin_main_FlorSelect_text = {
    1:_(u'Регион'),
    2:_(u'Всички'),
}
mashin_main_FlorSelect_button = {
    'm_button1':_(u'Затвори')
}
mashin_main_FlorSelect_tolltip = {
    'bpButton1':_(u'Добавя нов регион'),
    'm_listCtrl1':_(u'Двоен клик избира')
}

# FlorAdd
mashin_main_FlorAdd_name = _(u'Добави Регион')
mashin_main_FlorAdd_button = {
    'm_button3':_(u'Затвори'),
    'm_button4':_(u'Запис')
}

# AddModel
mashin_main_AddModel_name = _(u'Добави Модел')
mashin_main_AddModel_button = {
    'm_button1':_(u'Затвори'),
    'm_button14':_(u'Запис')
}
mashin_main_AddModel_text = {
    1:_(u'Модели')
}

# AddMaker
mashin_main_AddMaker_name = _(u'Добави Производител')
mashin_main_AddMaker_button = {
    'm_button3':_(u'Затвори'),
    'm_button4':_(u'Запис')
}

# AddMashin
mashin_main_AddMashin_name = _(u'Добави машина')
mashin_main_AddMashin_button = {
    'm_button20':_(u'Вземи информация'),
    'm_button18':_(u'Затвори'),
    'm_button19':_(u'Запис'),
    'm_radioBtn1':_(u'SAS наличен'),
    'm_radioBtn2':_(u'SAS липсва'),
    'm_checkBox1':_(u'Работеща'),
    'm_checkBox3':_(u'Превъртане в дясно'),
    'm_button11':_(u'Вземи UUID'),
    'm_button13':_(u'Ново IP'),
}

mashin_main_AddMashin_text = {
    1:_(u"Сериен номер"),
    2:_(u"SMIB IP"),
    3:_(u"Регион"),
    4:_(u"Модел"),
    5:_(u"Производител"),
    6:_(u"SMIB IP"),
    7:_(u"UUID"),
    8:_(u"Версия"),
    9:_(u"Няма информация"),
    10:_(u'Номер в зала'),
    11:_(u'Вход'),
    12:_(u"Изход"),
    13:_(u"М.Вход"),
    14:_(u"М.Изход"),
    15:_(u"Залог"),
    16:_(u"Печалба"),
    17:_(u"Бил"),
    18:_(u"Коеф"),
    19:_(u"М.Коеф"),
}
mashin_main_AddMashin_tolltip = {
    'm_bpButton4':_(u'Добавя нов регион'),
    'm_bpButton3':_(u'Добавя нов модел'),
    'm_bpButton2':_(u'Добавя нов производител'),
    'm_textCtrl37':_(u'ctrl+n променя IP със следващо свободно'),
    'm_button20':_(u'Взима броячи, при нулиране или нова машина'),
    'm_checkBox3':_(u'При прехвърляне на 8 цифри превърта брояча'),
    'm_checkBox1':_(u'Вади машината от залата'),
    'm_radioBtn2':_(u'Машини без SAS, повредени машини.'),
}

# ----------------------------------------------------------
# licenz.main.py
# ----------------------------------------------------------
# Active
licenz_main_Active_name = _(u'Инсталирай лиценз')
licenz_main_Active_text = {
    'm_staticText1':_(u'Хардуерен код'),
    'm_staticText2':_(u'Избери лиценз'),
    1:_(u'Няма връзка със сървъра')
}
licenz_main_Active_tooltip = {
    'm_filePicker1':_(u'Валидност на лиценз 40 минути')
}

# Licenz
licenz_main_Licenz_name = _(u'Настройки/Лицензи')
licenz_main_Licenz_button = {
    'm_tool3':_(u'Добави лиценз'),
    'm_tool4':_(u'Затвори'),
}
licenz_main_Licenz_text = {
    1:_(u'Лиценз!'),
    2:_(u"Номер"),
    3:_(u'Име'),
    4:_(u'Активиран до'),
}
licenz_main_Licenz_tooltip = {
    'm_listCtrl1':_(u'Двоен клик проверява лиценз'),
    'm_tool3':_(u'Инсталира нов лиценз'),
    'm_tool4':_(u'Връща в предходното меню'),
}

# ----------------------------------------------------------
# order.main.py
# ----------------------------------------------------------
# UserEditOrderSelect
order_main_UserEditOrderSelect = {
    'name':_(u'Редактирай отчет на потребител'),
    'm_staticText18':_(u'Потребител'),
    'm_button14':_(u'Отказ'),
    'm_button15':_(u'Избери'),
}

# Order
order_main_Order_name = {
    1:_(u'Отчет'),
    2:_(u'Начало')
}
order_main_Order_button = {
    'm_tool6':order_m_tool6,
    'm_tool2':order_m_tool2,
    'm_tool102':order_m_tool102,
    'm_tool3':order_m_tool3,
    'm_tool4':order_m_tool4,
    'm_tool8':order_m_tool8,
    'm_tool101':order_m_tool101,
    'm_tool111':order_m_tool111,
    'm_tool10':order_m_tool10,
    'm_tool1':_(u'Затвори'),
}
order_main_Order_text = {
    1:_(u'Каса'),
    2:_(u'Регион'),
    3:_(u'Потребител'),
    4:_(u'Съобщения'),
    5:_(u'Няма'),
    6:_(u'Номер'),
    7:_(u'Модел'),
    8:_(u'Вход'),
    9:_(u'Изход'),
    10:_(u'Бил'),
    11:_(u'Тотал'),
    12:_(u'Разходи'),
    13:_(u'Приходи'),
    14:_(u'Сума'),
    15:_(u'Грешка при отчитане на машини'),
    16:_(u'Да направя ли повторен опит?'),
    17:_(u'Отчитане на машина'),
    18:_(u'Неуспешно вземане на броячи при отчет.'),
    19:_(u'Всички'),
    20:_(u'Общо'),
    'yes':_(u'Има съобщение'),
    21:_(u'Искате ли да направите трансфер?'),
    22:_(u'Искате ли печат на РКО?'),
    23:_(u'Да променя ли кейсистемата?'),
    # 9:_(u''),
    # 10:_(u''),
    # 11:_(u''),
}
order_main_Order_tooltip = {
    'm_tool6':_(u'Печат на касов ордер'),
    'm_tool2':_(u'Добавя нов приход'),
    'm_tool102':_(u'Трансфер на пари към друг потребител'),
    'm_tool3':_(u'Добавя нов разход'),
    'm_tool4':_(u'Потребителя има липса / изплаща стара липса'),
    'm_tool8':_(u'Отчита машини по SAS'),
    'm_tool101':_(u'Отчита повредени машини / машини без SAS'),
    'm_tool111':_(u'Изважда бил от машини'),
    'm_tool10':_(u'Приключва смяна и занулява каса'),
    'm_tool1':_(u'Връща в предходното меню'),
    'm_listCtrl1':_(u'Двоен клик редактира'),
    'm_listCtrl2':_(u'Двоен клик редактира'),
    'm_listCtrl3':_(u'Двоен клик редактира'),
}

# BillEnableGuage
order_main_BillEnableGuage_name = _(u'Активиране на бил аксептори')
order_main_BillEnableGuage_button = {
    'm_button1': _(u'Затвори'),
}
order_main_BillEnableGuage_text = {
    'm_staticText15': _(u'Машина'),
    'error': _(u'Грешка'),
    'OK': _(u'OK'),
}

# BillGet
order_main_BillGet_name = _(u'Извади бил')
order_main_BillGet_text = {
    1:_(u'Бил'),
    2:_(u"Номер"),
    3:_(u"Модел"),
    4: _(u'Няма информация')
}
order_main_BillGet_button = {
    'm_button7':_(u'Отказ'),
    'm_button8':_(u'Извади'),
}
order_main_BillGet_tolltip = {
    'm_listCtrl5':_(u'Двоен клик блокира / пуска бил')
}

# BillInfoGuage
order_main_BillInfoGuage_name = _(u'Тегли броячите на бил')
order_main_BillInfoGuage_button = {
    'm_button1':_(u'Затвори'),
}
order_main_BillInfoGuage_text = {
    'm_staticText15': _(u'Машина'),
    'OK': _(u'OK'),
    'error': _(u'Грешка'),
}

# GetBillGuage
order_main_GetBillGuage_name = _(u'Тегли броячите на бил')
order_main_GetBillGuage_button = {
    'm_button1':_(u'Затвори'),
}
order_main_GetBillGuage_text = {
    'm_staticText15': _(u'Машина'),
    'OK': _(u'OK'),
    'error': _(u'Грешка'),
}

# GetCounter
order_main_GetCounter_name = _(u'Тегли броячи на машини')
order_main_GetCounter_button = {
    'm_button1':_(u'Затвори'),
}
order_main_GetCounter_text = {
    'm_staticText15': _(u'Машина'),
    'OK': _(u'OK'),
    'error': _(u'Грешка'),
}

# NotSASCounter
order_main_NotSASCounter_name = _(u'Ръчен отчет на машини!')
order_main_NotSASCounter_text = {
    'm_staticText15':_(u'Машина'),
    'm_staticText16':_(u'Вход'),
    'm_staticText18':_(u'Изход'),
    'm_staticText20':_(u'Бил'),
    'm_staticText22':_(u'Тотал'),
    'm_staticText17': u'0.00',
    'm_staticText19': u'0.00',
    'm_staticText21':u'0',
}
order_main_NotSASCounter_button = {
    'm_checkBox1':_(u'Механични броячи'),
    'm_button6':_(u'Затвори'),
    'm_button7':_(u'Запис'),
}
order_main_NotSASCounter_tooltip = {
    'm_checkBox1':_(u'Отчитане по механични броячи'),
    'm_textCtrl10_1':_(u'Сума в касета на бил'),
    'm_textCtrl10':_(u'0 при липса на бил'),
}
# WorkEnd
# order_main_WorkEnd_name = _(u'Край на смяна-отключвам бил аксептори')
# order_main_WorkEnd_button = {
#     'm_button1':_(u'Затвори'),
# }
# order_main_WorkEnd_text = {
#     'm_staticText15': _(u'Машина'),
#     'OK': _(u'OK'),
#     'error': _(u'Грешка'),
# }

# OrderByHand
order_main_OrderByHand_name = _(u'Ръчно отчитане')
order_main_OrderByHand_button = {
    'm_button4':_(u'Затвори'),
}
order_main_OrderByHand_text = {
    1:_(u"Номер"),
    2:_(u"Модел"),
}

# ----------------------------------------------------------
# order.mex_chk.py
# ----------------------------------------------------------
# MexEdit
order_mex_chk_MexEdit_name = _(u'Редактиране на механични броячи на машина')
order_mex_chk_MexEdit_button = {
    'm_button10':_(u'Затвори'),
    'm_button11':_(u'Запис'),
}
order_mex_chk_MexEdit_text = {
    'm_staticText12':_(u'Вход'),
    'm_staticText13':_(u'Изход'),
}

# MexCheck
order_mex_chk_MexCheck_name = {
    1:_(u'Проверка на механични броячи'),
    2:_(u'Начало'),
}
order_mex_chk_MexCheck_text = {
    1:_(u"Номер"),
    2:_(u"Модел"),
    3:_(u"Вход"),
    4:_(u"Изход"),
}
order_mex_chk_MexCheck_tooltip = {
    'm_listCtrl6':_(u'Двоен клик редактира'),
}
order_mex_chk_MexCheck_button = {
    'm_button9':_(u'Печат'),
    'm_button7':_(u'Запис'),
    'm_button8':_(u'Затвори'),
}

# ----------------------------------------------------------
# cust.main.py
# ----------------------------------------------------------
# SetMonyOnUser
cust_MonyOnCart_IN = _(u'Пари по карта IN')
cust_MonyOnCart_OUT = _(u'Пари по карта OUT')
cust_main_SetMonyOnUser_name = _(u'Добави пари в карта')
cust_main_SetMonyOnUser_text = {
    'm_staticText75':_(u'Име'),
}
cust_main_SetMonyOnUser_button = {
    'm_button20':_(u'Отказ'),
    'm_button21':_(u'Запис')
}

# ATM
cust_main_atm_name = _(u'Банков трансфер')
cust_main_ATM_text = {
    'm_staticText75':_(u'Име'),
}
cust_main_ATM_button = {
    'm_button20':_(u'Отказ'),
    'm_button21':_(u'Запис')
}

OCR_READ = {
    'name': _(u'Четене на лична карта'),
    1:_(u'Моля поставете карта в четеца!'),
    2: _(u'Информацията е заредена успешно'),
    3:_(u'Вписан в списъка на НАП'),
    4:_(u'Неуспешна проверка в НАП'),
            }
# SetMonyOnUserCart
cust_main_SetMonyOnUserCart_name = _(u'Четене на карта')
cust_main_SetMonyOnUserCart_text = {
    1:_(u'Моля поставете карта в четеца!'),
    2:_(u'Невалидна карта!'),
    3:_(u'Невалиден потребител!'),
    4:_(u'Потребител'),
    5:_(u'Неактивен клиент')
    # 5:_(u'Моля поставете карта в четеца!')
}
cust_main_SetMonyOnUserCart_button = {
    'm_button8':_(u'Добави'),
    'm_button7':_(u'Затвори'),
}

# PayMony
cust_main_PayMony_name = _(u'Четене на карта')
cust_main_PayMony_text = {
    1:_(u'Моля поставете карта в четеца!'),
    2:_(u'Невалидна карта!'),
    3:_(u'Невалиден потребител!'),
    4:_(u'Потребител'),
    # 5:_(u'Моля поставете карта в четеца!'),
    6:_(u'Пари'),
    7:_(u'Искате ли печат на разходен касов ордер'),
    8:_(u'Неактивен клиент'),
}
cust_main_PayMony_button = {
    'm_button8':_(u'Изплати'),
    'm_button7':_(u'Затвори'),
}

# TaloniPrint
cust_main_TaloniPrint_name = _(u'Четене на карта')
cust_main_TaloniPrint_text = {
    1:_(u'Моля поставете карта в четеца!'),
    2:_(u'Невалидна карта!'),
    3:_(u'Невалиден потребител!'),
    4:_(u'Потребител'),
    5:_(u'Недостатъчна наличност!'),
    6:_(u'Талони'),
    7:_(u'Искате ли печат на копие'),
    8:_(u'Печат на талони'),
    9:_(u'Липсва'),
    10:_(u'Неактивен клиент')
}
cust_main_TaloniPrint_button = {
    'm_button8':_(u'Печат'),
    'm_button7':_(u'Затвори'),
}


# MonyBackPay
cust_MonyBack = _(u'Мъни Бек')
cust_main_MonyBackPay_name = _(u'Четене на карта')
cust_main_MonyBackPay_text = {
    1:_(u'Моля поставете карта в четеца!'),
    2:_(u'Невалидна карта!'),
    3:_(u'Невалиден потребител!'),
    4:_(u'Потребител'),
    # 5:_(u'Моля поставете карта в четеца!'),
    6:_(u'Мънибек'),
    7:_(u'Недостатъчна наличност!'),
    8:_(u'Неактивен клиент')
}
cust_main_MonyBackPay_button = {
    'm_button8':_(u'Изплати'),
    'm_button7':_(u'Затвори'),
}

# AddCart
cust_main_AddCart_name = _(u'Четене на карта')
cust_main_AddCart_text = {
    1:_(u'Моля поставете карта в четеца!'),
    # 2:_(u'Невалидна карта!'),
    # 3:_(u'Невалиден потребител!'),
    2:_(u'Моля извадете карта!'),
    3:_(u'Добави'),
    4:_(u'Премахни'),
}
cust_main_AddCart_button = {
    'm_button8':_(u'Запис'),
    'm_button7':_(u'Затвори'),
}
# AllUserEditByGroup
cust_main_AllUserEditByGroup_name = _(u'Редактира клиенти в група')
cust_main_AllUserEditByGroup_button = {
    'm_button14': _(u'Затвори'),
}

#
# CleanTalon
cust_main_CleanTalon_name = _(u'Редактира клиенти в група')
cust_main_CleanTalon_button = {
    'm_button14': _(u'Затвори'),
}

# AddGrup
cust_main_AddGrup_name = _(u'Група клиенти')
cust_main_AddGrup_text = {
    'm_checkBox55':_(u'Точки в пари'),
    'm_checkBox51':_(u'Позволена за избор'),
    'm_checkBox47':_(u'Не усвояем'),
    'm_checkBox46':_(u'Текущ месец'),
    'm_staticText2':_(u'Име на група'),
    'm_staticText3':_(u'Процент за отчисление'),
    'm_staticText77':_(u'Минимално изплащане'),
    'm_staticText90':_(u'Максимално изплащане'),
    'm_staticText71':_(u'Бонуси'),
    'm_staticText39':_(u'На сума'),
    'm_staticText78':_(u'Забрани изход'),
    'm_staticText5':_(u'Коефициент'),
    'count':_(u'Количество'),
    'mony':_(u'Сума'),
    'm_checkBox40':_(u'Предупреди за бонус'),
    'm_checkBox42':_(u'По BET'),
    'm_checkBox49':_(u'Процент от тотал'),
}
cust_main_AddGrup_button = {
    'm_radioBtn2':_(u'По IN'),
    'm_checkBox59':_(u'Добави сандък x2'),
    'm_radioBtn1':_(u'По Бет'),
    'm_radioBtn12':_(u'Директен'),
    'm_checkBox31':_(u'Удържане'),
    'm_checkBox8':_(u'Веднъж на ден'),
    'm_checkBox9':_(u'Предходен тотал'),
    'm_checkBox12':_(u'Изчакай вход'),
    'm_checkBox20':_(u'Всички'),
    'm_checkBox18':_(u'Понеделник'),
    'm_checkBox19':_(u'Вторник'),
    'm_checkBox21':_(u'Сряда'),
    'm_checkBox24':_(u'Четвъртък'),
    'm_checkBox25':_(u'Петък'),
    'm_checkBox26':_(u'Събота'),
    'm_checkBox27':_(u'Неделя'),
    'm_checkBox1':_(u'Мъни Бек'),
    'm_checkBox2':_(u'Бонуси'),
    'm_checkBox3':_(u'Томбола'),
    'm_radioBtn9':_(u'По Бет'),
    'm_radioBtn10':_(u'По Тотал'),
    'm_button4':_(u'Затвори'),
    'm_button5':_(u'Запис'),
    'm_checkBox53':_(u'Много от редирект'),
    1:_(u'Всички'),
    2:_(u'Мъже'),
    3:_(u'Жени'),
}
cust_main_AddGrup_tooltip = {
    'm_spinCtrl21':_(u'Забранява да се изплаща по-малък мънибек'),
    'm_checkBox1':_(u'Спира отчислението на мънибек'),
    'm_checkBox2':_(u'Спира бонусите'),
    'm_checkBox3':_(u'Спира трупането на талони'),
    'm_textCtrl5':_(u'На 100 лева Х талони'),
    'm_spinCtrl22':_(u'Забранява изход иска AFT'),
    'm_spinCtrl39':_(u'Сума от вход при която ще покаже съобщение за право на хартиен талон'),
    'm_checkBox42':_(u'Превъртане на бонуса по бет'),
}

# AddSity
cust_main_AddSity_name = _(u'Добави град')
cust_main_AddSity_text = {
    'm_staticText40':_(u'Град'),
}
cust_main_AddSity_button = {
    'm_button9':_(u'Затвори'),
    'm_button10':_(u'Запис'),
}
# AddCust
cust_main_AddCust_name = _(u'Добави клиент')
cust_main_AddCust_text = {
    'm_button34':_(u'Прочети лична карта'),
    'm_staticText80':_(u'Код на държава'),
    'm_checkBox56':_(u'Точки в пари'),
    'm_checkBox48':_(u'Не усвояем'),
    'm_checkBox45':_(u'Текущ месец'),
    'm_staticText3011':_(u'Група'),
    'm_staticText42':_(u'Общо карти'),
    'm_staticText311':_(u'Процент на отчисление'),
    'm_staticText77':_(u'Минимално изплащане'),
    'm_staticText89':_(u'Максимално изплащане'),
    'm_staticText511':_(u'Коефициент на 100 лв.'),
    'm_staticText1711':_(u'Име'),
    'm_staticText1811':_(u'Телефон'),
    'm_staticText2011':_(u'E-mail'),
    'm_staticText2411':_(u'ЕГН'),
    'm_staticText2511':_(u'ЛК'),
    'm_staticText2611':_(u'Адрес'),
    'm_staticText2711':_(u'Град'),
    'm_staticText2811':_(u'Валидна до'),
    'm_staticText39111':_(u'На сума'),
    'm_staticText79':_(u'Забрани изход'),
    'count':_(u'Количество'),
    'mony':_(u'Сума'),
    'm_checkBox41':_(u'Предупреди за бонус'),
    'm_checkBox43':_(u'По BET'),
    'man': _(u'Мъж'),
    'women':_(u'Жена'),
    'all':_(u'Всички'),
}
cust_main_AddCust_button = {
    'm_button1011':_(u'Добави Група'),
    'm_radioBtn311':_(u'От Група'),
    'm_radioBtn411':_(u'Персонални'),
    'm_checkBox13':_(u'Забрана'),
    'm_radioBtn9':_(u'По Бет'),
    'm_radioBtn10':_(u'По Тотал'),
    'm_radioBtn211':_(u'По IN'),
    'm_radioBtn111':_(u'По Бет'),
    'm_radioBtn11':_(u'Директен'),
    'm_checkBox30':_(u'Удържане'),
    'm_checkBox10':_(u'Веднъж на ден'),
    'm_checkBox11':_(u'Предходен тотал'),
    'm_checkBox131':_(u'Изчакай вход'),
    'm_checkBox22':_(u'Всички'),
    'm_checkBox23':_(u'Понеделник'),
    'm_checkBox24':_(u'Вторник'),
    'm_checkBox25':_(u'Сряда'),
    'm_checkBox26':_(u'Четвъртък'),
    'm_checkBox27':_(u'Петък'),
    'm_checkBox29':_(u'Неделя'),
    'm_checkBox28':_(u'Събота'),
    'm_button911':_(u'Запис'),
    'm_button811':_(u'Затвори'),
    'm_checkBox50':_(u'Процент от тотал'),
    'm_checkBox52':_(u'Много от редирект'),
    1:_(u"Искате ли да премахнете всички карти?"),
    2:_(u'Изтриване на карти'),
    'm_button29':_(u'Валидирай ЕГН'),
    'm_checkBox59':_(u'Вписан в НАП'),
    'm_checkBox601':_(u'Мъж'),
}
cust_main_AddCust_tooltip = {
    'm_button811':_(u'Добавя снимка на клиент'),
    'm_button1011':_(u'Добавя нова група'),
    'm_bpButton312':_(u'Добавя карта'),
    'm_bpButton13':_(u'Премахва всички карти'),
    'm_bpButton81':_(u'Премахва една карта'),
    'm_bpButton311':_(u'Добавя град'),
    'm_spinCtrl40':_(u'Сума от вход при която ще покаче съобщение за право на хартиен талон'),
    'm_checkBox43':_(u'Превъртане на бонуса по BET'),
}

# ShowCust
cust_main_ShowCust_name = _(u'Месечна статистика')
cust_main_ShowCust_text = {
    'm_staticText78':_(u'Група'),
    'm_staticText79':_(u'Индивидуални настройки'),
    'yes':_(u'Да'),
    'no':_(u'Не'),
    'm_staticText58':_(u'Неусвоен'),
    'm_staticText60':_(u'Усвоен'),
    'm_staticText64':_(u'Общо'),
    'm_staticText80':_(u'Последно дата'),
    'm_staticText82':_(u'Общо'),
    'm_staticText86':_(u'Предпочитана машина'),
    'm_staticText44':_(u'Вход'),
    'm_staticText46':_(u'Изход'),
    'm_staticText48':_(u'Бил'),
    'm_staticText50':_(u'Игри'),
    'm_staticText52':_(u'Средно Бет'),
    'm_staticText581':_(u'Неусвоен'),
    'm_staticText601':_(u'Усвоен'),
    'm_staticText641':_(u'Общо'),
    'm_staticText84':_(u'Сума'),
    'm_staticText90':_(u'Общо карти'),
    'm_staticText94':_(u'Тотал'),
    'm_staticText811':_(u'ЕГН'),
}
cust_main_ShowCust_button = {
    'm_button14':_(u'Затвори')
}
# FreeTalon
cust_main_FreeTalon_name = _(u'Свободен печат на талони')
cust_main_FreeTalon_text = {
    'm_staticText81':_(u'Брой талони'),
    'm_staticText82':_(u'Име'),
    1:_(u'Искате ли печат на копие'),
    2:_(u'Печат на талони')
}
cust_main_FreeTalon_button = {
    'm_button22':_(u'Затвори'),
    'm_button23':_(u'Печат'),
}

# Main
cust_main_Main_name = {1:_(u'Клиенти'), 2:_(u'Начало')}
cust_main_Main_text = {
    1:_(u"Група"),
    2:_(u"ID"),
    3:_(u"Име"),
    4:_(u"Група"),
    5:_(u"Пари по карта"),
    6:_(u"Забрана"),
    7:_(u"Персонални"),
    'yes': _(u'Да'),
    'no':_(u'Не'),
    8:_(u"Всички"),
    9:_(u"Без забрана"),
    10:_(u"Със забрана"),
    11:_(u"Персонални настройки"),
    12:_(u"Име"),
    13:_(u'ЕГН'),
    14:_(u'Телефон'),
    15:_(u'E-mail'),
    16:_(u'ЛК'),
    17:_(u'Карти'),
    'text_del_grup':_(u'Искате ли да премахнете групата и всички пренасочвания?'),
    18:_(u'Записан в НАП'),
}

cust_main_Main_button = {
    'm_tool2':cust_m_tool2,
    'm_tool9':cust_m_tool9,
    'm_tool3':cust_m_tool3,
    'm_tool4':cust_m_tool4,
    'm_tool5':cust_m_tool5,
    'm_tool7':cust_m_tool7,
    'm_tool8':cust_m_tool8,
    'm_tool91':cust_m_tool91,
    'm_tool1':cust_m_tool1,
}
cust_main_Main_tooltip = {
    'm_tool2': _(u'Добавя нов клиент'),
    'm_tool9': _(u'Редактира избран клиент'),
    'm_tool3': _(u'Добавя нова група'),
    'm_tool4': _(u'Изплаща мънибек'),
    'm_tool5': _(u'Печата талони за томбола'),
    'm_tool7': _(u'Добавя пари в карта на клиент'),
    'm_tool8': _(u'Изплаща пари от карта на клиент'),
    'm_tool91': _(u'Печата свободно талони за томбола'),
    'm_tool1': _(u'Връща в предходното меню'),
    'm_listCtrl1': _(u'Двоен клик редактира'),
    'm_listCtrl2': _(u'Двоен клик показва статистика'),
    'm_searchCtrl1': _(u'Enter търси сред клиентите'),
}

# ----------------------------------------------------------
# report.main.py
# ----------------------------------------------------------
report_main_Main_name = {1:_(u'Справки'), 2:_(u'Начало')}
report_main_Main_button = {
    'm_tool2':report_m_tool2,
    'm_tool3':report_m_tool3,
    'm_tool4':report_m_tool4,
    'm_tool6':report_m_tool6,
    'm_tool9':report_m_tool9,
    'm_tool7':report_m_tool7,
    'm_tool8':report_m_tool8,
    'm_tool1':report_m_tool1,
}
report_main_Main_tooltip = {
    'm_tool2':_(u'Справка клиенти'),
    'm_tool3':_(u'Справка Машини'),
    'm_tool4':_(u'Справка крупиета'),
    'm_tool6':_(u'Справка Джакпот сървър'),
    'm_tool9':_(u'Отпечатай текуща справка'),
    'm_tool7':_(u'Изпрати текупа справка на E-mail'),
    'm_tool8':_(u'Експортирай справка в ексел'),
    'm_tool1':_(u'Връща в предходното меню'),
}
report_main_Main_report_name = {
    1:_(u'Потребители'),
    2:_(u'Справка изваден бил'),
    3:_(u'Справка Липси'),
    4:_(u'Отчетени пари'),
    5:_(u'Приходи'),
    6:_(u'Разходи'),
    7:_(u'Лог файл'),
    8:_(u'Бонус Карти'),
    9:_(u'Вход / Изход по карти'),
    10:_(u'Клиенти'),
    11:_(u'Спечелени Бонуси'),
    12:_(u'Изплатен мънибек'),
    13:_(u'Отпечатани талони'),
    14:_(u'Вход / Изход'),
    15:_(u'Статистика'),
    16:_(u'Машини'),
    17:_(u'Справка IN, OUT, Total'),
    18:_(u'Справка изваден бил'),
    19:_(u'Справка възвръщаемост'),
    20:_(u'Механични IN, OUT, Total'),
    21:_(u'Официални отчети'),
    22:_(u'Вход/Изход'),
    23:_(u'SMIB лог'),
    24:_(u'Джакпот'),
    25:_(u'Джакпот'),
    26:_(u'Работно време'),
    27:_(u'Ремонт на машини'),
    28:_(u'Нулирани машини'),
    29:_(u'Трансфери'),
    30:_(u'Банкови преводи'),
    31:_(u'Генериран бил'),
    32:_(u'Количество карти'),
    33:_(u'Натрупан мънибек'),
    34:_(u'Разходни ордери'),
    35:_(u'Пари преди отчет'),
    36:_(u'Натрупани точки'),
    37:_(u'Точки в пари'),
    38:_(u'Проверено ЕГН'),
}

# ----------------------------------------------------------
# cust_report.py
# ----------------------------------------------------------
report_atm = {
    'name':_(u'Банкови преводи'),
    'm_radioBtn7': _(u'Обобщена по крупие'),
    'm_radioBtn14':_(u'Обобщи по клиент'),
    'm_radioBtn15':_(u'Обобщена по дата'),
    1:_(u'ID'),
    2:_(u'Дата'),
    3:_(u'Клиент'),
    4:_(u'Потребител'),
    5:_(u'Сума'),
    6:_(u'Общо'),
}
cust_report_Report_name = _(u'Справки/Клиенти')
cust_report_Report_text = {
    'm_staticText7':_(u'Потребител')
}
cust_report_Report_button = {
    'm_radioBtn9':_(u'Активни потребители'),
    'm_radioBtn8':_(u'Не активни потребители'),
    'm_radioBtn10':_(u'Не обобщавай'),
    'm_radioBtn14':_(u'Обобщена по потребител'),
    'm_radioBtn7':_(u'Обобщена по ден'),
    'm_radioBtn15':_(u'Обобщена по машини'),
    'm_checkBox6':_(u'Сортиране в обратен ред'),
    'm_radioBtn16':_(u'Генерирай таблица'),
    'm_radioBtn17':_(u'Генерирай графика'),
    'm_button6':_(u'Генерирай'),
}
cust_report_Report_tooltim = {
    'm_calendar1':_(u'От дата'),
    'm_calendar2':_(u'До дата'),
}

# Transfer
cust_report_Transfer_text = {
    'name':_(u'Трансфери'),
    1:_(u'Всички'),
    2:_(u'Дата'),
    3:_(u'От Потребител'),
    4:_(u'Към Потребител'),
    5:_(u'Основание'),
    6:_(u'Инфо'),
    7:_(u'Сума'),
    8:_(u'Общо'),
    9:_(u'Каса'),
    10:_(u'Допълване'),
    11:_(u'Налични'),
    12:_(u'Друго'),
}

# BonusGet
cust_report_BonusGet_text = {
    'm_radioBtn15': _(u'Обобщи по машина'),
    'm_radioBtn14':_(u'Обобщена по клиент'),
    'table_name':_(u'Спечелени Бонуси'),
    1:_(u'Дата'),
    2:_(u'Клиент'),
    3:_(u'Машина'),
    4:_(u'Модел'),
    5:_(u'Група'),
    6:_(u'Сума'),
    7:_(u'Общо'),
    9:_(u'Клиент'),
    10:_(u'Общо Сума'),
    11:_(u'Отложен'),
    12:_(u'Да'),
    'm_checkBox6':_(u'Покажи отказани'),
    13:_(u'Инициализиран'),
    14:_(u'Отворен'),
    15:_(u'Брой'),
    16: _(u'Пренасочен'),
    17:_(u'От група')
    # 17:_(u'Пренасочен'),
}

# MonyBackGet
cust_report_MonyBackGet_text = {
    'm_radioBtn15':_(u'Обобщи по крупие'),
    'm_radioBtn14': _(u'Обобщена по клиент'),
    'table_name':_(u'Изплатен Мънибек'),
    1:_(u'Дата'),
    2:_(u'Клиент'),
    3:_(u'Крупие'),
    4:_(u'Сума'),
    5:_(u'Общо'),
}

# TombulaGet
cust_report_TombulaGet_text = {
    'm_radioBtn15':_(u'Обобщи по крупие'),
    'm_radioBtn14':_(u'Обобщи по клиент'),
    'table_name':_(u'Отпечатани Талони'),
    1:_(u'Дата'),
    2:_(u'Клиент'),
    3:_(u'Крупие'),
    4:_(u'Брой Талони'),
    5:_(u'Общо'),
}

cust_report_TombulaOnMonyGet_text = {
    'm_radioBtn15':_(u'Обобщи по крупие'),
    'm_radioBtn14':_(u'Обобщи по клиент'),
    'table_name':_(u'Отпечатани Талони в пари'),
    1:_(u'Дата'),
    2:_(u'Клиент'),
    3:_(u'Крупие'),
    4:_(u'Сума'),
    5:_(u'Общо'),
}
# Statistic
cust_report_Statistic_text = {
    'm_radioBtn7':_(u'Обобщена по клиент'),
    'm_radioBtn14':_(u'По клиент с bet/won'),
    'm_radioBtn15':_(u'Обобщена по дата'),
    'table_name':_(u'Статистика Клиенти'),
    1:_(u'Станал/Дата'),
    2:_(u'Машина'),
    3:_(u'Клиент'),
    4:_(u'Група'),
    5:_(u'Вход'),
    6:_(u'Изход'),
    7:_(u'Тотал'),
    8:_(u'Бил'),
    9:_(u'Печалба'),
    10:_(u'Залог'),
    11:_(u'Среден залог'),
    12:_(u'Кредит IN'),
    13:_(u'Кредит OUT'),
    14:_(u'Бонуси'),
    15:_(u'Номер'),
    16:_(u'Седнал/Дата'),
    17:_(u'Модел'),
    18:_(u'Изиграни игри'),
    19:_(u'Дата'),
    20:_(u'Общо')
}

# InOut
report_InOut_text = {
    'table_name':_(u'In/Out'),
    'm_radioBtn10':_(u'Всички'),
    'm_radioBtn14':_(u'Вход'),
    'm_radioBtn15':_(u'Изход'),
    1:_(u'ID'),
    2:_(u'Дата'),
    3:_(u'Машина'),
    4:_(u'Вход'),
    5:_(u'Изход'),
    6:_(u'Бил'),
    7:_(u'Не'),
    8:_(u'Клиент'),
    9:_(u'Регион'),
    10:_(u'Модел'),
    11:_(u'Горница'),
    12:_(u'Да'),
    13: _(u'Крупие'),
    14: _(u'Липсва'),
    15:_(u'Общо')
}

# InOutAFT
cust_report_InOut_text = {
    'table_name':_(u'In/Out AFT'),
    'm_radioBtn10':_(u'Всички'),
    'm_radioBtn14':_(u'Вход'),
    'm_radioBtn15':_(u'Изход'),
    'total':_(u'Общо'),
    1:_(u'ID'),
    2:_(u'Дата'),
    3:_(u'Машина'),
    4:_(u'Клиент'),
    5:_(u'Група'),
    6:_(u'Вход'),
    7:_(u'Изход'),
    8:_(u'Потребител'),


}

# ----------------------------------------------------------
# jpreport.py
# ----------------------------------------------------------
cust_report_JPDateSelect_text = {
    'm_staticText6':_(u'От Дата'),
    'm_staticText7':_(u'До Дата'),
    'm_button11':_(u'Покажи'),
    'table_name':_(u'Джакпот'),
    1:_(u'Дата'),
    2:_(u'Час'),
    3:_(u'Машина'),
    4:_(u'Група'),
    5:_(u'Ниво'),
    6:_(u'Сума'),
    7:_(u'Общо'),
}

# ----------------------------------------------------------
# user_report.py
# ----------------------------------------------------------
# Report
user_report_Report_button = {
    'm_radioBtn9':_(u'Активни потребители'),
    'm_radioBtn8':_(u'Не активни потребители'),
    'm_radioBtn10':_(u'Не обобщавай'),
    'm_radioBtn7':_(u'Обобщена по ден'),
    'm_radioBtn14':_(u'Обобщена по потребител'),
    'm_radioBtn15':_(u'Обобщена по машини'),
    'm_checkBox6':_(u'Сортиране в обратен ред'),
    'm_radioBtn16':_(u'Генерирай таблица'),
    'm_radioBtn17':_(u'Генерирай графика'),
    'm_button6':_(u'Генерирай'),
}
user_report_Report_text = {
    'm_staticText7':_(u'Потребител'),
    1:_(u'Всички'),

}
user_report_Report_tooltip = {
    'm_calendar1':_(u'От дата'),
    'm_calendar2':_(u'До дата'),
}
# BonusCart
user_report_BonusCart_text = {
    'name':_(u'Бонус Карти'),
    1:_(u'Дата'),
    2:_(u'Карта'),
    3:_(u'Потребител'),
    4:_(u'Машина'),
    5:_(u'Модел'),
    6:_(u'Удържан'),
    7:_(u'Сума Бонус'),
    8:_(u'Сума'),
    9:_(u'Кредит'),
    10:_(u'Общо'),
    11:_(u'Бонус'),
    12:_(u'Всички'),
    13:_(u'Клиент'),
}

# BillReport
user_report_BillReport_text = {
    'name':_(u'Изваден бил'),
    1:_(u'Дата'),
    2:_(u'Потребител'),
    3:_(u'Машина'),
    4:_(u'Модел'),
    5:_(u'Сума'),
    6:_(u'Общо'),
    7:_(u'Всички'),
}

egn_checked = {
    'name':_(u'Проверено ЕГН'),
    1:_(u'Всички'),
    2:_(u'Номер'),
    3:_(u'Дата'),
    4:_(u'Потребител'),
    5:_(u'ЕГН'),
    6:_(u'Клиент'),
    7:_(u'Ръчно'),
    8:_(u'Да'),
}

# Lipsi
user_report_Lipsi_text = {
    'name':_(u'Справка Липси'),
    'm_radioBtn10':_(u"Покажи по дни"),
    'm_radioBtn14':_(u'Сумиране на липси'),
    1:_(u'Всички'),
    2:_(u'Дата'),
    3:_(u'Потребител'),
    4:_(u'Сума'),
    5:_(u'Тип'),
    6:_(u'Липса'),
    7:_(u'Изплащане на липса'),
}
# BosGetMony
user_report_BosGetMony_text = {
    'name':_(u'Отчетени пари'),
    'm_radioBtn10':_(u'Покажи по дни'),
    'm_radioBtn15':_(u'Сумиране по потребител'),
    'm_radioBtn14':_(u'Сумирай по потребител и регион'),
    1:_(u'Всички'),
    2:_(u'Дата'),
    3:_(u'Потребител'),
    4:_(u'Регион'),
    5:_(u'Сума'),
    'total':_(u'Общо')
}
# MonyBeforOdrer
user_report_MonyBeforOdrer_text = {
    'name':_(u'Пари преди отчет'),
    'm_radioBtn10':_(u'Покажи по дни'),
    'm_radioBtn15':_(u'Сумиране по потребител'),
    'm_radioBtn14':_(u'Сумирай по потребител и регион'),
    1:_(u'Всички'),
    2:_(u'Дата'),
    3:_(u'Потребител'),
    5:_(u'Сума'),
}

# Prigodi
user_report_Prigodi_text = {
    'name':_(u'Приходи'),
    'm_radioBtn10':_(u"Не сумирана"),
    'm_radioBtn15':_(u'Сумиране по потребител'),
    'm_radioBtn14':_(u'Сумирай по основание'),
    1:_(u'Всички'),
    2:_(u'Дата'),
    3:_(u'Потребител'),
    4:_(u'Основание'),
    5:_(u'Инфо'),
    6:_(u'Сума'),
    7:_(u'Общо'),
}
# Razhodi
user_report_Razhodi_text = {
    'name':_(u'Разходи'),
    'm_radioBtn10':_(u"Не сумирана"),
    'm_radioBtn15':_(u'Сумиране по потребител'),
    'm_radioBtn14':_(u'Сумирай по основание'),
    1:_(u'Всички'),
    2:_(u'Дата'),
    3:_(u'Потребител'),
    4:_(u'Основание'),
    5:_(u'Инфо'),
    6:_(u'Сума'),
    7:_(u'Общо'),
}
# ConterGetError
user_report_ConterGetError_text = {
    'name':_(u'Грешки при отчет'),
    1:_(u'Дата'),
    2:_(u'Потребител'),
    3:_(u'Машина'),
    4:_(u'Информация'),
    5:_(u'Всички'),
}
# InOut
user_report_InOut_text = {
    'm_radioBtn10':_(u'Всички'),
    'm_radioBtn14':_(u'Вход'),
    'm_radioBtn15':_(u'Изход'),
    'name':_(u'Пари по карта'),
    1:_(u'ID'),
    2:_(u'Дата'),
    3:_(u'Потребител'),
    4:_(u'Клиент'),
    5:_(u'Група'),
    6:_(u'Вход'),
    7:_(u'Изход'),
    8:_(u'Всички'),
    9:_(u'Общо'),
}

# ----------------------------------------------------------
# mashin_report.py
# ----------------------------------------------------------

# BonusLock
mashin_report_BonusLock = {
    'm_button20':_(u'Затвори'),
    1:_(u'Дата'),
    2:_(u'Карта'),
    3:_(u'Машина'),
    4:_(u'Модел'),
    5:_(u'Удържан'),
    6:_(u'Сума Бонус'),
    7:_(u'Сума'),
    8:_(u'Общо'),
    9:_(u'Клиент'),
    10:_(u'Отложен'),
    11:_(u'Пренасочен'),
    12:_(u'ДА'),
}
# RealTimeLock
mashin_report_RealTimeLock = {
    'm_button20':_(u'Затвори'),
    1:_(u"Няма информация"),
}
# Report
mashin_report_Report = {
    1:_(u'Всички'),
    2:_(u'Производител'),
    3:_(u'Mашина'),
    4:_(u'Регион'),
    5:_(u'Потребител'),
    6:_(u'Модел'),
    'm_radioBtn28':_(u'По Bet и Won'),
    'm_radioBtn29':_(u'По IN и OUT'),
    'm_radioBtn10':_(u'Не обобщавай'),
    'm_radioBtn7':_(u'Обобщена по ден'),
    'm_radioBtn15':_(u'Обобщена по машини'),
    'm_radioBtn42':_(u'По регион'),
    'm_radioBtn14':_(u'Обобщена по производител'),
    'm_radioBtn16':_(u'Генерирай таблица'),
    'm_radioBtn17':_(u'Генерирай графика'),
    'm_button6':_(u'Генерирай'),
    'm_calendar1':_(u'От Дата'),
    'm_calendar2':_(u'До Дата'),
    'm_button6_tooltip':_(u'Изготви справката'),
}

# InOutReport
mashin_report_InOutReport = {
    'name':_(u'Справка IN, OUT'),
    1:_(u'Производител'),
    2:_(u'Машина'),
    3:_(u'Регион'),
    4:_(u'Потребител'),
    5:_(u'Дата'),
    6:_(u'Машина'),
    7:_(u'Сериен'),
    8:_(u'Модел'),
    9:_(u'Стар Вход'),
    10:_(u'Старт Изход'),
    11:_(u'Нов вход'),
    12:_(u'Нов изход'),
    13:_(u'Стар Бил'),
    14:_(u'Нов Бил'),
    15:_(u'Бил Сума'),
    16:_(u'Вход сума'),
    17:_(u'Изход сума'),
    18:_(u'Тотал'),
    19:_(u'Общо'),
    20:_(u'Всички'),
    21:_(u'Потребител'),

}
# Mehanic
mashin_report_Mehanic = {
    'name':_(u'Механични IN, OUT'),
    1:_(u'Дата'),
    2:_(u'Машина'),
    3:_(u'Модел'),
    4:_(u'Стар Вход'),
    5:_(u'Старт Изход'),
    6:_(u'Нов вход'),
    7:_(u'Нов изход'),
    8:_(u'Вход сума'),
    9:_(u'Изход сума'),
    10:_(u'Тотал'),
    11:_(u'Общо'),
    12:_(u'Производител'),
    13:_(u'Регион'),
}
# MonyReturn
mashin_report_MonyReturn = {
    'name':_(u'Възвръщаемост'),
    1:_(u'Всички'),
    2:_(u'Производител'),
    3:_(u'Модел'),
    4:_(u'Регион'),
    5:_(u'Машина'),
    6:_(u'Модел'),
    7:_(u'Изход'),
    8:_(u'Вход'),
    9:_(u'Върнати пари %'),
    10:_(u'Печалба'),
    11:_(u'Залог'),
    12:_(u'Възвръщаемост %'),
    13:_(u'Общо'),
    'm_checkBox15':_(u'От/До Дата'),
    'm_checkBox15t':_(u'Използва календара'),
    15:_(u'Тотал'),
    16:_(u'Дата'),

}
# BillGet
mashin_report_BillGet = {
    'name':_(u'Генериран Бил'),
    1:_(u'Всички'),
    2:_(u'Производител'),
    3:_(u'Машина'),
    4:_(u'Регион'),
    5:_(u'Потребител'),
    6:_(u'Дата'),
    7:_(u'Машина'),
    8:_(u'Модел'),
    9:_(u'Бил'),
    10:_(u'Общо'),
}
# MCurenState
mashin_report_MCurenState = {
    'name':_(u'Наблюдение в реално време'),
    'm_checkBox9':_(u'Текущ кредит'),
    'm_checkBox3':_(u'Вход'),
    'm_checkBox4':_(u'Изход'),
    'm_checkBox81':_(u'Бил'),
    'm_checkBox5':_(u'Тотал'),
    'm_checkBox7':_(u'Печалба в игра ( won )'),
    'm_checkBox6':_(u'Залог ( bet )'),
    'm_checkBox8':_(u'Процент на възвръщаемост'),
    'm_staticText7':_(u'Време за опресняване'),
    'm_staticText5':_(u'0 = Зависи от машината'),
    'm_staticText4':_(u'Секунди на машина'),
    'm_button8':_(u'Затвори'),
    'm_button6':_(u'Напред'),
    1:_(u'Машина'),
    2:_(u'Модел'),
    3:_(u'Играч'),
}
# OrderEdit
mashin_report_OrderEdit = {
    'name':_(u'Редакция на отчет'),
    'm_button7':_(u'Запис'),
    'm_button8':_(u'Печат'),
    'm_button12':_(u'E-MAIL'),
    'm_button9':_(u'Затвори'),
    'm_button17':_(u'Номер'),
    'm_button18':_(u'Дата'),
    'm_button19':_(u'Ред ремонт'),
    'm_button20':_(u'Изтрий'),
    1:_(u'N'),
    2:_(u'ИА'),
    3:_(u'ВХОД(IN)'),
    4:_(u'ИЗХОД(OUT)'),
    5:_(u'M.ВХОД(IN)'),
    6:_(u'M.ИЗХОД(OUT)'),
    7:_(u'ВХОД'),
    8:_(u'ИЗХОД'),
    9:_(u'ТОТАЛ'),
    10:_(u'ДНЕВЕН ОТЧЕТ'),
    11:_(u'МЕСЕЧЕН ОТЧЕТ'),
}
# EditDayReportMashin
mashin_report_EditDayReportMashin = {
    'name':_(u'Редактиране на броячи'),
    'm_staticText15':_(u'Машина'),
    'm_staticText16':_(u'Вход'),
    'm_staticText18':_(u'Изход'),
    'm_staticText20':_(u'М.Вход'),
    'm_staticText181':_(u'М.Изход'),
    'm_staticText22':_(u'Тотал'),
    'm_button6':_(u'Затвори'),
    'm_button7':_(u'Запис'),
}
# DayOrderShow
mashin_report_DayOrderShow = {
    'm_button6':_(u'Покажи'),
    1:_(u'Дневен'),
    2:_(u'Месечен'),
    3:_(u'Ордер'),
    4:_(u'Общо'),
    5:_(u'ID'),
    6:_(u'Дата'),
    7:_(u'Номер'),
    8:_(u'Потребител'),
    9:_(u'Тотал'),
    10:_(u'Генериран'),
}
# H24
mashin_report_H24 = {
    'name':_(u'24 часа'),
    'm_checkBox141':_(u'Машини IN/OUT'),
    'm_checkBox14':_(u'Джакпоти / Бонус карти'),
    'm_checkBox181':_(u'Обобщена таблица'),
    'm_checkBox6':_(u'Приходи / Разходи'),
    'm_checkBox17':_(u'Клиентски бонус'),
    'm_button6':_(u'Генерирай'),
    1:_(u'Приходи'),
    2:_(u'Разходи'),
    3:_(u'Мънибек'),
    4:_(u'Бил'),
    5:_(u'Основание'),
    6:_(u'Сума'),
    7:_(u'Потребител'),
    8:_(u'Усвоен'),
    9:_(u'Общо'),
    10:_(u'Джакпот'),
    11:_(u'Бонус Карти'),
    12:_(u'Дата'),
    13:_(u'Час'),
    14:_(u'Машина'),
    15:_(u'Група'),
    16:_(u'Регион'),
    17:_(u'Номер'),
    18:_(u'Клиент'),
    19:_(u'Модел'),
    20:_(u'Парични трансфери'),
    21:_(u'Липси'),
    22:_(u'От потребител'),
    23:_(u'Към потребител'),
    24:_(u'Стар вход'),
    25:_(u'Стар изход'),
    26:_(u'Нов вход'),
    27:_(u'Нов изход'),
    28:_(u'Стар Бил'),
    29:_(u'Нов Бил'),
    30:_(u'Бил'),
    31:_(u'Вход сума'),
    32:_(u'Изход сума'),
    33:_(u'Тотал'),
    34:_(u'Вход'),
    35:_(u'Изход'),
    36:_(u'Усвоен Бил'),
    37:_(u'Неусвоен Бил'),
    38:_(u'Джакпот'),
    39:_(u'Бонуси'),
    40:_(u'Мънибек'),
    41:_(u'Общо'),
}
# SMIBLog
mashin_report_SMIBLog = {
    'name':_(u'SMIB Лог'),
    1:_(u'Всички'),
    2:_(u'ID'),
    3:_(u'Дата'),
    4:_(u'Машина'),
    5:_(u'Съобщение'),
    6:_(u'Регион'),
    7:_(u'Име'),
    8:_(u'Процес'),
    9:_(u'Функция'),
    10:_(u'Ред'),
    11:_(u'Инфо'),
    12:_(u'Ниво')
}
# EXPORT
report_export = {
    'name':_(u'Експорт'),
    'm_button13':_(u'Затвори'),
    'm_button14':_(u'Експорт'),
    'm_textCtrl1':_(u'Име на файл')
}

# ----------------------------------------------------------
# report_task.py
# ----------------------------------------------------------
report_task = {
    1:_(u'Няма информация'),
    2:_(u'Текущ кредит'),
    3:_(u'Играч'),
    4:_(u'Бил'),
    5:_(u'Залог ( bet )'),
    6:_(u'Печалба в игра ( won )'),
    7:_(u'Вход'),
    8:_(u'Изход'),
    9:_(u'Тотал'),
    10:_(u'Процент на възвръщаемост'),

}

# ----------------------------------------------------------
# config_main.py
# ----------------------------------------------------------

# RebootSMIB
config_RebootSMIB = {
    'name':_(u'Рестарт SMIB'),
    'm_button23':_(u'Затвори')
}
# UpdateSMIB
config_UpdateSMIB = {
    'name':_(u'Update SMIB'),
    'm_button23':_(u'Затвори')
}
# Update
config_Update = {
    'm_checkBox43':_(u'Минимална ревизия'),
    'm_checkBox43t':_(u'Ъпдейтва всички програми ако ревизията е по-малка.'),
    'm_checkBox54':_(u'Миграция'),
    'm_checkBox54t':_(u'Обновява базата данни спрямо избраната ревизия!'),
    'make_backup':_(u'Направете архив на базата!\nИскате ли да продължите?'),
    'yes_on_backup':_(u'Архивиране')
}

# UserHaveMony
order_UserHaveMony = {
    'name': _(u'Налични пари'),
    'm_staticText12':_(u'Налични пари'),
    'm_button10':_(u'Затвори'),
    'm_button11':_(u'Запис')

}
# SystemConf
config_SystemConf = {
    'm_button58':_(u'Токен НАП'),
    'm_checkBox61':_(u'Блокирай при точки'),
    'm_checkBox561':_(u'Пари преди отчет'),
    'm_checkBox561t':_(u'Въвеждат се налични пари преди отчитане на машини'),
    'm_checkBox56':_(u'Крупие/име на отчет'),
    'm_checkBox56t':_(u'Показва име на крупие на дневен и месечен отчет'),
    'm_checkBox50':_(u'Печат на ордер'),
    'm_button3':_(u'Свери'),
    'm_staticText79':_(u'ЕИК'),
    'm_button3t':_(u'Сверява дата и час'),
    'm_staticText13':_(u'Език'),
    'm_staticText122':_(u'Организатор'),
    'm_staticText131':_(u'Адрес'),
    'm_staticText141':_(u'Игрална зала'),
    'm_staticText151':_(u'Адрес зала'),
    'm_staticText1511':_(u'Управител'),
    # 'm_staticText33':_(u'E-MAIL'),
    # 'm_staticText78':_(u'E-MAIL Сервиз'),
    # 'm_staticText67':_(u'Subject'),
    'm_checkBox1':_(u'Дебъг'),
    'm_checkBox11':_(u'ДБ Дебъг'),
    'm_checkBox2':_(u'Цял Екран'),
    'm_checkBox4':_(u'Клавиатура'),
    # 'm_checkBox41':_(u'Изключи бил'),
    # 'm_checkBox13':_(u'Авто E-mail'),
    # 'm_checkBox33':_(u'Извади целия бил'),
    'm_checkBox35':_(u'Зачисли удържане'),
    'm_checkBox38':_(u'Вход веднъж'),
    'm_button6':_(u'Запис'),
    'm_checkBox1t':_(u'Грешките се пренасочват към допълнителен прозорец'),
    'm_checkBox11t':_(u'Записва се комуникацията с базата'),
    'm_checkBox2t':_(u'Програмата стартира на цял екран. Не позволява отваряне на други приложения.'),
    'm_checkBox4t':_(u'Показва виртуална клавиатура'),
    # 'm_checkBox41t':_(u'Блокира бил при отчет'),
    # 'm_checkBox13t':_(u'Изпраща дневния отчет на E-MAIL'),
    # 'm_checkBox33t':_(u'Целия бил по подразбиране е маркиран за вадене'),
    # 'm_checkBox35t':_(u'Зачислява удържаните бонуси на крупието'),
    'm_checkBox38t':_(u'Потребителя може да влезе само веднъж. Позволява изхвърляне на потребител'),
}
# PrinterRFIDConf
config_PrinterRFIDConf = {
    'm_checkBox76':_(u'Наличен'),
    'm_staticText85':_(u'Порт'),
    'm_textCtrl28t':_(u'Споделете принтера. Въведете името на споделяне. Не използвайте интервали в името'),
    'm_checkBox6':_(u'Директен Печат'),
    'm_checkBox44':_(u'Печат на сървър'),
    'm_checkBox51':_(u'Директен Печат POS'),
    'm_checkBox52':_(u'Печат на сървър POS'),
    'm_checkBox44t':_(u'Печата на принтера закачен на сървъра'),
    'm_checkBox39':_(u'POS Printer'),
    'm_staticText16':_(u'PDF Софтуер'),
    'm_staticText18':_(u'Принтер по подразбиране'),
    'm_staticText68':_(u'POS Принтер'),
    'm_staticText69':_(u'Размер на хартия'),
    'm_button47':_(u'Тест POS Принтер'),
    'm_button471':_(u'Добави инфо'),
    'm_checkBox7':_(u'Използвай'),
    'm_staticText20':_(u'Порт'),
    'm_staticText26':_(u'Скорост ( серийна комуникация )'),
    'm_staticText27':_(u'Таймаут ( секунди )'),
    'm_staticText22':_(u'Време на сканиране ( милисекунди )'),
    'm_button6':_(u'Запис'),
    'm_checkBox6t':_(u'Отпечатва директно на принтера.'),
    'm_checkBox39t':_(u'Позволява използване на принтер за томбола'),
    'm_textCtrl6t':_(u'Име на програма за отваряне на pdf. Трябва да е премахнат директен печат.'),
    'm_button47t':_(u'Тества принтера за томбола'),
    'm_button471t':_(u'Добавя информация на талона за томбола'),
    'm_checkBox7t':_(u'Позволява вход с карта не с парола'),
    'm_choice3t':_(u'Скорост на rfid четеца'),
    'm_spinCtrl5t':_(u'След колко време да генерира грешка при липса на поставена карта'),
    'm_spinCtrl3t':_(u'Време на сканиране на четеца'),
    'm_checkBox8':_(u'Активиране на RFID'),
    'm_checkBox8t':_(u'Позволява да се използва на rfid четец'),
    'm_checkBox58':_(u'Мънибек на POS'),
}

# PosPrinterConf
config_PosPrinterConf = {
    'name':_(u'Настройки принтер томбола'),
    'm_staticText69':_(u'Обект'),
    'm_staticText70':_(u'Населено място'),
    'm_staticText71':_(u'Адрес'),
    'm_button50':_(u'Затвори'),
    'm_button51':_(u'Запис'),
}

# NetworkConf
config_NetworkConf = {
    'm_checkBox77':_(u'Отключи с OCR'),
    'm_checkBox74':_(u'Променливо криптиране'),
    'm_checkBox74t':_(u'Променя динамично криптирането след всяка заявка!'),
    'm_checkBox38':_(u'Отвори порт'),
    'm_staticText32':_(u'Буфер'),
    'm_staticText33':_(u'Таймаут'),
    'm_checkBox10':_(u'Използвай RTC сървър'),
    'm_button3':_(u'Свери'),
    'm_button11':_(u'Запис'),
    'm_checkBox38t':_(u'Отваря защитната стена, не трябва да има наложена забрана за текущото IP'),
    'm_spinCtrl7t':_(u'Размер на комуникационния буфер'),
    'm_spinCtrl8t':_(u'Генерира грешка при провалена връзка след Х секунди'),
    'm_checkBox10t':_(u'Сверява часовника от сървъра'),
    'm_button3t':_(u'Сверява часовниковия механизъм на сървъра'),
    'm_checkBox39':_(u'Трейдинг'),
    'm_checkBox40':_(u'Часовник'),
    'm_checkBox42':_(u'Logging'),
    'm_checkBox41':_(u'Gmail'),
    'm_button48':_(u'Зареди'),
    'm_button49':_(u'Запис'),
    1:_(u'Стена'),
    2:_(u'Бан'),
    3:_(u'Няма'),
    'm_checkBox39t':_(u'Вкарва сървъра в трейдинг режим'),
    'm_checkBox40t':_(u'При наличие на часовников механизъм'),
    'm_checkBox41t':_(u'Използва gmail за изпращане на E-mail'),
    'm_button48t':_(u'Зарежда текущата конфигурация'),
    'm_button49t':_(u'Записва настройките в сървъра'),
    'm_textCtrl18t':_(u'E-mail адрес за уведомяване при печалба'),
    'm_textCtrl19t':_(u'Заглавие на e-mail'),
    'm_checkBox42t':_(u'Активира лог сървър'),
    'm_staticText75':_(u'Принтер'),
    'm_choice17':_(u'Принтер по подразбиране'),
    'm_checkBox54':_(u'Трейд'),

}
# POSInstall
config_POSInstall = {
    1:_(u'Добавен е нов POS %s.'),
    'name':_(u'Нов POS терминал'),
    'm_staticText30':_(u'Име на терминала'),
    'm_staticText29':_(u'ID на терминала'),
    'm_button9':_(u'Отказ'),
    'm_button10':_(u'Запис'),
    'm_textCtrl11':_(u'Свободен текст. За разпознаване!'),
    'm_textCtrl10':_(u'ID на терминал'),
}
# POS
config_POS = {
    'm_button7':_(u'Инсталирай'),
    'm_button8':_(u'Премахни'),
    'm_button20':_(u'Инициализация'),
    'm_button7t':_(u'Инсталира нов POS терминал'),
    'm_button8t':_(u'Премахва избрания терминал'),
    'm_button20t':_(u'Изтрива всички освен текущия терминал'),
    1:_(u'ID'),
    2:_(u'Име на терминал'),
}
# UpdateRev
config_UpdateRev = {
    'name':_(u'Ревизия'),
    'm_staticText68':_(u'Ревизия номер'),
    'm_button41':_(u'Отказ'),
    'm_button42':_(u'Запис'),
    'm_textCtrl16':_(u'Празно за последна ревизия'),
}

# KSGuage
config_KSGuage = {
    'name':_(u'Програмиране на ключове'),
    'm_button23':_(u'Затвори')
}

# KeySystem
config_KeySystem = {
    'm_checkBox10':_(u'Скачащ ключ'),
    'm_checkBox10t':_(u'Всяко крупие работи със собствен ключ'),
    'm_button24':_(u'Запис'),
    'm_staticText34':_(u'Избери машина'),
    'm_button14':_(u'Реле 1'),
    'm_button12':_(u'Реле 2'),
    'm_checkBox59':_(u'Промени при отчет'),
    'm_choice6':_(u'Програмиране на избрана машина'),
    1:_(u"Всички машини"),
    2:_(u'Ключът за кредит е променен'),
    3:_(u'Ключът за отчет е променен'),
    4:_(u'Промяна в настройките')
}
# DB
config_DB = {
    'm_staticText7':_(u'Архивиране'),
    'm_button48':_(u'Архивирай'),
    'm_button49':_(u'Възстанови'),
    'm_button43':_(u'Почисти База'),
    'm_button46':_(u'Вакумирай'),
    'm_button47':_(u'Ново индексиране'),
    'm_dirPicker2':_(u'Избери директория за архива'),
    'm_filePicker4':_(u'Избери архив за възстановяване'),
    'm_button43t':_(u'Изтрива информация по-стара от една година'),
    'm_button46t':_(u'Ускорява работата на базата, не влияе на информацията'),
    'm_button47t':_(u'Ускорява работата на базата, не влияе на информацията'),
    'm_button50':_(u'Почисти SMIB Лог'),
    'm_button50t':_(u'Изпразва таблицата за грешки'),
    'cleaan_old_data_warning':_(u'Искате ли да изтриете всички стари данни\nПромените ще влязат в сила незабавно!\nМоже да отнеме много време!'),
    'long_time':_(u'Може да отнеме много време!\nМоля изчакайте до приключване на процеса!')
}
# ShowLog
config_ShowLog = {
    'name':_(u'Лог от SMIB'),
    'm_button42':_(u'Затвори'),
}
# AllSMIBConf
config_AllSMIBConf = {
    'name':_(u'Конфигурирай всички SMIB'),
    'm_button23':_(u'Затвори')
}
# SMIB
config_SMIB = {
    'm_checkBox62':_(u'Джакпот към аут'),
    'm_staticText81':_(u'Скин'),
    'm_staticText77':_(u'Лого'),
    'm_checkBox54':_(u'Зареди видео'),
    'm_staticText802':_(u'Номер видео'),
    'list_1':_(u'ЕГТ'),
    'list_2':_(u'Казино технологии CT6'),
    'list_3':_(u'Казино технологии АРМ'),
    'list_4':_(u'Мегаджак'),
    'list_5':_(u'Аматик нов'),
    'list_6':_(u'Аматик стар'),
    'list_7':_(u'Импера'),
    'list_8':_(u'Проксима'),
    'list_9':_(u'Апекс'),
    'm_staticText80':_(u'Конфигурация'),
    'm_textCtrl24':_(u'SAS Таймаут'),
    'm_textCtrl23':_(u'Забавя комуникацията между командите'),
    'm_textCtrl22':_(u'Номер по sas. 00 взема автоматично'),
    'm_staticText33':_(u'SMIB'),
    'm_checkBox21':_(u'RFID'),
    'm_checkBox25':_(u'Джакпот сървър'),
    'm_checkBox22':_(u'Кей Система'),
    'm_checkBox20':_(u'SAS'),
    'm_checkBox56':_(u'Без транзакция'),
    'm_checkBox56t':_(u'Винаги подава нулева AFT транзакция'),
    'm_checkBox24':_(u'Клиентски карти'),
    'm_checkBox23':_(u'Бонус Карти'),
    'm_checkBox21t':_(u'Спира/Пуска картов четец'),
    'm_checkBox25t':_(u'Спира/Пуска Отчисление за джакпот'),
    'm_checkBox22t':_(u'Спира/Пуска кей система'),
    'm_checkBox20t':_(u'Спира/Пуска SAS комуникация'),
    'm_checkBox24t':_(u'Спира/Пуска клиентски карти'),
    'm_checkBox23t':_(u'Спира/Пуска Бонус карти'),

    'm_checkBox27':_(u'Свери час'),
    'm_checkBox311':_(u'Провери за игра'),
    'm_checkBox37':_(u'AFT key 43'),
    'm_checkBox39':_(u'Забави рилл'),
    'm_checkBox26':_(u'SAS Сигурност'),
    'm_checkBox28':_(u'AFT'),
    'm_checkBox281':_(u'USB2RS'),
    'm_checkBox391':_(u'Забави комуникация'),
    'm_checkBox27t':_(u'Синхронизира дата и час на машина със сървър'),
    'm_checkBox311t':_(u'Задължително за машини на EGT'),
    'm_checkBox37t':_(u'Използва се при някой версии на Vega'),
    'm_checkBox39t':_(u'Блокира аутоплей на EGT след рестарт. Цел сигурност'),
    'm_checkBox26t':_(u'Блокира машината ако влезе легаси без SMIB модула'),
    'm_checkBox28t':_(u'Активира AFT протокол'),
    'm_checkBox281t':_(u'Използва USB към RS232 кабел'),
    'm_checkBox391t':_(u'Забавя комуникацията. За КТ с ARM процесор'),

    'm_checkBox31':_(u'Изплащане на ръка'),
    'm_checkBox29':_(u'Заключи при загуба'),
    'm_staticText37':_(u'Брой Грешки'),
    'm_staticText38':_(u'Падане при кредит'),
    'm_checkBox31t':_(u'Джакпота се изплаща на ръка. За някой megajack или по желание'),
    'm_checkBox29t':_(u'Заключва машината ако загуби сървър. Отключва при намиране. При примигване провери кабел.'),
    'm_spinCtrl13t':_(u'Заключва при загуба на сървър Х умножено по време за грешка в комуникация. 20*10 секъунда = 200 секунди'),
    'm_spinCtrl14t':_(u'Ако кредита е по-малко от зададения, не е възможно падане на мистерия.'),

    'm_checkBox30':_(u'Заключи бил без клиент'),
    'm_checkBox321':_(u'Заключи без клиент'),
    'm_staticText522':_(u'Таймаут'),
    'm_staticText682':_(u'Кредит'),
    'm_checkBox30t':_(u'Заключва бил ако няма клиентска карта'),
    'm_checkBox321t':_(u'Машината е заключена ако няма поставена карта на клиент'),
    'm_spinCtrl201t':_(u'Време за изтриване на клиент след премахване на карта'),
    'm_spinCtrl211t':_(u'Бонус се отваря ако кредита падне под посочената сума'),
    'm_textCtrl26t':_(u'Време за реакция на реле'),
    'm_staticText43':_(u'Удържане над'),
    'm_staticText67':_(u'Scantime'),
    'm_staticText68':_(u'Timeout'),
    'm_button391':_(u'Запиши Четец'),
    'm_staticText42':_(u'Изтрий на буфер'),
    'm_checkBox341':_(u'Уведоми при печалба'),
    'm_staticText681':_(u'Сума'),
    'm_spinCtrl19t':_(u'При кредит по-голям от зададения, бонуса се удържа'),
    'm_spinCtrl22t':_(u'Време на сканиране на четеца'),
    'm_spinCtrl23t':_(u'Генерира грешка при липса на карта след Х секунди'),
    'm_button391t':_(u'Препрограмира картовия четец. Влияе на цялата система.'),
    'm_spinCtrl18t':_(u'Ако крупието задържа картата (избягва двойно падане на бонус)'),
    'm_checkBox341t':_(u'Изпраща E-mail при печалба'),
    'm_spinCtrl24t':_(u'Ако печалбата е равна или по-голяма от посочената (върната в едно завъртане)'),

    'm_checkBox35':_(u'Изпращай към сървър'),
    'm_staticText54':_(u'IP'),
    'm_staticText521':_(u'Ниво'),
    'm_checkBox35t':_(u'Записва грешки от SMIB в база на сървъра'),
    'm_textCtrl14t':_(u'Позволява наблюдение от друг компютър. Иска допълнителна сервизна програма.'),
    'm_choice16t':_(u'Ниво на грешките които да се записват.'),

    'm_checkBox32':_(u'Много ключове'),
    'm_checkBox33':_(u'AFT'),
    'm_staticText39':_(u'Канал 1'),
    'm_staticText40':_(u'Канал 2'),
    'm_button431':_(u'Тест на реле'),
    'm_button431t':_(u'Отваря последователно двата канала на релето'),
    'm_spinCtrl15t':_(u'Канал 1 кредит, при грешно поставен кабел промени.'),
    'm_spinCtrl16t':_(u'Канал 2 отчет, при грешно поставен кабел промени.'),
    'm_checkBox33t':_(u'Позволява вход и изход от клиентска карта.'),
    'm_checkBox32t':_(u'Могат да се използват до 5 ключа едновременно.'),

    'm_checkBox34':_(u'Рестарт при грешка'),
    'm_staticText44':_(u'Интервал на проверка'),
    'm_staticText45':_(u'Критична температура'),
    'm_checkBox34t':_(u'Рестартира SMIB ако намери грешка в системата'),
    'm_spinCtrl20t':_(u'Интервал на проверка за грешки'),
    'm_spinCtrl21t':_(u'При достигане на посочената температура изключва едно от ядрата на процесора'),

    'm_button38':_(u'Покажи лог'),
    'm_button42':_(u'Включи деноминация'),
    'm_button37':_(u'Авто Ъпдейт'),
    'm_button36':_(u'Рестарт'),
    'm_button39':_(u'Нулирай'),
    'm_button40':_(u'Изключи от джакпот'),
    'm_button41':_(u'Изключи деноминация'),
    'm_button43':_(u'Включи в джакпот'),
    'm_button38t':_(u'Показва лог файла записан на SMIB модула'),
    'm_button42t':_(u'Позволява игра на избраната деноминация.'),
    'm_button37t':_(u'Извършва ъпдейт на SMIB модула. Изисква интернет връзка.'),
    'm_button36t':_(u'Софтуерен рестарт на SMIB'),
    'm_button39t':_(u'Връща фабричните настройки'),
    'm_button40t':_(u'Избраната игра не отчислява в джакпот сървъра.'),
    'm_button41t':_(u'Забранява играта на избраната деноминация'),
    'm_button43t':_(u'Включва отчислението на избраната игра'),

    'm_staticText48':_(u'Сървър'),
    'm_staticText46':_(u'Система'),
    'm_staticText50':_(u'Кей система'),
    'm_staticText52':_(u'Джакпот'),
    'm_staticText49':_(u'RFID'),
    'm_staticText47':_(u'SAS'),
    'm_staticText51':_(u'Бонус Карти'),
    'm_staticText53':_(u'Клиенти'),

    'm_button35':_(u'Запис'),
    1:_(u'Всички'),
    'm_checkBox42':_(u'Спри аутоплей'),
    'm_checkBox42t':_(u'Спира аутоплей на ЕГТ'),
    'm_spinCtrl26t':_(u'Спира аутоплей при печалба = или > от посочената'),
    'm_spinCtrl27t':_(u'Аутоплей ще тръгне след Х минути, 0 не пуска бутона до отключване на SMIB'),
    'm_checkBox47':_(u'Проверка процеси'),
    'm_checkBox48':_(u'Проверка нет'),
    'm_checkBox50':_(u'Проверка система'),
    'm_checkBox47t':_(u'Проверява всички процеси и ги рестартира при грешка'),
    'm_checkBox48t':_(u'Проверява за достъп до сървърите, и се опитва да поправи мрежовата връзка'),
    'm_checkBox50t':_(u'Проверява температура, ампераж и напрежение на SMIB модула'),
    'm_checkBox49':_(u'Лог файл'),
    'm_checkBox49t':_(u'Записва грешките в системните логове на SMIB устройството'),
    'm_staticText801':_(u'Език'),
    'm_checkBox51t':_(u'Ако кредита не е над сумата за превъртане не позволява аут'),
    'm_checkBox51':_(u'Аут под сума'),
    'm_checkBox57':_(u'Използвай AFT'),
    'm_checkBox79':_(u'Мънибек'),
    'm_staticText90':_(u'SAS Номер'),
    'm_staticText92':_(u'Сериен таймаут'),
    'm_staticText89':_(u'AFT заключване'),
    'm_spinCtrl30': _(u'Мили секунди (0, 100, 200, ...'),
    'm_checkBox80':_(u'Транзакция от EMG')

}

SMIB_SaveSection = {'name':_(u'Запиши конфигурация'),
                    'm_button58':_(u'Затвори'),
                    'm_button59':_(u'Запис')}
# Sys
config_Sys = {
    'name':_(u'Настройки/Системни'),
    1:_(u'Система'),
    2:_(u'Мрежа'),
    3:_(u'Принтер/Картов четец'),
    4:_(u'Работни станции'),
    5:_(u'Кей Система'),
    6:_(u'База Данни'),
    7:_(u'SMIB'),
    8:_(u'Ъпдейт'),
}
# AddBonusCart
config_AddBonusCart = {
    'name':_(u'Добавяне на бонус карта'),
    'm_staticText38':_(u'Имe за разпознаване'),
    'm_staticText39':_(u'Стойност'),
    'm_staticText69':_(u'Превърти'),
    'm_radioBox1':[_(u'Статична стойност'),_(u'Статична с удържане'),_(u'1 към 1'),_(u'1 към 1 с удържане'),_(u'Умножена по 2'),_(u'Умножена по 2 с удържане'),_(u'Не усвояем вход')],
    'm_checkBox52':_(u'Задължителен клиент'),
    'm_checkBox52t':_(u'Изисква клиентска карта за да падне'),
    'm_radioBtn7':_(u'Активна'),
    'm_radioBtn8':_(u'Неактивна'),
    'm_staticText46':_(u'Номер на карта'),
    'm_staticText47':_(u'Съществува'),
    'm_button28':_(u'Затвори'),
    'm_button29':_(u'Запис'),
}
# BonusCartSave
config_BonusCartSave = {
    'name':_(u'Запис на бонус карти'),
    'm_button23':_(u'Затвори'),

}
# ReadBonusCart
config_ReadBonusCart = {
    'name':_(u'Добавяне на карта'),
    'm_button7':_(u'Затвори'),
    'm_button8':_(u'OK'),
    1:_(u'Моля поставете карта в четеца!'),
    2:_(u'Моля извадете карта!'),
    3:_(u'Картата се използва!'),
}
# BonusCart
config_BonusCart = {
    'name':[_(u'Настройки/Бонус Карти'),_(u'Настройки')],
    1:_(u'Номер'),
    2:_(u'Име'),
    3:_(u'Стойност на карта'),
    4:_(u'Тип на карта'),
    5:_(u'Нова карта'),
    6:_(u'Активирай нова карта'),
    7:_(u'Затвори'),
    8:_(u'Статична стойност'),
    9:_(u'Статична стойност с удържане'),
    10:_(u'Стойноста умножена по 2'),
    11:_(u'Стойноста умножена по 2 с удържане'),
    12:_(u'Стойност 1 към 1'),
    13:_(u'Стойност 1 към 1 с удържане'),
    14:_(u'Създаване на нова карта'),
    15:_(u'Запис на всички карти в машините'),
    16:_(u'Връща в предходното меню'),
    17:_(u'Двоен клик редактира'),
    18:_(u'Неуспешен запис'),
    19:_(u'Запис бонус карти'),
    20:_(u'Не усвоямен вход'),
}
# Abaut
config_Abaut = {
    'name':_(u'Относно'),
    'm_staticText54':_(u'Версия'),
    'm_staticText56':_(u'DB ревизия'),
    'm_staticText58':_(u'Редирект сървър'),
    'm_staticText60':_(u'Спонсор'),
    'm_staticText62':_(u'E-mail'),
    'm_button38':_(u'Затвори'),
    'm_staticText73':_(u'Ревизия'),
    'm_button52':_(u'Какво ново'),
}
# MainConf
config_MainConf = {
    'name':[_(u'Настройки'), _(u'Начало')],
    1:_(u'Управление на потребителите в системата'),
    2:_(u'Настройки на машини и броячи'),
    3:_(u'Настройки на бонус карти'),
    4:_(u'Настройки на джакпот сървър'),
    5:_(u'Системни настройки'),
    6:_(u'Добавяне на лицензи'),
    7:_(u'Рестартиране на програмата. За да влязат в сила системните настройки.'),
    8:_(u'Документация на програмата'),
    9:_(u'Информация за версията и ревизията'),
    10:_(u'Връща в предходно меню'),
}

# Report MonyOpis
report_mony_Opis = {
    'name':_(u'Опис на пари'),
    1: _(u'Не обобщена'),
    2:_(u'Всички'),
    3:_(u'Дата'),
    4:_(u'Крупие'),
    5: _(u'Тотал'),
    6:_(u'Брой'),
    7:_(u'Банкноти'),
    8:_(u'Общо'),
    9:_(u'Номер'),

}
# report_WorkTime
report_WorkTime = {
    1: _(u'Обобщена'),
    2:_(u'Всички'),
    3:_(u'Потребител'),
    4:_(u'Начало на смяна'),
    5:_(u'Край на смяна'),
    6:_(u'Часове'),
    7:_(u'Не обобщена'),
    'name':_(u'Работно време')
}

service_Main = {
    'name': _(u'Сервиз'),
    'm_tool4':_(u'Затвори'),
    'm_tool4m':_(u'Връща в предходно меню'),
    'm_tool2':_(u'Нова задача'),
    'm_tool3':_(u'Стоп Аларма'),
    'm_tool41':_(u'Старт Аларма'),
    'm_tool5':_(u'Ремонт'),
    'm_tool6':_(u'Мониторинг'),
    'm_tool6m':_(u'Мониторинг на всички машини'),
    'm_tool2m':_(u'Отваря нова задача за сервиза'),
    'm_tool3m':_(u'Спира алармата на машината'),
    'm_tool41m':_(u'Пуска алармата на машината'),
    'm_tool5m':_(u'Изпълнение на задачата за ремонт'),
    1:_(u'Няма'),
    2:_(u'Номер'),
    3:_(u'Модел'),
    4:_(u'Сериен Номер'),
    5:_(u'Инфо'),
    6:_(u'Дата'),
}

service_NewTask = {
    'name': _(u'Нов ремонт'),
    'm_staticText1':_(u'Машина'),
    'm_button1':_(u'Затвори'),
    'm_button2':_(u'Запис'),
    1:_(u'Машина'),
    2:_(u'Потребител'),
    3:_(u'Проблем'),
    4:_(u'Липсва'),
    5:_(u'Всички SMIB'),
    6:_(u'Изпълни команда'),

}

service_Fix = {
    'name':_(u'Ремонт'),
    'm_radioBtn1':_(u'Без Нулиране'),
    'm_radioBtn1t':_(u'Машината не се нулира'),
    'm_radioBtn2':_(u'Нулиране'),
    'm_radioBtn2t':_(u'Ще нулира машината'),
    'm_checkBox1':_(u'Отчети Ръчно'),
    'm_checkBox1t':_(u'Отчета ще е ръчен. В противен случай ще опита автоматичен отчет.'),
    'm_checkBox2':_(u'Извади Бил'),
    'm_checkBox2t':_(u'Ще се извадят парите от касетата на била.'),
    'm_checkBox3':_(u'Без Отчет'),
    'm_checkBox3t':_(u'Няма да се отчита машината'),
    'm_staticText2':_(u'Сума на ремонт'),
    'm_staticText3':_(u'Описание'),
    'm_button3':_(u'Затвори'),
    'm_button4':_(u'Поправи'),
    'm_checkBox4':_(u'Трансфер на пари'),
    'm_checkBox4t':_(u'Ще прехвърли парите на крупие.'),

}

report_mashin_FixLog = {
    1:_(u'Производител'),
    2:_(u'Всички'),
    'name': _(u'Ремонти'),
    3:_(u'Дата'),
    4:_(u'Потребител'),
    5:_(u'Инфо'),
    6:_(u'Машина'),
    7:_(u'Модел'),
    8:_(u'Сериен номер'),
    9:_(u'Дата Ремонт'),
    10:_(u'Ремонт инфо'),
    11:_(u'Нулиране'),
    12:_(u'Ремонт Потребител'),
    13:_(u'Сума'),
    14:_(u'Общо'),
    15:_(u'ДА'),
}
report_mashin_NullDevice = {
    1:_(u'Произвожител'),
    2:_(u'Всички'),
    'name': _(u'Нулиране'),
    3:_(u'Машина'),
    4:_(u'Модел'),
    5:_(u'Сериен Номер'),
    6:_(u'Дата'),
    7:_(u'Вход'),
    8:_(u'Изход'),
    9:_(u'М. Вход'),
    10:_(u'М. Изход'),
    11:_(u'Бил'),
    12:_(u'Потребител'),
}

# MAIN SETEMGTIME
set_emg_time={
    'name':_(u'Свери час на EMG'),
    'm_staticText11':_(u'Дата'),
    'm_staticText12':_(u'Формат 06.30.2020'),
    'm_staticText111':_(u'Час'),
    'm_staticText121':_(u'Формат 12:35'),
    'm_button19':_(u'Затвори'),
    'm_button20':_(u'Запис'),
              }

# cust ReplaceGroupRow
msg_ReplaceGroupRow = {
    1:_(u'Име'),
    2:_(u'Променя бонус по тотал'),
    3:_(u'ДА'),
    4:_(u'От Група'),
    5: _(u'Към група'),
    'name':_(u'Правила за смяна на група'),
    'm_button22':_(u'Затвори'),
    'm_listCtrl4':_(u'Двоен клик редактира'),
    'm_bpButton9':_(u'Премахва правило'),
    'm_bpButton10':_(u'Добавя правило'),
}
msg_NewGroupReplaceRight = {
    'name':_(u'Правило'),
    'm_checkBox57':_(u'По текущ тотал'),
    'from_time':_(u'От Час'),
    'to_time':_(u'До Час'),
    'm_staticText83':_(u'Име на правило'),
    'm_staticText84':_(u'Група'),
    'm_staticText85':_(u'Да стане'),
    'm_checkBox41':_(u'Понеделник'),
    'm_checkBox43':_(u'Вторник'),
    'm_checkBox45':_(u'Сряда'),
    'm_checkBox47':_(u'Четвъртък'),
    'm_checkBox42':_(u'Петък'),
    'm_checkBox44':_(u'Събота'),
    'm_checkBox46':_(u'Неделя'),
    'm_checkBox49':_(u'Винаги'),
    'm_button24':_(u'Затвори'),
    'm_button25':_(u'Запис'),
    'm_checkBox451':_(u'При тотал от'),
    'm_spinCtrl411':_(u'Гупата ще се сменя при тотал от предходен ден до посочената сума'),

}

del_old_data= {
    'name':_('Изтриване на стара информация'),
    'm_button23':_(u'ОК'),
}


clean_user_loged_in = {
    'name': _(u'Отключи потребители'),
    'm_staticText16': _(u'Администратор'),
    'm_staticText17': _(u'Парола'),
    # 'm_staticText18': _(u'Pos Име'),
    'm_button30': _(u'Затвори'),
    'm_button31': _(u'Отключи'),
}

bonus_cart = _(u'Бонус Карти')
bonus_cart_hold = _(u'Удържани Бонус Карти')
aft_in = _(u'Виртуален IN')
aft_out = _(u'Виртуален OUT')
mony_transfer = _(u'Трансфер')

report_custCount = {
    'name':_(u'Количество карти'),
    1:_(u'Обобщено по клиент'),
    2:_(u'Клиент'),
    3:_(u'Брой Карти'),
    4:_(u'Общо раздадени'),
    5:_(u'Разбита справка'),
    6:_(u'Дата на създаване'),
    7:_(u'Номер на карта'),
    8:_(u'Създадено от'),
    9:_(u'Не се използва календар'),
}

user_HOLD_mony = {
    'name':_(u'Удържане на липса'),
    'm_staticText10':_(u'Сума за удържане на липса'),
    'm_staticText11':_(u'Потребител'),
    'm_staticText12':_(u'Общо задължение'),
    'm_button9':_(u'Затвори'),
    'm_button10':_(u'Запис'),
}

# Cust Reserve
cust_reserve_class = {
    'name': cust_reserve,
    'm_staticText85':_(u'Клиент: %s'),
    'm_staticText86':_(u'Дата (31.12.2020)'),
    'm_staticText87':_(u'Час (11:45)'),
    'm_button25':_(u'Отказ'),
    'm_button26':_(u'Запис'),
    'm_staticText89':_(u'Машина'),
    'm_textCtrl15t':_(u'Дата във формат 31.12.2020'),
    'm_textCtrl16t':_(u'Час във формат 11:45'),
}

EditOrderNom = {
    'name':_(u'Редакция на номер на отчет'),
    'm_button14':_(u'Запис'),
    'm_button13':_(u'Затвори'),
    'm_textCtrl1':_(u'Цяло число'),
}
EditOrderDates = {
    'name':_(u'Редакция на дата на отчет'),
    'm_button14':_(u'Запис'),
    'm_button13':_(u'Затвори'),
    'm_textCtrl1':_(u'Формат Година-Месец-Дата'),
}

mounths = {
    '01':_(u'Януари'),
    '02':_(u'Февруари'),
    '03':_(u'Март'),
    '04':_(u'Април'),
    '05':_(u'Май'),
    '06':_(u'Юни'),
    '07':_(u'Юли'),
    '08':_(u'Август'),
    '09':_(u'Септември'),
    '10':_(u'Октомври'),
    '11':_(u'Ноември'),
    '12':_(u'Декември'),
}

MonyBackInUser = {
    'name':_(u'Натрупан Мънибек'),
    'm_radioBtn10':_(u'Сортирай по сума'),
    'm_radioBtn7':_(u'Сортирай по клиент'),
    1:_(u'Клиент'),
    2:_(u'Сума'),
    3:_(u'Общо')
                  }

DrawBackInUser = {
    'name':_(u'Натрупани Точки'),
    'm_radioBtn10':_(u'Сортирай по брой'),
    'm_radioBtn7':_(u'Сортирай по клиент'),
    1:_(u'Клиент'),
    2:_(u'Брой'),
    3:_(u'Общо')
                  }

RKO_Copy = {
    'm_button6':_(u'Покажи'),
    1: _(u'Номер'),
    2: _(u'Дата'),
    3: _(u'Клиент'),
    4: _(u'Издал'),
    5: _(u'Сума')

            }

cust_cart_price = {'title': _(u'Цена на карта'),
             1:_(u'Група'),
             2:_(u'Брой'),
             3:_(u'Цена'),
             'm_button22':_(u'Затвори')
             }

cust_SetCartPrice = {
            'title':_(u'Цена на карта'),
            'm_staticText91':_(u'Брой карти'),
            'm_staticText92':_(u'Група'),
            'm_staticText93':_(u'Цена'),
            'm_button27':_(u'Отказ'),
            'm_button28':_(u'Запис'),
}

odrer_SelectUser = {
    'title':_(u'Избери смяна'),
    'm_staticText36':_(u'Потребител'),
    'm_button18':_(u'Отказ'),
    'm_button19':_(u'Запис')
}

report_MonyOnCart = {
    'name':_(u'Пари по карта'),
    1:_(u'Клиент'),
    2:_(u'Сума'),
    3:_(u'Общо'),
}

conf_NRA = {
    'name':_(u'НАП Токен'),
    'm_staticText82':_(u'Клиент ID'),
    'm_staticText83':_(u'Токен PROD'),
    'm_staticText84':_(u'Валиден до'),
    'm_button59':_(u'Затвори'),
    'm_button60':_(u'Запис')
}

DevType = {
    'name':_(u'Тип на машина'),
    'm_button13':_(u'Затвори'),
    'm_button14':_(u'Запиши'),
           }

SelectDate_Cust_statistic_DEL = {'name': _(u'Избери Дата'),
                                 'm_button41': _(u'Затвори'),
                                 'm_button42':_(u'Изтрий')}