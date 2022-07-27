class Protected:
    def __init__(self):
        self._protectedVar = 5

obj = Protected()
obj._protectedVar = 7
print(obj.protectedVar)

class Private:
    def __init__(self):
        self.__privateVar = 32

    def getPrivate(self):
        print(self.privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Private()
obj.getPrivate()
obj.setPrivate(50)
obj.getPrivate()
        
