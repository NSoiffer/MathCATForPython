import wx
# import wx.xrc
import gettext
import addonHandler

_ = gettext.gettext
addonHandler.initTranslation()

###########################################################################
# Class MathCATPreferencesDialog
###########################################################################


class MathCATPreferencesDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            # Translators: title for MathCAT preferences dialog
            title=_("MathCAT Preferences"),
            pos=wx.DefaultPosition,
            size=wx.Size(-1, -1),
            style=wx.DEFAULT_DIALOG_STYLE,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gbSizerMathCATPreferences = wx.GridBagSizer(0, 0)
        gbSizerMathCATPreferences.SetFlexibleDirection(wx.BOTH)
        gbSizerMathCATPreferences.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_panelCategories = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL
        )
        bSizerCategories = wx.BoxSizer(wx.VERTICAL)

        self.m_staticTextCategories = wx.StaticText(
            self.m_panelCategories,
            wx.ID_ANY,
            # Translators: A heading that labels three navigation pane tab names in the MathCAT dialog
            _("Categories:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticTextCategories.Wrap(-1)

        bSizerCategories.Add(self.m_staticTextCategories, 0, wx.ALL, 5)

        m_listBoxPreferencesTopicChoices = [
            # Translators: these are navigation pane headings for the MathCAT preferences dialog under the title "Categories"
            _("Speech"),
            # Translators: these are navigation pane headings for the MathCAT preferences dialog under the title "Categories"
            _("Navigation"),
            # Translators: these are navigation pane headings for the MathCAT preferences dialog under the title "Categories"
            _("Braille"),
        ]
        self.m_listBoxPreferencesTopic = wx.ListBox(
            self.m_panelCategories,
            wx.ID_ANY,
            wx.Point(-1, -1),
            wx.Size(-1, -1),
            m_listBoxPreferencesTopicChoices,
            wx.LB_NO_SB | wx.LB_SINGLE,
        )
        bSizerCategories.Add(self.m_listBoxPreferencesTopic, 0, wx.ALL, 5)

        bSizerCategories.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_bitmapLogo = wx.StaticBitmap(
            self.m_panelCategories,
            wx.ID_ANY,
            wx.NullBitmap,
            wx.DefaultPosition,
            wx.Size(126, 85),
            0,
        )
        bSizerCategories.Add(self.m_bitmapLogo, 0, wx.ALL, 5)

        self.m_panelCategories.SetSizer(bSizerCategories)
        self.m_panelCategories.Layout()
        bSizerCategories.Fit(self.m_panelCategories)
        gbSizerMathCATPreferences.Add(
            self.m_panelCategories,
            wx.GBPosition(0, 0),
            wx.GBSpan(1, 1),
            wx.EXPAND | wx.ALL,
            5,
        )

        self.m_simplebookPanelsCategories = wx.Simplebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_panelSpeech = wx.Panel(
            self.m_simplebookPanelsCategories,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.BORDER_SIMPLE | wx.TAB_TRAVERSAL,
        )
        bSizerSpeech = wx.BoxSizer(wx.VERTICAL)

        bSizerImpairment = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticTextImpairment = wx.StaticText(
            self.m_panelSpeech,
            wx.ID_ANY,
            # Translators: this is the text label for whom to target the speech for (options are below)
            _("Generate speech for:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticTextImpairment.Wrap(-1)

        bSizerImpairment.Add(self.m_staticTextImpairment, 0, wx.ALL, 5)

        m_choiceImpairmentChoices = [
            # Translators: these are the categories of impairments that MathCAT supports
            # Translators: Learning disabilities includes dyslexia and ADHD
            _("Learning disabilities"),
            # Translators: target people who are blind
            _("Blindness"),
            # Translators: target people who have low vision
            _("Low vision"),
        ]
        self.m_choiceImpairment = wx.Choice(
            self.m_panelSpeech,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            m_choiceImpairmentChoices,
            0,
        )
        self.m_choiceImpairment.SetSelection(1)
        bSizerImpairment.Add(self.m_choiceImpairment, 0, wx.ALL, 5)

        bSizerSpeech.Add(bSizerImpairment, 1, wx.EXPAND, 5)

        bSizerLanguage = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticTextLanguage = wx.StaticText(
            self.m_panelSpeech,
            wx.ID_ANY,
            # Translators: label for pull down allowing users to choose the speech language for math
            _("Language:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticTextLanguage.Wrap(-1)

        bSizerLanguage.Add(self.m_staticTextLanguage, 0, wx.ALL, 5)

        m_choiceLanguageChoices = ["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]
        self.m_choiceLanguage = wx.Choice(
            self.m_panelSpeech,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            m_choiceLanguageChoices,
            0,
        )
        self.m_choiceLanguage.SetSelection(0)
        bSizerLanguage.Add(self.m_choiceLanguage, 0, wx.ALL, 5)

        bSizerSpeech.Add(bSizerLanguage, 1, wx.EXPAND, 5)

        bSizerSpeechStyle = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticTextSpeechStyle = wx.StaticText(
            self.m_panelSpeech,
            wx.ID_ANY,
            # Translators: label for pull down allowing users to choose the "style" (version, rules) of speech for math
            _("Speech style:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticTextSpeechStyle.Wrap(-1)

        bSizerSpeechStyle.Add(self.m_staticTextSpeechStyle, 0, wx.ALL, 5)

        m_choiceSpeechStyleChoices = ["xxxxxxxxxxxxxxxx"]
        self.m_choiceSpeechStyle = wx.Choice(
            self.m_panelSpeech,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            m_choiceSpeechStyleChoices,
            0,
        )
        self.m_choiceSpeechStyle.SetSelection(0)
        bSizerSpeechStyle.Add(self.m_choiceSpeechStyle, 0, wx.ALL, 5)

        bSizerSpeech.Add(bSizerSpeechStyle, 1, wx.EXPAND, 5)

        bSizerSpeechAmount = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticTextSpeechAmount = wx.StaticText(
            self.m_panelSpeech,
            wx.ID_ANY,
            # Translators: label for pull down to specify how verbose/terse the speech should be
            _("Speech verbosity:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticTextSpeechAmount.Wrap(-1)

        bSizerSpeechAmount.Add(self.m_staticTextSpeechAmount, 0, wx.ALL, 5)

        # Translators: options for speech verbosity.
        m_choiceSpeechAmountChoices = [
            # Translators: options for speech verbosity -- "terse" = use less words
            _("Terse"),
            # Translators: options for speech verbosity -- "medium" = try to be nether too terse nor too verbose words
            _("Medium"),
            # Translators: options for speech verbosity -- "verbose" = use more words
            _("Verbose"),
        ]
        self.m_choiceSpeechAmount = wx.Choice(
            self.m_panelSpeech,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            m_choiceSpeechAmountChoices,
            0,
        )
        self.m_choiceSpeechAmount.SetSelection(0)
        bSizerSpeechAmount.Add(self.m_choiceSpeechAmount, 0, wx.ALL, 5)

        bSizerSpeech.Add(bSizerSpeechAmount, 1, wx.EXPAND, 5)

        bSizerRelativeSpeed = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticTextRelativeSpeed = wx.StaticText(
            self.m_panelSpeech,
            wx.ID_ANY,
            # Translators: label for slider that specifies a percentage of the normal speech rate that should be used for math
            _("Relative speech rate:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticTextRelativeSpeed.Wrap(-1)

        bSizerRelativeSpeed.Add(self.m_staticTextRelativeSpeed, 0, wx.ALL, 5)

        self.m_sliderRelativeSpeed = wx.Slider(
            self.m_panelSpeech,
            wx.ID_ANY,
            100,
            10,
            100,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.SL_HORIZONTAL,
        )
        self.m_sliderRelativeSpeed.SetLineSize(9)
        bSizerRelativeSpeed.Add(self.m_sliderRelativeSpeed, 0, wx.ALL, 5)

        bSizerSpeech.Add(bSizerRelativeSpeed, 1, wx.EXPAND, 5)

        bSizerPauseFactor = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticPauseFactor = wx.StaticText(
            self.m_panelSpeech,
            wx.ID_ANY,
            # Translators: label for slider that specifies relative factor to increase or decrease pauses in the math speech
            _("Pause factor:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticPauseFactor.Wrap(-1)

        bSizerPauseFactor.Add(self.m_staticPauseFactor, 0, wx.ALL, 5)

        self.m_sliderPauseFactor = wx.Slider(
            self.m_panelSpeech,
            wx.ID_ANY,
            7,
            0,
            14,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.SL_HORIZONTAL,
        )
        bSizerPauseFactor.Add(self.m_sliderPauseFactor, 0, wx.ALL, 5)

        bSizerSpeech.Add(bSizerPauseFactor, 1, wx.EXPAND, 5)

        bSizerSpeechSound = wx.BoxSizer(wx.HORIZONTAL)

        self.m_checkBoxSpeechSound = wx.CheckBox(
            self.m_panelSpeech,
            wx.ID_ANY,
            # Translators: label for check box controling a beep sound
            _("Make a sound when starting/ending math speech"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        bSizerSpeechSound.Add(self.m_checkBoxSpeechSound, 0, wx.ALL, 5)

        bSizerSpeech.Add(bSizerSpeechSound, 1, wx.EXPAND, 5)

        bSizerSubjectArea = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticTextSubjectArea = wx.StaticText(
            self.m_panelSpeech,
            wx.ID_ANY,
            # Translators: label for pull down to specify a subject area (Geometry, Calculus, ...)
            _("Subject area to be used when it cannot be determined automatically:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticTextSubjectArea.Wrap(-1)

        bSizerSubjectArea.Add(self.m_staticTextSubjectArea, 0, wx.ALL, 5)

        # Translators: a generic (non-specific) math subject area
        m_choiceSubjectAreaChoices = [_("General")]
        self.m_choiceSubjectArea = wx.Choice(
            self.m_panelSpeech,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            m_choiceSubjectAreaChoices,
            0,
        )
        self.m_choiceSubjectArea.SetSelection(0)
        bSizerSubjectArea.Add(self.m_choiceSubjectArea, 0, wx.ALL, 5)

        bSizerSpeech.Add(bSizerSubjectArea, 1, wx.EXPAND, 5)

        bSizerSpeechForChemical = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticTextSpeechForChemical = wx.StaticText(
            self.m_panelSpeech,
            wx.ID_ANY,
            # Translators: label for pull down to specify how verbose/terse the speech should be
            _("Speech for chemical formulas:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticTextSpeechForChemical.Wrap(-1)

        bSizerSpeechForChemical.Add(self.m_staticTextSpeechForChemical, 0, wx.ALL, 5)

        m_choiceSpeechForChemicalChoices = [
            # Translators: values for chemistry options with example speech in parenthesis
            _("Spell it out (H 2 O)"),
            # Translators: values for chemistry options with example speech in parenthesis (never interpret as chemistry)
            _("Off (H sub 2 O)"),
        ]
        self.m_choiceSpeechForChemical = wx.Choice(
            self.m_panelSpeech,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            m_choiceSpeechForChemicalChoices,
            0,
        )
        self.m_choiceSpeechForChemical.SetSelection(0)
        bSizerSpeechForChemical.Add(self.m_choiceSpeechForChemical, 0, wx.ALL, 5)

        bSizerSpeech.Add(bSizerSpeechForChemical, 1, wx.EXPAND, 5)

        self.m_panelSpeech.SetSizer(bSizerSpeech)
        self.m_panelSpeech.Layout()
        bSizerSpeech.Fit(self.m_panelSpeech)
        self.m_simplebookPanelsCategories.AddPage(self.m_panelSpeech, "a page", False)
        self.m_panelNavigation = wx.Panel(
            self.m_simplebookPanelsCategories,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.BORDER_SIMPLE | wx.TAB_TRAVERSAL,
        )
        bSizerNavigation = wx.BoxSizer(wx.VERTICAL)

        sbSizerNavigationMode = wx.StaticBoxSizer(
            wx.StaticBox(
                self.m_panelNavigation,
                wx.ID_ANY,
                # Translators: label for pull down to specify one of three modes use to navigate math expressions
                _("Navigation mode to use when beginning to navigate an equation:"),
            ),
            wx.VERTICAL,
        )

        m_choiceNavigationModeChoices = [
            # Translators: names of different modes of navigation. "Enhanced" mode understands math structure
            _("Enhanced"),
            # Translators: "Simple" walks by character expect for things like fractions, roots, and scripts
            _("Simple"),
            # Translators: "Character" moves around by character, automatically moving into fractions, etc
            _("Character"),
        ]
        self.m_choiceNavigationMode = wx.Choice(
            sbSizerNavigationMode.GetStaticBox(),
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            m_choiceNavigationModeChoices,
            0,
        )
        self.m_choiceNavigationMode.SetSelection(1)
        sbSizerNavigationMode.Add(self.m_choiceNavigationMode, 0, wx.ALL, 5)

        self.m_checkBoxResetNavigationMode = wx.CheckBox(
            sbSizerNavigationMode.GetStaticBox(),
            wx.ID_ANY,
            # Translators: label for checkbox that controls whether any changes to the navigation mode should be preserved
            _("Reset navigation mode on entry to an expression"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        sbSizerNavigationMode.Add(self.m_checkBoxResetNavigationMode, 0, wx.ALL, 5)

        bSizerNavigation.Add(sbSizerNavigationMode, 1, wx.EXPAND, 5)

        sbSizerNavigationSpeech = wx.StaticBoxSizer(
            wx.StaticBox(
                self.m_panelNavigation,
                wx.ID_ANY,
                # Translators: label for pull down to specify whether the expression is spoken or described (an overview)
                _("Navigation speech to use when beginning to navigate an equation:"),
            ),
            wx.VERTICAL,
        )

        # Translators: either "Speak" the expression or give a description (overview) of the expression
        m_choiceNavigationSpeechChoices = [
            # Translators: "Speak" the expression after moving to it
            _("Speak"),
            # Translators: "Describe" the expression after moving to it ("overview is a synonym")
            _("Describe/overview"),
        ]
        self.m_choiceNavigationSpeech = wx.Choice(
            sbSizerNavigationSpeech.GetStaticBox(),
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            m_choiceNavigationSpeechChoices,
            0,
        )
        self.m_choiceNavigationSpeech.SetSelection(1)
        sbSizerNavigationSpeech.Add(self.m_choiceNavigationSpeech, 0, wx.ALL, 5)

        self.m_checkBoxResetNavigationSpeech = wx.CheckBox(
            sbSizerNavigationSpeech.GetStaticBox(),
            wx.ID_ANY,
            # Translators: label for checkbox that controls whether any changes to the speak vs overview reading should be ignored
            _("Reset navigation speech on entry to an expression"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_checkBoxResetNavigationSpeech.SetValue(True)
        sbSizerNavigationSpeech.Add(self.m_checkBoxResetNavigationSpeech, 0, wx.ALL, 5)

        bSizerNavigation.Add(sbSizerNavigationSpeech, 1, wx.EXPAND, 5)

        bSizerNavigationZoom = wx.BoxSizer(wx.VERTICAL)

        self.m_checkBoxAutomaticZoom = wx.CheckBox(
            self.m_panelNavigation,
            wx.ID_ANY,
            # Translators: label for checkbox that controls whether arrow keys move out of fractions, etc.,
            # or whether you have to manually back out of the fraction, etc.
            _("Automatic zoom out of 2D notations"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        bSizerNavigationZoom.Add(self.m_checkBoxAutomaticZoom, 0, wx.ALL, 5)

        bSizerSpeechAmountNavigation = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticTextSpeechAmountNavigation = wx.StaticText(
            self.m_panelNavigation,
            wx.ID_ANY,
            # Translators: label for pull down to specify whether you want a terse or verbose reading of navigation commands
            _("Speech amount for navigation:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticTextSpeechAmountNavigation.Wrap(-1)

        bSizerSpeechAmountNavigation.Add(self.m_staticTextSpeechAmountNavigation, 0, wx.ALL, 5)

        # Translators: options for navigation verbosity.
        m_choiceSpeechAmountNavigationChoices = [
            # Translators: options for navigation verbosity -- "terse" = use less words
            _("Terse"),
            # Translators: options for navigation verbosity -- "medium" = try to be nether too terse nor too verbose words
            _("Medium"),
            # Translators: options for navigation verbosity -- "verbose" = use more words
            _("Verbose"),
        ]
        self.m_choiceSpeechAmountNavigation = wx.Choice(
            self.m_panelNavigation,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            m_choiceSpeechAmountNavigationChoices,
            0,
        )
        self.m_choiceSpeechAmountNavigation.SetSelection(0)
        bSizerSpeechAmountNavigation.Add(self.m_choiceSpeechAmountNavigation, 0, wx.ALL, 5)

        bSizerNavigationZoom.Add(bSizerSpeechAmountNavigation, 1, wx.EXPAND, 5)

        bSizerNavigation.Add(bSizerNavigationZoom, 1, wx.EXPAND, 5)

        bSizerCopyMathAs = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticTextCopyMathAs = wx.StaticText(
            self.m_panelNavigation,
            wx.ID_ANY,
            # Translators: label for pull down to specify how math will be copied to the clipboard
            _("Copy math as:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticTextCopyMathAs.Wrap(-1)

        bSizerCopyMathAs.Add(self.m_staticTextCopyMathAs, 0, wx.ALL, 5)

        # Translators: options for copy math as.
        m_choiceCopyMathAsChoices = [
            # Translators: options for Copy expression to clipboard as -- "MathML"
            _("MathML"),
            # Translators: options for Copy expression to clipboard as -- "LaTeX"
            _("LaTeX"),
            # Translators: options for Copy expression to clipboard as -- "ASCIIMath"
            _("ASCIIMath"),
        ]
        self.m_choiceCopyMathAs = wx.Choice(
            self.m_panelNavigation,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            m_choiceCopyMathAsChoices,
            0,
        )
        self.m_choiceCopyMathAs.SetSelection(0)
        bSizerCopyMathAs.Add(self.m_choiceCopyMathAs, 0, wx.ALL, 5)

        bSizerNavigation.Add(bSizerCopyMathAs, 1, wx.EXPAND, 5)

        self.m_panelNavigation.SetSizer(bSizerNavigation)
        self.m_panelNavigation.Layout()
        bSizerNavigation.Fit(self.m_panelNavigation)
        self.m_simplebookPanelsCategories.AddPage(
            self.m_panelNavigation, "a page", False
        )
        self.m_panelBraille = wx.Panel(
            self.m_simplebookPanelsCategories,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.BORDER_SIMPLE | wx.TAB_TRAVERSAL,
        )
        bSizerBraille = wx.BoxSizer(wx.VERTICAL)

        bSizerBrailleMathCode = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticTextBrailleMathCode = wx.StaticText(
            self.m_panelBraille,
            wx.ID_ANY,
            # Translators: label for pull down to specify which braille code to use
            _("Braille math code for refreshable displays:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticTextBrailleMathCode.Wrap(-1)

        bSizerBrailleMathCode.Add(self.m_staticTextBrailleMathCode, 0, wx.ALL, 5)
        m_choiceBrailleMathCodeChoices = ["xxxxxxxxxxx"]
        self.m_choiceBrailleMathCode = wx.Choice(
            self.m_panelBraille,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            m_choiceBrailleMathCodeChoices,
            0,
        )
        self.m_choiceBrailleMathCode.SetSelection(1)
        bSizerBrailleMathCode.Add(self.m_choiceBrailleMathCode, 0, wx.ALL, 5)

        bSizerBraille.Add(bSizerBrailleMathCode, 1, wx.EXPAND, 5)

        bSizerBrailleHighlights = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticTextBrailleHighlights = wx.StaticText(
            self.m_panelBraille,
            wx.ID_ANY,
            # Translators: label for pull down to specify how braille dots should be modified when navigating/selecting subexprs
            _("Highlight with dots 7 && 8 the current nav node:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticTextBrailleHighlights.Wrap(-1)

        bSizerBrailleHighlights.Add(self.m_staticTextBrailleHighlights, 0, wx.ALL, 5)

        m_choiceBrailleHighlightsChoices = [
            # Translators: options for using dots 7 and 8:
            # Translators: "off" -- don't highlight
            _("Off"),
            # Translators: "First character" -- only the first character of the current navigation node uses dots 7 & 8
            _("First character"),
            # Translators: "Endpoints" -- only the first and last character of the current navigation node uses dots 7 & 8
            _("Endpoints"),
            # Translators: "All" -- all the characters for the current navigation node use dots 7 & 8
            _("All"),
        ]
        self.m_choiceBrailleHighlights = wx.Choice(
            self.m_panelBraille,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            m_choiceBrailleHighlightsChoices,
            0,
        )
        self.m_choiceBrailleHighlights.SetSelection(1)
        bSizerBrailleHighlights.Add(self.m_choiceBrailleHighlights, 0, wx.ALL, 5)

        bSizerBraille.Add(bSizerBrailleHighlights, 1, wx.EXPAND, 5)

        bSizerBraille.Add((0, 0), 1, wx.EXPAND, 5)

        bSizerBraille.Add((0, 0), 1, wx.EXPAND, 5)

        bSizerBraille.Add((0, 0), 1, wx.EXPAND, 5)

        bSizerBraille.Add((0, 0), 1, wx.EXPAND, 5)

        bSizerBraille.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_panelBraille.SetSizer(bSizerBraille)
        self.m_panelBraille.Layout()
        bSizerBraille.Fit(self.m_panelBraille)
        self.m_simplebookPanelsCategories.AddPage(self.m_panelBraille, "a page", False)

        gbSizerMathCATPreferences.Add(
            self.m_simplebookPanelsCategories,
            wx.GBPosition(0, 1),
            wx.GBSpan(1, 1),
            wx.EXPAND | wx.ALL,
            10,
        )

        self.m_staticlineAboveButtons = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        gbSizerMathCATPreferences.Add(
            self.m_staticlineAboveButtons,
            wx.GBPosition(1, 0),
            wx.GBSpan(1, 2),
            wx.EXPAND | wx.ALL,
            5,
        )

        self.m_panelButtons = wx.Panel(self, wx.ID_ANY, wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizerButtons = wx.BoxSizer(wx.HORIZONTAL)

        bSizerButtons.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_buttonOK = wx.Button(
            self.m_panelButtons,
            wx.ID_ANY,
            # Translators: dialog "ok" button
            _("OK"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        bSizerButtons.Add(self.m_buttonOK, 0, wx.ALL, 5)

        self.m_buttonCancel = wx.Button(
            self.m_panelButtons,
            wx.ID_ANY,
            # Translators: dialog "cancel" button
            _("Cancel"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        bSizerButtons.Add(self.m_buttonCancel, 0, wx.ALL, 5)

        self.m_buttonApply = wx.Button(
            self.m_panelButtons,
            wx.ID_ANY,
            # Translators: dialog "apply" button
            _("Apply"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        bSizerButtons.Add(self.m_buttonApply, 0, wx.ALL, 5)

        self.m_buttonReset = wx.Button(
            self.m_panelButtons,
            wx.ID_ANY,
            # Translators: button to reset all the preferences to their default values
            _("Reset to defaults"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        bSizerButtons.Add(self.m_buttonReset, 0, wx.ALL, 5)

        self.m_buttonHelp = wx.Button(
            self.m_panelButtons,
            wx.ID_ANY,
            # Translators: button to bring up a help page
            _("Help"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        bSizerButtons.Add(self.m_buttonHelp, 0, wx.ALL, 5)

        self.m_panelButtons.SetSizer(bSizerButtons)
        self.m_panelButtons.Layout()
        bSizerButtons.Fit(self.m_panelButtons)
        gbSizerMathCATPreferences.Add(
            self.m_panelButtons,
            wx.GBPosition(2, 1),
            wx.GBSpan(1, 2),
            wx.EXPAND | wx.ALL,
            5,
        )

        self.SetSizer(gbSizerMathCATPreferences)
        self.Layout()
        gbSizerMathCATPreferences.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CHAR_HOOK, self.MathCATPreferencesDialogOnCharHook)
        self.Bind(wx.EVT_KEY_UP, self.MathCATPreferencesDialogOnKeyUp)
        self.m_listBoxPreferencesTopic.Bind(wx.EVT_LISTBOX, self.OnListBoxCategories)
        self.m_choiceLanguage.Bind(wx.EVT_CHOICE, self.OnLanguage)
        self.m_sliderRelativeSpeed.Bind(
            wx.EVT_SCROLL_CHANGED, self.OnRelativeSpeedChanged
        )
        self.m_sliderPauseFactor.Bind(wx.EVT_SCROLL_CHANGED, self.OnPauseFactorChanged)
        self.m_buttonOK.Bind(wx.EVT_BUTTON, self.OnClickOK)
        self.m_buttonCancel.Bind(wx.EVT_BUTTON, self.OnClickCancel)
        self.m_buttonApply.Bind(wx.EVT_BUTTON, self.OnClickApply)
        self.m_buttonReset.Bind(wx.EVT_BUTTON, self.OnClickReset)
        self.m_buttonHelp.Bind(wx.EVT_BUTTON, self.OnClickHelp)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def MathCATPreferencesDialogOnCharHook(self, event):
        event.Skip()

    def MathCATPreferencesDialogOnKeyUp(self, event):
        event.Skip()

    def OnListBoxCategories(self, event):
        event.Skip()

    def OnLanguage(self, event):
        event.Skip()

    def OnRelativeSpeedChanged(self, event):
        event.Skip()

    def OnPauseFactorChanged(self, event):
        event.Skip()

    def OnClickOK(self, event):
        event.Skip()

    def OnClickCancel(self, event):
        event.Skip()

    def OnClickApply(self, event):
        event.Skip()

    def OnClickReset(self, event):
        event.Skip()

    def OnClickHelp(self, event):
        event.Skip()
