import cv2
import numpy as np

def remove_background(image_path):
    img = cv2.imread(image_path)

    mask = np.zeros(img.shape[:2], np.uint8)
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    rect = (50, 50, img.shape[1]-50, img.shape[0]-50)

    cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT) #GrabCut algorithm

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    result = img * mask2[:, :, np.newaxis]

    cv2.imshow("Original Image", img)
    cv2.imshow("Foreground", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":

    image_path = "img-path"
    remove_background(image_path)
