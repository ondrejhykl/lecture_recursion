import matplotlib.pyplot as plt


def floodfill(img, x, y):
    if x < 0 or y < 0 or y >= len(img) or x >= len(img[y]):
        return img
    elif img[y][x] == 0 or img[y][x] == 2:
        return img
    else:
        if img[y][x] == 1:
            img[y][x] = 2

            plt.imshow(img, cmap="summer")
            plt.show(block=False)
            plt.pause(0.001)
            plt.clf()

            floodfill(img, x + 1, y)
            floodfill(img, x - 1, y)
            floodfill(img, x, y + 1)
            floodfill(img, x, y - 1)
            return img


def main():
    # img = plt.imread("files/img0.png")[:, :, 0]
    # img = plt.imread("files/img1.png")[:, :, 0]
    img = plt.imread("files/img2.png")[:, :, 0]

    img = floodfill(img, 0, 0)

    plt.imshow(img, cmap="summer")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()
