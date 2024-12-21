# -*- coding:utf-8 -*-
'''
Created on 2.11.2017 г.

@author: dedal
'''
import wx
from threading import *
import libs  # @UnresolvedImport
import order.task  # @UnresolvedImport
import time
import gui_lib

CURENT_STATE_GET = wx.NewId()
CURENT_STATE_GET_RUN = wx.NewId()
CURENT_STATE_GET_STOP = wx.NewId()


def CURENT_STATE(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, CURENT_STATE_GET, func)


class GetCurentState(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(CURENT_STATE_GET)
        self.data = data


class CurentState(Thread):
    """Worker Thread Class."""

    def __init__(self, notify_window, col, row, refresh_time):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self._notify_window = notify_window
        self._want_abort = 0
        self.row = row
        self.col = col
        self.refresh_time = refresh_time
        # if self.refresh_time < 1:
        #     self.refresh_time = 0.07
        #         self.empty_row = []
        self.sums = {}
        self.start()

    def run(self):
        row = []
        NOT_WORK_SMIB = {}
        while True:
            in_sum = 0
            bill_sum = 0
            out_sum = 0
            total_sum = 0

            for item in self.row:
                libs.DB.expire(item)
                bill = None
                counter = None
                credit = None
                player = False
                time.sleep(self.refresh_time)
                if item.ip not in NOT_WORK_SMIB:
                    for d in range(3):
                        counter = libs.udp.send('real_time_look', ip=item.ip)
                        if counter != None:
                            break
                        time.sleep(self.refresh_time)
                    if counter != None:
                        player = counter['player']
                    else:
                        NOT_WORK_SMIB[item.ip] = [time.time(), counter]
                elif NOT_WORK_SMIB[item.ip][0] + 30 <= time.time():
                    del NOT_WORK_SMIB[item.ip]
                #     counter = libs.udp.send('sas.mether_count', ip=item.ip)
                #     if counter != None:
                #         player = libs.udp.send('get_player', ip=item.ip)
                #     else:
                #         NOT_WORK_SMIB[item.ip] = time.time()
                else:
                    # time.sleep(1)
                    counter = NOT_WORK_SMIB[item.ip][1]
                if counter != None:
                    if None in list(counter.values()):
                        counter = None
                    bill = counter['bill']
                    credit = counter['curent credit']
                # print item.nom_in_l, counter
                var = [str(item.nom_in_l), str(item.model.name)]
                #                 print _(u"Тотал") in self.col
                if gui_lib.msg.report_task[3] in self.col:
                    if player is False or player == None:
                        var.append(gui_lib.msg.report_task[1])
                    else:
                        var.append(player)
                if gui_lib.msg.report_task[4] in self.col and len(self.col) == 1:
                    if bill != None:
                        bill_sum += item.bill_in_device + (bill - item.bill)
                        bill = item.bill_in_device + (bill - item.bill)
                        var.append("{:.2f}".format(bill))
                    #                         self.sums[_(u'Бил')] = self.sums[_(u'Бил')] + bill
                    else:
                        var.append(gui_lib.msg.report_task[1])
                elif gui_lib.msg.report_task[2] in self.col and len(self.col) == 1:
                    if credit != None:
                        var.append("{:.2f}".format(credit))
                    else:
                        var.append(gui_lib.msg.report_task[1])

                elif gui_lib.msg.report_task[2] in self.col and gui_lib.msg.report_task[4] in self.col and len(
                        self.col) == 2:
                    if credit != None:
                        var.append("{:.2f}".format(credit))
                    #                         self.sums[_(u'Кредит')] = self.sums[_(u'Кредит')] + credit
                    else:
                        var.append(gui_lib.msg.report_task[1])
                    if bill != None:
                        bill = item.bill_in_device + (bill - item.bill)
                        var.append("{:.2f}".format(bill))
                    #                         self.sums[_(u'Бил')] = self.sums[_(u'Бил')] + bill
                    else:
                        var.append(gui_lib.msg.report_task[1])

                else:
                    if counter != None:
                        if gui_lib.msg.report_task[2] in self.col:
                            if credit != None:
                                var.append("{:.2f}".format(credit))
                            else:
                                var.append(gui_lib.msg.report_task[1])

                        if item.mk_revert is False:
                            counter = order.task.mk_left_revert(item, counter)
                        else:
                            counter = order.task.mk_right_revert(item, counter)

                        if gui_lib.msg.report_task[5] in self.col:
                            try:
                                item.play_bet
                            except AttributeError:
                                item.play_bet = 0.00
                                var.append("{:.2f}".format(0.00))
                                item.play_bet = counter['bet']
                            else:
                                var.append("{:.2f}".format((counter['bet'] - item.play_bet) * item.el_coef))
                                #                                 item.play_bet = (counter['bet'])
                                item.play_bet = counter['bet']

                        if gui_lib.msg.report_task[6] in self.col:
                            try:
                                item.play_won
                            except AttributeError:
                                item.play_won = 0.00
                                var.append("{:.2f}".format(0.00))
                                item.play_won = counter['won']
                            else:
                                var.append("{:.2f}".format((counter['won'] - item.play_won) * item.el_coef))
                                item.play_won = (counter['won'])

                        if gui_lib.msg.report_task[7] in self.col:
                            in_sum += (counter['in'] - item.el_in) * item.el_coef
                            var.append("{:.2f}".format((counter['in'] - item.el_in) * item.el_coef))
                        #                             self.sums[_(u"Вход")] = self.sums[_(u"Вход")] + (counter['in'] - item.el_in)*item.el_coef
                        if gui_lib.msg.report_task[8] in self.col:
                            out_sum += (counter['out'] - item.el_out) * item.el_coef
                            var.append("{:.2f}".format((counter['out'] - item.el_out) * item.el_coef))
                        #                             self.sums[_(u'Изход')] = self.sums[_(u'Изход')] + (counter['out'] - item.el_out)*item.el_coef

                        #                             self.sums[_(u'Кредит')] = self.sums[_(u'Кредит')] + credit
                        if gui_lib.msg.report_task[4] in self.col:
                            if bill != None:
                                bill_sum += item.bill_in_device + (bill - item.bill)
                                bill = item.bill_in_device + (bill - item.bill)
                                var.append("{:.2f}".format(bill))
                            #                                 self.sums[_(u'Бил')] = self.sums[_(u'Бил')] + bill
                            else:
                                var.append(gui_lib.msg.report_task[1])
                        if gui_lib.msg.report_task[9] in self.col:
                            total = ((counter['in'] - item.el_in) * item.el_coef) - (
                                        (counter['out'] - item.el_out) * item.el_coef)
                            total_sum += total
                            var.append("{:.2f}".format(total))
                        #                             self.sums[_(u"Тотал")] = self.sums[_(u"Тотал")] + ((counter['in'] - item.el_in)*item.el_coef) - ((counter['out'] - item.el_out)*item.el_coef)

                        #                             self.sums[_(u"Печалба в игра ( won )")] = self.sums[_(u"Печалба в игра ( won )")] + ((counter['won'] - item.won)*item.el_coef)

                        #                             self.sums[_(u"Залог ( bet )")] = self.sums[_(u"Залог ( bet )")] + ((counter['bet'] - item.bet)*item.el_coef)
                        if gui_lib.msg.report_task[10] in self.col:
                            try:
                                pr = ((counter['won'] * item.el_coef) / (counter['bet'] * item.el_coef)) * 100
                            #                                 self.sums[_(u"Процент на възвръщаемост")] = self.sums[_(u"Процент на възвръщаемост")] + (pr/count)
                            except ZeroDivisionError:
                                pr = 0.00
                            var.append("{:.2f}".format(pr))
                    else:
                        #                         print self.col, len(self.col)
                        for i in range(len(self.col) - 1):
                            var.append(gui_lib.msg.report_task[1])
                if not self._want_abort:
                    pass
                else:
                    break
                row.append(var)
            if not self._want_abort:
                tmp = [u'', u'']
                for i in self.col:
                    #                 tmp.append(u'-'* 10)
                    if i == gui_lib.msg.report_task[7]:
                        tmp.append("{:.2f}".format(in_sum))
                    elif i == gui_lib.msg.report_task[8]:
                        tmp.append("{:.2f}".format(out_sum))
                    elif i == gui_lib.msg.report_task[9]:
                        tmp.append("{:.2f}".format(total_sum))
                    elif i == gui_lib.msg.report_task[4]:
                        tmp.append("{:.2f}".format(bill_sum))
                    else:
                        tmp.append(u'')
                row.insert(0, tmp)
                empty = []
                for i in range(len(tmp)):
                    empty.append('-' * 10)
                row.insert(1, empty)
                if None not in row:
                    wx.PostEvent(self._notify_window, GetCurentState(row))
                row = []

            else:
                break


    def abort(self):
        """abort worker thread."""
        self._want_abort = 1


if __name__ == '__main__':
    pass
