class Entry:
    def __init__(self):
        self.reg = []
    def entry(self, passport_number):
        self.reg[passport_number]=1
    def leave(self):
         if self.reg is not None:
             return self.reg.pop(0)
         else:
            raise IndexError()

entry=Entry()
entry.entry("AV")
entry.entry("ABC")
print(entry.reg)
print(entry.leave())
print(entry.reg)
#print(entry.leave())