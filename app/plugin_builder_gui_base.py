# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Kicad Plugin Builder"), pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"MyMenuItem"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem1 )

        self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"MyMenuItem"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem2 )

        self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"MyMenuItem"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem3 )

        self.m_menubar1.Append( self.m_menu1, _(u"MyMenu") )

        self.m_menu2 = wx.Menu()
        self.m_menuItem4 = wx.MenuItem( self.m_menu2, wx.ID_ANY, _(u"MyMenuItem"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.Append( self.m_menuItem4 )

        self.m_menuItem5 = wx.MenuItem( self.m_menu2, wx.ID_ANY, _(u"MyMenuItem"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.Append( self.m_menuItem5 )

        self.m_menubar1.Append( self.m_menu2, _(u"about") )

        self.SetMenuBar( self.m_menubar1 )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.MainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.MainPanel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.MainPanel, wx.ID_ANY, _(u"JSON file") ), wx.HORIZONTAL )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )


        sbSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

        self.m_filePicker1 = wx.FilePickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.json"), wx.DefaultPosition, wx.Size( -1,-1 ), wx.FLP_DEFAULT_STYLE )
        sbSizer1.Add( self.m_filePicker1, 0, wx.ALL, 5 )

        self.validate_button = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"Validate"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer1.Add( self.validate_button, 0, wx.ALL, 5 )


        self.MainPanel.SetSizer( sbSizer1 )
        self.MainPanel.Layout()
        sbSizer1.Fit( self.MainPanel )
        bSizer3.Add( self.MainPanel, 1, wx.SHAPED, 5 )

        sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"label") ), wx.HORIZONTAL )

        self.m_dirPicker1 = wx.DirPickerCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, _(u"Select a folder"), wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        sbSizer3.Add( self.m_dirPicker1, 0, wx.ALL, 5 )

        self.m_toggleBtn1 = wx.ToggleButton( sbSizer3.GetStaticBox(), wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer3.Add( self.m_toggleBtn1, 0, wx.ALL, 5 )


        bSizer3.Add( sbSizer3, 1, wx.EXPAND, 5 )

        sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Output") ), wx.VERTICAL )

        self.m_textCtrl1 = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,200 ), wx.TE_MULTILINE|wx.BORDER_NONE )
        sbSizer4.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 2 )


        bSizer3.Add( sbSizer4, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer3 )
        self.Layout()
        bSizer3.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.validate_button.Bind( wx.EVT_BUTTON, self.on_validate )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_validate( self, event ):
        event.Skip()


