from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
time = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global time
    window.after_cancel(time)
    l1.config(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 42, "bold"))
    l4.config(fg=GREEN, font=(FONT_NAME, 8, "bold"))
    canvas.itemconfig(timer,text ="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global rep
    rep += 1
    work_sec = WORK_MIN*60
    break_sec = SHORT_BREAK_MIN*60
    long_sec = LONG_BREAK_MIN*60
    if rep%2 != 0:
        l1.config(text="WORK", fg=RED, bg=YELLOW, font=(FONT_NAME, 42, "bold"))
        count_down(work_sec)
    elif rep %2 ==0:
        l1.config(text="REST", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 42, "bold"))
        count_down(break_sec)
    elif rep % 8==0:
        l1.config(text="BREAK:))", fg=PINK, bg=YELLOW, font=(FONT_NAME, 42, "bold"))

        count_down(long_sec)

    #count_down(2*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global time
    min = count//60
    sec = count%60

    if sec <10:
        sec = f"0{sec}"
    if min <10:
        min = f"0{min}"

    canvas.itemconfig(timer,text=f"{min}:{sec}")
    if count>0:
       time =  window.after(1000,count_down,count-1)
    else:
        start()
        if rep%2 ==0:
            x = rep//2
            text = "✅"
            text *= x
            l4.config(text=f"{text}",fg=GREEN, font=(FONT_NAME, 8, "bold"))


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50,bg=YELLOW)



canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
canvas.image = tomato
timer = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


#title
l1 = Label()
l1.config(text="TIMER",fg=GREEN,bg=YELLOW,font=(FONT_NAME,42,"bold"))
l1.grid(column=1,row=0)

#start
l2 = Button(text="Start",highlightthickness=0,command=start)
l2.grid(column=0,row=3)

#reset
l3 = Button(text="reset",highlightthickness=0,command=reset)
l3.grid(column=2,row=3)

#checkmark
#text = "✅"
l4 = Label()
l4.config(fg=GREEN,font=(FONT_NAME,8,"bold"))
l4.grid(column=1,row=4)








window.mainloop()










