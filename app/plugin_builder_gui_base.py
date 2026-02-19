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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Kicad Plugin Builder"), pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"JSON file") ), wx.HORIZONTAL )

        self.m_filePicker1 = wx.FilePickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.json"), wx.DefaultPosition, wx.Size( -1,-1 ), wx.FLP_DEFAULT_STYLE )
        sbSizer1.Add( self.m_filePicker1, 0, wx.ALL, 5 )

        self.validate_button = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"Validate"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer1.Add( self.validate_button, 0, wx.ALL, 5 )


        bSizer3.Add( sbSizer1, 1, wx.EXPAND, 5 )

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

        self.Centre( wx.BOTH )

        # Connect Events
        self.validate_button.Bind( wx.EVT_BUTTON, self.on_validate )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_validate( self, event ):
        event.Skip()


