import wx
from db.connection_provider import ConnectionProvider

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

        # 번호 입력 구분 패널
        panel_number_input_type = wx.Panel(self)
        panel_number_input_type_sizer = wx.StaticBoxSizer(wx.HORIZONTAL, panel_number_input_type, "입력 구분")
        panel_number_input_type.SetSizer(panel_number_input_type_sizer)

        # 입력 구분 라디오 버튼 그룹
        radio_number_input_single = wx.RadioButton(panel_number_input_type, label="단건 입력", style=wx.RB_GROUP)
        radio_number_input_batch = wx.RadioButton(panel_number_input_type, label="일괄 등록")

        # 입력 구분 sizer에 라디오 버튼 그룹 추가
        panel_number_input_type_sizer.Add(radio_number_input_single, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        panel_number_input_type_sizer.Add(radio_number_input_batch, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        # 번호 입력 TextCtrl 패널
        panel_number_combobox = wx.Panel(self)
        panel_number_combobox_sizer = wx.BoxSizer(wx.HORIZONTAL)
        panel_number_combobox.SetSizer(panel_number_combobox_sizer)

        number_list = []
        for number in range(1,45):
            number_list.append(str(number))

        inital_value = "select number"

        # 번호 입력 ComboBox
        combobox_number_first = wx.ComboBox(panel_number_combobox, id=0, value=inital_value, choices=number_list, size=wx.Size(100, 30))
        combobox_number_second = wx.ComboBox(panel_number_combobox, id=1, value=inital_value, choices=number_list, size=wx.Size(100, 30))
        combobox_number_third = wx.ComboBox(panel_number_combobox, id=2, value=inital_value, choices=number_list, size=wx.Size(100, 30))
        combobox_number_fourth = wx.ComboBox(panel_number_combobox, id=3, value=inital_value, choices=number_list, size=wx.Size(100, 30))
        combobox_number_fifth = wx.ComboBox(panel_number_combobox, id=4, value=inital_value, choices=number_list, size=wx.Size(100, 30))
        combobox_number_sixth = wx.ComboBox(panel_number_combobox, id=5, value=inital_value, choices=number_list, size=wx.Size(100, 30))

        # 번호 저장 버튼
        button_save_number = wx.Button(panel_number_combobox, id=0, label="저장")

        # 번호 입력 ComboBox sizer에 ComboBox 추가
        panel_number_combobox_sizer.Add(combobox_number_first, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        panel_number_combobox_sizer.Add(combobox_number_second, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        panel_number_combobox_sizer.Add(combobox_number_third, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        panel_number_combobox_sizer.Add(combobox_number_fourth, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        panel_number_combobox_sizer.Add(combobox_number_fifth, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        panel_number_combobox_sizer.Add(combobox_number_sixth, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        panel_number_combobox_sizer.Add(button_save_number, 0, wx.ALIGN_LEFT | wx.ALL, 10)

        button_save_number.Bind(wx.EVT_BUTTON, self.save_number)

        # 데이터 관리 sizer에 번호 타입 패널을 추가
        panel_data_manager_sizer.Add(panel_number_type, 0, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 15)
        panel_data_manager_sizer.Add(panel_number_input_type, 0, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 15)
        panel_data_manager_sizer.Add(panel_number_combobox, 0, wx.ALIGN_LEFT | wx.ALL, 15)

    def save_number(self, event):
        print("번호 저장..")
