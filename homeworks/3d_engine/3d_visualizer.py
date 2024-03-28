import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

texture = mpimg.imread("resources/texture.png")
height_map = mpimg.imread("resources/heightmap.png")

def draw_triangle(x, y, z, screen_width):
    image = texture.copy()
    dx = int(2 * z / screen_width)
    point = [x - z, y - z]
    while point[1] < y:
        point[0] = x - y + point[1]
        while point[0] < x + y - point[1] and point[0] < len(image):
            image[point[1], point[0]] = (1, 0, 0)
            point[0] += 1
        point[1] += dx

    return image

def render_without_heights(p_x, p_y, camera_height, horizon, scale_height, distance, screen_width, screen_height):
    image = np.ones((screen_height, screen_width, 3)) * np.array([0.529, 0.808, 0.922])

    def draw_vertical_line(point_x, height, max_height, color):
        while height < max_height:
            if (image[int(height), int(point_x)][0] == 0.529 and
                    image[int(height), int(point_x)][1] == 0.808 and
                    image[int(height), int(point_x)][2] == 0.922):
                image[int(height), int(point_x)] = color
            else:
                break
            height += 1

    for z in range(1, distance):
        p_left = [-z + p_x, -z + p_y]
        p_right = [z + p_x, -z + p_y]
        dx = (p_right[0] - p_left[0]) / screen_width

        for i in range(0, screen_width):
            height_on_screen = camera_height / z * scale_height + horizon
            draw_vertical_line(i, height_on_screen, screen_height, texture[int(p_left[1]), int(p_left[0])])
            p_left[0] += dx

    return image

def render_with_heights(p_x, p_y, camera_height, horizon, scale_height, distance, screen_width, screen_height):
    image = np.ones((screen_height, screen_width, 3)) * np.array([0.529, 0.808, 0.922])

    def draw_vertical_line(point_x, height, max_height, color):
        while height < max_height:
            if (image[int(height), int(point_x)][0] == 0.529 and
                    image[int(height), int(point_x)][1] == 0.808 and
                    image[int(height), int(point_x)][2] == 0.922):
                image[int(height), int(point_x)] = color
            else:
                break
            height += 1

    for z in range(1, distance):
        p_left = [-z + p_x, -z + p_y]
        p_right = [z + p_x, -z + p_y]
        dx = (p_right[0] - p_left[0]) / screen_width

        for i in range(0, screen_width):
            height_on_screen = height_map[int(p_left[1]), int(p_left[0])] * screen_height * scale_height / z + horizon - camera_height
            draw_vertical_line(i, height_on_screen / 2, screen_height, texture[int(p_left[1]), int(p_left[0])])
            p_left[0] += dx

    return image


img1 = draw_triangle(400, 300, 200, 128)
img2 = render_without_heights(400, 300, 150, 100, 200, 200, 1000, 1000)
img3 = render_with_heights(400, 300, 150, 100, 200, 200, 1000, 1000)
plt.imshow(img1)
plt.show()
plt.imshow(img2)
plt.show()
plt.imshow(img3)
plt.show()