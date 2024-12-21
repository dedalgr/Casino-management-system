#-*- coding:utf-8 -*-
import config
import os
from subprocess import Popen, PIPE

KEY = '''vc3Qtq+Qf0k7PJSwDlJKw44HpS/+jU6+dFMRxCuy6g5Hw235NLAS5YAa1c/FPboGNCfUGnW/shvpQIEfGuTYpgHgXH3M9s47jTvs9tRsof/bhH1Lrk+cZrKfLp8vaGvNTiiMYGz1Uyv2tyylkGUA5tY1c4MA/v7O3eZnk1OeLvVVqqLxr5cxOf45jKCX+hxV2skR9H2qAYXMTiwmjwVRMjlvbyMyCxxS3DeUvdoFibCcw12f/D1nbIa6sHFXNY9U9/gp4m9+Xt5xyw6SRotllTQxX2zoBfAnYXftL3VHSAcStPiYyd2EocUd738Fvj1u'''
RAND_KEY = '''KRJGxB0HYzmWFxoZxYwnMxDz9ZRu6dA50hC-SwVelKsV9_i2nbJOEGVCeN8rhRXsF3nNtxz7m5KDUMnAUBGhcov4l5uC66PgGIgQjPXOhXITsliUbH51J4eR050VPSURyF492TYXfC_BeQIR4qyGozWhfl2vULIkng48vvLSGF2v2g9tsk417I9RFbs-DV4fGPFpNqFnKXeXysUN4el_vknSPyiSrhJ1aM6x1zD3TeDqqpbdybhUIF8-05L0u4k06csbz5xkOaKeDkm98aVIfoB81-BpQljkzNc1Ou6D8J5TvSaWF13JAGKJlj9fCbrRE4ieU_oLC-9QbC0F2Vfzaj7f5lZUh47w6PmgqGUJdgQrGxugx4nsZwXKqO26qjmt4n1faqjqk36nZruXGhMBltqVQ5SEJFfzC7lXpjlPuwXuJ0qbLuMoHnQ3sI8R3ViqMfs0Q0UkdXqu-VlzQM0mEQ=='''

