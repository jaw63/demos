import tkinter as tk
from tkinter.colorchooser import askcolor

class PaintApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Paint App")
        self.master.resizable(False, False)
        self.color = "black"
        self.canvas_width = 500
        self.canvas_height = 500
        self.create_widgets()
        self.create_canvas()

    def create_widgets(self):
        self.color_button = tk.Button(self.master, text="Select Color", command=self.select_color)
        self.color_button.pack(side="left", padx=(10,0), pady=(10,0))
        self.clear_button = tk.Button(self.master, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack(side="left", padx=(10,0), pady=(10,0))

    def create_canvas(self):
        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack(side="top", padx=(10,0), pady=(10,0))
        self.canvas.bind("<B1-Motion>", self.draw)

    def select_color(self):
        self.color = askcolor()[1]

    def clear_canvas(self):
        self.canvas.delete("all")

    def draw(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
