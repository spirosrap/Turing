from time import sleep
import os
import sys
import threading
machine = [] #the machine currently running
state = 's1' #the state at which the current machine is at
position = 0 #the position at which the tape is reading 
tape = [] #the tape
endstates = [] #end states
tapelength = 0 #length of tape
stored = {}
speed = 10.0
maxlength = 46
printing = True

def behavior(moves):
    for b in moves:
        if b == 'R':
            moveright()
        elif b == 'L':
            moveleft()
        elif b == 'none':
            1 == 1
        elif b == 'E':
            delete()
        elif b[0] == 'P':
            write(b[1:])
        elif b[0] == 'S':
            store(b[1:])
        else:
            print("i don't know what move to make",move)
                
def moveright():
    global position
    position = position + 1
    printtape(state)
def moveleft():
    global position
    position = position - 1
    printtape(state)
def write(char):
    tape[position] = char
    printtape(state)
    #tape[position] = stored[char]
    #tape[position + 1] = char
def delete():
    tape[position] = "_"
    printtape(state)
def store(c):
    stored[c] = tape[position]        
    printtape(state)
def chkhead(s):
    if s == "all":
        return True
    elif s == "any":
        return tape[position]!="_"
    elif s == "none":
        return tape[position]=="_"        
    elif s[0] == "#":
        return tape[position] != s[1:] and tape[position] != "_"
    elif s[0] == "=":
        if s[1] == "#":
            return stored[s[2:]] != tape[position]
        else:
            return stored[s[1:]] == tape[position]    
            
    else:
        return tape[position] == s           


def execute():
    global state
    global position
    os.system('clear')        
    printtape()
    sleep(1/speed)
    while not(state in endstates):
        found = False
        inst = []
        for i in machine:
            if(i[0] == state and chkhead(i[1])):
                found = True
                inst = i
                break
        if(found):
            behavior(inst[2])
            state = inst[3]
            execute()
        else:
            print("error")
            exit()                
            
def reading():
    return tape[position]

def printtape(s):
    global state
    global position
    global tape
    global maxlength
    state = s
    if(printing):
        sleep(1/speed)
        os.system('clear')
        p = position
        halfmax = int(maxlength/2)
        if(position < halfmax):
            displayed = tape[:maxlength]
        elif (position > halfmax):
            if((position+halfmax) > len(tape)):
                displayed = tape[-(position+halfmax) + len(tape)+(position - halfmax):(position+halfmax)]
                p = halfmax + (position+halfmax) - len(tape)
            else:
                displayed = tape[(position - halfmax):(position+halfmax)]
                p = halfmax
        else:
            displayed = tape[:maxlength]
            p = halfmax
    
        print(' '.join(str(e) for e in displayed)," :state:->",state)
        temp = displayed[p]
        displayed[p] = '^'
        print(' '.join(str(e) if str(e) == '^' else " " for e in displayed))
        displayed[p] = temp
        
    
def printtape2(s):
    global state
    global position
    global tape
    global maxlength
    state = s
    
    print(' '.join(str(e) for e in tape)," :state:->",state)
    
stored = {"b":"1","c":"0","a":"0","t":"0","g":"0","s":"0"}

# instructions in user friendly format
# state - readingsymbol - behavior - nextstate
tape = "e e 0 a 0 a 0 c 0 b 0 b 1 c 1 C 0 c 0 a 0 a 0 c 0 b 0 b 1 c 1 C 0 c 0 a 0 a 0 c 0 b 0 b 1 c 1 C 0 c _ _ _ _ _ _ _ ".split()
tape1 = "e e 0 a 0 a 0 c 0 b 0 b 1 c 1 C 0 c _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _".split()

#for the machine I of 3 (prints 0101010101010...)
# The $ sign is the "::" symbol on Turing's paper
tape = "e e ; _ D _ A _ D _ D _ C _ R _ D _ A _ A _ ; _ D _ A _ A _ D _ D _ R _ D _ A _ A _ A _ ; "\
        "_ D _ A _ A _ A _ D _ D _ C _ C _ R _ D _ A _ A _ A _ A _ ; _ D _ A _ A _ A _ A _ D _ D _ R _ D _ A _ $ _ _ _ "\
        "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "\
        "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "\
        "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "\
        "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "\
        "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "\
        "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "\
        "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "\
        "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "\
        "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _".split()
        

