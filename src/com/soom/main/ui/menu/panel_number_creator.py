import wx

class NumberCreator(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "탭 페이지: 번호 생성 영역", (20, 20))