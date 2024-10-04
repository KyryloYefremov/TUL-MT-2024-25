import cv2
import matplotlib.pyplot as plt


def read_bmp(file):
    bgr = cv2.imread(file)
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

    rgb = rgb.astype('uint8')

    ###### Show RGB ######
    fig, axs = plt.subplots(1, 2, figsize=(10, 10))
    axs[0].imshow(rgb)
    axs[0].set_title('RGB')

    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    axs[1].imshow(gray, cmap='gray')
    axs[1].set_title('Gray')

    fig.tight_layout()
    plt.show()

    ###### Show HSV ######
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    axs[0, 0].imshow(rgb)
    axs[0, 0].set_title('RGB')

    axs[0, 1].imshow(hsv[:, :, 0], cmap='jet')
    axs[0, 1].set_title('H')
    fig.colorbar(axs[0, 1].images[0], ax=axs[0, 1])

    axs[1, 0].imshow(hsv[:, :, 1], cmap='jet')
    axs[1, 0].set_title('S')
    fig.colorbar(axs[1, 0].images[0], ax=axs[1, 0])

    axs[1, 1].imshow(hsv[:, :, 2], cmap='jet')
    axs[1, 1].set_title('V')
    fig.colorbar(axs[1, 1].images[0], ax=axs[1, 1])

    fig.tight_layout()
    plt.show()

    ###### Show YCrCb ######
    ycrcb = cv2.cvtColor(rgb, cv2.COLOR_RGB2YCrCb)
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    axs[0, 0].imshow(rgb)
    axs[0, 0].set_title('RGB')

    axs[0, 1].imshow(ycrcb[:, :, 0], cmap='gray')
    axs[0, 1].set_title('Y')
    fig.colorbar(axs[0, 1].images[0], ax=axs[0, 1])

    axs[1, 0].imshow(ycrcb[:, :, 1], cmap='jet')
    axs[1, 0].set_title('Cr')
    fig.colorbar(axs[1, 0].images[0], ax=axs[1, 0])

    axs[1, 1].imshow(ycrcb[:, :, 2], cmap='jet')
    axs[1, 1].set_title('Cb')
    fig.colorbar(axs[1, 1].images[0], ax=axs[1, 1])

    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    read_bmp("cv03_objekty1.bmp")
