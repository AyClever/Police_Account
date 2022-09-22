from tkinter import *
from settings import *

app = Tk()
app.config(bg=BLUE)
app.title(APP_NAME)
app.minsize(700, 450)
app.maxsize(700, 450)


canvas = Canvas(app, width=700, height=500, bg=BLUE, highlightthickness=0)
img = PhotoImage(file='rsz_1station.png')
canvas.create_image(200, 260, image=img)
canvas.grid(row=0, columnspan=2)

canvas_wid = Frame()
Label(canvas_wid, text=APP_NAME, bg=BLUE, fg=BLACK, font=FONT).grid()
canvas.create_window(250, 40, window=canvas_wid)
canvas.grid(row=0, columnspan=3)

sign_up_wid = Frame(bg=BLUE)
Button(sign_up_wid, text='SIGN UP', bg=BLACK, fg=WHITE, font=FONT, relief=FLAT).grid()
canvas.create_window(200, 115, window=sign_up_wid)
canvas.grid(row=0, columnspan=2)

login_wid = Frame(bg=BLUE)
Button(login_wid, text='LOGIN', bg=BLACK, fg=WHITE, font=FONT, relief=FLAT).grid()
canvas.create_window(330, 115, window=login_wid)
canvas.grid(row=0, columnspan=2)


canvas_frame = Canvas(app, height=550, width=700, bg=BLUE, highlightthickness=0)
img2 = PhotoImage(file='crime3.png')
canvas.create_image(540, 300, image=img2)
canvas.grid(row=0, column=2)


app.mainloop()
