# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class AddCart
###########################################################################

class AddCart ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добавяне на карта", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.Size( 540,112 ), wx.DefaultSize )

		gSizer14 = wx.GridSizer( 2, 1, 0, 0 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Моля поставете карта в четеца!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText13.SetForegroundColour( wx.Colour( 197, 33, 33 ) )

		gSizer14.Add( self.m_staticText13, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer10 = wx.GridSizer( 1, 2, 0, 0 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Добави", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		gSizer14.Add( gSizer10, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer14 )
		self.Layout()
		gSizer14.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button8.Bind( wx.EVT_BUTTON, self.OnAddNew )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnAddNew( self, event ):
		event.Skip()


###########################################################################
## Class MainCust
###########################################################################

class MainCust ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer7 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_toolBar5 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL|wx.TB_TEXT )
		self.m_toolBar5.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_tool2 = self.m_toolBar5.AddTool( wx.ID_ANY, u"Нов клиент", wx.Bitmap( u"img/64x64/gnome-about-me.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool9 = self.m_toolBar5.AddTool( wx.ID_ANY, u"Редактирай Клиент", wx.Bitmap( u"img/64x64/User-Info-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool3 = self.m_toolBar5.AddTool( wx.ID_ANY, u"Нова група", wx.Bitmap( u"img/64x64/system-users.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool4 = self.m_toolBar5.AddTool( wx.ID_ANY, u"Мънибек", wx.Bitmap( u"img/64x64/Gnome-Emblem-Shared-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool5 = self.m_toolBar5.AddTool( wx.ID_ANY, u"Печат на талони", wx.Bitmap( u"img/64x64/Gnome-Emblem-Photos-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool7 = self.m_toolBar5.AddTool( wx.ID_ANY, u"Добави пари", wx.Bitmap( u"img/64x64/speedcrunch.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool8 = self.m_toolBar5.AddTool( wx.ID_ANY, u"Изплати", wx.Bitmap( u"img/64x64/Gnome-Go-Jump-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool91 = self.m_toolBar5.AddTool( wx.ID_ANY, u"С. Талон", wx.Bitmap( u"img/64x64/Gnome-Printer-Printing-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool1 = self.m_toolBar5.AddTool( wx.ID_ANY, u"Затвори", wx.Bitmap( u"img/64x64/dialog-error.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar5.Realize()

		fgSizer7.Add( self.m_toolBar5, 0, wx.EXPAND, 5 )

		fgSizer71 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer71.SetFlexibleDirection( wx.BOTH )
		fgSizer71.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		fgSizer71.Add( self.m_choice3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_searchCtrl1 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TE_PROCESS_ENTER )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( True )
		fgSizer71.Add( self.m_searchCtrl1, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_bpButton9 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton9.SetBitmap( wx.Bitmap( u"img/32x32/Gnome-Network-Server-32.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer71.Add( self.m_bpButton9, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer7.Add( fgSizer71, 1, wx.EXPAND, 5 )

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer12.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_listCtrl2 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer12.Add( self.m_listCtrl2, 1, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5 )


		fgSizer8.Add( fgSizer12, 1, wx.EXPAND, 5 )


		fgSizer7.Add( fgSizer8, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer7 )
		self.Layout()
		fgSizer7.Fit( self )

		# Connect Events
		self.Bind( wx.EVT_TOOL, self.AddUser, id = self.m_tool2.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnEditCust, id = self.m_tool9.GetId() )
		self.Bind( wx.EVT_TOOL, self.AddGrup, id = self.m_tool3.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnMonyBackPay, id = self.m_tool4.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnTalonPrint, id = self.m_tool5.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnMonyAdd, id = self.m_tool7.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnPay, id = self.m_tool8.GetId() )
		self.Bind( wx.EVT_TOOL, self.FreeTalon, id = self.m_tool91.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnClose, id = self.m_tool1.GetId() )
		self.m_searchCtrl1.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.OnSearch )
		self.m_searchCtrl1.Bind( wx.EVT_TEXT_ENTER, self.OnSearch )
		self.m_bpButton9.Bind( wx.EVT_BUTTON, self.OnCHKnra )
		self.m_listCtrl1.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnGrupFilter )
		self.m_listCtrl2.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnUserShow )
		self.m_listCtrl2.Bind( wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightMenu )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def AddUser( self, event ):
		event.Skip()

	def OnEditCust( self, event ):
		event.Skip()

	def AddGrup( self, event ):
		event.Skip()

	def OnMonyBackPay( self, event ):
		event.Skip()

	def OnTalonPrint( self, event ):
		event.Skip()

	def OnMonyAdd( self, event ):
		event.Skip()

	def OnPay( self, event ):
		event.Skip()

	def FreeTalon( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()

	def OnSearch( self, event ):
		event.Skip()


	def OnCHKnra( self, event ):
		event.Skip()

	def OnGrupFilter( self, event ):
		event.Skip()

	def OnUserShow( self, event ):
		event.Skip()

	def RightMenu( self, event ):
		event.Skip()


###########################################################################
## Class ShowCust
###########################################################################

class ShowCust ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Месечна статистика", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Customer" ), wx.VERTICAL )

		self.m_staticText42 = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Григор Колев", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		self.m_staticText42.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText42.SetForegroundColour( wx.Colour( 0, 11, 250 ) )

		sbSizer21.Add( self.m_staticText42, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText43 = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"01.02.2019 / 06.02.2019", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		self.m_staticText43.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText43.SetForegroundColour( wx.Colour( 0, 11, 250 ) )

		sbSizer21.Add( self.m_staticText43, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText78 = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Група: Vip", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( -1 )

		self.m_staticText78.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText78.SetForegroundColour( wx.Colour( 0, 11, 250 ) )

		sbSizer21.Add( self.m_staticText78, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText811 = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"ЕГН", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText811.Wrap( -1 )

		self.m_staticText811.SetForegroundColour( wx.Colour( 0, 11, 250 ) )

		sbSizer21.Add( self.m_staticText811, 0, wx.ALL, 5 )

		self.m_staticText79 = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Индивидуални настройки: Не", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )

		self.m_staticText79.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText79.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		sbSizer21.Add( self.m_staticText79, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		fgSizer8.Add( sbSizer21, 1, wx.EXPAND, 5 )

		sbSizer22 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Statistics" ), wx.VERTICAL )

		gSizer14 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText44 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Вход:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		gSizer14.Add( self.m_staticText44, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText45 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		gSizer14.Add( self.m_staticText45, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer22.Add( gSizer14, 1, wx.EXPAND, 5 )

		gSizer15 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText46 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Изход: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		gSizer15.Add( self.m_staticText46, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText47 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		gSizer15.Add( self.m_staticText47, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer22.Add( gSizer15, 1, wx.EXPAND, 5 )

		gSizer30 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText94 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Тотал:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText94.Wrap( -1 )

		gSizer30.Add( self.m_staticText94, 0, wx.ALL, 5 )

		self.m_staticText95 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText95.Wrap( -1 )

		gSizer30.Add( self.m_staticText95, 0, wx.ALL, 5 )


		sbSizer22.Add( gSizer30, 1, wx.EXPAND, 5 )

		gSizer16 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText48 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Бил: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		gSizer16.Add( self.m_staticText48, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText49 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		gSizer16.Add( self.m_staticText49, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer22.Add( gSizer16, 1, wx.EXPAND, 5 )

		gSizer17 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText50 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Игри: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		gSizer17.Add( self.m_staticText50, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		gSizer17.Add( self.m_staticText51, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer22.Add( gSizer17, 1, wx.EXPAND, 5 )

		gSizer18 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText52 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Средно Бет: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		gSizer18.Add( self.m_staticText52, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText53 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		gSizer18.Add( self.m_staticText53, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer22.Add( gSizer18, 1, wx.EXPAND, 5 )


		fgSizer8.Add( sbSizer22, 1, wx.EXPAND, 5 )

		sbSizer23 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Moneyback" ), wx.VERTICAL )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText58 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Не усвоен:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )

		fgSizer9.Add( self.m_staticText58, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText59 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )

		fgSizer9.Add( self.m_staticText59, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer23.Add( fgSizer9, 1, wx.EXPAND, 5 )

		fgSizer10 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText60 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Усвоен: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )

		fgSizer10.Add( self.m_staticText60, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText61 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		fgSizer10.Add( self.m_staticText61, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer23.Add( fgSizer10, 1, wx.EXPAND, 5 )

		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText64 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Общо: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )

		fgSizer12.Add( self.m_staticText64, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText65 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )

		fgSizer12.Add( self.m_staticText65, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer23.Add( fgSizer12, 1, wx.EXPAND, 5 )


		fgSizer8.Add( sbSizer23, 1, wx.EXPAND, 5 )

		sbSizer26 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Draw" ), wx.VERTICAL )

		fgSizer91 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer91.SetFlexibleDirection( wx.BOTH )
		fgSizer91.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText581 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Не усвоен:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText581.Wrap( -1 )

		fgSizer91.Add( self.m_staticText581, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText591 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText591.Wrap( -1 )

		fgSizer91.Add( self.m_staticText591, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer26.Add( fgSizer91, 1, wx.EXPAND, 5 )

		fgSizer101 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer101.SetFlexibleDirection( wx.BOTH )
		fgSizer101.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText601 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Усвоен: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText601.Wrap( -1 )

		fgSizer101.Add( self.m_staticText601, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText611 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText611.Wrap( -1 )

		fgSizer101.Add( self.m_staticText611, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer26.Add( fgSizer101, 1, wx.EXPAND, 5 )

		fgSizer121 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer121.SetFlexibleDirection( wx.BOTH )
		fgSizer121.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText641 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Общо: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText641.Wrap( -1 )

		fgSizer121.Add( self.m_staticText641, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText651 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText651.Wrap( -1 )

		fgSizer121.Add( self.m_staticText651, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer26.Add( fgSizer121, 1, wx.EXPAND, 5 )


		fgSizer8.Add( sbSizer26, 1, wx.EXPAND, 5 )

		sbSizer27 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Visits" ), wx.VERTICAL )

		fgSizer23 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer23.SetFlexibleDirection( wx.BOTH )
		fgSizer23.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText80 = wx.StaticText( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Последно дата: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )

		fgSizer23.Add( self.m_staticText80, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText81 = wx.StaticText( sbSizer27.GetStaticBox(), wx.ID_ANY, u"03.02.2019", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		fgSizer23.Add( self.m_staticText81, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer27.Add( fgSizer23, 1, wx.EXPAND, 5 )

		fgSizer24 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText82 = wx.StaticText( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Общо:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )

		fgSizer24.Add( self.m_staticText82, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText83 = wx.StaticText( sbSizer27.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )

		fgSizer24.Add( self.m_staticText83, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer27.Add( fgSizer24, 1, wx.EXPAND, 5 )


		fgSizer8.Add( sbSizer27, 1, wx.EXPAND, 5 )

		sbSizer29 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Bonus" ), wx.VERTICAL )

		fgSizer25 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer25.SetFlexibleDirection( wx.BOTH )
		fgSizer25.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText84 = wx.StaticText( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Сума:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )

		fgSizer25.Add( self.m_staticText84, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText85 = wx.StaticText( sbSizer29.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )

		fgSizer25.Add( self.m_staticText85, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer29.Add( fgSizer25, 1, wx.EXPAND, 5 )


		fgSizer8.Add( sbSizer29, 1, wx.EXPAND, 5 )

		sbSizer30 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Machines" ), wx.VERTICAL )

		fgSizer26 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer26.SetFlexibleDirection( wx.BOTH )
		fgSizer26.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText86 = wx.StaticText( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Предпочитана машина: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )

		fgSizer26.Add( self.m_staticText86, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText87 = wx.StaticText( sbSizer30.GetStaticBox(), wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText87.Wrap( -1 )

		fgSizer26.Add( self.m_staticText87, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer30.Add( fgSizer26, 1, wx.EXPAND, 5 )


		fgSizer8.Add( sbSizer30, 1, wx.EXPAND, 5 )

		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Card" ), wx.VERTICAL )

		fgSizer27 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer27.SetFlexibleDirection( wx.BOTH )
		fgSizer27.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText90 = wx.StaticText( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Общ карти: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText90.Wrap( -1 )

		fgSizer27.Add( self.m_staticText90, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText91 = wx.StaticText( sbSizer31.GetStaticBox(), wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		fgSizer27.Add( self.m_staticText91, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer31.Add( fgSizer27, 1, wx.EXPAND, 5 )


		fgSizer8.Add( sbSizer31, 1, wx.EXPAND, 5 )


		fgSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button14 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button14, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( fgSizer8 )
		self.Layout()
		fgSizer8.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button14.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()



###########################################################################
## Class AddCust
###########################################################################

class AddCust ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Клиент", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )

		fgSizer6 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_scrolledWindow3 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow3.SetScrollRate( 5, 5 )
		fgSizer8 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer711 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_bpButton211 = wx.BitmapButton( self.m_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton211.SetBitmap( wx.Bitmap( u"img/128x128/Assistant.png", wx.BITMAP_TYPE_ANY ) )
		gSizer711.Add( self.m_bpButton211, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer311 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1711 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"Име", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1711.Wrap( -1 )

		self.m_staticText1711.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText1711.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer311.Add( self.m_staticText1711, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl911 = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer311.Add( self.m_textCtrl911, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText1811 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"Телефон", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1811.Wrap( -1 )

		self.m_staticText1811.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText1811.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer311.Add( self.m_staticText1811, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl1011 = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer311.Add( self.m_textCtrl1011, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText2011 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"E-mail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2011.Wrap( -1 )

		self.m_staticText2011.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText2011.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer311.Add( self.m_staticText2011, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl1211 = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer311.Add( self.m_textCtrl1211, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button34 = wx.Button( self.m_scrolledWindow3, wx.ID_ANY, u"Прочети лична карта", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer311.Add( self.m_button34, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText41 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"PIN: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		self.m_staticText41.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText41.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer9.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.m_staticText421 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText421.Wrap( -1 )

		self.m_staticText421.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText421.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer9.Add( self.m_staticText421, 0, wx.ALL, 5 )


		bSizer311.Add( bSizer9, 1, wx.EXPAND, 5 )


		gSizer711.Add( bSizer311, 1, wx.EXPAND, 5 )

		sbSizer921 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"Personal data" ), wx.HORIZONTAL )

		bSizer411 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2411 = wx.StaticText( sbSizer921.GetStaticBox(), wx.ID_ANY, u"ЕГН", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2411.Wrap( -1 )

		bSizer411.Add( self.m_staticText2411, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl1621 = wx.TextCtrl( sbSizer921.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer411.Add( self.m_textCtrl1621, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox601 = wx.CheckBox( sbSizer921.GetStaticBox(), wx.ID_ANY, u"Мъж", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox601.SetValue(True)
		bSizer411.Add( self.m_checkBox601, 0, wx.ALL, 5 )

		self.m_button29 = wx.Button( sbSizer921.GetStaticBox(), wx.ID_ANY, u"Валидирай ЕГН", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer411.Add( self.m_button29, 0, wx.ALL, 5 )

		self.m_staticText2511 = wx.StaticText( sbSizer921.GetStaticBox(), wx.ID_ANY, u"SN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2511.Wrap( -1 )

		bSizer411.Add( self.m_staticText2511, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl1721 = wx.TextCtrl( sbSizer921.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer411.Add( self.m_textCtrl1721, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText2611 = wx.StaticText( sbSizer921.GetStaticBox(), wx.ID_ANY, u"Адрес", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2611.Wrap( -1 )

		bSizer411.Add( self.m_staticText2611, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl1811 = wx.TextCtrl( sbSizer921.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer411.Add( self.m_textCtrl1811, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer921.Add( bSizer411, 1, wx.EXPAND, 5 )

		bSizer511 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2711 = wx.StaticText( sbSizer921.GetStaticBox(), wx.ID_ANY, u"Град", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2711.Wrap( -1 )

		bSizer511.Add( self.m_staticText2711, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		m_choice211Choices = []
		self.m_choice211 = wx.Choice( sbSizer921.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), m_choice211Choices, 0 )
		self.m_choice211.SetSelection( 0 )
		bSizer511.Add( self.m_choice211, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_bpButton311 = wx.BitmapButton( sbSizer921.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton311.SetBitmap( wx.Bitmap( u"img/22x22/list-add.png", wx.BITMAP_TYPE_ANY ) )
		bSizer511.Add( self.m_bpButton311, 0, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5 )

		self.m_staticText2811 = wx.StaticText( sbSizer921.GetStaticBox(), wx.ID_ANY, u"Валидна до", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2811.Wrap( -1 )

		bSizer511.Add( self.m_staticText2811, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl18 = wx.TextCtrl( sbSizer921.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer511.Add( self.m_textCtrl18, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText80 = wx.StaticText( sbSizer921.GetStaticBox(), wx.ID_ANY, u"Код на държава", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )

		bSizer511.Add( self.m_staticText80, 0, wx.ALL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( sbSizer921.GetStaticBox(), wx.ID_ANY, u"BGR", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer511.Add( self.m_textCtrl20, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer921.Add( bSizer511, 1, wx.EXPAND, 5 )


		gSizer711.Add( sbSizer921, 1, wx.EXPAND, 5 )


		fgSizer8.Add( gSizer711, 1, wx.EXPAND, 5 )

		gSizer911 = wx.GridSizer( 0, 3, 0, 0 )

		bSizer611 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3011 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"Група", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3011.Wrap( -1 )

		bSizer611.Add( self.m_staticText3011, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_choice311Choices = []
		self.m_choice311 = wx.Choice( self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice311Choices, 0 )
		self.m_choice311.SetSelection( 0 )
		bSizer611.Add( self.m_choice311, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button1011 = wx.Button( self.m_scrolledWindow3, wx.ID_ANY, u"Добави Група", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer611.Add( self.m_button1011, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer19 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"Card" ), wx.VERTICAL )

		gSizer131 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_bpButton312 = wx.BitmapButton( sbSizer19.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton312.SetBitmap( wx.Bitmap( u"img/22x22/list-add.png", wx.BITMAP_TYPE_ANY ) )
		gSizer131.Add( self.m_bpButton312, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_bpButton13 = wx.BitmapButton( sbSizer19.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton13.SetBitmap( wx.Bitmap( u"img/22x22/media-playlist-shuffle.png", wx.BITMAP_TYPE_ANY ) )
		gSizer131.Add( self.m_bpButton13, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_bpButton81 = wx.BitmapButton( sbSizer19.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton81.SetBitmap( wx.Bitmap( u"img/22x22/list-remove.png", wx.BITMAP_TYPE_ANY ) )
		gSizer131.Add( self.m_bpButton81, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer19.Add( gSizer131, 1, wx.EXPAND, 5 )

		self.m_staticText42 = wx.StaticText( sbSizer19.GetStaticBox(), wx.ID_ANY, u"Общо карти: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		sbSizer19.Add( self.m_staticText42, 0, wx.ALL, 5 )


		bSizer611.Add( sbSizer19, 1, wx.EXPAND, 5 )


		gSizer911.Add( bSizer611, 1, wx.EXPAND, 5 )

		sbSizer1011 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"Settings" ), wx.VERTICAL )

		self.m_radioBtn311 = wx.RadioButton( sbSizer1011.GetStaticBox(), wx.ID_ANY, u"От Група", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1011.Add( self.m_radioBtn311, 0, wx.ALL, 5 )

		self.m_radioBtn411 = wx.RadioButton( sbSizer1011.GetStaticBox(), wx.ID_ANY, u"Персонални", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1011.Add( self.m_radioBtn411, 0, wx.ALL, 5 )

		self.m_checkBox13 = wx.CheckBox( sbSizer1011.GetStaticBox(), wx.ID_ANY, u"Забрана", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1011.Add( self.m_checkBox13, 0, wx.ALL, 5 )

		self.m_checkBox59 = wx.CheckBox( sbSizer1011.GetStaticBox(), wx.ID_ANY, u"Вписън в НАП", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1011.Add( self.m_checkBox59, 0, wx.ALL, 5 )


		gSizer911.Add( sbSizer1011, 1, wx.EXPAND, 5 )

		sbSizer141 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"Processes" ), wx.VERTICAL )

		self.m_checkBox111 = wx.CheckBox( sbSizer141.GetStaticBox(), wx.ID_ANY, u"Мъни Бек", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer141.Add( self.m_checkBox111, 0, wx.ALL, 5 )

		self.m_checkBox211 = wx.CheckBox( sbSizer141.GetStaticBox(), wx.ID_ANY, u"Бонуси", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer141.Add( self.m_checkBox211, 0, wx.ALL, 5 )

		self.m_checkBox311 = wx.CheckBox( sbSizer141.GetStaticBox(), wx.ID_ANY, u"Томбула", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer141.Add( self.m_checkBox311, 0, wx.ALL, 5 )


		gSizer911.Add( sbSizer141, 1, wx.EXPAND, 5 )


		fgSizer8.Add( gSizer911, 1, wx.EXPAND, 5 )

		gSizer1011 = wx.GridSizer( 0, 4, 0, 0 )

		sbSizer511 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"Moneyback" ), wx.VERTICAL )

		self.m_staticText311 = wx.StaticText( sbSizer511.GetStaticBox(), wx.ID_ANY, u"Процент на отчисление", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText311.Wrap( -1 )

		self.m_staticText311.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText311.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		sbSizer511.Add( self.m_staticText311, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl411 = wx.TextCtrl( sbSizer511.GetStaticBox(), wx.ID_ANY, u"0.2", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer511.Add( self.m_textCtrl411, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText77 = wx.StaticText( sbSizer511.GetStaticBox(), wx.ID_ANY, u"Минимално изплащане", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )

		self.m_staticText77.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText77.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		sbSizer511.Add( self.m_staticText77, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_spinCtrl20 = wx.SpinCtrl( sbSizer511.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, 0, 1000, 0 )
		sbSizer511.Add( self.m_spinCtrl20, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText89 = wx.StaticText( sbSizer511.GetStaticBox(), wx.ID_ANY, u"Максимално изплащане", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText89.Wrap( -1 )

		self.m_staticText89.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText89.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		sbSizer511.Add( self.m_staticText89, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_spinCtrl42 = wx.SpinCtrl( sbSizer511.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sbSizer511.Add( self.m_spinCtrl42, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer1011.Add( sbSizer511, 1, wx.EXPAND, 5 )

		sbSizer711 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"Draw" ), wx.VERTICAL )

		self.m_staticText511 = wx.StaticText( sbSizer711.GetStaticBox(), wx.ID_ANY, u"Коефицент на 100 лв.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText511.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		sbSizer711.Add( self.m_staticText511, 0, wx.ALL, 5 )

		self.m_textCtrl511 = wx.TextCtrl( sbSizer711.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer711.Add( self.m_textCtrl511, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_checkBox56 = wx.CheckBox( sbSizer711.GetStaticBox(), wx.ID_ANY, u"Точки в пари", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer711.Add( self.m_checkBox56, 0, wx.ALL, 5 )

		self.m_spinCtrl48 = wx.SpinCtrl( sbSizer711.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 100, 1 )
		sbSizer711.Add( self.m_spinCtrl48, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_radioBtn9 = wx.RadioButton( sbSizer711.GetStaticBox(), wx.ID_ANY, u"По Бет", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_radioBtn9, 0, wx.ALL, 5 )

		self.m_radioBtn10 = wx.RadioButton( sbSizer711.GetStaticBox(), wx.ID_ANY, u"По Тотал", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_radioBtn10, 0, wx.ALL, 5 )


		sbSizer711.Add( bSizer10, 1, wx.EXPAND, 5 )


		gSizer1011.Add( sbSizer711, 1, wx.EXPAND, 5 )

		sbSizer9111 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"Bonus" ), wx.VERTICAL )

		self.m_radioBtn211 = wx.RadioButton( sbSizer9111.GetStaticBox(), wx.ID_ANY, u"По IN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn211.SetValue( True )
		sbSizer9111.Add( self.m_radioBtn211, 0, wx.ALL, 5 )

		self.m_radioBtn111 = wx.RadioButton( sbSizer9111.GetStaticBox(), wx.ID_ANY, u"По Бет", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9111.Add( self.m_radioBtn111, 0, wx.ALL, 5 )

		self.m_radioBtn11 = wx.RadioButton( sbSizer9111.GetStaticBox(), wx.ID_ANY, u"Деректен", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9111.Add( self.m_radioBtn11, 0, wx.ALL, 5 )

		self.m_checkBox48 = wx.CheckBox( sbSizer9111.GetStaticBox(), wx.ID_ANY, u"Не усвояем", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9111.Add( self.m_checkBox48, 0, wx.ALL, 5 )

		self.m_checkBox30 = wx.CheckBox( sbSizer9111.GetStaticBox(), wx.ID_ANY, u"Удържане", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9111.Add( self.m_checkBox30, 0, wx.ALL, 5 )

		self.m_checkBox10 = wx.CheckBox( sbSizer9111.GetStaticBox(), wx.ID_ANY, u"Веднъж на ден", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9111.Add( self.m_checkBox10, 0, wx.ALL, 5 )

		self.m_checkBox11 = wx.CheckBox( sbSizer9111.GetStaticBox(), wx.ID_ANY, u"Предходен тотал", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9111.Add( self.m_checkBox11, 0, wx.ALL, 5 )

		self.m_checkBox45 = wx.CheckBox( sbSizer9111.GetStaticBox(), wx.ID_ANY, u"Текущ месец", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9111.Add( self.m_checkBox45, 0, wx.ALL, 5 )

		self.m_checkBox131 = wx.CheckBox( sbSizer9111.GetStaticBox(), wx.ID_ANY, u"Изчакай вход", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9111.Add( self.m_checkBox131, 0, wx.ALL, 5 )

		self.m_spinCtrl33 = wx.SpinCtrl( sbSizer9111.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000000, 0 )
		sbSizer9111.Add( self.m_spinCtrl33, 0, wx.ALL, 5 )

		self.m_checkBox52 = wx.CheckBox( sbSizer9111.GetStaticBox(), wx.ID_ANY, u"Много от редирект ", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9111.Add( self.m_checkBox52, 0, wx.ALL, 5 )

		m_choice10Choices = []
		self.m_choice10 = wx.Choice( sbSizer9111.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice10Choices, 0 )
		self.m_choice10.SetSelection( 0 )
		sbSizer9111.Add( self.m_choice10, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer1011.Add( sbSizer9111, 1, wx.EXPAND, 5 )

		sbSizer20 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"Бонус" ), wx.VERTICAL )

		self.m_staticText39111 = wx.StaticText( sbSizer20.GetStaticBox(), wx.ID_ANY, u"На сума", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39111.Wrap( -1 )

		sbSizer20.Add( self.m_staticText39111, 0, wx.ALL, 5 )

		self.m_spinCtrl14111 = wx.SpinCtrl( sbSizer20.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 50000, 20 )
		sbSizer20.Add( self.m_spinCtrl14111, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText79 = wx.StaticText( sbSizer20.GetStaticBox(), wx.ID_ANY, u"Забрани изход", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )

		sbSizer20.Add( self.m_staticText79, 0, wx.ALL, 5 )

		self.m_checkBox43 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"По BET", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer20.Add( self.m_checkBox43, 0, wx.ALL, 5 )

		self.m_spinCtrl23 = wx.SpinCtrl( sbSizer20.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 100000, 1 )
		sbSizer20.Add( self.m_spinCtrl23, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox41 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"Предупреди за бонус", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer20.Add( self.m_checkBox41, 0, wx.ALL, 5 )

		self.m_spinCtrl40 = wx.SpinCtrl( sbSizer20.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10000, 0 )
		sbSizer20.Add( self.m_spinCtrl40, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox50 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"Процент от тотал", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox50.Enable( False )

		sbSizer20.Add( self.m_checkBox50, 0, wx.ALL, 5 )

		self.m_spinCtrl45 = wx.SpinCtrl( sbSizer20.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 100, 0 )
		self.m_spinCtrl45.Enable( False )

		sbSizer20.Add( self.m_spinCtrl45, 0, wx.ALL|wx.EXPAND, 5 )

		m_choice9Choices = []
		self.m_choice9 = wx.Choice( sbSizer20.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice9Choices, 0 )
		self.m_choice9.SetSelection( 0 )
		sbSizer20.Add( self.m_choice9, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer22 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox22 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"Всички", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox22.SetValue(True)
		bSizer17.Add( self.m_checkBox22, 0, wx.ALL, 5 )

		self.m_checkBox23 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"Понеделник", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_checkBox23, 0, wx.ALL, 5 )

		self.m_checkBox24 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"Вторник", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_checkBox24, 0, wx.ALL, 5 )

		self.m_checkBox25 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"Сряда", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_checkBox25, 0, wx.ALL, 5 )


		gSizer22.Add( bSizer17, 1, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox26 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"Четвъртък", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_checkBox26, 0, wx.ALL, 5 )

		self.m_checkBox27 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"Петък", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_checkBox27, 0, wx.ALL, 5 )

		self.m_checkBox28 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"Събота", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_checkBox28, 0, wx.ALL, 5 )

		self.m_checkBox29 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"Неделя", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_checkBox29, 0, wx.ALL, 5 )


		gSizer22.Add( bSizer18, 1, wx.EXPAND, 5 )


		sbSizer20.Add( gSizer22, 1, wx.EXPAND, 5 )


		gSizer1011.Add( sbSizer20, 1, wx.EXPAND, 5 )


		fgSizer8.Add( gSizer1011, 1, wx.EXPAND, 5 )

		gSizer11 = wx.GridSizer( 1, 2, 0, 0 )

		self.m_listCtrl6 = wx.ListCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		gSizer11.Add( self.m_listCtrl6, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer31 = wx.GridSizer( 1, 0, 0, 0 )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.m_button37 = wx.Button( self.m_scrolledWindow3, wx.ID_ANY, u"Премахни", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.m_button37, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button36 = wx.Button( self.m_scrolledWindow3, wx.ID_ANY, u"Добави", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.m_button36, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox60 = wx.CheckBox( self.m_scrolledWindow3, wx.ID_ANY, u"Добави сандък x2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox60.Hide()

		bSizer23.Add( self.m_checkBox60, 0, wx.ALL, 5 )


		gSizer31.Add( bSizer23, 1, wx.EXPAND, 5 )


		gSizer11.Add( gSizer31, 1, wx.EXPAND, 5 )


		fgSizer8.Add( gSizer11, 1, wx.EXPAND, 5 )


		self.m_scrolledWindow3.SetSizer( fgSizer8 )
		self.m_scrolledWindow3.Layout()
		fgSizer8.Fit( self.m_scrolledWindow3 )
		fgSizer6.Add( self.m_scrolledWindow3, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer1611 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button811 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1611.Add( self.m_button811, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button911 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1611.Add( self.m_button911, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		fgSizer6.Add( gSizer1611, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer6 )
		self.Layout()
		fgSizer6.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.Bind( wx.EVT_SIZE, self.OnSize )
		self.m_bpButton211.Bind( wx.EVT_BUTTON, self.OnPicAdd )
		self.m_textCtrl911.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_textCtrl1011.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_textCtrl1211.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_button34.Bind( wx.EVT_BUTTON, self.ReadOCR )
		self.m_textCtrl1621.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_button29.Bind( wx.EVT_BUTTON, self.IsEGNValid )
		self.m_textCtrl1721.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_textCtrl1811.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_choice211.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_bpButton311.Bind( wx.EVT_BUTTON, self.OnAddSity )
		self.m_bpButton311.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_choice311.Bind( wx.EVT_CHOICE, self.OnGroupConf )
		self.m_button1011.Bind( wx.EVT_BUTTON, self.AddGroup )
		self.m_bpButton312.Bind( wx.EVT_BUTTON, self.AddCart )
		self.m_bpButton13.Bind( wx.EVT_BUTTON, self.OnDelAll )
		self.m_bpButton81.Bind( wx.EVT_BUTTON, self.OnDelCart )
		self.m_radioBtn311.Bind( wx.EVT_RADIOBUTTON, self.OnPersonal )
		self.m_radioBtn311.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_radioBtn411.Bind( wx.EVT_RADIOBUTTON, self.OnPersonal )
		self.m_radioBtn411.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_checkBox13.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_checkBox111.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_checkBox211.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_checkBox311.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_textCtrl411.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_spinCtrl20.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_textCtrl511.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_checkBox56.Bind( wx.EVT_CHECKBOX, self.OnPointInMony )
		self.m_radioBtn9.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_radioBtn10.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_radioBtn211.Bind( wx.EVT_RADIOBUTTON, self.ShowOnLost )
		self.m_radioBtn211.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_radioBtn111.Bind( wx.EVT_RADIOBUTTON, self.HideOnLost )
		self.m_radioBtn111.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_radioBtn11.Bind( wx.EVT_RADIOBUTTON, self.OnDirectBonus )
		self.m_radioBtn11.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_checkBox48.Bind( wx.EVT_CHECKBOX, self.HideOptions )
		self.m_checkBox10.Bind( wx.EVT_CHECKBOX, self.MountChange )
		self.m_checkBox10.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_checkBox11.Bind( wx.EVT_CHECKBOX, self.DayChange )
		self.m_checkBox11.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_checkBox45.Bind( wx.EVT_CHECKBOX, self.MountChange )
		self.m_checkBox131.Bind( wx.EVT_CHECKBOX, self.OnShowWaithMony )
		self.m_checkBox131.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_spinCtrl14111.Bind( wx.EVT_SET_FOCUS, self.OnPass )
		self.m_checkBox22.Bind( wx.EVT_CHECKBOX, self.AllDayClick )
		self.m_checkBox23.Bind( wx.EVT_CHECKBOX, self.OneDayClick )
		self.m_checkBox24.Bind( wx.EVT_CHECKBOX, self.OneDayClick )
		self.m_checkBox25.Bind( wx.EVT_CHECKBOX, self.OneDayClick )
		self.m_checkBox26.Bind( wx.EVT_CHECKBOX, self.OneDayClick )
		self.m_checkBox27.Bind( wx.EVT_CHECKBOX, self.OneDayClick )
		self.m_checkBox28.Bind( wx.EVT_CHECKBOX, self.OneDayClick )
		self.m_checkBox29.Bind( wx.EVT_CHECKBOX, self.OneDayClick )
		self.m_listCtrl6.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnEditBonus )
		self.m_button37.Bind( wx.EVT_BUTTON, self.DelBonus )
		self.m_button36.Bind( wx.EVT_BUTTON, self.SetBonus )
		self.m_button811.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button911.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnSize( self, event ):
		event.Skip()

	def OnPicAdd( self, event ):
		event.Skip()

	def OnPass( self, event ):
		event.Skip()



	def ReadOCR( self, event ):
		event.Skip()


	def IsEGNValid( self, event ):
		event.Skip()




	def OnAddSity( self, event ):
		event.Skip()


	def OnGroupConf( self, event ):
		event.Skip()

	def AddGroup( self, event ):
		event.Skip()

	def AddCart( self, event ):
		event.Skip()

	def OnDelAll( self, event ):
		event.Skip()

	def OnDelCart( self, event ):
		event.Skip()

	def OnPersonal( self, event ):
		event.Skip()











	def OnPointInMony( self, event ):
		event.Skip()



	def ShowOnLost( self, event ):
		event.Skip()


	def HideOnLost( self, event ):
		event.Skip()


	def OnDirectBonus( self, event ):
		event.Skip()


	def HideOptions( self, event ):
		event.Skip()

	def MountChange( self, event ):
		event.Skip()


	def DayChange( self, event ):
		event.Skip()



	def OnShowWaithMony( self, event ):
		event.Skip()



	def AllDayClick( self, event ):
		event.Skip()

	def OneDayClick( self, event ):
		event.Skip()







	def OnEditBonus( self, event ):
		event.Skip()

	def DelBonus( self, event ):
		event.Skip()

	def SetBonus( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class AddSity
###########################################################################

class AddSity ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добави град", pos = wx.DefaultPosition, size = wx.Size( 355,162 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 314,131 ), wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"Град", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		bSizer8.Add( self.m_staticText40, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_textCtrl21, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer11 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_button9, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_button10, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		bSizer8.Add( gSizer11, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_textCtrl21.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_button9.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button10.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()




###########################################################################
## Class AllCart
###########################################################################

class AllCart ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добави Карта", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_listCtrl3 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,300 ), wx.LC_REPORT )
		bSizer9.Add( self.m_listCtrl3, 0, wx.ALL, 5 )

		gSizer12 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_bpButton4 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton4.SetBitmap( wx.Bitmap( u"img/22x22/list-add.png", wx.BITMAP_TYPE_ANY ) )
		gSizer12.Add( self.m_bpButton4, 0, wx.ALL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.m_button12, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		bSizer9.Add( gSizer12, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()
		bSizer9.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_listCtrl3.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnDel )
		self.m_bpButton4.Bind( wx.EVT_BUTTON, self.OnAdd )
		self.m_button11.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button12.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnDel( self, event ):
		event.Skip()

	def OnAdd( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class AllUserEditByGroup
###########################################################################

class AllUserEditByGroup ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Промяна на всички потребители", pos = wx.DefaultPosition, size = wx.Size( 617,104 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.Size( 617,102 ), wx.DefaultSize )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,-1 ), wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 )
		self.m_gauge1.SetMinSize( wx.Size( 600,-1 ) )

		bSizer12.Add( self.m_gauge1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button14 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button14, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button14.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()



###########################################################################
## Class AddGrup
###########################################################################

class AddGrup ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer20 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 900,500 ), wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Име на група", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText2.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_checkBox51 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Позволена за избор", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox51, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		fgSizer21.Add( bSizer1, 1, wx.EXPAND, 5 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"Processes" ), wx.HORIZONTAL )

		self.m_checkBox1 = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Мъни Бек", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Бонуси", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		self.m_checkBox3 = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Томбула", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_checkBox3, 0, wx.ALL, 5 )


		fgSizer21.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"Moneyback" ), wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Процент за отчисление", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText3.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		sbSizer5.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		sbSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_textCtrl4 = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, u"0,2", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_textCtrl4, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText77 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Минимално изплащане", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )

		self.m_staticText77.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText77.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		sbSizer5.Add( self.m_staticText77, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_spinCtrl21 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 5 )
		sbSizer5.Add( self.m_spinCtrl21, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText90 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Максимално изплащане", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText90.Wrap( -1 )

		self.m_staticText90.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText90.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		sbSizer5.Add( self.m_staticText90, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_spinCtrl43 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sbSizer5.Add( self.m_spinCtrl43, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer21.Add( sbSizer5, 1, wx.EXPAND, 5 )

		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"Draw" ), wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Коефицент", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText5.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		sbSizer7.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_radioBtn9 = wx.RadioButton( sbSizer7.GetStaticBox(), wx.ID_ANY, u"По Бет", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_radioBtn9, 0, wx.ALL, 5 )

		self.m_radioBtn10 = wx.RadioButton( sbSizer7.GetStaticBox(), wx.ID_ANY, u"По Тотал", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_radioBtn10, 0, wx.ALL, 5 )


		sbSizer7.Add( bSizer10, 1, wx.EXPAND, 5 )

		self.m_textCtrl5 = wx.TextCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer7.Add( self.m_textCtrl5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_checkBox55 = wx.CheckBox( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Точки в пари", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer7.Add( self.m_checkBox55, 0, wx.ALL, 5 )

		self.m_spinCtrl47 = wx.SpinCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 100, 1 )
		sbSizer7.Add( self.m_spinCtrl47, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer21.Add( sbSizer7, 1, wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 2, 2, 0, 0 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText71 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Бонуси", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		self.m_staticText71.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText71.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer2.Add( self.m_staticText71, 0, wx.ALL, 5 )

		self.m_staticText39 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"На сума", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		bSizer2.Add( self.m_staticText39, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_spinCtrl14 = wx.SpinCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 50000, 20 )
		bSizer2.Add( self.m_spinCtrl14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText78 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Забрани изход", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( -1 )

		bSizer2.Add( self.m_staticText78, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_checkBox42 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"По BET", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_checkBox42, 0, wx.ALL, 5 )

		self.m_spinCtrl22 = wx.SpinCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10000, 1 )
		bSizer2.Add( self.m_spinCtrl22, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox40 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Предупреди за бонус", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_checkBox40, 0, wx.ALL, 5 )

		self.m_spinCtrl39 = wx.SpinCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 2000, 100 )
		bSizer2.Add( self.m_spinCtrl39, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox49 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Процен от тотал", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox49.Enable( False )

		bSizer2.Add( self.m_checkBox49, 0, wx.ALL, 5 )

		self.m_spinCtrl44 = wx.SpinCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 100, 0 )
		self.m_spinCtrl44.Enable( False )

		bSizer2.Add( self.m_spinCtrl44, 0, wx.ALL|wx.EXPAND, 5 )

		m_choice8Choices = []
		self.m_choice8 = wx.Choice( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice8Choices, 0 )
		self.m_choice8.SetSelection( 0 )
		bSizer2.Add( self.m_choice8, 0, wx.ALL|wx.EXPAND, 5 )

		m_choice11Choices = []
		self.m_choice11 = wx.Choice( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice11Choices, 0 )
		self.m_choice11.SetSelection( 0 )
		bSizer2.Add( self.m_choice11, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer5.Add( bSizer2, 1, wx.EXPAND, 5 )

		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"Bonus" ), wx.VERTICAL )

		self.m_radioBtn2 = wx.RadioButton( sbSizer9.GetStaticBox(), wx.ID_ANY, u"По IN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn2.SetValue( True )
		sbSizer9.Add( self.m_radioBtn2, 0, wx.ALL, 5 )

		self.m_radioBtn1 = wx.RadioButton( sbSizer9.GetStaticBox(), wx.ID_ANY, u"По Бет", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

		self.m_radioBtn12 = wx.RadioButton( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Директен", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9.Add( self.m_radioBtn12, 0, wx.ALL, 5 )

		self.m_checkBox47 = wx.CheckBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Не усвояем", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9.Add( self.m_checkBox47, 0, wx.ALL, 5 )

		self.m_checkBox31 = wx.CheckBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Удържане", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9.Add( self.m_checkBox31, 0, wx.ALL, 5 )

		self.m_checkBox8 = wx.CheckBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Веднъж на ден", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox8.SetValue(True)
		sbSizer9.Add( self.m_checkBox8, 0, wx.ALL, 5 )

		self.m_checkBox9 = wx.CheckBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Предходен тотал", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9.Add( self.m_checkBox9, 0, wx.ALL, 5 )

		self.m_checkBox46 = wx.CheckBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Текущ месец", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9.Add( self.m_checkBox46, 0, wx.ALL, 5 )

		self.m_checkBox12 = wx.CheckBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Изчакай вход", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox12.SetValue(True)
		sbSizer9.Add( self.m_checkBox12, 0, wx.ALL, 5 )

		self.m_spinCtrl34 = wx.SpinCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sbSizer9.Add( self.m_spinCtrl34, 0, wx.ALL, 5 )

		self.m_checkBox53 = wx.CheckBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Много от редирект", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9.Add( self.m_checkBox53, 0, wx.ALL, 5 )


		gSizer5.Add( sbSizer9, 1, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox20 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Всички", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox20.SetValue(True)
		bSizer13.Add( self.m_checkBox20, 0, wx.ALL, 5 )

		self.m_checkBox18 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Понеделник", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_checkBox18, 0, wx.ALL, 5 )

		self.m_checkBox19 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Вторник", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_checkBox19, 0, wx.ALL, 5 )

		self.m_checkBox21 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Сряда", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_checkBox21, 0, wx.ALL, 5 )


		gSizer5.Add( bSizer13, 1, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox24 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Четвъртък", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_checkBox24, 0, wx.ALL, 5 )

		self.m_checkBox25 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Петък", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_checkBox25, 0, wx.ALL, 5 )

		self.m_checkBox26 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Събота", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_checkBox26, 0, wx.ALL, 5 )

		self.m_checkBox27 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Неделя", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_checkBox27, 0, wx.ALL, 5 )


		gSizer5.Add( bSizer15, 1, wx.EXPAND, 5 )


		fgSizer21.Add( gSizer5, 1, wx.EXPAND, 5 )

		gSizer11 = wx.GridSizer( 1, 1, 0, 0 )

		sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"Bonus" ), wx.VERTICAL )

		self.m_listCtrl5 = wx.ListCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_REPORT )
		sbSizer21.Add( self.m_listCtrl5, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox59 = wx.CheckBox( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Добави сандък x2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox59.Hide()

		bSizer24.Add( self.m_checkBox59, 0, wx.ALL, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button33 = wx.Button( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Премахни", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_button33, 0, wx.ALL, 5 )

		self.m_button32 = wx.Button( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Добави", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_button32, 0, wx.ALL, 5 )


		bSizer24.Add( bSizer22, 1, wx.EXPAND, 5 )


		sbSizer21.Add( bSizer24, 1, wx.EXPAND, 5 )


		gSizer11.Add( sbSizer21, 0, 0, 5 )


		fgSizer21.Add( gSizer11, 1, wx.EXPAND, 5 )


		self.m_scrolledWindow2.SetSizer( fgSizer21 )
		self.m_scrolledWindow2.Layout()
		fgSizer20.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )

		gSizer19 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer19.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer19.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		fgSizer20.Add( gSizer19, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer20 )
		self.Layout()
		fgSizer20.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_SIZE, self.OnSize )
		self.m_checkBox55.Bind( wx.EVT_CHECKBOX, self.OnPointInMony )
		self.m_checkBox49.Bind( wx.EVT_CHECKBOX, self.old_total_change )
		self.m_radioBtn2.Bind( wx.EVT_RADIOBUTTON, self.ShowOnLost )
		self.m_radioBtn1.Bind( wx.EVT_RADIOBUTTON, self.HideOnLost )
		self.m_radioBtn12.Bind( wx.EVT_RADIOBUTTON, self.OnOnDirectBonus )
		self.m_checkBox47.Bind( wx.EVT_CHECKBOX, self.HideOptions )
		self.m_checkBox9.Bind( wx.EVT_CHECKBOX, self.DayChange )
		self.m_checkBox46.Bind( wx.EVT_CHECKBOX, self.MountChange )
		self.m_checkBox12.Bind( wx.EVT_CHECKBOX, self.OnShowWaithMony )
		self.m_checkBox20.Bind( wx.EVT_CHECKBOX, self.AllDayClick )
		self.m_checkBox18.Bind( wx.EVT_CHECKBOX, self.OneDayClick )
		self.m_checkBox19.Bind( wx.EVT_CHECKBOX, self.OneDayClick )
		self.m_checkBox21.Bind( wx.EVT_CHECKBOX, self.OneDayClick )
		self.m_checkBox24.Bind( wx.EVT_CHECKBOX, self.OneDayClick )
		self.m_checkBox25.Bind( wx.EVT_CHECKBOX, self.OneDayClick )
		self.m_checkBox26.Bind( wx.EVT_CHECKBOX, self.OneDayClick )
		self.m_checkBox27.Bind( wx.EVT_CHECKBOX, self.OneDayClick )
		self.m_listCtrl5.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnEditBonus )
		self.m_button33.Bind( wx.EVT_BUTTON, self.DelBonus )
		self.m_button32.Bind( wx.EVT_BUTTON, self.SetBonus )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button5.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnSize( self, event ):
		event.Skip()

	def OnPointInMony( self, event ):
		event.Skip()

	def old_total_change( self, event ):
		event.Skip()

	def ShowOnLost( self, event ):
		event.Skip()

	def HideOnLost( self, event ):
		event.Skip()

	def OnOnDirectBonus( self, event ):
		event.Skip()

	def HideOptions( self, event ):
		event.Skip()

	def DayChange( self, event ):
		event.Skip()

	def MountChange( self, event ):
		event.Skip()

	def OnShowWaithMony( self, event ):
		event.Skip()

	def AllDayClick( self, event ):
		event.Skip()

	def OneDayClick( self, event ):
		event.Skip()







	def OnEditBonus( self, event ):
		event.Skip()

	def DelBonus( self, event ):
		event.Skip()

	def SetBonus( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class SetMonyOnUser
###########################################################################

class SetMonyOnUser ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добави Пари", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer21 = wx.FlexGridSizer( 4, 0, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer20 = wx.GridSizer( 2, 0, 0, 0 )

		self.m_staticText75 = wx.StaticText( self, wx.ID_ANY, u"Име", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText75.Wrap( -1 )

		self.m_staticText75.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText75.SetForegroundColour( wx.Colour( 0, 11, 250 ) )

		gSizer20.Add( self.m_staticText75, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_spinCtrl19 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 5000, 0 )
		gSizer20.Add( self.m_spinCtrl19, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer21.Add( gSizer20, 1, wx.EXPAND, 5 )

		gSizer21 = wx.GridSizer( 0, 4, 0, 0 )

		self.m_button15 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 100,150 ), 0 )
		gSizer21.Add( self.m_button15, 0, wx.ALL, 5 )

		self.m_button16 = wx.Button( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.Size( 100,150 ), 0 )
		gSizer21.Add( self.m_button16, 0, wx.ALL, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"100", wx.DefaultPosition, wx.Size( 100,150 ), 0 )
		gSizer21.Add( self.m_button17, 0, wx.ALL, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"<", wx.DefaultPosition, wx.Size( 100,150 ), 0 )
		gSizer21.Add( self.m_button22, 0, wx.ALL, 5 )


		fgSizer21.Add( gSizer21, 1, wx.EXPAND, 5 )

		gSizer22 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Отказ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.m_button20, 0, wx.ALL, 5 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.m_button21, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		fgSizer21.Add( gSizer22, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer21 )
		self.Layout()
		fgSizer21.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button15.Bind( wx.EVT_BUTTON, self.add_1 )
		self.m_button16.Bind( wx.EVT_BUTTON, self.add_10 )
		self.m_button17.Bind( wx.EVT_BUTTON, self.add_100 )
		self.m_button22.Bind( wx.EVT_BUTTON, self.del_last )
		self.m_button20.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button21.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def add_1( self, event ):
		event.Skip()

	def add_10( self, event ):
		event.Skip()

	def add_100( self, event ):
		event.Skip()

	def del_last( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class FreeTalon
###########################################################################

class FreeTalon ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Свободни талони", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer22 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"Брой талоини", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		bSizer17.Add( self.m_staticText81, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_spinCtrl25 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 100, 0 )
		bSizer17.Add( self.m_spinCtrl25, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText82 = wx.StaticText( self, wx.ID_ANY, u"Име", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )

		bSizer17.Add( self.m_staticText82, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,150 ), wx.TE_MULTILINE )
		bSizer17.Add( self.m_textCtrl13, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer22.Add( bSizer17, 1, wx.EXPAND, 5 )

		gSizer26 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer26.Add( self.m_button22, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"Печат", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer26.Add( self.m_button23, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		fgSizer22.Add( gSizer26, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer22 )
		self.Layout()
		fgSizer22.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button22.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button23.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class ReplaceGroupRow
###########################################################################

class ReplaceGroupRow ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Правила за смяна на група", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer23 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer23.SetFlexibleDirection( wx.BOTH )
		fgSizer23.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_listCtrl4 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,300 ), wx.LC_REPORT )
		fgSizer23.Add( self.m_listCtrl4, 0, wx.ALL, 5 )

		gSizer24 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_bpButton9 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton9.SetBitmap( wx.Bitmap( u"img/32x32/remove.png", wx.BITMAP_TYPE_ANY ) )
		gSizer24.Add( self.m_bpButton9, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_bpButton10 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton10.SetBitmap( wx.Bitmap( u"img/32x32/add.png", wx.BITMAP_TYPE_ANY ) )
		gSizer24.Add( self.m_bpButton10, 0, wx.ALL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		fgSizer23.Add( gSizer24, 1, wx.EXPAND, 5 )

		gSizer25 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer25.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_button22, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer23.Add( gSizer25, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer23 )
		self.Layout()
		fgSizer23.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_listCtrl4.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnEdit )
		self.m_bpButton9.Bind( wx.EVT_BUTTON, self.OnDel )
		self.m_bpButton10.Bind( wx.EVT_BUTTON, self.OnAdd )
		self.m_button22.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnEdit( self, event ):
		event.Skip()

	def OnDel( self, event ):
		event.Skip()

	def OnAdd( self, event ):
		event.Skip()



###########################################################################
## Class NewGroupReplaceRight
###########################################################################

class NewGroupReplaceRight ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ново Правило", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer24 = wx.FlexGridSizer( 5, 0, 0, 0 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText83 = wx.StaticText( self, wx.ID_ANY, u"Име на правило", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )

		fgSizer24.Add( self.m_staticText83, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl14.Enable( False )

		fgSizer24.Add( self.m_textCtrl14, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer25 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer25.SetFlexibleDirection( wx.BOTH )
		fgSizer25.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText84 = wx.StaticText( self, wx.ID_ANY, u"Група", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )

		fgSizer25.Add( self.m_staticText84, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice5Choices = []
		self.m_choice5 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,-1 ), m_choice5Choices, 0 )
		self.m_choice5.SetSelection( 0 )
		fgSizer25.Add( self.m_choice5, 0, wx.ALL, 5 )

		self.m_staticText85 = wx.StaticText( self, wx.ID_ANY, u"Да стане", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )

		fgSizer25.Add( self.m_staticText85, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice6Choices = []
		self.m_choice6 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,-1 ), m_choice6Choices, 0 )
		self.m_choice6.SetSelection( 0 )
		fgSizer25.Add( self.m_choice6, 0, wx.ALL, 5 )

		self.m_checkBox451 = wx.CheckBox( self, wx.ID_ANY, u"При тотал до", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.m_checkBox451, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl411 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 20000, 0 )
		fgSizer25.Add( self.m_spinCtrl411, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_checkBox57 = wx.CheckBox( self, wx.ID_ANY, u"Предходен тотал", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.m_checkBox57, 0, wx.ALL, 5 )


		fgSizer24.Add( fgSizer25, 1, wx.EXPAND, 5 )

		gSizer31 = wx.GridSizer( 4, 6, 0, 0 )

		self.m_checkBox41 = wx.CheckBox( self, wx.ID_ANY, u"Понеделник", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_checkBox41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl41 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 0 )
		self.m_spinCtrl41.Enable( False )

		gSizer31.Add( self.m_spinCtrl41, 0, wx.ALL, 5 )

		self.m_spinCtrl42 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 24, 0 )
		self.m_spinCtrl42.Enable( False )

		gSizer31.Add( self.m_spinCtrl42, 0, wx.ALL, 5 )

		self.m_checkBox42 = wx.CheckBox( self, wx.ID_ANY, u"Петък", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_checkBox42, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl43 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 0 )
		self.m_spinCtrl43.Enable( False )

		gSizer31.Add( self.m_spinCtrl43, 0, wx.ALL, 5 )

		self.m_spinCtrl44 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 24, 0 )
		self.m_spinCtrl44.Enable( False )

		gSizer31.Add( self.m_spinCtrl44, 0, wx.ALL, 5 )

		self.m_checkBox43 = wx.CheckBox( self, wx.ID_ANY, u"Вторник", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_checkBox43, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl45 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 0 )
		self.m_spinCtrl45.Enable( False )

		gSizer31.Add( self.m_spinCtrl45, 0, wx.ALL, 5 )

		self.m_spinCtrl46 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 24, 0 )
		self.m_spinCtrl46.Enable( False )

		gSizer31.Add( self.m_spinCtrl46, 0, wx.ALL, 5 )

		self.m_checkBox44 = wx.CheckBox( self, wx.ID_ANY, u"Събота", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_checkBox44, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl47 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 0 )
		self.m_spinCtrl47.Enable( False )

		gSizer31.Add( self.m_spinCtrl47, 0, wx.ALL, 5 )

		self.m_spinCtrl48 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 24, 0 )
		self.m_spinCtrl48.Enable( False )

		gSizer31.Add( self.m_spinCtrl48, 0, wx.ALL, 5 )

		self.m_checkBox45 = wx.CheckBox( self, wx.ID_ANY, u"Сряда", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_checkBox45, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl49 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 0 )
		self.m_spinCtrl49.Enable( False )

		gSizer31.Add( self.m_spinCtrl49, 0, wx.ALL, 5 )

		self.m_spinCtrl50 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 24, 0 )
		self.m_spinCtrl50.Enable( False )

		gSizer31.Add( self.m_spinCtrl50, 0, wx.ALL, 5 )

		self.m_checkBox46 = wx.CheckBox( self, wx.ID_ANY, u"Неделя", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_checkBox46, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl51 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 0 )
		self.m_spinCtrl51.Enable( False )

		gSizer31.Add( self.m_spinCtrl51, 0, wx.ALL, 5 )

		self.m_spinCtrl52 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 24, 0 )
		self.m_spinCtrl52.Enable( False )

		gSizer31.Add( self.m_spinCtrl52, 0, wx.ALL, 5 )

		self.m_checkBox47 = wx.CheckBox( self, wx.ID_ANY, u"Четвъртък", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_checkBox47, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl53 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 0 )
		self.m_spinCtrl53.Enable( False )

		gSizer31.Add( self.m_spinCtrl53, 0, wx.ALL, 5 )

		self.m_spinCtrl54 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 24, 0 )
		self.m_spinCtrl54.Enable( False )

		gSizer31.Add( self.m_spinCtrl54, 0, wx.ALL, 5 )

		self.m_checkBox49 = wx.CheckBox( self, wx.ID_ANY, u"Винаги", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox49.SetValue(True)
		gSizer31.Add( self.m_checkBox49, 0, wx.ALL, 5 )


		fgSizer24.Add( gSizer31, 1, wx.EXPAND, 5 )

		gSizer30 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer30.Add( self.m_button24, 0, wx.ALL, 5 )

		self.m_button25 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer30.Add( self.m_button25, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		fgSizer24.Add( gSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer24 )
		self.Layout()
		fgSizer24.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_checkBox451.Bind( wx.EVT_CHECKBOX, self.OnEnable )
		self.m_checkBox41.Bind( wx.EVT_CHECKBOX, self.OnClick )
		self.m_checkBox42.Bind( wx.EVT_CHECKBOX, self.OnClick )
		self.m_checkBox43.Bind( wx.EVT_CHECKBOX, self.OnClick )
		self.m_checkBox44.Bind( wx.EVT_CHECKBOX, self.OnClick )
		self.m_checkBox45.Bind( wx.EVT_CHECKBOX, self.OnClick )
		self.m_checkBox46.Bind( wx.EVT_CHECKBOX, self.OnClick )
		self.m_checkBox47.Bind( wx.EVT_CHECKBOX, self.OnClick )
		self.m_checkBox49.Bind( wx.EVT_CHECKBOX, self.OnClick )
		self.m_button24.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button25.Bind( wx.EVT_BUTTON, self.OnSave )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnEnable( self, event ):
		event.Skip()

	def OnClick( self, event ):
		event.Skip()









	def OnSave( self, event ):
		event.Skip()


###########################################################################
## Class Reserve
###########################################################################

class Reserve ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Резервация", pos = wx.DefaultPosition, size = wx.Size( 414,335 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText85 = wx.StaticText( self, wx.ID_ANY, u"Клиент: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )

		bSizer18.Add( self.m_staticText85, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText89 = wx.StaticText( self, wx.ID_ANY, u"Машина", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText89.Wrap( -1 )

		bSizer18.Add( self.m_staticText89, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_choice6Choices = []
		self.m_choice6 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice6Choices, 0 )
		self.m_choice6.SetSelection( 0 )
		bSizer18.Add( self.m_choice6, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText86 = wx.StaticText( self, wx.ID_ANY, u"Дата (31.12.2020)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )

		bSizer18.Add( self.m_staticText86, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_textCtrl15, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText87 = wx.StaticText( self, wx.ID_ANY, u"Час (11:45)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText87.Wrap( -1 )

		bSizer18.Add( self.m_staticText87, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_textCtrl16, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer28 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button25 = wx.Button( self, wx.ID_ANY, u"Отказ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer28.Add( self.m_button25, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button26 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer28.Add( self.m_button26, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		bSizer18.Add( gSizer28, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer18 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button25.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button26.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class SetCartPrice
###########################################################################

class SetCartPrice ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Цена на карта", pos = wx.DefaultPosition, size = wx.Size( 300,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.Size( 300,-1 ), wx.DefaultSize )

		gSizer29 = wx.GridSizer( 1, 1, 0, 0 )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"Брой карти", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		bSizer19.Add( self.m_staticText91, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_spinCtrl46 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		bSizer19.Add( self.m_spinCtrl46, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText92 = wx.StaticText( self, wx.ID_ANY, u"Група", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText92.Wrap( -1 )

		bSizer19.Add( self.m_staticText92, 0, wx.ALL|wx.EXPAND, 5 )

		m_choice7Choices = []
		self.m_choice7 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice7Choices, 0 )
		self.m_choice7.SetSelection( 0 )
		bSizer19.Add( self.m_choice7, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText93 = wx.StaticText( self, wx.ID_ANY, u"Цена", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText93.Wrap( -1 )

		bSizer19.Add( self.m_staticText93, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_textCtrl18, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button27 = wx.Button( self, wx.ID_ANY, u"Отказ", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_button27, 1, wx.ALL, 5 )

		self.m_button28 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_button28, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer19.Add( bSizer20, 1, wx.EXPAND, 5 )


		gSizer29.Add( bSizer19, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer29 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button27.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button28.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class SelectDate
###########################################################################

class SelectDate ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Избери Дата", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer28 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer28.SetFlexibleDirection( wx.BOTH )
		fgSizer28.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer35 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_calendar3 = wx.adv.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS )
		gSizer35.Add( self.m_calendar3, 0, wx.ALL, 5 )


		fgSizer28.Add( gSizer35, 1, wx.EXPAND, 5 )

		gSizer36 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button41 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer36.Add( self.m_button41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_button42 = wx.Button( self, wx.ID_ANY, u"Изтрий", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer36.Add( self.m_button42, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		fgSizer28.Add( gSizer36, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer28 )
		self.Layout()
		fgSizer28.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button41.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button42.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


