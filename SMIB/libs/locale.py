#-*- coding:utf-8 -*-
'''
Created on 9.09.2018 г.

@author: dedal
'''

import gettext
import os


def INIT(lang='BG_bg'):
    locale_folder = os.path.abspath(os.path.join(os.path.abspath('locale')))
    gettext.install('messages', locale_folder, unicode=True, names=['ugettext'], codeset='utf-8')
    lang = gettext.translation('messages', 'locale', fallback=True, languages=[lang])
    lang.install()
    
def make_mo(local):
    for item in local:
        command = 'msgfmt -o locale/%s/LC_MESSAGES/messages.mo locale/%s/LC_MESSAGES/messages.po' % (item, item)
        os.system(command)

def get_files(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):  # @UnusedVariable
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

def mk_po(local_path, path_for_translation, new=False):
    all_file = get_files(path_for_translation)
    files = []
    for i in all_file:
        if i[-3:] == '.py':
            files.append(i)
    if new == False:
        command = 'xgettext -j -d locale/%s/LC_MESSAGES/messages %s'  % (local_path, files)
        os.system(command)
    else:
        command = 'xgettext -d locale/messages %s' % (files)
        os.system(command)
    return True

def load_local(path):
    gettext.install('messages', path, unicode=True, names=['ugettext'], codeset='utf-8')
    return True