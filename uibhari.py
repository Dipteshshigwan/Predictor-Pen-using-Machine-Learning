from tkinter import *
from tkinter.ttk import Frame, Button, Label, Style
import time
import socket

running = False
#idx = 0

def start():
    global running
    running = True

def stop():
    global running
    running = False
        
def emessage():
    area.delete(0.0, 'end')
    print("Erased")

def hpage():
    top = Toplevel()
    top.title("Help")
    top.geometry("350x300+300+300")

def spage():
    top = Toplevel()
    top.title("Setting")
    top.geometry("350x300+300+300")

def emode():
     
    #top = Toplevel()
    canvas_width = 500
    canvas_height = 150
    
    def emessage1():
        area1.delete(ALL)
        print("Erased")
    
    def hpage():
        top = Toplevel()
        top.title("Help")
        top.geometry("350x300+300+300")
    
    def spage():
        top = Toplevel()
        top.title("Setting")
        top.geometry("350x300+300+300")
    
    def paint( event ):
        python_green = "#476042"
        x1, y1 = ( event.x - 2 ), ( event.y - 2 )            #co-ordinates to be feed in....
        x2, y2 = ( event.x + 2 ), ( event.y + 2 )
        x3, y3 = ( event.x + 1 ), ( event.y + 1 )
        x4, y4 = ( event.x - 1 ), ( event.y - 1 )
        #w.create_oval( x1, y1, x2, y2, fill = python_green )
        area1.create_line( x1, y1, x2, y2, x3, y3, x4 , y4, fill = python_green)
    
       #button = ttk.Button(main_frame, text='Flip pen color')
       #button.grid()
       #button['command'] = lambda: flip_pen_color(pen_data)
    
    #signal=1
    
    top = Tk()
    top.geometry("350x300+300+300")
    
    top.title( "Predictor World!" )
    
    top.columnconfigure(1, weight=1)
    top.columnconfigure(3, pad=7) 
    top.rowconfigure(3, weight=1)
    top.rowconfigure(5, pad=7)

    lbl = Label(top, text="Gesture Identified....(Free-Hand Mode)")
    lbl.grid(sticky=W, row=0, column=0)
    
    area1 = Canvas(top, width=canvas_width, height=canvas_height)
    area1.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E+W+S+N)  
    #area1.pack(fill = BOTH, expand = True)
    area1.bind( "<B1-Motion>", paint )
    
    '''stop = Button(top, text="Activate")
    stop.grid(row=1, column=3)
    start = Button(top, text="Deactivate")
    start.grid(row=2, column=3)'''

    close = Button(top, text="Close", command=top.destroy)
    close.grid(row=1, column=3)
    
    bbtn = Button(top, text="Clear", command=emessage1)
    bbtn.grid(row=3, column=3)
    
    nbtn = Button(top, text="Mode")
    nbtn.grid(row=4, column=3, pady=4)
        
    hbtn = Button(top, text="Help", command=hpage)
    hbtn.grid(row=5, column=0, padx=5)
    
    sbtn = Button(top, text="Setting", command=spage)
    sbtn.grid(row=5, column=3)
    
    #message = Label( top, text = "Press and Drag the mouse to draw" )
    #message.pack( side = BOTTOM )  
        
    #mainloop()

###########################################################################################################

#def ask():
    #op = input("Enter")
    #return op

    
master = Tk()

master.geometry("350x300+300+300")

master.title("Predictor World!")

master.columnconfigure(1, weight=1)
master.columnconfigure(3, pad=7) 
master.rowconfigure(3, weight=1)
master.rowconfigure(5, pad=7)

lbl = Label(master, text="Gesture Identified....")
lbl.grid(sticky=W, row=0, column=0)

area = Text(master)
area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E+W+S+N)

start = Button(master, text="Activate", command=start)
start.grid(row=1, column=3)
stop = Button(master, text="Deactivate", command=stop)
stop.grid(row=2, column=3)

bbtn = Button(master, text="Clear", command=emessage)
bbtn.grid(row=3, column=3)

nbtn = Button(master, text="Mode", command=emode)
nbtn.grid(row=4, column=3, pady=4)
        
hbtn = Button(master, text="Help", command=hpage)
hbtn.grid(row=5, column=0, padx=5)

sbtn = Button(master, text="Setting", command=spage)
sbtn.grid(row=5, column=3)


while True:
    #if idx % 5 == 0:
    master.update()
        
        
    if running:
        #time.sleep(1)
        print("Recieved")
        try:
            s = socket.socket()
            host = socket.gethostname()
            port = 12345
            s.connect((host, port))
            print("Connecting Established")
            letter = s.recv(1024).decode()
            area.insert(5.0,letter)       #To be taken input in variable String
        except ValueError:
            print()
        #idx += 1

master.mainloop()


