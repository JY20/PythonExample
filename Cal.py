state = True
r = 0 # the resistance value
i = 0 # the current value
v = 0 # the voltage value

def Vcal(): # calculating the v value with i and r
    userInput = input("What is the current in amps" + "\n")
    if userInput.isdigit():
        i = int(userInput)
        userInput = input("What is the resistance in ohms" + "\n")
        if userInput.isdigit():
            r = int(userInput)
            v = i*r
            print("The voltage is")
            print(v)
            print("volts")
        else:
            print("input not vaild")
    else:
        print("input not vaild")

def Ical():# calculating the i value with v and r
    userInput = input("What is the voltage in volts" + "\n")
    if userInput.isdigit():
        v = int(userInput)
        userInput = input("What is the resistance in ohms" + "\n")
        if userInput.isdigit():
            r = int(userInput)
            i = v/r
            print("The current is")
            print(i)
            print("amps")
        else:
            print("input not vaild")
    else:
        print("input not vaild")

def Rcal(): # calculating the r value with i and v
    userInput = input("What is the voltage in volts" + "\n")
    if userInput.isdigit():
        v = int(userInput)
        userInput = input("What is the current in amps" + "\n")
        if userInput.isdigit():
            i = int(userInput)
            r = v/i
            print("The resistance is")
            print(r)
            print("Ohms")
        else:
            print("input not vaild")
    else:
        print("input not vaild")

while (state == True): # user interface of the program
    print("Enter 1 to calculate the voltage")
    print("Enter 2 to calculate the current")
    print("Enter 3 to calculate the resistance")
    Input = input("What do you want to calulate" + "\n")
    if (Input == "1"):
        Vcal()
    elif (Input == "2"):
        Ical()
    elif (Input == "3"):
        Rcal()
    else:
        print("Input not valid")