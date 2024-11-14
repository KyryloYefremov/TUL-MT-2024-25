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

# TODO: fix algorithm
def dct_difference(prev_frame, curr_frame, top_coeffs=5):    
    def compute_dct(gray_frame):
        M, N = gray_frame.shape
        dct_result = np.zeros((M, N))
        
        def c(k):
            return 1 / np.sqrt(2) if k == 0 else 1
        
        # Создаем индексы x и y, а также u и v
        x = np.arange(M)
        y = np.arange(N)
        u = np.arange(M).reshape((M, 1))
        v = np.arange(N).reshape((N, 1))
        
        # Вычисляем матрицы косинусов для всех значений x, y, u и v
        cos_x_u = np.cos((2 * x[:, None] + 1) * u * np.pi / (2 * M))  # M x M
        cos_y_v = np.cos((2 * y + 1) * v * np.pi / (2 * N))           # N x N
        
        # Вычисляем DCT
        for u in range(M):
            for v in range(N):
                # Вычисляем сумму по x и y для заданных u и v
                sum_result = np.sum(gray_frame * cos_x_u[:, u] * cos_y_v[:, v])
                dct_result[u, v] = (2 * c(u) * c(v) / N) * sum_result
        
        return dct_result


    prev_frame_dct = compute_dct(prev_frame)
    curr_frame_dct = compute_dct(curr_frame)

    prev_frame_dct = prev_frame_dct.flatten() * prev_frame_dct.flatten()
    curr_frame_dct = curr_frame_dct.flatten() * curr_frame_dct.flatten()

    prev_frame_energy = np.log(prev_frame_dct)
    curr_frame_energy = np.log(curr_frame_dct)

    top_indices = np.argpartition(prev_frame_energy, -top_coeffs)[-top_coeffs:]  # Индексы P самых больших значений
    prev = prev_frame_energy[top_indices]
    top_indices = np.argpartition(curr_frame_energy, -top_coeffs)[-top_coeffs:]
    curr = curr_frame_energy[top_indices]
    

    return np.sum(prev - curr)




if __name__ == "__main__":
    cap = cv2.VideoCapture('cv08/cv08_video.mp4')
    NFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 

    ret, prev_bgr = cap.read()
    prev_gray = np.array(cv2.cvtColor(prev_bgr, cv2.COLOR_BGR2GRAY), dtype=np.int64)

    method_1_diffs = []
    method_2_diffs = []
    method_3_diffs = []
    method_4_diffs = []

    for i in range(1, NFrames):
        ret, bgr = cap.read()

        if not ret:
            break

        curr_gray = np.array(cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY), dtype=np.int64)

        method_1_diffs.append(abs_pixel_sum_difference(prev_gray, curr_gray))
        method_2_diffs.append(sum_pixel_abs_difference(prev_gray, curr_gray))
        method_3_diffs.append(histogram_difference(prev_gray, curr_gray))
        method_4_diffs.append(dct_difference(prev_gray, curr_gray))

        prev_gray = curr_gray 
    
    cap.release()

    vs = np.zeros(NFrames)
    MAX = max(method_1_diffs)
    vs[208] = MAX
    vs[268] = MAX

    # Plot the differences
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2 строки, 2 столбца подграфиков

    # Первый подграфик
    axs[0, 0].plot(vs, color='red', label='Segments boarders')
    axs[0, 0].plot(method_1_diffs, color='blue', label='Frame difference')
    # axs[0, 0].set_xlabel('Frames')
    # axs[0, 0].set_ylabel('Sum of Pixel Differences')
    axs[0, 0].set_title('Method #1')
    axs[0, 0].grid()

    # Второй подграфик
    axs[0, 1].plot(vs, color='red', label='Segments boarders')
    axs[0, 1].plot(method_2_diffs, color='blue', label='Frame difference')
    # axs[0, 1].set_xlabel('Frames')
    # axs[0, 1].set_ylabel('Sum of Pixel Differences')
    axs[0, 1].set_title('Method #2')
    axs[0, 1].grid()

    # Третий подграфик
    axs[1, 0].plot(vs, color='red', label='Segments boarders')
    axs[1, 0].plot(method_3_diffs, color='blue', label='Frame difference')
    axs[1, 0].set_title('Method #3')
    axs[1, 0].grid()

    # Четвертый подграфик
    axs[1, 1].plot(vs, color='red', label='Segments boarders')
    axs[1, 1].plot(method_4_diffs, color='blue', label='Frame difference')
    axs[1, 1].set_title('Method #4')
    axs[1, 1].grid()

    # Добавляем общие подписи
    # fig.suptitle("Четыре функции на подграфиках")  # Общий заголовок для всех графиков
    # plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Оставляем место для общего заголовка

    # Отображаем график
    plt.show()