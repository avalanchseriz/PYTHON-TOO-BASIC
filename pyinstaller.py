import tkinter as tk
import math
import time


def greet():
    tk.showinfo("J.A.R.V.I.S.", "Hello, sir! How can I assist you today?")

def animate():
    angle = 0
    glow_intensity = 0
    while True:
        # Clear canvas
        canvas.delete("all")
        
        # Calculate arc reactor position
        x = 150 + 50 * math.cos(math.radians(angle))
        y = 150 + 50 * math.sin(math.radians(angle))
        
        # Draw outer circle
        canvas.create_oval(100, 100, 200, 200, outline="blue", width=3)
        
        # Draw inner circle with periodic glow
        inner_color = f"#{glow_intensity:02x}{glow_intensity:02x}ff"
        canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=inner_color, outline="blue", width=3)
        
        # Increase angle for rotation
        angle += 5
        
        # Update glow intensity for pulsating effect
        glow_intensity = int(128 * math.sin(time.time() * 3) + 128)
        
        # Update the window
        app.update_idletasks()
        app.update()
        time.sleep(0.05)  # Adjust the sleep time to control animation speed

# Create the main application window
app = tk.Tk()
app.title("J.A.R.V.I.S.")

# Create a canvas widget
canvas = tk.Canvas(app, width=300, height=300, bg="black")
canvas.pack(padx=20, pady=20)

# Create a label widget
label = tk.Label(app, text="Welcome to J.A.R.V.I.S.", font=("Arial", 18))
label.pack()

# Create a button widget
button = tk.Button(app, text="Greet", command=greet)
button.pack(pady=10)

# Start animation
animate()

# Run the application
app.mainloop()
