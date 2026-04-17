import random

def generate_colors(n=10):
    return[(random.randint(0, 255), random.randint(50, 255), random.randint(50, 255)) for _ in range(n)]
def change_one_color(colors):
    new_colors = colors[:]
    index = random.randint(0, len(colors)-1)

    old = new_colors[index]
    new = old

    while new == old:
        new = (random.randint(50,255),
               random.randint(50,255),
               random.randint(50,255))

    new_colors[index] = new
    return new_colors, index
