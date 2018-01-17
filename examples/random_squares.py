import cairodrawbot as db
import numpy as np

# Set the canvas size:
width = 200
height = 400
surface = db.Surface(width, height, bg_color=(1,1,1))

# Generate squares
square_count = 1000
angles = 2*np.pi* np.random.rand(square_count)
sizes = 20 + 20 * np.random.rand(square_count)
positions = width * np.random.rand(square_count, 2)
colors = np.random.rand(square_count, 3)

# Draw squares
for angle, size, position, color in zip(angles, sizes, positions, colors):
    square = db.square(size,
                       xy=position,
                       angle=angle,
                       fill=color,
                       stroke_width=size/20)
    square.draw(surface)

# Export image
surface.write_to_png("random_squares.png")
