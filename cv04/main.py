import cv2
import matplotlib.pyplot as plt
import numpy as np


def brightness_correct(files: tuple[str, str], const_br=255):
    """
    Function for brightness correction of images.
    :param files: tuple of filenames where first is the image with mistake and second is the etalon image
    :param const_br: constant brightness value (default 255)
    """
    img_with_noise = cv2.imread(files[0])
    img_with_noise = cv2.cvtColor(img_with_noise, cv2.COLOR_BGR2RGB)
    noise = cv2.imread(files[1])
    noise = cv2.cvtColor(noise, cv2.COLOR_BGR2RGB)

    # Calculate the noise of the image
    with np.errstate(invalid='ignore'):
        img_etalon = np.true_divide(img_with_noise, noise)
        img_etalon[~np.isfinite(img_etalon)] = 0

    # Plot results
    fig, axs = plt.subplots(1, 3, figsize=(12, 8))
    axs[0].imshow(img_with_noise)
    axs[0].set_title('f(x, y)')
    axs[1].imshow(noise)
    axs[1].set_title('e(x, y)')
    axs[2].imshow(img_etalon)
    axs[2].set_title('g(x, y)')


    plt.tight_layout()
    plt.show()


def histogram_equalize(file: str):
    """
    Function for histogram equalization of image.
    :param file: filename of the image
    """
    img = cv2.imread(file)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    hist = np.histogram(img.flatten(), bins=256, range=(0, 256))[0]

    img_eq = np.zeros_like(img, dtype=np.float64)
    qk = img.max()
    q0 = img.min()
    H = hist.cumsum()
    N = img.size
    for p in range(256):
        q = H[p] * (qk - q0) / N
        img_eq[img == p] = q + q0

    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    axs[0, 0].imshow(img_rgb, cmap='gray')
    axs[0, 0].set_title('Original image')
    axs[0, 1].hist(img.flatten(), bins=256, range=(0, 256))
    axs[0, 1].set_title('Histogram of original image')
    axs[1, 0].imshow(img_eq, cmap='gray')
    axs[1, 0].set_title('Equalized image')
    axs[1, 1].hist(img_eq.flatten(), bins=256, range=(0, 256))
    axs[1, 1].set_title('Histogram of equalized image')







    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    filenames01 = [
        ('Cv04_porucha1.bmp', 'Cv04_porucha1_etalon.bmp'),
        ('Cv04_porucha2.bmp', 'Cv04_porucha2_etalon.bmp'),
    ]
    # for fns in filenames01:
    #     brightness_correct(fns)

    filename02 = 'Cv04_rentgen.bmp'
    histogram_equalize(filename02)