import cv2
import numpy as np
import matplotlib.pyplot as plt


def abs_pixel_sum_difference(prev_frame: np.array, curr_frame: np.array):
    return np.abs(prev_frame.sum() - curr_frame.sum())


def sum_pixel_abs_difference(prev_frame, curr_frame):
    return np.sum(np.abs(prev_frame - curr_frame))


def histogram_difference(prev_frame, curr_frame):
    # compute histograms
    hist_prev = np.histogram(prev_frame.flatten(), bins=256, range=(0, 256))[0]
    hist_curr = np.histogram(curr_frame.flatten(), bins=256, range=(0, 256))[0]
    
    return np.sum(np.abs(hist_prev - hist_curr))


def dct_difference(prev_frame, curr_frame, top_coeffs=5):    
    ### This implemantation might work, but is very slow
    # def compute_dct(gray_frame):
    #     M, N = gray_frame.shape
    #     dct_result = np.zeros((M, N))
        
    #     # coefficient compution
    #     c = lambda k: 1 / np.sqrt(2) if k == 0 else 1
        
    #     # init
    #     x = np.arange(M)
    #     y = np.arange(N)
    #     u = np.arange(M).reshape((M, 1))
    #     v = np.arange(N).reshape((N, 1))
        
    #     # compute cos matrices for x, y, u and v
    #     cos_x_u = np.cos((2 * x + 1) * u * np.pi / (2 * M))  # M x M 
    #     cos_y_v = np.cos((2 * y + 1) * v * np.pi / (2 * N))  # N x N 
        
    #     # compute DCT
    #     for u in range(M):
    #         for v in range(N):
    #             # compute the sum along x and y for u and v
    #             sum_result = np.sum(gray_frame * cos_x_u[:, u].reshape(M, 1) * cos_y_v[:, v])
    #             dct_result[u, v] = (2 * c(u) * c(v) / N) * sum_result
        
    #     return dct_result

    prev_frame_dct = cv2.dct(np.float32(prev_frame))
    curr_frame_dct = cv2.dct(np.float32(curr_frame))

    # compute power of each frame dct
    prev_frame_power = (prev_frame_dct ** 2).flatten()
    curr_frame_power = (curr_frame_dct ** 2).flatten()

    # find 'top_coeffs' the most higher values
    prev_top_coeffs = np.sort(prev_frame_power)[::-1][:top_coeffs]
    curr_top_coeffs = np.sort(curr_frame_power)[::-1][:top_coeffs]

    # normilize using logarithm
    prev = np.log(prev_top_coeffs)
    curr = np.log(curr_top_coeffs)
    
    return np.sum(abs(prev - curr))


if __name__ == "__main__":
    cap = cv2.VideoCapture('cv08/cv08_video.mp4')
    NFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 

    ret, prev_bgr = cap.read()
    prev_gray = np.array(cv2.cvtColor(prev_bgr, cv2.COLOR_BGR2GRAY), dtype=np.int64)

    method_1_diffs = []
    method_2_diffs = []
    method_3_diffs = []
    method_4_diffs = []

    # per frame
    for i in range(1, NFrames):
        ret, bgr = cap.read()

        # if reading wasn't successful => quit
        if not ret:
            break
        
        curr_gray = np.array(cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY), dtype=np.int64)

        # compute difference btw frame[i] and frame[i+1] using all 4 methods. Store results for every method
        method_1_diffs.append(abs_pixel_sum_difference(prev_gray, curr_gray))
        method_2_diffs.append(sum_pixel_abs_difference(prev_gray, curr_gray))
        method_3_diffs.append(histogram_difference(prev_gray, curr_gray))
        method_4_diffs.append(dct_difference(prev_gray, curr_gray))

        prev_gray = curr_gray 
    
    cap.release()

    vs = np.zeros(NFrames)  # vector to represent segments boundaries

    # Plot the differences
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    
    # 1)
    MAX = max(method_1_diffs)
    vs[208] = MAX
    vs[268] = MAX
    axs[0, 0].plot(vs, color='red', label='Segments boarders')
    axs[0, 0].plot(method_1_diffs, color='blue', label='Frame difference')
    axs[0, 0].set_title('Method #1')

    # 2)
    MAX = max(method_2_diffs)
    vs[208] = MAX
    vs[268] = MAX
    axs[0, 1].plot(vs, color='red', label='Segments boarders')
    axs[0, 1].plot(method_2_diffs, color='blue', label='Frame difference')
    axs[0, 1].set_title('Method #2')
    
    # 3)
    MAX = max(method_3_diffs)
    vs[208] = MAX
    vs[268] = MAX
    axs[1, 0].plot(vs, color='red', label='Segments boarders')
    axs[1, 0].plot(method_3_diffs, color='blue', label='Frame difference')
    axs[1, 0].set_title('Method #3')

    # 4)
    MAX = max(method_4_diffs)
    vs[208] = MAX
    vs[268] = MAX
    axs[1, 1].plot(vs, color='red', label='Segments boarders')
    axs[1, 1].plot(method_4_diffs, color='blue', label='Frame difference')
    axs[1, 1].set_title('Method #4')

    plt.show()