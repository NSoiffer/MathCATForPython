# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
# import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MathCATPreferencesDialog
###########################################################################

class MathCATPreferencesDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"MathCAT Preferences"), pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panelCategories = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizerCategories = wx.BoxSizer( wx.VERTICAL )

		self.m_staticTextCategories = wx.StaticText( self.m_panelCategories, wx.ID_ANY, _(u"Categories:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCategories.Wrap( -1 )

		bSizerCategories.Add( self.m_staticTextCategories, 0, wx.ALL, 5 )

		m_listBoxPreferencesTopicChoices = [ _(u"Speech"), _(u"Navigation"), _(u"Braille") ]
		self.m_listBoxPreferencesTopic = wx.ListBox( self.m_panelCategories, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( -1,-1 ), m_listBoxPreferencesTopicChoices, wx.LB_NO_SB|wx.LB_SINGLE )
		bSizerCategories.Add( self.m_listBoxPreferencesTopic, 0, wx.ALL, 5 )


		bSizerCategories.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_bitmapLogo = wx.StaticBitmap( self.m_panelCategories, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 126,85 ), 0 )
		bSizerCategories.Add( self.m_bitmapLogo, 0, wx.ALL, 5 )


		self.m_panelCategories.SetSizer( bSizerCategories )
		self.m_panelCategories.Layout()
		bSizerCategories.Fit( self.m_panelCategories )
		gbSizer1.Add( self.m_panelCategories, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_simplebookPanelsCategories = wx.Simplebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panelSpeech = wx.Panel( self.m_simplebookPanelsCategories, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		bSizer121 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticTextGenerateSpeechFor1 = wx.StaticText( self.m_panelSpeech, wx.ID_ANY, _(u"Generate speech for:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextGenerateSpeechFor1.Wrap( -1 )

		bSizer6.Add( self.m_staticTextGenerateSpeechFor1, 0, wx.ALL, 5 )

		m_choiceImpairmentChoices = [ _(u"Learning disabilities"), _(u"Blindness"), _(u"Low vision") ]
		self.m_choiceImpairment = wx.Choice( self.m_panelSpeech, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceImpairmentChoices, 0 )
		self.m_choiceImpairment.SetSelection( 1 )
		bSizer6.Add( self.m_choiceImpairment, 0, wx.ALL, 5 )


		bSizer121.Add( bSizer6, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText311 = wx.StaticText( self.m_panelSpeech, wx.ID_ANY, _(u"Language:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText311.Wrap( -1 )

		bSizer7.Add( self.m_staticText311, 0, wx.ALL, 5 )

		m_choiceLanguageChoices = [ _(u"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") ]
		self.m_choiceLanguage = wx.Choice( self.m_panelSpeech, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceLanguageChoices, 0 )
		self.m_choiceLanguage.SetSelection( 0 )
		bSizer7.Add( self.m_choiceLanguage, 0, wx.ALL, 5 )


		bSizer121.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer713 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2111 = wx.StaticText( self.m_panelSpeech, wx.ID_ANY, _(u"Speech style:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2111.Wrap( -1 )

		bSizer713.Add( self.m_staticText2111, 0, wx.ALL, 5 )

		m_choiceSpeechStyleChoices = [ _(u"xxxxxxxxxxxxxxxx") ]
		self.m_choiceSpeechStyle = wx.Choice( self.m_panelSpeech, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceSpeechStyleChoices, 0 )
		self.m_choiceSpeechStyle.SetSelection( 0 )
		bSizer713.Add( self.m_choiceSpeechStyle, 0, wx.ALL, 5 )


		bSizer121.Add( bSizer713, 1, wx.EXPAND, 5 )

		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText211 = wx.StaticText( self.m_panelSpeech, wx.ID_ANY, _(u"Speech amount:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )

		bSizer71.Add( self.m_staticText211, 0, wx.ALL, 5 )

		m_choiceSpeechAmountChoices = [ _(u"Terse"), _(u"Medium"), _(u"Verbose") ]
		self.m_choiceSpeechAmount = wx.Choice( self.m_panelSpeech, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceSpeechAmountChoices, 0 )
		self.m_choiceSpeechAmount.SetSelection( 0 )
		bSizer71.Add( self.m_choiceSpeechAmount, 0, wx.ALL, 5 )


		bSizer121.Add( bSizer71, 1, wx.EXPAND, 5 )

		bSizer7131 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText21111 = wx.StaticText( self.m_panelSpeech, wx.ID_ANY, _(u"Relative speech rate:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21111.Wrap( -1 )

		bSizer7131.Add( self.m_staticText21111, 0, wx.ALL, 5 )

		self.m_sliderRelativeSpeed = wx.Slider( self.m_panelSpeech, wx.ID_ANY, 100, 20, 200, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer7131.Add( self.m_sliderRelativeSpeed, 0, wx.ALL, 5 )


		bSizer121.Add( bSizer7131, 1, wx.EXPAND, 5 )

		bSizerPauseFactor = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticPauseFactor = wx.StaticText( self.m_panelSpeech, wx.ID_ANY, _(u"Pause factor:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticPauseFactor.Wrap( -1 )

		bSizerPauseFactor.Add( self.m_staticPauseFactor, 0, wx.ALL, 5 )

		self.m_sliderPauseFactor = wx.Slider( self.m_panelSpeech, wx.ID_ANY, 7, 0, 14, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizerPauseFactor.Add( self.m_sliderPauseFactor, 0, wx.ALL, 5 )


		bSizer121.Add( bSizerPauseFactor, 1, wx.EXPAND, 5 )

		bSizer7121 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBoxSpeechSound = wx.CheckBox( self.m_panelSpeech, wx.ID_ANY, _(u"Make a sound when starting/ending math speech"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7121.Add( self.m_checkBoxSpeechSound, 0, wx.ALL, 5 )


		bSizer121.Add( bSizer7121, 1, wx.EXPAND, 5 )

		bSizer712 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText411 = wx.StaticText( self.m_panelSpeech, wx.ID_ANY, _(u"Subject area to be used when it cannot be determined automatically:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText411.Wrap( -1 )

		bSizer712.Add( self.m_staticText411, 0, wx.ALL, 5 )

		m_choiceSubjectAreaChoices = [ _(u"General") ]
		self.m_choiceSubjectArea = wx.Choice( self.m_panelSpeech, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceSubjectAreaChoices, 0 )
		self.m_choiceSubjectArea.SetSelection( 0 )
		bSizer712.Add( self.m_choiceSubjectArea, 0, wx.ALL, 5 )


		bSizer121.Add( bSizer712, 1, wx.EXPAND, 5 )

		bSizer711 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText511 = wx.StaticText( self.m_panelSpeech, wx.ID_ANY, _(u"Speech for chemical formulas:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		bSizer711.Add( self.m_staticText511, 0, wx.ALL, 5 )

		m_choiceSpeechForChemicalChoices = [ _(u"Spell it out (H 2 O)"), _(u"As compound (Water)"), _(u"Off (H sub 2 O)") ]
		self.m_choiceSpeechForChemical = wx.Choice( self.m_panelSpeech, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceSpeechForChemicalChoices, 0 )
		self.m_choiceSpeechForChemical.SetSelection( 0 )
		bSizer711.Add( self.m_choiceSpeechForChemical, 0, wx.ALL, 5 )


		bSizer121.Add( bSizer711, 1, wx.EXPAND, 5 )


		self.m_panelSpeech.SetSizer( bSizer121 )
		self.m_panelSpeech.Layout()
		bSizer121.Fit( self.m_panelSpeech )
		self.m_simplebookPanelsCategories.AddPage( self.m_panelSpeech, _(u"a page"), False )
		self.m_panelNavigation = wx.Panel( self.m_simplebookPanelsCategories, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		bSizer1211 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panelNavigation, wx.ID_ANY, _(u"Navigation mode to use when beginning to navigate an equation:") ), wx.VERTICAL )

		m_choiceNavigationModeChoices = [ _(u"Enhanced"), _(u"Simple"), _(u"Character") ]
		self.m_choiceNavigationMode = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceNavigationModeChoices, 0 )
		self.m_choiceNavigationMode.SetSelection( 1 )
		sbSizer1.Add( self.m_choiceNavigationMode, 0, wx.ALL, 5 )

		self.m_checkBoxResetNavigationMode = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"Reset navigation mode on entry to an expression"), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_checkBoxResetNavigationMode, 0, wx.ALL, 5 )


		bSizer1211.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_panelNavigation, wx.ID_ANY, _(u"Navigation speech to use when beginning to navigate an equation:") ), wx.VERTICAL )

		m_choiceNavigationSpeechChoices = [ _(u"Speak"), _(u"Describe/overview") ]
		self.m_choiceNavigationSpeech = wx.Choice( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceNavigationSpeechChoices, 0 )
		self.m_choiceNavigationSpeech.SetSelection( 1 )
		sbSizer11.Add( self.m_choiceNavigationSpeech, 0, wx.ALL, 5 )

		self.m_checkBoxResetNavigationSpeech = wx.CheckBox( sbSizer11.GetStaticBox(), wx.ID_ANY, _(u"Reset navigation speech on entry to an expression"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxResetNavigationSpeech.SetValue(True)
		sbSizer11.Add( self.m_checkBoxResetNavigationSpeech, 0, wx.ALL, 5 )


		bSizer1211.Add( sbSizer11, 1, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBoxAutomaticZoom = wx.CheckBox( self.m_panelNavigation, wx.ID_ANY, _(u"Automatic zoom out of 2D notations"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_checkBoxAutomaticZoom, 0, wx.ALL, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3111 = wx.StaticText( self.m_panelNavigation, wx.ID_ANY, _(u"Speech amount for navigation:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3111.Wrap( -1 )

		bSizer15.Add( self.m_staticText3111, 0, wx.ALL, 5 )

		m_choiceSpeechAmountNavigationChoices = [ _(u"Terse"), _(u"Medium"), _(u"Verbose") ]
		self.m_choiceSpeechAmountNavigation = wx.Choice( self.m_panelNavigation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceSpeechAmountNavigationChoices, 0 )
		self.m_choiceSpeechAmountNavigation.SetSelection( 0 )
		bSizer15.Add( self.m_choiceSpeechAmountNavigation, 0, wx.ALL, 5 )


		bSizer16.Add( bSizer15, 1, wx.EXPAND, 5 )


		bSizer1211.Add( bSizer16, 1, wx.EXPAND, 5 )


		self.m_panelNavigation.SetSizer( bSizer1211 )
		self.m_panelNavigation.Layout()
		bSizer1211.Fit( self.m_panelNavigation )
		self.m_simplebookPanelsCategories.AddPage( self.m_panelNavigation, _(u"a page"), False )
		self.m_panelBraille = wx.Panel( self.m_simplebookPanelsCategories, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		bSizer12111 = wx.BoxSizer( wx.VERTICAL )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticTextGenerateSpeechFor112 = wx.StaticText( self.m_panelBraille, wx.ID_ANY, _(u"Braille math code for refreshable displays:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextGenerateSpeechFor112.Wrap( -1 )

		bSizer17.Add( self.m_staticTextGenerateSpeechFor112, 0, wx.ALL, 5 )

		m_choiceBrailleMathCodeChoices = [ _(u"Nemeth"), _(u"UEB") ]
		self.m_choiceBrailleMathCode = wx.Choice( self.m_panelBraille, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceBrailleMathCodeChoices, 0 )
		self.m_choiceBrailleMathCode.SetSelection( 1 )
		bSizer17.Add( self.m_choiceBrailleMathCode, 0, wx.ALL, 5 )


		bSizer12111.Add( bSizer17, 1, wx.EXPAND, 5 )

		bSizer171 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticTextBrailleHighlights = wx.StaticText( self.m_panelBraille, wx.ID_ANY, _(u"Highlight with dots 7 && 8 the current nav node:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextBrailleHighlights.Wrap( -1 )

		bSizer171.Add( self.m_staticTextBrailleHighlights, 0, wx.ALL, 5 )

		m_choiceBrailleHighlightsChoices = [ _(u"Off"), _(u"First character"), _(u"Endpoints"), _(u"All") ]
		self.m_choiceBrailleHighlights = wx.Choice( self.m_panelBraille, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceBrailleHighlightsChoices, 0 )
		self.m_choiceBrailleHighlights.SetSelection( 1 )
		bSizer171.Add( self.m_choiceBrailleHighlights, 0, wx.ALL, 5 )


		bSizer12111.Add( bSizer171, 1, wx.EXPAND, 5 )


		bSizer12111.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer12111.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer12111.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer12111.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer12111.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panelBraille.SetSizer( bSizer12111 )
		self.m_panelBraille.Layout()
		bSizer12111.Fit( self.m_panelBraille )
		self.m_simplebookPanelsCategories.AddPage( self.m_panelBraille, _(u"a page"), False )

		gbSizer1.Add( self.m_simplebookPanelsCategories, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 10 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer1.Add( self.m_staticline1, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND |wx.ALL, 5 )

		self.m_panelButtons = wx.Panel( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizerButtons = wx.BoxSizer( wx.HORIZONTAL )


		bSizerButtons.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_buttonOK = wx.Button( self.m_panelButtons, wx.ID_ANY, _(u"OK"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerButtons.Add( self.m_buttonOK, 0, wx.ALL, 5 )

		self.m_buttonCancel = wx.Button( self.m_panelButtons, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerButtons.Add( self.m_buttonCancel, 0, wx.ALL, 5 )

		self.m_buttonApply = wx.Button( self.m_panelButtons, wx.ID_ANY, _(u"Apply"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerButtons.Add( self.m_buttonApply, 0, wx.ALL, 5 )

		self.m_buttonReset = wx.Button( self.m_panelButtons, wx.ID_ANY, _(u"Reset to defaults"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerButtons.Add( self.m_buttonReset, 0, wx.ALL, 5 )

		self.m_buttonHelp1 = wx.Button( self.m_panelButtons, wx.ID_ANY, _(u"Help"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerButtons.Add( self.m_buttonHelp1, 0, wx.ALL, 5 )


		self.m_panelButtons.SetSizer( bSizerButtons )
		self.m_panelButtons.Layout()
		bSizerButtons.Fit( self.m_panelButtons )
		gbSizer1.Add( self.m_panelButtons, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 2 ), wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( gbSizer1 )
		self.Layout()
		gbSizer1.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CHAR_HOOK, self.MathCATPreferencesDialogOnCharHook )
		self.Bind( wx.EVT_KEY_UP, self.MathCATPreferencesDialogOnKeyUp )
		self.m_listBoxPreferencesTopic.Bind( wx.EVT_LISTBOX, self.OnListBoxCategories )
		self.m_choiceLanguage.Bind( wx.EVT_CHOICE, self.OnLanguage )
		self.m_sliderRelativeSpeed.Bind( wx.EVT_SCROLL_CHANGED, self.OnRelativeSpeedChanged )
		self.m_sliderPauseFactor.Bind( wx.EVT_SCROLL_CHANGED, self.OnPauseFactorChanged )
		self.m_buttonOK.Bind( wx.EVT_BUTTON, self.OnClickOK )
		self.m_buttonCancel.Bind( wx.EVT_BUTTON, self.OnClickCancel )
		self.m_buttonApply.Bind( wx.EVT_BUTTON, self.OnClickApply )
		self.m_buttonReset.Bind( wx.EVT_BUTTON, self.OnClickReset )
		self.m_buttonHelp1.Bind( wx.EVT_BUTTON, self.OnClickHelp )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def MathCATPreferencesDialogOnCharHook( self, event ):
		event.Skip()

	def MathCATPreferencesDialogOnKeyUp( self, event ):
		event.Skip()

	def OnListBoxCategories( self, event ):
		event.Skip()

	def OnLanguage( self, event ):
		event.Skip()

	def OnRelativeSpeedChanged( self, event ):
		event.Skip()

	def OnPauseFactorChanged( self, event ):
		event.Skip()

	def OnClickOK( self, event ):
		event.Skip()

	def OnClickCancel( self, event ):
		event.Skip()

	def OnClickApply( self, event ):
		event.Skip()

	def OnClickReset( self, event ):
		event.Skip()

	def OnClickHelp( self, event ):
		event.Skip()


