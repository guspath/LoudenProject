import sqlite3


class DBProxy:

    def __init__(self, db_n: str):
        self.db_n = db_n
        self.connection = sqlite3.connect(db_n)
        self.connection.execute('''
                                            CREATE TABLE IF NOT EXISTS dados(
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            name TEXT NOT NULL,
                                           score INTEGER NOT NULL,
                                           date TEXT NOT NULL)
                                        '''
                                )

    def save_db(self, score_dict: dict):
        self.connection.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dict)
        self.connection.commit()

    def db_top10(self) -> list:
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        return self.connection.close()

