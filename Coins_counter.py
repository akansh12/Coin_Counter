import argparse
import cv2
import numpy as np


# Fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# Loading and converting the image into numpy array
# Printing the corresponding values
image = cv2.imread(args["image"])


# Showing the Original Image
cv2.imshow('Original',image)
cv2.waitKey(0)

# Convert image to gray scale
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",gray)
cv2.waitKey(0)
#Bluring the image
blured=cv2.GaussianBlur(gray,(13,13),0)
cv2.imshow("Gaussian blurred",blured)
cv2.waitKey(0)

#Performing Canny edge Detection
canny=cv2.Canny(blured,30,150)
cv2.imshow("canny_edge_detection",canny)
cv2.waitKey(0)

#Counting the contours
(_,cnts,_)=cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print('No. of coins in the image are:{}'.format(len(cnts)))

#Drawing the contours with green color

coins=image.copy()
cv2.drawContours(coins,cnts,-1,(0,255,0),2)
cv2.imshow('contours',coins)
cv2.waitKey(0)

