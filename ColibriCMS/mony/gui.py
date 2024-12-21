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
## Class MonyInOut
###########################################################################

class MonyInOut ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Приход", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 4, 0, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer7 = wx.GridSizer( 4, 0, 0, 0 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Сума", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer7.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Допълнителна информация", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer7.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_textCtrl3, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer1.Add( gSizer7, 1, wx.EXPAND, 5 )

		self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,200 ), wx.LC_REPORT|wx.LC_SINGLE_SEL )
		fgSizer1.Add( self.m_listCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton1.SetBitmap( wx.Bitmap( u"img/22x22/list-add.png", wx.BITMAP_TYPE_ANY ) )
		gSizer5.Add( self.m_bpButton1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_bpButton2 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton2.SetBitmap( wx.Bitmap( u"img/22x22/list-remove.png", wx.BITMAP_TYPE_ANY ) )
		gSizer5.Add( self.m_bpButton2, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer1.Add( gSizer5, 1, wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		fgSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()
		fgSizer1.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class MonyTransfer
###########################################################################

class MonyTransfer ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Паричен трансфер", pos = wx.DefaultPosition, size = wx.Size( 348,307 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Сума", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText14.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer5.Add( self.m_staticText14, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl6, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Към Крупие", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText15.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer5.Add( self.m_staticText15, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		bSizer5.Add( self.m_choice3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Основание", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText16.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer5.Add( self.m_staticText16, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_radioBtn3 = wx.RadioButton( self, wx.ID_ANY, u"Каса", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_radioBtn3, 0, wx.ALL, 5 )

		self.m_radioBtn4 = wx.RadioButton( self, wx.ID_ANY, u"Допълване", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_radioBtn4, 0, wx.ALL, 5 )

		self.m_radioBtn5 = wx.RadioButton( self, wx.ID_ANY, u"Налични", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_radioBtn5, 0, wx.ALL, 5 )

		self.m_radioBtn6 = wx.RadioButton( self, wx.ID_ANY, u"Друго", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_radioBtn6, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer2, 1, wx.EXPAND, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl5.Hide()

		bSizer5.Add( self.m_textCtrl5, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer25 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button27 = wx.Button( self, wx.ID_ANY, u"Отказ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_button27, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button26 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_button26, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		bSizer5.Add( gSizer25, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_radioBtn3.Bind( wx.EVT_RADIOBUTTON, self.OnHideInfo )
		self.m_radioBtn4.Bind( wx.EVT_RADIOBUTTON, self.OnHideInfo )
		self.m_radioBtn5.Bind( wx.EVT_RADIOBUTTON, self.OnHideInfo )
		self.m_radioBtn6.Bind( wx.EVT_RADIOBUTTON, self.OnShowInfo )
		self.m_button27.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button26.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnHideInfo( self, event ):
		event.Skip()



	def OnShowInfo( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class Lipsi
###########################################################################

class Lipsi ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Липси", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer2 = wx.GridSizer( 4, 0, 0, 0 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Сума", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer2.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_radioBtn1 = wx.RadioButton( self, wx.ID_ANY, u"Липса", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

		self.m_radioBtn2 = wx.RadioButton( self, wx.ID_ANY, u"Изплащане", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_radioBtn2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer2.Add( fgSizer9, 1, wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		gSizer2.Add( gSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer2 )
		self.Layout()
		gSizer2.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class TransverPassword
###########################################################################

class TransverPassword ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Потвърди паричен трансфер", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 450,200 ), wx.DefaultSize )

		gSizer8 = wx.GridSizer( 4, 0, 0, 0 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Сума:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText7.SetForegroundColour( wx.Colour( 214, 0, 0 ) )

		bSizer3.Add( self.m_staticText7, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"10,00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText9.SetForegroundColour( wx.Colour( 233, 0, 0 ) )

		bSizer3.Add( self.m_staticText9, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		gSizer8.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Потвърди: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText11.SetForegroundColour( wx.Colour( 9, 9, 234 ) )

		bSizer4.Add( self.m_staticText11, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText12.SetForegroundColour( wx.Colour( 9, 9, 234 ) )

		bSizer4.Add( self.m_staticText12, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		gSizer8.Add( bSizer4, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
		gSizer8.Add( self.m_textCtrl6, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Отказ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Потвърди", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		gSizer8.Add( gSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer8 )
		self.Layout()
		gSizer8.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_textCtrl6.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button8.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()




