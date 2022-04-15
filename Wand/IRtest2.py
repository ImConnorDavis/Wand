import lirc
sockid = lirc.init("IRtest")
while True:
    codeIR = lirc.nextcode()
    if codeIR != []:
        if codeIR[0] == "KEY_1":
            print "Attack 1"

    
