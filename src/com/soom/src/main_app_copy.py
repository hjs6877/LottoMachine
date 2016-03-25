import wx


class MainApp(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="SOOM Lotto Machine")

        # 메인 패널 생성
        # 메인 패널에 BoxSizer를 설정.
        self.main_panel = wx.Panel(self)
        self.main_panel_box_sizer = wx.BoxSizer(wx.VERTICAL)

        # title 생성
        self.title_text = wx.StaticText(self.main_panel, label="SOOM Lotto Machine")

        # 메인 메뉴 버튼 BoxSizer 생성
        self.menu_panel = wx.Panel(self.main_panel)
        self.menu_button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # 버튼 생성(메인 메뉴 버튼/번호 생성 버튼/통계 버튼)
        self.manage_data_button = wx.Button(self.menu_panel, label="데이터 관리")
        self.create_number_button = wx.Button(self.menu_panel, label="번호 생성")
        self.statistic_button = wx.Button(self.menu_panel, label="통계")

        # 컨텐츠 영역
        self.manage_data_panel = wx.Panel(self.main_panel)
        self.manage_data_sizer = wx.StaticBoxSizer(wx.VERTICAL, self.manage_data_panel, "데이터 관리")

        # 데이터 관리 > 테스트 텍스트
        self.manage_data_text = wx.StaticText(self.manage_data_panel, label="데이터 관리 테스트 텍스트")

        # 각각의 위젯 영역 설정
        self.config_main_panel()
        self.config_title()
        self.config_menu_button()
        self.config_manage_data_box()

    def config_main_panel(self):
        self.main_panel.SetBackgroundColour(wx.Colour(143, 188, 143, 0))
        self.main_panel.SetSizer(self.main_panel_box_sizer)
        # src 패널의 BoxSizer에 타이틀 위젯을 추가한다.
        self.main_panel_box_sizer.Add(self.title_text, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        # src 패널의 BoxSizer에 메뉴 패널 위젯을 추가한다.
        self.main_panel_box_sizer.Add(self.menu_panel, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        # src 패널의 BoxSizer에 데이터 관리 패널 위젯을 추가한다.
        self.main_panel_box_sizer.Add(self.manage_data_panel, 1, wx.EXPAND | wx.ALL, 10)

    def config_title(self):
        font1 = wx.Font(20, wx.SWISS, wx.SLANT, wx.BOLD, False, u'Comic Sans MS')
        self.title_text.SetFont(font1)

    def config_menu_button(self):
        self.menu_panel.SetSizer(self.menu_button_sizer)
        self.menu_button_sizer.Add(self.manage_data_button, 0, wx.ALL, 20)
        self.menu_button_sizer.Add(self.create_number_button, 0, wx.ALL, 20)
        self.menu_button_sizer.Add(self.statistic_button, 0, wx.ALL, 20)
        # self.Bind(wx.EVT_CLOSE, self.on_close)

    def config_manage_data_box(self):
        self.manage_data_panel.SetSizer(self.manage_data_sizer)
        self.manage_data_sizer.Add(self.manage_data_text)

    # def on_close(self, event):
    #     if wx.MessageBox("프로그램을 종료할까요?"
    #                      , "확인"
    #                      , wx.YES_NO) != wx.YES:
    #         event.Skip(False)
    #     else:
    #         self.Destroy()

if __name__ == '__main__':
    app = wx.App()
    frame = MainApp()

    frame.SetSize(wx.Size(1024, 768))
    # frame.SetBackgroundColour(wx.Colour(220, 220, 220, 0))

    frame.Show()

    app.MainLoop()

