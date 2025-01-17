import tkinter as tk
import tkinter.ttk

inner_small_size = 35
outer_small_size = 50
inner_large_size = 150
outer_large_size = 200

def draw_large_purple_solid_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+outer_large_size, starty+outer_large_size, fill="purple")

def draw_small_purple_solid_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+outer_small_size, starty+outer_small_size, fill="purple")

def draw_large_purple_hollow_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+outer_large_size, starty+outer_large_size, fill="purple")
  canvas.create_rectangle(startx+outer_small_size, starty+outer_small_size, startx+inner_large_size, starty+inner_large_size, fill="white")

def draw_small_purple_hollow_square(canvas: object, startx: int, starty: int) -> None:
  canvas.create_rectangle(startx, starty, startx+outer_small_size, starty+outer_small_size, fill="purple")
  canvas.create_rectangle(startx+inner_large_size, starty+inner_large_size, startx+inner_small_size, starty+inner_small_size, fill="white")

def draw_large_purple_solid_cricle(canvas: object, startx: int, starty: int) -> None:
  canvas.create_oval(startx, starty, startx+outer_large_size, starty+outer_large_size, fill="purple")

def draw_small_green_solid_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+outer_small_size, starty+outer_small_size, fill="green")

def draw_small_purple_solid_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+outer_small_size, starty+outer_small_size, fill="purple")
  
def draw_large_green_hollow_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+outer_large_size, starty+outer_large_size, fill="green", outline="green", width=2)
    canvas.create_oval(startx+outer_small_size, starty+outer_small_size, startx+inner_large_size, starty+inner_large_size, fill="white", outline="green", width=2)
  
def draw_large_purple_hollow_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+outer_large_size, starty+outer_large_size, fill="purple", outline="purple", width=2)
    canvas.create_oval(startx+outer_small_size, starty+outer_small_size, startx+inner_large_size, starty+inner_large_size, fill="white", outline="purple", width=2)

def draw_small_green_hollow_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+outer_small_size, starty+outer_small_size, fill="green", outline="green", width=2)
    canvas.create_oval(startx+inner_large_size, starty+inner_large_size, startx+inner_small_size, starty+inner_small_size, fill="white", outline="green", width=2)

def draw_small_purple_hollow_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+outer_small_size, starty+outer_small_size, fill="purple", outline="purple", width=2)
    canvas.create_oval(startx+inner_large_size, starty+inner_large_size, startx+inner_small_size, starty+inner_small_size, fill="white", outline="purple", width=2)

def draw_large_green_solid_square(canvas: object, startx: int, starty: int) -> None:
    canvas.create_rectangle(startx, starty, startx+outer_large_size, starty+outer_large_size, fill="green")

def draw_small_green_solid_square(canvas: object, startx: int, starty: int) -> None:
    canvas.create_rectangle(startx, starty, startx+outer_small_size, starty+outer_small_size, fill="green")

def draw_large_green_hollow_square(canvas: object, startx: int, starty: int) -> None:
    canvas.create_rectangle(startx, starty, startx+outer_large_size, starty+outer_large_size, fill="green")
    canvas.create_rectangle(startx+outer_small_size, starty+outer_small_size, startx+inner_large_size, starty+inner_large_size, fill="white")

def draw_small_green_hollow_square(canvas: object, startx: int, starty: int) -> None:
    canvas.create_rectangle(startx, starty, startx+outer_small_size, starty+outer_small_size, fill="green")
    canvas.create_rectangle(startx+inner_large_size, starty+inner_large_size, startx+inner_small_size, starty+inner_small_size, fill="white")

def draw_large_green_solid_circle(canvas: object, startx: int, starty: int) -> None:
    canvas.create_oval(startx, starty, startx+outer_large_size, starty+outer_large_size, fill="green")

def draw_piece(canvas: object, piece: str, startx: int, starty: int) -> None:
  """ Unifying function that will draw any of the 16 pieces """
  piece_draw_functions = {
        "large_purple_solid_square": draw_large_purple_solid_square,
        "small_purple_solid_square": draw_small_purple_solid_square,
        "large_purple_hollow_square": draw_large_purple_hollow_square,
        "small_purple_hollow_square": draw_small_purple_hollow_square,
        "large_purple_solid_circle": draw_large_purple_solid_cricle,
        "small_green_solid_circle": draw_small_green_solid_circle,
        "small_purple_solid_circle": draw_small_purple_solid_circle,
        "large_green_hollow_circle": draw_large_green_hollow_circle,
        "large_purple_hollow_circle": draw_large_purple_hollow_circle,
        "small_green_hollow_circle": draw_small_green_hollow_circle,
        "small_purple_hollow_circle": draw_small_purple_hollow_circle,
        "large_green_solid_square": draw_large_green_solid_square,
        "small_green_solid_square": draw_small_green_solid_square,
        "large_green_hollow_square": draw_large_green_hollow_square,
        "small_green_hollow_square": draw_small_green_hollow_square,
        "large_green_solid_circle": draw_large_green_solid_circle,
    }
  
  # Call the appropriate function based on the piece identifier
  if piece in piece_draw_functions:
        piece_draw_functions[piece](canvas, startx, starty)
  else:
        print(f"Error: Unknown piece identifier '{piece}'")

def create_board():
    root = tk.Tk()
    root.title('Game Board')
    root.geometry('1200x800')
    canvas = tk.Canvas(root)
    canvas.pack(fill=tk.BOTH, expand=1)
    canvas.configure(bg="white")

    canvas.create_rectangle(300, 100, 300+600, 100+600, fill="white")
    # horizontal lines
    canvas.create_line(300, 400, 900, 400, fill="black", width=1)
    canvas.create_line(300, 250, 900, 250, fill="black", width=1)
    canvas.create_line(300, 550, 900, 550, fill="black", width=1)
    # vertical lines
    canvas.create_line(600, 100, 600, 700, fill="black", width=1)
    canvas.create_line(450, 100, 450, 700, fill="black", width=1)
    canvas.create_line(750, 100, 750, 700, fill="black", width=1)

    root.mainloop()

def test():
  root = tk.Tk()
  root.title('Shapes')
  root.geometry('700x700')

  canvas = tk.Canvas()
  canvas.pack(fill=tk.BOTH, expand=1)
  canvas.configure(bg="white")

  # draw_solid_purple_large_square(canvas, 0, 0)
  # draw_hollow_purple_large_square(canvas, 250, 0)
  # draw_hollow_purple_small_square(canvas, 500, 0)
  # draw_solid_purple_large_circle(canvas, 0, 250)

  # # Cruse
  # draw_solid_green_small_circle(canvas, 100, 500)
  # draw_solid_purple_small_circle(canvas, 100, 600)
  # draw_hollow_green_large_circle(canvas, 250, 250)
  # draw_hollow_purple_large_circle(canvas, 500, 250)
  # draw_hollow_green_small_circle(canvas, 250, 500)
  # draw_hollow_purple_small_circle(canvas, 400, 500)

  # draw_solid_green_large_square(canvas, 0, 0)
  # draw_hollow_green_large_square(canvas, 0, 0)
  # draw_hollow_green_small_square(canvas, 300, 300)
  # draw_solid_green_large_circle(canvas, 2, 2)

  root.mainloop()

create_board()
# test()