#Abbreviated tables - further examples (4)
def f(a,b,c):
    printtape("f")
    if (tape[position] == "e"):
        moveleft()
        f1(a,b,c)
    elif (tape[position] != "e") and (tape[position] != "_"):
        moveleft()
        f(a,b,c)
    elif (tape[position] == "_"):
        moveleft()
        f(a,b,c)
        
    else:
        print("error")    
        exit()

def f1(a,b,c):
    printtape("f1")
    if (tape[position] == c):
        a()
    elif (tape[position] != c) and (tape[position] != "_"):
        moveright()
        f1(a,b,c)
    elif (tape[position] == "_"):
        moveright()
        f2(a,b,c)
    else:
        print("error")    
        exit()
        
def f2(a,b,c):
    printtape("f2")
    if (tape[position] == c):
        a()
    elif (tape[position] != c) and (tape[position] != "_"):
        moveright()
        f1(a,b,c)
    elif (tape[position] == "_"):
        b()
    else:
        print("error")    
        exit()
        
def H1():
    printtape("H1")        
def H2():
    printtape("H2")
def H3():
    printtape("H3")
    
def e1(a,b,c):
    printtape("e1")    
    delete()
    a()
        
def e(a,b,c):
    printtape("e(a,b,c)")
    if c == None:
        e(lambda: e(a,b,None),a,b)                        
    else:
        f(lambda:e1(a,b,c) ,b,c)  
            
def pe(a,b):
    printtape("p(a,b)")
    f(lambda:pe1(a,b),a,"e")
    
def pe1(a,b):
    printtape("pe1(a,b)")
    if (tape[position]!="_"):
        moveright()
        moveright()
        pe1(a,b)
    elif (tape[position]=="_"):
        write(b)
        a()
    else:
        print("error")
                
def l(a):
    printtape("l(a)")
    moveleft()
    a()
    
def r(a):
    printtape("r(a)")
    moveright()
    a()

def ft(a1,a2,a3):
    printtape("ft(a,b,c)")
    f(lambda:l(a1),a2,a3)
    
def ftt(a1,a2,a3):
    printtape("ftt(a,b,c)")
    f(lambda:r(a1),a2,a3)
    
def ca(a1,a2,a3):
    printtape("c(a,b,c)")
    ft(lambda:c1(a1),a2,a3)
    
def c1(a1):
    printtape("c1(a)")
    pe1(a1,tape[position])
    
def ce(a1,a2,a3):
    if(a3 == None):
        printtape("ce(a,b)")
        ce(lambda:ce(a1,a2,None),a1,a2)
    else:
        printtape("ce(a,b,c)")
        ca(lambda:e(a1,a2,a3),a2,a3)
        
def re(a,b,c,d):
    if(d == None):
        printtape("re(a,b,c)")
        re(lambda:re(a,b,c,None),a,b,c)
    else:
        printtape("re(a,b,c,d)")
        f(lambda:re1(a,b,c,d),b,c)
    
def re1(a,b,c,d):
    printtape("re1(a,b,c,d)")
    delete()
    write(d)
    a()
    
def cr(a,b,c):
    if(c == None):
        printtape("cr(a,b)")
        cr(lambda:cr(a,b,None),lambda:re(a,"t",b,None),b)
    else:    
        printtape("cr(a,b,c)")
        ca(lambda:re(a,b,c,"t"),b,c)
    
    
def cp(a1,a2,a3,a4,a5):
    printtape("cp(a1,a2,a3,a4,a5)")
    ft(lambda:cp1(a1,a2,a5),lambda:f(a2,a3,a5),a4)
    
def cp1(a,b,c):
    printtape("cp1(a,b,c)")
    store("g")
    ft(lambda:cp2(a,b,"g"),b,c)    
    
def cp2(a,b,c):
    printtape("cp2(a,b,c)")
    if(stored[c] == tape[position]):
        a()
    else:
        b()        
        
def cpe(a1,a2,a3,a4,a5):
    if(a5==None):
        printtape("cpe(a1,a2,a3,a4)")
        cpe(lambda:cpe(a1,a2,a3,a4,None),a1,a2,a3,a4)
    else:
        printtape("cpe(a1,a2,a3,a4,a5)")
        cp(lambda:e(lambda:e(a1,a1,a5),a1,a4),a2,a3,a4,a5)        
    
