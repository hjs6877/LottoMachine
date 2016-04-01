from db.connection_provider import ConnectionProvider


class DbManager:
    def __init__(self):
        self.connection = ConnectionProvider.get_connection()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE if not exists BUY_NUMBER ("
                            "seq_no INTEGER PRIMARY KEY AUTOINCREMENT,  nth INTEGER, lottery_date DATETIME, "
                            "num1 INTEGER, num2 INTEGER, num3 INTEGER, num4 INTEGER, num5 INTEGER, num6 INTEGER)")
