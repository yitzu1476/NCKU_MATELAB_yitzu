# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:06:21 2020

@author: USER
"""

import os
import cv2
import clr
import time
import numpy as np
import Rudder_Controller
dll_AUV = clr.AddReference('UAVMotorLib')
import UAVMotorLib

Thruster = UAVMotorLib.Class_Thruster()
INS = UAVMotorLib.Class_INS()

kernel = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])

def standard_range(value):
    if value >= 0:
        n_value = value
    else:
        n_value = value + 360
    return n_value

def target_range(value, error):
    if error >= 0:
        if value >= abs(error):
            n_value = value + error + 360
        if value < abs(error):
            n_value = value + error
    if error < 0:
        if (360-value) >= abs(error):
            n_value = value + error
        if (360-value) < abs(error):
            n_value = abs(value + error - 360)
    return n_value

def Yaw_Detection(TCOM, RCOM, ICOM):
    ThrusterCOM = 'COM'+str(TCOM)
    Thruster.OpenPort(ThrusterCOM, '9600')
    
    INSCOM = 'COM'+str(ICOM)
    INS.OpenPort(INSCOM, '115200')
    INS.StartLog()
    
    Rudder = Rudder_Controller.RudderController(RCOM)
    
    # create folder
    cwd = str(os.getcwd())
    cwdt = time.time()
    root_name = cwd + '/all_result/video' + str(cwdt) + '_Yaw'
    os.makedirs(root_name)
    root_name = cwd + '/all_result/video' + str(cwdt) + '_Yaw/cam1'
    os.makedirs(root_name)
    root_name = cwd + '/all_result/video' + str(cwdt) + '_Yaw/cam2'
    os.makedirs(root_name)
    
    #record
    yaw_deg = []
    yaw_standard = []
    yaw_targeterror = []
    ins_1 = []
    ins_2 = []
    ins_3 = []
    ins_4 = []
    ins_5 = []
    ins_6 = []
    ins_7 = []
    ins_8 = []
    ins_9 = []
    
    # target yaw
    error = 180-12
    
    start_time = time.time()
    ttime = 0
    
    cap = cv2.VideoCapture(0) #two eyes
    cap2 = cv2.VideoCapture(1) #wide
    img_cnt = 0
    while (ttime < 70):
        ret, frame = cap.read()
        ret2, frame2 = cap2.read()
        if ret:
            this_time = time.time()
            img_cnt = img_cnt + 1
            ttime = this_time - start_time
            print('time ', ttime)
            
            # save image
            timetxt = str(time.ctime(this_time))
            
            save_root = cwd + '/all_result/video' + str(cwdt) + '_Yaw' + '/cam1/img' + str(img_cnt) + '.jpg'
            aframe = cv2.putText(frame, timetxt, (10,10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1, cv2.LINE_AA)
            cv2.imwrite(save_root, aframe)
            
            save_root = cwd + '/all_result/video' + str(cwdt) + '_Yaw' + '/cam2/img' + str(img_cnt) + '.jpg'
            aframe2 = cv2.putText(frame2, timetxt, (10,10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1, cv2.LINE_AA)
            cv2.imwrite(save_root, aframe2)
            
            Thruster.SpeedUp(300, 10)
            
            INS.StartLog()
            yaw_stand = standard_range(INS.Yaw_Deg)
            yaw_target = target_range(yaw_stand, error)
            
            if yaw_target > 225:
                Rudder.SetTarget(1, 2000)
                Rudder.SetTarget(0, 1000)
            if yaw_target <= 255 and yaw_target > 205:
                Rudder.SetTarget(1, 1800)
                Rudder.SetTarget(0, 1200)
            if yaw_target <= 205 and yaw_target > 185:
                Rudder.SetTarget(1, 1650)
                Rudder.SetTarget(0, 1350)
            if yaw_target <= 185 and yaw_target > 175:
                Rudder.SetTarget(1, 1500)
                Rudder.SetTarget(0, 1500)
            if yaw_target <= 175 and yaw_target > 155:
                Rudder.SetTarget(1, 1350)
                Rudder.SetTarget(0, 1650)
            if yaw_target <= 155 and yaw_target > 135:
                Rudder.SetTarget(1, 1200)
                Rudder.SetTarget(0, 1800)
            if yaw_target <= 135:
                Rudder.SetTarget(1, 1000)
                Rudder.SetTarget(0, 2000)
            
            yaw_deg.append(INS.Yaw_Deg)
            yaw_standard.append(yaw_stand)
            yaw_targeterror.append(yaw_target)
            print('deg: ',INS.Yaw_Deg)
            print('sta: ', yaw_stand)
            print('tar: ', yaw_target)
            
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
            
            cv2.imshow('two eyes', aframe)
            
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
    
    root_name = cwd + '/all_result/video' + str(cwdt) + '_Yaw'
    
    yaw_deg_file = root_name + '/yaw_deg_file.txt'
    with open(yaw_deg_file, 'w') as yawD:
        for item in range(len(yaw_deg)):
            yawD.write(str(yaw_deg[item]))
            yawD.write('\n')
    yawD.close()
    
    yaw_sta_file = root_name + '/yaw_sta_file.txt'
    with open(yaw_sta_file, 'w') as yawS:
        for item in range(len(yaw_standard)):
            yawS.write(str(yaw_standard[item]))
            yawS.write('\n')
    yawS.close()
    
    yaw_tar_file = root_name + '/yaw_tar_file.txt'
    with open(yaw_tar_file, 'w') as yawT:
        for item in range(len(yaw_targeterror)):
            yawT.write(str(yaw_targeterror[item]))
            yawT.write('\n')
    yawT.close()
    
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
    
    
    