def q(a1,a2):
    if(a2==None):
        printtape("q(a1)")
        if (tape[position] != "_"):
            moveright()
            q(a1,None)
        elif (tape[position] == "_"):
            moveright()
            q1(a1,None)
        else:
            print("error")    
    else:
        printtape("q(a1,a2)")
        q(lambda:q1(a1,a2),None)
                    
def q1(a1,a2):
    if(a2==None):
        printtape("q1(a1)")
        if (tape[position] != "_"):
            moveright()
            q(a1,None)
        elif (tape[position] == "_"):
            moveright()
            a1()
        else:
            print("error")
    else:
        printtape("q1(a1,a2)")
        if (tape[position] == a2):
            a1()
        elif (tape[position] != a2):
            moveleft()
            q1(a1,a2)
        else:
            print("error")

def pe2(a1,a2,a3):
    printtape("pe2(a1,a2,a3)")
    pe(lambda:pe(a1,a3),a2)

def ce2(a1,a2,a3):
    printtape("ce2(a1,a2,a3)")
    ce(lambda:ce(a1,a3,None),a2,None)
    
def ce3(a1,a2,a3,a4):
    printtape("ce3(a1,a2,a3,a4)")    
    ce(lambda:ce2(a1,a3,a4),a2,None)
    
def ce4(a1,a2,a3,a4,a5):
    printtape("ce4(a1,a2,a3,a4,a5)")
    ce(lambda:ce3(a1,a3,a4,a5),a2,None)
    
def ce5(a1,a2,a3,a4,a5,a6):
    printtape("ce4(a1,a2,a3,a4,a5,a6)")
    ce(lambda:ce4(a1,a3,a4,a5,a6),a2,None)
            

def el(a1):
    printtape("el(a1)")    
    if (tape[position] == "e"):
        moveright()
        el1(a1)
    elif (tape[position] != "e"):
        moveleft()
        el(a1)
    else:
        print("error")
        
def el1(a1):
    printtape("el1(a1)")
    if (tape[position] != "_"):
        moveright()
        delete()
        moveright()
        el1(a1)
    elif (tape[position] == "_"):
        a1()
    else:
        print("error")
        
            
#start machine    

#f(H1,H2,"b")
#e(H1,H2,"a")
#e(H2,"a",None)
#pe(H2,"b")
#ft(H1,H2,"a")
#ca(H1,H2,"a")
#ce(H2,"a",None)
#re(H1,"a","b",None)
#cr(H1,"a",None)
#cp(H1,H2,H3,"a","b")
#cpe(H1,H2,H3,"a","b")
#cpe(H1,H2,"a","b",None)
#q(H1,"b")
#pe2(H1,"a","b")
#ce3(H1,"a","b","c")
#el(H1)

#Detailed description of the universal machine

#Subsidiary skeleton table
def con(a1,a2):
    printtape("con(a1,a2)")
    if(tape[position]  == "A"):
        moveleft()
        write(a2)
        moveright()
        con1(a1,a2)
    elif(tape[position]  != "A"):
        moveright()
        moveright()
        con(a1,a2)        
    else:
        print("error con(a1,a2)")
        
def con1(a1,a2):
    printtape("con1(a1,a2)")
    if(tape[position] == "A"):
        moveright()
        write(a2)
        moveright()
        con1(a1,a2)
    elif(tape[position] == "D"):
        moveright()
        write(a2)
        moveright()
        con2(a1,a2)        
    else:
        print("error con1(a1,a2)")

def con2(a1,a2):
    printtape("con2(a1,a2)")
    if(tape[position]  == "C"):
        moveright()
        write(a2)
        moveright()
        con2(a1,a2)
    elif(tape[position] != "C"):
        moveright()
        moveright()
        a1()        
    else:
        print("error con2(a1,a2)")
            
#The table for Universal Machine
#The machine prints :DAD on the F-squares after ::->anf
def b():
    printtape("b")
    f(lambda:b1(),lambda:b1(),"$")
    
def b1():
    printtape("b1")
    moveright()
    moveright()
    write(":")    
    moveright()
    moveright()
    write("D")
    moveright()
    moveright()
    write("A")
    moveright()
    moveright()
    write("D")    
    anf()    

