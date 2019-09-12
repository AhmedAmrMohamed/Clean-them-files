import params
import wordDistance 
import os

class Engine:
    def __init__(s,src,dst=None):
        s.distance = wordDistance.Distance(params.costs)
        s.src = src
        s.done = set()
        s.tester()
    def tester(s):
        logger = open('log.csv','w')
        files = os.listdir(s.src)
        for trgt in files:
            for comp in files:
                if (comp,trgt) in s.done:
                    continue
                s.done.add((comp,trgt))
                # print(trgt,comp)
                res = s.distance(trgt,comp)
                print(f'{trgt},{comp},{res}',file = logger)
        logger.close()
        




