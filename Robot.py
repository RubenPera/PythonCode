import cv2
import sys
import os
from Enums import *
from Engines import *
from Sensors import *
from Sign import *
import threading
import time
import numpy

class Robot:
    def __init__(self, name, error):
        self.name = name
        self.error = error
        self.ELeft = Engine(1)
        self.ERight = Engine(0)
        self.Camera = Camera(0)
        self.Degree = Degree(1)
        self.images = []
        self.images.append(Sign(PriorityEnum.MoBa, "images/move_backward.png"))
        self.images.append(Sign(PriorityEnum.MoFo, "images/move_forward.png"))
        self.images.append(Sign(PriorityEnum.StLe, "images/Steer_left.png"))
        self.images.append(Sign(PriorityEnum.StRi, "images/Steer_right.png"))
        self.images.append(Sign(PriorityEnum.TuLe, "images/turn_left.png"))
        self.images.append(Sign(PriorityEnum.TuRi, "images/turn_right.png"))
        #img = cv2.imread(self.images[0].url)
        self.Analyse("images/check.png")
        # self.Move(EngineDirection.Forward, EngineDirection.Backward, EngineIntensity.Speed1, EngineIntensity.Speed2)

    def run(self, test, test2):
        time.sleep(2)
        print("test " + test + test2)

    def start(self):
        var = self.Camera.get()
        self.ELeft.Move(EngineDirection.Forward, EngineIntensity.Speed9)
        self.ERight.Move(EngineDirection.Forward, EngineIntensity.Speed9)

        t=threading.Thread(target=self.run, args=('bob','bob2',))
        #t.daemon = False  # set thread to daemon ('ok' won't be printed in this case)
        i = 0
        t.start()
        while(i < 6):
            time.sleep(1)
            print("This is main")
            i += 1
        self.Stop()
        return







        #alle code die uitgevoert moet gaan worden

    def Move(self, DLeft, DRight, ILeft, IRight):
        self.ELeft.Move(DLeft, ILeft)
        self.ERight.Move(DRight, IRight)
        return

    def Stop(self):
        self.ELeft.Stop()
        self.ERight.Stop()

    def Execute(self, i):
        if(i is SignID.Stop.value):
            print("STOPPING")

    def Analyse(self, camimg):
        retlist = []
        for item in self.images:
            img = cv2.imread(camimg)
            template = cv2.imread(item.url)
            result = numpy.array([0])
            result = cv2.matchTemplate(img, template, eval('cv2.TM_CCOEFF_NORMED'))
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            print("minval: " + str(min_val) + "; maxval :" + str(max_val) + "; minloc: "+ str(min_loc) + "; maxloc: " + str(max_loc))
            if(str(max_loc) != "(0, 0)" and str(min_loc) != "(0, 0)"):
                retlist.append(item.SignID)
