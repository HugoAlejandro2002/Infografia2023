
def get_line(x0, y0, x1, y1):
    points = []

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    d_x = x1 - x0
    d_y = y1 - y0


    steep = abs(d_y) > abs(d_x)

    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    d_x = x1 - x0
    d_y = y1 - y0

    p_k = 2 * d_y - d_x
    y_k = y0

    for x_k in range(x0, x1 + 1):
        if steep:
            points.append((y_k, x_k))
        else:
            points.append((x_k, y_k))

        if p_k < 0:
            p_k += 2 * d_y
        else:
            y_k += 1
            p_k += 2 * d_y - 2 * d_x

    return points

if __name__ == "__main__":
    print(get_line(2, 2, 10, 5))