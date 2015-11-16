def sPrintA():         
    #A    
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(45)
    forward(.5,1)
    turnBy(-90)
    forward(.5,.6)
    turnBy(-90)
    forward(.5,.5)
    turnBy(-90)
    forward(.5,.6)
    backward(.5,.6)
    turnBy(90)
    forward(.5,.5)
    turnBy(45)
    forward(.5,.1)
    turnBy(135)

def sPrintB():         
    #B   
    turnBy(-45)
    wait(0.2)
    forward(.5,.1) # for 1.5 cm
    wait(0.2)
    turnBy(45)
    wait(0.2)
    forward(.5,1)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    forward(.5,.6)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    forward(.5,.5)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    forward(.5,.6)
    wait(0.2)
    backward(.5,.6)
    wait(0.2)
    turnBy(90)
    wait(0.2)
    forward(.5,.5)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    forward(.5,.6)
    wait(0.2)
    backward(.5,.6)
    wait(0.2)
    turnBy(-45)
    wait(0.2)
    backward(.5,.1)
    wait(0.2)
    turnBy(-45)

def sPrintC():         
    #C
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(45)
    forward(.5,1)
    turnBy(-90)
    forward(.5,.6)
    backward(.5,.6)
    turnBy(-90)
    forward(.5,1)
    turnBy(90)
    forward(.5,.6)
    turnBy(-45)
    forward(.5,.1)
    turnBy(135)

def sPrintD():         
    #D
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(45)
    forward(.5,1)
    turnBy(-90)
    forward(.5,.6)
    turnBy(-90)
    forward(.5,1)
    turnBy(-90)
    forward(.5,.6)
    backward(.5,.6)
    turnBy(-45)
    backward(.5,.1)
    turnBy(-45)

def sPrintE():         
    #E
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(45)
    forward(.5,1)
    turnBy(-90)
    forward(.5,.6)
    backward(.5,.6)
    turnBy(-90)
    forward(.5,.4) # go to half of E
    turnBy(90)
    forward(.5,.4)
    backward(.5,.4)
    turnBy(-90)
    forward(.5,.6) # go to full of E
    turnBy(90)
    forward(.5,.6)
    turnBy(-45)
    forward(.5,.1)
    turnBy(135)

def sPrintF():    # Uses Removal of Pen
    #F
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(45)
    forward(.5,1)
    turnBy(-90)
    forward(.5,.6)
    backward(.5,.6)
    turnBy(-90)
    forward(.5,.4) # go to half of E
    turnBy(90)
    forward(.5,.4)
    backward(.5,.4)
    turnBy(-90)
    forward(.5,.4) # go to full of E
    turnBy(90)
    beep(0.16,100,100)
    print ("Remove Pen ")
    wait(5)
    forward(.5,.7)
    turnBy(90)
    beep(.16,100,100)
    print("Restrore Pen")
    wait(5)
    

def sPrintG():         
    #G
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(45)
    forward(.5,1)
    turnBy(-90)
    forward(.5,.6)
    backward(.5,.6)
    turnBy(-90)
    forward(.5,1)  
    turnBy(90)
    forward(.5,.6)
    turnBy(90)
    forward(.5,.3)
    turnBy(90)
    forward(.5,.3)
    turnBy(90)
    forward(.5,.1)
    backward(.5,.1)
    turnBy(-90)
    backward(.5,.3)
    turnBy(-90)
    backward(.5,.3)
    turnBy(45)
    forward(.5,.1)
    turnBy(-45)

def sPrintH():         
    #H
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(45)
    forward(.5,1)
    backward(.5,.4)
    turnBy(-90)
    forward(.5,.6)
    turnBy(90)
    forward(.5,.4) # go to half of E
    backward(.5,1)
    turnBy(45)
    backward(.5,.1)
    turnBy(-45)


def sPrintI():         
    #I
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(-45)
    forward(.5,.2)
    turnBy(90)
    forward(.5,1)
    turnBy(90)
    forward(.5,.1)
    backward(.5,.1)
    backward(.5,.1)
    forward(.5,.1)
    turnBy(-90)
    backward(.5,1)
    turnBy(-90)
    forward(.5,.2) 
    turnBy(-45)
    forward(.5,.1)
    turnBy(135)

