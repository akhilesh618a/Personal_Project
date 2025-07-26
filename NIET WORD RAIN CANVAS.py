
import tkinter as tk
import random


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FONT_SIZE = 20
WORD = "NIET"
COLUMN_WIDTH = FONT_SIZE + 5
ROW_HEIGHT = FONT_SIZE + 2
SPEED = 80  

class NIETRain:
    def __init__(self, root):
        self.root = root
        self.root.title("NIET Word Rain by _akhiii_co.n")
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
        self.canvas.pack()

        self.columns = WINDOW_WIDTH // COLUMN_WIDTH
        self.word_positions = [random.randint(-len(WORD), WINDOW_HEIGHT // ROW_HEIGHT) for _ in range(self.columns)]

        self.animate()

    def animate(self):
        self.canvas.delete("all")

        for i in range(self.columns):
            x = i * COLUMN_WIDTH
            start_y = self.word_positions[i] * ROW_HEIGHT

            for j, char in enumerate(WORD):
                y = start_y + j * ROW_HEIGHT
                if 0 <= y < WINDOW_HEIGHT:
                    
                    color = "lime" if j == len(WORD) - 1 else "green"
                    self.canvas.create_text(
                        x, y, text=char,
                        fill=color, font=("Courier", FONT_SIZE, "bold"), anchor="nw"
                    )

            
            self.word_positions[i] += 1

            
            if start_y > WINDOW_HEIGHT + len(WORD) * ROW_HEIGHT:
                if random.random() > 0.975:
                    self.word_positions[i] = -len(WORD)

        self.root.after(SPEED, self.animate)


if __name__ == "__main__":
    root = tk.Tk()
    app = NIETRain(root)
    root.mainloop()
