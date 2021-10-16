class Location:
    def __init__(self, title, names=None, specialAttr=None, positions=None, exits=None):
        if title is None:
            title = ""
        if names is None:
            names = list()
        if specialAttr is None:
            specialAttr = list()
        if positions is None:
            positions = list()
        if exits is None:
            exits = list()
        self.title = title
        self.locs = list()
        for i in range(len(names)):
            self.locs.append((names[i], specialAttr[i], positions[i]))
        self.exits = exits

    def getAllFromNumber(self, num):
        return self.locs[num - 1]

    def getNameFromNumber(self, num):
        return self.locs[num-1][0]

    def getSpecialAttrFromNumber(self, num):
        return self.locs[num-1][1]

    def getPositionsFromNumber(self, num):
        return self.locs[num-1][2]



