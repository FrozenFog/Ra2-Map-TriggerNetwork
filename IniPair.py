class IniPair:
    Name = ""
    Value = None

    def __init__(self):
        self.Name = ""
        self.Value = None

    def IsNull(self):
        return  self.Name == "" or self.Value is None or self.Value == ""

