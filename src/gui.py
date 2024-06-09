# -*- coding: utf-8 -*-

# #########################################################################
# # Python code generated with wxFormBuilder (version 4.1.0-69d57cd9)
# # http://www.wxformbuilder.org/
# #
# # PLEASE DO *NOT* EDIT THIS FILE!
# #########################################################################

import wx
import wx.xrc

ID_CLOSE = 1000
ID_CONFIGURATION = 1001
ID_GET_HELP = 1002
ID_CHECK_FOR_UPDATES = 1003
ID_ABOUT = 1004


# #########################################################################
# # Class MainFrame
# #########################################################################


class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"AWS Manager", pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.menuitemFile = wx.Menu()
        self.menuitemFileClose = wx.MenuItem(self.menuitemFile, ID_CLOSE, u"Close", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemFile.Append(self.menuitemFileClose)

        self.m_menubar1.Append(self.menuitemFile, u"File")

        self.menuItemExtras = wx.Menu()
        self.menuitemExtrasConfiguration = wx.MenuItem(self.menuItemExtras, ID_CONFIGURATION, u"Configuration", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuItemExtras.Append(self.menuitemExtrasConfiguration)

        self.m_menubar1.Append(self.menuItemExtras, u"Extras")

        self.menuitemHelp = wx.Menu()
        self.menuitemHelpSupport = wx.MenuItem(self.menuitemHelp, ID_GET_HELP, u"Support...", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemHelp.Append(self.menuitemHelpSupport)

        self.menuitemHelpUpdate = wx.MenuItem(self.menuitemHelp, ID_CHECK_FOR_UPDATES, u"Check for updates", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemHelp.Append(self.menuitemHelpUpdate)

        self.menuitemHelpAbout = wx.MenuItem(self.menuitemHelp, ID_ABOUT, u"About...", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemHelp.Append(self.menuitemHelpAbout)

        self.m_menubar1.Append(self.menuitemHelp, u"Help")

        self.SetMenuBar(self.m_menubar1)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel1 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_notebook1.AddPage(self.m_panel1, u"a page", False)

        bSizer3.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(bSizer3)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.gicClose)
        self.Bind(wx.EVT_SHOW, self.gicShow)
        self.Bind(wx.EVT_MENU, self.miFileClose, id=self.menuitemFileClose.GetId())
        self.Bind(wx.EVT_MENU, self.miExtrasConfiguration, id=self.menuitemExtrasConfiguration.GetId())
        self.Bind(wx.EVT_MENU, self.miHelpSupport, id=self.menuitemHelpSupport.GetId())
        self.Bind(wx.EVT_MENU, self.miHelpUpdate, id=self.menuitemHelpUpdate.GetId())
        self.Bind(wx.EVT_MENU, self.miHelpAbout, id=self.menuitemHelpAbout.GetId())

    def __del__(self):
        pass
    # Virtual event handlers, override them in your derived class

    def gicClose(self, event):
        event.Skip()

    def gicShow(self, event):
        event.Skip()

    def miFileClose(self, event):
        event.Skip()

    def miExtrasConfiguration(self, event):
        event.Skip()

    def miHelpSupport(self, event):
        event.Skip()

    def miHelpUpdate(self, event):
        event.Skip()

    def miHelpAbout(self, event):
        event.Skip()

# #########################################################################
# # Class dialogConfiguration
# #########################################################################


class dialogConfiguration(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Configuration", pos=wx.DefaultPosition, size=wx.Size(851, 370), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer1 = wx.FlexGridSizer(0, 1, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer2 = wx.FlexGridSizer(0, 1, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"If you provide no AWS credentials here, the default of your general credentials will be used.", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        fgSizer2.Add(self.m_staticText5, 0, wx.ALL, 5)
        fgSizer1.Add(fgSizer2, 1, wx.EXPAND, 5)
        fgSizer3 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"AWS_ACCESS_KEY_ID", wx.DefaultPosition, wx.Size(200, -1), 0)
        self.m_staticText6.Wrap(-1)

        fgSizer3.Add(self.m_staticText6, 0, wx.ALL, 5)
        self.textAwsAccessKeyId = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer3.Add(self.textAwsAccessKeyId, 1, wx.ALL | wx.EXPAND, 5)
        fgSizer1.Add(fgSizer3, 1, wx.EXPAND, 5)
        fgSizer4 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"AWS_SECRET_ACCESS_KEY", wx.DefaultPosition, wx.Size(200, -1), 0)
        self.m_staticText7.Wrap(-1)

        fgSizer4.Add(self.m_staticText7, 0, wx.ALL, 5)
        self.textAwsSecretAccessKey = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer4.Add(self.textAwsSecretAccessKey, 1, wx.ALL | wx.EXPAND, 5)
        fgSizer1.Add(fgSizer4, 1, wx.EXPAND, 5)
        fgSizer5 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer5.AddGrowableCol(1)
        fgSizer5.AddGrowableCol(2)
        fgSizer5.AddGrowableRow(1)
        fgSizer5.SetFlexibleDirection(wx.BOTH)
        fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer5.SetMinSize(wx.Size(-1, 100))
        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"AWS_SESSION_TOKEN", wx.DefaultPosition, wx.Size(200, -1), 0)
        self.m_staticText8.Wrap(-1)

        fgSizer5.Add(self.m_staticText8, 0, wx.ALL, 5)
        self.textAwsSessionToken = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), wx.TE_MULTILINE)
        fgSizer5.Add(self.textAwsSessionToken, 1, wx.ALL | wx.EXPAND, 5)
        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"If session token is provided, please keep in mind, that this will be expire some time!", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        fgSizer5.Add(self.m_staticText9, 1, wx.ALL | wx.EXPAND, 5)
        fgSizer1.Add(fgSizer5, 1, wx.EXPAND, 5)
        fgSizer6 = wx.FlexGridSizer(0, 4, 0, 0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"AWS_PROFILE", wx.DefaultPosition, wx.Size(200, -1), 0)
        self.m_staticText10.Wrap(-1)

        fgSizer6.Add(self.m_staticText10, 0, wx.ALL, 5)
        comboBoxAwsProfileChoices = []
        self.comboBoxAwsProfile = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxAwsProfileChoices, 0)
        fgSizer6.Add(self.comboBoxAwsProfile, 0, wx.ALL, 5)
        self.buttonReloadAwsProfile = wx.Button(self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.buttonReloadAwsProfile, 0, wx.ALL, 5)
        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"If available, select exising profile. After adding new profiles, please reload.", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)

        fgSizer6.Add(self.m_staticText11, 0, wx.ALL, 5)
        fgSizer1.Add(fgSizer6, 1, wx.EXPAND, 5)
        fgSizer7 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer7.SetFlexibleDirection(wx.BOTH)
        fgSizer7.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"AWS_DEFAULT_REGION", wx.DefaultPosition, wx.Size(200, -1), 0)
        self.m_staticText12.Wrap(-1)

        fgSizer7.Add(self.m_staticText12, 0, wx.ALL, 5)
        comboBoxAwsDefaultRegionChoices = []
        self.comboBoxAwsDefaultRegion = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxAwsDefaultRegionChoices, 0)
        fgSizer7.Add(self.comboBoxAwsDefaultRegion, 0, wx.ALL, 5)
        fgSizer1.Add(fgSizer7, 1, wx.EXPAND, 5)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonSave = wx.Button(self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.buttonSave, 0, wx.ALL, 5)
        self.buttonCancel = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.buttonCancel, 0, wx.ALL, 5)
        fgSizer1.Add(bSizer2, 1, wx.EXPAND, 5)
        self.SetSizer(fgSizer1)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_SHOW, self.showConfiguration)
        self.buttonReloadAwsProfile.Bind(wx.EVT_BUTTON, self.reloadAwsProfiles)
        self.buttonSave.Bind(wx.EVT_BUTTON, self.saveConfig)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.cancelConfig)

    def __del__(self):
        pass
    # Virtual event handlers, override them in your derived class

    def showConfiguration(self, event):
        event.Skip()

    def reloadAwsProfiles(self, event):
        event.Skip()

    def saveConfig(self, event):
        event.Skip()

    def cancelConfig(self, event):
        event.Skip()

