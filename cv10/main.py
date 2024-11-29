import numpy as np
import cv2
from matplotlib import pyplot as plt


def detect_circles(img: np.ndarray):
    H, W, _ = img.shape  # get height and width of an img

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    try:
        circles = cv2.HoughCircles(
            gray,                # grayscale img
            cv2.HOUGH_GRADIENT,  # detection method
            dp=1.5,              # resolution of the original image / resolution of the accum. matrix
            minDist=30,          # min distance btw circles' centers
            param1=100,          # canny edge detection
            param2=30,           # threshold value of the accum. matrix for circle detection
            minRadius=0,         # min circle radius
            maxRadius=50         # max circle radius
        )
    except Exception as e:
        print("Wasn't found any circles")
        print(e)
        exit(1)
    else:
        ### DRAW CIRCLES
        # circles = np.uint16(np.around(circles))
        # for i in circles[0,:]:
        #     # draw the outer circle
        #     cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        #     # draw the center of the circle
        #     cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

        circles_number = circles.shape[1]
        
        cv2.putText(
            img,
            str(circles_number), 
                (W//2 - 25 , H-20),  # position
                cv2.FONT_HERSHEY_SIMPLEX,  # font
                2,  # font scale 
                (0, 255, 0),  # rgb color (green)
                3,  # text thickness
                cv2.LINE_AA  # line type
            )

        cv2.imshow('Detected circles', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def markup_based_code(gray_img: np.ndarray):
    markers = []
    eroded = gray_img.copy()
    kernel = np.ones((3, 3), np.uint8)

    erosion_number = 0

    while np.any(eroded):
        erosion_number += 1
        prev_eroded = eroded.copy()
        eroded = cv2.erode(eroded, kernel, iterations=1)
        eroded_part = prev_eroded - eroded

        coords = np.column_stack(np.where(eroded_part == 1))  # coordinates of markers
        markers = coords

    return markers, erosion_number-1


def markup_based_decode(markers, shape, erosions_number):
    reconstructed = np.zeros(shape, dtype=np.uint8)
    kernel = np.ones((3, 3), np.uint8)

    for marker in markers:
        reconstructed[marker[0], marker[1]] = 1

    reconstructed = cv2.dilate(reconstructed, kernel, iterations=erosions_number)
    return reconstructed


if __name__ == "__main__":
    ### Task 1 ###
    cv_dir = 'cv10/'
    filenames = [
        'Cv11_c01.bmp',
        'Cv11_c02.bmp',
        'Cv11_c03.bmp',
        'Cv11_c04.bmp',
        'Cv11_c05.bmp',
        'Cv11_c06.bmp',
    ]

    for filename in filenames:
        try:
            img = cv2.imread(cv_dir + filename)
            detect_circles(img)
        except Exception as e:
            print(f'Chyba pri cteni souboru: {filename}.\n{e}\n')
            exit(1)

    ### Task 2 ###
    filename = 'Cv11_merkers.bmp'
    try:
        img = cv2.imread(cv_dir + filename)
    except Exception as e:
        print(f'Chyba pri cteni souboru: {filename}.\n{e}\n')
        exit(1)

    # split the img to 2 parts (up and bottom)
    H = img.shape[0]  # img height
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) / 255.0  # convert to grayscale binary img
    up_gray = gray[:H // 2, :]
    bottom_gray = gray[H // 2:, :]

    # run markup based coding on two halfs
    up_markers, erosions_num_up = markup_based_code(up_gray)
    bottom_markers, erosions_num_bottom = markup_based_code(bottom_gray)

    up_coded_img = np.zeros(up_gray.shape)
    for marker in up_markers:
        up_coded_img[marker[0], marker[1]] = 1
    bottom_coded_img = np.zeros(bottom_gray.shape)
    for marker in bottom_markers:
        bottom_coded_img[marker[0], marker[1]] = 1
    coded_img = np.vstack((up_coded_img, bottom_coded_img))

    # run decoding
    reconstructed_upper = markup_based_decode(up_markers, up_gray.shape, erosions_num_up)
    reconstructed_lower = markup_based_decode(bottom_markers, bottom_gray.shape, erosions_num_bottom)

    # reconstruct the original img from two halfs
    reconstructed_image = np.vstack((reconstructed_upper, reconstructed_lower))

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.title("Původní obrázek")
    plt.imshow(gray, cmap='gray')
    plt.subplot(1, 3, 2)
    plt.title("Zakodovaný obrázek")
    plt.imshow(coded_img, cmap='gray')
    plt.subplot(1, 3, 3)
    plt.title("Rekonstruovaný obrázek")
    plt.imshow(reconstructed_image, cmap='gray')
    plt.show()

    # markers coords
    print(f"Obrazek 1:\nZnacky: {up_markers}\nPocet erozi: {erosions_num_up}")
    print("=============")
    print(f"Obrazek 2:\nZnacky: {bottom_markers}\nPocet erozi: {erosions_num_bottom}")
    

        
    



    