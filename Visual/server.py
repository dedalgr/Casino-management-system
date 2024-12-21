# -*- coding:utf-8 -*-
from libs.sock.udp_socket import server
from queue import PriorityQueue
import threading
import config
import log
from libs import subversion
import os

Q = PriorityQueue()

class Prioritize:

    def __init__(self, priority, item):
        self.priority = priority
        self.item = item

    def __eq__(self, other):
        return self.priority == other.priority

    def __lt__(self, other):
        return self.priority < other.priority

# def clean_q(numb=None):
#     global Q
#     if numb is None:
#         Q.queue = []
#     else:
#         tmp = []
#         for i in Q.queue:
#             if i.priority == numb:
#                 pass
#             else:
#                 tmp.append(i)
#         Q.queue = tmp
#     return Q.queue

server.LOG_SERVER.setLevel(log.LOG_LEVEL)
class Handler(server.EchoRequestHandler):

    def handle(self):
        global Q
        try:
            # self.handle_timeout()
            data = self.get_data()

            if data != None and data != False and data != self:
                log.stdout_logger.debug('server get data: %s' % (data))
                if data[0] == "set_ip":
                    Q.put(Prioritize(2, data))
                    data = True
                elif data[0] == 'get_conf':
                    data = {
                        'name':config.CONF.get('SYSTEM', 'name', 'str'),
                        'micro':config.CONF.get('SYSTEM', 'visual_micro', 'bool'),
                        'activ': config.CONF.get('FIELD', 'field_active', 'bool'),
                        'background': config.CONF.get('BACKGROUND', 'anime', 'str'),
                        'mony':config.CONF.get('SYSTEM', 'mony', 'str'),
                        'jump':config.CONF.get('UDP', 'iv_jump', 'bool'),
                        'sum_runner_rnage':config.CONF.get('SYSTEM', 'sum_runner_rnage', 'bool'),
                        'color_name': config.CONF.get('FIELD', 'color_name', 'bool'),
                        'font': config.CONF.get('FONT', 'name', 'int'),
                            }
                elif data[0] == 'set_conf':
                    config.CONF.update_option('SYSTEM', name=data[1]['name'])
                    config.CONF.update_option('SYSTEM', visual_micro=data[1]['visual_micro'])
                    config.CONF.update_option('FIELD', field_active=data[1]['field_active'])
                    config.CONF.update_option('SYSTEM', mony=data[1]['mony'])
                    config.CONF.update_option('SYSTEM', sum_runner_rnage=data[1]['sum_runner_rnage'])
                    config.CONF.update_option('UDP', iv_jump=data[1]['iv_jump'])
                    config.CONF.update_option('BACKGROUND', anime=data[1]['anime'])
                    config.CONF.update_option('FIELD', color_name=data[1]['color_name'])
                    config.CONF.update_option('FONT', name=data[1]['font'])
                    data = True
                elif data[0] == 'svn_update':
                    if os.uname()[-1] == 'armv7l':
                        var = 'ARM'
                    else:
                        var = 'Linux'
                    url = 'svn://NEW_SVN_IP/home/svn/Visual_BIN/%s/%s' % ('2_1', var)
                    connect = subversion.SubVersion(config.ROOT_PATH, url, 'smib', 'smib_update')
                    connect.checkout()
                    revision = connect.update()
                    if revision:
                        data = True
                    else:
                        data = False
                elif data[0] == 'chk_alife':
                    return True
                elif data[0] == 'ALIFE':
                    return True
                # elif data[0] == 'down_rotation':
                #     Q.put((99, data))
                #     data = True
                elif data[0] == 'REBOOT_VISUAL':
                    # clean_q()
                    Q.put(Prioritize(98, data))
                elif data[0] == 'KILL':
                    # clean_q()
                    Q.put(Prioritize(97, data))
                elif data[0] == 'DOWN':
                    # clean_q(4)
                    Q.put(Prioritize(4, data))
                    data = True
                elif data[0] == 'ERROR':
                    # clean_q()
                    Q.put(Prioritize(3, data))
                    data = True
                elif data[0] == 'SET_DB':
                    # clean_q()
                    Q.put(Prioritize(1, data))
                    data = True
                elif data[0] == 'START_RUNER':
                    # clean_q(numb=100)
                    Q.put(Prioritize(100, data))
                    data = 'NO RETURN'
                elif data[0] == 'RUNER':
                    # clean_q(numb=101)
                    Q.put(Prioritize(101, data))
                    data = 'NO RETURN'
                elif data[0] == 'ADD_BET':
                    # clean_q(numb=102)
                    Q.put(Prioritize(102, data))
                    data = 'NO RETURN'
                # elif data[0] == 'WHO':
                #     data = who()
                # elif data[0] == 'DEL_ERROR_LOG':
                #     cmd = 'cat /dev/null > %s' % (conf.ERR_LOG)
                #     os.system(cmd)
                #     data = True
                # elif data[0] == 'GET_ERROR_LOG':
                #     try:
                #         data = file(conf.ERR_LOG, 'r').read()
                #     except:
                #         data = u''
                # elif data[0] == 'INIT':
                #     DB = db.Berkeley()
                #     data = DB.get_key('INIT')
                elif data[0] == 'AUDIO_TEST':
                    Q.put(Prioritize(9, data))
                    data = True
                else:
                    data = True
                if data == 'NO RETURN':
                    pass
                else:
                    self.send_data(data)
        except Exception as e:
            self.log.critical(e, data)
        return True


