class Protected: #this is our protected class
    def __init__(self):
        self._protectedVar = 5 #protected class denoted with single _

obj = Protected()
obj._protectedVar = 7
print(obj.protectedVar)
#^this objs get data from protected variable

class Private:
    def __init__(self):
        self.__privateVar = 32 #private class denoted with double __

    def getPrivate(self):
        print(self.privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Private()
obj.getPrivate()
obj.setPrivate(50)
obj.getPrivate()
        
#^ these obj's get data from private variable
