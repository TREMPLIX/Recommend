import datetime
from datetime import date
import os
from component.logs.core.logs_core import LogsCore


class logging(LogsCore):

    def __init__(self):
        super().__init__()

    def write_logs(self, messages):
        d = datetime.datetime.now().time()
        msg = "{}, {} \n".format(messages, d)
        self.write_log(msg)
