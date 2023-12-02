import numpy as np
import base64
import cv2

from deepface import DeepFace


def loadBase64Img(image_b64):
    nparr = np.fromstring(base64.b64decode(image_b64), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


def verify(img1, img2):
    img1 = loadBase64Img(img1)
    img2 = loadBase64Img(img2)
    obj = DeepFace.verify(
        img1_path=img1,
        img2_path=img2,
    )
    return obj
