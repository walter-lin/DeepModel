import os
import cv2
import numpy as np

img_size = 32

def load_data():
    x_train = []
    y_train = []
        
    filenames = os.listdir("./trainImg/0")
    for fname in filenames:
        img = cv2.imread("./trainImg/0/" + fname, cv2.IMREAD_COLOR)
        img = cv2.resize(img,(img_size,img_size))
        x_train.append(img)
        y_train.append(0)        

    filenames = os.listdir("./trainImg/1")
    for fname in filenames:
        img = cv2.imread("./trainImg/1/" + fname, cv2.IMREAD_COLOR)
        img = cv2.resize(img,(img_size,img_size))
        x_train.append(img)
        y_train.append(1)  

    x_train = np.array(x_train, dtype=np.float32)
    y_train = np.array(y_train)

    x_test = []
    y_test = []
        
    filenames = os.listdir("./testImg/0")
    for fname in filenames:
        img = cv2.imread("./testImg/0/" + fname, cv2.IMREAD_COLOR)
        img = cv2.resize(img,(img_size,img_size))
        x_test.append(img)
        y_test.append(0)        

    filenames = os.listdir("./testImg/1")
    for fname in filenames:
        img = cv2.imread("./testImg/1/" + fname, cv2.IMREAD_COLOR)
        img = cv2.resize(img,(img_size,img_size))
        x_test.append(img)
        y_test.append(1)  

    x_test = np.array(x_test, dtype=np.float32)
    y_test = np.array(y_test)
    
    return (x_train,y_train), (x_test,y_test)