#The machine marks the configuration in the last complete configuration with y. ->kom
def anf():
    printtape("anf")
    q(lambda:anf1(),":")
    
def anf1():
    printtape("anf1")
    con(lambda:kom(),"y")

#The machine finds the last semicolon not marked with z. 
#It marks this semicolon with z and the configuration following it with x    
def kom():
    printtape("kom")    
    if(tape[position] == ";"):
        moveright()
        write("z")
        moveleft()
        con(lambda:kmp(),"x")
    elif(tape[position] == "z"):
        moveleft()    
        moveleft()
        kom()
    elif(tape[position] == "e"):
        fail1()    
    elif (not (tape[position] == "z")) and  (not(tape[position] == ";")) and (not (tape[position] == "e")):
        moveleft()
        kom()
    else:
        print("error: kom()")

#The machine compares the sequences marked x and y. It erases all letters x and y
#->sim if they are alike. Otherwise kom.    
def kmp():
    #exit()
    printtape("kmp")
    cpe(lambda:e(lambda:e(lambda:anf(), "x",None), "y",None), lambda:sim(), "x", "y",None)
    
def fail1():
    printtape("fail-1")
    
#The machine marks out the instructions. That part of the instructions which
#refers to operations to be carried out is marked with u, and the final m-configuration with y.
#The letters z are erased
def sim():
    printtape("sim")
    ft(lambda:sim1(),lambda:sim1(),"z")
    
def sim1():
    printtape("sim1")
    con(lambda:sim2(),"_")
    
def sim2():
    printtape("sim2")
    if(tape[position] == "A"):
        sim3()
    elif(tape[position] != "A"):
        moveleft()
        write("u")        
        moveright()
        moveright()
        moveright()
        sim2()
    else:
        print("error sim2")
                                    

def sim3():
    printtape("sim3")
    if(tape[position] != "A"):
        moveleft()
        write("y")
        e(lambda:mk(),"z",None)        
    elif(tape[position] == "A"):
        moveleft()
        write("y")        
        moveright()
        moveright()
        moveright()
        sim3()
    else:
        print("error sim2")    

#mk. The last complete configuration is marked out into four sections. 
#The configuration is left unmarked. The symbol directly
#preceding it is marked with x. The remainder of the complete conWguration is 
#divided into two parts, of which the first is marked
#with v and the last with w. A colon is printed after the whole. -> sh.

def mk():
    printtape("mk()")
    q(lambda:mk1(),":")
    
def mk1():
    printtape("mk1()")
    if(tape[position] != "A"):
        moveright()
        moveright()
        mk1()
    elif (tape[position] == "A"):
        moveleft()
        moveleft()
        moveleft()
        moveleft()
        mk2()
    else:
        print("error mk1()")

def mk2():
    printtape("mk2()")
    if(tape[position] == "C"):
        moveright()          
        write("x")
        moveleft()
        moveleft()         
        moveleft()
        mk2()
    elif(tape[position] == ":"):
        mk4()
    elif(tape[position] == "D"):            
        moveright()
        write("x")
        moveleft()
        moveleft()
        moveleft()
        mk3()
    else:
        print("error mk2()")
        
def mk3():
    printtape("mk3()")
    if(tape[position] != ":"):
        moveright()
        write("v")
        moveleft()
        moveleft()
        moveleft()
        mk3()
    elif(tape[position] == ":"):
        mk4()
    else:
        print("error: mk3()")
        
def mk4():
    printtape("mk4()")           
    con(lambda:l(lambda:l(lambda:mk5())),"_")
    
def mk5():
    printtape("mk5()")
    if(tape[position] != "_"):
        moveright()
        write("w")
        moveright()
        mk5()
    elif(tape[position == "_"]):
        write(":")
        sh()         

#sh. The instructions (marked u) are examined. If it is found that they involve "Print 0"
#or "Print 1", then 0 : or 1 : is printed at the end.

def sh():
    printtape("sh()")
    f(lambda:sh1(),lambda:inst(),"u")
    
def sh1():
    printtape("sh1()")    
    moveleft()
    moveleft()
    moveleft()
    sh2()

def sh2():
    printtape("sh2()")
    if(tape[position] == "D"):
        moveright()            
        moveright()
        moveright()
        moveright()
        sh3()
    elif(tape[position] != "D"):
        inst()
    else:
        print("error sh2()")
        