PRIVATE_KEY = '''-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEAtaRy1R+IGQ/3Vjt42aqM8Q2kqkB9ZkvltQIPaq/nvYHm8Vr9wcZ8
+3ABQbvZumi3dTpjKNnAcVTEtnFyDAm0eieyKngrfU/7k5C66gZQY0o6bP459QnlpHnlgC
GoO5pfnfpF+qLf2cJRnvxwG8zK1kL/+NBAbezaFc11AtHCzrksIZGhX+jxDzI/nDQKuFPi
ipbyQW2zo+xh5jHxXkoTv7iNs19ct0lxD31jz3++Y4bbAA/BqcR3gtUFnzy/7lUWeEXHGL
CFBzHVDGxYz7xu1bDwMyfadUROTmFwoTo4cZTDUaqnpgcuJwhEeMcpkgrwykaV/UZn7+TE
gNyvcTDiMtqY/D61DGLYNaN/i4NQV/f6rS42tvxO89LOSdgGaQUdILHOgaU7rVD5Ke9hkP
2B7XoyeCZdgnWux7ONum9hkIvxQ93jCo1w+JvKfFfu1du+CArpWfiX1o3vcl5mON7kPbK1
jiLGnGOy3La52YZJ1vY/dy7w0cAgE9rMIElbWI5XAAAFiLfXIOG31yDhAAAAB3NzaC1yc2
EAAAGBALWkctUfiBkP91Y7eNmqjPENpKpAfWZL5bUCD2qv572B5vFa/cHGfPtwAUG72bpo
t3U6YyjZwHFUxLZxcgwJtHonsip4K31P+5OQuuoGUGNKOmz+OfUJ5aR55YAhqDuaX536Rf
qi39nCUZ78cBvMytZC//jQQG3s2hXNdQLRws65LCGRoV/o8Q8yP5w0CrhT4oqW8kFts6Ps
YeYx8V5KE7+4jbNfXLdJcQ99Y89/vmOG2wAPwanEd4LVBZ88v+5VFnhFxxiwhQcx1QxsWM
+8btWw8DMn2nVETk5hcKE6OHGUw1Gqp6YHLicIRHjHKZIK8MpGlf1GZ+/kxIDcr3Ew4jLa
mPw+tQxi2DWjf4uDUFf3+q0uNrb8TvPSzknYBmkFHSCxzoGlO61Q+SnvYZD9ge16MngmXY
J1rsezjbpvYZCL8UPd4wqNcPibynxX7tXbvggK6Vn4l9aN73JeZjje5D2ytY4ixpxjsty2
udmGSdb2P3cu8NHAIBPazCBJW1iOVwAAAAMBAAEAAAGARv0vN+Xr3cekpZn2oDMMhEUNvt
AXcjxlWPmmJs76pdC3/knOdMXrIKVkiFkvPbAhSvp3uIZptKEphBgQN24vj7Il6n0umfoB
W2mr8zxmfHeNH/23jvHAQyi0rf/5bNnnVqlyYgL3s3ZDSfxkoCjIeTaULZzOIWf4z56NhX
2PQhWSjsgIpqA2XfcIbzbTnbiDCCD4KuQB2iXPGRUZvPz8fOhW0OyLIsLcIe6ibH0DXohc
3MhLqtqyznoMiXBHnpC338Q3lEJHX+Vbynm17JXYDWMoudgV6GKGTyrpw8dT5FLYPUjcch
bBT0Of9853xLRQ52wpb8uxNI8nGH5ckJr4Ekz2Zael8PrMvRnTJ8wK5BcCkudom685NMDn
ymiJtiX15+6XNujbUZ0qmbLS5Xoir0WcZIFFTqt0W5RXSCOyKmMedar/hoMX+1kKCabfEw
x3rpMBh0AueUaoad3CcF8CFUbaqj5pZx/awQvinpU/68EKfa1UJpP/PfmvnGFI5F/RAAAA
wG2RvS8hefhkCuqJzciz4/BgCVTLtJIFx1TyJ8Kac+8gi8UNNyU/2cJpU5deGCuqxescSN
Kdg02uM8O+tW6f7LjvKTJpkkkxO3vNuIty4LAN14l/wvIVZBaqPQAG+Zzuc/qPT4uEWLth
uHhXy+tHcljW5NVFqH+A2GMMvGM3gmmoBYeBJgddkkg5H1YmFmvnoh7Qule+umadCjRJAn
/kuW2XVRM4xXqvF4LJs+NLvYXcGOXaNWJkEx5GIMeG80laTQAAAMEA3ovqgvDZGw/TV1/2
ZfkQytDtsfulNko+BulqJEUdbfWkyPqLxlNtbyVGwqi3icWZaS4aImAtER74Gi3HvEcGgX
nSGp21HaxO1oc4yHBCyyv3+dyDKAJdI4jnKKoeDXgfAl7YDIxa0mKLGLIHZJN6WFFY/UaO
sqGt6PBYyH/ZmfhYXRAWqJLBfw8sn6N9iDE2J8B3h1zRc0wq460hlI2eTN/Gsy9vQr6yBH
nIAhcpegH0dqJpKluevEtHfNZWMysPAAAAwQDQ8nMQU/CgMa6NFWp0wogJ8YJ/4p4rAztj
7qLDB+tU8/DJLyWmPUTcazWmEA6XUT/LOyhZEGDoi0qmiUYMktsH0FVQF6S+FI/KDO6AKA
ueoPxaw6iNm9VeSRPseQnNxBqnsHlJNXEJivfjgjYZSydXqveA6h/fCvSJPS0fzXchgwwV
0MFDZgk2/izVJkwpvSyKxwAWfzZTiJhN+8wXfph8Z1kmez7oP+LH64JnSEf2hER1UkqLvD
PXd2T+byOsiDkAAAAPZGVkYWxAZGViaWFuLTExAQIDBA==
-----END OPENSSH PRIVATE KEY-----'''

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))

def get_ip(**kwargs):
    f = os.popen('sudo ifconfig | grep "192.168" | cut -d" " -f10')
    your_ip = f.read()
    return your_ip[:-1]

# def passwd_change():
#     if DEBUG == True:
#         return True
#     command = 'encfsctl autopasswd %s' % ('/home/colibri/.colibri')
#     # cat /proc/cpuinfo | grep Serial
#     old_passwd = get_ip()
#     new_passwd = os.popen("udevadm info --query=all --name=/dev/mmcblk0p1 | grep ID_SERIAL").read()[:-1]
#     cmd = 'printf "%s\n%s\n%s\n" | sudo cryptsetup luksAddKey /home/colibri/colibri.img' % (old_passwd, new_passwd, new_passwd)
#     os.system(cmd)
#     return True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))

