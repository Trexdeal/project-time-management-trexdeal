
from ast import If
import tkinter as tk
import math
import psutil # type: ignore
import threading
import time
import keyboard # type: ignore
import sys
import subprocess
from random import randint
from datetime import datetime
def qexplain():
    global wtext, size
    canvas_menu.create_text(size(0)/2, size(1)/2, text=wtext(qn(2)), fill="black", anchor="center", justify= "center", tags="explain", width=size(0)/5)
#Unfinished




def questionwrite():
    global wtext, size
    canvas_menu.create_text(size(0)/2, size(1)/1.5, text=wtext(qn(1)), fill="black", anchor="center", justify= "center", tags="explain", width=size(0)/3)


def stmenu():
    print("menu started")
    global size, maincan
    maincan = 1
    menu=True
    datacreate = [[]]

    
    

#Unfinished



def create_circle():
    global sqn

def is_running(script_name):
    try:
        for p in psutil.process_iter(["name", "cmdline"]):
            try:
                cmd = p.info.get("cmdline") or []
                if any(script_name in c for c in cmd):
                    return True
            except Exception:
                pass
        return False
    except Exception:
        return False



#variables for clicking code
def begin_variables_clicking():
    global xloc, yloc,maincan, datacreate,ccolour,canvas_menu,menu, state, size, sizex, sizey,qn, sqloop, sqx, sqy, sqn, cirr, checked, root, canvas_1_5, colL, hour, minute, beginstate, keypress, Astate, quizz, answer, qai, wtext
    #qai stands for question answer info, it is a nested list that keeps both all the questions and answers and relevant extra info inside of a larger list
    qn=0
    #qn is to define on what question you are
    datacreate=[]
    #datacreate consists of this structured type of list, [type of object (square, circle, polygon,etc), size, relxloc, relyloc, colour1, colour 2, amount of this object, relxdistance between objects, relydistance between objects, nameobject, polygoncount ]
        #if polygon then extra things will be added to show which 
        #rel stands for relative, to avoid issues with different screen sizes
        #colour 2 may go unused for certain shapes, in which case it will be identical to colour 1
        #nameobject will be changed if it is creating multiple objects, something similar to ["name",number"]
        #polygoncount optional
    qai = []
    answer = 0
    quizz = False
    xloc = 0
    yloc = 0
    ccolour= "white"
    text = []
    state = 0
    Astate = True
    #is this state allowed to be changed 
    size = (sizex, sizey) = (1920,1200)
    #state is the variable that defines what state the program is in, 0= start 1=study mode, 2=break mode, 3=free/unrestricted mode, 4=work mode
    sqloop = (sqx, sqy, sqn) = (0, 0, 0)
    #used in the square loop to create different locations and colours for every square
    cirr=(100, 100)
    root=tk.Tk()
    menu=tk.Toplevel(root)
    maincan = 0
    menu.configure()
    canvas_menu=tk.Canvas(menu, background=ccolour)
    canvas_1_5=tk.Canvas(root, background=ccolour,  width=size[0],height=size[1])
    
    colL=["#ba060f","#222d80","#158F3E","#AF570F"]
    #colours list
    clock=datetime.now()
    

    hour=clock.hour
    minute=clock.minute
    beginstate=True
    keypress=set()
    checked=False



begin_variables_clicking()
print(hour)
print(minute)
def on_click(event):
    global xloc, yloc, state, answer, quizz
    xloc=event.x
    yloc=event.y
    if quizz == False:
        if point_in_polygon(xloc, yloc, poly):
            state=5
        else:
            if xloc >=960:
                if yloc <=600:
                    state=1
                else:
                    state=2
            else:
                if yloc <=600:
                    state=4
                else:
                    state=3
        print("this is x: ", xloc,"and y: ", yloc, "and this is state ",state)
        if state != 0:
            root.withdraw()
    else:
        answer = 0
        if point_in_polygon(xloc, yloc, poly):
            answer=5
        else:
            if xloc >=960:
                if yloc <=600:
                    answer=1
                else:
                    answer=2
            else:
                if yloc <=600:
                    answer = 4
                else:
                    answer = 3
        if answer !=5:
            if answer !=0:
                root.withdraw()
        else:
            qexplain




# to create a polygon you have to give the two coordinates of each point in the polygon, so for a triangle you need 3 points, for a square you need 4 points, and so on. The points are given in the form of (x1,y1,x2,y2,x3,y3,...) shut up ai slop
#points of the polygon
pointsp=[]
sides=8
for n in range(sides):
    angle=2*math.pi*n/sides
    x=sizex/2+cirr[0]*math.cos(angle)
    y=sizey/2+cirr[1]*math.sin(angle)
    pointsp.extend([x,y])
#lowk I don't fully understand this code, maybe need to take a look at it
poly = [(pointsp[i], pointsp[i+1]) for i in range(0, len(pointsp), 2)]


