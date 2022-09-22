from tkinter import *
from settings import *

app = Tk()
app.config(bg=BLACK)
app.title(APP_NAME)
app.minsize(550, 550)
app.maxsize(550, 550)

canvas = Canvas(app, height=600, width=300, bg=BLACK, highlightthickness=0)
img = PhotoImage(file='police.png')
canvas.create_image(150, 290, image=img)


canvas_wid = Frame(bg=BLACK)
Label(canvas_wid, text='SIGN_UP', bg=WHITE, font=FONT, fg=BLUE).grid(row=0, column=0, columnspan=2, ipadx=30,
                                                                           sticky='news')
Label(canvas_wid, text='Full Name:', bg=BLACK, fg=BLUE).grid(row=1, column=0, ipadx=10, sticky='news')
user = Entry(canvas_wid)
user.grid(row=1, column=1, pady=5, sticky='news')

Label(canvas_wid, text='Age:', bg=BLACK, fg=BLUE).grid(row=2, column=0, ipadx=10, sticky='news')
user = Entry(canvas_wid)
user.grid(row=2, column=1, pady=5, sticky='news')

Label(canvas_wid, text='Gender:', bg=BLACK, fg=BLUE).grid(row=3, column=0, ipadx=10, sticky='news')
user = Entry(canvas_wid)
user.grid(row=3, column=1, pady=5, sticky='news')

Label(canvas_wid, text='Username:', bg=BLACK, fg=BLUE).grid(row=4, column=0, ipadx=10, sticky='news')
user = Entry(canvas_wid)
user.grid(row=4, column=1, pady=5, sticky='news')

Label(canvas_wid, text='Password:', bg=BLACK, fg=BLUE).grid(row=5, column=0, ipadx=10, sticky='news')
user = Entry(canvas_wid)
user.grid(row=5, column=1, pady=5, sticky='news')

Button(canvas_wid, text='SUBMIT', bg=WHITE, font=FONT, relief=FLAT, fg=BLUE).grid(row=6, ipady=3, column=1, pady=10,
                                                                                        columnspan=2,
                                                                                        sticky='news')

canvas.create_window(400, 280, window=canvas_wid)
canvas.grid(row=0, column=0)


app.mainloop()