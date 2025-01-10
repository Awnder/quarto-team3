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

# Cruse
def draw_solid_green_small_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+50, starty+50, fill="green")

def draw_solid_purple_small_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+50, starty+50, fill="purple")
  
def draw_hollow_green_large_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+200, starty+200, fill="green", outline="green", width=2)
    canvas.create_oval(startx+50, starty+50, startx+150, starty+150, fill="white", outline="green", width=2)
  
def draw_hollow_purple_large_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+200, starty+200, fill="purple", outline="purple", width=2)
    canvas.create_oval(startx+50, starty+50, startx+150, starty+150, fill="white", outline="purple", width=2)

def draw_hollow_green_small_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+50, starty+50, fill="green", outline="green", width=2)
    canvas.create_oval(startx+15, starty+15, startx+35, starty+35, fill="white", outline="green", width=2)

def draw_hollow_purple_small_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+50, starty+50, fill="purple", outline="purple", width=2)
    canvas.create_oval(startx+15, starty+15, startx+35, starty+35, fill="white", outline="purple", width=2)

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
