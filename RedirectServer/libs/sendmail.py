#-*- coding: utf-8 -*-

'''
Created on 28.11.2014
Author: Grigor Kolev
'''

import smtplib
# import ssl
from email.mime.text import MIMEText
import os
import threading
import time

FROM_MAIL = 'toymail@gmail.com'
PASSWD = 'set_passwd'

def Gmail(msg, to_mail, subject=None):
    if to_mail == '':
        return False
    t = threading.Thread(target=_Gmail, kwargs={'msg':msg, 'to_mail':to_mail, 'subject':subject})
    t.start()
    return True

def _Gmail(msg, to_mail, subject=None):
    # https://www.google.com/settings/security/lesssecureapps
    # global FROM_MAIL
    # FROM_MAIL = 'colibri.cms@gmail.com'
    # FROM_MAIL = 'colibri.cms@gmail.com'
    for i in range(3):
        if to_mail != '':
    #         context = ssl.create_default_context()
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
        #         server.ehlo()
                server.starttls()
        #         server.ehlo()
                server.login(FROM_MAIL, PASSWD)
                msg = MIMEText(msg.encode('utf-8'), 'html', 'utf-8')
                if subject != None and subject != '':
                    msg['Subject'] = subject
                server.sendmail(FROM_MAIL, to_mail, msg.as_string())
                server.quit()
            except Exception as e:
                print(e)
                time.sleep(600)
            else:
                break
    return True


def sendMail(msg, to_mail, subject=None):
    FROM_MAIL = 'colibri.cms@abv.bg'
    if to_mail != '':
        sendmail_location = "/usr/sbin/sendmail" # sendmail location
        p = os.popen('%s -t -i "%s"' % (sendmail_location, to_mail), "w")
        p.write("From: %s\n" % FROM_MAIL)
        p.write("To: %s\n" % (to_mail))
        if subject != None:
            p.write("Subject: %s\n" % (subject))
        else:
            p.write("Subject: Colibri CMS\n")
        msg = MIMEText(msg.encode('utf-8'), 'html', 'utf-8')
#         p.write("\n") # blank line separating headers from body
        p.write(msg.as_string())
        status = p.close()
        return True
    return False

if __name__ == '__main__':
    print(sendMail(msg='''<html><h1>test</h1></html>''', to_mail ='grigor.kolev@gmail.com', subject='Test!'))
    print(Gmail(msg='''<html><h1>test</h1></html>''', to_mail='grigor.kolev@gmail.com', subject='Test!'))
