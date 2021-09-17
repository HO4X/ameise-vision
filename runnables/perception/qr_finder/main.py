#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
import time 

from pyzbar import pyzbar

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from shapely.geometry import Polygon

# get video resolution in pixels
camera_res_height = 1200   
camera_res_width = 1920
camera_fov = 90  # camera FOV in degrees

IMAGE_TOPIC = "/pylon_camera_node/image_rect"

bridge = CvBridge()

def callback(data):
    start_time = time.time() # start time of the loop

    try:
      frame = bridge.imgmsg_to_cv2(data, 'bgr8')
    except CvBridgeError as e:
      print(e)
    
    print(frame.shape)
    print(frame[1000][1000][0])
    frame = np.array(frame, dtype = np.uint8 )

    qrcodes = pyzbar.decode(frame)
    
    # loop over the detected qr codes
    for qrcode in qrcodes:
        print("Found QR")
        # find qr code location and draw a box around it
        print(qrcode.polygon)
        (x1, y1), (x2, y2), (x3, y3), (x4, y4) = qrcode.polygon

        qr_polygon = Polygon(zip([x1, x2, x3, x4], [y1, y2, y3, y4]))

        qr_corner_array = np.array([(x1, y1), (x2, y2), (x3, y3), (x4, y4)])

        qr_size = qr_polygon.area

        # print(f'QR Code size: {qr_size} Pixels')

        # distance calculation

        camera_pixel_count = camera_res_width * camera_res_height

        calibration = 15  # TODO Calibration factor

        distance = round((camera_pixel_count / qr_size) / calibration, 2)

        print(f'Distance: {distance}m')

        # camera angle calculation

        [(x_center_qr, y_center_qr)] = qr_polygon.centroid.coords  # calc center coordinates of qr code polyon

        x_center_camera = camera_res_width / 2
        y_center_camera = camera_res_height / 2

        distance_qr_camera_center = ((((x_center_camera - x_center_qr )**2) + ((y_center_camera-y_center_qr)**2) )**0.5)

        camera_degrees_per_pixel = camera_fov / (np.sqrt(camera_res_width ** 2 + camera_res_height ** 2))

        print(camera_degrees_per_pixel)

        angle_camera_qr = round(distance_qr_camera_center * camera_degrees_per_pixel, 2)

        print(f'QR Code Angle: {angle_camera_qr}')

        # Draw Polygon lines around qr code
        polygonCornerpoints = qr_corner_array.reshape((-1, 1, 2))

        polygonColor = (128, 255, 0)  # green polygon lines
        polygonIsClosed = True  # connected polygon lines
        polygonThickness = 2  # thickness of polygon lines

        cv2.polylines(frame, [polygonCornerpoints], polygonIsClosed, polygonColor, polygonThickness)

        # decode qr code payload
        qrCodeData = qrcode.data.decode("utf-8")

        # show qr code data inside the videostream
        cvtextColor = (0, 0, 255)  # red font color
        cvFontSize = 0.6  # font size
        cvtextThickness = 2  # text thickness
        cvFontStyle = cv2.FONT_HERSHEY_SIMPLEX  # font style

        # show qr code payload
        payload = (f'Payload: {qrCodeData}')
        cv2.putText(frame, payload, (x1, y1 - 30),
                    cvFontStyle, cvFontSize, cvtextColor, cvtextThickness)

        # show qr code distance
        distance = (f'Distance: {distance}m / Angle: {angle_camera_qr}')
        cv2.putText(frame, distance, (x1, y1 - 10),
                    cvFontStyle, cvFontSize, cvtextColor, cvtextThickness)

        # if qrCodeData not in qrcodes_found:

        #     qrcodes_found.add(qrCodeData)
        #     # extract signID
        #     signID = getSignId(qrCodeData)

        #     if signID is not None:
        #         # get information from backend API
        #         signBackendInfo = requestSignData(signID)

        #         # print qr code info to console
        #         print("[QR CODE DETECTED] Payload: " + qrCodeData + " / BackendInfo: " + str(signBackendInfo))

        #         # track vehicle passed the sign
        #         postVehicleEvent(signID)

    cv2.imshow("Videostream QR Reader", frame)
    # cv2.imshow("Videostream QR Reader", np.array(frame, dtype = np.uint8 ))
    cv2.waitKey(1)

    print("FPS: ", 1.0 / (time.time() - start_time)) # FPS = 1 / time to process loop

    #rospy.loginfo(rospy.get_caller_id())

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=False)

    rospy.Subscriber(IMAGE_TOPIC, Image, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()