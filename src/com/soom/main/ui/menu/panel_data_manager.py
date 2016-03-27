import wx

class DataManager(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "탭 페이지: 데이터 관리 영역", (20, 20))