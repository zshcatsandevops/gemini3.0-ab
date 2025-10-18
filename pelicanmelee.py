#!/usr/bin/env python3
"""
Super Smash Bros. Melee Trophy Viewer — "Pelicin on Bicycle"
-------------------------------------------------------------
Version C (Final Melee Style)
Full Melee-style GUI recreation using Tkinter, featuring the
detailed vector-drawn "Pelicin on Bicycle" trophy.

(C) 2025 Flames Co. Labs / Samsoft Interactive
"""

import tkinter as tk
import math

# --- Constants & Melee UI Palette ---------------------------------
APP_TITLE = "Super Smash Bros. Melee — Trophy Viewer"
APP_WIDTH = 640
APP_HEIGHT = 480
BG_COLOR = "#000010"        # Deep Melee blue
FG_COLOR = "white"
GOLD = "#FFD700"
ACCENT = "#404060"          # Separator and highlight color
UI_PANEL = "#101030"        # Right panel background
VIEWPORT_BG = "#202040"     # Trophy viewport background

# --- Trophy Data --------------------------------------------------
TROPHY_NAME = "Pelicin on Bicycle"

TROPHY_FLAVOR_TEXT = (
    "A rarely seen subspecies of the Great North American Pelican, the Pelicin is "
    "known for its insatiable desire for land-based transportation, a curious "
    "trait for a water fowl. After observing a local cycling club, a Pelicin (with "
    "considerable difficulty) acquired a two-wheeler and set about mastering it. "
    "This trophy depicts an early, wobbly attempt.\n\n"
    "N.B.: A fully trained Pelicin can be observed in the background of the Big Blue stage, "
    "often causing minor traffic jams."
)

TROPHY_STATS = (
    "Source: Miscellaneous\n"
    "Type: Normal Trophy\n"
    "How to Get: Complete Classic Mode on Hard with 3 characters."
)

# --- Pelican Color Palette ----------------------------------------
PELICAN_BODY = "#dfe6e9"
PELICAN_BEAK = "#f9d74a"
PELICAN_POUCH = "#f5b445"
PELICAN_LEG = "#f9d74a"
BIKE_FRAME = "#c0392b"
TIRE = "#2c3e50"
METAL = "#bdc3c7"
BASKET = "#a1887f"
FISH = "#7f8c8d"
GOGGLES = "#5d4037"
GOGGLES_LENS = "#75b6d9"
BASE = "#1e272e"

# --- Drawing Functions --------------------------------------------

def draw_wheel(canvas, cx, cy, radius, spokes=10):
    """Draws a bicycle wheel, adapted for the trophy viewport."""
    canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius,
                      fill=TIRE, width=2, outline=METAL)
    canvas.create_oval(cx - radius + 4, cy - radius + 4, cx + radius - 4, cy + radius - 4,
                      outline=METAL, width=2)
    for i in range(spokes):
        angle = (i / spokes) * 2 * math.pi
        x2 = cx + (radius - 4) * math.cos(angle)
        y2 = cy + (radius - 4) * math.sin(angle)
        canvas.create_line(cx, cy, x2, y2, fill=METAL, width=1)
    canvas.create_oval(cx - 4, cy - 4, cx + 4, cy + 4, fill=METAL, outline="black")

