# Open-source stopwatch made by Kenickle
# Feel free to install, share or do as you please with the stopwatch!

import timer, ttkthemes, tkinter as tk
from tkinter import ttk

# Create new instance of timer
newTimer = timer.Timer()

# Create the frame for the timer
root = ttkthemes.ThemedTk()
root.title("Stopwatch:")

# Create an instance of Style for text formatting
style = ttk.Style()

# Make a variable for the theme to be used later
theme = tk.StringVar()

def dynamic_fonts(event):
    # Specify the correct font size for the size of the window
    fontsize = round(min(root.winfo_width() / 3 / 10, root.winfo_height() / 3.2))
    [style.configure(x, font=(None, fontsize)) for x in ["TButton", "TMenubutton", "TLabel"]]

def update():
    '''Update everything every 10ms'''

    # Update theme
    root.config(theme=theme.get())

    # Update label
    displaytime.config(text=newTimer.gettime(True), anchor="center")
    displaytime.pack(side="top", fill="both", expand=True)

    root.after(10, update)

# Themes array
my_themes = sorted(root.get_themes())

# Buttons frame
frame = ttk.Frame(root)

# Create all of the widgets
displaytime = ttk.Label(root)
ttk.Sizegrip(root).pack(side="bottom", fill="both", expand=False)
ttk.OptionMenu(root, theme, "equilux", *my_themes).pack(side="bottom", fill="both", expand=True)
ttk.Button(frame, text="Start timer", command=newTimer.start).pack(side="left", fill="both", expand=True)
ttk.Button(frame, text="Stop timer", command=newTimer.stop).pack(side="left", fill="both", expand=True)
ttk.Button(frame, text="Resume timer", command=newTimer.resume).pack(side="left", fill="both", expand=True)

# Pack the frame created earlier
frame.pack(side="bottom", fill="both", expand=True)

# All necessary updates for running the stopwatch
update()

# Set up the font scaling
root.bind("<Configure>", dynamic_fonts)

root.mainloop()
