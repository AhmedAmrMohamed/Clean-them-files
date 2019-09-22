import engine
import os
# path = '/media/theunderdog/cheking for bad stuff part2/Music/Shazam -  World Top 100 08.05. (2018)'
path = '/media/theunderdog/cheking for bad stuff part2/Musicexp/dest'
en = engine.Engine(path)
do = en.done
li = set(os.listdir(path))
for x in do:
    li.remove(x)

fil = open('log.txt','w')
for i in li:
    print(i,file=fil)
fil.close()
