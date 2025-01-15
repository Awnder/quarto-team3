import tkinter as tk
import tkinter.ttk



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
