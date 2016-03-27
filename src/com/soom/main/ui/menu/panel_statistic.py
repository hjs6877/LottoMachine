import wx

class Statistic(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "탭 페이지: 통계 영역", (20, 20))
