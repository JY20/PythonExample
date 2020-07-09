dataW  = open("data.txt", "w+") 
dataR = open('data.txt', 'r')
contentsB = dataR.read()
print(contentsB+ "ss")
idLen = 11
length = 5

class showsW:
    
    def __init__(self, info):
        self.info = info
    def get_info(self):
        temp = ""
        for i in range(len(self.info)):
            temp += str(self.info[i])
        return temp
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
        inputArr = [None]*length
        for i in range(length):
            input
    except ValueError:
        print("Error") 
        inputs()

def change_info(self):
    self.input = input("First letter of the piece of information you want to change")
    infoLet = ["n", "t", "s", "e"]
    for i in range (len(infoLet)):
        if (self.input.lower() == infoLet[i]):
            print("sss")

ex = [11,"s", "s","s","s"]
d = showsW(ex)
print(d.get_info())
