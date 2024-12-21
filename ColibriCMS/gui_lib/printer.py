# -*- coding:utf-8 -*-
'''
Created on 23.06.2017 г.

@author: dedal
'''
import wx
from . import gui
from wx.html import HtmlEasyPrinting, HtmlPrintout
import libs
import jinja2 as jinja
import os
import pdfkit
import pickle


# from wx.lib.pdfviewer import pdfViewer, pdfButtonPanel  # @UnresolvedImport
# import wx.lib.sized_controls as sc


def create_env():
    loader = jinja.FileSystemLoader(libs.conf.TEMPLATES + libs.conf.USE_LANGUAGE + '/')
    env = jinja.Environment(loader=loader)
    return env


env = create_env()


def render(name, context=None):
    context = context or {}
    return env.get_template(name).render(context)


def pdf_mk(html, pdf_file, pos=False, size=(80, 130)):
    if pos is False:
        options = {
            'page-size': 'A4',
            # 'page-width': 80,
            # 'page-height': 180,
            'encoding': "UTF-8",
            'no-outline': None,
            'quiet': ''
        }
    else:
        options = {
            # 'page-size': 'A4',
            'page-width': size[0],
            'page-height': size[1],
            'encoding': "UTF-8",
            'no-outline': None,
            'quiet': ''
        }
    if os.name == 'posix':
        return pdfkit.from_string(html, pdf_file, options=options)
    else:
        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        return pdfkit.from_string(html, pdf_file, options=options, configuration=config)


class HTMLPrinter(HtmlEasyPrinting):
    def __init__(self, parent):
        HtmlEasyPrinting.__init__(self)
        self.parent = parent
        self.SetParentWindow(parent)

    def OnPageSetup(self, event):
        self.PageSetup()

    def Print(self, text):
        self.SetStandardFonts()
        self.PrintText(text)

    def PreviewText(self, text):
        # Не работи. Вади фрейм на заден план
        HtmlEasyPrinting.PreviewText(self, text)


def PDFPrint(pdf_files, ranges=1, default=libs.conf.PRINTER_DEFAULT, pos=False):
    data = open(pdf_files, 'rb').read()

    if libs.conf.PRINT_ON_SERVER is True and pos is False:
        data = bytes(data, encoding='utf-8').hex()
        response = libs.udp.send('print_on_server', libs.conf.SERVER, tmp_file=data, ranges=ranges)
        return response
    elif libs.conf.PRINT_ON_SERVER_POS is True and pos is True:
        data = bytes(data, encoding='utf-8').hex()
        response = libs.udp.send('print_on_server_pos', libs.conf.SERVER, tmp_file=data, ranges=ranges)
        return response
    if pos is True and libs.conf.PRINT_ON_SERVER_POS is False and libs.conf.PRINT_DIRECT_POS is True and libs.conf.DEFAULT_POS_PRINTER == '':
        return False
    if os.name == 'posix':
        cmd = 'lp -d %s %s' % (default, pdf_files)
        for i in range(ranges):
            os.system(cmd)
        return True
    else:
        pdf_files = pdf_files.replace('/', '\\')
        cmd = r'print /d:\\localhost\\%s %s' % (default, pdf_files)
        for i in range(ranges):
            os.system(cmd)
        return True


# class PDFViewer(sc.SizedFrame):
#     def __init__(self, parent, **kwds):
#         super(PDFViewer, self).__init__(parent, **kwds)
#
#         paneCont = self.GetContentsPane()
#         self.buttonpanel = pdfButtonPanel(paneCont, wx.NewId(),
#                                 wx.DefaultPosition, wx.DefaultSize, 0)
#         self.buttonpanel.SetSizerProps(expand=True)
#         self.viewer = pdfViewer(paneCont, wx.NewId(), wx.DefaultPosition,
#                                 wx.DefaultSize,
#                                 wx.HSCROLL|wx.VSCROLL|wx.SUNKEN_BORDER)
#         self.viewer.UsePrintDirect = False
#         self.viewer.SetSizerProps(expand=True, proportion=1)
#         # introduce buttonpanel and viewer to each other
#         self.buttonpanel.viewer = self.viewer
#         self.viewer.LoadFile('tmp.pdf')
#
#         self.Layout()


def PrintOnServer(template, data):
    html = render(template, data)
    if os.name == 'posix':
        tmp_folder = '/tmp/'
    else:
        tmp_folder = libs.conf.TEMPLATES
    pdf_mk(html, tmp_folder + 'tmp.pdf')
    my_pdf = open(tmp_folder + 'tmp.pdf', 'rb').read()
    return my_pdf


def Print(parent, template, data, ranges=1):
    # if libs.conf.PRINTER_USE_PDF is False:
    #     html = render(template, data)
    #     printer = HTMLPrinter(parent)
    #     printer.Print(html)
    #     return True
    # else:
    html = render(template, data)
    if os.name == 'posix':
        tmp_folder = '/tmp/'
    else:
        tmp_folder = r'C:/Users/Public/'
    pdf_mk(html, tmp_folder + 'tmp.pdf')
    if libs.conf.PRINT_DIRECT is True:
        PDFPrint(tmp_folder + 'tmp.pdf', ranges)
    else:
        # wx.LaunchDefaultApplication(tmp_folder + 'tmp.pdf')
        cmd = libs.conf.PDF_PROGRAM + ' ' + tmp_folder + 'tmp.pdf'
        os.popen(cmd)
    return True
