import  IniEnt, IniPair

class IniFile:
    __datadict = {}

    def __init__(self):
        self.__datadict = {}

    def AddEnt(self, ent, name):
        self.__datadict[name] = ent

    def __getitem__(self, item):
        if self.__datadict.keys().__contains__(item):
            return self.__datadict[item]
        else:
            return None

    def ReadData(self, lines):
        entname = ""
        ent = IniEnt.IniEnt()
        pair = IniPair.IniPair()
        for line in lines:
            if line.startswith(";"):
                continue
            if line.count(";") > 0:
                line = line[:line.index(";")]
            line = line.strip()
            if line == "":
                continue
            if line.startswith("["):
                if not ent.IsEmpty():
                    self.AddEnt(ent, entname)
                    ent = IniEnt.IniEnt()
                entname = line[1:-1]
                ent.Name = entname
                continue
            sl = line.split("=")
            if len(sl) != 2:
                continue
            pair.Name = sl[0]
            pair.Value = sl[1]
            ent.AddPair(pair, sl[0])
            pair = IniPair.IniPair()
        self.AddEnt(ent, entname)

    def __setitem__(self, key, value):
        self.__datadict[key] = value