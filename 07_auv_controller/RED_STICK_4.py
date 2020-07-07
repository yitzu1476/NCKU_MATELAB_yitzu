# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 09:40:35 2020

@author: joyce
"""

import os
import cv2
import clr
import time
import imutils
import numpy as np
import statistics
import Rudder_Controller
dll_AUV = clr.AddReference('UAVMotorLib')
import UAVMotorLib

Thruster = UAVMotorLib.Class_Thruster()
INS = UAVMotorLib.Class_INS()

kernel = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
edged = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

#undistort
mtx = np.array([[0,0,0],[0,0,0],[0,0,0]])
dist = np.array([[0.0,0.0,0.0,0.0,0.0]])

mtx[0][0] = 259
mtx[1][1] = 260
mtx[0][2] = 305
mtx[1][2] = 266
mtx[2][2] = 1
dist[0][0] = -0.448
dist[0][1] = 0.158
dist[0][2] = -0.03

def RED_STICK(TCOM, RCOM, ICOM):
    ThrusterCOM = 'COM'+str(TCOM)
    Thruster.OpenPort(ThrusterCOM, '9600')
    
    INSCOM = 'COM'+str(ICOM)
    INS.OpenPort(INSCOM, '115200')
    
    Rudder = Rudder_Controller.RudderController(RCOM)
    
    # create folder
    cwd = str(os.getcwd())
    cwdt = time.time()
    root_name = cwd + '/all_result/video' + str(cwdt) + '_RB_STICK'
    os.makedirs(root_name)
    root_name = cwd + '/all_result/video' + str(cwdt) + '_RB_STICK/cam1'
    os.makedirs(root_name)
    root_name = cwd + '/all_result/video' + str(cwdt) + '_RB_STICK/cam2'
    os.makedirs(root_name)
    
    #paras
    area_red = 100
    x_ps_red = 160
    y_ps_red = 120
    start_time = time.time()
    frame_1 = False
    direct = 'front'
    heading = 'front'
    F2B_cnt = 0
    B2F_cnt = 0
    
    #record
    RBxscnt = []
    RByscnt = []
    RBx_R = []
    RBy_R = []
    ins_1 = []
    ins_2 = []
    ins_3 = []
    ins_4 = []
    ins_5 = []
    ins_6 = []
    ins_7 = []
    ins_8 = []
    ins_9 = []
    RBascnt = []
    sscnt = []
    
    cap = cv2.VideoCapture(1) #two eyes
    cap2 = cv2.VideoCapture(0) #wide
    img_cnt = 0
    while True:
        ret, frame = cap.read()
        ret2, frame2 = cap2.read()
        if ret:
            this_time = time.time()
            img_cnt = img_cnt + 1
            
            # save image
            timetxt = str(time.ctime(this_time))
            
            save_root = cwd + '/all_result/video' + str(cwdt) + '_RB_STICK' + '/cam1/img' + str(img_cnt) + '.jpg'
            #aframe = cv2.putText(frame, timetxt, (10,10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1, cv2.LINE_AA)
            aframe = frame
            cv2.imwrite(save_root, aframe)
            
            save_root = cwd + '/all_result/video' + str(cwdt) + '_RB_STICK' + '/cam2/img' + str(img_cnt) + '.jpg'
            aframe2 = cv2.putText(frame2, timetxt, (10,10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1, cv2.LINE_AA)
            cv2.imwrite(save_root, aframe2)
            
            cv2.imshow('ori', frame)
        
            '''For Red Bucket'''
            # cover
            frame = cv2.rectangle(frame, (320, 0), (640, 240), (255, 255, 255), -1)
                    
            # kernel
            frame = cv2.filter2D(frame,-1,kernel)
            
            # color detection
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower = np.array([0.0,16.0,30.0])
            upper = np.array([45.0,180.0,150.0])
            red_mask = cv2.inRange(hsv, lower, upper)
            
            tocont = False
            contours = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)
            for contour in contours:
                ara = cv2.contourArea(contour)
                if ara > 20:
                    print(ara)
                    tocont = True
                    area_red = ara
                    x, y, w, h = cv2.boundingRect(contour)
                    frame_1 = True
                    aft_frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 5)
                    x_ps_red = x+(w/2)
                    y_ps_red = y+(h/2)
                    
            '''Controller'''
            # Depth control
            
            #Thruster control
            # Red Y position logic: y=(25/6)x-500
            back = False
            print('y ',y_ps_red)
            if float(this_time-start_time) >= 15:
                RBy = len(RByscnt)
                if RBy != 0:
                    mean_RBy = statistics.mean(RByscnt[RBy-100:])
                    thruster_pos = statistics.mean([mean_RBy,y_ps_red])
                    if thruster_pos > 180:
                        thruster_to_control = 450
                    if thruster_pos > 140 and thruster_pos <= 180:
                        thruster_to_control = 400
                    if thruster_pos > 100 and thruster_pos <= 140:
                        thruster_to_control = 250
                    if thruster_pos > 60 and thruster_pos <= 100:
                        thruster_to_control = 0
                        back = True
                    if thruster_pos <= 60:
                        back = True
                        thruster_to_control = -200
                    #thruster_to_control = (thruster_pos*(25/6))-500
                    Thruster.SpeedUp(int(thruster_to_control), 10)
            else:
                if tocont == True:
                    if y_ps_red > 180:
                        thruster_to_control = 200
                    if y_ps_red > 140 and y_ps_red <= 180:
                        thruster_to_control = 100
                    if y_ps_red > 100 and y_ps_red <= 140:
                        thruster_to_control = 0
                    if y_ps_red > 60 and y_ps_red <= 100:
                        thruster_to_control = -200
                        back = True
                    if y_ps_red <= 60:
                        back = True
                        thruster_to_control = -100
                    #thruster_to_control = (y_ps_red*(25/6))-500
                    Thruster.SpeedUp(int(thruster_to_control), 10)
            
            if tocont == True:
                print('thrust ',thruster_to_control)
            
            # Rudeer control            
            # Red X position logic: y=(25/8)x+1000 or y=-(25/8)x+2000
            red_rudder = (x_ps_red*(25/8))+1000
            
            #rudder_to_control = stick_rudder*0.2 + red_rudder*0.8
            rudder_to_control = red_rudder
            rudder_1 = 3000-int(rudder_to_control)
            
            if F2B_cnt > 0 and F2B_cnt < 10:
                F2B_cnt = F2B_cnt + 1
                Rudder.SetTarget(1, int(rudder_to_control))
                Rudder.SetTarget(0, int(rudder_1))
                heading = 'back'
            
            elif B2F_cnt > 0 and B2F_cnt < 10:
                B2F_cnt = B2F_cnt + 1
                Rudder.SetTarget(0, int(rudder_to_control))
                Rudder.SetTarget(1, int(rudder_1))
                heading = 'front'
            
            elif F2B_cnt == 10:
                F2B_cnt = 0
                Rudder.SetTarget(1, int(rudder_to_control))
                Rudder.SetTarget(0, int(rudder_1))
                heading = 'back'
            
            elif B2F_cnt == 10:
                B2F_cnt = 0
                Rudder.SetTarget(0, int(rudder_to_control))
                Rudder.SetTarget(1, int(rudder_1))
                heading = 'front'
            
            else:
                if heading == 'front' and back == True:
                    direct = 'F2B'
                if heading == 'back' and back == False:
                    direct = 'B2F'
                if heading == 'front' and back == False:
                    direct = 'F'
                if heading == 'back' and back == True:
                    direct = 'B'
                
                if direct == 'B':
                    Rudder.SetTarget(0, int(rudder_to_control))
                    Rudder.SetTarget(1, int(rudder_1))
                    heading = 'back'
                if direct == 'F':
                    Rudder.SetTarget(1, int(rudder_to_control))
                    Rudder.SetTarget(0, int(rudder_1))
                    heading = 'front'
                    
                if direct == 'F2B':
                    F2B_cnt = F2B_cnt + 1
                    Rudder.SetTarget(1, int(rudder_to_control))
                    Rudder.SetTarget(0, int(rudder_1))
                if direct == 'B2F':
                    B2F_cnt = B2F_cnt + 1
                    Rudder.SetTarget(0, int(rudder_to_control))
                    Rudder.SetTarget(1, int(rudder_1))
            print('rudder ',rudder_to_control)
            
            if tocont == True:
                RBxscnt.append(x_ps_red)
                RByscnt.append(y_ps_red)
                RBx_R.append(x_ps_red)
                RBy_R.append(y_ps_red)
            else:
                RBx_R.append('x')
                RBy_R.append('x')
            
            # Record
            INS.StartLog()
            ins_record_1 = str(INS.GetDeltaAngAndVelocity())+'\t'+str(INS.GetAccelAndAngRate())+'\t'+str(INS.GetEulerAngles())+'\t'+str(INS.DeltaAng_VelRecordtimer)
            ins_record_2 = str(INS.Roll_Ang)+'\t'+str(INS.Pitch_Ang)+'\t'+str(INS.Yaw_Ang)+'\t'+str(INS.Roll_Pitch_YawRecordtimer)
            ins_record_3 = str(INS.Roll_Deg)+'\t'+str(INS.Pitch_Deg)+'\t'+str(INS.Yaw_Deg)
            ins_record_4 = str(INS.DeltaVel[0])+'\t'+str(INS.DeltaVel[1])+'\t'+str(INS.DeltaVel[2])
            ins_record_5 = str(INS.DeltaAng[0])+'\t'+str(INS.DeltaAng[1])+'\t'+str(INS.DeltaAng[2])
            ins_record_6 = str(INS.Raw_Accel[0])+'\t'+str(INS.Raw_Accel[1])+'\t'+str(INS.Raw_Accel[2])
            ins_record_7 = str(INS.Raw_AngRt[0])+'\t'+str(INS.Raw_AngRt[1])+'\t'+str(INS.Raw_AngRt[2])
            ins_record_8 = str(INS.Accel_AngRecord_Accel[0])+'\t'+str(INS.Accel_AngRecord_Accel[1])+'\t'+str(INS.Accel_AngRecord_Accel[2])
            ins_record_9 = str(INS.Accel_AngRecord_AngRt[0])+'\t'+str(INS.Accel_AngRecord_AngRt[1])+'\t'+str(INS.Accel_AngRecord_AngRt[2])
            
            ins_1.append(ins_record_1)
            ins_2.append(ins_record_2)
            ins_3.append(ins_record_3)
            ins_4.append(ins_record_4)
            ins_5.append(ins_record_5)
            ins_6.append(ins_record_6)
            ins_7.append(ins_record_7)
            ins_8.append(ins_record_8)
            ins_9.append(ins_record_9)
            sscnt.append(this_time)
            
            if tocont == True:
                RBascnt.append(area_red)
            else:
                RBascnt.append('x')
            
            # show after frame
            x_text = 'X position: ' + str(x_ps_red)
            y_text = 'Y position: ' + str(y_ps_red)
            a_text = 'Area: ' + str(area_red)
            
            if frame_1 == False:
                continue
            
            aft_frame = cv2.putText(aft_frame, x_text, (100,50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1, cv2.LINE_AA)
            aft_frame = cv2.putText(aft_frame, y_text, (100,100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1, cv2.LINE_AA)
            aft_frame = cv2.putText(aft_frame, a_text, (100,200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1, cv2.LINE_AA)
            cv2.imshow('two eyes', aft_frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cap2.release()
    cv2.destroyAllWindows()
    Thruster.Stop(True)
    Thruster.ClosePort()
    Rudder.SetTarget(0, 1500)
    Rudder.SetTarget(1, 1500)
    Rudder.SetTarget(2, 1500)
    Rudder.SetTarget(3, 1500)
    Rudder.ClosePort()
    INS.Close()
    
    root_name = cwd + '/all_result/video' + str(cwdt) + '_RB_STICK'
    
    x_file = root_name + '/RBx_file.txt'
    with open(x_file, 'w') as fx:
        for item in range(len(RBx_R)):
            fx.write(str(RBx_R[item]))
            fx.write('\n')
    fx.close()
    
    y_file = root_name + '/RBy_file.txt'
    with open(y_file, 'w') as fy:
        for item in range(len(RBy_R)):
            fy.write(str(RBy_R[item]))
            fy.write('\n')
    fy.close()
    
    area_file = root_name + '/RBarea_file.txt'
    with open(area_file, 'w') as fa:
        for item in range(len(RBascnt)):
            fa.write(str(RBascnt[item]))
            fa.write('\n')
    fa.close()
    
    time_file = root_name + '/time_file.txt'
    with open(time_file, 'w') as ft:
        for item in range(len(sscnt)):
            ft.write(str(sscnt[item]))
            ft.write('\n')
    ft.close()
    
    ins1_file = root_name + '/ins1_file.txt'
    with open(ins1_file, 'w') as fins1:
        for item in range(len(ins_1)):
            fins1.write(str(ins_1[item]))
            fins1.write('\n')
    fins1.close()
    
    ins2_file = root_name + '/ins2_file.txt'
    with open(ins2_file, 'w') as fins2:
        for item in range(len(ins_2)):
            fins2.write(str(ins_2[item]))
            fins2.write('\n')
    fins2.close()
    
    ins3_file = root_name + '/ins3_file.txt'
    with open(ins3_file, 'w') as fins3:
        for item in range(len(ins_3)):
            fins3.write(str(ins_3[item]))
            fins3.write('\n')
    fins3.close()
    
    ins4_file = root_name + '/ins4_file.txt'
    with open(ins4_file, 'w') as fins4:
        for item in range(len(ins_4)):
            fins4.write(str(ins_4[item]))
            fins4.write('\n')
    fins4.close()
    
    ins5_file = root_name + '/ins5_file.txt'
    with open(ins5_file, 'w') as fins5:
        for item in range(len(ins_5)):
            fins5.write(str(ins_5[item]))
            fins5.write('\n')
    fins5.close()
    
    ins6_file = root_name + '/ins6_file.txt'
    with open(ins6_file, 'w') as fins6:
        for item in range(len(ins_6)):
            fins6.write(str(ins_6[item]))
            fins6.write('\n')
    fins6.close()
    
    ins7_file = root_name + '/ins7_file.txt'
    with open(ins7_file, 'w') as fins7:
        for item in range(len(ins_7)):
            fins7.write(str(ins_7[item]))
            fins7.write('\n')
    fins7.close()
    
    ins8_file = root_name + '/ins8_file.txt'
    with open(ins8_file, 'w') as fins8:
        for item in range(len(ins_8)):
            fins8.write(str(ins_8[item]))
            fins8.write('\n')
    fins8.close()
    
    ins9_file = root_name + '/ins9_file.txt'
    with open(ins9_file, 'w') as fins9:
        for item in range(len(ins_9)):
            fins9.write(str(ins_9[item]))
            fins9.write('\n')
    fins9.close()

    
    
    
    
    