from tkinter import *
from settings import *

app = Tk()
app.config(bg=YELLOW)
app.title(APP_NAME)
app.minsize(700, 550)
app.maxsize(700, 550)

canvas = Canvas(app, height=600, width=300, bg=WHITE, highlightthickness=0)
img = PhotoImage(file='police.png')
canvas.create_image(150, 290, image=img)
canvas.grid(row=0, column=0)

canvas_wid = Canvas(app, height=600, width=500, bg=YELLOW, highlightthickness=0)
bg_image = PhotoImage(file='rsz_emer.png')
canvas_wid.create_image(200, 80, image=bg_image)
bg_image1 = PhotoImage(file='rsz_police-car.png')
canvas_wid.create_image(200, 430, image=bg_image1)
login_wid = Frame(bg=YELLOW)
Label(login_wid, text='LOGIN', bg=YELLOW, fg=BLUE, font=FONT).grid(row=0, column=0, columnspan=2, ipadx=50,
                                                                   sticky='news')
Label(login_wid, text='Username', bg=YELLOW, fg=BLUE).grid(row=1, column=0, ipadx=10, sticky='news')
user = Entry(login_wid)
user.grid(row=1, column=1, pady=5, sticky='news')

Label(login_wid, text='Password', bg=YELLOW, fg=BLUE).grid(row=2, column=0, ipadx=10, sticky='news')
password = Entry(login_wid)
password.grid(row=2, column=1, pady=5, sticky='news')

login = Button(login_wid, text='LOGIN', relief=FLAT, bg=BLUE, fg=WHITE)
login.grid(row=3, column=1, pady=5, sticky='news')

fg_paswd = Label(login_wid, text='Forget Password?', bg=YELLOW, fg=BLUE)
fg_paswd.grid(row=4, columnspan=3, pady=20, sticky='news')

canvas_wid.grid(row=0, column=1)
canvas_wid.create_window(200, 230, window=login_wid)

app.mainloop()