# #########################################################################
# # Class dialogAbout
# #########################################################################


class dialogAbout(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"About AWS Manager", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.bitmapLogo = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.bitmapLogo, 0, wx.ALL, 5)
        self.staticTextName = wx.StaticText(self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextName.Wrap(-1)

        bSizer2.Add(self.staticTextName, 0, wx.ALL, 5)
        self.staticTextLicence = wx.StaticText(self, wx.ID_ANY, u"Licenced under", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextLicence.Wrap(-1)

        bSizer2.Add(self.staticTextLicence, 0, wx.ALL, 5)
        self.staticTextGithub = wx.StaticText(self, wx.ID_ANY, u"More on GitHub", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextGithub.Wrap(-1)

        self.staticTextGithub.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString))
        self.staticTextGithub.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer2.Add(self.staticTextGithub, 0, wx.ALL, 5)
        self.staticTextIcon8 = wx.StaticText(self, wx.ID_ANY, u"Icons by Icons8.com", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextIcon8.Wrap(-1)

        self.staticTextIcon8.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT))

        bSizer2.Add(self.staticTextIcon8, 0, wx.ALL, 5)
        m_sdbSizer2 = wx.StdDialogButtonSizer()
        self.m_sdbSizer2OK = wx.Button(self, wx.ID_OK)
        m_sdbSizer2.AddButton(self.m_sdbSizer2OK)
        self.m_sdbSizer2Cancel = wx.Button(self, wx.ID_CANCEL)
        m_sdbSizer2.AddButton(self.m_sdbSizer2Cancel)
        m_sdbSizer2.Realize()
        bSizer2.Add(m_sdbSizer2, 1, wx.EXPAND, 5)
        self.SetSizer(bSizer2)
        self.Layout()
        bSizer2.Fit(self)
        self.Centre(wx.BOTH)

        # Connect Events
        self.staticTextGithub.Bind(wx.EVT_LEFT_DOWN, self.openGithub)
        self.staticTextIcon8.Bind(wx.EVT_LEFT_DOWN, self.openIcons8)

    def __del__(self):
        pass
    # Virtual event handlers, override them in your derived class

    def openGithub(self, event):
        event.Skip()

    def openIcons8(self, event):
        event.Skip()
