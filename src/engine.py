from docdis import Docdis
import os
import shutil
import math

class Engine:
    def __init__(s,src,*,dst=None,degree = 0.7):
        s.distance = Docdis()
        s.src = src
        s.dst = dst
        s.deg = max(min(math.pi/2,degree),0)
        s.done  = s.core()
        s.copier()

    def core(s):
        '''
        return a set of the file names where every pairwise
        elemets have a distance > degree
        '''
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

    def setupdst(s):
        dst = s.dst
        if '~' in dst:
            dst = os.path.exapnduser(dst)
        dst = dst.replace('\\' , '/')
        if not os.path.isdir(dst):
            os.mkdir(dst)

    def copier(s):
        s.setupdst()
        cp = shutil.copy
        for sng in s.done:
            print(f'cp {sng}')
            cp(s.src+'/'+sng,s.dst+'/'+sng)
            

