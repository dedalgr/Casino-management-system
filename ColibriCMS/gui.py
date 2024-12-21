# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ColibriCMS", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.ICONIZE|wx.MAXIMIZE|wx.MAXIMIZE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.OnSesionUpdate )
		self.Bind( wx.EVT_CLOSE, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnSesionUpdate( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()


###########################################################################
## Class MakeOrder
###########################################################################

class MakeOrder ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Отчет", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer6 = wx.GridSizer( 2, 0, 0, 0 )

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Report Type" ), wx.VERTICAL )

		self.m_radioBtn1 = wx.RadioButton( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Дневен отчет", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

		self.m_radioBtn2 = wx.RadioButton( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Месечен отчет", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_radioBtn2, 0, wx.ALL, 5 )


		fgSizer8.Add( sbSizer1, 1, wx.EXPAND, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Номер на отчет", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		fgSizer9.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_spinCtrl6 = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 15000, 0 )
		fgSizer9.Add( self.m_spinCtrl6, 0, wx.ALL, 5 )


		fgSizer8.Add( fgSizer9, 1, wx.EXPAND|wx.ALIGN_RIGHT, 5 )


		gSizer6.Add( fgSizer8, 1, wx.EXPAND, 5 )

		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"От/До Дата", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.Hide()

		gSizer7.Add( self.m_checkBox2, 0, wx.ALL, 5 )


		gSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, u"01.06.2023", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl10.Hide()

		gSizer7.Add( self.m_textCtrl10, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, u"30.06.2023", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl11.Hide()

		gSizer7.Add( self.m_textCtrl11, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Генерирай", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		gSizer6.Add( gSizer7, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer6 )
		self.Layout()
		gSizer6.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_radioBtn1.Bind( wx.EVT_RADIOBUTTON, self.OnDoc )
		self.m_radioBtn2.Bind( wx.EVT_RADIOBUTTON, self.OnDoc )
		self.m_button5.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnDoc( self, event ):
		event.Skip()



	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class Server
###########################################################################

class Server ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer7 = wx.GridSizer( 3, 0, 0, 0 )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer7.Add( gSizer5, 1, wx.EXPAND, 5 )

		gSizer4 = wx.GridSizer( 0, 3, 0, 0 )

		gSizer71 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer4.Add( gSizer71, 1, wx.EXPAND, 5 )

		fgSizer7 = wx.FlexGridSizer( 5, 0, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Сървър", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText5.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer7.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice1Choices = []
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, wx.CB_SORT )
		self.m_choice1.SetSelection( 0 )
		self.m_choice1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer7.Add( self.m_choice1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_bpButton3 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton3.SetBitmap( wx.Bitmap( u"img/22x22/list-add.png", wx.BITMAP_TYPE_ANY ) )
		gSizer10.Add( self.m_bpButton3, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Вход", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer10.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer7.Add( gSizer10, 1, wx.EXPAND, 5 )

		gSizer25 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_checkBox3 = wx.CheckBox( self, wx.ID_ANY, u"Отвори порт", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_checkBox3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_checkBox4 = wx.CheckBox( self, wx.ID_ANY, u"TCP", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_checkBox4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )


		fgSizer7.Add( gSizer25, 1, wx.EXPAND, 5 )

		gSizer31 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_checkBox5 = wx.CheckBox( self, wx.ID_ANY, u"Скачащо криптиране", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_checkBox5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer7.Add( gSizer31, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer4.Add( fgSizer7, 1, wx.EXPAND, 5 )


		gSizer7.Add( gSizer4, 1, wx.EXPAND, 5 )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer7.Add( gSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer7 )
		self.Layout()
		gSizer7.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_bpButton3.Bind( wx.EVT_BUTTON, self.OnAdd )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnAdd( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class NewServer
###########################################################################

class NewServer ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добави сървър", pos = wx.DefaultPosition, size = wx.Size( 396,290 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer49 = wx.GridSizer( 5, 0, 0, 0 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Име", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText9.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer49.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer49.Add( self.m_textCtrl4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Адрес", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText10.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer49.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		gSizer49.Add( self.m_textCtrl5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		gSizer53 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer53.Add( self.m_button16, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Добави", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer53.Add( self.m_button17, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		gSizer49.Add( gSizer53, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer49 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl5.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_button16.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button17.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnGo( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()



###########################################################################
## Class MainPanel
###########################################################################

class MainPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = 0, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer1 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_toolBar2 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_FLAT|wx.TB_HORIZONTAL|wx.TB_TEXT )
		self.m_toolBar2.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_tool3 = self.m_toolBar2.AddTool( wx.ID_ANY, u"Регион", wx.Bitmap( u"img/64x64/network-server-database.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool9 = self.m_toolBar2.AddTool( wx.ID_ANY, u"Отчети", wx.Bitmap( u"img/64x64/Emblem-Money-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool5 = self.m_toolBar2.AddTool( wx.ID_ANY, u"Настройки", wx.Bitmap( u"img/64x64/Gnome-Applications-System-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool8 = self.m_toolBar2.AddTool( wx.ID_ANY, u"М. Броячи", wx.Bitmap( u"img/64x64/Gnome-System-Search-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool91 = self.m_toolBar2.AddTool( wx.ID_ANY, u"Печат на отчет", wx.Bitmap( u"img/64x64/Accessories-Dictionary-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool10 = self.m_toolBar2.AddTool( wx.ID_ANY, u"Справки", wx.Bitmap( u"img/64x64/Gnome-X-Office-Presentation-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool102 = self.m_toolBar2.AddTool( wx.ID_ANY, u"Клиенти", wx.Bitmap( u"img/64x64/system-users.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool101 = self.m_toolBar2.AddTool( wx.ID_ANY, u"Начало на смяна", wx.Bitmap( u"img/64x64/Gnome-Appointment-New-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool103 = self.m_toolBar2.AddTool( wx.ID_ANY, u"РКО", wx.Bitmap( u"img/64x64/okular.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool21 = self.m_toolBar2.AddTool( wx.ID_ANY, u"Изход", wx.Bitmap( u"img/64x64/Gnome-Application-Exit-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar2.Realize()

		fgSizer1.Add( self.m_toolBar2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer23 = wx.GridSizer( 4, 0, 0, 0 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Каса:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText8.SetForegroundColour( wx.Colour( 174, 0, 0 ) )

		gSizer23.Add( self.m_staticText8, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Регион: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText11.SetForegroundColour( wx.Colour( 174, 0, 0 ) )

		gSizer23.Add( self.m_staticText11, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Потребител: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText10.SetForegroundColour( wx.Colour( 174, 0, 0 ) )

		gSizer23.Add( self.m_staticText10, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Съобщения: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText15.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizer23.Add( self.m_staticText15, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer1.Add( gSizer23, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_listCtrl4 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_VRULES|wx.TAB_TRAVERSAL )
		self.m_listCtrl4.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_listCtrl4.SetMinSize( wx.Size( 920,-1 ) )

		fgSizer8.Add( self.m_listCtrl4, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,160 ), wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 20, 20 )
		self.m_scrolledWindow1.SetMinSize( wx.Size( 120,160 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_button9 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Проверка/SMIB", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_button9.Hide()

		bSizer1.Add( self.m_button9, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button26 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Намерих грешка", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button26.Hide()

		bSizer1.Add( self.m_button26, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button301 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Съобщение", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button301.Hide()

		bSizer1.Add( self.m_button301, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button25 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Бонус Карти", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button25.Hide()

		bSizer1.Add( self.m_button25, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button7 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Извади Бил", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button7.Hide()

		bSizer1.Add( self.m_button7, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button8 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Добави ключ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button8.Hide()

		bSizer1.Add( self.m_button8, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button6 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Пусни бил", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.Hide()

		bSizer1.Add( self.m_button6, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button30 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Спри Бил", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button30.Hide()

		bSizer1.Add( self.m_button30, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button12 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Резервация", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button12.Hide()

		bSizer1.Add( self.m_button12, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button21 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Забави рилове", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button21.Hide()

		bSizer1.Add( self.m_button21, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button13 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Наблюдавай", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button13.Hide()

		bSizer1.Add( self.m_button13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_button15 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Рестарт SMIB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button15.Hide()

		bSizer1.Add( self.m_button15, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button22 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Отключи/SMIB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button22.Hide()

		bSizer1.Add( self.m_button22, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button251 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Извади пари", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button251.Hide()

		bSizer1.Add( self.m_button251, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button32 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Изтрий играч", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button32.Hide()

		bSizer1.Add( self.m_button32, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button35 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Свери Час", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button35.Hide()

		bSizer1.Add( self.m_button35, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer1 )
		self.m_scrolledWindow1.Layout()
		fgSizer8.Add( self.m_scrolledWindow1, 0, wx.ALL, 5 )


		fgSizer1.Add( fgSizer8, 0, wx.EXPAND, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()
		fgSizer1.Fit( self )

		# Connect Events
		self.Bind( wx.EVT_TOOL, self.OnMexCHK, id = self.m_tool8.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnClient, id = self.m_tool102.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnWorkStartNow, id = self.m_tool101.GetId() )
		self.m_staticText15.Bind( wx.EVT_LEFT_DCLICK, self.OnShowMSG )
		self.m_button9.Bind( wx.EVT_BUTTON, self.OnMashinStartCHK )
		self.m_button26.Bind( wx.EVT_BUTTON, self.OnBugReport )
		self.m_button301.Bind( wx.EVT_BUTTON, self.OnMSG )
		self.m_button25.Bind( wx.EVT_BUTTON, self.OnBonusLog )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnGetBill )
		self.m_button8.Bind( wx.EVT_BUTTON, self.OnCreditNotWork )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnNotBillStart )
		self.m_button30.Bind( wx.EVT_BUTTON, self.OnBilHalt )
		self.m_button12.Bind( wx.EVT_BUTTON, self.OnRezerve )
		self.m_button21.Bind( wx.EVT_BUTTON, self.HoldRill )
		self.m_button13.Bind( wx.EVT_BUTTON, self.OnRealTimeLook )
		self.m_button15.Bind( wx.EVT_BUTTON, self.OnReboot )
		self.m_button22.Bind( wx.EVT_BUTTON, self.UnLoockSMIB )
		self.m_button251.Bind( wx.EVT_BUTTON, self.OnOut )
		self.m_button32.Bind( wx.EVT_BUTTON, self.PlayerReset )
		self.m_button35.Bind( wx.EVT_BUTTON, self.SetEMGTime )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnMexCHK( self, event ):
		event.Skip()

	def OnClient( self, event ):
		event.Skip()

	def OnWorkStartNow( self, event ):
		event.Skip()

	def OnShowMSG( self, event ):
		event.Skip()

	def OnMashinStartCHK( self, event ):
		event.Skip()

	def OnBugReport( self, event ):
		event.Skip()

	def OnMSG( self, event ):
		event.Skip()

	def OnBonusLog( self, event ):
		event.Skip()

	def OnGetBill( self, event ):
		event.Skip()

	def OnCreditNotWork( self, event ):
		event.Skip()

	def OnNotBillStart( self, event ):
		event.Skip()

	def OnBilHalt( self, event ):
		event.Skip()

	def OnRezerve( self, event ):
		event.Skip()

	def HoldRill( self, event ):
		event.Skip()

	def OnRealTimeLook( self, event ):
		event.Skip()

	def OnReboot( self, event ):
		event.Skip()

	def UnLoockSMIB( self, event ):
		event.Skip()

	def OnOut( self, event ):
		event.Skip()

	def PlayerReset( self, event ):
		event.Skip()

	def SetEMGTime( self, event ):
		event.Skip()


###########################################################################
## Class KSChangeGuage
###########################################################################

class KSChangeGuage ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Смяна на ключ", pos = wx.DefaultPosition, size = wx.Size( 117,131 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 )
		bSizer8.Add( self.m_gauge1, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Машина: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer8.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button21, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button21.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()



###########################################################################
## Class LoginPanel
###########################################################################

class LoginPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		gSizer7 = wx.GridSizer( 3, 0, 0, 0 )

		gSizer5 = wx.GridSizer( 0, 3, 0, 0 )

		gSizer28 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"12.07.2021 17:15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		self.m_staticText61.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText61.SetForegroundColour( wx.Colour( 38, 197, 41 ) )

		gSizer28.Add( self.m_staticText61, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		gSizer5.Add( gSizer28, 1, wx.EXPAND, 5 )

		gSizer30 = wx.GridSizer( 0, 1, 0, 0 )


		gSizer5.Add( gSizer30, 1, wx.EXPAND, 5 )

		gSizer29 = wx.GridSizer( 0, 1, 0, 0 )


		gSizer5.Add( gSizer29, 1, wx.EXPAND, 5 )


		gSizer7.Add( gSizer5, 1, wx.EXPAND, 5 )

		gSizer4 = wx.GridSizer( 0, 3, 0, 0 )

		gSizer71 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer4.Add( gSizer71, 1, wx.EXPAND, 5 )

		gSizer8 = wx.GridSizer( 5, 0, 0, 0 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Потребителско име", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText5.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer8.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		m_choice1Choices = []
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, wx.CB_SORT )
		self.m_choice1.SetSelection( 0 )
		self.m_choice1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer8.Add( self.m_choice1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Парола", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText6.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer8.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
		self.m_textCtrl5.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer8.Add( self.m_textCtrl5, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Вход с карта", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer10.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Вход", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer10.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		gSizer8.Add( gSizer10, 1, wx.EXPAND, 5 )


		gSizer4.Add( gSizer8, 1, wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer4.Add( gSizer9, 1, wx.EXPAND, 5 )


		gSizer7.Add( gSizer4, 1, wx.EXPAND, 5 )

		gSizer6 = wx.GridSizer( 0, 3, 0, 0 )


		gSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Промени сървър", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		gSizer6.Add( self.m_checkBox1, 0, wx.ALL, 5 )


		gSizer7.Add( gSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer7 )
		self.Layout()
		gSizer7.Fit( self )

		# Connect Events
		self.m_textCtrl5.Bind( wx.EVT_TEXT_ENTER, self.OnIn )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnInWithCart )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnIn )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.OnServer )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnIn( self, event ):
		event.Skip()

	def OnInWithCart( self, event ):
		event.Skip()


	def OnServer( self, event ):
		event.Skip()


###########################################################################
## Class Diagnostic
###########################################################################

class Diagnostic ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 381,285 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer10 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_richText2 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,200 ), wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.WANTS_CHARS|wx.BORDER_NONE )
		fgSizer10.Add( self.m_richText2, 1, wx.EXPAND|wx.ALL|wx.ALIGN_RIGHT, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_button19 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button19, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		fgSizer10.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button19.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()



###########################################################################
## Class RegisterKey
###########################################################################

class RegisterKey ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Регистриране на POS терминал", pos = wx.DefaultPosition, size = wx.Size( 517,190 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Нямате права за достъп!\nМоля свържете се със администратор!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText10.SetForegroundColour( wx.Colour( 163, 0, 0 ) )

		bSizer3.Add( self.m_staticText10, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.TE_READONLY )
		self.m_textCtrl5.SetMinSize( wx.Size( 500,-1 ) )

		bSizer3.Add( self.m_textCtrl5, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer25 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button30 = wx.Button( self, wx.ID_ANY, u"Сървър", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_button30, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Напред", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_button18, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		bSizer3.Add( gSizer25, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_textCtrl5.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_button30.Bind( wx.EVT_BUTTON, self.OnRevert )
		self.m_button18.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()

	def OnRevert( self, event ):
		event.Skip()



###########################################################################
## Class HoldRill
###########################################################################

class HoldRill ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Забавяне на рилове", pos = wx.DefaultPosition, size = wx.Size( 253,183 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Време за забавяне", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer4.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"(кратно на 100)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText12.SetForegroundColour( wx.Colour( 219, 0, 0 ) )

		bSizer4.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_radioBtn3 = wx.RadioButton( self, wx.ID_ANY, u"Софтуер", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn3.Hide()

		bSizer6.Add( self.m_radioBtn3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_radioBtn4 = wx.RadioButton( self, wx.ID_ANY, u"Хардуер", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn4.Hide()

		bSizer6.Add( self.m_radioBtn4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )

		self.m_spinCtrl2 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 500, 0 )
		bSizer4.Add( self.m_spinCtrl2, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer21 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button19 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer21.Add( self.m_button19, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer21.Add( self.m_button20, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		bSizer4.Add( gSizer21, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_spinCtrl2.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_button19.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button20.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
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
## Class SetPosID
###########################################################################

class SetPosID ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Регистрирай", pos = wx.DefaultPosition, size = wx.Size( 386,301 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Потребител", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer6.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_choice4Choices = []
		self.m_choice4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 0 )
		bSizer6.Add( self.m_choice4, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Парола", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer6.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
		bSizer6.Add( self.m_textCtrl6, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Pos Име", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer6.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer6.Add( self.m_textCtrl7, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer26 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button30 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer26.Add( self.m_button30, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button31 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer26.Add( self.m_button31, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		bSizer6.Add( gSizer26, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_textCtrl6.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_textCtrl7.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_button30.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button31.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()





###########################################################################
## Class SetTime
###########################################################################

class SetTime ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Свери час на EMG", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Дата", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer4.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Формат 2020-06-30", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText12.SetForegroundColour( wx.Colour( 219, 0, 0 ) )

		bSizer4.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl8, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"Час", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		self.m_staticText111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText111.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer4.Add( self.m_staticText111, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText121 = wx.StaticText( self, wx.ID_ANY, u"Формат 12:35", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		self.m_staticText121.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText121.SetForegroundColour( wx.Colour( 219, 0, 0 ) )

		bSizer4.Add( self.m_staticText121, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl9, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer21 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button19 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer21.Add( self.m_button19, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer21.Add( self.m_button20, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		bSizer4.Add( gSizer21, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()
		bSizer4.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button19.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button20.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


