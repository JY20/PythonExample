dataW  = open("data.txt", "w+") 
dataR = open('data.txt', 'r')
contentsB = dataR.read()
print(contentsB+ "ss")
id = 11
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
def inputs(id):
    inputArr = [None]*length
    inputArr[0] = id
    inputArr[1] = input("what is the show name" + "\n")
    inputArr[2] = input("what type of show is it" + "\n")
    inputArr[3] = input("what season are you on" + "\n")
    inputArr[4] = input("what episode are you on" + "\n")
    try:
        for i in range (2):
            temp = str(inputArr[i+1])
            temp = int(inputArr[i+3])
        listShows[id] = showsW(inputArr)
    except ValueError:
        print("Error") 
        inputs(id)

def change_info(self):
    self.input = input("First letter of the piece of information you want to change")
    infoLet = ["n", "t", "s", "e"]
    for i in range (len(infoLet)):
        if (self.input.lower() == infoLet[i]):
            print("sss")

def copy(inArr):
    outArr = [None] * id
    for i in range(id):
        outArr[i] = inArr[i]
    outArr[id] = [None] 
    return outArr
listShows = [None] * id
id = id + 1
listShows = copy(listShows)
