import tkinter as tk
import tkinter.ttk

def draw_solid_green_large_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+200, starty+200, fill="green")

def draw_solid_green_small_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+50, starty+50, fill="green")

def draw_hollow_green_large_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+200, starty+200, fill="green")
  canvas.create_rectangle(startx+50, starty+50, startx+150, starty+150, fill="white")

def draw_hollow_green_small_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+50, starty+50, fill="green")
  canvas.create_rectangle(startx+15, starty+15, startx+35, starty+35, fill="white")

def draw_solid_green_large_circle(canvas: object, startx: int, starty: int) -> None:
  canvas.create_oval(startx, starty, startx+200, starty+200, fill="green")

def test():
  root = tk.Tk()
  root.title('Shapes')
  root.geometry('500x500')

  canvas = tk.Canvas()
  canvas.pack(fill=tk.BOTH, expand=1)
  canvas.configure(bg="white")

  draw_solid_green_large_square(canvas, 0, 0)
  draw_hollow_green_large_square(canvas, 0, 0)
  draw_hollow_green_small_square(canvas, 300, 300)
  draw_solid_green_large_circle(canvas, 2, 2)

  root.mainloop()

test()