import numpy as np
import cv2

def calc_histo(image, histSize, ranges=[0,256]):
    hist = np.zeros((histSize,1), np.float32)

    gap = ranges[1]/histSize

    for i in (image/gap).flat:
        hist[int(i)] += 1
    
    return hist

def draw_histo(hist, shape=(200,256)):
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist,hist,0,shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1]/hist.shape[0]

    for i, h in enumerate(hist):
        x = int(round(i*gap))
        w = int(round(gap))
        cv2.rectangle(hist_img, (x,0,2,int(h)), 0, cv2.FILLED)

    return cv2.flip(hist_img,0)



def make_palette(rows):
    hue = [round(i*180/rows) for i in range(rows)]
    hsv = [ [[h,255,255]] for h in hue ]
    hsv = np.array(hsv, np.uint8)

    return cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)


def draw_hist_hue(hist, shape=(200,256,3)):
    hsv_palette = make_palette(hist.shape[0])
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist,hist,0,shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1]/hist.shape[0]

    for i, h in enumerate(hist):
        x = int(round(i*gap))
        w = int(round(gap))
        cv2.rectangle(hist_img, (x,0,2,int(h)), 0, cv2.FILLED)

    return cv2.flip(hist_img,0)