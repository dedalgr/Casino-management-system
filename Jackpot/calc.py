#-*- coding:utf-8 -*-
'''
Created on 18.03.2017 г.

@author: dedal
'''

import random

def mk_range(start, stop, step):
    start = int(start/0.01)
    stop = int(stop/0.01)
    step = int(step/0.01)
    return list(range(start, stop, step))

# def mk_range(start, stop, step):
#    return numpy.arange(start, stop, step).tolist()

def mk_random(array, choose=1, mony=True):
    try:
        random.shuffle(array)
        if choose == 1:
            data =  random.sample(array,  choose)[0]
            if mony == True:
                data = data*0.01
        else:
            data =  random.sample(array,  choose)
            if mony == True:
                var = []
                for i in data:
                    var.append(i*0.01)
                data = var
        return data
    except ValueError:
        return False

def mk_time_range(start, stop, step):
    data = mk_range(start, stop, step)
    tmp = []
    for i in data:
        if (i*0.01)%1 <= 0.59:
            tmp.append(i)
    return tmp


