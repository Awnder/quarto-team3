import tkinter as tk
import tkinter.ttk

def draw_board():
    root= tk.Tk()
    root.title('Game Board')
    root.geometry('2400x1600')
    canvas = tk.Canvas(root)
    canvas.pack(fill=tk.BOTH, expand=1)
    canvas.configure(bg="white")

    canvas.create_rectangle(400, 50, 1200, 850, fill="white", outline="black", width=1)

    canvas.create_line(400, 250, 1200, 250, fill="black", width=1)
    canvas.create_line(400, 450, 1200, 450, fill="black", width=1)
    canvas.create_line(400, 650, 1200, 650, fill="black", width=1)

    canvas.create_line(600, 50, 600, 850, fill="black", width=1)
    canvas.create_line(800, 50, 800, 850, fill="black", width=1)
    canvas.create_line(1000, 50, 1000, 850, fill="black", width=1)

    draw_large_purple_solid_square(canvas, 250, 75)
    draw_large_purple_hollow_square(canvas, 250, 190)
    draw_large_purple_solid_circle(canvas, 250, 305)
    draw_large_purple_hollow_circle(canvas, 250, 420)
    draw_small_purple_solid_square(canvas, 275, 535)
    draw_small_purple_hollow_square(canvas, 275, 600)
    draw_small_purple_solid_circle(canvas, 275, 665)
    draw_small_purple_hollow_circle(canvas, 275, 730)

    draw_large_green_solid_square(canvas, 50, 75)
    draw_large_green_hollow_square(canvas, 50, 190)
    draw_large_green_solid_circle(canvas, 50, 305)
    draw_large_green_hollow_circle(canvas, 50, 420)
    draw_small_green_solid_square(canvas, 75, 535)
    draw_small_green_hollow_square(canvas, 75, 600)
    draw_small_green_solid_circle(canvas, 75, 665)
    draw_small_green_hollow_circle(canvas, 75, 730)

    root.mainloop()

small_small = 15
small_large = 50
large_small = 25
large_large = 100

def draw_large_purple_solid_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+large_large, starty+large_large, fill="purple4")

def draw_large_purple_hollow_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+large_large, starty+large_large, fill="purple4")
  canvas.create_rectangle(startx+large_small, starty+large_small, startx+large_large-large_small, starty+large_large-large_small, outline="purple4", fill="mediumpurple1")

def draw_large_purple_solid_circle(canvas: object, startx: int, starty: int) -> None:
  canvas.create_oval(startx, starty, startx+large_large, starty+large_large, fill="purple4")

def draw_large_purple_hollow_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+large_large, starty+large_large, fill="purple4", outline="purple4", width=2)
    canvas.create_oval(startx+large_small, starty+large_small, startx+large_large-large_small, starty+large_large-large_small, fill="mediumpurple1", outline="purple4", width=2)

def draw_small_purple_solid_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+small_large, starty+small_large, fill="purple4")

def draw_small_purple_hollow_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+small_large, starty+small_large, fill="purple4")
  canvas.create_rectangle(startx+small_small, starty+small_small, startx+small_large-small_small, starty+small_large - small_small, outline="purple4", fill="mediumpurple1")

def draw_small_purple_solid_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+small_large, starty+small_large, fill="purple4")

def draw_small_purple_hollow_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+small_large, starty+small_large, fill="purple4", outline="purple4", width=2)
    canvas.create_oval(startx+small_small, starty+small_small, startx+small_large-small_small, starty+small_large - small_small, fill="mediumpurple1", outline="purple4", width=2)

def draw_large_green_solid_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+large_large, starty+large_large, fill="seagreen")

def draw_large_green_hollow_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+large_large, starty+large_large, fill="seagreen")
  canvas.create_rectangle(startx+large_small, starty+large_small, startx+large_large-large_small, starty+large_large-large_small, outline="seagreen", fill="mediumseagreen")

def draw_large_green_solid_circle(canvas: object, startx: int, starty: int) -> None:
  canvas.create_oval(startx, starty, startx+large_large, starty+large_large, fill="seagreen")

def draw_large_green_hollow_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+large_large, starty+large_large, fill="seagreen", outline="seagreen", width=2)
    canvas.create_oval(startx+large_small, starty+large_small, startx+large_large-large_small, starty+large_large-large_small, fill="mediumseagreen", outline="seagreen", width=2)

def draw_small_green_solid_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+small_large, starty+small_large, fill="seagreen")

def draw_small_green_hollow_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+small_large, starty+small_large, fill="seagreen")
  canvas.create_rectangle(startx+small_small, starty+small_small, startx+small_large-small_small, starty+small_large - small_small, outline="seagreen", fill="mediumseagreen")

def draw_small_green_solid_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+small_large, starty+small_large, fill="seagreen")

def draw_small_green_hollow_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+small_large, starty+small_large, fill="seagreen", outline="seagreen", width=2)
    canvas.create_oval(startx+small_small, starty+small_small, startx+small_large-small_small, starty+small_large - small_small, fill="mediumseagreen", outline="seagreen", width=2)

def draw_piece(canvas: object, piece: str, startx: int, starty: int) -> None:
  peice_functions = {
        "lpss": draw_large_purple_solid_square,
        "spss": draw_small_purple_solid_square,
        "lphs": draw_large_purple_hollow_square,
        "sphc": draw_small_purple_hollow_circle,
        "lpsc": draw_large_purple_solid_circle,
        "sgsc": draw_small_green_solid_circle,
        "spsc": draw_small_purple_solid_circle,
        "lghc": draw_large_green_hollow_circle,
        "lphc": draw_large_purple_hollow_circle,
        "sghc": draw_small_green_hollow_circle,
        "sphs": draw_small_purple_hollow_square,
        "lgss": draw_large_green_solid_square,
        "sgss": draw_small_green_solid_square,
        "lghs": draw_large_green_hollow_square,
        "sghs": draw_small_green_hollow_square,
        "lgsc": draw_large_green_solid_circle,
    }
  if piece in peice_functions:
        peice_functions[piece](canvas, startx, starty)
  else:
        print(f"Error: Unknown piece name '{piece}'")

draw_board()
