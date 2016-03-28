import wx

class DataManager(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        panel_data_manager_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(panel_data_manager_sizer)

        # 번호 타입 라디오 버튼 그룹을 담는 패널
        panel_number_type = wx.Panel(self)
        panel_number_type_sizer = wx.StaticBoxSizer(wx.HORIZONTAL, panel_number_type, "입력번호 타입")
        panel_number_type.SetSizer(panel_number_type_sizer)

        # 번호 타입 라디오 버튼 그룹
        radio_number_buy = wx.RadioButton(panel_number_type, label="구매 번호", style=wx.RB_GROUP)
        radio_number_win = wx.RadioButton(panel_number_type, label="당첨 번호")

        # 번호 타입 sizer에 라디오 버튼 그룹 추가
        panel_number_type_sizer.Add(radio_number_buy, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        panel_number_type_sizer.Add(radio_number_win, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        # 번호 입력 구분
        panel_number_input_type = wx.Panel(self)
        panel_number_input_type_sizer = wx.StaticBoxSizer(wx.HORIZONTAL, panel_number_input_type, "입력 구분")
        panel_number_input_type.SetSizer(panel_number_input_type_sizer)

        # 입력 구분 라디오 버튼 그룹
        radio_number_input_single = wx.RadioButton(panel_number_input_type, label="단건 입력", style=wx.RB_GROUP)
        radio_number_input_batch = wx.RadioButton(panel_number_input_type, label="일괄 등록")

        # 입력 구분 sizer에 라디오 버튼 그룹 추가
        panel_number_input_type_sizer.Add(radio_number_input_single, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        panel_number_input_type_sizer.Add(radio_number_input_batch, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        # 데이터 관리 sizer에 번호 타입 패널을 추가
        panel_data_manager_sizer.Add(panel_number_type, 0, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 15)
        panel_data_manager_sizer.Add(panel_number_input_type, 0, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 15)
