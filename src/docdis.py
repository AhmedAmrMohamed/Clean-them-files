import re
import math as ma
class Docdis:
    def __init__(se,*,debug = False):
        se.setDebug(debug)
        se.puncs = ['.','&','-','_','$',',']
    def __call__(se,doc1,doc2,*,debug = False):
        v1 = se.getvec(se.fixword(doc1))
        v2 = se.getvec(se.fixword(doc2))
        if debug:
            se.setDebug(True)
        if se.debug:
            print(v1,v2,end = "\n")
        try:
            return se.dist(v1,v2)
        except Exception as e:
            print('doc1',doc1)
            print('doc2',doc2)
            print(e)
    
    def fixword(se,doc):
        doc = doc.split('.')
        doc.pop()
        doc = '.'.join(doc)
        for pun in se.puncs:
            doc = doc.replace(pun,' ')
        return doc.split()
        

    def setDebug(se,flag):
        se.debug = flag

    def getvec(se,doc):
        vec = {}
        for word in doc:
            vec[word] = vec.get(word,0)+1
        return vec

    def getmag(se,vec):
        ret = 0
        for word in vec:
            ret+=vec[word]**2
        return ret**0.5

    def innerproduct(se,vec1,vec2):
        product = 0
        for word in vec1:
            product += vec1[word] * vec2.get(word,0)
        return product

    def dist(se,v1,v2):
        # try:
            ip = se.innerproduct
            gm = se.getmag
            return ma.acos(ip(v1,v2)/round((gm(v1))*gm(v2),8))
        # except Exception as exc:
            # print(exc)
            # print(v1)
            # print(v2)
            # print('ip',ip(v1,v2))
            # print('g1',gm(v1))
            # print('g2',gm(v2))
            # print('bo',gm(v1)*gm(v2))
  





# def getvecr(se,doc):
        # '''not in use for now'''
        # vec    = {}
        # reader = open(doc,'r')
        # reader = reader.read().split()
        # reader = list(map(se.fixword,reader))
        # for word in reader:
            # vec[word] = vec.get(word,0)+1
        # return vec


