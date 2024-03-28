import tkinter
from pathlib import Path

SCREEN_X, SCREEN_Y = 160, 170

SCALE_X = 3
SCALE_Y = 2

STEP_SIZE = 1
FIND_SIZE = 1
PIXEL_SIZE = 1

COLORS = [
    (0, 0, 0),
    (0, 0, 168),
    (0, 168, 0),
    (0, 168, 168),
    (168, 0, 0),
    (168, 0, 168),
    (168, 84, 0),
    (168, 168, 168),
    (84, 84, 84),
    (84, 84, 252),
    (84, 252, 84),
    (84, 252, 252),
    (252, 84, 84),
    (252, 84, 252),
    (252, 252, 84),
    (252, 252, 252)
]

def draw(pic, dx=0, dy=0):
    def draw_line(coords, color_index):
        r, g, b = COLORS[color_index]
        canvas.create_line(
            *[((x + dx) * SCALE_X, (y + dy) * SCALE_Y) for x, y in coords],
            fill=f'#{r:02x}{g:02x}{b:02x}', width=3)

    def fill():
        pass

    def parse_until_F(index):
        parsed = []
        while True:
            if pic[index] >= 240:
                break

            parsed.append(pic[index])
            index += 1

        return parsed

    current_picture_color = 0
    can_draw_picture = False

    ind = 0
    while ind < len(pic):
        print(len(pic) - ind)
        match pic[ind]:
            case 240: #F0 - Change picture color and enable picture draw
                current_picture_color = pic[ind + 1]
                can_draw_picture = True
            case 241: #F1 - Disable picture draw
                can_draw_picture = False
            case 242: #F2 - Change priority color and enable priority draw
                pass # Don't used in task
            case 243: #F3 - Disable priority draw
                pass # Don't used in task
            case 244: #F4 - Draw a Y corner
                if can_draw_picture:
                    coordinates = parse_until_F(ind + 1)
                    x_start, y_start = coordinates[0], coordinates[1]
                    for i in range(2, len(coordinates)):
                        if i % 2 == 0:
                            x_end, y_end = x_start, coordinates[i]
                            draw_line([(x_start, y_start), (x_end, y_end)],
                                      current_picture_color)
                            y_start = y_end
                        else:
                            x_end, y_end = coordinates[i], y_start
                            draw_line([(x_start, y_start), (x_end, y_end)],
                                    current_picture_color)
                            x_start = x_end
                    print("F4 -> " + '.'.join(hex(s) for s in coordinates))
            case 245: #F5 - Draw an X corner
                if can_draw_picture:
                    coordinates = parse_until_F(ind + 1)
                    x_start, y_start = coordinates[0], coordinates[1]
                    for i in range(2, len(coordinates)):
                        if i % 2 != 0:
                            x_end, y_end = x_start, coordinates[i]
                            draw_line([(x_start, y_start), (x_end, y_end)],
                                      current_picture_color)
                            y_start = y_end
                        else:
                            x_end, y_end = coordinates[i], y_start
                            draw_line([(x_start, y_start), (x_end, y_end)],
                                      current_picture_color)
                            x_start = x_end
                    print("F5 -> " + '.'.join(str(s) for s in coordinates))
            case 246: #F6 - Absolute line
                if can_draw_picture:
                    coordinates = parse_until_F(ind + 1)
                    for i in range(0, len(coordinates) - 2, 2):
                        x0, y0 = coordinates[i], coordinates[i + 1]
                        x1, y1 = coordinates[i + 2], coordinates[i + 3]
                        draw_line([(x0, y0), (x1, y1)], current_picture_color)

                    print("F6 -> " + '.'.join(hex(s) for s in coordinates))
            case 247: #F7 - Relative line
                if can_draw_picture:
                    coordinates = parse_until_F(ind + 1)
                    x_start, y_start = coordinates[0], coordinates[1]
                    for byte in coordinates[2:]:
                        sign_x = (byte & int('10000000', 2)) >> 7
                        disp_x = (byte & int('01110000', 2)) >> 4
                        sign_y = (byte & int('00001000', 2)) >> 3
                        disp_y = byte & int('00000111', 2)
                        x_end, y_end = x_start + (-1) ** sign_x * disp_x, y_start + (-1) ** sign_y * disp_y
                        draw_line([(x_start, y_start), (x_end, y_end)], current_picture_color)
                        x_start, y_start = x_end, y_end

                    print("F7 -> " + '.'.join(hex(s) for s in coordinates))
            case 248: #F8 - Fill
                coordinates = parse_until_F(ind + 1)
                if len(coordinates) > 0:
                    for i in range(0, len(coordinates), 2):
                        #x_start, y_start = coordinates[i], coordinates[i + 1]
                        fill()

                    print("F8 -> " + '.'.join(hex(s) for s in coordinates))
            case _:
                pass

        ind += 1


tk = tkinter.Tk()

picture_1_bytes = Path('data/PIC.1').read_bytes()
picture_2_bytes = Path('data/PIC.2').read_bytes()
picture_3_bytes = Path('data/PIC.28').read_bytes()
picture_4_bytes = Path('data/PIC.44').read_bytes()

canvas = tkinter.Canvas(width=SCREEN_X * SCALE_X * 2, height=SCREEN_Y * SCALE_Y * 2)
canvas.create_rectangle(0, 0, SCREEN_X * SCALE_X * 2, SCREEN_Y * SCALE_Y * 2, fill="#ffffff", outline="")
canvas.pack()

draw(picture_2_bytes, 1, 1)
draw(picture_1_bytes, SCREEN_X + 1, 1)
draw(picture_3_bytes, 1, SCREEN_Y - 1)
draw(picture_4_bytes, SCREEN_X + 1, SCREEN_Y - 1)

tk.mainloop()