import IniPair

class IniEnt:

    __datadict = {}
    Name = ""

    def __init__(self, ):
        self.Name = ""
        self.__datadict = {}

    def AddPair(self, pair, pairname):
        self.__datadict[pairname] = pair

    def IsEmpty(self):
        return  len(self.__datadict) == 0

    def ClearItem(self):
        self.__datadict = {}

    def Data(self):
        return self.__datadict.values()

    def __getitem__(self, item):
        if self.__datadict.keys().__contains__(item):
            return  self.__datadict[item]
        else:
            return None

    def __setitem__(self, key, value):
        self.__datadict[key] = value