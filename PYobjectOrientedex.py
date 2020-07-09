dataW  = open("data.txt", "w+") 
dataR = open('data.txt', 'r')
#for i in range(10):
    #dataW.write("This is line %d\r\n" % (i+1))
#dataW.close()
contentsB = dataR.read()
print(contentsB)

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
            if (self.input.lower() == infoLet[i]):
                print("sss")
    def get_info(self):
        return self.name + "    " + self.typ + "    " + str(self.seasons) + "    " + str(self.episodes)

def clean():
    dataW.truncate(0)
    dataW.close()

def inputs():
    name = input("what is the show name" + "\n")
    typ = input("what type of show is it" + "\n")
    seasons = input("what season are you on" + "\n")
    episodes = input("what episode are you on" + "\n")
    try:
        temp = str(name)
        temp = str(typ)
        temp = int(seasons)
        temp = int(episodes)
    except ValueError:
        print("Error") 
        inputs()
inputs()
