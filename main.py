import time
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Rasterization")

fig1 = plt.Figure(figsize=(5, 4), dpi=60)
ax1 = fig1.add_subplot(111)
ax1.set_title('Digital Difference Analyzer')
canvas1 = FigureCanvasTkAgg(fig1, master=root)
canvas1.get_tk_widget().grid(row=0, column=0, padx=0, pady=0)

fig2 = plt.Figure(figsize=(5, 4), dpi=60)
ax2 = fig2.add_subplot(111)
ax2.set_title('Step by step')
canvas2 = FigureCanvasTkAgg(fig2, master=root)
canvas2.get_tk_widget().grid(row=0, column=1, padx=0, pady=0)

fig3 = plt.Figure(figsize=(5, 4), dpi=60)
ax3 = fig3.add_subplot(111)
ax3.set_title('Bresenham circle')
canvas3 = FigureCanvasTkAgg(fig3, master=root)
canvas3.get_tk_widget().grid(row=0, column=2, padx=0, pady=0)

fig4 = plt.Figure(figsize=(5, 4), dpi=60)
ax4 = fig4.add_subplot(111)
ax4.set_title('Bresenham line')
canvas4 = FigureCanvasTkAgg(fig4, master=root)
canvas4.get_tk_widget().grid(row=0, column=3, padx=0, pady=0)

params1_x1 = tk.Scale(root, from_=0, to=300, orient=tk.HORIZONTAL, label="x1")
params1_x1.grid(row=1, column=0, padx=5, pady=5)

params1_y1 = tk.Scale(root, from_=0, to=300, orient=tk.HORIZONTAL, label="y1")
params1_y1.grid(row=2, column=0, padx=5, pady=5)

params1_x2 = tk.Scale(root, from_=0, to=300, orient=tk.HORIZONTAL, label="x2")
params1_x2.grid(row=3, column=0, padx=5, pady=5)

params1_y2 = tk.Scale(root, from_=0, to=300, orient=tk.HORIZONTAL, label="y2")
params1_y2.grid(row=4, column=0, padx=5, pady=5)

submit1 = ttk.Button(root, text="Submit")
submit1.grid(row=5, column=0, padx=5, pady=5)

label11 = tk.Label(root, text="Time:")
label11.grid(row=6, column=0, padx=5, pady=5)

params2_x1 = tk.Scale(root, from_=0, to=300, orient=tk.HORIZONTAL, label="x1")
params2_x1.grid(row=1, column=1, padx=5, pady=5)

params2_y1 = tk.Scale(root, from_=0, to=300, orient=tk.HORIZONTAL, label="y1")
params2_y1.grid(row=2, column=1, padx=5, pady=5)

params2_x2 = tk.Scale(root, from_=0, to=300, orient=tk.HORIZONTAL, label="x2")
params2_x2.grid(row=3, column=1, padx=5, pady=5)

params2_y2 = tk.Scale(root, from_=0, to=300, orient=tk.HORIZONTAL, label="y2")
params2_y2.grid(row=4, column=1, padx=5, pady=5)

submit2 = ttk.Button(root, text="Submit")
submit2.grid(row=5, column=1, padx=5, pady=5)


params3_r = tk.Scale(root, from_=0, to=50, orient=tk.HORIZONTAL, label="r")
params3_r.grid(row=1, column=2, padx=5, pady=5)

params3_x = tk.Scale(root, from_=0, to=50, orient=tk.HORIZONTAL, label="x")
params3_x.grid(row=2, column=2, padx=5, pady=5)

params3_y = tk.Scale(root, from_=0, to=50, orient=tk.HORIZONTAL, label="y")
params3_y.grid(row=3, column=2, padx=5, pady=5)

submit3 = ttk.Button(root, text="Submit")
submit3.grid(row=5, column=2, padx=5, pady=5)

params4_x1 = tk.Scale(root, from_=0, to=300, orient=tk.HORIZONTAL, label="x1")
params4_x1.grid(row=1, column=3, padx=5, pady=5)

params4_y1 = tk.Scale(root, from_=0, to=300, orient=tk.HORIZONTAL, label="y1")
params4_y1.grid(row=2, column=3, padx=5, pady=5)

params4_x2 = tk.Scale(root, from_=0, to=300, orient=tk.HORIZONTAL, label="x2")
params4_x2.grid(row=3, column=3, padx=5, pady=5)