def sPrintJ():         
    #J
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(45)
    forward(.5,.1)
    backward(5.,.1)
    turnBy(-90)
    forward(.5,.5)
    turnBy(90)
    forward(.5,1)
    turnBy(90)
    forward(.5,.1)
    backward(.5,.1)
    backward(.5,.1)
    forward(.5,.1)
    turnBy(-90)
    backward(.5,1)
    turnBy(45)
    backward(.5,.1)
    turnBy(-45)

def sPrintK():         
    #K
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(45)
    forward(.5,1)
    backward(.5,.4)
    turnBy(45)
    forward(.5,.5)
    backward(.5,.5)
    turnBy(-90)
    forward(.5,.5)
    forward(.5,.1)
    tunrBy(135)

def sPrintL():         
    #L
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(45)
    forward(.5,1)
    backward(.5,1)
    turnBy(-90)
    forward(.5,.6)
    turnBy(-45)
    forward(.5,.1)
    turnBy(45)


def sPrintM():
    #M
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(45)
    forward(.5,1)
    turnBy(45)
    backward(.5,.3)
    turnBy(90)
    forward(.5,.3)
    turnBy(45)
    backward(.5,1)
    turnBy(45)
    backward(.5,.1)
    tunrBy(-45)

def sPrintN():
    #N
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(45)
    forward(.5,1)
    turnBy(45)
    backward(.5,1)
    turnBy(-45)
    forward(.5,1)
    backward(.5,1)
    turnBy(45)
    backward(.5,.1)
    tunrBy(-45)
    
def sPrintO():
    #O
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(-45)
    forward(.5,.4)
    # usemotor to draw circle
    forward(.5,.4)
    turnBy(-45)
    forward(.5,.1)
    turnBy(135)
    
def sPrintP():  #Uses Removal of Pen
    #P
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(45)
    forward(.5,1)
    turnBy(-90)
    forward(.5,.6)
    turnBy(-90)
    forward(.5,.4) 
    turnBy(-90)
    forward(.5,.6)
    turnBy(90)
    forward(.5,.4)
    beep(0.16,100,100)
    print ("Remove Pen ")
    turnBy(90)
    wait(5)
    forward(.5,.7)
    turnBy(-45)
    forward(.5,.1)
    turnBy(135)
    beep(.16,100,100)
    print("Restrore Pen")

    wait(5)
    
def sPrintQ():
    #Q
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(-45)
    forward(.5,.4)
    # usemotor to draw circle
    turnBy(30)
    forward(.5,.3)
    backward(.5,.3)
    tunrBy(30)
    forward(.5,.4)
    turnBy(-45)
    forward(.5,.1)
    turnBy(135)
    
def sPrintR():
    #R
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(45)
    forward(.5,1)
    turnBy(-90)
    forward(.5,.6)
    turnBy(-90)
    forward(.5,.4)
    turnBy(-90)
    forward(.5,.6)
    backward(.5,.1)
    tunrBy(-45)
    backward(.5,.4)
    backward(.5,.1)
    turnBy(-45)
    
def sPrintS():
    #S
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(-45)
    forward(.5,.6)
    tunrBy(90)
    forward(.5,.4)
    tunrBy(90)
    forward(.5,.6)
    tunrBy(-90)
    forward(.5,.4)
    turnBy(-90)
    forward(.5,.6)
    backward(.5,.6)
    tunrBy(90)
    backward(.5,.4)
    tunrBy(90)
    backward(.5,.6)
    turnBy(-90)
    backward(.5,.4)
    turnBy(45)
    backward(.5,.1)
    tunrBy(-45)
    
    
def sPrintT():  #Uses Removal of Pen
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(-45)
    print("Remove Pen")
    wait(5)
    forward(.5,.4)
    turnBy(90)
    print("Restore Pen")
    wait(5)
    forward(.5,1)
    tunrBy(90)
    forward(.5,.3)
    backward(.5,.3)
    backward(.5,.3)
    forward(.5,.3)
    turnBy(-90)
    backward(.5,1)
    turnBy(-90)
    print("Remove Pen")
    wait(5)
    forward(.5,.4)
    turnBy(135)
    backward(.5,.1)
    tunrBy(-45)
    print("Restore Pen")
    wait(5)
    
