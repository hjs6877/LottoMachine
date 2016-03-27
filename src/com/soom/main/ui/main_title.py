import wx

class MainTitle(wx.StaticText):
    def __init__(self, parent):
        wx.StaticText.__init__(self, parent, label="SOOM Lotto Machine")
        self.__config_title()

    def __config_title(self):
        font = wx.Font(20, wx.SWISS, wx.SLANT, wx.BOLD, False, u'Comic Sans MS')
        self.SetFont(font)