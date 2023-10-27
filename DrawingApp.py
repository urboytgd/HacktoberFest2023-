import tkinter as tk
from tkinter import colorchooser, filedialog
import PIL
from PIL import Image, ImageDraw

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Drawing App")

        self.canvas = tk.Canvas(self.root, bg="white", width=600, height=400)
        self.canvas.pack(pady=20)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20)

        self.color_button = tk.Button(self.button_frame, text="Choose Color", command=self.choose_color)
        self.color_button.pack(side="left", padx=10)

        self.export_button = tk.Button(self.button_frame, text="Export", command=self.export_image)
        self.export_button.pack(side="left", padx=10)

        self.canvas.bind("<B1-Motion>", self.paint)

        self.last_x, self.last_y = None, None
        self.color = "black"
        self.image = PIL.Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)

    def paint(self, event):
        x, y = event.x, event.y
        if self.last_x and self.last_y:
            self.canvas.create_line((self.last_x, self.last_y, x, y), fill=self.color, width=2, capstyle=tk.ROUND, smooth=tk.TRUE)
            self.draw.line((self.last_x, self.last_y, x, y), fill=self.color, width=2, capstyle=tk.ROUND)
        self.last_x, self.last_y = x, y

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color

    def export_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            self.image.save(file_path)

    def reset_last_positions(self, event):
        self.last_x, self.last_y = None, None

    def run(self):
        self.canvas.bind("<ButtonRelease-1>", self.reset_last_positions)
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    app.run()
