# MathCAT add-on: generates speech, braille, and allows exploration of expressions written in MathML
# The goal of this add-on is to replicate/improve upon the functionality of MathPlayer which has been discontinued.
# Author: Neil Soiffer
# Copyright: this file is copyright GPL2
#   The code additionally makes use of the MathCAT library (written in Rust) which is covered by the MIT license
#   and also (obviously) requires external speech engines and braille drivers.
#   The plugin also requires the use of a small python dll: python3.dll
#   python3.dll has "Copyright © 2001-2022 Python Software Foundation; All Rights Reserved"


import globalPlugins                        # we are a global plugin
import globalPluginHandler                  # we are a global plugin
import globalVars
from logHandler import log                  # logging
import mathPres                             # math plugin stuff
from gui import mainFrame
import wx

from .MathCAT import MathCAT
from .MathCATPreferences import UserInterface

mathPres.registerProvider(MathCAT(), speech=True, braille=True, interaction=True)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # MathCAT.__init__(self)
        self.add_MathCAT_menu()

    def add_MathCAT_menu(self):
        if not globalVars.appArgs.secure:
            self.preferencesMenu = mainFrame.sysTrayIcon.preferencesMenu
            self.settings = self.preferencesMenu.Append(wx.ID_ANY, _("&MathCAT Settings..."))
            mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.on_settings, self.settings)

    def on_settings(self, evt):
        mainFrame._popupSettingsDialog(UserInterface)

    def terminate(self):
        try:
            if not globalVars.appArgs.secure:
                self.preferencesMenu.Remove(self.settings)
        except (AttributeError, RuntimeError):
            pass

