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
## Class KeyBordINT
###########################################################################

class KeyBordINT ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_READONLY )
		fgSizer1.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 7, 0, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"cansel", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button10, 0, wx.ALL, 5 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button18, 0, wx.ALL, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"<-", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button17, 0, wx.ALL, 5 )

		self.m_button92 = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button92, 0, wx.ALL, 5 )

		self.m_button31 = wx.Button( self, wx.ID_ANY, u"A", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		self.m_button31.Hide()

		fgSizer2.Add( self.m_button31, 0, wx.ALL, 5 )

		self.m_button32 = wx.Button( self, wx.ID_ANY, u"B", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		self.m_button32.Hide()

		fgSizer2.Add( self.m_button32, 0, wx.ALL, 5 )

		self.m_button33 = wx.Button( self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		self.m_button33.Hide()

		fgSizer2.Add( self.m_button33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button38 = wx.Button( self, wx.ID_ANY, u"D", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		self.m_button38.Hide()

		fgSizer2.Add( self.m_button38, 0, wx.ALL, 5 )

		self.m_button39 = wx.Button( self, wx.ID_ANY, u"E", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		self.m_button39.Hide()

		fgSizer2.Add( self.m_button39, 0, wx.ALL, 5 )

		self.m_button40 = wx.Button( self, wx.ID_ANY, u"F", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		self.m_button40.Hide()

		fgSizer2.Add( self.m_button40, 0, wx.ALL, 5 )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button20.Hide()

		fgSizer2.Add( self.m_button20, 0, wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button21, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button4, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"*", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button22, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button8, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button23, 0, wx.ALL, 5 )

		self.m_button19 = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button19, 0, wx.ALL, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button11, 0, wx.ALL, 5 )

		self.m_button12 = wx.Button( self, wx.ID_ANY, u"ok", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button12, 0, wx.ALL, 5 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		fgSizer2.Add( self.m_button24, 0, wx.ALL, 5 )


		fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )


		fgSizer1.Add( ( 0, 30), 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()
		fgSizer1.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button10.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button18.Bind( wx.EVT_BUTTON, self.OnClear )
		self.m_button17.Bind( wx.EVT_BUTTON, self.OnDel )
		self.m_button92.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button31.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button32.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button33.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button38.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button39.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button40.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button20.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button21.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button5.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button22.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button8.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button9.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button23.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button19.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button11.Bind( wx.EVT_BUTTON, self.OnInt )
		self.m_button12.Bind( wx.EVT_BUTTON, self.OnGo )
		self.m_button24.Bind( wx.EVT_BUTTON, self.OnRavno )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnClear( self, event ):
		event.Skip()

	def OnDel( self, event ):
		event.Skip()

	def OnInt( self, event ):
		event.Skip()






















	def OnGo( self, event ):
		event.Skip()

	def OnRavno( self, event ):
		event.Skip()


###########################################################################
## Class KeyBordB
###########################################################################

class KeyBordB ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer3 = wx.FlexGridSizer( 6, 0, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer3.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer4 = wx.FlexGridSizer( 1, 11, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button27 = wx.Button( self, wx.ID_ANY, u"я", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer4.Add( self.m_button27, 0, wx.ALL, 5 )

		self.m_button28 = wx.Button( self, wx.ID_ANY, u"в", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer4.Add( self.m_button28, 0, wx.ALL, 5 )

		self.m_button29 = wx.Button( self, wx.ID_ANY, u"е", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer4.Add( self.m_button29, 0, wx.ALL, 5 )

		self.m_button30 = wx.Button( self, wx.ID_ANY, u"р", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer4.Add( self.m_button30, 0, wx.ALL, 5 )

		self.m_button31 = wx.Button( self, wx.ID_ANY, u"т", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer4.Add( self.m_button31, 0, wx.ALL, 5 )

		self.m_button32 = wx.Button( self, wx.ID_ANY, u"ъ", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer4.Add( self.m_button32, 0, wx.ALL, 5 )

		self.m_button33 = wx.Button( self, wx.ID_ANY, u"у", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer4.Add( self.m_button33, 0, wx.ALL, 5 )

		self.m_button34 = wx.Button( self, wx.ID_ANY, u"и", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer4.Add( self.m_button34, 0, wx.ALL, 5 )

		self.m_button35 = wx.Button( self, wx.ID_ANY, u"о", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer4.Add( self.m_button35, 0, wx.ALL, 5 )

		self.m_button36 = wx.Button( self, wx.ID_ANY, u"п", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer4.Add( self.m_button36, 0, wx.ALL, 5 )

		self.m_button37 = wx.Button( self, wx.ID_ANY, u"ч", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer4.Add( self.m_button37, 0, wx.ALL, 5 )


		fgSizer3.Add( fgSizer4, 1, wx.EXPAND, 5 )

		fgSizer13 = wx.FlexGridSizer( 0, 11, 0, 0 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button38 = wx.Button( self, wx.ID_ANY, u"а", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer13.Add( self.m_button38, 0, wx.ALL, 5 )

		self.m_button39 = wx.Button( self, wx.ID_ANY, u"с", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer13.Add( self.m_button39, 0, wx.ALL, 5 )

		self.m_button40 = wx.Button( self, wx.ID_ANY, u"д", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer13.Add( self.m_button40, 0, wx.ALL, 5 )

		self.m_button41 = wx.Button( self, wx.ID_ANY, u"ф", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer13.Add( self.m_button41, 0, wx.ALL, 5 )

		self.m_button42 = wx.Button( self, wx.ID_ANY, u"г", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer13.Add( self.m_button42, 0, wx.ALL, 5 )

		self.m_button43 = wx.Button( self, wx.ID_ANY, u"х", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer13.Add( self.m_button43, 0, wx.ALL, 5 )

		self.m_button44 = wx.Button( self, wx.ID_ANY, u"й", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer13.Add( self.m_button44, 0, wx.ALL, 5 )

		self.m_button45 = wx.Button( self, wx.ID_ANY, u"к", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer13.Add( self.m_button45, 0, wx.ALL, 5 )

		self.m_button46 = wx.Button( self, wx.ID_ANY, u"л", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer13.Add( self.m_button46, 0, wx.ALL, 5 )

		self.m_button47 = wx.Button( self, wx.ID_ANY, u"ш", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer13.Add( self.m_button47, 0, wx.ALL, 5 )

		self.m_button48 = wx.Button( self, wx.ID_ANY, u"щ", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer13.Add( self.m_button48, 0, wx.ALL, 5 )


		fgSizer3.Add( fgSizer13, 1, wx.EXPAND, 5 )

		fgSizer10 = wx.FlexGridSizer( 0, 10, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button49 = wx.Button( self, wx.ID_ANY, u"shift", wx.DefaultPosition, wx.Size( 80,50 ), 0 )
		fgSizer10.Add( self.m_button49, 0, wx.ALL, 5 )

		self.m_button50 = wx.Button( self, wx.ID_ANY, u"з", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer10.Add( self.m_button50, 0, wx.ALL, 5 )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"ь", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer10.Add( self.m_button51, 0, wx.ALL, 5 )

		self.m_button52 = wx.Button( self, wx.ID_ANY, u"ц", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer10.Add( self.m_button52, 0, wx.ALL, 5 )

		self.m_button53 = wx.Button( self, wx.ID_ANY, u"ж", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer10.Add( self.m_button53, 0, wx.ALL, 5 )

		self.m_button54 = wx.Button( self, wx.ID_ANY, u"б", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer10.Add( self.m_button54, 0, wx.ALL, 5 )

		self.m_button55 = wx.Button( self, wx.ID_ANY, u"н", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer10.Add( self.m_button55, 0, wx.ALL, 5 )

		self.m_button56 = wx.Button( self, wx.ID_ANY, u"м", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer10.Add( self.m_button56, 0, wx.ALL, 5 )

		self.m_button69 = wx.Button( self, wx.ID_ANY, u"ю", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer10.Add( self.m_button69, 0, wx.ALL, 5 )

		self.m_button70 = wx.Button( self, wx.ID_ANY, u"<-", wx.DefaultPosition, wx.Size( 80,50 ), 0 )
		fgSizer10.Add( self.m_button70, 0, wx.ALL, 5 )


		fgSizer3.Add( fgSizer10, 1, wx.EXPAND, 5 )

		fgSizer11 = wx.FlexGridSizer( 0, 7, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button63 = wx.Button( self, wx.ID_ANY, u"123", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer11.Add( self.m_button63, 0, wx.ALL, 5 )

		self.m_button64 = wx.Button( self, wx.ID_ANY, u",", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer11.Add( self.m_button64, 0, wx.ALL, 5 )

		self.m_button65 = wx.Button( self, wx.ID_ANY, u"lang", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer11.Add( self.m_button65, 0, wx.ALL, 5 )

		self.m_button66 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 280,50 ), 0 )
		fgSizer11.Add( self.m_button66, 0, wx.ALL, 5 )

		self.m_button67 = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		fgSizer11.Add( self.m_button67, 0, wx.ALL, 5 )

		self.m_button68 = wx.Button( self, wx.ID_ANY, u"Row", wx.DefaultPosition, wx.Size( 45,50 ), 0 )
		fgSizer11.Add( self.m_button68, 0, wx.ALL, 5 )

		self.m_button691 = wx.Button( self, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.Size( 65,50 ), 0 )
		fgSizer11.Add( self.m_button691, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer3.Add( fgSizer11, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer3 )
		self.Layout()
		fgSizer3.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button27.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button28.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button29.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button30.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button31.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button32.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button33.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button34.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button35.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button36.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button37.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button38.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button39.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button40.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button41.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button42.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button43.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button44.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button45.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button46.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button47.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button48.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button49.Bind( wx.EVT_BUTTON, self.OnCtrl )
		self.m_button50.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button51.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button52.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button53.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button54.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button55.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button56.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button69.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button70.Bind( wx.EVT_BUTTON, self.OnDel )
		self.m_button63.Bind( wx.EVT_BUTTON, self.OnSM )
		self.m_button64.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button65.Bind( wx.EVT_BUTTON, self.OnLang )
		self.m_button66.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button67.Bind( wx.EVT_BUTTON, self.OnB )
		self.m_button68.Bind( wx.EVT_BUTTON, self.OnNewRow )
		self.m_button691.Bind( wx.EVT_BUTTON, self.OnEnter )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnB( self, event ):
		event.Skip()






















	def OnCtrl( self, event ):
		event.Skip()









	def OnDel( self, event ):
		event.Skip()

	def OnSM( self, event ):
		event.Skip()


	def OnLang( self, event ):
		event.Skip()



	def OnNewRow( self, event ):
		event.Skip()

	def OnEnter( self, event ):
		event.Skip()


###########################################################################
## Class SelectLang
###########################################################################

class SelectLang ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer14 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer16 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_choice1Choices = [ wx.EmptyString ]
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 180,-1 ), m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		fgSizer16.Add( self.m_choice1, 0, wx.ALL, 5 )


		fgSizer14.Add( fgSizer16, 1, wx.EXPAND, 5 )

		fgSizer15 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button95 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.m_button95, 0, wx.ALL, 5 )

		self.m_button96 = wx.Button( self, wx.ID_ANY, u"ОК", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.m_button96, 0, wx.ALL, 5 )


		fgSizer14.Add( fgSizer15, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer14 )
		self.Layout()
		fgSizer14.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button95.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button96.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