def sPrintU():
    #U
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(45)
    forward(.5,.1)
    backward(5.,1)
    turnBy(-90)
    forward(.5,.6)
    turnBy(90)
    forward(.5,1)
    backward(.5,1)
    turnBy(45)
    backward(.5,.1)
    turnBy(-45)

def sPrintV(): #Uses Removal of Pen
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(-45)
    print("Remove Pen")
    beep(.16,100,100)
    wait(5)
    forward(.5,.4)
    turnBy(120)
    beep(.16,100,100)
    print("Restore Pen")
    wait(5)
    forward(.5,1)
    backward(.5,1)
    turnBy(-60)
    forward(.5,1)
    backward(.5,1)
    turnBy(-60)
    print("Remove Pen")
    beep(.16,100,100)
    wait(5)
    forward(.5,.4)
    turnBy(135)
    backward(.5,.1)
    tunrBy(-45)
    print("Restore Pen")
    beep(.16,100,100)
    wait(5)
    
def sPrintW():
    #W
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(45)
    forward(.5,1)
    backward(.5,1)
    turnBy(-45)
    forward(.5,.3)
    tunrBy(-90)
    forward(.5,.3)
    tunrBy(135)
    forward(.5,1)
    backward(.5,1)
    turnBy(45)
    backward(.5,.1)
    tunrBy(-45)


def sPrintX():
    #X
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    forward(.5,1)
    backward(.5,.4)
    turnBy(90)
    forward(.5,.4)
    backward(.5,1)
    backward(.5,.1)
    turnBy(-45)
    
def sPrintY():  #Uses Removal of Pen
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    turnBy(-45)
    print("Remove Pen")
    beep(.16,100,100)
    wait(5)
    forward(.5,.4)
    turnBy(90)
    print("Restore Pen")
    beep(.16,100,100)
    wait(5)
    forward(.5,.4)
    turnBy(30)
    forward(.5,.4)
    backward(.5,.4)
    turnBy(-60)
    forward(.5,.4)
    backward(.5,.4)
    turnBy(30)
    backward(.5,.4)
    turnBy(-90)
    print("Remove Pen")
    beep(.16,100,100)
    wait(5)
    forward(.5,.4)
    turnBy(135)
    backward(.5,.1)
    tunrBy(-45)
    print("Restore Pen")
    beep(.16,100,100)
    wait(5)
    
def sPrintZ():
    #Z
    turnBy(-45)
    forward(.5,.1) # for 1.5 cm
    forward(.5,1)
    turnBy(-45)
    backward(.5,.6)
    forward(.5,.6)
    turnBy(45)
    backward(.5,1)
    turnBy(-45)
    forward(.5,.6)
    turnBy(-45)
    forward(.5,.1)
    turnBy(135)
    

def scribblerPrint(a):    
    if a=='A':
        sPrintA()
    elif a=='B':
        sPrintB()
    elif a=='B':
        sPrintB()
    elif a=='C':
        sPrintC()
    elif a=='D':
        sPrintD()
    elif a=='E':
        sPrintE()
    elif a=='F':
        sPrintF()
    elif a=='G':
        sPrintG()
    elif a=='H':
        sPrintH()
    elif a=='I':
        sPrintI()
    elif a=='J':
        sPrintJ()
    elif a=='K':
        sPrintK()
    elif a=='L':
        sPrintL()
    elif a=='M':
        sPrintM()
    elif a=='N':
        sPrintN()
    elif a=='O':
        sPrintO()
    elif a=='P':
        sPrintP()
    elif a=='Q':
        sPrintQ()
    elif a=='R':
        sPrintR()
    elif a=='S':
        sPrintS()
    elif a=='T':
        sPrintT()
    elif a=='U':
        sPrintU()
    elif a=='V':
        sPrintV()
    elif a=='W':
        sPrintW()
    elif a=='X':
        sPrintX()
    elif a=='Y':
        sPrintY()
    elif a=='Z':
        sPrintZ()

if _name_== "_main_":
    name= raw_input()
    a= name.split(" ")
    for i in a:
        b=a.split()
        for j in b:
            ScribblerPrint(j) 
        
