import tkinter as tk

CANVAS_WIDTH: int = 400
CANVAS_HEIGHT: int = 400
CELL_SIZE: int = 40
ERASER_SIZE: int = 20

class CanvasEraserApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack()

        self.cells = {}
        self.draw_grid()

        # Create eraser (invisible, just for tracking)
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, outline='red')

        self.canvas.bind("<B1-Motion>", self.erase_cells)

    def draw_grid(self):
        for y in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for x in range(0, CANVAS_WIDTH, CELL_SIZE):
                rect = self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill='blue', outline='black')
                self.cells[(x, y)] = rect

    def erase_cells(self, event):
        # Center the eraser around the mouse
        x1 = event.x - ERASER_SIZE // 2
        y1 = event.y - ERASER_SIZE // 2
        x2 = x1 + ERASER_SIZE
        y2 = y1 + ERASER_SIZE
        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        # Erase overlapping cells
        for (x, y), rect in self.cells.items():
            cell_coords = self.canvas.coords(rect)
            if self.rects_intersect(cell_coords, (x1, y1, x2, y2)):
                self.canvas.itemconfig(rect, fill='white')

    def rects_intersect(self, r1, r2):
        # r1 and r2 = (x1, y1, x2, y2)
        return not (r1[2] <= r2[0] or r1[0] >= r2[2] or r1[3] <= r2[1] or r1[1] >= r2[3])

def main():
    root = tk.Tk()
    root.title("Canvas Eraser")
    app = CanvasEraserApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