def debug():
    return BASE_DIR == '/home/dedal/Colibri/Jackpot'

DEBUG = debug()
IN_THREAD = False
# IV_JUMP = True
CONF_FILE = 'server.conf'

def ssh_port():
    cmd = 'sudo grep Port /etc/ssh/sshd_config'
    data = os.popen(cmd).read()
    data = data.replace('Port ', '')
    try:
        data = int(data)
    except ValueError:
        try:
            cmd = 'sudo grep "\<Port\>" /etc/ssh/sshd_config'
            data = os.popen(cmd).read()[:-1]
            data = data.replace('Port ', '')
            data = int(data)
        except ValueError:
            return None
    return data


my_ssh_port = ssh_port()


class ConfFile(config.ConfFile):

    def __init__(self, conf_file):
        try:
            config.ConfFile.__init__(self, conf_file)
            self.option_update()
        except config.NotConfigFile:
            config.ConfFile.__init__(self, conf_file, make_new=True)
            self.new()

    def option_update(self):
        try:
            self.get('system', 'mem_timeout', 'int')
        except:
            self.add_option('system', mem_timeout=5)
        try:
            self.get('UDP', 'iv_jump', 'bool')
        except Exception as e:
            print(e)
            self.add_option('UDP', iv_jump=False)

    def read_db_n(self):
        if os.name == 'posix':
            var = os.popen('df -h | grep -w /').read()
            var = var.split()
            cmd = 'udevadm info --query=all --name=%s | grep ID_SERIAL=' % (var[0])
            data = os.popen(cmd).read()
            # data = data.replace('E: ID_SERIAL=', '')
            return data[:-1]
        else:
            var = os.popen('vol').read()
            var = var.split()
            return var[-1]

    def change_pass(self, **kwargs):

        # command = 'encfsctl autopasswd %s' % ('/home/colibri/.colibri')
        old_passwd = get_ip()
        if 'new_passwd' not in kwargs:
            new_passwd = self.read_db_n()
        else:
            new_passwd = kwargs['new_passwd']
        # command = command.split()
        # p = Popen([] + command, stdin=PIPE, stderr=PIPE, universal_newlines=True)
        # sudo_prompt = p.communicate(old_passwd + '\n' + new_passwd + '\n')[1]

        cmd = 'printf "%s\n%s\n%s\n" | sudo cryptsetup luksAddKey /home/colibri/colibri.img' % (old_passwd, new_passwd, new_passwd)
        os.system(cmd)
        cmd = 'udevadm info --query=all --name=%s | grep ID_SERIAL=' % ('/dev/mmcblk1p1')
        data = os.popen(cmd).read()
        if data:
            cmd = 'printf "%s\n%s\n%s\n" | sudo cryptsetup luksAddKey /home/colibri/colibri.img' % (old_passwd, data, data)
            os.system(cmd)
        os.system('printf "%s\n" | sudo cryptsetup luksRemoveKey /home/colibri/colibri.img' % (old_passwd))
        return True

    def new(self):
        self.add_section('system')
        # conf_file.add_option('system', version='1_1')
        self.add_option('system', jp_grup_block_time=1)
        # conf_file.add_option('system', iv_jump=False)
        self.add_option('system', down_count=1)
        self.add_option('system', q_count=50)
        self.add_option('system', not_chk_on_start=True)
        self.add_option('system', mem_timeout=4)

        self.add_section('UDP')
        #     conf_file.add_option('UDP', protocol='TCP')
        #     conf_file.add_option('UDP', threading=False)
        self.add_option('UDP', udp_buffer=4096)
        self.add_option('UDP', smib_port=30593)
        self.add_option('UDP', server_port=2522)
        self.add_option('UDP', visual_timeout=0)
        self.add_option('UDP', visual_port=2552)
        self.add_option('UDP', udp_timeout=12)
        self.add_option('UDP', iv_jump=False)

        self.add_section('LOG')
        self.add_option('LOG', log_file='server.log')
        self.add_option('LOG', use_file=False)
        self.add_option('LOG', msg_log=True)
        self.add_option('LOG', count=1)

        self.add_section('RTC')
        # conf_file.add_option('RTC', use=True)
        self.add_option('RTC', I2C_Bus=2)
        self.add_option('RTC', bug=False)
        self.add_option('RTC', timezon='Europe/Sofia')
        try:
            self.change_pass()
        except Exception as e:
            print(e)
    
    

