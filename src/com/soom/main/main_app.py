import wx
from ui.main_title import MainTitle
from ui.menu.notebook_menu import NotebookMenu
from db.db_manager import DbManager

class MainApp(wx.Frame):
    def __init__(self):
        db_manager = DbManager()
        db_manager.create_table()

        wx.Frame.__init__(self, parent=None, title="SOOM Lotto Machine")

        # 메인 패널 생성
        self.main_panel = wx.Panel(self)
        self.main_panel_box_sizer = wx.BoxSizer(wx.VERTICAL)

        # 메인 타이틀 생성
        self.main_title = MainTitle(self.main_panel)

        # 메인 메뉴 Notebook 생성
        self.notebook_menu = NotebookMenu(self.main_panel)

        self.__config_main_panel()

    def __config_main_panel(self):
        self.main_panel.SetBackgroundColour(wx.Colour(143, 188, 143, 0))
        self.main_panel.SetSizer(self.main_panel_box_sizer)

        # main 패널의 BoxSizer에 위젯을 추가한다.
        self.main_panel_box_sizer.Add(self.main_title, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        self.main_panel_box_sizer.Add(self.notebook_menu, 1, wx.EXPAND | wx.ALL, 5)



        # class MainApp(wx.Frame):
        #     def __init__(self):
        #         wx.Frame.__init__(self, parent=None, title="SOOM Lotto Machine")
        #

        #          # 메인 메뉴 탭 BoxSizer 생성
        #         self.menu_notebook_panel = wx.Panel(self.main_panel)
        #         self.menu_notebook_sizer = wx.BoxSizer()
        #
        #         # Notebook(탭) 생성
        #         self.notebook = wx.Notebook(self.menu_notebook_panel)
        #
        #         page_manage_data = PageManageData(self.notebook)
        #         self.notebook.AddPage(page_manage_data, "데이터 관리")
        #
        #         page_create_number = PageCreateNumber(self.notebook)
        #         self.notebook.AddPage(page_create_number, "번호 생성")
        #
        #         page_statistic = PageStatistic(self.notebook)
        #         self.notebook.AddPage(page_statistic, "통계")
        #
        #         # 각각의 위젯 영역 설정
        #         self.config_main_panel()
        #         self.config_title()
        #         self.config_menu_tab()
        #

        #
        #     def config_title(self):
        #         font1 = wx.Font(20, wx.SWISS, wx.SLANT, wx.BOLD, False, u'Comic Sans MS')
        #         self.title_text.SetFont(font1)
        #
        #     def config_menu_tab(self):
        #         self.menu_notebook_panel.SetBackgroundColour(wx.YELLOW)
        #         self.menu_notebook_panel.SetSizer(self.menu_notebook_sizer)
        #         self.menu_notebook_sizer.Add(self.notebook, 1, wx.EXPAND)




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