def sh3():
    printtape("sh3()")                                    
    if(tape[position] == "C"):
        moveright()
        moveright()
        sh4()
    elif(tape[position] != "C"):
        inst()
    else:
        print("error: sh3()")
        
def sh4():
    printtape("sh4()")
    if(tape[position] == "C"):
        moveright()
        moveright()
        sh5()
    elif(tape[position] != "C"):
        pe2(lambda:inst(),"0",":")
    else:
        print("error: sh4()")

def sh5():            
    printtape("sh5()")
    if(tape[position] == "C"):
        inst()
    elif(tape[position] != "C"):
        pe2(lambda:inst(),"1",":")
    else:
        print("error: sh5()")

def inst():
    H1()
            
def instTEST():
    printtape("inst()")
    q(lambda:l(lambda:inst1(None)),"u")
    
def inst1(a1):         
    if(a1 == None):
        printtape("inst1()")
        a = tape[position]
        moveright()
        delete()
        inst1(a)
    elif (a1 == "R"):
        printtape("inst(a1)")
        ce5(lambda:q(lambda:inst2(),"A"),"v", "x", "u", "y", "w")
    elif (a1 == "L"):
        f(lambda:inst4(),lambda:fail2(),"x")
    elif (a1 == "N"):
        ce5(lambda:ov(),"v", "x", "y", "u", "w")
    else:
        print("error: inst1(a1)")    
        
    
def inst2():
    printtape("inst2()")
    moveright()        
    moveright()
    inst3()
    
def inst3():
    printtape("inst3()")
        
    if(tape[position] == "_"):
        write("D")
        ov()
    elif (tape[position] == "D"):
        ov()
    else:
        print("error: inst3()")        
        
def inst4():
    printtape("inst4()")
    ce5(lambda:ov(),"v","y","x","u","w")

def fail2():
    printtape("Fail - 2")

        
def ov():
    printtape("ov()")
    el(lambda:anf())

printing = False

def main2():
    global speed,position,tape,printing
    speed = 10.0
    position = 4
    tape = "e e 0 a 0 a 0 c 0 b 0 b 1 c 1 C 0 c 0 a 0 a 0 c 0 b 0 b 1 c 1 C 0 c 0 a 0 a 0 c 0 b 0 b 1 c 1 C 0 c _ _ _ _ _ _ _ ".split()
    printing = True
    pe(lambda:H2(),"0")
        
def main():
    speed = 260.0
    position = 4
    b()

    instTEST()
    os.system('clear')    
    printtape2("1")
    sleep(2)
    os.system('clear')
    
    instTEST()
    os.system('clear')    
    printtape2("1")
    sleep(2)
    os.system('clear')

    instTEST()
    os.system('clear')    
    printtape2("1")
    sleep(2)
    os.system('clear')
    
    instTEST()
    os.system('clear')    
    printtape2("1")
    sleep(2)
    os.system('clear')
    
    instTEST()
    os.system('clear')    
    printtape2("1")
    sleep(2)
    os.system('clear')
    
    instTEST()
    os.system('clear')    
    printtape2("1")
    sleep(2)
    os.system('clear')
    
    instTEST()
    os.system('clear')    
    printtape2("1")
    sleep(2)
    os.system('clear')
    
    instTEST()
    os.system('clear')    
    printtape2("1")
    sleep(2)
    os.system('clear')
    
    instTEST()
    os.system('clear')    
    printtape2("1")
    sleep(2)
    os.system('clear')
    
    instTEST()
    os.system('clear')    
    printtape2("1")
    sleep(2)
    os.system('clear')
    
    instTEST()
    os.system('clear')    
    printtape2("1")
    sleep(2)
    os.system('clear')
    
    instTEST()
    os.system('clear')    
    printtape2("1")
    sleep(2)
    os.system('clear')
    
    instTEST()
    os.system('clear')    
    printtape2("1")
    sleep(2)
    os.system('clear')
    

    printtape2(state)
        
    
if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target
    
#ce(lambda:H1(),"y",None)
#tape = "e e 0 a 0 a 0 c 0 b 0 b 1 c 1 C 0 c _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _".split()
#cpe(lambda:H1(),lambda:H2(),"a","b",None)
