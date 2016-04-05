import wx
import wx.adv

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
        radio_number_win = wx.RadioButton(panel_number_type, label="당첨 번호", style=wx.RB_GROUP)
        radio_number_buy = wx.RadioButton(panel_number_type, label="구매 번호")


        # 번호 타입 sizer에 라디오 버튼 그룹 추가
        panel_number_type_sizer.Add(radio_number_win, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        panel_number_type_sizer.Add(radio_number_buy, 0, wx.ALIGN_LEFT | wx.ALL, 5)

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
        for number in range(1, 46):
            number_list.append(str(number))

        installment_list = []
        for installment in range(1, 1001):
            installment_list.append(str(installment))

        init_value = "select number"

        # TODO input field를 만들고 버튼 클릭 시, 캘린더를 띄워서 선택 된 날짜를 input field에 setValue한다.
        self.calendar_lottery = wx.adv.GenericCalendarCtrl(self, id=-1, size=(200,200), name="calendar_lottery")

        # 번호 입력 ComboBox
        self.combobox_installment = wx.ComboBox(panel_number_combobox, id=0, value="회차 선택", choices=installment_list, size=wx.Size(100, 30))
        self.combobox_number_first = wx.ComboBox(panel_number_combobox, id=1, value=init_value, choices=number_list, size=wx.Size(100, 30))
        self.combobox_number_second = wx.ComboBox(panel_number_combobox, id=2, value=init_value, choices=number_list, size=wx.Size(100, 30))
        self.combobox_number_third = wx.ComboBox(panel_number_combobox, id=3, value=init_value, choices=number_list, size=wx.Size(100, 30))
        self.combobox_number_fourth = wx.ComboBox(panel_number_combobox, id=4, value=init_value, choices=number_list, size=wx.Size(100, 30))
        self.combobox_number_fifth = wx.ComboBox(panel_number_combobox, id=5, value=init_value, choices=number_list, size=wx.Size(100, 30))
        self.combobox_number_sixth = wx.ComboBox(panel_number_combobox, id=6, value=init_value, choices=number_list, size=wx.Size(100, 30))

        # 번호 저장 버튼
        button_save_number = wx.Button(panel_number_combobox, id=0, label="저장")

        # 번호 입력 ComboBox sizer에 ComboBox 추가
        panel_number_combobox_sizer.Add(self.combobox_installment, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        panel_number_combobox_sizer.Add(self.combobox_number_first, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        panel_number_combobox_sizer.Add(self.combobox_number_second, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        panel_number_combobox_sizer.Add(self.combobox_number_third, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        panel_number_combobox_sizer.Add(self.combobox_number_fourth, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        panel_number_combobox_sizer.Add(self.combobox_number_fifth, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        panel_number_combobox_sizer.Add(self.combobox_number_sixth, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        panel_number_combobox_sizer.Add(button_save_number, 0, wx.ALIGN_LEFT | wx.ALL, 10)

        # 이벤트 바인딩
        button_save_number.Bind(wx.EVT_BUTTON, self.save_number)

        # 데이터 관리 sizer에 번호 타입 패널을 추가
        panel_data_manager_sizer.Add(panel_number_type, 0, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 10)
        panel_data_manager_sizer.Add(panel_number_input_type, 0, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 10)
        panel_data_manager_sizer.Add(panel_number_combobox, 0, wx.ALIGN_LEFT | wx.ALL, 15)
        panel_data_manager_sizer.Add(self.calendar_lottery, 0, wx.ALIGN_LEFT | wx.ALL, 15)



    def save_number(self, event):
        installment = self.combobox_installment.GetValue()
        number1 = self.combobox_number_first.GetValue()
        number2 = self.combobox_number_second.GetValue()
        number3 = self.combobox_number_third.GetValue()
        number4 = self.combobox_number_fourth.GetValue()
        number5 = self.combobox_number_fifth.GetValue()
        number6 = self.combobox_number_sixth.GetValue()
        selected_number_list = [number1, number2, number3, number4, number5, number6]

        result = self.validate_input(installment, selected_number_list)

        if result:
            print("번호 저장..")

    def validate_input(self, installment, selected_number_list):
        str_alert = "알림"
        num_dic = {}

        if installment == '회차 선택':
            wx.MessageBox("회차를 선택하세요.", str_alert, wx.OK | wx.ICON_EXCLAMATION)
            return False

        for number in selected_number_list:
            if number == 'select number':
                wx.MessageBox("선택하지 않은 번호가 있습니다.", str_alert, wx.OK | wx.ICON_EXCLAMATION)
                return False
            if num_dic.get(number):
                wx.MessageBox("중복된 번호가 존재합니다.", str_alert, wx.OK | wx.ICON_EXCLAMATION)
                return False
            else:
                num_dic[number] = True
        return True


