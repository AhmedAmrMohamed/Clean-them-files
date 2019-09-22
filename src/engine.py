from docdis import Docdis
from heap import Heap
import os
import math

class Engine:
    def __init__(s,src,*,dst=None,degree = 0.7):
        s.distance = Docdis()
        s.src = src
        s.deg = max(min(math.pi/2,degree),0)
        s.done  = s.core()

    def core(s):
        done = set()
        for trgt in os.listdir(s.src):
           add = True
           for comp in done:
               dis = s.distance(trgt,comp)
               if dis < s.deg:
                   add = False
                   break
           if add:
               done.add(trgt)
        return done

                

