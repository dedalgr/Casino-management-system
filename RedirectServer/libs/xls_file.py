#-*- coding: utf-8 -*-

'''
Created on 28.11.2014
Author: Grigor Kolev
'''
import xlsxwriter


class Makexls():
    
    
    def __init__(self, filename):
        
        self.workbook = xlsxwriter.Workbook(filename)
        self.worksheet = self.workbook.add_worksheet()
        self.row = 0
        self.col = 0
        self.m_row = []
    
    
    def head(self, *head):
        self.head = head
        self.worksheet.write_row(self.row, self.col,  tuple(self.head))
        return True
        
    
    def set_data(self, *data):

        self.row += 1
        var = []
        for info in data:
            var.append(info)
        self.m_row.append( var )
        return True
        
    
    def write(self):
        self.row  = 0
        for data in self.m_row:
            self.row += 1
            self.worksheet.write_row(self.row, self.col, tuple(data))
        self.workbook.close()
        return True

if __name__ == '__main__':
    xlmx = Makexls('/home/dedal/test.xlsx')
    xlmx.head(
                   u'Naam',
                   u'Adres',
                   u'mail'
                  )

    xlmx.set_data('test', 3, 'nqma')
    xlmx.set_data('nqma1', 'test1', 2 )
    xlmx.write()