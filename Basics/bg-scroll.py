import tkinter

x = 0
def scroll_bg():
    global x
    x = x + 1
    if x == 480:
        x = 0
    canvas.delete("BG")
    canvas.create_image(x-240, 150, image=img_bg, tag="BG")
    canvas.create_image(x+240, 150, image=img_bg, tag="BG")
    root.after(50, scroll_bg)

root = tkinter.Tk()
root.title("BG Print")
canvas = tkinter.Canvas(width=480, height=300)
canvas.pack()
img_bg = tkinter.PhotoImage(file="park.png")
#canvas.create_image(240, 150, image=img_bg)
scroll_bg()
root.mainloop()