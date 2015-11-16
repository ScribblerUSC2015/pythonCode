from Myro import *
init("/dev/tty.Fluke2-0214-Fluke2")
def sPrintA():
    #A    
    turnBy(-45)
    wait(0.2)
    forward(.5,.1) # for 1.5 cm
    wait(0.2)
    turnBy(45)
    wait(0.2)
    forward(.5,1)
    turnBy(-90)
    forward(.5,.6)
    turnBy(-90)
    forward(.5,.4)
    turnBy(-90)
    forward(.5,.6)
    backward(.5,.6)
    turnBy(90)
    forward(.5,.4)
    turnBy(45)
    forward(.5,.1)
    turnBy(135)
    wait(0.2)

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
    forward(.5,.4)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    forward(.5,.6)
    wait(0.2)
    backward(.5,.6)
    wait(0.2)
    turnBy(90)
    wait(0.2)
    forward(.5,.4)
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
    wait(0.2)

def sPrintC():         
    #C
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
    backward(.5,.6)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    forward(.5,1)
    wait(0.2)
    turnBy(90)
    wait(0.2)
    forward(.5,.6)
    wait(0.2)
    turnBy(-45)
    wait(0.2)
    forward(.5,.1)
    wait(0.2)
    turnBy(135)
    wait(0.2)

def sPrintD():         
    #D
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
    forward(.5,1)
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

def sPrintE():         
    #E
    wait(0.2)
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
    backward(.5,.6)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    forward(.5,.4) # go to half of E
    wait(0.2)
    turnBy(90)
    wait(0.2)
    forward(.5,.4)
    wait(0.2)
    backward(.5,.4)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    forward(.5,.6) # go to full of E
    wait(0.2)
    turnBy(90)
    wait(0.2)
    forward(.5,.6)
    wait(0.2)
    turnBy(-45)
    wait(0.2)
    forward(.5,.1)
    wait(0.2)
    turnBy(135)
    wait(0.2)

def sPrintF():         
    #F
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
    backward(.5,.6)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    forward(.5,.4) # go to half of E
    wait(0.2)
    turnBy(90)
    wait(0.2)
    forward(.5,.4)
    wait(0.2)
    backward(.5,.4)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    forward(.5,.4) # go to full of E
    wait(0.2)
    turnBy(90)
    wait(5)
    beep(1,100,100)
    print ("Remove Pen ")
    forward(.5,.7)
    wait(0.2)
    turnBy(-45)
    wait(0.2)
    forward(.5,.1)
    wait(0.2)
    turnBy(135)
    wait(2)
    beep(1,200,200)
    print("Restrore Pen")

def sPrintG():         
    #G
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
    backward(.5,.6)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    forward(.5,1)  
    wait(0.2)
    turnBy(90)
    wait(0.2)
    forward(.5,.6)
    wait(0.2)
    turnBy(90)
    wait(0.2)
    forward(.5,.3)
    wait(0.2)
    turnBy(90)
    wait(0.2)
    forward(.5,.3)
    wait(0.2)
    turnBy(90)
    wait(0.2)
    forward(.5,.1)
    wait(0.2)
    backward(.5,.1)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    backward(.5,.3)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    backward(.5,.3)
    wait(0.2)
    turnBy(45)
    wait(0.2)
    backward(.5,.1)
    wait(0.2)
    turnBy(-45)

def sPrintH():         
    #H
    turnBy(-45)
    wait(0.2)
    forward(.5,.1) # for 1.5 cm
    wait(0.2)
    turnBy(45)
    wait(0.2)
    forward(.5,1)
    wait(0.2)
    backward(.5,.4)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    forward(.5,.6)
    wait(0.2)
    turnBy(90)
    wait(0.2)
    forward(.5,.4) # go to half of E
    wait(0.2)
    backward(.5,1)
    wait(0.2)
    turnBy(45)
    wait(0.2)
    backward(.5,.1)
    wait(0.2)
    turnBy(-45)


def sPrintI():         
    #I
    turnBy(-45)
    wait(0.2)
    forward(.5,.1) # for 1.5 cm
    wait(0.2)
    turnBy(-45)
    wait(0.2)
    forward(.5,.2)
    wait(0.2)
    turnBy(90)
    wait(0.2)
    forward(.5,1)
    wait(0.2)
    turnBy(90)
    wait(0.2)
    forward(.5,.1)
    wait(0.2)
    backward(.5,.1)
    wait(0.2)
    backward(.5,.1)
    wait(0.2)
    forward(.5,.1)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    backward(.5,1)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    forward(.5,.2) 
    wait(0.2)
    turnBy(-45)
    wait(0.2)
    forward(.5,.1)
    wait(0.2)
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
    wait(0.2)
    forward(.5,.1) # for 1.5 cm
    wait(0.2)
    turnBy(45)
    wait(0.2)
    forward(.5,1)
    wait(0.2)
    backward(.5,.4)
    wait(0.2)
    turnBy(-45)
    wait(0.2)
    forward(.5,.5)
    wait(0.2)
    backward(.5,.5)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    forward(.5,.4)
    wait(0.2)
    forward(.5,.2)
    wait(0.2)
    turnBy(135)
    wait(0.2)

def sPrintL():         
    #L
    turnBy(-45)
    wait(0.2)
    forward(.5,.1) # for 1.5 cm
    wait(0.2)
    turnBy(45)
    wait(0.2)
    forward(.5,1)
    wait(0.2)
    backward(.5,1)
    wait(0.2)
    turnBy(-90)
    wait(0.2)
    forward(.5,.6)
    wait(0.2)
    turnBy(-45)
    wait(0.2)
    forward(.5,.1)
    wait(0.2)
    turnBy(135)

'''
def sPrintM():
def sPrintN():
def sPrintO():
def sPrintP():
def sPrintQ():
def sPrintR():
def sPrintS():
def sPrintT():
def sPrintU():
def sPrintV():
def sPrintW():
def sPrintX():
def sPrintY():
def sPrintZ():
'''

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

a="ABCDEFGHIJKL"
print(a)

for i in range(0,len(a)):
    print(a[i])
    scribblerPrint(a[i])

