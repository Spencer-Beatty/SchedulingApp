import enum
import py_compile

class ActivityRequest:
    def __init__(self, name, type, finishDate, timeAllotment):
        self.name = name
        self.type = type
        self.finishDate = finishDate
        self.timeAllotment = timeAllotment
    