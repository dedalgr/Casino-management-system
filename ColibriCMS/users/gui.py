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
## Class AddUser
###########################################################################

class AddUser ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добави потребител!", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		gSizer121 = wx.GridSizer( 2, 0, 0, 0 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Име", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer121.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer121.Add( self.m_textCtrl10, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( gSizer121, 1, wx.EXPAND, 5 )

		gSizer7 = wx.GridSizer( 2, 2, 0, 0 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Парола", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer7.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Повтори парола", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer7.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer7.Add( self.m_textCtrl7, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer7.Add( self.m_textCtrl8, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( gSizer7, 1, wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 3, 0, 0 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_radioBtn2 = wx.RadioButton( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Активен", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn2.SetValue( True )
		self.m_radioBtn2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		sbSizer2.Add( self.m_radioBtn2, 0, wx.ALL, 5 )

		self.m_radioBtn3 = wx.RadioButton( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Неактивен", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_radioBtn3, 0, wx.ALL, 5 )


		gSizer9.Add( sbSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		gSizer10 = wx.GridSizer( 2, 0, 0, 0 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Избери Група", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer10.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		gSizer10.Add( self.m_choice3, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer9.Add( gSizer10, 1, wx.EXPAND, 5 )

		gSizer11 = wx.GridSizer( 2, 0, 0, 0 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText12.SetForegroundColour( wx.Colour( 30, 71, 25 ) )
		self.m_staticText12.Hide()

		gSizer11.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Добави Карта", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_button7, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer9.Add( gSizer11, 1, wx.EXPAND, 5 )


		bSizer3.Add( gSizer9, 1, wx.EXPAND, 5 )

		gSizer12 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		bSizer3.Add( gSizer12, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()
		bSizer3.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnAddCart )
		self.m_button5.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnSave )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnAddCart( self, event ):
		event.Skip()


	def OnSave( self, event ):
		event.Skip()


###########################################################################
## Class AddCart
###########################################################################

class AddCart ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добавяне на карта", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 540,112 ), wx.DefaultSize )

		gSizer14 = wx.GridSizer( 2, 0, 0, 0 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Моля поставете карта в четеца!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText13.SetForegroundColour( wx.Colour( 197, 33, 33 ) )
		self.m_staticText13.SetMinSize( wx.Size( 540,-1 ) )

		gSizer14.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Премахни", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		gSizer14.Add( gSizer10, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer14 )
		self.Layout()
		gSizer14.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnDelCart )
		self.m_button8.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnDelCart( self, event ):
		event.Skip()



###########################################################################
## Class LogedInUser
###########################################################################

class LogedInUser ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Влезли Постребители", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer7 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_listCtrl3 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl3.SetMinSize( wx.Size( 400,200 ) )

		fgSizer7.Add( self.m_listCtrl3, 0, wx.ALL, 5 )

		gSizer11 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_button9, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		fgSizer7.Add( gSizer11, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer7 )
		self.Layout()
		fgSizer7.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_listCtrl3.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnOut )
		self.m_button9.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnOut( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()


###########################################################################
## Class UserPanel
###########################################################################

class UserPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer7 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_toolBar5 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL|wx.TB_TEXT )
		self.m_toolBar5.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_tool2 = self.m_toolBar5.AddTool( wx.ID_ANY, u"Добави група", wx.Bitmap( u"img/64x64/kopete.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool3 = self.m_toolBar5.AddTool( wx.ID_ANY, u"Добави потребител", wx.Bitmap( u"img/64x64/Gnome-Stock-Person-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool4 = self.m_toolBar5.AddTool( wx.ID_ANY, u"Активни", wx.Bitmap( u"img/64x64/User-Info-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool5 = self.m_toolBar5.AddTool( wx.ID_ANY, u"Удържане на липса", wx.Bitmap( u"img/64x64/kontact.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool1 = self.m_toolBar5.AddTool( wx.ID_ANY, u"Затвори", wx.Bitmap( u"img/64x64/dialog-error.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar5.Realize()

		fgSizer7.Add( self.m_toolBar5, 0, wx.EXPAND, 5 )

		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl1.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer12.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_listCtrl2 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl2.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer12.Add( self.m_listCtrl2, 1, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5 )


		fgSizer7.Add( fgSizer12, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer7 )
		self.Layout()

		# Connect Events
		self.Bind( wx.EVT_TOOL, self.OnClose, id = self.m_tool1.GetId() )
		self.m_listCtrl1.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnShowUserInGrup )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnShowUserInGrup( self, event ):
		event.Skip()


###########################################################################
## Class AddGrup
###########################################################################

class AddGrup ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добави група", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer4 = wx.FlexGridSizer( 4, 0, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Име на група", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer4.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer5 = wx.FlexGridSizer( 4, 0, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"Изключи бил", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		self.m_checkBox3 = wx.CheckBox( self, wx.ID_ANY, u"Извади целия билл", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_checkBox3, 0, wx.ALL, 5 )

		self.m_checkBox5 = wx.CheckBox( self, wx.ID_ANY, u"Авто E-mail", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_checkBox5, 0, wx.ALL, 5 )

		self.m_checkBox71 = wx.CheckBox( self, wx.ID_ANY, u"По подразбиране", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_checkBox71, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_checkBox51 = wx.CheckBox( self, wx.ID_ANY, u"РКО E-mail", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_checkBox51, 0, wx.ALL, 5 )


		fgSizer5.Add( bSizer4, 1, wx.EXPAND, 5 )

		gSizer14 = wx.GridSizer( 2, 3, 0, 0 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"E-MAIL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		gSizer14.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"E-MAIL SERVICE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		gSizer14.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Subject", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gSizer14.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.m_textCtrl9, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.m_textCtrl10, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.m_textCtrl8, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer5.Add( gSizer14, 1, wx.EXPAND, 5 )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Всички права", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer10.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Права на групата", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer10.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		fgSizer5.Add( gSizer10, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer30 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer30.SetFlexibleDirection( wx.BOTH )
		fgSizer30.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_treeCtrl1 = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,200 ), wx.TR_DEFAULT_STYLE|wx.TR_HAS_BUTTONS|wx.TR_HIDE_ROOT|wx.TR_ROW_LINES|wx.TR_SINGLE )
		fgSizer30.Add( self.m_treeCtrl1, 0, wx.ALL, 5 )

		gSizer12 = wx.GridSizer( 2, 1, 0, 0 )

		self.m_bpButton2 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton2.SetBitmap( wx.Bitmap( u"img/32x32/Gnome-Go-Next-32.png", wx.BITMAP_TYPE_ANY ) )
		gSizer12.Add( self.m_bpButton2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_bpButton3 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton3.SetBitmap( wx.Bitmap( u"img/32x32/Gnome-Go-Previous-32.png", wx.BITMAP_TYPE_ANY ) )
		gSizer12.Add( self.m_bpButton3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		fgSizer30.Add( gSizer12, 1, wx.EXPAND, 5 )

		self.m_treeCtrl2 = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,200 ), wx.TR_DEFAULT_STYLE|wx.TR_HAS_BUTTONS|wx.TR_HIDE_ROOT|wx.TR_ROW_LINES|wx.TR_SINGLE )
		fgSizer30.Add( self.m_treeCtrl2, 0, wx.ALL, 5 )


		fgSizer5.Add( fgSizer30, 1, wx.EXPAND, 5 )


		fgSizer4.Add( fgSizer5, 1, wx.EXPAND, 5 )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer4.Add( gSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer4 )
		self.Layout()
		fgSizer4.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_bpButton2.Bind( wx.EVT_BUTTON, self.OnAddRight )
		self.m_bpButton3.Bind( wx.EVT_BUTTON, self.OnDelRight )
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnSave )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnAddRight( self, event ):
		event.Skip()

	def OnDelRight( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()

	def OnSave( self, event ):
		event.Skip()


###########################################################################
## Class HoldMony
###########################################################################

class HoldMony ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Удържане на липса", pos = wx.DefaultPosition, size = wx.Size( 393,220 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Сума за удържане на липса", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText10.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		self.m_staticText10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Потребител:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer2.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Общо задължение: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer2.Add( self.m_staticText12, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 20000, 0 )
		bSizer1.Add( self.m_spinCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer13 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer13.Add( self.m_button9, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer13.Add( self.m_button10, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		bSizer1.Add( gSizer13, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button9.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button10.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


