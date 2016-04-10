import sqlite3


class ConnectionProvider:
    connection = None

    @staticmethod
    def get_connection():
        return sqlite3.connect("lotto.db")