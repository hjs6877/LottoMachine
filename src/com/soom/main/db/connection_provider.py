import sqlite3


class ConnectionProvider:
    connection = None

    @staticmethod
    def get_connection():
        if(ConnectionProvider.connection == None):
            ConnectionProvider.connection = sqlite3.connect("lotto.db")

        return ConnectionProvider.connection