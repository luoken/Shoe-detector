'''
1. This program demonstrates some image/video preprocessing for object detection using opencv:
* # color filtering
* # convert to grayscale
* # use thresholds
* # find contours
* # draw boxes around objects

2. Outputs to a video file too
* # Output is created in current directory

Usage:
  detection.py [path/to/video.avi]
'''

import cv2
import numpy as np
import pandas as pd
import sys
import glob

# **************************** USEFUL METHODS ********************* #

def resize(frame, scale): # resize image to scale value param
    return cv2.resize(frame, (int(frame.shape[1] * scale), int(frame.shape[0] * scale) ))


def scaled(frame, scale): # returns new scale value
    frame_shape_x, frame_shape_y, channels = frame.shape
    if(frame_shape_x > scale):
        return scale / frame_shape_x
    else:
        return 1
    

def color_filter(frame, lower_upper_list):
    lower = np.array(lower_upper_list[0], dtype="uint8")
    upper = np.array(lower_upper_list[1], dtype="uint8")

    mask = cv2.inRange(frame, lower, upper)
    output = cv2.bitwise_and(frame, frame, mask = mask)

    return output, mask


def create_all_boxes(frame_contours_list):
    box_list = []
    for contour in frame_contours_list:
        cv2.boudingRect(contour)
        box_list.append(contour)
    return box_list


def filter_boxes(frame_rectangle_list, filter_size=0):
    filtered_boxes = []
    for rectangle in frame_rectangle_list:
        if(rectangle[2] * rectangle[3] > filter_size):
            filtered_boxes.append(rectangle)
    return filtered_boxes


def draw_rectangles(frame, frame_rectangle_list, x_offset=0, y_offset=0):
    for x, y, w, h in frame_rectangle_list:
        cv2.rectangle(
            frame,
            (x - x_offset, y - y_offset),
            ((x + x_offset) + w, (y + y_offset) + h),
            (0, 255, 0),
            2
        )


# ****************************** /END METHODS/ ******************** #

# ***************************************************************** #

if __name__ == '__main__':

    print(__doc__)

    try:
        video_path = sys.argv[1] # path to video file
    except:
        print("Using default video path since NO arg to was provided..")
        print(" ## videos/video_test.avi\n")
        video_path = "videos/video_test.avi" # default

    file_name = "./run_.avi" # name of file it will create
    video = cv2.VideoCapture(video_path) # video object

    ## preprocess params
    lower_blue = np.array([0, 50, 50]) # color filter params
    upper_blue = np.array([130, 250, 255]) # color filter params
    threshold_color = [0, 255, 0] # green
    box_filter_size = 400
        
    ## for outputting video
    fps = 30.0 # change this to run at a slower speed
    fourcc  = cv2.VideoWriter_fourcc(*"M", "J", "P", "G") # create write object for mac
    video_res = (640, 480) # has to be frame size of video/img
    out = cv2.VideoWriter(file_name, fourcc, fps, video_res ) # define writer object

    # loop runs until entire video is read or press q
    while(video.isOpened() ):
        
        ret, frame = video.read() # frame is the 'image'
        
        if(ret):
            ''' ------------------- PREPROCESS START ------------------- '''
            video_frame, mask = color_filter(frame, [lower_blue, upper_blue]) # color preprocess

            video_frame_gray = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY) # convert to gray
            
            ret, frame_thresh = cv2.threshold(video_frame_gray, 127, 255, cv2.THRESH_TOZERO) # perform thresholding

            frame_c, frame_contours, frame_heirarchy = cv2.findContours(frame_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # calculate contours
            
            frame_copy = frame.copy() # so you don't write over the 'image'
            
            cv2.drawContours(frame_copy, frame_contours, -1, threshold_color, 3) # to see what the contours look like; -1 means draw all contours
            ''' ------------------- /PREPROCESS END ------------------- '''
            
            # utilities
            frame_all_boxes = [cv2.boundingRect(c) for c in frame_contours] # draw boxes around boxes
            frame_filtered_boxes = filter_boxes(frame_all_boxes, box_filter_size) # filter boxes based on filter size
            draw_rectangles(frame, frame_filtered_boxes, 5, 5) # last 2 params are offset - self explanatory?

            out.write(frame) # write to file

            ''' ------------------- VIEW MULTIPLE TEST SCREENS ------------------- '''
            cv2.imshow("original", frame) # view actual frame
            cv2.moveWindow("original", 0, 0) # last 2 params are x, y coords of screen
            
            cv2.imshow("thresholding", frame_thresh) # threshold frame
            cv2.moveWindow("thresholding", 640, 0)

            cv2.imshow("contours", frame_copy)
            cv2.moveWindow("contours", 0, 520)

            cv2.imshow("grayscale", video_frame_gray) # grayscale frame
            cv2.moveWindow("grayscale", 640, 520)
            ''' -------------------------- /VIEW END ----------------------------- '''

            if(cv2.waitKey(1) & 0xFF == ord("q") ):
                break
        else:
            break

    out.release()
    video.release()
    cv2.destroyAllWindows()
