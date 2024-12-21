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
## Class OrderPanel
###########################################################################

class OrderPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer10 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_toolBar1 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL|wx.TB_TEXT )
		self.m_toolBar1.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_tool6 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Печат", wx.Bitmap( u"img/64x64/Gnome-Printer-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool2 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Приходи", wx.Bitmap( u"img/64x64/Gnome-Edit-Redo-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool102 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Трансфер", wx.Bitmap( u"img/64x64/Gnome-Object-Flip-Horizontal-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool3 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Разходи", wx.Bitmap( u"img/64x64/Gnome-Edit-Undo-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool4 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Липси", wx.Bitmap( u"img/64x64/Gnome-List-Remove-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool8 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Отчет", wx.Bitmap( u"img/64x64/Gnome-Emblem-Downloads-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool101 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Ръчен отчет", wx.Bitmap( u"img/64x64/Gnome-Preferences-Desktop-Keyboard-Shortcuts-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool111 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Бил", wx.Bitmap( u"img/64x64/Gnome-Insert-Link-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool10 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Край на смяна", wx.Bitmap( u"img/64x64/Gnome-View-Refresh-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool1 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Затвори", wx.Bitmap( u"img/64x64/dialog-error.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar1.Realize()

		fgSizer10.Add( self.m_toolBar1, 1, wx.EXPAND, 5 )

		gSizer7 = wx.GridSizer( 4, 0, 0, 0 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Каса: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText1.SetForegroundColour( wx.Colour( 172, 0, 0 ) )

		gSizer7.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Регион: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText3.SetForegroundColour( wx.Colour( 172, 0, 0 ) )

		gSizer7.Add( self.m_staticText3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Потребител:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText14.SetForegroundColour( wx.Colour( 172, 0, 0 ) )

		gSizer7.Add( self.m_staticText14, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizer7.Add( self.m_staticText16, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer10.Add( gSizer7, 1, wx.EXPAND, 5 )

		fgSizer4 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer31 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer31.SetFlexibleDirection( wx.BOTH )
		fgSizer31.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer4 = wx.GridSizer( 2, 1, 0, 0 )

		self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_VRULES )
		self.m_listCtrl1.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer4.Add( self.m_listCtrl1, 0, wx.ALL, 5 )

		self.m_listCtrl2 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_VRULES )
		self.m_listCtrl2.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer4.Add( self.m_listCtrl2, 0, wx.ALL, 5 )


		fgSizer31.Add( gSizer4, 1, wx.EXPAND, 5 )

		self.m_listCtrl3 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_VRULES )
		fgSizer31.Add( self.m_listCtrl3, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer4.Add( fgSizer31, 1, wx.EXPAND, 5 )


		fgSizer10.Add( fgSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer10 )
		self.Layout()
		fgSizer10.Fit( self )

		# Connect Events
		self.Bind( wx.EVT_TOOL, self.OnBillGet, id = self.m_tool111.GetId() )
		self.m_staticText1.Bind( wx.EVT_LEFT_DCLICK, self.MakeMonyOrder )
		self.m_staticText14.Bind( wx.EVT_LEFT_DCLICK, self.LoadUser )
		self.m_staticText16.Bind( wx.EVT_LEFT_DCLICK, self.OnShowMSG )
		self.m_listCtrl1.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnShowMaker )
		self.m_listCtrl2.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnShowEnableDisable )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnBillGet( self, event ):
		event.Skip()

	def MakeMonyOrder( self, event ):
		event.Skip()

	def LoadUser( self, event ):
		event.Skip()

	def OnShowMSG( self, event ):
		event.Skip()

	def OnShowMaker( self, event ):
		event.Skip()

	def OnShowEnableDisable( self, event ):
		event.Skip()


###########################################################################
## Class GetCounter
###########################################################################

