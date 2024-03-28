import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


SCREEN_X, SCREEN_Y = 160, 170

BASE_COLOR = (1, 1, 1)
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

def draw(pic, delta_x=0, delta_y=0):
    def draw_line(coords, color_index):
        x1, y1 = coords[0][0] + delta_x, coords[0][1] + delta_y
        x2, y2 = coords[1][0] + delta_x, coords[1][1] + delta_y
        color = [i / 255 for i in COLORS[color_index]]
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = -1 if x1 > x2 else 1
        sy = -1 if y1 > y2 else 1
        err = dx - dy

        while True:
            RENDER_TEXTURE[y1, x1] = color
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy
    def fill(start_x, start_y, color_index):
        start_x, start_y = start_x + delta_x, start_y + delta_y
        color = [i / 255 for i in COLORS[color_index]]
        target_color = BASE_COLOR

        if np.all(target_color == color):
            return

        stack = [(start_x, start_y)]
        fill_cache = set()
        while stack:
            x, y = stack.pop()
            if (not (x, y) in fill_cache
                    and np.all(RENDER_TEXTURE[y, x] == target_color)):
                fill_cache.add((x, y))
                RENDER_TEXTURE[y, x] = color
                if x > 0 and np.all(RENDER_TEXTURE[y, x - 1] == target_color):
                    stack.append((x - 1, y))
                if x < RENDER_TEXTURE.shape[1] - 1 and np.all(
                        RENDER_TEXTURE[y, x + 1] == target_color):
                    stack.append((x + 1, y))
                if y > 0 and np.all(RENDER_TEXTURE[y - 1, x] == target_color):
                    stack.append((x, y - 1))
                if y < RENDER_TEXTURE.shape[0] - 1 and np.all(
                        RENDER_TEXTURE[y + 1, x] == target_color):
                    stack.append((x, y + 1))
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
        match pic[ind]:
            case 240: #F0 - Change picture color and enable picture draw
                current_picture_color = pic[ind + 1]
                can_draw_picture = True
                print("F0 -> change picture color to " + str(COLORS[current_picture_color]))
            case 241: #F1 - Disable picture draw
                can_draw_picture = False
                print("F1 -> disable picture draw")
            case 242: #F2 - Change priority color and enable priority draw
                print("F2 -> change priority color")
            case 243: #F3 - Disable priority draw
                print("F3 -> disable priority draw")
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
                    print("F4 -> draw a Y corner at " + '.'.join(hex(s) for s in coordinates))
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
                    print("F5 -> draw a X corner at " + '.'.join(str(s) for s in coordinates))
            case 246: #F6 - Absolute line
                if can_draw_picture:
                    coordinates = parse_until_F(ind + 1)
                    for i in range(0, len(coordinates) - 2, 2):
                        x0, y0 = coordinates[i], coordinates[i + 1]
                        x1, y1 = coordinates[i + 2], coordinates[i + 3]
                        draw_line([(x0, y0), (x1, y1)], current_picture_color)

                    print("F6 -> draw an absolute line at " + '.'.join(hex(s) for s in coordinates))
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

                    print("F7 -> draw a relative line at " + '.'.join(hex(s) for s in coordinates))
            case 248: #F8 - Fill
                coordinates = parse_until_F(ind + 1)
                if len(coordinates) > 0:
                    for i in range(0, len(coordinates), 2):
                        x_start, y_start = coordinates[i], coordinates[i + 1]
                        fill(x_start, y_start, current_picture_color)
                    print("F8 -> fill image at " + '.'.join(hex(s) for s in coordinates))
            case _:
                pass

        ind += 1

def beauty_texture():
    print("Make the texture beautiful!")
    for x in range(SCREEN_X * SCALE_X):
        for y in range(SCREEN_Y * SCALE_Y):
            if tuple(RENDER_TEXTURE[y, x]) == (1, 1, 1):
                if x - 1 > 0:
                    RENDER_TEXTURE[y, x] = RENDER_TEXTURE[y, x - 1]
                elif x + 1 < SCREEN_X:
                    RENDER_TEXTURE[y, x] = RENDER_TEXTURE[y, x + 1]
                elif y - 1 > 0:
                    RENDER_TEXTURE[y, x] = RENDER_TEXTURE[y - 1, x]
                elif y + 1 < SCREEN_Y:
                    RENDER_TEXTURE[y, x] = RENDER_TEXTURE[y + 1, x]

# Read binary data files
picture_1_bytes = Path('data/PIC.1').read_bytes()
picture_1_fix_bytes = Path('data/PIC_fix.1').read_bytes()
picture_2_bytes = Path('data/PIC.2').read_bytes()
picture_3_bytes = Path('data/PIC.28').read_bytes()
picture_4_bytes = Path('data/PIC.44').read_bytes()

# Set the Render Texture
SCALE_X = 2
SCALE_Y = 2
RENDER_TEXTURE = np.ones((SCREEN_Y * SCALE_Y, SCREEN_X * SCALE_X, 3)) * np.array(BASE_COLOR)

# Draw all screens
draw(picture_2_bytes, 0, 0)
draw(picture_1_fix_bytes, SCREEN_X, 0)
draw(picture_3_bytes, 0, SCREEN_Y)
draw(picture_4_bytes, SCREEN_X, SCREEN_Y)

# Delete white pixels from texture
#beauty_texture()

# Show the texture
plt.imshow(RENDER_TEXTURE)
plt.axis('off')
plt.show()