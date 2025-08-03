
import turtle
import colorsys
import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab

def draw_art(shape='spiral', iterations=150, pensize=2.5, color_mode='rainbow', save_image=False):
    screen = turtle.Screen()
    screen.title("Raksha Bandhan Spiral Art")
    screen.bgcolor('black')
    screen.tracer(3)
    artist = turtle.Turtle()
    artist.pensize(pensize)
    artist.speed(0)
    h = 0.7

    for i in range(iterations):
        if color_mode == 'rainbow':
            c = colorsys.hsv_to_rgb(h, 1, 1)
        elif color_mode == 'fire':
            c = colorsys.hsv_to_rgb(h, 1, 0.8)
        elif color_mode == 'ice':
            c = colorsys.hsv_to_rgb(0.6 + h / 3, 0.4, 1)
        elif color_mode == 'pastel':
            c = colorsys.hsv_to_rgb(h, 0.3, 1)
        elif color_mode == 'neon':
            c = colorsys.hsv_to_rgb(h, 1, 0.6)
        else:
            c = (1, 1, 1)

        artist.color(c)
        h += 0.004

        if shape == 'spiral':
            radius = max(190 - i, 20)
            artist.circle(radius, 90)
            artist.left(90)
            artist.left(22)
            artist.circle(radius, 90)
            artist.left(20)

        elif shape == 'flower':
            artist.forward(i * 0.6)
            artist.left(61)
            artist.forward(i * 0.6)
            artist.left(61)

        elif shape == 'starburst':
            artist.forward(i)
            artist.left(144)

        elif shape == 'galaxy':
            artist.forward(i * 0.4)
            artist.left(i % 360)

    artist.penup()
    artist.goto(0, 260)
    artist.pencolor("white")
    artist.write("Happy Raksha Bandhan 🎉", align="center", font=("Comic Sans MS", 14, "bold"))
    artist.hideturtle()

    screen.update()

    if save_image:
        canvas = screen.getcanvas()
        x0 = canvas.winfo_rootx()
        y0 = canvas.winfo_rooty()
        x1 = x0 + canvas.winfo_width()
        y1 = y0 + canvas.winfo_height()
        filename = f"RakshaBandhan_Art_{shape}_{color_mode}.png"
        ImageGrab.grab(bbox=(x0, y0, x1, y1)).save(filename)
        print(f"Image saved as {filename}")

    turtle.done()
def launch_gui():
    def start_drawing():
        try:
            iterations = int(iterations_var.get())
            pensize = float(pensize_var.get())
            color_mode = color_var.get()
            shape_mode = shape_var.get()
            save_img = save_var.get()

            if close_var.get():
                root.after(100, root.destroy)

            draw_art(shape_mode, iterations, pensize, color_mode, save_img)

        except Exception as e:
            print(f"Error: {e}")

    root = tk.Tk()
    root.title("Raksha Bandhan ")
    root.geometry("420x400")
    root.configure(bg="#1e1e1e")
    title = tk.Label(root, text="Raksha Bandhan 🎨 ", bg="#1e1e1e", fg="#FCDDEC",
                     font=("Helvetica", 16, "bold"))
    title.pack(pady=10)
    iterations_var = tk.StringVar(value="150")
    pensize_var = tk.StringVar(value="2.5")
    color_var = tk.StringVar(value="rainbow")
    shape_var = tk.StringVar(value="spiral")
    save_var = tk.BooleanVar(value=True)
    close_var = tk.BooleanVar(value=False)
    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(pady=10)
    def label_entry(row, text, var, width=10):
        tk.Label(frame, text=text, bg="#1e1e1e", fg="white").grid(row=row, column=0, sticky="w")
        tk.Entry(frame, textvariable=var, width=width).grid(row=row, column=1)
    label_entry(0, "Iterations:", iterations_var)
    label_entry(1, "Pen Size:", pensize_var)
    tk.Label(frame, text="Color Scheme:", bg="#1e1e1e", fg="white").grid(row=2, column=0, sticky="w")
    ttk.Combobox(frame, textvariable=color_var, values=["rainbow", "fire", "ice", "pastel", "neon"], width=10).grid(row=2, column=1)
    tk.Label(frame, text="Shape Type:", bg="#1e1e1e", fg="white").grid(row=3, column=0, sticky="w")
    ttk.Combobox(frame, textvariable=shape_var, values=["spiral", "flower", "starburst", "galaxy"], width=10).grid(row=3, column=1)
    tk.Checkbutton(frame, text="Save as PNG", variable=save_var, bg="#1e1e1e", fg="white", selectcolor="black").grid(row=4, column=0, columnspan=2, sticky="w")
    tk.Checkbutton(frame, text="Close GUI after start", variable=close_var, bg="#1e1e1e", fg="white", selectcolor="black").grid(row=5, column=0, columnspan=2, sticky="w")
    btn_frame = tk.Frame(root, bg="#1e1e1e")
    btn_frame.pack(pady=15)
    tk.Button(btn_frame, text="Start Drawing", command=start_drawing, bg="#2ecc71", fg="white", width=18).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Exit", command=root.quit, bg="#e74c3c", fg="white", width=10).grid(row=1, column=0, pady=10)
    root.mainloop()
if __name__ == "__main__":
    launch_gui()