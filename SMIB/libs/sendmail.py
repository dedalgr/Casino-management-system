#-*- coding: utf-8 -*-

'''
Created on 28.11.2014
Author: Grigor Kolev
'''

import smtplib
# import ssl
from email.mime.text import MIMEText
import os
FROM_MAIL = 'colibri_cms@localhost'
PASSWD = 'use_system10'

def Gmail(msg, to_mail, subject=None):
    # https://www.google.com/settings/security/lesssecureapps
    global FROM_MAIL
    FROM_MAIL = 'colibri.cms@gmail.com'
    if to_mail != '':
#         context = ssl.create_default_context()
        server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.ehlo()
        server.starttls()
#         server.ehlo()
        server.login(FROM_MAIL, PASSWD)
        msg = MIMEText(msg.encode('utf-8'), 'html', 'utf-8')
        if subject != None:
            msg['Subject'] = subject
        server.sendmail(FROM_MAIL, to_mail, msg.as_string())
        server.quit()
    return True


def sendMail(msg, to_mail, subject=None):
    if to_mail != '':
        sendmail_location = "/usr/sbin/sendmail" # sendmail location
        p = os.popen("%s -t" % sendmail_location, "w")
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