def run_server(handler=Handler, **kwargs):  # @UndefinedVariable
    '''
    Стартита TCP сървър като демон.
    Използва _tcp.EchoRequestHandler
    :param port:  Порт на лоцалния TCP сървър. Взима се от conf
    :param args: Ne se podawat argumenti
    :return: Не връща резултат. Стартира безкраен демон.
    '''

    # if 'logging' in kwargs:
    #     server.LOG_SERVER = kwargs['logging']

    if 'crypt' in kwargs:
        server.CRYPT = kwargs['crypt']

    if 'use_json' in kwargs:
        server.SERVER_USE_JSON = kwargs['use_json']

    if 'timeout' in kwargs:
        server.TIMEOUT = kwargs['timeout']

    if 'buffer' in kwargs:
        server.BUFFER = kwargs['buffer']

    if 'in_thread' in kwargs:
        server.SERVER_IN_THREADING = kwargs['in_thread']

    if 'port' in kwargs:
        server.PORT = kwargs['port']

    if 'ip' in kwargs:
        server.IP = kwargs['ip']

    if 'logging' in kwargs:
        handler.log = kwargs['logging']
    else:
        handler.log = server.LOG_SERVER
    if 'rsa' in kwargs:
        handler.RSA = kwargs['rsa']
    else:
        handler.RSA = server.RSA
    address = (server.IP, server.PORT)
    handler.log.info('SERVER PROC STARTING!')
    handler.log.info('BIND: %s', address)
    handler.log.info('IN THREAD: %s', server.SERVER_IN_THREADING)
    handler.log.info('CRYPT: %s', server.CRYPT)
    handler.log.info('RSA: %s', handler.RSA)
    handler.log.info('BUFFER: %s', server.BUFFER)

    # let the kernel give us a port
    # server.LOG_SERVER.info('SERVER PROC STARTING!')
    # server.LOG_SERVER.info('BIND: %s', address)
    # server.LOG_SERVER.info('IN THREAD: %s', server.SERVER_IN_THREADING)
    # server.LOG_SERVER.info('CRYPT: %s', server.CRYPT )
    # server.LOG_SERVER.info('BUFFER: %s', server.BUFFER )

    if server.SERVER_IN_THREADING == True:
        my_server = server.ThreadedServer(address, handler)
    else:
        my_server = server.SocketServer.UDPServer(address, handler)

    # my_server._handle_request_noblock()
    my_server.allow_reuse_address = True
    my_server.allow_reuse = True
    # server._handle_request_noblock = True
    my_server.timeout = server.TIMEOUT
    handler.log.info('start server')
    t = threading.Thread(target=my_server.serve_forever)
    t.start()
    return my_server