# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Activ
###########################################################################

class Activ ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Активиране", pos = wx.DefaultPosition, size = wx.Size( 708,282 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer7 = wx.GridSizer( 5, 0, 0, 0 )

		gSizer8 = wx.GridSizer( 0, 0, 0, 0 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"БАЗОВ КОД", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText1.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer8.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		gSizer7.Add( gSizer8, 1, wx.EXPAND, 5 )

		gSizer11 = wx.GridSizer( 0, 0, 0, 0 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_PROCESS_TAB|wx.TE_READONLY )
		self.m_textCtrl1.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_textCtrl1.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		gSizer11.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		gSizer7.Add( gSizer11, 1, wx.EXPAND, 5 )

		gSizer12 = wx.GridSizer( 0, 0, 0, 0 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"КОД ЗА АКТИВАЦИЯ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText2.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer12.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		gSizer7.Add( gSizer12, 1, wx.EXPAND, 5 )

		gSizer13 = wx.GridSizer( 0, 0, 0, 0 )

		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gSizer13.Add( self.m_filePicker1, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer7.Add( gSizer13, 1, wx.EXPAND, 5 )

		m_sdbSizer3 = wx.StdDialogButtonSizer()
		self.m_sdbSizer3OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer3.AddButton( self.m_sdbSizer3OK )
		self.m_sdbSizer3Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer3.AddButton( self.m_sdbSizer3Cancel )
		m_sdbSizer3.Realize();

		gSizer7.Add( m_sdbSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer3Cancel.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_sdbSizer3OK.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class LicenzPanel
###########################################################################

class LicenzPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer1 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_toolBar1 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL|wx.TB_TEXT )
		self.m_toolBar1.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_tool3 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Добави", wx.Bitmap( u"img/64x64/xarchiver-add.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool4 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Затвори", wx.Bitmap( u"img/64x64/dialog-error.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar1.Realize()

		fgSizer1.Add( self.m_toolBar1, 0, wx.EXPAND, 5 )

		gSizer16 = wx.GridSizer( 0, 0, 0, 0 )

		self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 490,180 ), wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl1.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_listCtrl1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_listCtrl1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizer16.Add( self.m_listCtrl1, 0, wx.ALL, 5 )


		fgSizer1.Add( gSizer16, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()

		# Connect Events
		self.Bind( wx.EVT_TOOL, self.OnAdd, id = self.m_tool3.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnClose, id = self.m_tool4.GetId() )
		self.m_listCtrl1.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnCheck )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnAdd( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()

	def OnCheck( self, event ):
		event.Skip()


