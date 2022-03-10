
# startTime and endTime refer to when during the day they can be implemented

class ActivityType:
    def __init__(self, type, startTime, endTime, days): 
        self.type = type
        self.startTime = startTime
        self.endTime = endTime
        if days == "All" or days == "all":
            self.days = ["a"]
        else:
            self.days = {"Monday":1}
        self.lengths = []
        self.currentLength = 0
        self.index = -1

    def addLengths(self, newLengths):
        for length in newLengths:
            self.lengths.append(length)

    def allDays(self):
        self.days

    def __iter__(self):
        self.currentLength = len(self.lengths)
        self.index= -1
        return self

    def __next__(self):
        self.index = self.index+1
        if self.index == self.currentLength:
            raise StopIteration
        return self.lengths[self.index]
    

x = ActivityType("class",9,10,"All")
print(x.days)
y = ActivityType("class",9,10,["Tuesday"])
print(y.days)

