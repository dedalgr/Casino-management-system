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
## Class Main
###########################################################################

class Main ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer1 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_toolBar1 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL|wx.TB_TEXT )
		self.m_toolBar1.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_tool2 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Нова задача", wx.Bitmap( u"img/64x64/preferences-system-time.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool3 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Стоп Аларма", wx.Bitmap( u"img/64x64/Gnome-Audio-Volume-Muted-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool41 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Старт Аларма", wx.Bitmap( u"img/64x64/Gnome-Audio-Volume-High-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool5 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Ремонт", wx.Bitmap( u"img/64x64/cpu.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool6 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Диагностика", wx.Bitmap( u"img/64x64/Gnome-Preferences-Other-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool4 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Затвори", wx.Bitmap( u"img/64x64/dialog-error.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar1.Realize()

		fgSizer1.Add( self.m_toolBar1, 0, 0, 5 )

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
		self.Bind( wx.EVT_TOOL, self.NewTask, id = self.m_tool2.GetId() )
		self.Bind( wx.EVT_TOOL, self.AlarmStop, id = self.m_tool3.GetId() )
		self.Bind( wx.EVT_TOOL, self.AlarmStart, id = self.m_tool41.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnFix, id = self.m_tool5.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnMonitoring, id = self.m_tool6.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnClose, id = self.m_tool4.GetId() )
		self.m_listCtrl1.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnShowInfo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def NewTask( self, event ):
		event.Skip()

	def AlarmStop( self, event ):
		event.Skip()

	def AlarmStart( self, event ):
		event.Skip()

	def OnFix( self, event ):
		event.Skip()

	def OnMonitoring( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()

	def OnShowInfo( self, event ):
		event.Skip()


###########################################################################
## Class NewTask
###########################################################################

class NewTask ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"За ремонт", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer2 = wx.FlexGridSizer( 5, 0, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Машина", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		fgSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		m_choice1Choices = []
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		fgSizer2.Add( self.m_choice1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_richText1 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,300 ), wx.TE_PROCESS_ENTER|wx.VSCROLL|wx.HSCROLL|wx.WANTS_CHARS|wx.BORDER_NONE )
		self.m_richText1.SetMinSize( wx.Size( 480,350 ) )

		fgSizer2.Add( self.m_richText1, 1, wx.EXPAND |wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		fgSizer2.Add( gSizer3, 0, wx.EXPAND|wx.ALIGN_BOTTOM, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()
		fgSizer2.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_choice1.Bind( wx.EVT_CHOICE, self.OnDeviceSelect )
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnSave )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnDeviceSelect( self, event ):
		event.Skip()


	def OnSave( self, event ):
		event.Skip()


###########################################################################
## Class Fix
###########################################################################

class Fix ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ремонт", pos = wx.DefaultPosition, size = wx.Size( 520,550 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer3 = wx.FlexGridSizer( 6, 0, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer4 = wx.GridSizer( 0, 3, 0, 0 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_radioBtn1 = wx.RadioButton( self, wx.ID_ANY, u"Без Нулиране", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

		self.m_radioBtn2 = wx.RadioButton( self, wx.ID_ANY, u"Нулиране", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_radioBtn2, 0, wx.ALL, 5 )


		gSizer4.Add( bSizer1, 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox3 = wx.CheckBox( self, wx.ID_ANY, u"Без Отчет", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox3.SetValue(True)
		bSizer2.Add( self.m_checkBox3, 0, wx.ALL, 5 )

		self.m_checkBox4 = wx.CheckBox( self, wx.ID_ANY, u"Трансфер на пари", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox4.SetValue(True)
		bSizer2.Add( self.m_checkBox4, 0, wx.ALL, 5 )


		gSizer4.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Отчети Ръчно", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"Извади Бил", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_checkBox2, 0, wx.ALL, 5 )


		gSizer4.Add( bSizer3, 1, wx.EXPAND, 5 )


		fgSizer3.Add( gSizer4, 1, wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Сума на ремонт", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		fgSizer3.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Описание", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer3.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.m_richText2 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,250 ), 0|wx.VSCROLL|wx.HSCROLL|wx.WANTS_CHARS|wx.BORDER_NONE )
		self.m_richText2.SetMinSize( wx.Size( 500,300 ) )

		fgSizer3.Add( self.m_richText2, 0, wx.ALL, 5 )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Поправи", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		fgSizer3.Add( gSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnCloce )
		self.m_radioBtn1.Bind( wx.EVT_RADIOBUTTON, self.OnHide )
		self.m_radioBtn2.Bind( wx.EVT_RADIOBUTTON, self.OnShow )
		self.m_checkBox3.Bind( wx.EVT_CHECKBOX, self.OnDeselect )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.OnDeselect3 )
		self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.OnDeselect3 )
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnSave )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnCloce( self, event ):
		event.Skip()

	def OnHide( self, event ):
		event.Skip()

	def OnShow( self, event ):
		event.Skip()

	def OnDeselect( self, event ):
		event.Skip()

	def OnDeselect3( self, event ):
		event.Skip()


	def OnClose( self, event ):
		event.Skip()

	def OnSave( self, event ):
		event.Skip()


###########################################################################
## Class RunCommand
###########################################################################

class RunCommand ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"RunUnixComand", pos = wx.DefaultPosition, size = wx.Size( 428,378 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer23 = wx.GridSizer( 8, 0, 0, 0 )

		self.m_staticText76 = wx.StaticText( self, wx.ID_ANY, u"Парола", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText76.Wrap( -1 )

		gSizer23.Add( self.m_staticText76, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer23.Add( self.m_textCtrl20, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText77 = wx.StaticText( self, wx.ID_ANY, u"Машина", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )

		gSizer23.Add( self.m_staticText77, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice17Choices = []
		self.m_choice17 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice17Choices, 0 )
		self.m_choice17.SetSelection( 0 )
		gSizer23.Add( self.m_choice17, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText78 = wx.StaticText( self, wx.ID_ANY, u"Команда", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( -1 )

		gSizer23.Add( self.m_staticText78, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_checkBox8 = wx.CheckBox( self, wx.ID_ANY, u"Покажи резултат", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer23.Add( self.m_checkBox8, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer23.Add( self.m_textCtrl21, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer23.Add( self.m_button51, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( gSizer23 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_textCtrl20.Bind( wx.EVT_TEXT_ENTER, self.OnSend )
		self.m_textCtrl21.Bind( wx.EVT_TEXT_ENTER, self.OnSend )
		self.m_button51.Bind( wx.EVT_BUTTON, self.OnSend )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnSend( self, event ):
		event.Skip()




###########################################################################
## Class MSG
###########################################################################

class MSG ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Response", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer48 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer48.SetFlexibleDirection( wx.BOTH )
		fgSizer48.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_richText2 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.WANTS_CHARS|wx.BORDER_NONE )
		self.m_richText2.SetMinSize( wx.Size( 500,400 ) )

		fgSizer48.Add( self.m_richText2, 1, wx.EXPAND |wx.ALL, 5 )

		gSizer24 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer24.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button53 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer24.Add( self.m_button53, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		fgSizer48.Add( gSizer24, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer48 )
		self.Layout()
		fgSizer48.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button53.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()



###########################################################################
## Class Guage
###########################################################################

class Guage ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 )
		bSizer15.Add( self.m_gauge1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_button23, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer15 )
		self.Layout()
		bSizer15.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button23.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()



###########################################################################
## Class Update
###########################################################################

class Update ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer22 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"SMIB" ), wx.VERTICAL )

		self.m_filePicker2 = wx.FilePickerCtrl( sbSizer14.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_filePicker2.Hide()

		sbSizer14.Add( self.m_filePicker2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button421 = wx.Button( sbSizer14.GetStaticBox(), wx.ID_ANY, u"Unix Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button421.Hide()

		sbSizer14.Add( self.m_button421, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button29 = wx.Button( sbSizer14.GetStaticBox(), wx.ID_ANY, u"Auto Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer14.Add( self.m_button29, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer22.Add( sbSizer14, 1, wx.EXPAND, 5 )

		sbSizer16 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"CMS" ), wx.VERTICAL )

		self.m_checkBox43 = wx.CheckBox( sbSizer16.GetStaticBox(), wx.ID_ANY, u"Добави минимална ревизия", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer16.Add( self.m_checkBox43, 0, wx.ALL, 5 )

		self.m_button31 = wx.Button( sbSizer16.GetStaticBox(), wx.ID_ANY, u"Auto Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer16.Add( self.m_button31, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer22.Add( sbSizer16, 0, wx.EXPAND, 5 )

		sbSizer25 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"RedirectServer" ), wx.VERTICAL )

		self.m_button41 = wx.Button( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Auto Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer25.Add( self.m_button41, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer22.Add( sbSizer25, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer22 )
		self.Layout()
		fgSizer22.Fit( self )

		# Connect Events
		self.m_button421.Bind( wx.EVT_BUTTON, self.SMIBUnixUpdate )
		self.m_button29.Bind( wx.EVT_BUTTON, self.SMIBAutoUpdate )
		self.m_button31.Bind( wx.EVT_BUTTON, self.OnMainAutoUpdate )
		self.m_button41.Bind( wx.EVT_BUTTON, self.OnRedirectUpdate )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def SMIBUnixUpdate( self, event ):
		event.Skip()

	def SMIBAutoUpdate( self, event ):
		event.Skip()

	def OnMainAutoUpdate( self, event ):
		event.Skip()

	def OnRedirectUpdate( self, event ):
		event.Skip()


