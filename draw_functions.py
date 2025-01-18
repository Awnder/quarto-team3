import tkinter as tk
import tkinter.ttk

class Quarto:
  def __init__(self):
    self.root = self.init_root()
    self.canvas = self.init_canvas()
    self.small_small = 15
    self.small_large = 50
    self.large_small = 25
    self.large_large = 100
    self.draw_board()
    self.board = [[None for _ in range(4)] for _ in range(4)] # creates a list of lists with 4 rows and 4 columns to fill in with pieces
    self.bind_highlight()
    self.root.mainloop()

  def init_root(self) -> tkinter.Tk:
    ''' returns a tkinter root window '''
    root = tk.Tk()
    root.title('Game Board')
    root.geometry('2400x1600')
    return root
  
  def init_canvas(self) -> tkinter.Canvas:
    ''' returns a tkinter canvas '''
    canvas = tk.Canvas(self.root)
    canvas.pack(fill=tk.BOTH, expand=1)
    canvas.configure(bg="white")
    return canvas

  def draw_board(self) -> None:
    ''' draws all pieces and board '''
    self.draw_piece("lpss", 250, 75)
    self.draw_piece("lpsc", 250, 305)
    self.draw_piece("spss", 275, 535)
    self.draw_piece("spsc", 275, 665)
    self.draw_piece("lphs", 250, 190)
    self.draw_piece("lphc", 250, 420)
    self.draw_piece("sphs", 275, 600)
    self.draw_piece("sphc", 275, 730)
    self.draw_piece("lgss", 50, 75)
    self.draw_piece("lgsc", 50, 305)
    self.draw_piece("sgss", 75, 535)
    self.draw_piece("sgsc", 75, 665)
    self.draw_piece("lghs", 50, 190)
    self.draw_piece("lghc", 50, 420)
    self.draw_piece("sghs", 75, 600)
    self.draw_piece("sghc", 75, 730)
    
    # have to draw 16 rectangles instead of lines in order to highlight them upon mouseover
    for i in range(4):
      for j in range(4):
        # instead of 200, use 202 to create 2px extra space between squares so highlight doesn't overlap
        id = self.canvas.create_rectangle(400 + 202 * i, 50 + 202 * j, 600 + 202 * i, 250 + 202 * j, fill="white", outline="black", width=1)
        self.canvas.addtag_withtag(f"board-{i}-{j}", id)

  def bind_highlight(self):
    ''' binds the highlight and unhighlight functions to all tags '''
    all_tags = []
    for id in self.canvas.find_all():
      tags = self.canvas.gettags(id)
      all_tags += tags
    
    for tag in all_tags:
      ids = self.canvas.find_withtag(tag)
      self.canvas.tag_bind(ids[0], "<Enter>", lambda event, id=ids[0]: self.highlight(event, id))
      self.canvas.tag_bind(ids[0], "<Leave>", lambda event, id=ids[0]: self.unhighlight(event, id))
      if len(ids) > 1: # only for hollow pieces, ensures that hovering over either the inner or outer piece will highlight both
        self.canvas.tag_bind(ids[1], "<Enter>", lambda event, id=ids[0]: self.highlight(event, id))
        self.canvas.tag_bind(ids[1], "<Leave>", lambda event, id=ids[0]: self.unhighlight(event, id))
    
  def highlight(self, event, id):
    ''' change border color to yellow and increase width of border upon mouseover '''
    self.canvas.itemconfig(id, outline="yellow", width=3)

  def unhighlight(self, event, id):
    ''' change border color to black and increase width of border upon mouseover '''
    self.canvas.itemconfig(id, outline="black", width=1)

  def draw_large_purple_solid_square(self, startx: int, starty: int) -> None:
    id = self.canvas.create_rectangle(startx, starty, startx+self.large_large, starty+self.large_large, fill="purple4")
    self.canvas.addtag_withtag("lpss", id)

  def draw_large_purple_hollow_square(self, startx: int, starty: int) -> None:
    id1 = self.canvas.create_rectangle(startx, starty, startx+self.large_large, starty+self.large_large, fill="purple4")
    id2 = self.canvas.create_rectangle(startx+self.large_small, starty+self.large_small, startx+self.large_large-self.large_small, starty+self.large_large-self.large_small, outline="purple4", fill="mediumpurple1")
    self.canvas.addtag_withtag("lphs", id1)
    self.canvas.addtag_withtag("lphs", id2)

  def draw_large_purple_solid_circle(self, startx: int, starty: int) -> None:
    id = self.canvas.create_oval(startx, starty, startx+self.large_large, starty+self.large_large, fill="purple4")
    self.canvas.addtag_withtag("lpsc", id)

  def draw_large_purple_hollow_circle(self, startx: int, starty: int) -> None:
    id1 = self.canvas.create_oval(startx, starty, startx+self.large_large, starty+self.large_large, fill="purple4", outline="purple4", width=2)
    id2 = self.canvas.create_oval(startx+self.large_small, starty+self.large_small, startx+self.large_large-self.large_small, starty+self.large_large-self.large_small, fill="mediumpurple1", outline="purple4", width=2)
    self.canvas.addtag_withtag("lphc", id1)
    self.canvas.addtag_withtag("lphc", id2)

  def draw_small_purple_solid_square(self, startx: int, starty: int) -> None:
    id = self.canvas.create_rectangle(startx, starty, startx+self.small_large, starty+self.small_large, fill="purple4")
    self.canvas.addtag_withtag("spss", id)

  def draw_small_purple_hollow_square(self, startx: int, starty: int) -> None:
    id1 = self.canvas.create_rectangle(startx, starty, startx+self.small_large, starty+self.small_large, fill="purple4")
    id2 = self.canvas.create_rectangle(startx+self.small_small, starty+self.small_small, startx+self.small_large-self.small_small, starty+self.small_large-self.small_small, outline="purple4", fill="mediumpurple1")
    self.canvas.addtag_withtag("sphs", id1)
    self.canvas.addtag_withtag("sphs", id2)

  def draw_small_purple_solid_circle(self, startx: int, starty: int) -> None:
    id = self.canvas.create_oval(startx, starty, startx+self.small_large, starty+self.small_large, fill="purple4")
    self.canvas.addtag_withtag("spsc", id)

  def draw_small_purple_hollow_circle(self, startx: int, starty: int) -> None:
    id1 = self.canvas.create_oval(startx, starty, startx+self.small_large, starty+self.small_large, fill="purple4", outline="purple4", width=2)
    id2 = self.canvas.create_oval(startx+self.small_small, starty+self.small_small, startx+self.small_large-self.small_small, starty+self.small_large-self.small_small, fill="mediumpurple1", outline="purple4", width=2)
    self.canvas.addtag_withtag("sphc", id1)
    self.canvas.addtag_withtag("sphc", id2)

  def draw_large_green_solid_square(self, startx: int, starty: int) -> None:
    id = self.canvas.create_rectangle(startx, starty, startx+self.large_large, starty+self.large_large, fill="seagreen")
    self.canvas.addtag_withtag("lgss", id)

  def draw_large_green_hollow_square(self, startx: int, starty: int) -> None:
    id1 = self.canvas.create_rectangle(startx, starty, startx+self.large_large, starty+self.large_large, fill="seagreen")
    id2 = self.canvas.create_rectangle(startx+self.large_small, starty+self.large_small, startx+self.large_large-self.large_small, starty+self.large_large-self.large_small, outline="seagreen", fill="mediumseagreen")
    self.canvas.addtag_withtag("lghs", id1)
    self.canvas.addtag_withtag("lghs", id2)

  def draw_large_green_solid_circle(self, startx: int, starty: int) -> None:
    id = self.canvas.create_oval(startx, starty, startx+self.large_large, starty+self.large_large, fill="seagreen")
    self.canvas.addtag_withtag("lgsc", id)

  def draw_large_green_hollow_circle(self, startx: int, starty: int) -> None:
    id1 = self.canvas.create_oval(startx, starty, startx+self.large_large, starty+self.large_large, fill="seagreen", outline="seagreen", width=2)
    id2 = self.canvas.create_oval(startx+self.large_small, starty+self.large_small, startx+self.large_large-self.large_small, starty+self.large_large-self.large_small, fill="mediumseagreen", outline="seagreen", width=2)
    self.canvas.addtag_withtag("lghc", id1)
    self.canvas.addtag_withtag("lghc", id2)

  def draw_small_green_solid_square(self, startx: int, starty: int) -> None:
    id = self.canvas.create_rectangle(startx, starty, startx+self.small_large, starty+self.small_large, fill="seagreen")
    self.canvas.addtag_withtag("sgss", id)

  def draw_small_green_hollow_square(self, startx: int, starty: int) -> None:
    id1 = self.canvas.create_rectangle(startx, starty, startx+self.small_large, starty+self.small_large, fill="seagreen")
    id2 = self.canvas.create_rectangle(startx+self.small_small, starty+self.small_small, startx+self.small_large-self.small_small, starty+self.small_large-self.small_small, outline="seagreen", fill="mediumseagreen")
    self.canvas.addtag_withtag("sghs", id1)
    self.canvas.addtag_withtag("sghs", id2)

  def draw_small_green_solid_circle(self, startx: int, starty: int) -> None:
    id = self.canvas.create_oval(startx, starty, startx+self.small_large, starty+self.small_large, fill="seagreen")
    self.canvas.addtag_withtag("sgsc", id)

  def draw_small_green_hollow_circle(self, startx: int, starty: int) -> None:
    id1 = self.canvas.create_oval(startx, starty, startx+self.small_large, starty+self.small_large, fill="seagreen", outline="seagreen", width=2)
    id2 = self.canvas.create_oval(startx+self.small_small, starty+self.small_small, startx+self.small_large-self.small_small, starty+self.small_large-self.small_small, fill="mediumseagreen", outline="seagreen", width=2)
    self.canvas.addtag_withtag("sghc", id1)
    self.canvas.addtag_withtag("sghc", id2)

  def draw_piece(self, piece: str, startx: int, starty: int) -> None:
    ''' lookup dictionary function to draw a piece based on its name '''
    piece_functions = {
      "lpss": self.draw_large_purple_solid_square,
      "spss": self.draw_small_purple_solid_square,
      "lphs": self.draw_large_purple_hollow_square,
      "sphc": self.draw_small_purple_hollow_circle,
      "lpsc": self.draw_large_purple_solid_circle,
      "sgsc": self.draw_small_green_solid_circle,
      "spsc": self.draw_small_purple_solid_circle,
      "lghc": self.draw_large_green_hollow_circle,
      "lphc": self.draw_large_purple_hollow_circle,
      "sghc": self.draw_small_green_hollow_circle,
      "sphs": self.draw_small_purple_hollow_square,
      "lgss": self.draw_large_green_solid_square,
      "sgss": self.draw_small_green_solid_square,
      "lghs": self.draw_large_green_hollow_square,
      "sghs": self.draw_small_green_hollow_square,
      "lgsc": self.draw_large_green_solid_circle,
    }
    if piece in piece_functions:
      piece_functions[piece](startx, starty)
    else:
      print(f"Error: Unknown piece name '{piece}'")
   

q = Quarto()