import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('standup.db', check_same_thread=False)
        self.init_db()

    def init_db(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS standups ("
                          "daily_message TEXT, bi_hourly_message TEXT, channel TEXT PRIMARY KEY, post_time TEXT, timezone TEXT)"
                          )
        self.conn.commit()

    def add_standups(self, daily_message, bi_hourly_message, channel, post_time, timezone):
        self.conn.execute("INSERT INTO standups "
                          "(daily_message, bi_hourly_message, channel, post_time, timezone) VALUES (?, ?, ?, ?, ?) "
                          "ON CONFLICT(channel) DO UPDATE SET "
                          "daily_message = excluded.daily_message,  "
                          "bi_hourly_message = excluded.bi_hourly_message, "
                          "post_time = excluded.post_time, "
                          "timezone = excluded.timezone",
                          (daily_message, bi_hourly_message, channel, post_time, timezone)
                          )
        self.conn.commit()

    def list_standups(self):
        rows = self.conn.execute("SELECT * FROM standups").fetchall()
        return rows