conf_file = ConfFile(CONF_FILE)

POLY = 0x104c11db7
CONST = 0xfe7830a5
GAME = ['clasic', 'time']

# system
VERSION = '2_1'
ROOT_PATH = os.path.dirname(os.path.abspath('__file__'))
JP_BLOCK_TIME = conf_file.get('system', 'jp_grup_block_time', 'int')

DOWN_COUNT = conf_file.get('system', 'down_count', 'int')
Q_COUNT = conf_file.get('system', 'q_count', 'int')
# DB
# DB_NAME = conf_file.get('DB', 'db_name', 'str')
# DB_PATH = conf_file.get('DB', 'db_path', 'str')
# DB_BACKUP_PATH = conf_file.get('DB', 'db_backup_path', 'str')

# UDP
# PROTOCOL = conf_file.get('UDP', 'protocol', 'str')
MEM_TIMEOUT = conf_file.get('system', 'mem_timeout', 'int')
UDP_BUFFER = conf_file.get('UDP', 'udp_buffer', 'int')
UDP_JP_PORT = conf_file.get('UDP', 'server_port', 'int')
UDP_TIMEOUT = conf_file.get('UDP', 'udp_timeout', 'int')
UDP_VISUAL_TIMEOUT = conf_file.get('UDP', 'visual_timeout', 'int')
UDP_SMIB_PORT =  conf_file.get('UDP', 'smib_port', 'int')
UDP_VISUAL_PORT = conf_file.get('UDP', 'visual_port', 'int')
IV_JUMP = conf_file.get('UDP', 'iv_jump', 'bool')

# SLEEP_BETWEN_LONG_MSG = conf_file.get('UDP', 'sleep_betwen_long_msg', 'float')

# log
ERR_LOG = conf_file.get('LOG', 'log_file', 'str')
ERR_USE_FILE = conf_file.get('LOG', 'use_file', 'bool')
ERR_MSG_LOG = conf_file.get('LOG', 'msg_log', 'bool')
ERR_LOG_COUNT = conf_file.get('LOG', 'count', 'int')

# RTC
# RTC_USE = conf_file.get('RTC', 'use', 'bool')
RTC_Bus = conf_file.get('RTC', 'I2C_Bus', 'int')
RTC_BUG_FIX = conf_file.get('RTC', 'bug', 'bool')
RTC_TIME_ZONE = conf_file.get('RTC', 'timezon', 'str')
if DEBUG == True:
    NOT_CHK_ON_START = True
else:
    try:
        NOT_CHK_ON_START = conf_file.get('system', 'not_chk_on_start', 'bool')
    except:
        NOT_CHK_ON_START = False

IP_TABLESS = [
    'sudo iptables -F',
    'sudo iptables -A INPUT -p icmp -j ACCEPT', # Позволява пинг използва се за проверка от SMIB
    'sudo iptables -A INPUT -s 127.0.0.1/24 --j ACCEPT', # Отваря всички локални портове
    'sudo iptables -I INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT', # Позволява използването на интерне
    'sudo iptables -A INPUT -p tcp --dport %s -j ACCEPT'  % (my_ssh_port), # Позволява връзка към SSH, Иска ключ
    # 'sudo iptables -A INPUT -p tcp --dport %s -j ACCEPT'  % (11211),
    # 'sudo iptables -A INPUT -p udp --dport %s -j ACCEPT'  % (11211),
    'sudo iptables -A INPUT -s NEW_SVN_IP -j ACCEPT', # Отваря всички портове за мен
    # 'sudo iptables -A INPUT -s 192.168.1.0/24 -j ACCEPT', # Отваря всичло за локална мрежа
    'sudo iptables -A INPUT -p udp --dport %s -j ACCEPT' % (UDP_JP_PORT), # Отваря всичло за 2522
    'sudo iptables -A INPUT -p udp --dport %s -j ACCEPT' % (UDP_VISUAL_PORT), # Отваря всичло за 2552
    'sudo iptables -A INPUT -i lo -p all -j ACCEPT',
    'sudo iptables -A INPUT -j DROP'
]
