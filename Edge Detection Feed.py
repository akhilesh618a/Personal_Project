
import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("[!] Could not open the webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("[!] Failed to grab frame.")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

   
    cv2.imshow("Original Webcam Feed", frame)
    cv2.imshow("Grayscale Feed", gray)
    cv2.imshow("Edge Detection Feed", edges)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




























































# import tkinter as tk
# import random
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600
# NUM_METEORS = 20
# METEOR_SPEED_MIN = 5
# METEOR_SPEED_MAX = 15
# TAIL_LENGTH = 10
# NUM_STARS = 100
# STAR_BLINK_PROBABILITY = 0.05
# NUM_PLANETS = 5

# class Star:
#     def __init__(self, canvas):
#         self.canvas = canvas
#         self.x = random.randint(0, WINDOW_WIDTH)
#         self.y = random.randint(0, WINDOW_HEIGHT)
#         self.size = random.randint(1, 3)
#         self.visible = True

#     def blink(self):
#         if random.random() < STAR_BLINK_PROBABILITY:
#             self.visible = not self.visible

#     def draw(self):
#         if self.visible:
#             self.canvas.create_oval(
#                 self.x - self.size, self.y - self.size,
#                 self.x + self.size, self.y + self.size,
#                 fill='white', outline=''
#             )

# class Planet:
#     def __init__(self, canvas):
#         self.canvas = canvas
#         self.x = random.randint(50, WINDOW_WIDTH - 50)
#         self.y = random.randint(50, WINDOW_HEIGHT - 50)
#         self.size = random.randint(10, 30)
#         self.color = random.choice(['blue', 'green', 'purple', 'cyan', 'magenta', 'orange'])

#     def draw(self):
#         self.canvas.create_oval(
#             self.x - self.size, self.y - self.size,
#             self.x + self.size, self.y + self.size,
#             fill=self.color, outline=''
#         )

# class Meteor:
#     def __init__(self, canvas):
#         self.canvas = canvas
#         self.reset()

#     def reset(self):
#         self.x = random.randint(0, WINDOW_WIDTH)
#         self.y = random.randint(-WINDOW_HEIGHT, 0)
#         self.speed = random.randint(METEOR_SPEED_MIN, METEOR_SPEED_MAX)
#         self.color = random.choice(['red', 'orange', 'yellow'])
#         self.trail = []

#     def move(self):
#         self.trail.append((self.x, self.y))
#         if len(self.trail) > TAIL_LENGTH:
#             self.trail.pop(0)
#         self.x += self.speed * 0.5
#         self.y += self.speed

#         if self.y > WINDOW_HEIGHT or self.x > WINDOW_WIDTH:
#             self.reset()

#     def draw(self):
#         for i, (tx, ty) in enumerate(self.trail):
#             trail_len = len(self.trail)
#             if trail_len == 0:
#                 continue
#             intensity = int(255 * (i + 1) / trail_len)
#             if self.color == 'red':
#                 color = f'#{intensity:02x}0000'
#             elif self.color == 'orange':
#                 color = f'#{intensity:02x}{int(intensity * 0.5):02x}00'
#             else:  
#                 color = f'#{intensity:02x}{intensity:02x}00'

#             self.canvas.create_line(tx, ty, tx + 2, ty + 2, fill=color, width=2)

#         self.canvas.create_oval(
#             self.x - 2, self.y - 2,
#             self.x + 2, self.y + 2,
#             fill=self.color, outline=''
#         )

# class MeteorShowerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title('Meteor Shower Simulation by Akhilesh')
#         self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='black')
#         self.canvas.pack()

#         self.stars = [Star(self.canvas) for _ in range(NUM_STARS)]
#         self.planets = [Planet(self.canvas) for _ in range(NUM_PLANETS)]
#         self.meteors = [Meteor(self.canvas) for _ in range(NUM_METEORS)]

#         self.animate()

#     def animate(self):
#         self.canvas.delete('all')

#         for planet in self.planets:
#             planet.draw()

#         for star in self.stars:
#             star.blink()
#             star.draw()

#         for meteor in self.meteors:
#             meteor.move()
#             meteor.draw()

#         self.root.after(50, self.animate)

# if __name__ == '__main__':
#     root = tk.Tk()
#     app = MeteorShowerApp(root)
#     root.mainloop()
