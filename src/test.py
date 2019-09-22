import engine
path = '/media/theunderdog/cheking for bad stuff part2/Music/Shazam -  World Top 100 08.05. (2018)'
# path = '/media/theunderdog/cheking for bad stuff part2/Music/lovely'
en = engine.Engine(path)
li = sorted(en.lis,key = lambda x:x[2])
for i in li:
    if i[2] < 1:
        print(i)
# from docdis import Docdis
# dis = Docdis()
# x=dis('001 Ahmed Amr', '002 Ahmed Amr Mohamed')
# print(x)
