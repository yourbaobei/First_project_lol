import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, bg="white", height=400, width=400)
for i in range(50, 400, 50):
    canvas.create_line((0, i), (400, i), fill="black")
    canvas.create_line((i, 0), (i, 400), fill="black")
canvas.pack()
tk.mainloop()