class GetCounter ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Взимане на броячи", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer3 = wx.GridSizer( 3, 0, 0, 0 )

		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 600,-1 ), wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 )
		gSizer3.Add( self.m_gauge1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Машина: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gSizer3.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		self.SetSizer( gSizer3 )
		self.Layout()
		gSizer3.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()



###########################################################################
## Class NotSASCounter
###########################################################################

class NotSASCounter ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Отчет на машини!", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION|wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer4 = wx.FlexGridSizer( 4, 0, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Машина", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer10.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Механични броячи", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_checkBox1, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer4.Add( gSizer10, 1, wx.EXPAND, 5 )

		fgSizer5 = wx.FlexGridSizer( 4, 3, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Вход:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer5.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl8.SetMinSize( wx.Size( 200,-1 ) )

		fgSizer5.Add( self.m_textCtrl8, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText17.SetForegroundColour( wx.Colour( 175, 0, 0 ) )

		fgSizer5.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Изход:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		self.m_staticText18.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText18.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer5.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl9.SetMinSize( wx.Size( 200,-1 ) )

		fgSizer5.Add( self.m_textCtrl9, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText19.SetForegroundColour( wx.Colour( 175, 0, 0 ) )

		fgSizer5.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Бил:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer5.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		self.m_textCtrl10.SetMinSize( wx.Size( 200,-1 ) )

		fgSizer5.Add( self.m_textCtrl10, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText21.SetForegroundColour( wx.Colour( 175, 0, 0 ) )

		fgSizer5.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		fgSizer4.Add( fgSizer5, 1, wx.EXPAND, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Тотал:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText22.SetForegroundColour( wx.Colour( 19, 145, 62 ) )

		fgSizer4.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		fgSizer4.Add( gSizer9, 1, wx.EXPAND|wx.ALIGN_BOTTOM, 5 )


		self.SetSizer( fgSizer4 )
		self.Layout()
		fgSizer4.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.OnCheck )
		self.m_textCtrl8.Bind( wx.EVT_TEXT, self.OnMathIn )
		self.m_textCtrl9.Bind( wx.EVT_TEXT, self.OnMathOut )
		self.m_textCtrl10.Bind( wx.EVT_TEXT, self.OnMathBill )
		self.m_textCtrl10.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnCheck( self, event ):
		event.Skip()

	def OnMathIn( self, event ):
		event.Skip()

	def OnMathOut( self, event ):
		event.Skip()

	def OnMathBill( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()




###########################################################################
## Class OrderByHand
###########################################################################

class OrderByHand ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ръчно отчитане", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION|wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer6 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_listCtrl4 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl4.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_listCtrl4.SetForegroundColour( wx.Colour( 174, 0, 0 ) )
		self.m_listCtrl4.SetMinSize( wx.Size( 400,200 ) )

		fgSizer6.Add( self.m_listCtrl4, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		self.SetSizer( fgSizer6 )
		self.Layout()
		fgSizer6.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_listCtrl4.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnOrder )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnOrder( self, event ):
		event.Skip()



###########################################################################
## Class BillGet
###########################################################################

class BillGet ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Извади бил", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer10 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_listCtrl5 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl5.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer10.Add( self.m_listCtrl5, 0, wx.ALL, 5 )

		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Бил: 0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText11.SetForegroundColour( wx.Colour( 17, 114, 0 ) )

		gSizer7.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		gSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Отказ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Извади", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		fgSizer10.Add( gSizer7, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer10 )
		self.Layout()
		fgSizer10.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button8.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class MexCheck
###########################################################################

class MexCheck ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_listCtrl6 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl6.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer8.Add( self.m_listCtrl6, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Печат", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button9, 0, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button8, 0, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5 )


		fgSizer8.Add( bSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer8 )
		self.Layout()

		# Connect Events
		self.m_listCtrl6.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnEdit )
		self.m_button9.Bind( wx.EVT_BUTTON, self.OnPrint )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnGo )
		self.m_button8.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnEdit( self, event ):
		event.Skip()

	def OnPrint( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()


###########################################################################
## Class MexEdit
###########################################################################

class MexEdit ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Механични броячи", pos = wx.DefaultPosition, size = wx.Size( 300,200 ), style = wx.CAPTION|wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 300,200 ), wx.DefaultSize )

		gSizer8 = wx.GridSizer( 5, 0, 0, 0 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Вход", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText12.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer8.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrl4, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Изход", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText13.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer8.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrl5, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_button10, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		gSizer8.Add( gSizer7, 1, wx.EXPAND|wx.ALIGN_BOTTOM, 5 )


		self.SetSizer( gSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl5.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_button10.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button11.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnGo( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()



###########################################################################
## Class BugReport
###########################################################################

class BugReport ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Доклад за грешки", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer7 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Описание", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		fgSizer7.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl7.SetMinSize( wx.Size( 500,300 ) )

		fgSizer7.Add( self.m_textCtrl7, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer26 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button29 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer26.Add( self.m_button29, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button30 = wx.Button( self, wx.ID_ANY, u"Изпрати", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer26.Add( self.m_button30, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		fgSizer7.Add( gSizer26, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer7 )
		self.Layout()
		fgSizer7.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button29.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button30.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class UserEditOrderSelect
###########################################################################

class UserEditOrderSelect ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Редактирай отчет на потребител ", pos = wx.DefaultPosition, size = wx.Size( 284,154 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer10 = wx.GridSizer( 3, 0, 0, 0 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Потребител", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		gSizer10.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		m_choice1Choices = []
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		gSizer10.Add( self.m_choice1, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer11 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button14 = wx.Button( self, wx.ID_ANY, u"Отказ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_button14, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button15 = wx.Button( self, wx.ID_ANY, u"Избери", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_button15, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer10.Add( gSizer11, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button14.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button15.Bind( wx.EVT_BUTTON, self.OnSelect )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnSelect( self, event ):
		event.Skip()


###########################################################################
## Class Opis
###########################################################################

class Opis ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Опис на пари", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer10 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"x100" ), wx.HORIZONTAL )

		self.m_spinCtrl1 = wx.SpinCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,25 ), wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sbSizer1.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		sbSizer1.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer10.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"x50" ), wx.HORIZONTAL )

		self.m_spinCtrl11 = wx.SpinCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,25 ), wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sbSizer11.Add( self.m_spinCtrl11, 0, wx.ALL, 5 )

		self.m_staticText221 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )

		sbSizer11.Add( self.m_staticText221, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer10.Add( sbSizer11, 1, wx.EXPAND, 5 )

		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"x20" ), wx.HORIZONTAL )

		self.m_spinCtrl12 = wx.SpinCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,25 ), wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sbSizer12.Add( self.m_spinCtrl12, 0, wx.ALL, 5 )

		self.m_staticText222 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText222.Wrap( -1 )

		sbSizer12.Add( self.m_staticText222, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer10.Add( sbSizer12, 1, wx.EXPAND, 5 )

		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"x10" ), wx.HORIZONTAL )

		self.m_spinCtrl13 = wx.SpinCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,25 ), wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sbSizer13.Add( self.m_spinCtrl13, 0, wx.ALL, 5 )

		self.m_staticText223 = wx.StaticText( sbSizer13.GetStaticBox(), wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText223.Wrap( -1 )

		sbSizer13.Add( self.m_staticText223, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer10.Add( sbSizer13, 1, wx.EXPAND, 5 )

		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"x5" ), wx.HORIZONTAL )

		self.m_spinCtrl14 = wx.SpinCtrl( sbSizer14.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,25 ), wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sbSizer14.Add( self.m_spinCtrl14, 0, wx.ALL, 5 )

		self.m_staticText224 = wx.StaticText( sbSizer14.GetStaticBox(), wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText224.Wrap( -1 )

		sbSizer14.Add( self.m_staticText224, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer10.Add( sbSizer14, 1, wx.EXPAND, 5 )

		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"x2" ), wx.HORIZONTAL )

		self.m_spinCtrl15 = wx.SpinCtrl( sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,25 ), wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sbSizer15.Add( self.m_spinCtrl15, 0, wx.ALL, 5 )

		self.m_staticText225 = wx.StaticText( sbSizer15.GetStaticBox(), wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText225.Wrap( -1 )

		sbSizer15.Add( self.m_staticText225, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer10.Add( sbSizer15, 1, wx.EXPAND, 5 )

		sbSizer16 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"x1" ), wx.HORIZONTAL )

		self.m_spinCtrl16 = wx.SpinCtrl( sbSizer16.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,25 ), wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sbSizer16.Add( self.m_spinCtrl16, 0, wx.ALL, 5 )

		self.m_staticText226 = wx.StaticText( sbSizer16.GetStaticBox(), wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText226.Wrap( -1 )

		sbSizer16.Add( self.m_staticText226, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer10.Add( sbSizer16, 1, wx.EXPAND, 5 )

		sbSizer17 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"x0.50" ), wx.HORIZONTAL )

		self.m_spinCtrl17 = wx.SpinCtrl( sbSizer17.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,25 ), wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sbSizer17.Add( self.m_spinCtrl17, 0, wx.ALL, 5 )

		self.m_staticText227 = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText227.Wrap( -1 )

		sbSizer17.Add( self.m_staticText227, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer10.Add( sbSizer17, 1, wx.EXPAND, 5 )

		sbSizer18 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"x0.20" ), wx.HORIZONTAL )

		self.m_spinCtrl18 = wx.SpinCtrl( sbSizer18.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,25 ), wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sbSizer18.Add( self.m_spinCtrl18, 0, wx.ALL, 5 )

		self.m_staticText228 = wx.StaticText( sbSizer18.GetStaticBox(), wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText228.Wrap( -1 )

		sbSizer18.Add( self.m_staticText228, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer10.Add( sbSizer18, 1, wx.EXPAND, 5 )

		sbSizer19 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"x0.10" ), wx.HORIZONTAL )

		self.m_spinCtrl19 = wx.SpinCtrl( sbSizer19.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,25 ), wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sbSizer19.Add( self.m_spinCtrl19, 0, wx.ALL, 5 )

		self.m_staticText229 = wx.StaticText( sbSizer19.GetStaticBox(), wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText229.Wrap( -1 )

		sbSizer19.Add( self.m_staticText229, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer10.Add( sbSizer19, 1, wx.EXPAND, 5 )

		sbSizer110 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"x0.05" ), wx.HORIZONTAL )

		self.m_spinCtrl110 = wx.SpinCtrl( sbSizer110.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,25 ), wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sbSizer110.Add( self.m_spinCtrl110, 0, wx.ALL, 5 )

		self.m_staticText2210 = wx.StaticText( sbSizer110.GetStaticBox(), wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2210.Wrap( -1 )

		sbSizer110.Add( self.m_staticText2210, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer10.Add( sbSizer110, 1, wx.EXPAND, 5 )

		sbSizer111 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"x0.02" ), wx.HORIZONTAL )

		self.m_spinCtrl111 = wx.SpinCtrl( sbSizer111.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,25 ), wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sbSizer111.Add( self.m_spinCtrl111, 0, wx.ALL, 5 )

		self.m_staticText2211 = wx.StaticText( sbSizer111.GetStaticBox(), wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2211.Wrap( -1 )

		sbSizer111.Add( self.m_staticText2211, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer10.Add( sbSizer111, 1, wx.EXPAND, 5 )

		sbSizer112 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"x0.01" ), wx.HORIZONTAL )

		self.m_spinCtrl112 = wx.SpinCtrl( sbSizer112.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,25 ), wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sbSizer112.Add( self.m_spinCtrl112, 0, wx.ALL, 5 )

		self.m_staticText2212 = wx.StaticText( sbSizer112.GetStaticBox(), wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2212.Wrap( -1 )

		sbSizer112.Add( self.m_staticText2212, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer10.Add( sbSizer112, 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Общо:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText51.SetForegroundColour( wx.Colour( 194, 0, 0 ) )

		fgSizer10.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		self.m_staticText52.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText52.SetForegroundColour( wx.Colour( 194, 0, 0 ) )

		fgSizer10.Add( self.m_staticText52, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_button16, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_button17, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( fgSizer10 )
		self.Layout()
		fgSizer10.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_spinCtrl1.Bind( wx.EVT_KEY_DOWN, self.onEnter )
		self.m_spinCtrl1.Bind( wx.EVT_SPINCTRL, self.c100 )
		self.m_spinCtrl1.Bind( wx.EVT_TEXT, self.c100 )
		self.m_spinCtrl1.Bind( wx.EVT_TEXT_ENTER, self.c100 )
		self.m_spinCtrl11.Bind( wx.EVT_KEY_DOWN, self.onEnter )
		self.m_spinCtrl11.Bind( wx.EVT_SPINCTRL, self.c50 )
		self.m_spinCtrl11.Bind( wx.EVT_TEXT, self.c50 )
		self.m_spinCtrl11.Bind( wx.EVT_TEXT_ENTER, self.c50 )
		self.m_spinCtrl12.Bind( wx.EVT_KEY_DOWN, self.onEnter )
		self.m_spinCtrl12.Bind( wx.EVT_SPINCTRL, self.c20 )
		self.m_spinCtrl12.Bind( wx.EVT_TEXT, self.c20 )
		self.m_spinCtrl12.Bind( wx.EVT_TEXT_ENTER, self.c20 )
		self.m_spinCtrl13.Bind( wx.EVT_KEY_DOWN, self.onEnter )
		self.m_spinCtrl13.Bind( wx.EVT_SPINCTRL, self.c10 )
		self.m_spinCtrl13.Bind( wx.EVT_TEXT, self.c10 )
		self.m_spinCtrl13.Bind( wx.EVT_TEXT_ENTER, self.c10 )
		self.m_spinCtrl14.Bind( wx.EVT_KEY_DOWN, self.onEnter )
		self.m_spinCtrl14.Bind( wx.EVT_SPINCTRL, self.c5 )
		self.m_spinCtrl14.Bind( wx.EVT_TEXT, self.c5 )
		self.m_spinCtrl14.Bind( wx.EVT_TEXT_ENTER, self.c5 )
		self.m_spinCtrl15.Bind( wx.EVT_KEY_DOWN, self.onEnter )
		self.m_spinCtrl15.Bind( wx.EVT_SPINCTRL, self.c2 )
		self.m_spinCtrl15.Bind( wx.EVT_TEXT, self.c2 )
		self.m_spinCtrl15.Bind( wx.EVT_TEXT_ENTER, self.c2 )
		self.m_spinCtrl16.Bind( wx.EVT_KEY_DOWN, self.onEnter )
		self.m_spinCtrl16.Bind( wx.EVT_SPINCTRL, self.c1 )
		self.m_spinCtrl16.Bind( wx.EVT_TEXT, self.c1 )
		self.m_spinCtrl16.Bind( wx.EVT_TEXT_ENTER, self.c1 )
		self.m_spinCtrl17.Bind( wx.EVT_KEY_DOWN, self.onEnter )
		self.m_spinCtrl17.Bind( wx.EVT_SPINCTRL, self.c50st )
		self.m_spinCtrl17.Bind( wx.EVT_TEXT, self.c50st )
		self.m_spinCtrl17.Bind( wx.EVT_TEXT_ENTER, self.c50st )
		self.m_spinCtrl18.Bind( wx.EVT_KEY_DOWN, self.onEnter )
		self.m_spinCtrl18.Bind( wx.EVT_SPINCTRL, self.c20st )
		self.m_spinCtrl18.Bind( wx.EVT_TEXT, self.c20st )
		self.m_spinCtrl18.Bind( wx.EVT_TEXT_ENTER, self.c20st )
		self.m_spinCtrl19.Bind( wx.EVT_KEY_DOWN, self.onEnter )
		self.m_spinCtrl19.Bind( wx.EVT_SPINCTRL, self.c10st )
		self.m_spinCtrl19.Bind( wx.EVT_TEXT, self.c10st )
		self.m_spinCtrl19.Bind( wx.EVT_TEXT_ENTER, self.c10st )
		self.m_spinCtrl110.Bind( wx.EVT_KEY_DOWN, self.onEnter )
		self.m_spinCtrl110.Bind( wx.EVT_SPINCTRL, self.c05st )
		self.m_spinCtrl110.Bind( wx.EVT_TEXT, self.c05st )
		self.m_spinCtrl110.Bind( wx.EVT_TEXT_ENTER, self.c05st )
		self.m_spinCtrl111.Bind( wx.EVT_KEY_DOWN, self.onEnter )
		self.m_spinCtrl111.Bind( wx.EVT_SPINCTRL, self.c02st )
		self.m_spinCtrl111.Bind( wx.EVT_TEXT, self.c02st )
		self.m_spinCtrl111.Bind( wx.EVT_TEXT_ENTER, self.c02st )
		self.m_spinCtrl112.Bind( wx.EVT_KEY_DOWN, self.onEnter )
		self.m_spinCtrl112.Bind( wx.EVT_SPINCTRL, self.c01st )
		self.m_spinCtrl112.Bind( wx.EVT_TEXT, self.c01st )
		self.m_spinCtrl112.Bind( wx.EVT_TEXT_ENTER, self.c01st )
		self.m_button16.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button17.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def onEnter( self, event ):
		event.Skip()

	def c100( self, event ):
		event.Skip()




	def c50( self, event ):
		event.Skip()




	def c20( self, event ):
		event.Skip()




	def c10( self, event ):
		event.Skip()




	def c5( self, event ):
		event.Skip()




	def c2( self, event ):
		event.Skip()




	def c1( self, event ):
		event.Skip()




	def c50st( self, event ):
		event.Skip()




	def c20st( self, event ):
		event.Skip()




	def c10st( self, event ):
		event.Skip()




	def c05st( self, event ):
		event.Skip()




	def c02st( self, event ):
		event.Skip()




	def c01st( self, event ):
		event.Skip()




	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class SelectUser
###########################################################################

class SelectUser ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Избери смяна", pos = wx.DefaultPosition, size = wx.Size( 279,135 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, u"Потребител", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		bSizer2.Add( self.m_staticText36, 0, wx.ALL|wx.EXPAND, 5 )

		m_choice2Choices = []
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		bSizer2.Add( self.m_choice2, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer12 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Отказ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.m_button18, 0, wx.ALL, 5 )

		self.m_button19 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.m_button19, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer2.Add( gSizer12, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button18.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button19.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


