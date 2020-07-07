# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 09:36:21 2020

@author: joyce
"""

import tkinter as tk
import cv2
import AllController_2
import RED_STICK_3
import yaw_detection

class MainPage_c:
    def __init__(self, root):
        MainPage_inc = tk.Frame(root)
        MainPage_inc.pack()
        self.root = root
        
        self.Cam_w = tk.Button(MainPage_inc, text='Wide Camera', command=self.opencam_w)
        self.Cam_t = tk.Button(MainPage_inc, text='Two eyes Camera', command=self.opencam_t)
        self.AUVPilot_b = tk.Button(MainPage_inc, text='AUV Pilot', command=self.openpilot)
        self.Manual_b = tk.Button(MainPage_inc, text='Manual Execute', command=self.openman)
        self.q_button = tk.Button(MainPage_inc, text='Quit', command=root.destroy)
        
        self.Cam_w.grid(row=0, column=0)
        self.Cam_t.grid(row=0, column=1)
        self.AUVPilot_b.grid(row=0, column=2)
        self.Manual_b.grid(row=0, column=3)
        self.q_button.grid(row=1, columnspan=4)
        
    def opencam_w(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('img',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        print(frame.shape)
        
    def opencam_t(self):
        cap = cv2.VideoCapture(1)
        while True:
            ret, frame = cap.read()
            cv2.imshow('img',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        print(frame.shape)
        
    def openpilot(self):
        APpage = tk.Toplevel(self.root)
        self.config2 = AUVPilot_c(APpage)
    
    def openman(self):
        MEpage = tk.Toplevel(self.root)
        self.config2 = ManualExe_c(MEpage)

class AUVPilot_c(tk.Toplevel):
    def __init__(self, root):
        self.root = root
        
        self.allCOM_lab = tk.Label(root, text='Device COM')
        self.allCOM_lab.grid(row=0, column=0, columnspan=4)
        
        self.SetThruster_lab = tk.Label(root, text='Thruster COM')
        self.SetThruster_ent = tk.Entry(root, width=5, bd=2)
        self.SetThruster_lab.grid(row=1, column=0)
        self.SetThruster_ent.grid(row=1, column=1)
        
        self.SetRudder_lab = tk.Label(root, text='Rudder COM')
        self.SetRudder_ent = tk.Entry(root, width=5, bd=2)
        self.SetRudder_lab.grid(row=2, column=0)
        self.SetRudder_ent.grid(row=2, column=1)
        
        self.SetINS_lab = tk.Label(root, text='INS COM')
        self.SetINS_ent = tk.Entry(root, width=5, bd=2)
        self.SetINS_lab.grid(row=3, column=0)
        self.SetINS_ent.grid(row=3, column=1)
        
        self.RedStick_but = tk.Button(root, text='Red + Stick', command=self.toRedStick)
        self.RedStick_but.grid(row=1, column=2, columnspan=2)
        self.yaw_but = tk.Button(root, text='Yaw Detection', command=self.toyaw)
        self.yaw_but.grid(row=2, column=2, columnspan=2)
    
    def toRedStick(self):
        print('to Red Stick')
        RED_STICK_3.RED_STICK(self.SetThruster_ent.get(), self.SetRudder_ent.get(), self.SetINS_ent.get())
    
    def toyaw(self):
        print('toyaw')
        yaw_detection.Yaw_Detection(self.SetThruster_ent.get(), self.SetRudder_ent.get(), self.SetINS_ent.get())
        
class ManualExe_c(tk.Toplevel):
    def __init__(self, root):
        self.root = root
        
        self.ManExe_lab = tk.Label(root, text='Manual Execute')
        self.ThrustRPM_lab = tk.Label(root, text='Thruster RPM: ')
        self.ThrustTime_lab = tk.Label(root, text='Thruster Time: ')
        self.ThrustRPM_ent = tk.Entry(root, width=5, bd=2)
        self.ThrustTime_ent = tk.Entry(root, width=5, bd=2)
        self.RudAngx_lab = tk.Label(root, text='Rudder X Angle: ')
        self.RudAngx_ent = tk.Entry(root, width=5, bd=2)
        self.RudAngy_lab = tk.Label(root, text='Rudder Y Angle: ')
        self.RudAngy_ent = tk.Entry(root, width=5, bd=2)
        self.Go_but = tk.Button(root, text='Go', command=self.ManControl)
        
        self.ThrusterCOM_lab = tk.Label(root, text='Thruster COM')
        self.RudderCOM_lab = tk.Label(root, text='Rudder COM')
        self.ThrusterCOM_ent = tk.Entry(root, width=5, bd=2)
        self.RudderCOM_ent = tk.Entry(root, width=5, bd=2)
        
        self.ManExe_lab.grid(row=0, column=0, columnspan=4)
        self.ThrustRPM_lab.grid(row=1, column=1)
        self.ThrustTime_lab.grid(row=2, column=1)
        self.ThrustRPM_ent.grid(row=1, column=2)
        self.ThrustTime_ent.grid(row=2, column=2)
        self.RudAngx_lab.grid(row=3, column=1)
        self.RudAngx_ent.grid(row=3, column=2)
        self.RudAngy_lab.grid(row=4, column=1)
        self.RudAngy_ent.grid(row=4, column=2)
        self.Go_but.grid(row=5, column=1, columnspan=4)
        
        self.ThrusterCOM_lab.grid(row=1, column=3)
        self.ThrusterCOM_ent.grid(row=1, column=4)
        self.RudderCOM_lab.grid(row=2, column=3)
        self.RudderCOM_ent.grid(row=2, column=4)
    
    def ManControl(self):
        print('to all control')
        AllController_2.AllControl(self.ThrustRPM_ent.get(), self.ThrustTime_ent.get(),
                                 self.RudAngx_ent.get(), self.RudAngy_ent.get(),
                                 self.ThrusterCOM_ent.get(), self.RudderCOM_ent.get())

        
MainPage = tk.Tk()
MainPage_call = MainPage_c(MainPage)
MainPage.mainloop()
        