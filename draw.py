#!/usr/bin/env python3

from PIL import Image, ImageDraw

def line(x1,y1,x2,y2,draw):
    draw.line((x1, y1, x2, y2), fill="black", width=2)

def four_sided(x1_init, y1_init, X, Y,draw):
    x1 = x1_init
    y1 = y1_init
    x2 = x1_init + X
    y2 = y1_init
    line(x1,y1,x2,y2,draw)
    line(x1,y1,x1,y2+Y,draw)
    line(x2,y2,x2,y2+Y,draw)
    line(x1,y1+Y,x2,y2+Y,draw)

def stack_horizontally(x1_init, y1_init, X, Y, count, draw):
    for i in range(count):
        x1 = x1_init + i*(X+1)
        y1 = y1_init
        four_sided(x1, y1, X, Y, draw)

def get_golden_ratio():
    return (1 + 5 ** 0.5) / 2

def main():
    Y = 100
    # X = Y * get_golden_ratio()     # for golden ratio
    # X = Y                          # for square
    X = Y * (3/2)                    # for approximation of golden ratio
    repeat = 5
    height = Y*repeat               # image height (must fit Y)
    width = round(X*repeat)         # image width (must fit X)

    # Create a white image
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    # Initial coordinates
    x1 = 0
    y1 = 0
    for i in range(repeat):
        stack_horizontally(x1, y1, X, Y, 8, draw)
        y1 += Y
    
    # View the image
    img.show()

    # Optional: save to file
    # img.save("perpendicular_line.png")


if __name__ == "__main__":
    main()
