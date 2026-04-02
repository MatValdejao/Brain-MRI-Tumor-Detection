# imports
import numpy as np
import matplotlib.pyplot as plt

def max_min(arr: np.ndarray):
    return arr.max(), arr.min()

def arrange_plots(images: np.ndarray, labels: np.ndarray):
    fig = plt.figure(figsize=(16, 8))

    # 2 by 5 grid format
    rows = 2
    cols = 5 

    for i in range(rows):
        for j in range(cols):
            # individual plot to grid
            ax = fig.add_subplot(rows, cols, i * cols + j + 1)
            image_index = int(np.random.randint(0, len(images), size=1))
            ax.imshow(images[image_index])
            
            # set title according to class
            ax.set_title(labels[image_index])
        

    return fig.show()

def average_image(images: np.ndarray, label: str):
    # find the mean image, splice per row
    mean_image = np.mean(images, axis=0)[0]

    # show image
    plt.imshow(mean_image/255)

    plt.title(label + ' Average Image')
    return plt.show()