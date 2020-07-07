class showsW:
    
    def __init__(self, name, typ, seasons, episodes):
        self.name = name
        self.typ = typ
        self.seasons = seasons
        self.episodes = episodes
    def change_info(self):
        self.input = input("First letter of the piece of information you want to change")
        infoLet = ["n", "t", "s", "e"]
        for i in range (len(infoLet)):
            if (lower(self.input) == infoLet[i]):
                print("sss")
    def get_info(self):
        return self.name + "    " + self.typ + "    " + self.seasons + "    " + self.episodes
d = showsW("dragonball", "anime", 1, 110)
print(d.get_info())