params4_y2 = tk.Scale(root, from_=0, to=300, orient=tk.HORIZONTAL, label="y2")
params4_y2.grid(row=4, column=3, padx=5, pady=5)

submit4 = ttk.Button(root, text="Submit")
submit4.grid(row=5, column=3, padx=5, pady=5)

label12 = tk.Label(root, text="")
label12.grid(row=7, column=0, padx=5, pady=5)
label22 = tk.Label(root, text="")
label22.grid(row=7, column=1, padx=5, pady=5)
label32 = tk.Label(root, text="")
label32.grid(row=7, column=2, padx=5, pady=5)
label42 = tk.Label(root, text="")
label42.grid(row=7, column=3, padx=5, pady=5)
label21 = tk.Label(root, text="Time:")
label21.grid(row=6, column=1, padx=5, pady=5)
label31 = tk.Label(root, text="Time:")
label31.grid(row=6, column=2, padx=5, pady=5)
label41 = tk.Label(root, text="Time:")
label41.grid(row=6, column=3, padx=5, pady=5)


def dda():
    ax1.clear()
    ax1.set_title('Digital Difference Analyzer')

    x1 = params1_x1.get()
    y1 = params1_y1.get()
    x2 = params1_x2.get()
    y2 = params1_y2.get()

    if x1 > x2 or y1 > y2:
        messagebox.showerror('error', 'Bad coordinates!')
        return

    dx = x2 - x1
    dy = y2 - y1

    if dx > dy:
        steps = dx
    else:
        steps = dy

    x_increment = dx / steps
    y_increment = dy / steps

    start = time.time()
    for i in range(int(steps)):
        ax1.plot(x1, y1, 'ko')
        fig1.canvas.draw()
        x1 = x1 + x_increment
        y1 = y1 + y_increment
    end = time.time()
    canvas1.draw()
    label12.config(text=(end - start))


def step_by_step():
    ax2.clear()
    ax2.set_title('Step by step')

    x1 = params2_x1.get()
    y1 = params2_y1.get()
    x2 = params2_x2.get()
    y2 = params2_y2.get()

    if x1 > x2:
        messagebox.showerror('error', 'Bad coordinates!')
        return

    k = (y2 - y1) / (x2 - x1)
    b = y2 - k * x2
    dx = abs(x2 - x1) / (max(abs(x2 - x1), abs(y2 - y1) * 2))
    if x2 > x1:
        dx = dx
    else:
        dx = -dx

    x = x1
    y = k * x + b

    start = time.time()
    while x < x2:
        ax2.plot(x, y, 'ko')
        fig2.canvas.draw()
        y = k * x + b
        x = x + dx
    end = time.time()
    canvas2.draw()
    label22.config(text=(end - start))


def plot(_x, _y, _radius):
    ax3.plot(_x, _y, 'ko')
    ax3.plot(-_x, _y, 'ko')
    ax3.plot(_x, -_y, 'ko')
    ax3.plot(-_x, -_y, 'ko')

    ax3.plot(_y, _x, 'ko')
    ax3.plot(_y, -_x, 'ko')
    ax3.plot(-_y, _x, 'ko')
    ax3.plot(-_y, -_x, 'ko')
    fig3.canvas.draw()


def bresenham_circle():
    ax3.clear()
    ax3.set_title('Bresenham circle')

    r = params3_r.get()
    x = params3_x.get()
    y = params3_y.get()

    d = 3 - 2 * r
    start = time.time()
    while y >= x:
        plot(x, y, r)
        x = x + 1
        if d > 0:
            y = y - 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
    end = time.time()
    canvas3.draw()
    label32.config(text=(end - start))


def bresenham_line():
    ax4.clear()
    ax4.set_title('Bresenham line')

    x1 = params4_x1.get()
    x2 = params4_x2.get()
    y1 = params4_y1.get()
    y2 = params4_y2.get()
    dx = x2 - x1
    dy = y2 - y1
    slope = abs(dy / dx)

    error = 0.0
    y = y1
    x = x1
    start = time.time()
    while x < x2:
        ax4.plot(x, y, 'ko')
        fig4.canvas.draw()
        x = x + 1
        error = error + slope
        if error >= 0.5:
            y = y + 1
            error -= 1.0
    end = time.time()
    canvas4.draw()
    label42.config(text=(end - start))


submit1.config(command=dda)
submit2.config(command=step_by_step)
submit3.config(command=bresenham_circle)
submit4.config(command=bresenham_line)


root.mainloop()
