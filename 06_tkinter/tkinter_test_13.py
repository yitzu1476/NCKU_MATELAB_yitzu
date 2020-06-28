# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 18:44:44 2020

@author: joyce
"""

import tkinter as tk

class MainPage_c:
    def __init__(self, root):
        MainPage_inc = tk.Frame(root)
        MainPage_inc.pack()
        self.root = root
        
        self.Cam_b = tk.Button(MainPage_inc, text='Camera Image', command=self.opencam)
        self.AUVPilot_b = tk.Button(MainPage_inc, text='AUV Pilot', command=self.openpilot)
        self.Manual_b = tk.Button(MainPage_inc, text='Manual Execute', command=self.openman)
        self.q_button = tk.Button(MainPage_inc, text='Quit', command=root.destroy)
        
        self.Cam_b.grid(row=0, column=0)
        self.AUVPilot_b.grid(row=0, column=1)
        self.Manual_b.grid(row=0, column=2)
        self.q_button.grid(row=1, columnspan=3)
    
    def opencam(self):
        print('opencam')
    
    def openpilot(self):
        APpage = tk.Toplevel(self.root)
        self.config2 = AUVPilot_c(APpage)
    
    def openman(self):
        MEpage = tk.Toplevel(self.root)
        self.config2 = ManualExe_c(MEpage)

class AUVPilot_c(tk.Toplevel):
    def __init__(self, root):
        self.root = root
        self.ParaSet_lab = tk.Label(root, text='Parameter Setting')
        self.AreaSma_ent = 30000
        self.AreaBig_ent = 100000
        self.ContSma_ent = 300
        self.ContBig_ent = -100
        self.AngSide_ent = 10
        self.AngDri_ent = 10
        
        self.TarArea_lab = tk.Label(root, text='Target Area')
        self.AreaSma_lab = tk.Label(root, text='Area too small: ')
        self.AreaBig_lab = tk.Label(root, text='Area too big: ')
        self.AreaSma_ent = tk.Entry(root, width=5, bd=2)
        self.AreaBig_ent = tk.Entry(root, width=5, bd=2)
        
        self.ContRPM_lab = tk.Label(root, text='Control RPM')
        self.ContSma_lab = tk.Label(root, text='When too small: ')
        self.ContBig_lab = tk.Label(root, text='When too big: ')
        self.ContSma_ent = tk.Entry(root, width=5, bd=2)
        self.ContBig_ent = tk.Entry(root, width=5, bd=2)
        
        self.ContAng_lab = tk.Label(root, text='Control Angle')
        self.AngSide_lab = tk.Label(root, text='When too right: ')
        self.AngDri_lab = tk.Label(root, text='When too left: ')
        self.AngSide_ent = tk.Entry(root, width=5, bd=2)
        self.AngDri_ent = tk.Entry(root, width=5, bd=2)
        self.Anghigh_lab = tk.Label(root, text='When too high: ')
        self.Anglow_lab = tk.Label(root, text='When too low: ')
        self.Anghigh_ent = tk.Entry(root, width=5, bd=2)
        self.Anglow_ent = tk.Entry(root, width=5, bd=2)
        
        self.ParaSet_lab.grid(row=0, columnspan=8)
        
        self.TarArea_lab.grid(row=1, column=0, columnspan=2)
        self.AreaSma_lab.grid(row=2, column=0)
        self.AreaBig_lab.grid(row=3, column=0)
        self.AreaSma_ent.grid(row=2, column=1)
        self.AreaBig_ent.grid(row=3, column=1)
        
        self.ContRPM_lab.grid(row=4, column=0, columnspan=2)
        self.ContSma_lab.grid(row=5, column=0)
        self.ContBig_lab.grid(row=6, column=0)
        self.ContSma_ent.grid(row=5, column=1)
        self.ContBig_ent.grid(row=6, column=1)
        
        self.ContAng_lab.grid(row=1, column=3, columnspan=2)
        self.AngSide_lab.grid(row=2, column=3)
        self.AngDri_lab.grid(row=3, column=3)
        self.AngSide_ent.grid(row=2, column=4)
        self.AngDri_ent.grid(row=3, column=4)
        self.Anghigh_lab.grid(row=4, column=3)
        self.Anglow_lab.grid(row=5, column=3)
        self.Anghigh_ent.grid(row=4, column=4)
        self.Anglow_ent.grid(row=5, column=4)
        
        self.bord3 = tk.Canvas(root, width=5, bg='black')
        self.bord3.grid(row=1, column=2, rowspan=9)
        self.bord4 = tk.Canvas(root, width=5, bg='black')
        self.bord4.grid(row=1, column=5, rowspan=9)
        
        self.allCOM_lab = tk.Label(root, text='Device COM')
        self.allCOM_lab.grid(row=1, column=6, columnspan=2)
        
        self.SetThruster_lab = tk.Label(root, text='Thruster COM')
        self.SetThruster_ent = tk.Entry(root, width=5, bd=2)
        self.SetThruster_lab.grid(row=2, column=6)
        self.SetThruster_ent.grid(row=2, column=7)
        
        self.SetRudder_lab = tk.Label(root, text='Rudder COM')
        self.SetRudder_ent = tk.Entry(root, width=5, bd=2)
        self.SetRudder_lab.grid(row=3, column=6)
        self.SetRudder_ent.grid(row=3, column=7)
        
        self.SetINS_lab = tk.Label(root, text='INS COM')
        self.SetINS_ent = tk.Entry(root, width=5, bd=2)
        self.SetINS_lab.grid(row=4, column=6)
        self.SetINS_ent.grid(row=4, column=7)
        
        self.FPDOnly_but = tk.Button(root, text='FPD Only Mode', command=self.toFPDonly)
        self.FPDOnly_but.grid(row=6, column=6, columnspan=2)
        self.FPDnoCont_but = tk.Button(root, text='FPD No Control', command=self.toFPDnoCont)
        self.FPDnoCont_but.grid(row=7, column=6, columnspan=2)
        self.RedBall_but = tk.Button(root, text='Red Ball Mode', command=self.toRedBall)
        self.RedBall_but.grid(row=8, column=6, columnspan=2)
        
    def toFPDonly(self):
        print('toFPD')

    def toFPDnoCont(self):
        print('toFPD no control')

    def toRedBall(self):
        print('to red ball')

    def toMaskOnly(self):
        print('toMask')
    
    def toMaskFPD(self):
        print('toMask+FPD')

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
        self.INSCOM_lab = tk.Label(root, text='INS COM')
        self.ThrusterCOM_ent = tk.Entry(root, width=5, bd=2)
        self.RudderCOM_ent = tk.Entry(root, width=5, bd=2)
        self.INSCOM_ent = tk.Entry(root, width=5, bd=2)
        
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
        self.INSCOM_lab.grid(row=3, column=3)
        self.INSCOM_ent.grid(row=3, column=4)
    
    def ManControl(self):
        print('to all control')

MainPage = tk.Tk()
MainPage_call = MainPage_c(MainPage)
MainPage.mainloop()