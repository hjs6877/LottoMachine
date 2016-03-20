import wx


class MainApp(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="SOOM Lotto")


if __name__ == '__main__':
    app = wx.App()
    frame = MainApp()

    frame.Show()

    app.MainLoop()

