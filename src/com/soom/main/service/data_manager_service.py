from db.connection_provider import ConnectionProvider

class DataManagerService:
    def __init__(self):
        pass

    def save_number_win(self, number_win_dic):
        connection = ConnectionProvider.get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO WIN_NUMBER (installment, lottery_date, num1, num2, num3, num4, num5, num6) "
                       "VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                       (
                           number_win_dic.get("installment"),
                           number_win_dic.get("lottery_date"),
                           number_win_dic.get("num1"),
                           number_win_dic.get("num2"),
                           number_win_dic.get("num3"),
                           number_win_dic.get("num4"),
                           number_win_dic.get("num5"),
                           number_win_dic.get("num6")))