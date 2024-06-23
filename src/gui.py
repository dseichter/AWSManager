# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

ID_CLOSE = 6000
ID_CONFIGURATION = 6001
ID_GET_HELP = 6002
ID_CHECK_FOR_UPDATES = 6003
ID_ABOUT = 6004

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"AWS Manager", pos = wx.DefaultPosition, size = wx.Size( 746,409 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.menuitemFile = wx.Menu()
        self.menuitemFileClose = wx.MenuItem( self.menuitemFile, ID_CLOSE, u"Close", wx.EmptyString, wx.ITEM_NORMAL )
        self.menuitemFile.Append( self.menuitemFileClose )

        self.m_menubar1.Append( self.menuitemFile, u"File" )

        self.menuItemExtras = wx.Menu()
        self.menuitemExtrasConfiguration = wx.MenuItem( self.menuItemExtras, ID_CONFIGURATION, u"Configuration", wx.EmptyString, wx.ITEM_NORMAL )
        self.menuItemExtras.Append( self.menuitemExtrasConfiguration )

        self.m_menubar1.Append( self.menuItemExtras, u"Extras" )

        self.menuitemHelp = wx.Menu()
        self.menuitemHelpSupport = wx.MenuItem( self.menuitemHelp, ID_GET_HELP, u"Support...", wx.EmptyString, wx.ITEM_NORMAL )
        self.menuitemHelp.Append( self.menuitemHelpSupport )

        self.menuitemHelpUpdate = wx.MenuItem( self.menuitemHelp, ID_CHECK_FOR_UPDATES, u"Check for updates", wx.EmptyString, wx.ITEM_NORMAL )
        self.menuitemHelp.Append( self.menuitemHelpUpdate )

        self.menuitemHelpAbout = wx.MenuItem( self.menuitemHelp, ID_ABOUT, u"About...", wx.EmptyString, wx.ITEM_NORMAL )
        self.menuitemHelp.Append( self.menuitemHelpAbout )

        self.m_menubar1.Append( self.menuitemHelp, u"Help" )

        self.SetMenuBar( self.m_menubar1 )

        gSizer1 = wx.GridSizer( 0, 1, 0, 0 )

        self.m_auinotebook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_WINDOWLIST_BUTTON )
        self.panelEC2 = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.m_splitter1 = wx.SplitterWindow( self.panelEC2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_BORDER )
        self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )

        self.m_panel11 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_treeCtrl1 = wx.TreeCtrl( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        bSizer4.Add( self.m_treeCtrl1, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_button4 = wx.Button( self.m_panel11, wx.ID_ANY, u"Reload EC2 Instances", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button4, 0, wx.ALL, 5 )


        self.m_panel11.SetSizer( bSizer4 )
        self.m_panel11.Layout()
        bSizer4.Fit( self.m_panel11 )
        self.m_panel15 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_splitter1.SplitVertically( self.m_panel11, self.m_panel15, 0 )
        bSizer8.Add( self.m_splitter1, 1, wx.EXPAND, 5 )


        self.panelEC2.SetSizer( bSizer8 )
        self.panelEC2.Layout()
        bSizer8.Fit( self.panelEC2 )
        self.m_auinotebook1.AddPage( self.panelEC2, u"EC2", False, wx.NullBitmap )
        self.panelLambda = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_splitter3 = wx.SplitterWindow( self.panelLambda, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
        self.m_splitter3.Bind( wx.EVT_IDLE, self.m_splitter3OnIdle )

        self.m_panel12 = wx.Panel( self.m_splitter3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        self.m_treeCtrl3 = wx.TreeCtrl( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        bSizer7.Add( self.m_treeCtrl3, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_button5 = wx.Button( self.m_panel12, wx.ID_ANY, u"Reload Lambda Functions", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_button5, 0, wx.ALL, 5 )


        self.m_panel12.SetSizer( bSizer7 )
        self.m_panel12.Layout()
        bSizer7.Fit( self.m_panel12 )
        self.m_panel13 = wx.Panel( self.m_splitter3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_splitter3.SplitVertically( self.m_panel12, self.m_panel13, 0 )
        bSizer3.Add( self.m_splitter3, 1, wx.EXPAND, 5 )


        self.panelLambda.SetSizer( bSizer3 )
        self.panelLambda.Layout()
        bSizer3.Fit( self.panelLambda )
        self.m_auinotebook1.AddPage( self.panelLambda, u"Lambda", False, wx.NullBitmap )
        self.panelS3 = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer81 = wx.BoxSizer( wx.VERTICAL )

        self.m_splitter11 = wx.SplitterWindow( self.panelS3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
        self.m_splitter11.Bind( wx.EVT_IDLE, self.m_splitter11OnIdle )

        self.m_panel111 = wx.Panel( self.m_splitter11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer41 = wx.BoxSizer( wx.VERTICAL )

        self.m_treeCtrl11 = wx.TreeCtrl( self.m_panel111, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        bSizer41.Add( self.m_treeCtrl11, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_button6 = wx.Button( self.m_panel111, wx.ID_ANY, u"Reload S3 Buckets", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer41.Add( self.m_button6, 0, wx.ALL, 5 )


        self.m_panel111.SetSizer( bSizer41 )
        self.m_panel111.Layout()
        bSizer41.Fit( self.m_panel111 )
        self.m_panel151 = wx.Panel( self.m_splitter11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_splitter11.SplitVertically( self.m_panel111, self.m_panel151, 0 )
        bSizer81.Add( self.m_splitter11, 1, wx.EXPAND, 5 )


        self.panelS3.SetSizer( bSizer81 )
        self.panelS3.Layout()
        bSizer81.Fit( self.panelS3 )
        self.m_auinotebook1.AddPage( self.panelS3, u"S3", False, wx.NullBitmap )
        self.panelRDS = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer82 = wx.BoxSizer( wx.VERTICAL )

        self.m_splitter12 = wx.SplitterWindow( self.panelRDS, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
        self.m_splitter12.Bind( wx.EVT_IDLE, self.m_splitter12OnIdle )

        self.m_panel112 = wx.Panel( self.m_splitter12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer42 = wx.BoxSizer( wx.VERTICAL )

        self.m_treeCtrl12 = wx.TreeCtrl( self.m_panel112, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        bSizer42.Add( self.m_treeCtrl12, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_button7 = wx.Button( self.m_panel112, wx.ID_ANY, u"Reload RDS Instances", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer42.Add( self.m_button7, 0, wx.ALL, 5 )


        self.m_panel112.SetSizer( bSizer42 )
        self.m_panel112.Layout()
        bSizer42.Fit( self.m_panel112 )
        self.m_panel152 = wx.Panel( self.m_splitter12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_splitter12.SplitVertically( self.m_panel112, self.m_panel152, 0 )
        bSizer82.Add( self.m_splitter12, 1, wx.EXPAND, 5 )


        self.panelRDS.SetSizer( bSizer82 )
        self.panelRDS.Layout()
        bSizer82.Fit( self.panelRDS )
        self.m_auinotebook1.AddPage( self.panelRDS, u"RDS", False, wx.NullBitmap )
        self.panelCloudfront = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer83 = wx.BoxSizer( wx.VERTICAL )

        self.m_splitter13 = wx.SplitterWindow( self.panelCloudfront, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
        self.m_splitter13.Bind( wx.EVT_IDLE, self.m_splitter13OnIdle )

        self.m_panel113 = wx.Panel( self.m_splitter13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer43 = wx.BoxSizer( wx.VERTICAL )

        self.m_treeCtrl13 = wx.TreeCtrl( self.m_panel113, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        bSizer43.Add( self.m_treeCtrl13, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_button8 = wx.Button( self.m_panel113, wx.ID_ANY, u"Reload Cloudfront Distributions", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer43.Add( self.m_button8, 0, wx.ALL, 5 )


        self.m_panel113.SetSizer( bSizer43 )
        self.m_panel113.Layout()
        bSizer43.Fit( self.m_panel113 )
        self.m_panel153 = wx.Panel( self.m_splitter13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_splitter13.SplitVertically( self.m_panel113, self.m_panel153, 0 )
        bSizer83.Add( self.m_splitter13, 1, wx.EXPAND, 5 )


        self.panelCloudfront.SetSizer( bSizer83 )
        self.panelCloudfront.Layout()
        bSizer83.Fit( self.panelCloudfront )
        self.m_auinotebook1.AddPage( self.panelCloudfront, u"Cloudfront", False, wx.NullBitmap )

        gSizer1.Add( self.m_auinotebook1, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( gSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.gicClose )
        self.Bind( wx.EVT_SHOW, self.gicShow )
        self.Bind( wx.EVT_MENU, self.miFileClose, id = self.menuitemFileClose.GetId() )
        self.Bind( wx.EVT_MENU, self.miExtrasConfiguration, id = self.menuitemExtrasConfiguration.GetId() )
        self.Bind( wx.EVT_MENU, self.miHelpSupport, id = self.menuitemHelpSupport.GetId() )
        self.Bind( wx.EVT_MENU, self.miHelpUpdate, id = self.menuitemHelpUpdate.GetId() )
        self.Bind( wx.EVT_MENU, self.miHelpAbout, id = self.menuitemHelpAbout.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def gicClose( self, event ):
        event.Skip()

    def gicShow( self, event ):
        event.Skip()

    def miFileClose( self, event ):
        event.Skip()

    def miExtrasConfiguration( self, event ):
        event.Skip()

    def miHelpSupport( self, event ):
        event.Skip()

    def miHelpUpdate( self, event ):
        event.Skip()

    def miHelpAbout( self, event ):
        event.Skip()

    def m_splitter1OnIdle( self, event ):
        self.m_splitter1.SetSashPosition( 0 )
        self.m_splitter1.Unbind( wx.EVT_IDLE )

    def m_splitter3OnIdle( self, event ):
        self.m_splitter3.SetSashPosition( 0 )
        self.m_splitter3.Unbind( wx.EVT_IDLE )

    def m_splitter11OnIdle( self, event ):
        self.m_splitter11.SetSashPosition( 0 )
        self.m_splitter11.Unbind( wx.EVT_IDLE )

    def m_splitter12OnIdle( self, event ):
        self.m_splitter12.SetSashPosition( 0 )
        self.m_splitter12.Unbind( wx.EVT_IDLE )

    def m_splitter13OnIdle( self, event ):
        self.m_splitter13.SetSashPosition( 0 )
        self.m_splitter13.Unbind( wx.EVT_IDLE )


###########################################################################
## Class dialogConfiguration
###########################################################################

class dialogConfiguration ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Configuration", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        fgSizer1 = wx.FlexGridSizer( 0, 1, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        fgSizer2 = wx.FlexGridSizer( 0, 1, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"If you provide no AWS credentials here, the default of your general credentials will be used.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        fgSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )


        fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )

        fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"AWS_ACCESS_KEY_ID", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_staticText6.Wrap( -1 )

        fgSizer3.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.textAwsAccessKeyId = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.textAwsAccessKeyId, 1, wx.ALL|wx.EXPAND, 5 )


        fgSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )

        fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer4.SetFlexibleDirection( wx.BOTH )
        fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"AWS_SECRET_ACCESS_KEY", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_staticText7.Wrap( -1 )

        fgSizer4.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.textAwsSecretAccessKey = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer4.Add( self.textAwsSecretAccessKey, 1, wx.ALL|wx.EXPAND, 5 )


        fgSizer1.Add( fgSizer4, 1, wx.EXPAND, 5 )

        fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
        fgSizer5.AddGrowableCol( 1 )
        fgSizer5.AddGrowableRow( 0 )
        fgSizer5.SetFlexibleDirection( wx.BOTH )
        fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        fgSizer5.SetMinSize( wx.Size( -1,100 ) )
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"AWS_SESSION_TOKEN", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_staticText8.Wrap( -1 )

        fgSizer5.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.textAwsSessionToken = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TE_MULTILINE )
        fgSizer5.Add( self.textAwsSessionToken, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"If session token is provided, please keep in mind, that this will be expire some time!", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        fgSizer5.Add( self.m_staticText9, 1, wx.ALL|wx.EXPAND, 5 )


        fgSizer1.Add( fgSizer5, 1, wx.EXPAND, 5 )

        fgSizer6 = wx.FlexGridSizer( 0, 4, 0, 0 )
        fgSizer6.SetFlexibleDirection( wx.BOTH )
        fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"AWS_PROFILE", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_staticText10.Wrap( -1 )

        fgSizer6.Add( self.m_staticText10, 0, wx.ALL, 5 )

        comboBoxAwsProfileChoices = []
        self.comboBoxAwsProfile = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxAwsProfileChoices, 0 )
        fgSizer6.Add( self.comboBoxAwsProfile, 0, wx.ALL, 5 )

        self.buttonReloadAwsProfile = wx.Button( self, wx.ID_ANY, u"Reload profiles", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer6.Add( self.buttonReloadAwsProfile, 0, wx.ALL, 5 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"If available, select exising profile. After adding new profiles, please reload.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        fgSizer6.Add( self.m_staticText11, 0, wx.ALL, 5 )


        fgSizer1.Add( fgSizer6, 1, wx.EXPAND, 5 )

        fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer7.SetFlexibleDirection( wx.BOTH )
        fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"AWS_DEFAULT_REGION", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_staticText12.Wrap( -1 )

        fgSizer7.Add( self.m_staticText12, 0, wx.ALL, 5 )

        comboBoxAwsDefaultRegionChoices = []
        self.comboBoxAwsDefaultRegion = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxAwsDefaultRegionChoices, 0 )
        fgSizer7.Add( self.comboBoxAwsDefaultRegion, 0, wx.ALL, 5 )


        fgSizer1.Add( fgSizer7, 1, wx.EXPAND, 5 )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.buttonSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.buttonSave, 0, wx.ALL, 5 )

        self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.buttonCancel, 0, wx.ALL, 5 )


        fgSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


        self.SetSizer( fgSizer1 )
        self.Layout()
        fgSizer1.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.buttonReloadAwsProfile.Bind( wx.EVT_BUTTON, self.reloadAwsProfiles )
        self.buttonSave.Bind( wx.EVT_BUTTON, self.saveConfig )
        self.buttonCancel.Bind( wx.EVT_BUTTON, self.cancelConfig )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def reloadAwsProfiles( self, event ):
        event.Skip()

    def saveConfig( self, event ):
        event.Skip()

    def cancelConfig( self, event ):
        event.Skip()


###########################################################################
## Class dialogAbout
###########################################################################

class dialogAbout ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About AWS Manager", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.bitmapLogo = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.bitmapLogo, 0, wx.ALL, 5 )

        self.staticTextName = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextName.Wrap( -1 )

        bSizer2.Add( self.staticTextName, 0, wx.ALL, 5 )

        self.staticTextLicence = wx.StaticText( self, wx.ID_ANY, u"Licenced under", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextLicence.Wrap( -1 )

        bSizer2.Add( self.staticTextLicence, 0, wx.ALL, 5 )

        self.staticTextGithub = wx.StaticText( self, wx.ID_ANY, u"More on GitHub", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextGithub.Wrap( -1 )

        self.staticTextGithub.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
        self.staticTextGithub.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

        bSizer2.Add( self.staticTextGithub, 0, wx.ALL, 5 )

        self.staticTextIcon8 = wx.StaticText( self, wx.ID_ANY, u"Icons by Icons8.com", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextIcon8.Wrap( -1 )

        self.staticTextIcon8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

        bSizer2.Add( self.staticTextIcon8, 0, wx.ALL, 5 )

        self.staticTextIcon9 = wx.StaticText( self, wx.ID_ANY, u"AWS Icons by Amazon Web Services Inc.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextIcon9.Wrap( -1 )

        self.staticTextIcon9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

        bSizer2.Add( self.staticTextIcon9, 0, wx.ALL, 5 )

        m_sdbSizer2 = wx.StdDialogButtonSizer()
        self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
        self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
        m_sdbSizer2.Realize()

        bSizer2.Add( m_sdbSizer2, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer2 )
        self.Layout()
        bSizer2.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.staticTextGithub.Bind( wx.EVT_LEFT_DOWN, self.openGithub )
        self.staticTextIcon8.Bind( wx.EVT_LEFT_DOWN, self.openIcons8 )
        self.staticTextIcon9.Bind( wx.EVT_LEFT_DOWN, self.openIconsAWS )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def openGithub( self, event ):
        event.Skip()

    def openIcons8( self, event ):
        event.Skip()

    def openIconsAWS( self, event ):
        event.Skip()


