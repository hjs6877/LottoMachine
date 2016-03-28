import wx
from panel_data_manager import DataManager
from panel_number_creator import NumberCreator
from panel_statistic import Statistic

class NotebookMenu(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.__config_notebook_menu()

    def __config_notebook_menu(self):
        # TODO notebook을 NotebookMenu 패널에서 분리 할 필요가 있음.
        notebook = wx.Notebook(self)
        data_manager = DataManager(notebook)

        number_creator = NumberCreator(notebook)
        statistic = Statistic(notebook)

        notebook.AddPage(data_manager, "데이터 관리")
        notebook.AddPage(number_creator, "번호 생성")
        notebook.AddPage(statistic, "통계")

        notebook_box_sizer = wx.BoxSizer()
        notebook_box_sizer.Add(notebook, 1, wx.EXPAND)

        self.SetSizer(notebook_box_sizer)
        self.SetBackgroundColour(wx.YELLOW)

