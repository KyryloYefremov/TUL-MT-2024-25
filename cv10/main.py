import numpy as np
import cv2


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


def markup_based_code(img: np.ndarray):
    ...


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
        markup_based_code(img)
    except Exception as e:
        print(f'Chyba pri cteni souboru: {filename}.\n{e}\n')
        exit(1)
    

        
    



    