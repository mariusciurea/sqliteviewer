import sqlite3
import pandas as pd


class Database:
    def __init__(self, db_location=''):
        self.db_location = db_location
        self.con = sqlite3.connect(db_location)
        self.cursor = self.con.cursor()

    def get_tables(self):
        tables = self.cursor.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
        return tables.fetchall()

    def get_df(self, table_name):
        return pd.read_sql(f"""SELECT * FROM {table_name};""", self.con)

    def query(self, sql_command):
        return pd.read_sql(f"""{sql_command}""", self.con)

    def close(self):
        self.con.close()


if __name__ == '__main__':
    users = Database("users.db")
