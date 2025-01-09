import tkinter as tk
import tkinter.ttk

def draw_solid_purple_large_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+200, starty+200, fill="purple")

def draw_solid_purple_small_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+50, starty+50, fill="purple")

def draw_hollow_purple_large_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+200, starty+200, fill="purple")
  canvas.create_rectangle(startx+50, starty+50, startx+150, starty+150, fill="white")

def draw_hollow_purple_small_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+50, starty+50, fill="purple")
  canvas.create_rectangle(startx+15, starty+15, startx+35, starty+35, fill="white")

def draw_solid_purple_large_circle(canvas: object, startx: int, starty: int) -> None:
  canvas.create_oval(startx, starty, startx+200, starty+200, fill="purple")

def test():
  root = tk.Tk()
  root.title('Shapes')
  root.geometry('500x500')

  canvas = tk.Canvas()
  canvas.pack(fill=tk.BOTH, expand=1)
  canvas.configure(bg="white")

  draw_solid_purple_large_square(canvas, 0, 0)
  draw_hollow_purple_large_square(canvas, 0, 0)
  draw_hollow_purple_small_square(canvas, 300, 300)
  draw_solid_purple_large_circle(canvas, 2, 2)

  root.mainloop()

test()