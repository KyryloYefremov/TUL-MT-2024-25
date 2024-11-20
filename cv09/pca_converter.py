import cv2
import numpy as np
import matplotlib.pyplot as plt


def pca(img_rgb):
    """
    Principal Component Analysis algorithm.
    Steps were taken from the uni lecture.
    """
    M = img_rgb.shape[-1]
    vectors = []

    # 1. split M-channel img to M vectors (by last dim - channel dim).
    for m in range(M):
        vectors.append(
            img_rgb[:, :, m].flatten()  # size N
            )

    # print([sig.shape for sig in vectors])
    
    # 2. compute 'mean vector'
    mean_vec = np.mean(vectors, axis=0)

    # 3. create new vectors as: vector - mean_vec for all M vectors
    w_vectors = vectors - mean_vec  # MxN

    # 4. create a martix of w_vectors 
    w_matrix = np.array(w_vectors)  # MxN

    # 5. compute covariance matrix
    cov_matrix = w_matrix @ w_matrix.T  # MxM

    # 6-7. calculate eigenvalues and eigenvectors. 
    _, eigenvectors_matrix = np.linalg.eig(cov_matrix)  # MxM

    # 8. eigenspace then is calculated as eigenvectors_matrix @ w_matrix
    eigenspace = eigenvectors_matrix @ w_matrix

    # 9. calculate all components as: k = e[i] + mean_vector, where eigenspace = [ e[0], ..., e[M-1] ]
    components = eigenspace + mean_vec

    return components


if __name__ == "__main__":
    bgr = cv2.imread('cv09/Cv09_obr.bmp')
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    rgb = rgb.astype('uint8')
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

    img_comps = pca(rgb)
    comp1 = img_comps[0].reshape(gray.shape)

    fig, axs = plt.subplots(1, 2, figsize=(10, 6))

    # show the origin image in gray scale
    axs[0].imshow(gray, cmap='gray')
    axs[0].set_title('RGB2GRAY')

    # show monochrome image received from pca algo
    axs[1].imshow(comp1, cmap='gray')
    axs[1].set_title('PCA K=1')
    
    plt.tight_layout()
    plt.show()