class Element:
    " key, value, index of the element "
    def __init__(self,key, value, index):
        self.__key = key
        self.__value = value
        self.__index = index

    def __eq__(self, other):
        "return boolean element1 equal element2"
        if type(self.getKey()) == type(other.getKey()):
            return self.getKey() == other.getKey()
        raise NotImplementedError("Can't compare, elements are not same type of data")

    def __lt__(self, other):
        " return boolean element1 less than element2"
        if type(self.getKey()) == type(other.getKey()):
            return self.getKey() < other.getKey()
        raise NotImplementedError("Can't compare, elements are not same type of data")
        
    def __str__(self):
        "return element as readable String"
        return "%s: %s (%d)" %(str(self.__key), str(self.__value),
                               self.__index)
    
    def __repr__(self):
        "representation of the element"
        return self.__str__()

    def getKey(self):
        return self.__key

    def setKey(self,key):
        self.__key = key

    def getValue(self):
        return self.__value

    def getIndex(self):
        return self.__index

    def setIndex(self, index):
        self.__index = index
        
    
    
        