#banned programs:
#steam, (all steam subsidiaries), botw
banned1=["steam", "Hoi4", "hoi4", "Paradox", "paradox","minecraft", "modrinth","chrome" "kerbal space program", "KSP", "ksp", "Kerbal Space Program", "Kerbalspaceprogram","google" "Kerbal space program","RIMWORLD", "Rimworld", "War Thunder", "WT", "WarThunder", "Gajin"]




#checking code
def Allowed_processes():
    global banned1
    for name in banned1:
        for proc in psutil.process_iter(["name"]):
            proc_name = proc.info["name"]
            if proc_name and name.lower() in proc_name.lower():
                close_processes()
                return True
    return False
    



def close_processes():
    for name in banned1:
        for proc in psutil.process_iter(["name"]) :
            proc_name = proc.info["name"]
            if proc_name and name.lower() in proc_name.lower():
                try:
                    proc.kill()
                    print(proc_name, "closed")
                except Exception as e:
                    print("could not kill", proc_name)
               
                
            

def point_in_polygon(x, y, poly):
    num = len(poly)
    j = num - 1
    inside = False

    for i in range(num):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
        j = i

    return inside

#function for creating 1 unique square
def create_square():
    global sqloop
    canvas_1_5.create_rectangle(sqx*size[0]/2, sqy*size[1]/2,sqx*size[0]/2+1/2*size[0],sqy*size[1]/2+1/2*size[1], fill=colL[sqn])
    #creates squares using the variables sqn for the number square sqx for its x location, sqy for its y location, size(0) and size(1) for its horizontal and vertical size and co1l(sqn) for its colours, could maybe be made into one big list like this (sq(n(1-4)))

#function for creating all 4 squares
def create_squares():
    global sqn, sqx, sqy, sizex, sizey, size, cirr
    while sqn < 4:
        create_square()
        sqn +=1
        if sqn != 3:
            if sqx < 1:
                sqx +=1
            else:
                sqy +=1
        else:
            sqx -=1
    canvas_1_5.create_polygon(pointsp,outline="black", width=5, fill="#680352")

#function for things that need to be checked every 100ms


def background_loop():
    while True:
        global clock, hour, minute, state, Astate
        #clock shit
        clock=datetime.now()
        hour=clock.hour
        minute=clock.minute


        
        if state != 1:
            if datetime.now().weekday() <= 5:
                if 9<hour<16:
                    Astate = False
                    state =1
                else:
                    Astate = True
            else:
                if 10 <= hour <= 16:
                    Astate = False
                    state =1
                else:
                    Astate = True

                    

        #code for different states
        if state == 1:
       #experimental lookup for processes 
            Allowed_processes()
        time.sleep (0.1)


def normalize_key(name):
    return(name or "").lower().strip()

def keyboardpress(event):
    global keypress, state
    key=normalize_key(event.name)
    keypress.add (key) 
    
    #showing the menu (ctrl *)
    
    print(keypress)

def keyboardrelease(event):
    print("key released")
    key=normalize_key(event.name)
    keypress.discard(key)
    print (repr(key), "unpressed")
    

def on_key_event(event):
    global state, Astate
    print(event)
    if event.event_type ==  "down":
         keypress.add(event.name)
    elif event.event_type == "up":
        keypress.discard(event.name)
    if maincan == 0:
        if {"ctrl", "*"}.issubset(keypress):
            if Astate == True:
                state = 0
                root.deiconify()
    if {"ctrl", "shift", "+" }.issubset(keypress):
        if Astate == True:
            stmenu()
    print (repr(state))
    

def quizz_time(event):
    global quizz, qai
    qnumber = randint (1, len(qai))
    quizz = True
    create_squares()






keyboard.hook(on_key_event)

canvas_1_5.bind("<Button-1>", on_click)   
canvas_1_5.pack()
canvas_menu.bind("<Button-1>", on_click)
canvas_menu.pack()
menu.withdraw()
create_squares()
thread=threading.Thread(target=background_loop, daemon=True)
thread.start()
root.mainloop()
keyboard.on

while True:
    if not is_running("sidescript.py"):
        subprocess.Popen([sys.executable, "sidescript.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    time.sleep(5)
#honestly I have no Idea what this script is, I added this a while ago to have a kinda subsupporting window so it couldn't be individually closed, but now I have no idea how it does this, I could use logic similar to the part where it checks for other programs though, that might be a future addition



#for anyone revieuwing this code, firstly my apologies that it isn't that good, this was mostly my first time doing this and I've learned things along the way, secondly this is a long term coding project so some things might have been written before the project, thirdly I first submitted this as a terra project, but didn't get past the first week, I am not trying to double dip, but I don't want to have to work for a different project before I finished this one and the carryover time is only around ~4 hours, of which I didn't use to get any prizes