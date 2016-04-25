import wx
import wx.adv
from db.connection_provider import ConnectionProvider
import sqlite3
import natsort

class DataManager(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.panel_data_manager_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.panel_data_manager_sizer)

        self.radio_number_win = None
        self.radio_number_buy = None
        self.radio_number_input_single = None
        self.radio_number_input_batch = None
        self.combobox_installment = None
        self.datepicker = None
        self.combobox_number_first = None
        self.combobox_number_second = None
        self.combobox_number_third = None
        self.combobox_number_fourth = None
        self.combobox_number_fifth = None
        self.combobox_number_sixth = None

        self.panel_number_type = self.init_panel_number_type()
        self.panel_number_input_type = self.init_panel_number_input()
        self.panel_installment = self.init_panel_installment()
        self.panel_number_combobox = self.init_panel_number_combobox()



        self.add_panels()

    def init_panel_number_type(self):
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

        return panel_number_type

    def init_panel_number_input(self):
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

        return panel_number_input_type

    def init_panel_installment(self):
       # 회차, 날짜 입력 패널
        panel_installment = wx.Panel(self)
        panel_installment_sizer = wx.StaticBoxSizer(wx.HORIZONTAL, panel_installment, "회차 및 날짜")
        panel_installment.SetSizer(panel_installment_sizer)

        installment_list = self.create_installment_list()

        # 회차 및 날짜 컨트롤
        self.combobox_installment = wx.ComboBox(panel_installment, id=0, value="회차 선택", choices=installment_list, size=wx.Size(100, 30))
        self.datepicker = wx.adv.DatePickerCtrl(panel_installment, style=wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN)

        # datepicker_png = wx.Image("ui/menu/datepicker.png", type=wx.BITMAP_TYPE_PNG, index=-1).ConvertToBitmap()
        # button_datepicker = wx.BitmapButton(panel_installment, bitmap=datepicker_png, size=wx.Size(22, 22))

        panel_installment_sizer.Add(self.combobox_installment, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        panel_installment_sizer.Add(self.datepicker, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        return panel_installment

    def init_panel_number_combobox(self):
        # 번호 입력 Combobox 패널
        panel_number_combobox = wx.Panel(self)
        panel_number_combobox_sizer = wx.StaticBoxSizer(wx.HORIZONTAL, panel_number_combobox, "번호 입력")
        panel_number_combobox.SetSizer(panel_number_combobox_sizer)

        number_list = []
        for number in range(1, 46):
            number_list.append(str(number))

        init_value = "select number"

        # 번호 입력 ComboBox
        self.combobox_number_first = wx.ComboBox(panel_number_combobox, id=1, value=init_value, choices=number_list, size=wx.Size(100, 30))
        self.combobox_number_second = wx.ComboBox(panel_number_combobox, id=2, value=init_value, choices=number_list, size=wx.Size(100, 30))
        self.combobox_number_third = wx.ComboBox(panel_number_combobox, id=3, value=init_value, choices=number_list, size=wx.Size(100, 30))
        self.combobox_number_fourth = wx.ComboBox(panel_number_combobox, id=4, value=init_value, choices=number_list, size=wx.Size(100, 30))
        self.combobox_number_fifth = wx.ComboBox(panel_number_combobox, id=5, value=init_value, choices=number_list, size=wx.Size(100, 30))
        self.combobox_number_sixth = wx.ComboBox(panel_number_combobox, id=6, value=init_value, choices=number_list, size=wx.Size(100, 30))

        # 번호 저장 버튼
        button_save_number = wx.Button(panel_number_combobox, id=0, label="저장")

        # 번호 입력 ComboBox sizer에 ComboBox 추가
        panel_number_combobox_sizer.Add(self.combobox_number_first, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        panel_number_combobox_sizer.Add(self.combobox_number_second, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        panel_number_combobox_sizer.Add(self.combobox_number_third, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        panel_number_combobox_sizer.Add(self.combobox_number_fourth, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        panel_number_combobox_sizer.Add(self.combobox_number_fifth, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        panel_number_combobox_sizer.Add(self.combobox_number_sixth, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        panel_number_combobox_sizer.Add(button_save_number, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        """
        이벤트 바인딩
        """
        button_save_number.Bind(wx.EVT_BUTTON, self.save_number)

        return panel_number_combobox

    def add_panels(self):
        # 데이터 관리 sizer에 번호 타입 패널을 추가
        self.panel_data_manager_sizer.Add(self.panel_number_type, 0, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 10)
        self.panel_data_manager_sizer.Add(self.panel_number_input_type, 0, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 10)
        self.panel_data_manager_sizer.Add(self.panel_installment, 0, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 10)
        self.panel_data_manager_sizer.Add(self.panel_number_combobox, 0, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 15)


    def create_installment_list(self):
        installment_list = []
        for installment in range(1, 1001):
            installment_list.append(str(installment))
        return installment_list

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

        # 번호 오름차순 정렬
        sorted_number_list = natsort.natsorted(selected_number_list)

        if result:
            connection = ConnectionProvider.get_connection()
            cursor = connection.cursor()

            try:
                cursor.execute("INSERT INTO win_number (installment, lottery_date, num1, num2, num3, num4, num5, num6)"
                           "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                            (installment
                             , '2016-04-10'
                             , sorted_number_list[0]
                             , sorted_number_list[1]
                             , sorted_number_list[2]
                             , sorted_number_list[3]
                             , sorted_number_list[4]
                             , sorted_number_list[5]))
                connection.commit()
            except sqlite3.IntegrityError as err:
                print("이미 입력된 회차입니다. ({0})".format(err))
                wx.MessageBox("이미 입력된 회차입니다.", "알림", wx.OK | wx.ICON_EXCLAMATION)
                connection.rollback()
            else:
                id = cursor.lastrowid
                if(id != None):
                    wx.MessageBox(str(id) + "회차를 저장했습니다.", "알림", wx.OK | wx.ICON_EXCLAMATION)
                    #     TODO 선택한 항목들 초기화
                else:
                    wx.MessageBox("정상적으로 저장되지 않았습니다. 다시 시도해주세요.", "알림", wx.OK | wx.ICON_EXCLAMATION)
            finally:
                cursor.close()
                connection.close()






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


