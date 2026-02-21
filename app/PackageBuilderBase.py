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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"KiCad Plugin Builder"), pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, _(u"Metadata File") ), wx.HORIZONTAL )

        self.m_filePicker1 = wx.FilePickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.json"), wx.DefaultPosition, wx.Size( 500,-1 ), wx.FLP_DEFAULT_STYLE )
        sbSizer1.Add( self.m_filePicker1, 0, wx.ALL, 5 )


        bSizer2.Add( sbSizer1, 1, wx.EXPAND, 5 )

        sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, _(u"Source Folder") ), wx.VERTICAL )

        self.m_dirPicker1 = wx.DirPickerCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, _(u"Select a folder"), wx.DefaultPosition, wx.Size( 500,-1 ), wx.DIRP_DEFAULT_STYLE )
        sbSizer11.Add( self.m_dirPicker1, 0, wx.ALL, 5 )


        bSizer2.Add( sbSizer11, 1, wx.EXPAND, 5 )

        sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, _(u"Icon File") ), wx.VERTICAL )

        self.m_filePicker12 = wx.FilePickerCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.Size( 500,-1 ), wx.FLP_DEFAULT_STYLE )
        sbSizer5.Add( self.m_filePicker12, 0, wx.ALL, 5 )


        bSizer2.Add( sbSizer5, 1, wx.EXPAND, 5 )

        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button3 = wx.Button( self.m_panel1, wx.ID_ANY, _(u"CLEAN"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button3, 0, wx.ALL, 5 )

        self.button_build = wx.Button( self.m_panel1, wx.ID_ANY, _(u"BUILD"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.button_build, 0, wx.ALL, 5 )


        bSizer2.Add( bSizer11, 1, wx.EXPAND, 5 )


        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_WORDWRAP )
        bSizer9.Add( self.m_textCtrl1, 0, wx.EXPAND|wx.SHAPED, 5 )


        bSizer1.Add( bSizer9, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        bSizer1.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.e_metadata_file_select )
        self.m_dirPicker1.Bind( wx.EVT_DIRPICKER_CHANGED, self.e_src_folder_select )
        self.m_filePicker12.Bind( wx.EVT_FILEPICKER_CHANGED, self.e_icon_file_select )
        self.m_button3.Bind( wx.EVT_BUTTON, self.e_button_clean )
        self.button_build.Bind( wx.EVT_BUTTON, self.e_button_build )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def e_metadata_file_select( self, event ):
        event.Skip()

    def e_src_folder_select( self, event ):
        event.Skip()

    def e_icon_file_select( self, event ):
        event.Skip()

    def e_button_clean( self, event ):
        event.Skip()

    def e_button_build( self, event ):
        event.Skip()


