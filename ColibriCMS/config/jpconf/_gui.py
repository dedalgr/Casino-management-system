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
import wx.adv

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Server Config", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer17 = wx.GridSizer( 0, 5, 0, 0 )

		fgSizer14 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bpButton6 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton6.SetBitmap( wx.Bitmap( u"img/64x64/Gnome-Preferences-Desktop-Remote-Desktop-64.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer14.Add( self.m_bpButton6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, u"Машини", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText53.Wrap( -1 )

		self.m_staticText53.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText53.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer14.Add( self.m_staticText53, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		gSizer17.Add( fgSizer14, 1, wx.EXPAND, 5 )

		fgSizer15 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bpButton7 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton7.SetBitmap( wx.Bitmap( u"img/64x64/Gnome-Preferences-Desktop-Wallpaper-64.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer15.Add( self.m_bpButton7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText54 = wx.StaticText( self, wx.ID_ANY, u"Дисплеи", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )

		self.m_staticText54.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText54.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer15.Add( self.m_staticText54, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		gSizer17.Add( fgSizer15, 1, wx.EXPAND, 5 )

		fgSizer16 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bpButton8 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton8.SetBitmap( wx.Bitmap( u"img/64x64/Gnome-Preferences-System-Network-64.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer16.Add( self.m_bpButton8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"Групи", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		self.m_staticText55.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText55.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer16.Add( self.m_staticText55, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		gSizer17.Add( fgSizer16, 1, wx.EXPAND, 5 )

		fgSizer17 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bpButton9 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton9.SetBitmap( wx.Bitmap( u"img/64x64/Emblem-Money-64.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer17.Add( self.m_bpButton9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText56 = wx.StaticText( self, wx.ID_ANY, u"Събития", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )

		self.m_staticText56.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText56.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer17.Add( self.m_staticText56, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		gSizer17.Add( fgSizer17, 1, wx.EXPAND, 5 )

		fgSizer18 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bpButton10 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton10.SetBitmap( wx.Bitmap( u"img/64x64/Gnome-Applications-System-64.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer18.Add( self.m_bpButton10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText57 = wx.StaticText( self, wx.ID_ANY, u"Сървър", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )

		self.m_staticText57.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText57.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer18.Add( self.m_staticText57, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		gSizer17.Add( fgSizer18, 1, wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bpButton5 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton5.SetBitmap( wx.Bitmap( u"img/64x64/Gnome-System-Users-64.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton5.SetToolTip( u"Добавяне и премахване на потребители" )

		fgSizer2.Add( self.m_bpButton5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Потребители", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText10.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer2.Add( self.m_staticText10, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		gSizer17.Add( fgSizer2, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer27 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer27.SetFlexibleDirection( wx.BOTH )
		fgSizer27.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bpButton111 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton111.SetBitmap( wx.Bitmap( u"img/64x64/Gnome-Insert-Object-64.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer27.Add( self.m_bpButton111, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"Опресни", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		self.m_staticText42.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText42.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer27.Add( self.m_staticText42, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		gSizer17.Add( fgSizer27, 1, wx.EXPAND, 5 )

		fgSizer29 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer29.SetFlexibleDirection( wx.BOTH )
		fgSizer29.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bpButton12 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton12.SetBitmap( wx.Bitmap( u"img/64x64/Gnome-Media-Floppy-64.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer29.Add( self.m_bpButton12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		self.m_staticText43.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText43.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer29.Add( self.m_staticText43, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		gSizer17.Add( fgSizer29, 1, wx.EXPAND, 5 )

		fgSizer39 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer39.SetFlexibleDirection( wx.BOTH )
		fgSizer39.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bpButton41 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton41.SetBitmap( wx.Bitmap( u"img/64x64/security-low.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton41.SetToolTip( u"Затваряне на програмата" )

		fgSizer39.Add( self.m_bpButton41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText131 = wx.StaticText( self, wx.ID_ANY, u"Задръж", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )

		self.m_staticText131.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText131.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer39.Add( self.m_staticText131, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		gSizer17.Add( fgSizer39, 1, wx.EXPAND, 5 )

		fgSizer40 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer40.SetFlexibleDirection( wx.BOTH )
		fgSizer40.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bpButton42 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton42.SetBitmap( wx.Bitmap( u"img/64x64/security-high.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton42.SetToolTip( u"Затваряне на програмата" )

		fgSizer40.Add( self.m_bpButton42, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText132 = wx.StaticText( self, wx.ID_ANY, u"Пусни", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText132.Wrap( -1 )

		self.m_staticText132.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText132.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer40.Add( self.m_staticText132, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		gSizer17.Add( fgSizer40, 1, wx.EXPAND, 5 )

		fgSizer38 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer38.SetFlexibleDirection( wx.BOTH )
		fgSizer38.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bpButton16 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton16.SetBitmap( wx.Bitmap( u"img/64x64/media-optical-recordable.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer38.Add( self.m_bpButton16, 0, wx.ALL, 5 )

		self.m_staticText63 = wx.StaticText( self, wx.ID_ANY, u"Архивирай", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )

		self.m_staticText63.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText63.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer38.Add( self.m_staticText63, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer17.Add( fgSizer38, 1, wx.EXPAND, 5 )

		fgSizer391 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer391.SetFlexibleDirection( wx.BOTH )
		fgSizer391.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bpButton17 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton17.SetBitmap( wx.Bitmap( u"img/64x64/media-optical.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer391.Add( self.m_bpButton17, 0, wx.ALL, 5 )

		self.m_staticText65 = wx.StaticText( self, wx.ID_ANY, u"Зареди", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )

		self.m_staticText65.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText65.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer391.Add( self.m_staticText65, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer17.Add( fgSizer391, 1, wx.EXPAND, 5 )

		fgSizer19 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer19.SetFlexibleDirection( wx.BOTH )
		fgSizer19.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bpButton11 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton11.SetBitmap( wx.Bitmap( u"img/64x64/Gnome-Help-Browser-64.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer19.Add( self.m_bpButton11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText58 = wx.StaticText( self, wx.ID_ANY, u"Помощ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )

		self.m_staticText58.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText58.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer19.Add( self.m_staticText58, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		gSizer17.Add( fgSizer19, 1, wx.EXPAND, 5 )

		fgSizer5 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bpButton4 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton4.SetBitmap( wx.Bitmap( u"img/64x64/Gnome-Application-Exit-64.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton4.SetToolTip( u"Затваряне на програмата" )

		fgSizer5.Add( self.m_bpButton4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText13.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer5.Add( self.m_staticText13, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		gSizer17.Add( fgSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer17 )
		self.Layout()
		gSizer17.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_bpButton6.Bind( wx.EVT_BUTTON, self.OnSMIB )
		self.m_bpButton7.Bind( wx.EVT_BUTTON, self.OnVisual )
		self.m_bpButton8.Bind( wx.EVT_BUTTON, self.OnGroup )
		self.m_bpButton9.Bind( wx.EVT_BUTTON, self.OnLog )
		self.m_bpButton10.Bind( wx.EVT_BUTTON, self.OnServer )
		self.m_bpButton5.Bind( wx.EVT_BUTTON, self.OnUser )
		self.m_bpButton111.Bind( wx.EVT_BUTTON, self.OnGetDB )
		self.m_bpButton12.Bind( wx.EVT_BUTTON, self.OnSetDB )
		self.m_bpButton41.Bind( wx.EVT_BUTTON, self.OnStop )
		self.m_bpButton42.Bind( wx.EVT_BUTTON, self.OnStart )
		self.m_bpButton16.Bind( wx.EVT_BUTTON, self.OnSave )
		self.m_bpButton17.Bind( wx.EVT_BUTTON, self.OnLoad )
		self.m_bpButton11.Bind( wx.EVT_BUTTON, self.OnHelp )
		self.m_bpButton4.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnSMIB( self, event ):
		event.Skip()

	def OnVisual( self, event ):
		event.Skip()

	def OnGroup( self, event ):
		event.Skip()

	def OnLog( self, event ):
		event.Skip()

	def OnServer( self, event ):
		event.Skip()

	def OnUser( self, event ):
		event.Skip()

	def OnGetDB( self, event ):
		event.Skip()

	def OnSetDB( self, event ):
		event.Skip()

	def OnStop( self, event ):
		event.Skip()

	def OnStart( self, event ):
		event.Skip()

	def OnSave( self, event ):
		event.Skip()

	def OnLoad( self, event ):
		event.Skip()

	def OnHelp( self, event ):
		event.Skip()



###########################################################################
## Class AllDial
###########################################################################

class AllDial ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer12 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_treeCtrl2 = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_HAS_BUTTONS|wx.TR_HAS_VARIABLE_ROW_HEIGHT|wx.TR_HIDE_ROOT|wx.TR_TWIST_BUTTONS )
		self.m_treeCtrl2.SetMinSize( wx.Size( 300,400 ) )

		fgSizer12.Add( self.m_treeCtrl2, 0, wx.ALL, 5 )

		fgSizer10 = wx.FlexGridSizer( 0, 0, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_richText2 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.WANTS_CHARS|wx.BORDER_NONE )
		self.m_richText2.Hide()
		self.m_richText2.SetMinSize( wx.Size( 300,400 ) )

		fgSizer10.Add( self.m_richText2, 1, wx.EXPAND |wx.ALL, 5 )


		fgSizer12.Add( fgSizer10, 1, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_show = wx.Button( self, wx.ID_ANY, u"Покажи", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		self.m_button_show.Hide()

		bSizer12.Add( self.m_button_show, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button_add = wx.Button( self, wx.ID_ANY, u"Добави", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		self.m_button_add.Hide()

		bSizer12.Add( self.m_button_add, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_button_edit = wx.Button( self, wx.ID_ANY, u"Редакция", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		self.m_button_edit.Hide()

		bSizer12.Add( self.m_button_edit, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button_del = wx.Button( self, wx.ID_ANY, u"Изтрий", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		self.m_button_del.Hide()

		bSizer12.Add( self.m_button_del, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_button_help = wx.Button( self, wx.ID_ANY, u"Помощ", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		self.m_button_help.Hide()

		bSizer12.Add( self.m_button_help, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_button_close = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		self.m_button_close.Hide()

		bSizer12.Add( self.m_button_close, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_button_free_1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		self.m_button_free_1.Hide()

		bSizer12.Add( self.m_button_free_1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button_free_2 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		self.m_button_free_2.Hide()

		bSizer12.Add( self.m_button_free_2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button_free_3 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		self.m_button_free_3.Hide()

		bSizer12.Add( self.m_button_free_3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button_free_4 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		self.m_button_free_4.Hide()

		bSizer12.Add( self.m_button_free_4, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer12.Add( bSizer12, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer12 )
		self.Layout()
		fgSizer12.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button_show.Bind( wx.EVT_BUTTON, self.OnShow )
		self.m_button_add.Bind( wx.EVT_BUTTON, self.OnAdd )
		self.m_button_edit.Bind( wx.EVT_BUTTON, self.OnEdit )
		self.m_button_del.Bind( wx.EVT_BUTTON, self.OnDel )
		self.m_button_help.Bind( wx.EVT_BUTTON, self.OnHelp )
		self.m_button_close.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnShow( self, event ):
		event.Skip()

	def OnAdd( self, event ):
		event.Skip()

	def OnEdit( self, event ):
		event.Skip()

	def OnDel( self, event ):
		event.Skip()

	def OnHelp( self, event ):
		event.Skip()



###########################################################################
## Class Activ
###########################################################################

class Activ ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Активация на програмата!", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer1 = wx.GridSizer( 5, 0, 0, 0 )

		gSizer2 = wx.GridSizer( 0, 0, 0, 0 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"БАЗОВ КОД", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText1.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		gSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 0, 0, 0 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 650,-1 ), wx.TE_PROCESS_TAB|wx.TE_READONLY )
		self.m_textCtrl1.SetMaxLength( 36 )
		self.m_textCtrl1.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_textCtrl1.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		gSizer3.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		gSizer1.Add( gSizer3, 1, wx.EXPAND, 5 )

		gSizer4 = wx.GridSizer( 0, 0, 0, 0 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"КОД ЗА АКТИВАЦИЯ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText2.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer4.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		gSizer1.Add( gSizer4, 1, wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 0, 0, 0, 0 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 650,-1 ), wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB )
		self.m_textCtrl2.SetMaxLength( 36 )
		self.m_textCtrl2.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_textCtrl2.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		gSizer5.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		gSizer1.Add( gSizer5, 1, wx.EXPAND, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		gSizer1.Add( m_sdbSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer1 )
		self.Layout()
		gSizer1.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_textCtrl2.Bind( wx.EVT_TEXT_ENTER, self.OnActiv )
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.OnActiv )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnActiv( self, event ):
		event.Skip()




###########################################################################
## Class Login
###########################################################################

class Login ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Вход", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer6 = wx.GridSizer( 3, 0, 0, 0 )

		gSizer10 = wx.GridSizer( 2, 0, 0, 0 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Потребител", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText7.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer10.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		gSizer10.Add( self.m_textCtrl7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		gSizer6.Add( gSizer10, 1, wx.EXPAND, 5 )

		gSizer11 = wx.GridSizer( 2, 0, 0, 0 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Парола", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText8.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer11.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TE_PASSWORD|wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB )
		gSizer11.Add( self.m_textCtrl8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		gSizer6.Add( gSizer11, 1, wx.EXPAND, 5 )

		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
		self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
		m_sdbSizer2.Realize();

		gSizer6.Add( m_sdbSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer6 )
		self.Layout()
		gSizer6.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_textCtrl8.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_sdbSizer2Cancel.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_sdbSizer2OK.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()




###########################################################################
## Class AddUser
###########################################################################

class AddUser ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добави потребител", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer9 = wx.GridSizer( 5, 0, 0, 0 )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Потребител:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText5.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer10.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PROCESS_TAB )
		gSizer10.Add( self.m_textCtrl5, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		gSizer9.Add( gSizer10, 1, wx.EXPAND, 5 )

		gSizer11 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Име:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText6.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer11.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PROCESS_TAB )
		gSizer11.Add( self.m_textCtrl6, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		gSizer9.Add( gSizer11, 1, wx.EXPAND, 5 )

		gSizer12 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Парола:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText7.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer12.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD|wx.TE_PROCESS_TAB )
		gSizer12.Add( self.m_textCtrl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )


		gSizer9.Add( gSizer12, 1, wx.EXPAND, 5 )

		gSizer13 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Парола:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText8.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer13.Add( self.m_staticText8, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD|wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB )
		gSizer13.Add( self.m_textCtrl8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )


		gSizer9.Add( gSizer13, 1, wx.EXPAND, 5 )

		m_sdbSizer3 = wx.StdDialogButtonSizer()
		self.m_sdbSizer3OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer3.AddButton( self.m_sdbSizer3OK )
		self.m_sdbSizer3Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer3.AddButton( self.m_sdbSizer3Cancel )
		m_sdbSizer3.Realize();

		gSizer9.Add( m_sdbSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer9 )
		self.Layout()
		gSizer9.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_textCtrl8.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
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
## Class AddIP
###########################################################################

class AddIP ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добавяне на машина", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"IP на SMIB модула", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText20.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer1.Add( self.m_staticText20, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_textCtrl12.SetMaxLength( 15 )
		self.m_textCtrl12.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_textCtrl12.SetToolTip( u"IP във формат: 192.168.0.55" )

		bSizer1.Add( self.m_textCtrl12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_choice2Choices = []
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		self.m_choice2.Hide()

		bSizer1.Add( self.m_choice2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Проверка на връзката", wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_textCtrl12.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()



###########################################################################
## Class AddSMIB
###########################################################################

class AddSMIB ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добавяне на машина", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer36 = wx.GridSizer( 3, 0, 0, 0 )

		gSizer22 = wx.GridSizer( 0, 2, 0, 0 )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"SMIB" ), wx.VERTICAL )

		self.m_staticText26 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"IP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		sbSizer5.Add( self.m_staticText26, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText27 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"SN:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		sbSizer5.Add( self.m_staticText27, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText28 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Версия:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		sbSizer5.Add( self.m_staticText28, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer22.Add( sbSizer5, 1, wx.EXPAND, 5 )

		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"SAS" ), wx.VERTICAL )

		self.m_radioBtn1 = wx.RadioButton( sbSizer6.GetStaticBox(), wx.ID_ANY, u"SAS Протокол", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

		self.m_radioBtn2 = wx.RadioButton( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Механични броячи", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.m_radioBtn2, 0, wx.ALL, 5 )


		gSizer22.Add( sbSizer6, 1, wx.EXPAND, 5 )


		gSizer36.Add( gSizer22, 1, wx.EXPAND, 5 )

		gSizer23 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Номер по лиценз", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		gSizer23.Add( self.m_staticText35, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		gSizer23.Add( self.m_textCtrl21, 0, wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Модел на машина", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		gSizer23.Add( self.m_staticText33, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer23.Add( self.m_textCtrl22, 0, wx.ALL, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Сериен номер", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		gSizer23.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl23 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer23.Add( self.m_textCtrl23, 0, wx.ALL, 5 )


		gSizer36.Add( gSizer23, 1, wx.EXPAND, 5 )

		m_sdbSizer5 = wx.StdDialogButtonSizer()
		self.m_sdbSizer5OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer5.AddButton( self.m_sdbSizer5OK )
		self.m_sdbSizer5Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer5.AddButton( self.m_sdbSizer5Cancel )
		m_sdbSizer5.Realize();

		gSizer36.Add( m_sdbSizer5, 1, wx.EXPAND|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.SetSizer( gSizer36 )
		self.Layout()
		gSizer36.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_textCtrl23.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_sdbSizer5Cancel.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_sdbSizer5OK.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()




###########################################################################
## Class AddSMIBToGroup
###########################################################################

class AddSMIBToGroup ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer11 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer12 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Машини в залата", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		fgSizer12.Add( self.m_staticText24, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		fgSizer12.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Машини в групата", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		fgSizer12.Add( self.m_staticText26, 0, wx.ALL|wx.EXPAND, 5 )

		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, 0 )
		self.m_listBox1.SetMinSize( wx.Size( 300,400 ) )

		fgSizer12.Add( self.m_listBox1, 0, wx.ALL, 5 )

		gSizer18 = wx.GridSizer( 3, 0, 0, 0 )

		self.m_bpButton9 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton9.SetBitmap( wx.Bitmap( u"img/32x32/add.png", wx.BITMAP_TYPE_ANY ) )
		gSizer18.Add( self.m_bpButton9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText67 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText67.Wrap( -1 )

		gSizer18.Add( self.m_staticText67, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bpButton10 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton10.SetBitmap( wx.Bitmap( u"img/32x32/remove.png", wx.BITMAP_TYPE_ANY ) )
		gSizer18.Add( self.m_bpButton10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer12.Add( gSizer18, 1, wx.EXPAND, 5 )

		m_listBox2Choices = []
		self.m_listBox2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, 0 )
		self.m_listBox2.SetMinSize( wx.Size( 300,400 ) )

		fgSizer12.Add( self.m_listBox2, 0, wx.ALL, 5 )


		fgSizer11.Add( fgSizer12, 1, wx.EXPAND, 5 )

		gSizer20 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button14 = wx.Button( self, wx.ID_ANY, u"Зарвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer20.Add( self.m_button14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button15 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer20.Add( self.m_button15, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer11.Add( gSizer20, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer11 )
		self.Layout()
		fgSizer11.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_listBox1.Bind( wx.EVT_LISTBOX, self.OnShowNomInL )
		self.m_bpButton9.Bind( wx.EVT_BUTTON, self.AddToGroup )
		self.m_bpButton10.Bind( wx.EVT_BUTTON, self.RemoveFromGroup )
		self.m_listBox2.Bind( wx.EVT_LISTBOX, self.OnShowNomInLRight )
		self.m_button14.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button15.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnShowNomInL( self, event ):
		event.Skip()

	def AddToGroup( self, event ):
		event.Skip()

	def RemoveFromGroup( self, event ):
		event.Skip()

	def OnShowNomInLRight( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class ClasicLevel
###########################################################################

class ClasicLevel ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Нива!", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer39 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer39.SetFlexibleDirection( wx.BOTH )
		fgSizer39.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer42 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer42.SetFlexibleDirection( wx.BOTH )
		fgSizer42.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer15 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Име на ниво", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText31.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer15.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer15.Add( self.m_textCtrl15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"Начална стойност", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		self.m_staticText39.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText39.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer15.Add( self.m_staticText39, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer15.Add( self.m_textCtrl22, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText54 = wx.StaticText( self, wx.ID_ANY, u"Задържане в %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )

		self.m_staticText54.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText54.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer15.Add( self.m_staticText54, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl33 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.m_textCtrl33, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText63 = wx.StaticText( self, wx.ID_ANY, u"Падане", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )

		self.m_staticText63.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText63.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		self.m_staticText63.Hide()

		fgSizer15.Add( self.m_staticText63, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl331 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl331.Hide()

		fgSizer15.Add( self.m_textCtrl331, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, u"Текуща стойност: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		self.m_staticText53.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText53.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer15.Add( self.m_staticText53, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText541 = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText541.Wrap( -1 )

		self.m_staticText541.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText541.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer15.Add( self.m_staticText541, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"Скрита стойност: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		self.m_staticText55.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText55.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer15.Add( self.m_staticText55, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText561 = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText561.Wrap( -1 )

		self.m_staticText561.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText561.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer15.Add( self.m_staticText561, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		fgSizer42.Add( fgSizer15, 1, wx.EXPAND, 5 )

		fgSizer16 = wx.FlexGridSizer( 0, 0, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer24 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Обхват", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText34.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer24.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		fgSizer26 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer26.SetFlexibleDirection( wx.BOTH )
		fgSizer26.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"От сума", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		fgSizer26.Add( self.m_staticText32, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer26.Add( self.m_textCtrl16, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"До сума", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		fgSizer26.Add( self.m_staticText33, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl17 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer26.Add( self.m_textCtrl17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer24.Add( fgSizer26, 1, wx.EXPAND, 5 )


		fgSizer16.Add( fgSizer24, 1, wx.EXPAND, 5 )

		fgSizer25 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer25.SetFlexibleDirection( wx.BOTH )
		fgSizer25.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Отчисление % ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		self.m_staticText35.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText35.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer25.Add( self.m_staticText35, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		fgSizer27 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer27.SetFlexibleDirection( wx.BOTH )
		fgSizer27.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, u"Отчисление %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		fgSizer27.Add( self.m_staticText37, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer27.Add( self.m_textCtrl20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )

		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, u"Скрит %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		fgSizer27.Add( self.m_staticText38, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer27.Add( self.m_textCtrl21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		fgSizer25.Add( fgSizer27, 1, wx.EXPAND, 5 )


		fgSizer16.Add( fgSizer25, 1, wx.EXPAND, 5 )


		fgSizer42.Add( fgSizer16, 1, wx.EXPAND, 5 )

		fgSizer38 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer38.SetFlexibleDirection( wx.BOTH )
		fgSizer38.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"BET" ), wx.VERTICAL )

		self.m_radioBtn3 = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Bet не участва", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn3.SetValue( True )
		sbSizer4.Add( self.m_radioBtn3, 0, wx.ALL, 5 )

		self.m_radioBtn4 = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Bet увеличава шанса", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_radioBtn4, 0, wx.ALL, 5 )

		self.m_checkBox171 = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Задължителна карта", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_checkBox171, 0, wx.ALL, 5 )


		fgSizer38.Add( sbSizer4, 0, 0, 5 )

		gSizer25 = wx.GridSizer( 3, 3, 0, 0 )

		self.m_staticText56 = wx.StaticText( self, wx.ID_ANY, u"Мин. Бет", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )

		self.m_staticText56.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText56.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer25.Add( self.m_staticText56, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_checkBox17 = wx.CheckBox( self, wx.ID_ANY, u"Умножи x2", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_checkBox17, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		gSizer25.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_textCtrl35 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_textCtrl35, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl32 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_textCtrl32, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_spinCtrl21 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 2, 5, 3 )
		gSizer25.Add( self.m_spinCtrl21, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText68 = wx.StaticText( self, wx.ID_ANY, u"От/До Час", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )

		self.m_staticText68.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText68.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer25.Add( self.m_staticText68, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl332 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_textCtrl332, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl34 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_textCtrl34, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer38.Add( gSizer25, 1, wx.EXPAND, 5 )


		fgSizer42.Add( fgSizer38, 0, 0, 5 )


		fgSizer39.Add( fgSizer42, 1, wx.EXPAND, 5 )

		gSizer39 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer39.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer39.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer39.Add( self.m_button16, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer39.Add( self.m_button17, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		fgSizer39.Add( gSizer39, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer39 )
		self.Layout()
		fgSizer39.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_radioBtn3.Bind( wx.EVT_RADIOBUTTON, self.OnShow )
		self.m_radioBtn4.Bind( wx.EVT_RADIOBUTTON, self.OnHide )
		self.m_checkBox17.Bind( wx.EVT_CHECKBOX, self.OnX2 )
		self.m_button16.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button17.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnShow( self, event ):
		event.Skip()

	def OnHide( self, event ):
		event.Skip()

	def OnX2( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class TimeLevel
###########################################################################

class TimeLevel ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Времева игра", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer21 = wx.FlexGridSizer( 5, 0, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer22 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer22.SetMinSize( wx.Size( 200,-1 ) )
		self.m_staticText411 = wx.StaticText( self, wx.ID_ANY, u"Име на ниво:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText411.Wrap( -1 )

		self.m_staticText411.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText411.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer22.Add( self.m_staticText411, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl241 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 280,-1 ), 0 )
		fgSizer22.Add( self.m_textCtrl241, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, u"Период:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		self.m_staticText37.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText37.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer22.Add( self.m_staticText37, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		m_choice4Choices = []
		self.m_choice4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 280,-1 ), m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 0 )
		fgSizer22.Add( self.m_choice4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"Стойност:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		self.m_staticText42.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText42.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		fgSizer22.Add( self.m_staticText42, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl25 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 280,-1 ), 0 )
		fgSizer22.Add( self.m_textCtrl25, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		fgSizer21.Add( fgSizer22, 1, wx.EXPAND, 5 )

		fgSizer28 = wx.FlexGridSizer( 2, 4, 0, 0 )
		fgSizer28.SetFlexibleDirection( wx.BOTH )
		fgSizer28.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Понеделник", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.Hide()

		fgSizer28.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"Вторник", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.Hide()

		fgSizer28.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		self.m_checkBox3 = wx.CheckBox( self, wx.ID_ANY, u"Сряда", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox3.Hide()

		fgSizer28.Add( self.m_checkBox3, 0, wx.ALL, 5 )

		self.m_checkBox4 = wx.CheckBox( self, wx.ID_ANY, u"Четвъртък", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox4.Hide()

		fgSizer28.Add( self.m_checkBox4, 0, wx.ALL, 5 )

		self.m_checkBox5 = wx.CheckBox( self, wx.ID_ANY, u"Петък", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox5.Hide()

		fgSizer28.Add( self.m_checkBox5, 0, wx.ALL, 5 )

		self.m_checkBox6 = wx.CheckBox( self, wx.ID_ANY, u"Събота", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox6.Hide()

		fgSizer28.Add( self.m_checkBox6, 0, wx.ALL, 5 )

		self.m_checkBox7 = wx.CheckBox( self, wx.ID_ANY, u"Неделя", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox7.Hide()

		fgSizer28.Add( self.m_checkBox7, 0, wx.ALL, 5 )


		fgSizer21.Add( fgSizer28, 1, wx.EXPAND, 5 )

		fgSizer23 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer23.SetFlexibleDirection( wx.BOTH )
		fgSizer23.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer24 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"От Час:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		fgSizer24.Add( self.m_staticText40, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl23 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer24.Add( self.m_textCtrl23, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"До Час:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		fgSizer24.Add( self.m_staticText41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer24.Add( self.m_textCtrl24, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer23.Add( fgSizer24, 1, wx.EXPAND, 5 )

		fgSizer26 = wx.FlexGridSizer( 4, 0, 0, 0 )
		fgSizer26.SetFlexibleDirection( wx.BOTH )
		fgSizer26.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_radioBtn5 = wx.RadioButton( self, wx.ID_ANY, u"Фиксирана стойност", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer26.Add( self.m_radioBtn5, 0, wx.ALL, 5 )

		self.m_radioBtn6 = wx.RadioButton( self, wx.ID_ANY, u"С натрупване", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer26.Add( self.m_radioBtn6, 0, wx.ALL, 5 )

		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"Отчисление %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		self.m_staticText45.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText45.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText45.Hide()

		fgSizer26.Add( self.m_staticText45, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl28 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl28.Hide()

		fgSizer26.Add( self.m_textCtrl28, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer23.Add( fgSizer26, 1, wx.EXPAND, 5 )


		fgSizer21.Add( fgSizer23, 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Минимален бет", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText51.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer5.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl281 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl281, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer21.Add( bSizer5, 1, wx.EXPAND, 5 )

		gSizer22 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.m_button16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.m_button17, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer21.Add( gSizer22, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer21 )
		self.Layout()
		fgSizer21.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_choice4.Bind( wx.EVT_CHOICE, self.OnFixFrame )
		self.m_radioBtn5.Bind( wx.EVT_RADIOBUTTON, self.OnRemoveProcent )
		self.m_radioBtn6.Bind( wx.EVT_RADIOBUTTON, self.OnAddProcent )
		self.m_button16.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button17.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnFixFrame( self, event ):
		event.Skip()

	def OnRemoveProcent( self, event ):
		event.Skip()

	def OnAddProcent( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class DateTime
###########################################################################

class DateTime ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Дата и час", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer30 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer30.SetFlexibleDirection( wx.BOTH )
		fgSizer30.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_calendar2 = wx.adv.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS )
		fgSizer30.Add( self.m_calendar2, 0, wx.ALL, 5 )

		gSizer25 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"Час:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		self.m_staticText45.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText45.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer25.Add( self.m_staticText45, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_spinCtrl2 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 24, 0 )
		gSizer25.Add( self.m_spinCtrl2, 0, wx.ALL, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 59, 0 )
		gSizer25.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )


		fgSizer30.Add( gSizer25, 1, wx.EXPAND, 5 )

		gSizer26 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer26.Add( self.m_button20, 0, wx.ALL, 5 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer26.Add( self.m_button21, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		fgSizer30.Add( gSizer26, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer30 )
		self.Layout()
		fgSizer30.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button20.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button21.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class GetDB
###########################################################################

class GetDB ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Изтегляне на информация от сървъра", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 )
		self.m_gauge1.SetMinSize( wx.Size( 500,-1 ) )

		bSizer3.Add( self.m_gauge1, 0, wx.ALL, 5 )

		self.m_staticText69 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )

		bSizer3.Add( self.m_staticText69, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button21, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()
		bSizer3.Fit( self )

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
## Class SelectLog
###########################################################################

class SelectLog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Покажи лог", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer32 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer32.SetFlexibleDirection( wx.BOTH )
		fgSizer32.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer34 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer34.SetFlexibleDirection( wx.BOTH )
		fgSizer34.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, u"От Дата", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		fgSizer34.Add( self.m_staticText53, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText54 = wx.StaticText( self, wx.ID_ANY, u"До Дата", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )

		fgSizer34.Add( self.m_staticText54, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_calendar5 = wx.adv.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS )
		fgSizer34.Add( self.m_calendar5, 0, wx.ALL, 5 )

		self.m_calendar6 = wx.adv.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS )
		fgSizer34.Add( self.m_calendar6, 0, wx.ALL, 5 )


		fgSizer32.Add( fgSizer34, 1, wx.EXPAND, 5 )

		gSizer28 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer28.Add( self.m_button23, 0, wx.ALL, 5 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"Изтегли", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer28.Add( self.m_button24, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		fgSizer32.Add( gSizer28, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer32 )
		self.Layout()
		fgSizer32.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button23.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button24.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class ClasicGrupConf
###########################################################################

class ClasicGrupConf ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Настройки на група", pos = wx.DefaultPosition, size = wx.Size( 640,474 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer35 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer35.SetFlexibleDirection( wx.BOTH )
		fgSizer35.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer30 = wx.GridSizer( 2, 0, 0, 0 )

		self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"Задържане в %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		self.m_staticText55.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText55.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer30.Add( self.m_staticText55, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl26 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer30.Add( self.m_textCtrl26, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer35.Add( gSizer30, 1, wx.EXPAND, 5 )

		fgSizer37 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer37.SetFlexibleDirection( wx.BOTH )
		fgSizer37.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Activ" ), wx.VERTICAL )

		self.m_checkBox8 = wx.CheckBox( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Винаги", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox8.SetValue(True)
		sbSizer5.Add( self.m_checkBox8, 0, wx.ALL, 5 )

		gSizer28 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_checkBox9 = wx.CheckBox( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Понеделник", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer28.Add( self.m_checkBox9, 0, wx.ALL, 5 )

		self.m_spinCtrl3 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 0 )
		gSizer28.Add( self.m_spinCtrl3, 0, wx.ALL, 5 )

		self.m_spinCtrl4 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 24, 1 )
		gSizer28.Add( self.m_spinCtrl4, 0, wx.ALL, 5 )


		sbSizer5.Add( gSizer28, 1, wx.EXPAND, 5 )

		gSizer281 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_checkBox91 = wx.CheckBox( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Вторник", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer281.Add( self.m_checkBox91, 0, wx.ALL, 5 )

		self.m_spinCtrl31 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 0 )
		gSizer281.Add( self.m_spinCtrl31, 0, wx.ALL, 5 )

		self.m_spinCtrl41 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 24, 1 )
		gSizer281.Add( self.m_spinCtrl41, 0, wx.ALL, 5 )


		sbSizer5.Add( gSizer281, 1, wx.EXPAND, 5 )

		gSizer2811 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_checkBox911 = wx.CheckBox( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Сряда", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2811.Add( self.m_checkBox911, 0, wx.ALL, 5 )

		self.m_spinCtrl311 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 0 )
		gSizer2811.Add( self.m_spinCtrl311, 0, wx.ALL, 5 )

		self.m_spinCtrl411 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 24, 1 )
		gSizer2811.Add( self.m_spinCtrl411, 0, wx.ALL, 5 )


		sbSizer5.Add( gSizer2811, 1, wx.EXPAND, 5 )

		gSizer2812 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_checkBox912 = wx.CheckBox( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Четвъртък", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2812.Add( self.m_checkBox912, 0, wx.ALL, 5 )

		self.m_spinCtrl312 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 0 )
		gSizer2812.Add( self.m_spinCtrl312, 0, wx.ALL, 5 )

		self.m_spinCtrl412 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 24, 1 )
		gSizer2812.Add( self.m_spinCtrl412, 0, wx.ALL, 5 )


		sbSizer5.Add( gSizer2812, 1, wx.EXPAND, 5 )

		gSizer2813 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_checkBox913 = wx.CheckBox( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Петък", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2813.Add( self.m_checkBox913, 0, wx.ALL, 5 )

		self.m_spinCtrl313 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 0 )
		gSizer2813.Add( self.m_spinCtrl313, 0, wx.ALL, 5 )

		self.m_spinCtrl413 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 24, 1 )
		gSizer2813.Add( self.m_spinCtrl413, 0, wx.ALL, 5 )


		sbSizer5.Add( gSizer2813, 1, wx.EXPAND, 5 )

		gSizer2814 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_checkBox914 = wx.CheckBox( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Събота", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2814.Add( self.m_checkBox914, 0, wx.ALL, 5 )

		self.m_spinCtrl314 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 0 )
		gSizer2814.Add( self.m_spinCtrl314, 0, wx.ALL, 5 )

		self.m_spinCtrl414 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 24, 1 )
		gSizer2814.Add( self.m_spinCtrl414, 0, wx.ALL, 5 )


		sbSizer5.Add( gSizer2814, 1, wx.EXPAND, 5 )

		gSizer2815 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_checkBox915 = wx.CheckBox( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Неделя", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2815.Add( self.m_checkBox915, 0, wx.ALL, 5 )

		self.m_spinCtrl315 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 0 )
		gSizer2815.Add( self.m_spinCtrl315, 0, wx.ALL, 5 )

		self.m_spinCtrl415 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 24, 1 )
		gSizer2815.Add( self.m_spinCtrl415, 0, wx.ALL, 5 )


		sbSizer5.Add( gSizer2815, 1, wx.EXPAND, 5 )


		fgSizer37.Add( sbSizer5, 1, wx.EXPAND, 5 )

		fgSizer44 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer44.SetFlexibleDirection( wx.BOTH )
		fgSizer44.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_checkBox18 = wx.CheckBox( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Глобална", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer11.Add( self.m_checkBox18, 0, wx.ALL, 5 )

		m_radioBox3Choices = [ u"No", u"Yes" ]
		self.m_radioBox3 = wx.RadioBox( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Progressive delay", wx.DefaultPosition, wx.DefaultSize, m_radioBox3Choices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox3.SetSelection( 1 )
		sbSizer11.Add( self.m_radioBox3, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		gSizer44 = wx.GridSizer( 2, 1, 0, 0 )

		self.m_staticText53 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Стъпка %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		gSizer44.Add( self.m_staticText53, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_spinCtrl19 = wx.SpinCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 10, 50, 0 )
		gSizer44.Add( self.m_spinCtrl19, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer5.Add( gSizer44, 1, wx.EXPAND, 5 )

		gSizer441 = wx.GridSizer( 2, 1, 0, 0 )

		self.m_staticText531 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Забавяне % на база бет", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText531.Wrap( -1 )

		gSizer441.Add( self.m_staticText531, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_spinCtrl191 = wx.SpinCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 50, 0 )
		gSizer441.Add( self.m_spinCtrl191, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer5.Add( gSizer441, 1, wx.EXPAND, 5 )


		sbSizer11.Add( bSizer5, 1, wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		fgSizer44.Add( sbSizer11, 1, wx.EXPAND, 5 )

		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Deduction if min bet" ), wx.VERTICAL )

		self.m_radioBtn11 = wx.RadioButton( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Неактивно", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.m_radioBtn11, 0, wx.ALL, 5 )

		self.m_radioBtn12 = wx.RadioButton( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Активно", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.m_radioBtn12, 0, wx.ALL, 5 )


		fgSizer44.Add( sbSizer12, 1, wx.EXPAND, 5 )


		fgSizer37.Add( fgSizer44, 1, wx.EXPAND, 5 )


		fgSizer35.Add( fgSizer37, 1, wx.EXPAND, 5 )

		gSizer29 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button25 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer29.Add( self.m_button25, 0, wx.ALL, 5 )

		self.m_button26 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer29.Add( self.m_button26, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		fgSizer35.Add( gSizer29, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer35 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_checkBox8.Bind( wx.EVT_CHECKBOX, self.RemoveAllSelection )
		self.m_checkBox9.Bind( wx.EVT_CHECKBOX, self.ActiveSelected )
		self.m_checkBox91.Bind( wx.EVT_CHECKBOX, self.ActiveSelected )
		self.m_checkBox911.Bind( wx.EVT_CHECKBOX, self.ActiveSelected )
		self.m_checkBox912.Bind( wx.EVT_CHECKBOX, self.ActiveSelected )
		self.m_checkBox913.Bind( wx.EVT_CHECKBOX, self.ActiveSelected )
		self.m_checkBox914.Bind( wx.EVT_CHECKBOX, self.ActiveSelected )
		self.m_checkBox915.Bind( wx.EVT_CHECKBOX, self.ActiveSelected )
		self.m_radioBox3.Bind( wx.EVT_RADIOBOX, self.OnProgresivHold )
		self.m_button25.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button26.Bind( wx.EVT_BUTTON, self.OnSave )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def RemoveAllSelection( self, event ):
		event.Skip()

	def ActiveSelected( self, event ):
		event.Skip()







	def OnProgresivHold( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()

	def OnSave( self, event ):
		event.Skip()


###########################################################################
## Class TimeLevelConf
###########################################################################

class TimeLevelConf ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Настройки група!", pos = wx.DefaultPosition, size = wx.Size( 488,262 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer41 = wx.GridSizer( 3, 0, 0, 0 )

		gSizer30 = wx.GridSizer( 2, 0, 0, 0 )

		self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"Задържане в минути", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		self.m_staticText55.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText55.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer30.Add( self.m_staticText55, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_textCtrl26 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer30.Add( self.m_textCtrl26, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer41.Add( gSizer30, 1, wx.EXPAND, 5 )

		gSizer43 = wx.GridSizer( 2, 2, 0, 0 )

		self.m_staticText551 = wx.StaticText( self, wx.ID_ANY, u"Минимално машини", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText551.Wrap( -1 )

		self.m_staticText551.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText551.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer43.Add( self.m_staticText551, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_spinCtrl20 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 50, 0 )
		gSizer43.Add( self.m_spinCtrl20, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText5511 = wx.StaticText( self, wx.ID_ANY, u"Последните Х минути", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5511.Wrap( -1 )

		self.m_staticText5511.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText5511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer43.Add( self.m_staticText5511, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_spinCtrl201 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 59, 1 )
		gSizer43.Add( self.m_spinCtrl201, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer41.Add( gSizer43, 1, wx.EXPAND, 5 )

		gSizer29 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button25 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer29.Add( self.m_button25, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button26 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer29.Add( self.m_button26, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		gSizer41.Add( gSizer29, 1, wx.EXPAND|wx.ALIGN_BOTTOM, 5 )


		self.SetSizer( gSizer41 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button25.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button26.Bind( wx.EVT_BUTTON, self.OnSave )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnSave( self, event ):
		event.Skip()


###########################################################################
## Class ServerSelect
###########################################################################

class ServerSelect ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Избери сървър", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText59 = wx.StaticText( self, wx.ID_ANY, u"Избери Сървър", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )

		self.m_staticText59.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText59.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer6.Add( self.m_staticText59, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		bSizer6.Add( self.m_choice3, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer40 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_bpButton15 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton15.SetBitmap( wx.Bitmap( u"img/22x22/list-add.png", wx.BITMAP_TYPE_ANY ) )
		gSizer40.Add( self.m_bpButton15, 0, wx.ALL, 5 )

		self.m_button27 = wx.Button( self, wx.ID_ANY, u"ОК", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer40.Add( self.m_button27, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer6.Add( gSizer40, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()
		bSizer6.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_bpButton15.Bind( wx.EVT_BUTTON, self.OnAddServer )
		self.m_button27.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnAddServer( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class AddServer
###########################################################################

class AddServer ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добави сървър", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText60 = wx.StaticText( self, wx.ID_ANY, u"Име на сървър", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )

		self.m_staticText60.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText60.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer7.Add( self.m_staticText60, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl30 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_textCtrl30, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"IP на сървър", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		self.m_staticText61.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText61.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer7.Add( self.m_staticText61, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl31 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_textCtrl31, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer41 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button28 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer41.Add( self.m_button28, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button29 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer41.Add( self.m_button29, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer7.Add( gSizer41, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()
		bSizer7.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button28.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button29.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class GlobalServer
###########################################################################

class GlobalServer ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"IP Глобален сървър", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText201 = wx.StaticText( self, wx.ID_ANY, u"Име на казино", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText201.Wrap( -1 )

		self.m_staticText201.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText201.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer1.Add( self.m_staticText201, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl121 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_textCtrl121.SetMaxLength( 15 )
		self.m_textCtrl121.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_textCtrl121.SetToolTip( u"IP във формат: 192.168.0.55" )

		bSizer1.Add( self.m_textCtrl121, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"IP на глобален", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText20.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer1.Add( self.m_staticText20, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_textCtrl12.SetMaxLength( 15 )
		self.m_textCtrl12.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_textCtrl12.SetToolTip( u"IP във формат: 192.168.0.55" )

		bSizer1.Add( self.m_textCtrl12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer43 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button32 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer43.Add( self.m_button32, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		gSizer43.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		bSizer1.Add( gSizer43, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl121.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_textCtrl12.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_button32.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnGo( self, event ):
		event.Skip()


	def OnClose( self, event ):
		event.Skip()



###########################################################################
## Class VisualConf
###########################################################################

class VisualConf ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Настройки", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText73 = wx.StaticText( self, wx.ID_ANY, u"Име", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText73.Wrap( -1 )

		bSizer10.Add( self.m_staticText73, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl38 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_textCtrl38, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText74 = wx.StaticText( self, wx.ID_ANY, u"Валута", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText74.Wrap( -1 )

		bSizer10.Add( self.m_staticText74, 0, wx.ALL, 5 )

		m_choice4Choices = [ u"BGN", u"EU" ]
		self.m_choice4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 0 )
		bSizer10.Add( self.m_choice4, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText75 = wx.StaticText( self, wx.ID_ANY, u"Фон", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText75.Wrap( -1 )

		bSizer10.Add( self.m_staticText75, 0, wx.ALL, 5 )

		self.m_spinCtrl22 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer10.Add( self.m_spinCtrl22, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText751 = wx.StaticText( self, wx.ID_ANY, u"Шрифт", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText751.Wrap( -1 )

		bSizer10.Add( self.m_staticText751, 0, wx.ALL, 5 )

		self.m_spinCtrl23 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10, 1 )
		bSizer10.Add( self.m_spinCtrl23, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button34 = wx.Button( self, wx.ID_ANY, u"Авто Ъпдейт", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button34, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox19 = wx.CheckBox( self, wx.ID_ANY, u"Микро", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_checkBox19, 0, wx.ALL, 5 )

		self.m_checkBox20 = wx.CheckBox( self, wx.ID_ANY, u"Активни", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_checkBox20, 0, wx.ALL, 5 )

		self.m_checkBox21 = wx.CheckBox( self, wx.ID_ANY, u"Събери рейндж", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_checkBox21, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox22 = wx.CheckBox( self, wx.ID_ANY, u"Потскачащ код", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox22.Enable( False )

		bSizer12.Add( self.m_checkBox22, 0, wx.ALL, 5 )

		self.m_checkBox23 = wx.CheckBox( self, wx.ID_ANY, u"Цветни имена", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_checkBox23, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer12, 1, wx.EXPAND, 5 )

		gSizer47 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button32 = wx.Button( self, wx.ID_ANY, u"Отказ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer47.Add( self.m_button32, 0, wx.ALL, 5 )

		self.m_button33 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer47.Add( self.m_button33, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer10.Add( gSizer47, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()
		bSizer10.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button34.Bind( wx.EVT_BUTTON, self.SVN )
		self.m_button32.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button33.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def SVN( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


