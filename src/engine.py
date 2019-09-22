from docdis import Docdis
import os
import math

class Engine:
    def __init__(s,src,*,dst=None,deg = 0.7):
        s.distance = Docdis()
        s.src = src
        s.done = set()
        s.lis = []
        s.deg = max(min(math.pi/2,s.deg),0)
        s.tester()

    def builddate(s):
        # logger = open('log.csv','w')
        files = os.listdir(s.src)
        for trgt in files:
            for comp in files:
                if (comp,trgt) in s.done or comp == trgt:
                    continue
                s.done.add((comp,trgt))
                # print(comp,trgt)
                # print(trgt,comp)
                res = s.distance(trgt,comp)
                s.lis.append((trgt,comp,res))
                # print(f'{trgt},{comp},{res}',file = logger)
        logger.close()
        return s.lis
        




