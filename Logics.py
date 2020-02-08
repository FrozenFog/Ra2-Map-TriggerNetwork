from IniEnt import IniEnt
from IniPair import IniPair

class Trigger:

    id = ""
    associated = ""
    disabled = False
    side = ""
    name = ""
    easy = False
    normal = False
    hard = False
    repeat = 0
    count = 3
    events = []
    actions = []

    setlocals = []
    readlocals = []
    movedtriggers = []

    def __init__(self):
        self.events = []
        self.actions = []
        self.setlocals = []
        self.readlocals = []
        self.movedtriggers = []

    def LoadTag(self, strings):
        sl = strings.split(",")
        self.side = sl[0]
        self.associated = sl[1]
        self.name = sl[2]
        self.disabled = sl[3] == "1"
        self.easy = sl[4] == "1"
        self.normal = sl[5] == "1"
        self.hard = sl[6] == "1"
        self.repeat = int(sl[7])

    def LoadEvent(self, strings):
        sl = strings.split(",")
        num = int(sl[0])
        i = 1
        while (num > 0):
            event = Event()
            event.eventid = int(sl[i])
            i += 1
            if event.eventid == 61 or event.eventid == 60:
                event.parameters = sl[i:i+3]
                i += 3
            else:
                event.parameters = sl[i:i+2]
                i += 2
            num -= 1
            self.events.append(event)

    def LoadAction(self, strings):
        sl = strings.split(",")
        num = int(sl[0])
        i = 1
        while (num > 0):
            action = Action()
            action.actionid = int(sl[i])
            i += 1
            action.parameters = sl[i:i+7]
            i += 7
            num -= 1
            self.actions.append(action)

    def Associated(self):
        return self.associated != "<none>"

    def Nothing(self):
        return  self.associated == "<none>" and len(self.setlocals) == 0 and len(self.readlocals) == 0 and len(self.movedtriggers) == 0



class Action:

    actionid = 0
    parameters = []

    def __init__(self):
        self.actionid = 0
        self.parameters = []


class Event:

    eventid = 0
    parameters = []

    def __init__(self):
        self.eventid = 0
        self.parameters = []

class Variable:

    varname = ""
    varid = ""
    varcount = 3

    def __init__(self):
        self.varcount = 0
        self.varname = ""