def draw_pelican_trophy(canvas):
    """Draws all components of the trophy, with coordinates adjusted for the viewport."""
    # --- Trophy Base ---
    canvas.create_oval(40, 310, 280, 330, fill=BASE, outline=METAL)
    canvas.create_text(160, 320, text="Pelicin on Bicycle", fill=PELICAN_BODY, font=("Arial", 9, "bold"))

    # --- Bicycle ---
    rear_wheel_x, rear_wheel_y = 100, 255
    front_wheel_x, front_wheel_y = 230, 255
    wheel_radius = 50
    bottom_bracket_x, bottom_bracket_y = 150, 255

    draw_wheel(canvas, rear_wheel_x, rear_wheel_y, wheel_radius)
    draw_wheel(canvas, front_wheel_x, front_wheel_y, wheel_radius)

    seat_tube_top_y = 180
    head_tube_top_y = 185
    canvas.create_line(bottom_bracket_x, bottom_bracket_y, bottom_bracket_x, seat_tube_top_y,
                      bottom_bracket_x, seat_tube_top_y, front_wheel_x, head_tube_top_y,
                      front_wheel_x, head_tube_top_y, bottom_bracket_x, bottom_bracket_y,
                      width=6, fill=BIKE_FRAME, capstyle="round", joinstyle="round")
    canvas.create_line(rear_wheel_x, rear_wheel_y, bottom_bracket_x, bottom_bracket_y,
                      bottom_bracket_x, seat_tube_top_y, rear_wheel_x, rear_wheel_y,
                      width=5, fill=BIKE_FRAME, capstyle="round", joinstyle="round")
    canvas.create_line(front_wheel_x, head_tube_top_y, front_wheel_x, rear_wheel_y, width=5, fill=BIKE_FRAME)
    canvas.create_line(front_wheel_x - 8, head_tube_top_y - 12, front_wheel_x + 22, head_tube_top_y,
                      width=5, fill=METAL, capstyle="round")
    canvas.create_polygon(145, 180, 160, 180, 152, 172, fill=TIRE)
    canvas.create_rectangle(147, 265, 155, 270, fill=METAL)

    # --- Pelican ---
    canvas.create_oval(115, 160, 215, 225, fill=PELICAN_BODY, outline="gray")
    canvas.create_polygon(150, 190, 210, 195, 205, 215, 165, 210, fill="#b2bec3", outline="gray")
    canvas.create_line(170, 175, 150, 130, 135, 115, width=20, fill=PELICAN_BODY, capstyle="round", smooth=True)
    canvas.create_oval(115, 90, 155, 130, fill=PELICAN_BODY, outline="gray")
    canvas.create_polygon(120, 105, 40, 110, 50, 125, 125, 120, fill=PELICAN_BEAK, outline="#636e72")
    canvas.create_arc(50, 115, 125, 145, start=180, extent=180, fill=PELICAN_POUCH, outline="#636e72")
    canvas.create_oval(60, 120, 72, 125, fill=FISH)
    canvas.create_oval(74, 119, 86, 124, fill=FISH)
    canvas.create_oval(88, 120, 100, 125, fill=FISH)
    canvas.create_oval(133, 103, 140, 110, fill="black")
    canvas.create_oval(138, 104, 139, 105, fill="white")
    canvas.create_oval(128, 95, 148, 105, fill=GOGGLES, outline="black")
    canvas.create_oval(131, 97, 145, 103, fill=GOGGLES_LENS)
    canvas.create_line(152, 220, 152, 265, width=8, fill=PELICAN_LEG, capstyle="round")

    # --- Basket ---
    canvas.create_polygon(235, 188, 270, 188, 265, 210, 240, 210, fill=BASKET, outline="black")
    canvas.create_oval(242, 192, 254, 197, fill=FISH)
    canvas.create_oval(252, 194, 264, 199, fill=FISH)

# --- Window Setup -------------------------------------------------
root = tk.Tk()
root.title(APP_TITLE)
root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# --- Frames -------------------------------------------------------
left_frame = tk.Frame(root, width=340, height=APP_HEIGHT, bg=BG_COLOR)
right_frame = tk.Frame(root, width=280, height=APP_HEIGHT, bg=UI_PANEL)
left_frame.pack(side="left", fill="y", padx=10, pady=10)
right_frame.pack(side="right", fill="both", padx=(0, 10), pady=10)
left_frame.pack_propagate(False)
right_frame.pack_propagate(False)

# --- Left Frame: Trophy Render Viewport ---------------------------
canvas = tk.Canvas(left_frame, width=320, height=340, bg=VIEWPORT_BG,
                   highlightthickness=2, highlightbackground=ACCENT)
canvas.pack(pady=(40,0))

# Draw the actual trophy
draw_pelican_trophy(canvas)

# --- Lighting Simulation Effect -----------------------------------
for i in range(12):
    y = 5 + i * 2
    # Creates a faint blueish scanline effect at the top
    hex_val = format(25 + i * 3, 'x')
    if len(hex_val) == 1: hex_val = '0' + hex_val
    canvas.create_line(0, y, 320, y, fill=f"#00{hex_val}ff", width=2)

# --- Right Frame: Info Panel --------------------------------------
title_label = tk.Label(right_frame, text=TROPHY_NAME, font=("Helvetica", 18, "bold"),
                       fg=GOLD, bg=UI_PANEL, anchor="w")
title_label.pack(pady=(10, 5), padx=10, fill="x")

separator = tk.Canvas(right_frame, height=2, bg=UI_PANEL, bd=0, highlightthickness=0)
separator.create_line(10, 1, 270, 1, fill=ACCENT)
separator.pack(fill="x", pady=5)

desc_label = tk.Label(right_frame, text=TROPHY_FLAVOR_TEXT, font=("Arial", 10),
                      fg=FG_COLOR, bg=UI_PANEL, justify="left", wraplength=260)
desc_label.pack(pady=(5, 10), padx=10, anchor="n")

stats_label = tk.Label(right_frame, text=TROPHY_STATS, font=("Arial", 9),
                       fg="lightgray", bg=UI_PANEL, justify="left")
stats_label.pack(anchor="w", padx=10, pady=(15, 10))

# --- Footer -------------------------------------------------------
footer = tk.Label(root, text="© 2025 Flames Co. Labs / Samsoft Interactive",
                  font=("Arial", 8), fg="gray", bg=BG_COLOR)
footer.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")

# --- Run ----------------------------------------------------------
root.mainloop()
