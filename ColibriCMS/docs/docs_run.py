#!/usr/bin/env python3
#-*- coding:utf-8 -*-
from multiprocessing import Process
import os

def run_devdoc():
    command = 'mkdocs serve --dev-addr=127.0.0.1:5000'
    os.system(command)


p = Process(target=run_devdoc())
p.daemon = True
p.start()
