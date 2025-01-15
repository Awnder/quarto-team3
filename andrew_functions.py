import tkinter as tk
import tkinter.ttk

fifteen = 15
thirty_five = 35
fifty = 50
one_hundred_fifty = 150
two_hundred = 200

def draw_large_purple_solid_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+two_hundred, starty+two_hundred, fill="purple")

def draw_small_purple_solid_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+fifty, starty+fifty, fill="purple")

def draw_large_purple_hollow_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+two_hundred, starty+two_hundred, fill="purple")
  canvas.create_rectangle(startx+fifty, starty+fifty, startx+one_hundred_fifty, starty+one_hundred_fifty, fill="white")

def draw_small_purple_hollow_circle(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+fifty, starty+fifty, fill="purple")
  canvas.create_rectangle(startx+one_hundred_fifty, starty+one_hundred_fifty, startx+thirty_five, starty+thirty_five, fill="white")

def draw_large_purple_solid_cricle(canvas: object, startx: int, starty: int) -> None:
  canvas.create_oval(startx, starty, startx+two_hundred, starty+two_hundred, fill="purple")

def draw_small_green_solid_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+fifty, starty+fifty, fill="green")

def draw_small_purple_solid_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+fifty, starty+fifty, fill="purple")
  
def draw_large_green_hollow_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+two_hundred, starty+two_hundred, fill="green", outline="green", width=2)
    canvas.create_oval(startx+fifty, starty+fifty, startx+one_hundred_fifty, starty+one_hundred_fifty, fill="white", outline="green", width=2)
  
def def_large_purple_hollow_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+two_hundred, starty+two_hundred, fill="purple", outline="purple", width=2)
    canvas.create_oval(startx+fifty, starty+fifty, startx+one_hundred_fifty, starty+one_hundred_fifty, fill="white", outline="purple", width=2)

def draw_small_green_hollow_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+fifty, starty+fifty, fill="green", outline="green", width=2)
    canvas.create_oval(startx+one_hundred_fifty, starty+one_hundred_fifty, startx+thirty_five, starty+thirty_five, fill="white", outline="green", width=2)

def draw_small_purple_hollow_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+fifty, starty+fifty, fill="purple", outline="purple", width=2)
    canvas.create_oval(startx+one_hundred_fifty, starty+one_hundred_fifty, startx+thirty_five, starty+thirty_five, fill="white", outline="purple", width=2)

def draw_large_green_solid_square(canvas: object, startx: int, starty: int) -> None:
    canvas.create_rectangle(startx, starty, startx+two_hundred, starty+two_hundred, fill="green")

def draw_small_green_solid_square(canvas: object, startx: int, starty: int) -> None:
    canvas.create_rectangle(startx, starty, startx+fifty, starty+fifty, fill="green")

def draw_large_green_hollow_square(canvas: object, startx: int, starty: int) -> None:
    canvas.create_rectangle(startx, starty, startx+two_hundred, starty+two_hundred, fill="green")
    canvas.create_rectangle(startx+fifty, starty+fifty, startx+one_hundred_fifty, starty+one_hundred_fifty, fill="white")

def draw_small_green_hollow_square(canvas: object, startx: int, starty: int) -> None:
    canvas.create_rectangle(startx, starty, startx+fifty, starty+fifty, fill="green")
    canvas.create_rectangle(startx+one_hundred_fifty, starty+one_hundred_fifty, startx+thirty_five, starty+thirty_five, fill="white")

def draw_large_green_solid_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+two_hundred, starty+two_hundred, fill="green")

def test():
  root = tk.Tk()
  root.title('Shapes')
  root.geometry('700x700')

  canvas = tk.Canvas()
  canvas.pack(fill=tk.BOTH, expand=1)
  canvas.configure(bg="white")

  draw_solid_purple_large_square(canvas, 0, 0)
  draw_hollow_purple_large_square(canvas, 250, 0)
  draw_hollow_purple_small_square(canvas, 500, 0)
  draw_solid_purple_large_circle(canvas, 0, 250)

  # Cruse
  draw_solid_green_small_circle(canvas, 100, 500)
  draw_solid_purple_small_circle(canvas, 100, 600)
  draw_hollow_green_large_circle(canvas, 250, 250)
  draw_hollow_purple_large_circle(canvas, 500, 250)
  draw_hollow_green_small_circle(canvas, 250, 500)
  draw_hollow_purple_small_circle(canvas, 400, 500)

  root.mainloop()

test()
