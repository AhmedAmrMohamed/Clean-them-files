def main():
    import engine
    import argparse
    import os
    '''start of help msgs'''
    helpsrc    = 'path to the src directory'
    helpdst    = 'path to the dst directory'
    helpdeg    = 'the degree of maximum simllarity allowed 0 <= degree <= pi/2 deafult 0.7'
    '''end of help msgs'''

    parser = argparse.ArgumentParser(prog = 'nameless for now i guess')
    parser.add_argument('-s','--source')
    parser.add_argument('-d','--destination')
    parser.add_argument('-g','--degree',default = 0.7)
    args = parser.parse_args()
    engine.Engine(args.source,args.destination,args.degree)
