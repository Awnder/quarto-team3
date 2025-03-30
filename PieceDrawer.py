import tkinter as tk

class PieceDrawer:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        # piece dimensions
        self.small_small = 15
        self.small_large = 50
        self.large_small = 25
        self.large_large = 100

    def draw_piece(self, piece: str, startx: int, starty: int) -> None:
        """lookup dictionary function to draw a piece based on its name"""
        piece_functions = {
            "lpss": self._draw_large_purple_solid_square,
            "spss": self._draw_small_purple_solid_square,
            "lphs": self._draw_large_purple_hollow_square,
            "sphc": self._draw_small_purple_hollow_circle,
            "lpsc": self._draw_large_purple_solid_circle,
            "sgsc": self._draw_small_green_solid_circle,
            "spsc": self._draw_small_purple_solid_circle,
            "lghc": self._draw_large_green_hollow_circle,
            "lphc": self._draw_large_purple_hollow_circle,
            "sghc": self._draw_small_green_hollow_circle,
            "sphs": self._draw_small_purple_hollow_square,
            "lgss": self._draw_large_green_solid_square,
            "sgss": self._draw_small_green_solid_square,
            "lghs": self._draw_large_green_hollow_square,
            "sghs": self._draw_small_green_hollow_square,
            "lgsc": self._draw_large_green_solid_circle,
        }
        if piece in piece_functions:
            piece_functions[piece](startx, starty)
        else:
            print(f"Error: Unknown piece name '{piece}'")

    def _draw_large_purple_solid_square(self, startx: int, starty: int) -> None:
        id = self.canvas.create_rectangle(startx, starty, startx + self.large_large, starty + self.large_large, fill="purple4")
        self.canvas.addtag_withtag("lpss", id)

    def _draw_large_purple_hollow_square(self, startx: int, starty: int) -> None:
        id1 = self.canvas.create_rectangle(startx, starty, startx + self.large_large, starty + self.large_large, fill="purple4")
        id2 = self.canvas.create_rectangle(startx + self.large_small, starty + self.large_small, startx + self.large_large - self.large_small, starty + self.large_large - self.large_small, outline="purple4", fill="mediumpurple1")
        self.canvas.addtag_withtag("lphs", id1)
        self.canvas.addtag_withtag("lphs", id2)

    def _draw_large_purple_solid_circle(self, startx: int, starty: int) -> None:
        id = self.canvas.create_oval(startx, starty, startx + self.large_large, starty + self.large_large, fill="purple4")
        self.canvas.addtag_withtag("lpsc", id)

    def _draw_large_purple_hollow_circle(self, startx: int, starty: int) -> None:
        id1 = self.canvas.create_oval(startx, starty, startx + self.large_large, starty + self.large_large, fill="purple4", outline="purple4", width=2)
        id2 = self.canvas.create_oval(startx + self.large_small, starty + self.large_small, startx + self.large_large - self.large_small, starty + self.large_large - self.large_small, fill="mediumpurple1", outline="purple4", width=2)
        self.canvas.addtag_withtag("lphc", id1)
        self.canvas.addtag_withtag("lphc", id2)

    def _draw_small_purple_solid_square(self, startx: int, starty: int) -> None:
        id = self.canvas.create_rectangle(startx, starty, startx + self.small_large, starty + self.small_large, fill="purple4")
        self.canvas.addtag_withtag("spss", id)

    def _draw_small_purple_hollow_square(self, startx: int, starty: int) -> None:
        id1 = self.canvas.create_rectangle(startx, starty, startx + self.small_large, starty + self.small_large, fill="purple4")
        id2 = self.canvas.create_rectangle(startx + self.small_small, starty + self.small_small, startx + self.small_large - self.small_small, starty + self.small_large - self.small_small, outline="purple4", fill="mediumpurple1")
        self.canvas.addtag_withtag("sphs", id1)
        self.canvas.addtag_withtag("sphs", id2)

    def _draw_small_purple_solid_circle(self, startx: int, starty: int) -> None:
        id = self.canvas.create_oval(startx, starty, startx + self.small_large, starty + self.small_large, fill="purple4")
        self.canvas.addtag_withtag("spsc", id)

    def _draw_small_purple_hollow_circle(self, startx: int, starty: int) -> None:
        id1 = self.canvas.create_oval(startx, starty, startx + self.small_large, starty + self.small_large, fill="purple4", outline="purple4", width=2)
        id2 = self.canvas.create_oval(startx + self.small_small, starty + self.small_small, startx + self.small_large - self.small_small, starty + self.small_large - self.small_small, fill="mediumpurple1", outline="purple4", width=2)
        self.canvas.addtag_withtag("sphc", id1)
        self.canvas.addtag_withtag("sphc", id2)

    def _draw_large_green_solid_square(self, startx: int, starty: int) -> None:
        id = self.canvas.create_rectangle(startx, starty, startx + self.large_large, starty + self.large_large, fill="seagreen")
        self.canvas.addtag_withtag("lgss", id)

    def _draw_large_green_hollow_square(self, startx: int, starty: int) -> None:
        id1 = self.canvas.create_rectangle(startx, starty, startx + self.large_large, starty + self.large_large, fill="seagreen")
        id2 = self.canvas.create_rectangle(startx + self.large_small, starty + self.large_small, startx + self.large_large - self.large_small, starty + self.large_large - self.large_small, outline="seagreen", fill="mediumseagreen")
        self.canvas.addtag_withtag("lghs", id1)
        self.canvas.addtag_withtag("lghs", id2)

    def _draw_large_green_solid_circle(self, startx: int, starty: int) -> None:
        id = self.canvas.create_oval(startx, starty, startx + self.large_large, starty + self.large_large, fill="seagreen")
        self.canvas.addtag_withtag("lgsc", id)

    def _draw_large_green_hollow_circle(self, startx: int, starty: int) -> None:
        id1 = self.canvas.create_oval(startx, starty, startx + self.large_large, starty + self.large_large, fill="seagreen", outline="seagreen", width=2)
        id2 = self.canvas.create_oval(startx + self.large_small, starty + self.large_small, startx + self.large_large - self.large_small, starty + self.large_large - self.large_small, fill="mediumseagreen", outline="seagreen", width=2)
        self.canvas.addtag_withtag("lghc", id1)
        self.canvas.addtag_withtag("lghc", id2)

    def _draw_small_green_solid_square(self, startx: int, starty: int) -> None:
        id = self.canvas.create_rectangle(startx, starty, startx + self.small_large, starty + self.small_large, fill="seagreen")
        self.canvas.addtag_withtag("sgss", id)

    def _draw_small_green_hollow_square(self, startx: int, starty: int) -> None:
        id1 = self.canvas.create_rectangle(startx, starty, startx + self.small_large, starty + self.small_large, fill="seagreen")
        id2 = self.canvas.create_rectangle(startx + self.small_small, starty + self.small_small, startx + self.small_large - self.small_small, starty + self.small_large - self.small_small, outline="seagreen", fill="mediumseagreen")
        self.canvas.addtag_withtag("sghs", id1)
        self.canvas.addtag_withtag("sghs", id2)

    def _draw_small_green_solid_circle(self, startx: int, starty: int) -> None:
        id = self.canvas.create_oval(startx, starty, startx + self.small_large, starty + self.small_large, fill="seagreen")
        self.canvas.addtag_withtag("sgsc", id)

    def _draw_small_green_hollow_circle(self, startx: int, starty: int) -> None:
        id1 = self.canvas.create_oval(startx, starty, startx + self.small_large, starty + self.small_large, fill="seagreen", outline="seagreen", width=2)
        id2 = self.canvas.create_oval(startx + self.small_small, starty + self.small_small, startx + self.small_large - self.small_small, starty + self.small_large - self.small_small, fill="mediumseagreen", outline="seagreen", width=2)
        self.canvas.addtag_withtag("sghc", id1)
        self.canvas.addtag_withtag("sghc", id2)
        self.canvas.addtag_withtag("sghc", id2)