import datetime
from datetime import date
import os


class logging:
    def __init__(self):
        self.log_filename = 'data/logs/{}.txt'.format(date.today())
        if not os.path.exists(self.log_filename):
            self.create_log_file()

    def create_log_file(self):
        f = open(self.log_filename, 'w')
        f.close()

    def open_log_file(self):
        self.f = open(self.log_filename, 'a')

    def close_log_file(self):
        self.f.close()

    def read_logs(self, messages):
        self.open_log_file()
        d = datetime.datetime.now().time()
        msg = '{}, {} \n'.format(messages, d)
        self.f.write(msg)
        self.close_log_file()

