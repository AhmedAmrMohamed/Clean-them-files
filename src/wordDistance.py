import params

class Distance():
    def __init__(s,costs):
        s.costs = costs
    def __call__(s,fir,sec,costs = None):
        s.fir   = fir
        s.sec   = sec
        s.costs = costs if costs else s.costs
        s.mem = {}
        s.res = s.solve()
        # print('res = ',s.res)
        return s.res

    def solve(s,firp=0,secp=0,ccost=0):
        sol = s.mem.get((firp,secp,ccost),None)
        if sol:
            return sol
        sol = s.costs['inf']
        # print(firp,s.fir[:firp],secp,s.sec[:secp],ccost)
        if firp == len(s.fir) and secp == len(s.sec):
            return ccost
        if firp < len(s.fir) and secp < len(s.sec):
            if s.fir[firp] == s.sec[secp]:
                sol = s.solve(firp+1,secp+1,ccost)
        if firp+1 <= len(s.fir):
            sol = min(sol,s.solve(firp+1,secp  ,ccost+s.costs['insert']))
        if secp+1 <= len(s.sec):
            sol = min(sol,s.solve(firp  ,secp+1,ccost+s.costs['remove']))
        s.mem[(firp,secp,ccost)] = sol
        return sol

# x=Distance('zeus','zeus ft halsey',params.costs)
# x=Distance()
# x('mohamed','ahmed',params.costs)
# print(params.costs)
